import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta
import re
from utils.sentiment_analysis import analyze_sentiment

def parse_relative_date(relative_str):
    current_time = datetime.now()
    if "h" in relative_str:
        hours = int(re.search(r"\d+", relative_str).group())
        return (current_time - timedelta(hours=hours)).strftime("%Y-%m-%d")
    elif "d" in relative_str:
        days = int(re.search(r"\d+", relative_str).group())
        return (current_time - timedelta(days=days)).strftime("%Y-%m-%d")
    return "Unknown Date"

def clean_source(source_text):
    if not source_text:
        return "Unknown Source"
    source_text = re.sub(r"\d+[hd]\s*on\s*", "", source_text)
    source_text = re.sub(r"\s*on MSN.*", "", source_text)
    return source_text.strip()

def fetch_news(company_name, max_articles=10):
    articles = []
    page = 1  
    max_retries = 5  

    while len(articles) < max_articles and page <= 3:
        search_url = f"https://www.bing.com/news/search?q={company_name}&first={page * 10}"
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "en-US,en;q=0.5",
        }

        for attempt in range(max_retries):
            try:
                response = requests.get(search_url, headers=headers, timeout=10)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, "html.parser")
                search_results = soup.find_all("div", class_="news-card")

                for item in search_results:
                    title_element = item.find("a", class_="title")
                    summary_element = item.find("div", class_="snippet")
                    source_element = item.find("div", class_="source")
                    date_element = item.find("time")

                    title = title_element.get_text(strip=True) if title_element else "No Title"
                    link = title_element["href"] if title_element and title_element.has_attr("href") else "No Link"
                    summary = summary_element.get_text(strip=True) if summary_element else "No Summary"
                    source_text = source_element.get_text(strip=True) if source_element else "Unknown Source"
                    source = clean_source(source_text)

                    publication_date = "Unknown Date"
                    if date_element and date_element.has_attr("datetime"):
                        publication_date = date_element["datetime"]
                    elif re.search(r"\d+[hd]", source_text):
                        publication_date = parse_relative_date(source_text)

                    if link.startswith("/news"):
                        link = "https://www.bing.com" + link

                    if "bing.com/news/search" in link:
                        continue  

                    articles.append({
                        "title": title, 
                        "summary": summary, 
                        "url": link,
                        "source": source,
                        "publication_date": publication_date,
                        "sentiment": analyze_sentiment(summary)
                    })

                    if len(articles) >= max_articles:
                        return articles  

                page += 1  
                time.sleep(3)  
                break  

            except requests.exceptions.RequestException as e:
                print(f"Retry {attempt+1}/{max_retries}: Connection failed. Error: {e}")
                time.sleep(5)  

        else:
            print("Max retries reached. Moving to the next page.")

    return articles  

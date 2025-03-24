import os
import pandas as pd
from utils.news_scraper import fetch_news
from utils.sentiment_analysis import analyze_sentiment
from utils.comparative_analysis import analyze_sentiment_distribution  
from utils.tts_generator import generate_hindi_speech

print("Script is running...")

# Define the company to search for
company = "Tesla"

# Fetch news articles
news_articles = fetch_news(company)

# Create output directory
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists

if not news_articles:
    print("No news articles found. Check Bing HTML structure.")
else:
    # Convert the list of articles into a DataFrame
    df = pd.DataFrame(news_articles)

    # Save the DataFrame to a CSV file inside output/
    csv_filename = os.path.join(output_dir, f"{company}_news_articles.csv")
    df.to_csv(csv_filename, index=False)
    print(f"News articles saved to {csv_filename}")

    # Compute sentiment distribution using `comparative_analysis.py`
    sentiment_distribution = analyze_sentiment_distribution(csv_filename) 
    print(f"🔹 Sentiment Distribution: {sentiment_distribution}")

    # Sentiment summary text
    sentiment_summary = (
        f"समाचार रिपोर्टिंग का विश्लेषण:\n"
        f"सकारात्मक लेख: {sentiment_distribution.get('Positive', 0)}\n"
        f"नकारात्मक लेख: {sentiment_distribution.get('Negative', 0)}\n"
        f"तटस्थ लेख: {sentiment_distribution.get('Neutral', 0)}"
    )

    # Save the speech output inside output/
    speech_filename = os.path.join(output_dir, "sentiment_summary.mp3")
    generate_hindi_speech(sentiment_summary, speech_filename)
    print(f"Speech saved as {speech_filename}")

## **📰 News Summarization and Sentiment-Based Text-to-Speech Application**

### **🔹 Project Overview**
This is a **web-based application** that extracts key insights from multiple news articles related to a given company, performs **sentiment analysis**, conducts a **comparative analysis**, and generates a **Hindi text-to-speech (TTS) output** summarizing the sentiment trends.  

Users can enter a **company name** and receive:

✅ Extracted news titles, summaries, and metadata  
✅ **Sentiment classification** (Positive, Negative, Neutral)  
✅ **Comparative sentiment analysis** across multiple articles  
✅ **Hindi audio summary** of the sentiment report  

---

## **🔹 Features & Workflow**
1️⃣ **News Extraction**: Fetches at least **10 relevant news articles** related to the given company using **NewsAPI**.  
2️⃣ **Sentiment Analysis**: Classifies each article as **Positive, Negative, or Neutral** using **VADER sentiment analysis**.  
3️⃣ **Comparative Analysis**: Provides an overview of how different articles portray the company.  
4️⃣ **Text-to-Speech (TTS) in Hindi**: Converts the final sentiment summary to **Hindi speech** using **gTTS (Google Text-to-Speech)**.  
5️⃣ **User Interface**: Interactive **web-based UI using Streamlit**.  
6️⃣ **Deployment**: Hosted on **Hugging Face Spaces** for easy access.  

---

## **🔹 Project Setup & Installation**
### **📌 Prerequisites**
- **Python 3.10+** installed  
- **Virtual Environment (venv) setup**  

### **📌 Clone the Repository**
```sh
git clone <https://github.com/Nikita-NA/News-Sentiment-App.git>
cd News-Sentiment-App
```

### **📌 Create & Activate Virtual Environment**
```sh
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### **📌 Install Dependencies**
```sh
pip install -r requirements.txt
```

### **📌 Run the Application**
```sh
python -m utils.api (in 1st terminal)
streamlit run app.py (in 2nd terminal)
```

---

## **🔹 API Endpoints**
| **Endpoint**         | **Method** | **Description** |
|----------------------|------------|----------------|
| `/fetch_news`       | `GET`       | Fetches news articles from **NewsAPI** |
| `/analyze_sentiment` | `POST`      | Performs sentiment analysis using **VADER** |
| `/generate_tts`      | `POST`      | Converts sentiment summary to **Hindi speech** using **gTTS** |

---

## **🔹 Folder Structure**
```
news-summarization-app
│── venv/               # Virtual environment
│── data/               # Stores raw & processed news data
│── static/             # Static assets (if needed)
│── templates/          # Frontend templates (Streamlit)
│── requirements.txt    # Dependencies list
│── app.py              # Main script to run the app
│── news_scraper.py     # News extraction logic
│── sentiment_analysis.py  # Sentiment analysis functions
│── tts_generator.py    # Text-to-Speech (TTS) implementation
│── README.md           # Documentation
│── .gitignore          # Ignore unnecessary files
```

---

## **🔹 Deployment**
The project is deployed on **Hugging Face Spaces** and can be accessed at:  
🔗 **[Live Demo](<your-huggingface-spaces-link>)**

---

## **🔹 Contributors**
- **Nikita N A**

---


## **📰 News Summarization and Text-to-Speech Application**

### **🔹 Project Overview**
This is a **web-based application** that extracts key details from multiple news articles related to a given company, performs **sentiment analysis**, conducts a **comparative analysis**, and generates a **Hindi text-to-speech (TTS) output**.  

The application allows users to enter a **company name** and receive:  
✅ Extracted news titles, summaries, and metadata  
✅ **Sentiment classification** (Positive, Negative, Neutral)  
✅ **Comparative sentiment analysis** across multiple articles  
✅ **Hindi audio summary** of the sentiment report  

---

## **🔹 Features & Workflow**
1️⃣ **News Extraction**: Scrapes at least **10 unique news articles** related to the given company using **BeautifulSoup (bs4)**.  
2️⃣ **Sentiment Analysis**: Classifies each article as **Positive, Negative, or Neutral**.  
3️⃣ **Comparative Analysis**: Highlights **how different articles portray the company**.  
4️⃣ **Text-to-Speech (TTS) in Hindi**: Converts the final sentiment summary to **Hindi speech** using an **open-source TTS model**.  
5️⃣ **User Interface**: Simple **web-based UI using Streamlit or Gradio**.  
6️⃣ **API-based Architecture**: Communication between the frontend and backend happens via APIs.  
7️⃣ **Deployment**: The app is deployed on **Hugging Face Spaces**.  

---

## **🔹 Project Setup & Installation**
### **📌 Prerequisites**
- **Python 3.13+** installed  
- **Virtual Environment (venv)** setup  

### **📌 Clone the Repository**
```sh
git clone <your-github-repo-link>
cd assignment_project
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
python app.py
```

---

## **🔹 API Endpoints**
| **Endpoint**         | **Method** | **Description** |
|----------------------|------------|----------------|
| `/fetch_news`       | `GET`       | Scrape news articles |
| `/analyze_sentiment` | `POST`      | Perform sentiment analysis |
| `/generate_tts`      | `POST`      | Convert summary to Hindi speech |

---

## **🔹 Folder Structure**
```
ASSIGNMENT TO SUBMIT
│── assignment_project
│   ├── venv/               # Virtual environment
│   ├── data/               # Stores raw & processed data
│   ├── models/             # Pretrained models (if needed)
│   ├── static/             # Static files (if needed)
│   ├── templates/          # Frontend templates (Gradio)
│   ├── requirements.txt    # Dependencies list
│   ├── app.py              # Main script to run the app
│   ├── api.py              # API endpoints
│   ├── utils.py            # Helper functions (scraping, sentiment analysis, TTS)
│   ├── README.md           # Documentation
│   ├── .gitignore          # Ignore unnecessary files
```

---

## **🔹 Deployment**
The project will be deployed on **Hugging Face Spaces**.  

---

## **🔹 TODO / Next Steps**
✅ Implement **news extraction** (Step 2)  
✅ Implement **sentiment analysis** (Step 3)  
✅ Implement **comparative analysis** (Step 4)  
✅ Integrate **text-to-speech (Hindi)** (Step 5)  
✅ Build **frontend (Streamlit/Gradio)** (Step 6)  
✅ Deploy on **Hugging Face Spaces** (Step 7)  

---

## **🔹 Contributors**
- **Nikita N A** (Assignment Submission)  

---
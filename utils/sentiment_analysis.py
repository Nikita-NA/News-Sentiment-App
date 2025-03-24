import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob

nltk.download('stopwords')
nltk.download('punkt')

def clean_text(text):
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)

def analyze_sentiment(text):
    if not text:
        return "Neutral"
    
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

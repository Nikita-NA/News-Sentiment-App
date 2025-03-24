from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import pandas as pd
from werkzeug.utils import secure_filename

# ✅ Import Utility Functions with Safe Handling
try:
    from utils.news_scraper import fetch_news
    from utils.sentiment_analysis import analyze_sentiment
    from utils.tts_generator import generate_hindi_speech
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    fetch_news, analyze_sentiment, generate_hindi_speech = None, None, None

# ✅ Initialize Flask App
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# ✅ Ensure Output Directory Exists
OUTPUT_DIR = os.path.abspath("output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ✅ Root Route (Avoids 404 Errors)
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API is working! Use /fetch_news, /analyze_sentiment, or /generate_tts"
    }), 200

# ✅ Fetch News Route
@app.route("/fetch_news", methods=["GET"])
def get_news():
    """Fetches news articles based on the company name."""
    if fetch_news is None:
        return jsonify({"error": "fetch_news function not found"}), 500

    company = request.args.get("company")
    if not company:
        return jsonify({"error": "Company name is required"}), 400

    news_articles = fetch_news(company)
    if not news_articles:
        return jsonify({"error": f"No news articles found for '{company}'"}), 404

    # ✅ Save to CSV securely
    csv_filename = os.path.join(OUTPUT_DIR, secure_filename(f"{company}_news.csv"))
    pd.DataFrame(news_articles).to_csv(csv_filename, index=False)

    return jsonify({
        "message": "News fetched successfully",
        "articles": news_articles,
        "csv_file": csv_filename
    })

# ✅ Sentiment Analysis Route
@app.route("/analyze_sentiment", methods=["POST"])
def sentiment_analysis():
    """Analyzes sentiment of text, fetched news articles, or from a CSV file."""
    if analyze_sentiment is None:
        return jsonify({"error": "analyze_sentiment function not found"}), 500

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input format. Expected a JSON request body."}), 400

    # ✅ Case 1: Sentiment analysis for a single text input
    if "text" in data:
        sentiment = analyze_sentiment(data["text"])
        return jsonify({
            "message": "Sentiment analysis completed",
            "text": data["text"],
            "sentiment": sentiment
        })

    # ✅ Case 2: Sentiment analysis for multiple articles
    if "articles" in data:
        if not isinstance(data["articles"], list):
            return jsonify({"error": "'articles' should be a list of dictionaries."}), 400
        
        for article in data["articles"]:
            if isinstance(article, dict):
                article["sentiment"] = analyze_sentiment(article.get("summary", ""))
            else:
                return jsonify({"error": "Invalid article format. Expected a dictionary."}), 400

        return jsonify({
            "message": "Sentiment analysis completed",
            "articles": data["articles"]
        })

    # ✅ Case 3: Sentiment analysis from a CSV file
    if "csv_path" in data:
        csv_path = data["csv_path"]

        # Ensure file exists
        if not os.path.isfile(csv_path):
            return jsonify({"error": f"File not found: {csv_path}"}), 404

        try:
            df = pd.read_csv(csv_path)
            if "summary" not in df.columns:
                return jsonify({"error": "CSV must contain a 'summary' column"}), 400

            # Apply sentiment analysis
            df["sentiment"] = df["summary"].apply(analyze_sentiment)

            # Save updated CSV
            output_csv = csv_path.replace(".csv", "_with_sentiment.csv")
            df.to_csv(output_csv, index=False)

            return jsonify({
                "message": "Sentiment analysis completed for CSV",
                "output_csv": output_csv
            })

        except Exception as e:
            return jsonify({"error": f"Failed to process CSV: {str(e)}"}), 500

    return jsonify({
        "error": "Invalid input format. Expected 'text', 'articles', or 'csv_path' key.",
        "received_data": data
    }), 400

# ✅ Text-to-Speech (TTS) Route
@app.route("/generate_tts", methods=["POST"])
def generate_tts():
    """Generates Hindi speech from sentiment summary and returns the MP3 file."""
    if generate_hindi_speech is None:
        return jsonify({"error": "generate_hindi_speech function not found"}), 500

    data = request.get_json()
    if not data or "summary" not in data:
        return jsonify({"error": "No summary provided"}), 400

    # ✅ Fix File Path Issue
    speech_filename = os.path.join(OUTPUT_DIR, "sentiment_summary.mp3")

    # ✅ Generate speech file
    success = generate_hindi_speech(data["summary"], speech_filename)

    # ✅ Ensure file was created
    if not success or not os.path.isfile(speech_filename):
        return jsonify({"error": "Failed to generate audio file"}), 500

    # ✅ Return the MP3 file securely
    return send_file(speech_filename, as_attachment=True)

# ✅ Run Flask App
if __name__ == "__main__":
    app.run(debug=True)

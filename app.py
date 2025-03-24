import os
import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Backend API URL
API_BASE_URL = "http://127.0.0.1:5000"

# Set Page Title
st.set_page_config(page_title="News Sentiment Analysis", page_icon="📰")

# Initialize Session State
if "news_fetched" not in st.session_state:
    st.session_state.news_fetched = False
if "audio_file" not in st.session_state:
    st.session_state.audio_file = None

# App Header
st.title("📢 News Sentiment Analysis App")
st.write("🔍 Fetch news articles, analyze sentiment, and listen to insights in **Hindi**.")

# User Input: Company Name
company = st.text_input("Enter company name", "")

# Button to Fetch News
if st.button("🚀 Fetch News"):
    st.session_state.news_fetched = False
    st.session_state.audio_file = None  # Reset previous audio
    st.write(f"🔄 Fetching news for **{company}**...")

    # 🔹 Call Backend API to Fetch News
    response = requests.get(f"{API_BASE_URL}/fetch_news", params={"company": company})
    
    if response.status_code == 200:
        news_data = response.json()
        news_articles = news_data.get("articles", [])

        if not news_articles:
            st.error("❌ No news articles found. Try another company.")
        else:
            # Convert to DataFrame
            df = pd.DataFrame(news_articles)

            # Display News Articles
            st.subheader("📰 Fetched News Articles")
            for idx, row in df.iterrows():
                with st.expander(f"**{idx+1}. {row['title']}**"):
                    st.write(f"**Summary:** {row['summary']}")
                    st.write(f"**Source:** {row['source']}")
                    st.write(f"**Date:** {row['publication_date']}")
                    st.write(f"**Sentiment:** `{row['sentiment']}`")
                    st.markdown(f"[🔗 Read More]({row['url']})")

            # 🔹 Call API for Sentiment Analysis
            sentiment_response = requests.post(f"{API_BASE_URL}/analyze_sentiment", json={"articles": news_articles})

            if sentiment_response.status_code == 200:
                sentiment_result = sentiment_response.json()
                sentiment_counts = {}
                for article in sentiment_result["articles"]:
                    sentiment = article["sentiment"]
                    sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1

                # Sentiment Summary
                sentiment_summary = (
                    f"समाचार रिपोर्टिंग का विश्लेषण:\n"
                    f"✅ सकारात्मक लेख: {sentiment_counts.get('Positive', 0)}\n"
                    f"❌ नकारात्मक लेख: {sentiment_counts.get('Negative', 0)}\n"
                    f"⚪ तटस्थ लेख: {sentiment_counts.get('Neutral', 0)}"
                )

                st.subheader("📊 Sentiment Analysis Summary")
                st.text(sentiment_summary)

                # Visualization - Sentiment Distribution
                st.subheader("📈 Sentiment Distribution Chart")
                fig, ax = plt.subplots()
                ax.bar(sentiment_counts.keys(), sentiment_counts.values(), color=["green", "red", "gray"])
                ax.set_ylabel("Number of Articles")
                ax.set_title("Sentiment Analysis Results")
                st.pyplot(fig)

                # Store for TTS
                st.session_state.news_fetched = True
                st.session_state.sentiment_summary = sentiment_summary
            else:
                st.error("⚠️ Error in sentiment analysis!")

    else:
        st.error("⚠️ Error fetching news!")

# **Audio Section - Generate and Play Only If News is Fetched**
if st.session_state.news_fetched:
    st.subheader("🔊 Listen to Summary in Hindi")

    # **Generate Audio Button**
    if st.button("▶️ Generate & Play Summary Audio", key="generate_audio"):
        tts_response = requests.post(f"{API_BASE_URL}/generate_tts", json={"summary": st.session_state.sentiment_summary})

        if tts_response.status_code == 200:
            with open("output/sentiment_summary.mp3", "wb") as f:
                f.write(tts_response.content)  # Save the received file locally

            st.session_state.audio_file = "output/sentiment_summary.mp3"

    # **Show Audio Player & Download Button Only If Audio Exists**
    if st.session_state.audio_file:
        st.audio(st.session_state.audio_file, format="audio/mp3")

        # **Download Button**
        with open(st.session_state.audio_file, "rb") as audio_file:
            st.download_button(
                label="⬇️ Download Summary Audio",
                data=audio_file,
                file_name="sentiment_summary.mp3",
                mime="audio/mp3",
                key="download_audio"
            )

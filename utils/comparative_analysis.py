import pandas as pd

def analyze_sentiment_distribution(csv_filename):
    """
    Computes sentiment distribution from the saved news articles CSV file.

    Parameters:
        csv_filename (str): The path to the CSV file containing news articles with sentiment labels.

    Returns:
        dict: A dictionary containing the count of Positive, Negative, and Neutral articles.
    """
    try:
        df = pd.read_csv(csv_filename)
        if "sentiment" not in df.columns:
            raise ValueError("The CSV file does not contain a 'sentiment' column.")
        sentiment_counts = df["sentiment"].value_counts().to_dict()
        return sentiment_counts
    except Exception as e:
        print(f"Error analyzing sentiment distribution: {e}")
        return {}

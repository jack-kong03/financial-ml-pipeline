from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize once
sid = SentimentIntensityAnalyzer()

def get_sentiment_score(text: str) -> float:
    """
    Returns a sentiment score between -1 (negative) and +1 (positive)
    """
    return sid.polarity_scores(text)['compound']
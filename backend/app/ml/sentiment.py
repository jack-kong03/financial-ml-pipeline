from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize once
sid = SentimentIntensityAnalyzer()

def get_sentiment_score(text: str) -> float:
    """
    Returns a sentiment score between -1 (negative) and +1 (positive)
    """
    return sid.polarity_scores(text)['compound']

def get_sentiment_label(text: str) -> str:
    """
    Returns 'Positive', 'Neutral', or 'Negative' based on VADER compound score
    """
    score = get_sentiment_score(text)
    if score >= 0.05:
        return "Positive"
        
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def get_sentiment_color(text: str) -> str:
    """
    Returns a color string based on the sentiment label.
    Positive -> green, Neutral -> gray, Negative -> red
    """
    label = get_sentiment_label(text)
    if label == "Positive":
        return "green"
    elif label == "Neutral":
        return "gray"
    elif label == "Negative":
        return "red"
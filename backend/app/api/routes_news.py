from fastapi import APIRouter, Query
import requests
import os
from app.ml.sentiment import get_sentiment_label

router = APIRouter(prefix="/api/news", tags=["News"])

symbol_map = {
    "AAPL": "Apple",
    "GOOGL": "Google",
    "MSFT": "Microsoft",
    "NVDA": "NVIDIA",
    "AMZN": "Amazon",
    "TSLA": "Tesla",
    "META": "Meta Platforms",
    "BTC-USD": "Bitcoin",
    "ETH-USD": "Ethereum",
    "SOL-USD": "Solana",
    "GC=F": "Gold",
    "^GSPC": "S&P 500",
    "^NDX": "Nasdaq 100"
}

@router.get("/")
def get_financial_news(symbols: str = Query(",".join(symbol_map.keys()))):
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return {"error": "NEWS_API_KEY not set in environment"}

    symbol_list = [s.strip() for s in symbols.split(",")]
    query_terms = " OR ".join([symbol_map.get(s, s) for s in symbol_list])
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query_terms}&language=en&sortBy=publishedAt&pageSize=10&apiKey={api_key}"
    )

    response = requests.get(url)
    if response.status_code != 200:
        return {"error": f"NewsAPI request failed: {response.status_code}"}

    data = response.json()
    articles = data.get("articles", [])

    results = []
    for article in articles:
        text = f"{article.get('title','')} {article.get('description','')}"
        sentiment_label = get_sentiment_label(text)
        results.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url"),
            "source": article.get("source", {}).get("name"),
            "publishedAt": article.get("publishedAt"),
            "sentiment": sentiment_label   # now returns 'Positive', 'Neutral', or 'Negative'
        })
    return results
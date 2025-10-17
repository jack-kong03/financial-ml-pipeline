from fastapi import APIRouter, Query
import requests
import os

router = APIRouter(prefix="/api/news", tags=["News"])

@router.get("/")
def get_financial_news(query: str = Query("stocks")):
    """
    Fetch latest financial or crypto news using NewsAPI.
    Example: /api/news?query=crypto
    """
    api_key = os.getenv("NEWS_API_KEY")
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&language=en&sortBy=publishedAt&pageSize=5&apiKey={api_key}"
    )

    response = requests.get(url)
    if response.status_code != 200:
        return {"error": f"NewsAPI request failed: {response.status_code}"}

    data = response.json()
    articles = data.get("articles", [])

    results = []
    for article in articles:
        results.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url"),
            "source": article.get("source", {}).get("name"),
            "publishedAt": article.get("publishedAt"),
        })

    return results
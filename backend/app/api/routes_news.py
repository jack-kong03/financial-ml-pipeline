from fastapi import APIRouter, Query
import requests
import os

router = APIRouter(prefix="/api/news", tags=["News"])

@router.get("/")
def get_financial_news(symbols: str = Query("AAPL,GOOGL,MSFT,NVDA,AMZN,TSLA,META,BTC,ETH,SOL,XRP,GC=F,^GSPC,^NDX")):
    """
    Fetch latest financial or crypto news using NewsAPI.
    Example: /api/news?symbols=AAPL,BTC
    """
    symbol_map = {
        "AAPL": "Apple",
        "GOOGL": "Alphabet",
        "MSFT": "Microsoft",
        "NVDA": "NVIDIA",
        "AMZN": "Amazon",
        "TSLA": "Tesla",
        "META": "Meta",
        "BTC": "Bitcoin",
        "ETH": "Ethereum",
        "SOL": "Solana",
        "XRP": "Ripple",
        "GC=F": "Gold",
        "^GSPC": "S&P 500",
        "^NDX": "Nasdaq 100"
    }

    symbol_list = [s.strip().upper() for s in symbols.split(",")]
    query_terms = [symbol_map.get(sym, sym) for sym in symbol_list]
    query = " OR ".join(query_terms)

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
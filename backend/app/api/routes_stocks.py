from fastapi import APIRouter, Query
import yfinance as yf

router = APIRouter(prefix="/api/stocks", tags=["Stocks"])

@router.get("/")
def get_multiple_stocks(symbols: str = Query("AAPL,GOOGL,MSFT,NVDA,AMZN,TSLA,META,GC=F,^GSPC,^NDX")):
    """
    Fetch multiple stocks at once using Yahoo Finance.
    Use query parameter 'symbols' as a comma-separated list, e.g. ?symbols=AAPL,TSLA,AMZN
    """
    symbol_list = [s.strip().upper() for s in symbols.split(",")]
    results = []

    for symbol in symbol_list:
        try:
            stock = yf.Ticker(symbol)
            info = stock.info

        # Try to get price directly; if missing, use the latest closing price
            price = info.get("currentPrice")
            if not price or price == 0:
                hist = stock.history(period="1d")
                if not hist.empty:
                    price = hist["Close"].iloc[-1]
                else:
                    price = 0

            results.append({
                "symbol": symbol,
                "name": info.get("shortName", "Unknown"),
                "sector": info.get("sector", "Unknown"),
                "price": round(price, 2),
                "change": round(info.get("regularMarketChangePercent", 0), 2),
                "volume": info.get("volume", 0)
           })
        except Exception as e:
            results.append({
                "symbol": symbol,
                "error": str(e)

           })

    return results
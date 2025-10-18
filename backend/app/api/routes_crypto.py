from fastapi import APIRouter, Query
import yfinance as yf

router = APIRouter(prefix="/api/crypto", tags=["Crypto"])

@router.get("/")
def get_multiple_crypto(symbols: str = Query("BTC-USD,ETH-USD,SOL-USD,XRP-USD")):
    """
    Fetch multiple cryptocurrencies using Yahoo Finance.
    Uses fallback to .history() for current price when .info is incomplete.
    """
    symbol_list = [s.strip().upper() for s in symbols.split(",")]
    results = []

    for symbol in symbol_list:
        try:
            crypto = yf.Ticker(symbol)
            info = crypto.info

            # Try to get price from info; if missing, use history fallback
            price = info.get("currentPrice")
            if not price or price == 0:
                hist = crypto.history(period="1d")
                if not hist.empty:
                    price = hist["Close"].iloc[-1]
                else:
                    price = 0

            results.append({
                "symbol": symbol,
                "name": info.get("shortName", "Unknown"),
                "price": round(price, 2),
                "change": round(info.get("regularMarketChangePercent", 0), 2),
                "volume": info.get("volume24Hr", info.get("volume", 0))
            })
        except Exception as e:
            results.append({
                "symbol": symbol,
                "error": str(e)
            })

    return results
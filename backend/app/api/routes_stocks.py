from fastapi import APIRouter

router = APIRouter(prefix="/api/stocks", tags=["Stocks"])

@router.get("/")
def get_stock_data():
    # Placeholder data — will be replaced with live API calls later
    return {
        "symbol": "AAPL",
        "price": 192.47,
        "change": "+1.35%",
        "volume": 54000000
    }
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_stocks, routes_crypto, routes_news
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Financial ML Pipeline Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_stocks.router)
app.include_router(routes_crypto.router)
app.include_router(routes_news.router)

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}
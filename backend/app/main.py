from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_stocks

app = FastAPI(title="Financial ML Pipeline Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_stocks.router)

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}
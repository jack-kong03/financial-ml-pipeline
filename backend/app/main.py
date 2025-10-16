from fastapi import FastAPI

app = FastAPI(title="Financial ML Pipeline Backend")

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}
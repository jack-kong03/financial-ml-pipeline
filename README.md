# 🧠 Financial-ML-Pipeline
> **End-to-end AI system for financial data ingestion, sentiment analysis, and predictive modeling — built entirely with free APIs and open-source tools.**

---

## 📘 Overview
`Financial-ML-Pipeline` is a modular, research-grade project that automates the full lifecycle of financial insight generation.  
It combines **stock**, **crypto**, and **news** data with **machine learning** and **NLP-based sentiment analysis** to deliver real-time, data-driven predictions and analytics — all using **100% free tiers**.

The goal is to provide developers and data scientists with a reproducible environment for experimenting with:
- Financial data pipelines  
- Natural Language Processing (NLP) for market sentiment  
- Time-series modeling and forecasting  
- Interactive dashboards for analysis and insight delivery  

---

## ⚙️ Key Features
- 📈 **Multi-asset data ingestion** (stocks & crypto) via free public APIs  
- 🧾 **News and sentiment extraction** using transformer models (FinBERT)  
- 🤖 **Machine Learning predictions** for short-term price movement  
- 🔄 **Automated data pipelines** and retraining jobs (via GitHub Actions)  
- 📊 **Interactive web dashboard** (Next.js + Recharts + TailwindCSS)  
- 🐳 **Containerized environment** for easy setup and deployment  
- ☁️ **Free hosting-ready** (Vercel + Render / Railway)  

---

## 🧩 System Architecture
    ┌────────────────────────────┐
    │   Frontend (Next.js)       │
    │  • Dashboard & Charts      │
    │  • Realtime Insights       │
    └────────────┬───────────────┘
                 │ REST API (FastAPI)
    ┌────────────┴───────────────┐
    │      Backend Services      │
    │  • Data ingestion (Yahoo,  │
    │    CoinGecko, News APIs)   │
    │  • Sentiment Analysis (AI) │
    │  • ML Prediction Engine    │
    └────────────┬───────────────┘
                 │
    ┌────────────┴───────────────┐
    │      Data Layer             │
    │  • SQLite / Supabase DB     │
    │  • Feature Store (Pandas)   │
    │  • Model Artifacts (.pkl)   │
    └────────────────────────────┘
    ---

## 🧠 How It Works
1. **Data Ingestion**
   - Fetches latest **stock prices** via Yahoo Finance (`yfinance`)
   - Retrieves **crypto data** from CoinGecko API
   - Collects **financial news** headlines via NewsData or GNews API  

2. **Pre-processing**
   - Cleans, aligns, and merges time-series data  
   - Extracts technical indicators (SMA, RSI, volatility)  
   - Maps news articles to related tickers  

3. **Sentiment Analysis**
   - Uses **FinBERT** (Hugging Face) for finance-specific sentiment classification  
   - Outputs a numerical sentiment score per headline  

4. **Feature Engineering**
   - Combines market and sentiment signals  
   - Generates a feature matrix for model training  

5. **Machine Learning**
   - Trains an **XGBoost** classifier (or other ML models) to predict short-term movement  
   - Performs walk-forward validation for time-series evaluation  

6. **API & Dashboard**
   - Serves predictions and metrics through a **FastAPI** backend  
   - Visualizes live charts, indicators, and AI predictions via **Next.js dashboard**  

7. **Automation**
   - **GitHub Actions** scheduled workflows automatically fetch data and retrain models  
   - Updates deployed backend/frontend with new model weights  

---

## 🧰 Tech Stack

| Category | Tools / Libraries |
|-----------|------------------|
| 🐍 **Backend** | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) |
| 🤖 **Machine Learning / NLP** | ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white) ![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?logo=xgboost&logoColor=white) ![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?logo=huggingface&logoColor=black) |
| 💾 **Data & APIs** | ![YahooFinance](https://img.shields.io/badge/Yahoo_Finance-720E9E?logo=yahoo&logoColor=white) ![CoinGecko](https://img.shields.io/badge/CoinGecko-4CBB17?logo=coingecko&logoColor=white) ![NewsAPI](https://img.shields.io/badge/News_API-000000?logo=rss&logoColor=white) |
| 🌐 **Frontend** | ![Next.js](https://img.shields.io/badge/Next.js-000000?logo=nextdotjs&logoColor=white) ![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black) ![TailwindCSS](https://img.shields.io/badge/TailwindCSS-38B2AC?logo=tailwindcss&logoColor=white) ![Recharts](https://img.shields.io/badge/Recharts-8884d8?logo=recharts&logoColor=white) |
| ☁️ **Hosting / CI** | ![Vercel](https://img.shields.io/badge/Vercel-000000?logo=vercel&logoColor=white) ![Render](https://img.shields.io/badge/Render-46E3B7?logo=render&logoColor=black) ![GitHub_Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white) |
| 🗄️ **Database / Storage** | ![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white) ![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?logo=supabase&logoColor=white) |

---

## 🧪 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/jack-kong03/financial-ml-pipeline.git
cd financial-ml-pipeline

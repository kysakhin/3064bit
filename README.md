# NewsSense: AI-Powered Fund Performance Explainer

An AI-driven system that explains mutual fund/ETF performance by connecting financial data with real-world news and events. Answers questions like *"Why did my fund drop today?"* using NLP and LLMs.

## ✨ Features

- **Natural Language Explanations**: Get human-like answers (e.g., "VTI dropped due to Fed rate hike concerns" instead of just "-2%")
- **Indian Market Focus**: Supports 20+ major Indian stocks (Reliance, HDFC Bank, TCS) and 15+ mutual funds (ICICI Prudential, HDFC Floating Rate)
- **Custom News Corpus**: Scraped and processed financial news with entity linking
- **Strict Financial Guardrails**: Rejects non-financial queries
- **Responsive UI**: Next.js frontend with modern dashboard

## 🛠 Tech Stack

| Component          | Technology                          |
|--------------------|-------------------------------------|
| Frontend           | Next.js 14, Tailwind CSS, Shadcn/ui |
| Backend            | Flask (Python)                      |
| LLM                | HuggingFaceH4/zephyr-7b-beta        |
| Vector DB          | ChromaDB                            |
| Embeddings         | all-MiniLM-L6-v2                    |
| NLP Pipeline       | LangChain                           |

## TOP Stocks we support
RELIANCE,
HDFCBANK,
TCS,
BHARTIARTL,
ICICIBANK,
SBIN,
INFY,
HINDUNILVR,
BAJFINANCE,
ITC,
LICI,
LT,
KOTAKBANK,
SUNPHARMA,
HCLTECH,
MARUTI,
NTPC,
ULTRACEMCO,
AXISBANK,
M&M

## Top mutal funds we support 
ICICI Prudential Value Discovery Fund
BHARAT Bond FOF - April 2031
HDFC Floating Rate Debt Fund
Nippon India Arbitrage Fund
Kotak Nifty SDL Apr 2027 Index Fund
Parag Parikh Flexi Cap Fund
ICICI Prudential Liquid Fund
HDFC Overnight Fund
BHARAT Bond ETF FOF - April 2032
Aditya Birla Sun Life Money Manager Fund
ICICI Prudential Bluechip Fund
Aditya Birla Sun Life Savings Fund
DSP ELSS Tax Saver Fund
SBI Long Term Equity Fund
Bandhan CRISIL IBX Gilt April 2028 Index Fund


## 🚀 Quick Start

1. **Backend**:
   ```bash
   cd flask_app
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   pip install flask langchain chromadb huggingface-hub
   python app.py
   ```

2. **Frontend**:
   cd frontend
   npm install
   npm run dev

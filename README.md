# 📈 AI Stock Analyst Pro

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-green.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Advanced Professional Stock Analysis Platform powered by Groq AI + Agno Agentic Framework**

Premium production-level stock analysis platform combining real-time financial data with AI-powered insights. Features glassmorphism UI, technical analysis, multi-timeframe charting, and sophisticated AI recommendations.

---

## 🚀 Features

### Core Features
- ✅ **Real-time Stock Data** - Live prices, market cap, PE ratio, dividends
- ✅ **AI-Powered Analysis** - Groq API + Agno for intelligent stock insights
- ✅ **Interactive Charts** - Candlestick, volume, multi-timeframe (1M, 3M, 6M, 1Y)
- ✅ **Technical Indicators** - RSI, MACD, Moving Averages
- ✅ **Stock Comparison** - Side-by-side analysis of two stocks
- ✅ **Market Trends** - Top gainers, losers, trending stocks
- ✅ **Watchlist** - Save and track favorite stocks
- ✅ **Premium UI** - Glassmorphism design, dark theme, smooth animations

### AI Analysis Includes
📌 **Company Overview** - Business model and sector analysis
💰 **Valuation Metrics** - PE Ratio, Market Cap, EPS, Dividend Yield
📈 **Growth Potential** - 52-week highs/lows, growth outlook
⚠️ **Risk Assessment** - Market and company-specific risks
📰 **News Sentiment** - Latest developments and sentiment analysis
🎯 **Buy/Hold/Sell Rating** - Professional recommendations
🧠 **Long-Term View** - 5-10 year outlook
📊 **Beginner Friendly Rating** - Difficulty assessment

---

## 🛠️ Tech Stack

### Frontend
- **Streamlit** - Modern web framework for data apps
- **Plotly** - Interactive charts and visualizations

### Backend
- **Flask** - REST API server
- **yFinance** - Real-time financial data
- **Groq API** - High-speed AI inference
- **Agno** - Agentic AI framework

### Libraries
- **Pandas & NumPy** - Data processing
- **Python-dotenv** - Environment management
- **Requests** - HTTP client

---

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API Key ([Get it free here](https://console.groq.com))
- Internet connection for real-time data

---

## 🔧 Installation & Setup

### 1. Clone or Download Project
```bash
cd AI_Stock_analyst
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

**Get your Groq API Key:**
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for free
3. Create an API key
4. Copy and paste in `.env`

---

## 🚀 Running the Application

### Start Backend (Flask API)
```bash
python app.py
```
✅ Flask server starts on `http://127.0.0.1:5000`

### Start Frontend (Streamlit UI) - In a new terminal
```bash
streamlit run ui.py
```
✅ Open browser to `http://localhost:8501`

---

## 📖 Usage Guide

### 🏠 Dashboard
- View top gainers and losers
- Quick market overview
- Real-time market trends

### 🔍 Stock Analysis
- Search any stock symbol (AAPL, NVDA, GOOGL, etc.)
- View detailed AI analysis
- Check technical indicators (RSI, MACD, MA)
- Interactive candlestick charts with volume analysis

### 📊 Compare Stocks
- Select two stocks (e.g., AAPL vs GOOGL)
- Side-by-side metrics comparison
- AI-powered comparison analysis

### 📈 Charts & Trends
- Multi-timeframe charting (1M, 3M, 6M, 1Y)
- Compare two stocks on same chart
- Volume analysis
- Candlestick patterns

### ⭐ Watchlist
- Add stocks to your watchlist
- Track real-time prices and changes
- Quick deletion option

---

## 📊 API Endpoints

### Main Endpoints

#### POST `/analyze`
**Analyze a stock with AI**
```bash
curl -X POST http://127.0.0.1:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"symbol": "AAPL"}'
```
Returns: Analysis, chart data, and metrics

#### GET `/chart/<symbol>/<period>`
**Get chart data for specific period**
```bash
curl http://127.0.0.1:5000/chart/AAPL/1mo
```
Periods: `1mo`, `3mo`, `6mo`, `1y`

#### GET `/metrics/<symbol>`
**Get stock metrics**
```bash
curl http://127.0.0.1:5000/metrics/AAPL
```

#### POST `/compare`
**Compare two stocks**
```bash
curl -X POST http://127.0.0.1:5000/compare \
  -H "Content-Type: application/json" \
  -d '{"symbol1": "AAPL", "symbol2": "GOOGL"}'
```

#### GET `/trending`
**Get trending stocks**
```bash
curl http://127.0.0.1:5000/trending
```

#### GET `/gainers`
**Get top gainers**
```bash
curl http://127.0.0.1:5000/gainers
```

#### GET `/losers`
**Get top losers**
```bash
curl http://127.0.0.1:5000/losers
```

#### GET `/health`
**API health check**
```bash
curl http://127.0.0.1:5000/health
```

---

## 📁 Project Structure

```
AI_Stock_Analyst/
│
├── ui.py                 # Streamlit frontend (main entry point)
├── app.py                # Flask backend API
├── agent.py              # AI Agent & Technical Analysis
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

### File Descriptions

**ui.py** (1200+ lines)
- Premium glassmorphism UI components
- Multi-page navigation (Dashboard, Analysis, Compare, Charts, Watchlist)
- Real-time data visualization
- Responsive layout
- Interactive charts with Plotly

**app.py** (350+ lines)
- Flask REST API with CORS support
- Multiple endpoints for stock data
- Chart formatting
- Error handling
- Metrics calculation

**agent.py** (250+ lines)
- Groq AI integration
- Technical indicators (RSI, MACD, MA)
- Stock analysis function
- Stock comparison logic
- Structured AI insights

---

## 🎨 UI Features

### Design Elements
- 🌙 **Dark Theme** - Eye-friendly, professional
- ✨ **Glassmorphism** - Modern frosted glass effect
- 🌈 **Gradient Backgrounds** - Smooth color transitions
- 🎭 **Hover Animations** - Interactive elements
- 💫 **Smooth Transitions** - Professional feel
- 📱 **Responsive Layout** - Works on all devices
- 🔵 **Neon Blue + Green Theme** - Finance-focused colors
- ⚡ **Loading States** - Progress indicators

---

## 🔒 Security

- API keys stored in `.env` (never commit to git)
- CORS enabled for safe cross-origin requests
- Input validation on all endpoints
- Error handling prevents data leaks
- `.gitignore` prevents accidental commits

---

## 🎯 Example Stocks to Analyze

**Tech Giants**
- AAPL (Apple)
- MSFT (Microsoft)
- GOOGL (Google)
- AMZN (Amazon)
- NVDA (NVIDIA)

**Growth Stocks**
- TSLA (Tesla)
- META (Meta)
- NFLX (Netflix)
- PYPL (PayPal)

**Financial**
- JPM (JPMorgan)
- BAC (Bank of America)
- GS (Goldman Sachs)

**Healthcare**
- JNJ (Johnson & Johnson)
- PFE (Pfizer)
- ABBV (AbbVie)

---

## 🐛 Troubleshooting

### Issue: "Backend server not running"
**Solution:** Make sure Flask app is running:
```bash
python app.py
```

### Issue: "GROQ_API_KEY not found"
**Solution:** Create `.env` file with your API key:
```env
GROQ_API_KEY=your_key_here
```

### Issue: "Module not found"
**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Port 5000 already in use
**Solution:** Change port in `app.py`:
```python
app.run(debug=True, host="127.0.0.1", port=5001)
```

### Issue: Slow AI responses
**Solution:** Increase timeout in `ui.py`:
```python
timeout=180  # 3 minutes
```

---

## 📈 Performance Optimization

- **Caching** - 5-minute cache on API responses
- **Lazy Loading** - Charts load on demand
- **Efficient Data Fetching** - Optimized yFinance queries
- **Fast AI Inference** - Groq's LPU for speed

---

## 🌍 Deployment Options

### Local Development
```bash
streamlit run ui.py
```

### Streamlit Cloud
```bash
streamlit deploy ui.py --name ai-stock-analyst
```

### Docker (Coming Soon)
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "ui.py"]
```

---

## 📝 Notes

- ⚠️ **Not Investment Advice** - This tool is for educational purposes only
- 📊 **Historical Data** - Past performance doesn't guarantee future results
- 🔄 **Real-time Data** - Prices may have slight delays
- 🤖 **AI Predictions** - Use as reference, not definitive recommendations

---

## 🤝 Contributing

Improvements and suggestions are welcome!

1. Fork the project
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📜 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review API documentation above
3. Check Streamlit/Flask documentation
4. Open an issue with details

---

## 🎓 Learning Resources

- [Streamlit Docs](https://docs.streamlit.io)
- [Flask Documentation](https://flask.palletsprojects.com)
- [yFinance Guide](https://yfinance.readthedocs.io)
- [Groq API Docs](https://console.groq.com/docs)
- [Plotly Charts](https://plotly.com/python)

---

## 🚀 Roadmap

- [ ] PDF Report Download
- [ ] Email Alerts
- [ ] Advanced Technical Analysis
- [ ] Options Analysis
- [ ] Portfolio Optimization
- [ ] Backtesting Engine
- [ ] Mobile App
- [ ] Real-time News Feed
- [ ] Sentiment Analysis
- [ ] Machine Learning Predictions

---

## ⭐ Credits

Built with:
- **Streamlit** - Frontend framework
- **Flask** - Backend API
- **Groq** - AI inference
- **yFinance** - Financial data
- **Plotly** - Visualizations
- **Agno** - Agentic framework

---

## 📌 Version

**v1.0.0** - Professional Release
- Complete AI analysis
- Multi-page UI
- All core features
- Production-ready

---

## 🎉 Happy Investing! 

Made with ❤️ for stock analysis enthusiasts

---

**Last Updated:** April 2026
**Status:** Active Development
**Maintainer:** AI Stock Analyst Team

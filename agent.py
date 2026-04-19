# from agno.agent import Agent
# from agno.models.groq import Groq
# from agno.tools.yfinance import YFinanceTools
# from agno.tools.duckduckgo import DuckDuckGoTools
# from dotenv import load_dotenv

# load_dotenv()

# # stock_agent = Agent(
# #     model=Groq(id="qwen/qwen3-32b"),
# #     tools=[
# #         YFinanceTools(),
# #         DuckDuckGoTools()
# #     ],
# #     markdown=True,
# #     description="You are an AI Stock Analyst.",
# #     instructions=[
# #         "Use YFinance tool for stock price, analyst recommendations, and fundamentals.",
# #         "Give response in markdown format.",
# #         "Use tables where possible."
# #     ]
# # )

# # def analyze_stock(symbol):
# #     query = f"Give latest stock price, analyst recommendations, and company fundamentals for {symbol}"
# #     response = stock_agent.run(query)
# #     return response.content

# from agno.agent import Agent
# from agno.models.groq import Groq
# from agno.tools.yfinance import YFinanceTools
# from dotenv import load_dotenv

# load_dotenv()

# stock_agent = Agent(
#     model=Groq(id="qwen/qwen3-32b"),
#     tools=[YFinanceTools()],
#     markdown=True,
#     description="Professional AI Stock Analyst",
# )

# def analyze_stock(symbol):
#     query = f"""
#     Give professional stock analysis for {symbol}
#     Include:
#     - Current stock price
#     - Buy Hold Sell recommendation
#     - PE Ratio
#     - Market Cap
#     - Growth potential
#     - Short summary
#     """
    
#     response = stock_agent.run(query)
#     return response.content

"""
AI Stock Analyst Agent using Groq + Agno
Professional stock analysis with structured insights
"""

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
import yfinance as yf
from datetime import datetime, timedelta
import json

load_dotenv()

# ==========================================
# AI STOCK ANALYST AGENT
# ==========================================

stock_agent = Agent(
    name="📈 AI Stock Analyst Pro",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(), DuckDuckGoTools()],
    markdown=True,
    description="Professional Stock Analyst with Real-time Data & Market Sentiment",
    instructions=[
        "Provide comprehensive stock analysis with data-driven insights.",
        "Use YFinance for stock metrics and DuckDuckGo for recent news.",
        "Structure analysis in clear sections with markdown formatting.",
        "Include specific metrics and percentages.",
        "Provide actionable buy/hold/sell recommendations.",
        "Assess risk factors and growth potential.",
        "Format response in markdown with bullet points and tables."
    ]
)

# ==========================================
# TECHNICAL ANALYSIS FUNCTIONS
# ==========================================

def calculate_rsi(prices, period=14):
    """Calculate Relative Strength Index"""
    deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    
    gains = [d if d > 0 else 0 for d in deltas]
    losses = [-d if d < 0 else 0 for d in deltas]
    
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    
    if avg_loss == 0:
        return 100 if avg_gain > 0 else 0
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)

def calculate_macd(prices, fast=12, slow=26, signal=9):
    """Calculate MACD indicator"""
    fast_ema = prices[-fast:]
    slow_ema = prices[-slow:]
    
    fast_ma = sum(fast_ema) / len(fast_ema)
    slow_ma = sum(slow_ema) / len(slow_ema)
    
    macd_line = fast_ma - slow_ma
    return round(macd_line, 4)

def calculate_moving_average(prices, period=20):
    """Calculate Simple Moving Average"""
    if len(prices) < period:
        period = len(prices)
    ma = sum(prices[-period:]) / period
    return round(ma, 2)

# ==========================================
# MAIN ANALYSIS FUNCTION
# ==========================================

def analyze_stock(symbol):
    """Comprehensive AI stock analysis"""
    try:
        symbol = symbol.upper()
        ticker = yf.Ticker(symbol)
        
        # Fetch historical data
        hist = ticker.history(period="1y")
        info = ticker.info
        
        # Calculate technical indicators
        prices = hist['Close'].tolist()
        rsi = calculate_rsi(prices) if len(prices) > 14 else None
        macd = calculate_macd(prices) if len(prices) > 26 else None
        ma_20 = calculate_moving_average(prices, 20) if len(prices) > 20 else None
        ma_50 = calculate_moving_average(prices, 50) if len(prices) > 50 else None
        
        # Current price data
        current_price = info.get("currentPrice", info.get("regularMarketPrice", 0))
        prev_close = info.get("previousClose", 0)
        change_pct = ((current_price - prev_close) / prev_close * 100) if prev_close else 0
        
        # Get AI analysis
        query = f"""
        Provide professional stock analysis for {symbol}.
        
        Current Price: ${current_price:.2f} ({change_pct:+.2f}%)
        
        Include EXACTLY these sections:
        
        📌 COMPANY OVERVIEW
        - Business model, sector, industry
        - Recent developments
        
        💰 VALUATION METRICS
        - PE Ratio: {info.get('trailingPE', 'N/A')}
        - Market Cap: {info.get('marketCap', 'N/A')}
        - EPS: {info.get('trailingEps', 'N/A')}
        - Dividend Yield: {info.get('dividendYield', 'N/A')}
        
        📈 GROWTH & POTENTIAL
        - 52 Week High: ${info.get('fiftyTwoWeekHigh', 'N/A')}
        - 52 Week Low: ${info.get('fiftyTwoWeekLow', 'N/A')}
        - Growth outlook
        
        ⚠️ RISK FACTORS
        - Market risks
        - Industry challenges
        - Company-specific risks
        
        📰 RECENT NEWS SENTIMENT
        - Latest news and sentiment analysis
        
        🎯 RATING & RECOMMENDATION
        Provide: STRONG BUY / BUY / HOLD / SELL / STRONG SELL
        
        🧠 LONG-TERM VIEW (5-10 years)
        
        📊 BEGINNER FRIENDLY?
        Rate difficulty and explain
        
        🔥 FINAL VERDICT
        One-line recommendation with confidence score (0-100%)
        """
        
        response = stock_agent.run(query)
        analysis_text = response.content if hasattr(response, 'content') else str(response)
        
        # Add technical indicators section
        tech_analysis = "\n\n### 📊 TECHNICAL INDICATORS\n"
        if rsi is not None:
            tech_analysis += f"- **RSI (14)**: {rsi} {'(Overbought ⚠️)' if rsi > 70 else '(Oversold ✅)' if rsi < 30 else '(Neutral ➡️)'}\n"
        if ma_20 is not None:
            status = "Above" if current_price > ma_20 else "Below"
            tech_analysis += f"- **MA(20)**: ${ma_20} ({status})\n"
        if ma_50 is not None:
            status = "Above" if current_price > ma_50 else "Below"
            tech_analysis += f"- **MA(50)**: ${ma_50} ({status})\n"
        if macd is not None:
            tech_analysis += f"- **MACD**: {macd}\n"
        
        analysis_text += tech_analysis
        
        return analysis_text
    
    except Exception as e:
        return f"❌ Error analyzing {symbol}: {str(e)}"

# ==========================================
# COMPARISON FUNCTION
# ==========================================

def compare_stocks(symbol1, symbol2):
    """Compare two stocks side by side"""
    try:
        sym1 = symbol1.upper()
        sym2 = symbol2.upper()
        
        ticker1 = yf.Ticker(sym1)
        ticker2 = yf.Ticker(sym2)
        
        info1 = ticker1.info
        info2 = ticker2.info
        
        query = f"""
        Compare stocks {sym1} and {sym2}.
        
        {sym1}:
        - Price: ${info1.get('currentPrice', 'N/A')}
        - PE: {info1.get('trailingPE', 'N/A')}
        - Market Cap: {info1.get('marketCap', 'N/A')}
        
        {sym2}:
        - Price: ${info2.get('currentPrice', 'N/A')}
        - PE: {info2.get('trailingPE', 'N/A')}
        - Market Cap: {info2.get('marketCap', 'N/A')}
        
        Provide detailed comparison and which is better value.
        """
        
        response = stock_agent.run(query)
        return response.content if hasattr(response, 'content') else str(response)
    
    except Exception as e:
        return f"Error comparing stocks: {str(e)}"
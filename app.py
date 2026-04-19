# # app.py (Flask Backend)

# from flask import Flask, request, jsonify
# from agent import analyze_stock

# app = Flask(__name__)

# @app.route("/analyze", methods=["POST"])
# def analyze():
#     data = request.json
#     symbol = data.get("symbol")

#     if not symbol:
#         return jsonify({"error": "Stock symbol required"}), 400

#     result = analyze_stock(symbol)
#     return jsonify({"result": result})

# if __name__ == "__main__":
#     app.run(debug=True)


"""
Flask Backend API for AI Stock Analyst
Production-level REST API with comprehensive stock analysis endpoints
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import analyze_stock, compare_stocks
import yfinance as yf
from datetime import datetime, timedelta
import json
import os

app = Flask(__name__)
CORS(app)

# ==========================================
# HELPER FUNCTIONS
# ==========================================

def get_stock_data(symbol, period="1mo"):
    """Fetch stock data from yfinance"""
    try:
        ticker = yf.Ticker(symbol.upper())
        hist = ticker.history(period=period)
        info = ticker.info
        
        return {
            "success": True,
            "data": hist,
            "info": info
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

def format_chart_data(hist):
    """Format historical data for charts"""
    return {
        "dates": hist.index.strftime("%Y-%m-%d").tolist(),
        "open": hist["Open"].round(2).tolist(),
        "high": hist["High"].round(2).tolist(),
        "low": hist["Low"].round(2).tolist(),
        "close": hist["Close"].round(2).tolist(),
        "volume": hist["Volume"].tolist()
    }

def get_stock_metrics(symbol):
    """Get key metrics for a stock"""
    try:
        ticker = yf.Ticker(symbol.upper())
        info = ticker.info
        hist = ticker.history(period="1d")
        
        current_price = info.get("currentPrice", info.get("regularMarketPrice", 0))
        prev_close = info.get("previousClose", 0)
        change = current_price - prev_close
        change_pct = (change / prev_close * 100) if prev_close else 0
        
        metrics = {
            "symbol": symbol.upper(),
            "current_price": round(current_price, 2),
            "change": round(change, 2),
            "change_pct": round(change_pct, 2),
            "market_cap": info.get("marketCap"),
            "pe_ratio": info.get("trailingPE"),
            "eps": info.get("trailingEps"),
            "dividend_yield": info.get("dividendYield"),
            "fifty_two_week_high": round(info.get("fiftyTwoWeekHigh", 0), 2),
            "fifty_two_week_low": round(info.get("fiftyTwoWeekLow", 0), 2),
            "volume": info.get("volume"),
            "avg_volume": info.get("averageVolume"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "beta": info.get("beta")
        }
        return metrics
    except Exception as e:
        return {"error": str(e)}

# ==========================================
# API ENDPOINTS
# ==========================================

@app.route("/analyze", methods=["POST"])
def analyze():
    """Main analysis endpoint"""
    try:
        data = request.json
        symbol = data.get("symbol", "").upper()
        
        if not symbol:
            return jsonify({"error": "Stock symbol required"}), 400
        
        # Get AI analysis
        analysis = analyze_stock(symbol)
        
        # Get stock data
        stock_data = get_stock_data(symbol, "1mo")
        if not stock_data["success"]:
            return jsonify({"error": f"Failed to fetch data for {symbol}"}), 400
        
        # Format chart data
        chart = format_chart_data(stock_data["data"])
        
        # Get metrics
        metrics = get_stock_metrics(symbol)
        
        return jsonify({
            "success": True,
            "analysis": analysis,
            "chart": chart,
            "metrics": metrics
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/chart/<symbol>/<period>", methods=["GET"])
def get_chart(symbol, period="1mo"):
    """Get chart data for different time periods"""
    try:
        stock_data = get_stock_data(symbol, period)
        
        if not stock_data["success"]:
            return jsonify({"error": "Failed to fetch chart data"}), 400
        
        chart = format_chart_data(stock_data["data"])
        metrics = get_stock_metrics(symbol)
        
        return jsonify({
            "success": True,
            "chart": chart,
            "metrics": metrics
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/metrics/<symbol>", methods=["GET"])
def metrics(symbol):
    """Get stock metrics"""
    try:
        data = get_stock_metrics(symbol)
        return jsonify({"success": True, "data": data})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/compare", methods=["POST"])
def compare():
    """Compare two stocks"""
    try:
        data = request.json
        symbol1 = data.get("symbol1", "").upper()
        symbol2 = data.get("symbol2", "").upper()
        
        if not symbol1 or not symbol2:
            return jsonify({"error": "Two stock symbols required"}), 400
        
        # Get AI comparison
        comparison = compare_stocks(symbol1, symbol2)
        
        # Get metrics for both
        metrics1 = get_stock_metrics(symbol1)
        metrics2 = get_stock_metrics(symbol2)
        
        return jsonify({
            "success": True,
            "comparison": comparison,
            "stocks": {
                "stock1": metrics1,
                "stock2": metrics2
            }
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/trending", methods=["GET"])
def trending():
    """Get trending/popular stocks"""
    try:
        # Popular tech stocks
        popular_stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META", "NFLX"]
        
        trending_data = []
        for symbol in popular_stocks:
            try:
                metrics = get_stock_metrics(symbol)
                if "error" not in metrics:
                    trending_data.append(metrics)
            except:
                pass
        
        # Sort by change percentage
        trending_data.sort(key=lambda x: x.get("change_pct", 0), reverse=True)
        
        return jsonify({
            "success": True,
            "trending": trending_data[:10]
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/gainers", methods=["GET"])
def gainers():
    """Get top gainers"""
    try:
        popular_stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META", "NFLX", 
                         "PYPL", "SQUARE", "AMD", "INTC", "IBM", "DELL", "HP"]
        
        gainers_data = []
        for symbol in popular_stocks:
            try:
                metrics = get_stock_metrics(symbol)
                if "error" not in metrics:
                    gainers_data.append(metrics)
            except:
                pass
        
        # Sort by positive change
        gainers_data = [s for s in gainers_data if s.get("change_pct", 0) > 0]
        gainers_data.sort(key=lambda x: x.get("change_pct", 0), reverse=True)
        
        return jsonify({
            "success": True,
            "gainers": gainers_data[:10]
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/losers", methods=["GET"])
def losers():
    """Get top losers"""
    try:
        popular_stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META", "NFLX",
                         "PYPL", "SQUARE", "AMD", "INTC", "IBM", "DELL", "HP"]
        
        losers_data = []
        for symbol in popular_stocks:
            try:
                metrics = get_stock_metrics(symbol)
                if "error" not in metrics:
                    losers_data.append(metrics)
            except:
                pass
        
        # Sort by negative change
        losers_data = [s for s in losers_data if s.get("change_pct", 0) < 0]
        losers_data.sort(key=lambda x: x.get("change_pct", 0))
        
        return jsonify({
            "success": True,
            "losers": losers_data[:10]
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({"status": "API is running ✅"})

# ==========================================
# ERROR HANDLERS
# ==========================================

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500

# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
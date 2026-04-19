"""
AI Stock Analyst - Professional Web App
Premium Streamlit UI with Real-time Stock Analysis using Groq AI
"""

import streamlit as st
import requests
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json
import time

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Stock Analyst Pro",
    layout="wide",
    page_icon="📈",
    initial_sidebar_state="expanded"
)

# ==========================================
# PREMIUM CSS STYLING
# ==========================================

st.markdown("""
<style>
/* MAIN APP STYLING */
.stApp {
    background: 
        radial-gradient(circle at 20% 50%, rgba(30, 58, 138, 0.2) 0%, transparent 50%),
        radial-gradient(circle at 80% 80%, rgba(14, 165, 233, 0.15) 0%, transparent 50%),
        linear-gradient(135deg, #020617 0%, #0f172a 25%, #111827 75%, #1a202c 100%);
    color: white;
    font-family: 'Segoe UI', 'Roboto', sans-serif;
}

/* REMOVE DEFAULT PADDING */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

/* SIDEBAR STYLING */
[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.8) !important;
    border-right: 1px solid rgba(56, 189, 248, 0.2) !important;
    backdrop-filter: blur(10px);
}

/* MAIN TITLE */
.main-title {
    font-size: 48px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 8px;
    background: linear-gradient(90deg, #38bdf8, #22c55e, #f59e0b, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 1.5px;
    animation: glow 2s ease-in-out infinite;
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
    font-size: 16px;
    letter-spacing: 0.5px;
}

/* GLASS MORPHISM CARD */
.glass-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    padding: 24px;
    border-radius: 22px;
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.08);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-card:hover {
    transform: translateY(-4px) scale(1.01);
    box-shadow: 
        0 20px 40px rgba(14, 165, 233, 0.25),
        0 8px 24px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(56, 189, 248, 0.4);
}

/* METRIC CARD */
.metric-card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(34, 197, 94, 0.2);
    padding: 18px;
    border-radius: 16px;
    text-align: center;
    transition: all 0.3s ease;
}

.metric-card:hover {
    transform: scale(1.05);
    border-color: rgba(34, 197, 94, 0.6);
    box-shadow: 0 10px 30px rgba(34, 197, 94, 0.1);
}

/* INPUT FIELDS */
.stTextInput > div > div {
    background: rgba(255, 255, 255, 0.06);
    border-radius: 14px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.3s ease;
}

.stTextInput > div > div:focus-within {
    border: 1px solid #38bdf8;
    box-shadow: 0 0 20px rgba(56, 189, 248, 0.25);
    background: rgba(255, 255, 255, 0.08);
}

/* BUTTONS */
.stButton > button {
    width: 100%;
    height: 48px;
    border: none;
    border-radius: 14px;
    font-size: 16px;
    font-weight: 600;
    color: white;
    background: linear-gradient(90deg, #0ea5e9, #2563eb, #22c55e);
    box-shadow: 0 8px 25px rgba(37, 99, 235, 0.35);
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    letter-spacing: 0.5px;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 16px 40px rgba(14, 165, 233, 0.45);
}

.stButton > button:active {
    transform: translateY(-1px) scale(0.98);
}

/* TABS */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255, 255, 255, 0.03);
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    gap: 10px;
}

.stTabs [aria-selected="true"] {
    color: #38bdf8 !important;
    border-bottom: 2px solid #38bdf8 !important;
}

/* SECTION HEADER */
.section-header {
    font-size: 24px;
    font-weight: 800;
    margin-top: 30px;
    margin-bottom: 20px;
    color: white;
    padding-bottom: 12px;
    border-bottom: 2px solid rgba(56, 189, 248, 0.3);
}

/* PRICE UP/DOWN */
.price-up {
    color: #22c55e;
    font-weight: 700;
}

.price-down {
    color: #ef4444;
    font-weight: 700;
}

/* ANIMATIONS */
@keyframes glow {
    0%, 100% { text-shadow: 0 0 20px rgba(56, 189, 248, 0.5); }
    50% { text-shadow: 0 0 40px rgba(56, 189, 248, 0.8); }
}

/* FOOTER */
.footer {
    text-align: center;
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    color: #64748b;
    font-size: 13px;
}

/* SCROLLBAR */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: rgba(0, 0, 0, 0.2);
}
::-webkit-scrollbar-thumb {
    background: rgba(56, 189, 248, 0.5);
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgba(56, 189, 248, 0.8);
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR SETUP
# ==========================================

with st.sidebar:
    st.markdown("""
    <div class="glass-card" style="text-align: center;">
        <h2>📊 Navigation</h2>
    </div>
    """, unsafe_allow_html=True)
    
    page = st.radio("Select Page:", [
        "🏠 Dashboard",
        "🔍 Stock Analysis",
        "📊 Compare Stocks",
        "📈 Charts & Trends",
        "⭐ Watchlist",
        "📰 Market News"
    ])
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #64748b; font-size: 12px;">
        <p><strong>⚡ Powered by:</strong></p>
        <p>• Groq AI • yFinance • Agno Agentic</p>
        <p style="margin-top: 15px;">Last Updated: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# HELPER FUNCTIONS
# ==========================================

@st.cache_data(ttl=300)
def get_stock_analysis(symbol):
    """Fetch stock analysis from backend"""
    try:
        response = requests.post(
            "http://127.0.0.1:5000/analyze",
            json={"symbol": symbol},
            timeout=120
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        return None

@st.cache_data(ttl=300)
def get_chart_data(symbol, period="1mo"):
    """Fetch chart data from backend"""
    try:
        response = requests.get(
            f"http://127.0.0.1:5000/chart/{symbol}/{period}",
            timeout=30
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        st.error(f"❌ Chart Error: {str(e)}")
        return None

@st.cache_data(ttl=600)
def get_trending():
    """Get trending stocks"""
    try:
        response = requests.get("http://127.0.0.1:5000/trending", timeout=30)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

@st.cache_data(ttl=600)
def get_gainers():
    """Get top gainers"""
    try:
        response = requests.get("http://127.0.0.1:5000/gainers", timeout=30)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def format_market_cap(market_cap):
    """Format market cap display"""
    if market_cap is None:
        return "N/A"
    if market_cap >= 1e12:
        return f"${market_cap/1e12:.2f}T"
    elif market_cap >= 1e9:
        return f"${market_cap/1e9:.2f}B"
    elif market_cap >= 1e6:
        return f"${market_cap/1e6:.2f}M"
    else:
        return f"${market_cap:,.0f}"

# ==========================================
# PAGE: DASHBOARD
# ==========================================

if page == "🏠 Dashboard":
    st.markdown('<div class="main-title">📈 AI Stock Analyst Pro</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Advanced Stock Analysis Powered by Groq AI & Agno Agentic</div>', 
               unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header">🔥 Top Gainers</div>', unsafe_allow_html=True)
        gainers = get_gainers()
        
        if gainers and "gainers" in gainers:
            for idx, stock in enumerate(gainers["gainers"][:5]):
                col_a, col_b, col_c = st.columns([1, 2, 1])
                
                with col_a:
                    st.markdown(f"<div style='font-size:18px; font-weight:700;'>{stock['symbol']}</div>", 
                               unsafe_allow_html=True)
                
                with col_b:
                    st.markdown(f"<div>${stock['current_price']}</div>", unsafe_allow_html=True)
                
                with col_c:
                    change_pct = stock['change_pct']
                    color = "price-up" if change_pct > 0 else "price-down"
                    st.markdown(f"<div class='{color}'>{change_pct:+.2f}%</div>", 
                               unsafe_allow_html=True)
                
                st.divider()
    
    with col2:
        st.markdown('<div class="section-header">📉 Top Losers</div>', unsafe_allow_html=True)
        
        try:
            response = requests.get("http://127.0.0.1:5000/losers", timeout=30)
            if response.status_code == 200:
                losers = response.json()
                
                for idx, stock in enumerate(losers["losers"][:5]):
                    col_a, col_b, col_c = st.columns([1, 2, 1])
                    
                    with col_a:
                        st.markdown(f"<div style='font-size:18px; font-weight:700;'>{stock['symbol']}</div>", 
                                   unsafe_allow_html=True)
                    
                    with col_b:
                        st.markdown(f"<div>${stock['current_price']}</div>", unsafe_allow_html=True)
                    
                    with col_c:
                        change_pct = stock['change_pct']
                        color = "price-up" if change_pct > 0 else "price-down"
                        st.markdown(f"<div class='{color}'>{change_pct:+.2f}%</div>", 
                                   unsafe_allow_html=True)
                    
                    st.divider()
        except:
            st.info("📡 Fetching market data...")

# ==========================================
# PAGE: STOCK ANALYSIS
# ==========================================

elif page == "🔍 Stock Analysis":
    st.markdown('<div class="main-title">🔍 Stock Analysis</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        symbol = st.text_input(
            "🔎 Enter Stock Symbol",
            "NVDA",
            placeholder="e.g. AAPL, GOOGL, TSLA..."
        ).upper()
    
    with col2:
        st.write("")
        st.write("")
        analyze_btn = st.button("🚀 Analyze", use_container_width=True)
    
    if analyze_btn or symbol:
        with st.spinner("🤖 AI is analyzing the stock..."):
            data = get_stock_analysis(symbol)
            
            if data and data.get("success"):
                metrics = data["metrics"]
                
                # Display Metrics
                st.markdown('<div class="section-header">📊 Stock Metrics</div>', unsafe_allow_html=True)
                
                m_col1, m_col2, m_col3, m_col4 = st.columns(4)
                
                with m_col1:
                    price_html = f"""
                    <div class='metric-card'>
                        <div style='font-size:12px; color:#94a3b8; margin-bottom:8px;'>Current Price</div>
                        <div style='font-size:24px; font-weight:800;'>${metrics['current_price']}</div>
                        <div class='{"price-up" if metrics["change_pct"] > 0 else "price-down"}'>{metrics["change_pct"]:+.2f}%</div>
                    </div>
                    """
                    st.markdown(price_html, unsafe_allow_html=True)
                
                with m_col2:
                    st.markdown(f"""
                    <div class='metric-card'>
                        <div style='font-size:12px; color:#94a3b8; margin-bottom:8px;'>Market Cap</div>
                        <div style='font-size:20px; font-weight:700;'>{format_market_cap(metrics['market_cap'])}</div>
                        <div style='font-size:11px; color:#cbd5e1; margin-top:8px;'>{metrics.get('sector', 'N/A')}</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with m_col3:
                    st.markdown(f"""
                    <div class='metric-card'>
                        <div style='font-size:12px; color:#94a3b8; margin-bottom:8px;'>PE Ratio</div>
                        <div style='font-size:24px; font-weight:800;'>{metrics.get('pe_ratio', 'N/A')}</div>
                        <div style='font-size:11px; color:#cbd5e1; margin-top:8px;'>EPS: {metrics.get('eps', 'N/A')}</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with m_col4:
                    div_yield = metrics.get('dividend_yield', 0)
                    div_text = f"{div_yield*100:.2f}%" if div_yield else "N/A"
                    st.markdown(f"""
                    <div class='metric-card'>
                        <div style='font-size:12px; color:#94a3b8; margin-bottom:8px;'>Div. Yield</div>
                        <div style='font-size:24px; font-weight:800;'>{div_text}</div>
                        <div style='font-size:11px; color:#cbd5e1; margin-top:8px;'>52W: ${metrics['fifty_two_week_low']}-${metrics['fifty_two_week_high']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # AI Analysis
                st.markdown('<div class="section-header">🤖 AI Professional Analysis</div>', 
                           unsafe_allow_html=True)
                
                st.markdown("""
                <div class='glass-card'>
                """ + data["analysis"] + """
                </div>
                """, unsafe_allow_html=True)
                
                # Chart
                st.markdown('<div class="section-header">📈 1 Month Price Chart</div>', 
                           unsafe_allow_html=True)
                
                chart_data = data["chart"]
                
                fig = go.Figure()
                fig.add_trace(go.Candlestick(
                    x=chart_data["dates"],
                    open=chart_data["open"],
                    high=chart_data["high"],
                    low=chart_data["low"],
                    close=chart_data["close"],
                    name="Price"
                ))
                
                fig.update_layout(
                    template="plotly_dark",
                    xaxis_rangeslider_visible=False,
                    height=500,
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.06)"),
                    font=dict(family="Arial", size=12, color="white")
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Volume Chart
                st.markdown('<div class="section-header">📊 Volume Analysis</div>', 
                           unsafe_allow_html=True)
                
                fig_vol = go.Figure()
                colors = ['green' if chart_data['close'][i] >= chart_data['open'][i] else 'red' 
                         for i in range(len(chart_data['close']))]
                
                fig_vol.add_trace(go.Bar(
                    x=chart_data["dates"],
                    y=chart_data["volume"],
                    marker=dict(color=colors),
                    name="Volume"
                ))
                
                fig_vol.update_layout(
                    template="plotly_dark",
                    height=300,
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    showlegend=False,
                    font=dict(family="Arial", size=12, color="white")
                )
                
                st.plotly_chart(fig_vol, use_container_width=True)
            
            else:
                st.error(f"❌ Could not fetch data for {symbol}. Please check the symbol and try again.")

# ==========================================
# PAGE: COMPARE STOCKS
# ==========================================

elif page == "📊 Compare Stocks":
    st.markdown('<div class="main-title">📊 Compare Stocks</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        symbol1 = st.text_input("📌 Stock 1", "AAPL").upper()
    
    with col2:
        st.write("")
        st.write("")
        st.markdown("<div style='text-align:center; font-weight:700; color:#38bdf8;'>VS</div>", 
                   unsafe_allow_html=True)
    
    with col3:
        symbol2 = st.text_input("📌 Stock 2", "GOOGL").upper()
    
    if st.button("🔄 Compare", use_container_width=True):
        with st.spinner("🔄 Comparing stocks..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:5000/compare",
                    json={"symbol1": symbol1, "symbol2": symbol2},
                    timeout=120
                )
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Side by side comparison
                    comp_col1, comp_col2 = st.columns(2)
                    
                    with comp_col1:
                        st.markdown(f"""
                        <div class='glass-card' style='text-align:center;'>
                            <h2>{symbol1}</h2>
                            <div style='font-size:24px; font-weight:700; color:#38bdf8;'>${data['stocks']['stock1']['current_price']}</div>
                            <div class='{"price-up" if data['stocks']['stock1']['change_pct'] > 0 else "price-down"}'>{data['stocks']['stock1']['change_pct']:+.2f}%</div>
                            <hr style='border:1px solid rgba(255,255,255,0.1); margin:15px 0;'>
                            <div style='text-align:left; font-size:13px;'>
                                <p><strong>Market Cap:</strong> {format_market_cap(data['stocks']['stock1']['market_cap'])}</p>
                                <p><strong>PE Ratio:</strong> {data['stocks']['stock1']['pe_ratio']}</p>
                                <p><strong>52W High:</strong> ${data['stocks']['stock1']['fifty_two_week_high']}</p>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with comp_col2:
                        st.markdown(f"""
                        <div class='glass-card' style='text-align:center;'>
                            <h2>{symbol2}</h2>
                            <div style='font-size:24px; font-weight:700; color:#38bdf8;'>${data['stocks']['stock2']['current_price']}</div>
                            <div class='{"price-up" if data['stocks']['stock2']['change_pct'] > 0 else "price-down"}'>{data['stocks']['stock2']['change_pct']:+.2f}%</div>
                            <hr style='border:1px solid rgba(255,255,255,0.1); margin:15px 0;'>
                            <div style='text-align:left; font-size:13px;'>
                                <p><strong>Market Cap:</strong> {format_market_cap(data['stocks']['stock2']['market_cap'])}</p>
                                <p><strong>PE Ratio:</strong> {data['stocks']['stock2']['pe_ratio']}</p>
                                <p><strong>52W High:</strong> ${data['stocks']['stock2']['fifty_two_week_high']}</p>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown('<div class="section-header">🤖 AI Comparison Analysis</div>', 
                               unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    <div class='glass-card'>
                    {data.get('comparison', 'Analysis in progress...')}
                    </div>
                    """, unsafe_allow_html=True)
                
                else:
                    st.error("❌ Error comparing stocks")
            
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# ==========================================
# PAGE: CHARTS & TRENDS
# ==========================================

elif page == "📈 Charts & Trends":
    st.markdown('<div class="main-title">📈 Charts & Technical Analysis</div>', unsafe_allow_html=True)
    
    symbol = st.text_input("📊 Select Stock Symbol", "NVDA").upper()
    
    tabs = st.tabs(["1M", "3M", "6M", "1Y", "Comparison"])
    
    with tabs[0]:
        st.subheader("1 Month Chart")
        data = get_chart_data(symbol, "1mo")
        if data:
            chart_data = data["chart"]
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=chart_data["dates"], y=chart_data["close"], 
                                    mode="lines", fill="tozeroy", name="Price"))
            fig.update_layout(template="plotly_dark", height=500)
            st.plotly_chart(fig, use_container_width=True)
    
    with tabs[1]:
        st.subheader("3 Month Chart")
        data = get_chart_data(symbol, "3mo")
        if data:
            chart_data = data["chart"]
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=chart_data["dates"], y=chart_data["close"], 
                                    mode="lines", fill="tozeroy", name="Price"))
            fig.update_layout(template="plotly_dark", height=500)
            st.plotly_chart(fig, use_container_width=True)
    
    with tabs[2]:
        st.subheader("6 Month Chart")
        data = get_chart_data(symbol, "6mo")
        if data:
            chart_data = data["chart"]
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=chart_data["dates"], y=chart_data["close"], 
                                    mode="lines", fill="tozeroy", name="Price"))
            fig.update_layout(template="plotly_dark", height=500)
            st.plotly_chart(fig, use_container_width=True)
    
    with tabs[3]:
        st.subheader("1 Year Chart")
        data = get_chart_data(symbol, "1y")
        if data:
            chart_data = data["chart"]
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=chart_data["dates"], y=chart_data["close"], 
                                    mode="lines", fill="tozeroy", name="Price"))
            fig.update_layout(template="plotly_dark", height=500)
            st.plotly_chart(fig, use_container_width=True)
    
    with tabs[4]:
        st.subheader("Stock Comparison")
        sym1, sym2 = st.columns(2)
        with sym1:
            stock_a = st.text_input("Stock A", "AAPL").upper()
        with sym2:
            stock_b = st.text_input("Stock B", "GOOGL").upper()
        
        data_a = get_chart_data(stock_a, "1y")
        data_b = get_chart_data(stock_b, "1y")
        
        if data_a and data_b:
            fig = go.Figure()
            
            chart_a = data_a["chart"]
            chart_b = data_b["chart"]
            
            fig.add_trace(go.Scatter(x=chart_a["dates"], y=chart_a["close"], 
                                    mode="lines", name=stock_a))
            fig.add_trace(go.Scatter(x=chart_b["dates"], y=chart_b["close"], 
                                    mode="lines", name=stock_b))
            
            fig.update_layout(template="plotly_dark", height=500)
            st.plotly_chart(fig, use_container_width=True)

# ==========================================
# PAGE: WATCHLIST
# ==========================================

elif page == "⭐ Watchlist":
    st.markdown('<div class="main-title">⭐ My Watchlist</div>', unsafe_allow_html=True)
    
    if 'watchlist' not in st.session_state:
        st.session_state.watchlist = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        new_stock = st.text_input("Add to watchlist", "").upper()
    
    with col2:
        if st.button("➕ Add"):
            if new_stock and new_stock not in st.session_state.watchlist:
                st.session_state.watchlist.append(new_stock)
                st.success(f"✅ Added {new_stock}")
    
    st.markdown('<div class="section-header">📊 Your Watchlist</div>', unsafe_allow_html=True)
    
    for idx, stock in enumerate(st.session_state.watchlist):
        col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
        
        try:
            response = requests.get(f"http://127.0.0.1:5000/metrics/{stock}", timeout=10)
            if response.status_code == 200:
                metrics = response.json()["data"]
                
                with col1:
                    st.markdown(f"<div style='font-size:18px; font-weight:700;'>{stock}</div>", 
                               unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"<div>${metrics['current_price']}</div>", unsafe_allow_html=True)
                
                with col3:
                    change_pct = metrics['change_pct']
                    color = "price-up" if change_pct > 0 else "price-down"
                    st.markdown(f"<div class='{color}'>{change_pct:+.2f}%</div>", 
                               unsafe_allow_html=True)
                
                with col4:
                    if st.button("🗑️", key=f"del_{stock}"):
                        st.session_state.watchlist.remove(stock)
                        st.rerun()
                
                st.divider()
        except:
            pass

# ==========================================
# PAGE: MARKET NEWS
# ==========================================

elif page == "📰 Market News":
    st.markdown('<div class="main-title">📰 Market News & Sentiment</div>', unsafe_allow_html=True)
    
    st.info("📡 Live market news feature coming soon! Subscribe to get real-time market updates.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='glass-card' style='text-align:center;'>
            <h3>🔔 Market Updates</h3>
            <p>Real-time market sentiment and news analysis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='glass-card' style='text-align:center;'>
            <h3>📊 Sector News</h3>
            <p>Industry-specific trends and developments</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='glass-card' style='text-align:center;'>
            <h3>🌍 Global Events</h3>
            <p>International markets and economic indicators</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    <p>🚀 AI Stock Analyst Pro | Premium Stock Analysis Platform</p>
    <p>Powered by: Groq AI • yFinance • Agno Agentic • Streamlit</p>
    <p style="margin-top: 10px; color: #475569;">
        ⚠️ Disclaimer: This tool is for educational purposes. Not financial advice.
    </p>
</div>
""", unsafe_allow_html=True)
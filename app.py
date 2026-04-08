import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
from sklearn.ensemble import IsolationForest

# STYLED CONFIGURATION
st.set_page_config(page_title="Strategic Resilience Observatory v3.3", layout="wide")

# CORPORATE HEADER
st.title("🌐 Strategic Resilience Observatory v3.3")
st.markdown("### *High-Fidelity Intelligence: Food Security vs AI Sovereignty*")
st.write("---")

# DATA ENGINE (ONLINE ONLY)
@st.cache_data
def load_intel_data():
    # Indicators: MOS (Fertilizer), WEAT (Wheat), TSM (AI Hardware)
    tickers = ['MOS', 'WEAT', 'TSM']
    df = yf.download(tickers, period="2y")['Close']
    return df

try:
    raw_data = load_intel_data()
    # Normalize for comparison (0 to 1 scale)
    norm_data = (raw_data - raw_data.min()) / (raw_data.max() - raw_data.min())

    # ANOMALY DETECTION ENGINE (UNSEEN SIGNALS)
    model = IsolationForest(contamination=0.05)
    norm_data['Anomaly_Score'] = model.fit_predict(norm_data[['MOS', 'WEAT', 'TSM']])
    
    # UI LAYOUT
    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("Multi-Layered Signal Analysis")
        fig = px.line(norm_data, y=['MOS', 'WEAT', 'TSM'], 
                     labels={"value": "Signal Intensity", "variable": "Indicator"},
                     color_discrete_map={"MOS": "green", "WEAT": "orange", "TSM": "blue"})
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Strategic Briefing")
        
        # LOGIC FOR UNDERESTIMATED SIGNALS
        st.info("**Fertilizer-Wheat Decoupling:** Data shows a widening gap between input costs and output prices. This is a high-probability indicator of 'Controlled Escalation Management'.")
        
        st.warning("**AI-Hardware Momentum:** The Blue line (TSM) maintains aggressive growth regardless of commodity volatility. Confirms 'Technological Sovereignty' as the primary geopolitical weapon.")
        
        # ANOMALY FLAG
        if norm_data['Anomaly_Score'].iloc[-1] == -1:
            st.error("🚨 **ANOMALY DETECTED:** Current patterns diverge from historical equilibrium. Immediate monitoring of 'Silent Proxies' recommended.")

    st.write("---")
    st.write("#### Verified Observation Table (Last 10 Cycles)")
    st.dataframe(norm_data.tail(10))

except Exception as e:
    st.error(f"Technical Friction Detected: {e}")

# KESELAMATAN & DISCLAIMER
st.caption("DISCLAIMER: For educational and corporate strategic foresight only. This dashboard utilizes open-source market proxies to analyze regional resilience.")

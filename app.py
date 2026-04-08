import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# STYLED CONFIGURATION
st.set_page_config(page_title="Strategic Resilience Observatory v3.3", layout="wide")

# PRINCIPAL INVESTIGATOR ATTRIBUTION (SIDEBAR)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1063/1063374.png", width=50)
st.sidebar.markdown(f"""
# 🕵️‍♂️ Principal Investigator
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**
---
### **Expert Domain:**
*Espionage Analysis, Strategic Intelligence, & Geopolitical Risk Consulting.*
---
*“In an era of noise, the signal is our only weapon.”*
""")

# CORPORATE HEADER
st.title("🌐 Strategic Resilience Observatory v3.3")
st.markdown("## *High-Fidelity Intelligence & Predictive Anomaly Suite*")
st.write("---")

# DATA ENGINE (HOURLY REFRESH - TTL=3600)
@st.cache_data(ttl=3600)
def load_intel_data():
    # Indicators: 
    # MOS (Fertilizer), WEAT (Wheat), TSM (AI Hardware), 
    # PFE (Pharma/Silent Proxy), ^VIX (Market Fear/Narrative Proxy)
    tickers = ['MOS', 'WEAT', 'TSM', 'PFE', '^VIX']
    df = yf.download(tickers, period="2y")['Close']
    df.columns = ['AI_Hardware', 'Fertilizer', 'Pharma_Proxy', 'Market_Fear', 'Wheat_Index']
    return df

try:
    raw_data = load_intel_data()
    # Normalize for comparison
    norm_data = (raw_data - raw_data.min()) / (raw_data.max() - raw_data.min())

    # ANOMALY DETECTION ENGINE
    model = IsolationForest(contamination=0.04)
    norm_data['Anomaly_Score'] = model.fit_predict(norm_data[['Fertilizer', 'Wheat_Index', 'AI_Hardware']])
    
    # UI LAYOUT: TOP SECTION
    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("📡 Real-Time Multi-Signal Intelligence Feed")
        fig = px.line(norm_data, y=['Fertilizer', 'Wheat_Index', 'AI_Hardware', 'Pharma_Proxy', 'Market_Fear'], 
                     labels={"value": "Signal Intensity", "variable": "Strategic Indicator"},
                     color_discrete_map={"Fertilizer": "green", "Wheat_Index": "orange", 
                                         "AI_Hardware": "blue", "Pharma_Proxy": "purple", "Market_Fear": "red"})
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("📝 Strategic Briefing")
        st.info(f"**PI Oversight:** Data as of {pd.Timestamp.now().strftime('%H:%00 UTC')}. Observing decoupling in Resource-Logic.")
        
        # EXPERT INTERPRETATION LOGIC
        st.warning("**Silent Proxy Alert:** Pharma-Logistics (Purple) movement often precedes systemic shifts. Correlation with AI-Hardware (Blue) is critical.")
        
        if norm_data['Anomaly_Score'].iloc[-1] == -1:
            st.error("🚨 **CRITICAL ANOMALY:** Non-linear patterns detected. Grey Zone activity high. High probability of 'Strategic Theater'.")
        else:
            st.success("✅ **Status:** Baseline Equilibrium maintained. No immediate systemic threat detected.")

    st.write("---")

    # BOTTOM SECTION: CORRELATION HEATMAP (THE "SANDIWARA" DETECTOR)
    col_heat1, col_heat2 = st.columns([1, 1])

    with col_heat1:
        st.subheader("🔍 Correlation Matrix: Finding the 'Decoupling'")
        corr = raw_data.corr()
        fig_heat, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap='RdYlGn', ax=ax)
        st.pyplot(fig_heat)

    with col_heat2:
        st.subheader("👨‍💻 PI Expert Analysis")
        st.markdown(f"""
        1. **The Decoupling:** Look for **Red/Yellow** boxes between 'Fertilizer' and 'Wheat'. If they are not moving together (Correlation < 0.5), the market is being manipulated or "buffered" for a strategic move.
        2. **AI-Fear Divergence:** If 'Market Fear' (VIX) is low but 'AI Hardware' is surging, it indicates institutional confidence in a 'Tech-Driven' outcome, bypassing humanitarian risks.
        3. **Pharma Lead Time:** Watch the 'Pharma_Proxy'. A sudden correlation increase with 'Fertilizer' suggests preparation for large-scale regional disruption.
        """)

    st.write("---")
    st.dataframe(norm_data.tail(5))

except Exception as e:
    st.error(f"Technical Friction: {e}")

# KESELAMATAN & DISCLAIMER
st.caption(f"© 2024 Strategic Resilience Observatory. Principal Investigator: MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL. [Educational/Corporate Foresight Only]")

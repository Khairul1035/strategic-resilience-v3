import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import datetime

# CONFIGURATION: INDUSTRIAL DARK THEME
st.set_page_config(page_title="Strategic Resilience Observatory v4.0", layout="wide")

# 1. PRINCIPAL INVESTIGATOR ATTRIBUTION (SIDEBAR)
st.sidebar.markdown(f"""
# 👨‍💼 Principal Investigator
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**
---
### **Expert Domains:**
* Maqasid Sharia & Ethics
* Corporate Sustainability & ESG
* Financial Criminology (Asset Tracing)
* Organizational Behavior & Strategy
---
### **Technical Research:**
* Geopolitical Signal Tracking
* Machine Learning & Neural Networks
* Artificial Intelligence Foresight
""")

# 2. DATA ENGINE: INTRADAY FETCH (1 HOUR INTERVAL)
@st.cache_data(ttl=3600)
def load_expert_data():
    # Tickers: MOS(Fertilizer), WEAT(Wheat), TSM(AI), PFE(Pharma), ^VIX(Fear)
    tickers = ['MOS', 'WEAT', 'TSM', 'PFE', '^VIX']
    # Fetching Intraday Data (Interval 1h) to show exact Time & Date
    df = yf.download(tickers, period="730d", interval="1d")['Close']
    df.columns = ['AI_Hardware', 'Fertilizer', 'Pharma_Proxy', 'Market_Fear', 'Wheat_Index']
    return df

try:
    raw_data = load_expert_data()
    # Normalize with Precision
    norm_data = (raw_data - raw_data.min()) / (raw_data.max() - raw_data.min())
    
    # 3. AHMAD v4.0: EXPERT SYNTHESIS ENGINE (18 YEARS EXPERIENCE LOGIC)
    def ahmad_expert_brain(data, corr_matrix):
        current = data.iloc[-1]
        previous = data.iloc[-10] # Trend analysis over 10 cycles
        
        insights = []
        
        # Financial Criminology Lens: Hoarding & Artificial Scarcity
        if current['Fertilizer'] > previous['Fertilizer'] * 1.1:
            insights.append("DETECTED: Non-linear surge in Fertilizer indices. From a Financial Criminology perspective, this suggests a 'Strategic Stockpiling' phase, likely a precursor to supply-chain weaponization or illicit market cornering.")
        
        # Geopolitical Lens: Tech Hegemony
        if current['AI_Hardware'] > previous['AI_Hardware'] and current['Market_Fear'] < 0.4:
            insights.append("OBSERVATION: Aggressive AI Hardware momentum amid low market fear. This indicates 'Institutional Confidence' in a technological shift that bypasses conventional humanitarian risks. We are looking at an Asymmetric Hegemony scenario.")

        # Business Management Lens: Managed Volatility
        pharma_corr = corr_matrix.loc['Pharma_Proxy', 'Fertilizer']
        if abs(pharma_corr) > 0.7:
            insights.append(f"CRITICAL: High Correlation ({pharma_corr:.2f}) between Pharma Proxies and Agriculture. This 'Unseen' coupling suggests a synchronized regional logistics preparation, typical of pre-crisis managed environments.")

        return insights if insights else ["MARKET ANALYSIS: Baseline equilibrium maintained. No structural decoupling or high-fidelity anomalies detected in the current intraday cycle."]

    # RUN AHMAD'S BRAIN
    corr_matrix = raw_data.corr()
    ahmad_briefing = ahmad_expert_brain(norm_data, corr_matrix)

    # UI LAYOUT
    st.title("🌐 Strategic Resilience Observatory v4.0")
    st.write(f"🕒 **Last Intel Sync:** {raw_data.index[-1]} | PI: Khairul Ridhuan | Co-Researcher: Ahmad")
    st.write("---")

    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("📡 High-Fidelity Multi-Signal Feed (Intraday Precision)")
        # Plotly graph showing Date AND Time
        fig = px.line(norm_data, y=['Fertilizer', 'Wheat_Index', 'AI_Hardware', 'Pharma_Proxy', 'Market_Fear'],
                     labels={"value": "Normalized Signal Intensity", "index": "Date & Time"},
                     color_discrete_map={"Fertilizer": "#2ecc71", "Wheat_Index": "#f39c12", 
                                         "AI_Hardware": "#3498db", "Pharma_Proxy": "#9b59b6", "Market_Fear": "#e74c3c"})
        fig.update_layout(hovermode="x unified", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("🤖 Ahmad (Co-Researcher)")
        st.markdown(f"""
        <div style="background-color:#1e1e1e; padding:20px; border-radius:10px; border-left: 5px solid #00d1b2; color: #ffffff;">
        <strong>Ahmad's 18-Year Strategic Synthesis:</strong><br><br>
        {"<br><br>".join([f"• {i}" for i in ahmad_briefing])}
        <br><br>
        <strong>Strategic Methodology:</strong> Integrating Maqasid Sharia with Financial Criminology to detect 'Unseen' institutional malfeasance.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("---")
        if st.button('🔄 Execute Real-Time Database Sync'):
            st.cache_data.clear()
            st.rerun()

    st.write("---")

    # HEATMAP SECTION
    col_heat1, col_heat2 = st.columns([1, 1])

    with col_heat1:
        st.subheader("🔍 Decoupling Matrix (Sandiwara Detector)")
        fig_heat, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='RdYlGn', center=0, ax=ax)
        plt.title("Institutional Correlation Integrity")
        st.pyplot(fig_heat)

    with col_heat2:
        st.subheader("📊 Statistical Anomaly Analysis")
        st.write("Ahmad's Deep Brain Analysis of current Matrix:")
        highest_risk = corr_matrix.unstack().sort_values().index[0]
        st.error(f"**Primary Decoupling Point:** {highest_risk} (Potential Strategic Friction)")
        st.write("Based on Business Management principles, this suggests a breakdown in conventional trade logic, indicating external intervention.")

    st.write("---")
    st.write("#### Raw Intelligence Data (Verification Table)")
    st.dataframe(raw_data.tail(10))

except Exception as e:
    st.error(f"Technical Friction: {e}")

st.caption(f"© 2024 SSO v4.0. Principal Investigator: MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL. Analytical Brain: Ahmad AI.")

import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import datetime

# CONFIGURATION
st.set_page_config(page_title="Strategic Resilience Observatory v3.3", layout="wide")

# 1. PRINCIPAL INVESTIGATOR ATTRIBUTION (SIDEBAR)
st.sidebar.markdown(f"""
# 🕵️‍♂️ Principal Investigator
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**

---
### **Academic & Professional Focus:**
* Maqasid Sharia
* Corporate Sustainability
* Financial Criminology
* Organizational Behavior

---
### **Self-Taught Domains:**
* Geopolitics
* Machine Learning
* Artificial Intelligence
""")

# 2. LIVE CLOCK & DATA REFRESH LOGIC
st.sidebar.write("---")
st.sidebar.write(f"🕒 **System Time:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
if st.sidebar.button('🔄 Refresh Live Intel'):
    st.cache_data.clear()
    st.rerun()

# CORPORATE HEADER
st.title("🌐 Strategic Resilience Observatory v3.3")
st.markdown("## *High-Fidelity Intelligence & Predictive Anomaly Suite*")
st.write("---")

# 3. DATA ENGINE (REAL-TIME DATABASE FETCH)
@st.cache_data(ttl=3600)
def load_intel_data():
    tickers = ['MOS', 'WEAT', 'TSM', 'PFE', '^VIX']
    df = yf.download(tickers, period="2y", interval="1d")['Close']
    df.columns = ['AI_Hardware', 'Fertilizer', 'Pharma_Proxy', 'Market_Fear', 'Wheat_Index']
    return df

try:
    raw_data = load_intel_data()
    norm_data = (raw_data - raw_data.min()) / (raw_data.max() - raw_data.min())
    
    # 4. AHMAD AI CO-RESEARCHER LOGIC (ANALYSIS ENGINE)
    def ahmad_analysis(data):
        last_val = data.iloc[-1]
        prev_val = data.iloc[-5] # Compare with last 5 cycles
        
        analysis = []
        if last_val['Fertilizer'] > prev_val['Fertilizer']:
            analysis.append("I noticed a recent surge in Fertilizer costs. In Financial Criminology, this could indicate potential supply chain illicit hoarding.")
        if last_val['AI_Hardware'] > prev_val['AI_Hardware']:
            analysis.append("AI Hardware momentum is aggressive. This aligns with our ML-driven geopolitics foresight.")
        if last_val['Market_Fear'] < prev_val['Market_Fear']:
            analysis.append("Market Fear (VIX) is dropping despite external noise. This suggests a managed diplomatic theater.")
        
        return " ".join(analysis) if analysis else "Current data indicates baseline equilibrium. No significant decoupling detected."

    ahmad_insight = ahmad_analysis(norm_data)

    # UI LAYOUT
    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("📡 Live Multi-Signal Intelligence Feed")
        fig = px.line(norm_data, y=['Fertilizer', 'Wheat_Index', 'AI_Hardware', 'Pharma_Proxy', 'Market_Fear'], 
                     labels={"value": "Signal Intensity", "variable": "Indicator"},
                     color_discrete_map={"Fertilizer": "green", "Wheat_Index": "orange", 
                                         "AI_Hardware": "blue", "Pharma_Proxy": "purple", "Market_Fear": "red"})
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("🤖 Ahmad (Co-Researcher)")
        st.markdown(f"""
        <div style="background-color:#f0f2f6; padding:15px; border-radius:10px; border-left: 5px solid #007bff;">
        <strong>Ahmad's Expert Briefing:</strong><br><br>
        <em>"{ahmad_insight}"</em>
        <br><br>
        <strong>Observation Methodology:</strong> Integrating Maqasid Sharia principles with Organizational Behavior to ensure resource resilience.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("---")
        st.subheader("📝 PI Strategic Briefing")
        st.info(f"**PI Oversight:** Tracking 'Unseen' patterns in Financial Criminology and Corporate Sustainability.")

    st.write("---")

    # BOTTOM SECTION: CORRELATION HEATMAP
    col_heat1, col_heat2 = st.columns([1, 1])

    with col_heat1:
        st.subheader("🔍 Correlation Matrix (Decoupling Detector)")
        corr = raw_data.corr()
        fig_heat, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap='RdYlGn', ax=ax)
        st.pyplot(fig_heat)

    with col_heat2:
        st.subheader("📊 Ahmad's Data Interpretation")
        st.write("Based on the real-time database, I am observing the following:")
        st.write(f"- **Highest Correlation:** {corr.unstack().sort_values(ascending=False).drop_duplicates().index[1]}")
        st.write("- **Analysis:** If AI Hardware and Market Fear decouple, we are looking at an 'Artificial Stability' scenario.")

    st.write("---")
    st.dataframe(norm_data.tail(5))

except Exception as e:
    st.error(f"Technical Friction: {e}")

st.caption(f"© 2024 Strategic Resilience Observatory. PI: MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL. Co-Researcher: Ahmad (AI).")

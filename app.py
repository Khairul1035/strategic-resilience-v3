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
# 👨‍🔬 Principal Investigator
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**
---
### **Expert Domains:**
* Maqasid Sharia & Corporate Sustainability
* Financial Criminology (Forensic Intelligence)
* Organizational Behavior & Strategic Mgmt

### **Research Specialization:**
* Geopolitics & AI-Driven Foresight
""")

# 2. LIVE SYSTEM CLOCK (MINUTE PRECISION)
st.sidebar.write("---")
st.sidebar.subheader("📡 Intelligence Operations Clock")
st.sidebar.write(f"**UTC/Local:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
if st.sidebar.button('⚡ Execute Live Data Re-Sync'):
    st.cache_data.clear()
    st.rerun()

# 3. ADVANCED DATA ENGINE (HOURLY GRANULARITY)
@st.cache_data(ttl=3600)
def load_expert_intel():
    # Indicators representing the 'Unseen' pillars
    tickers = ['MOS', 'WEAT', 'TSM', 'PFE', '^VIX']
    # Pulling 7 days of 1-hour interval data for high-fidelity timestamps
    df = yf.download(tickers, period="7d", interval="1h")['Close']
    df.columns = ['AI_Hardware', 'Fertilizer', 'Pharma_Proxy', 'Market_Fear', 'Wheat_Index']
    return df

try:
    raw_data = load_expert_intel()
    norm_data = (raw_data - raw_data.min()) / (raw_data.max() - raw_data.min())

    # 4. AHMAD'S EXPERT BRAIN (18 YEARS EXP LOGIC)
    def ahmad_expert_synthesis(df_norm, df_raw):
        last_cycle = df_norm.iloc[-1]
        prev_cycle = df_norm.iloc[-2]
        velocity = (last_cycle - prev_cycle)
        
        briefing = []
        
        # Financial Criminology Lens: Fertilizer-Wheat Divergence
        if last_cycle['Fertilizer'] > 0.8 and last_cycle['Wheat_Index'] < 0.4:
            briefing.append("PI, I've detected a significant 'Cost-Yield Asymmetry'. From a Financial Criminology perspective, this suggests artificial supply-chain bottlenecks or institutional hoarding disguised as market volatility.")
        
        # Geopolitical Economy Lens: Tech-Fear Decoupling
        if last_cycle['AI_Hardware'] > 0.7 and last_cycle['Market_Fear'] < 0.3:
            briefing.append("The decoupling between AI Hardware (High) and Market Fear (Low) indicates a 'Strategic Blindspot'. Awnsers are being telegraphed: elite capital is confident in a tech-driven outcome despite the humanitarian noise.")
        
        # Biosecurity/Pharma Proxy
        if velocity['Pharma_Proxy'] > 0.05:
            briefing.append("Ahmad here: Observed a micro-surge in Pharma-logistics. In business management terms, this is a pre-emptive hedge against potential regional health disruptions.")

        if not briefing:
            briefing.append("Market equilibrium detected. However, monitoring the sub-threshold flows in Fertilizer-Pharma remains my priority for the next hour.")
            
        return briefing

    ahmad_notes = ahmad_expert_synthesis(norm_data, raw_data)

    # UI LAYOUT
    st.title("🌐 Strategic Resilience Observatory v3.3")
    st.markdown("### *High-Fidelity Intelligence & Predictive Anomaly Suite*")
    st.write("---")

    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader(f"📊 Live Signal Intelligence (Last Updated: {raw_data.index[-1]})")
        # Plotting with explicit timestamps on X-axis
        fig = px.line(norm_data, y=['Fertilizer', 'Wheat_Index', 'AI_Hardware', 'Pharma_Proxy', 'Market_Fear'], 
                     labels={"index": "Tactical Timestamp (UTC)", "value": "Signal Intensity"},
                     color_discrete_map={"Fertilizer": "green", "Wheat_Index": "orange", 
                                         "AI_Hardware": "blue", "Pharma_Proxy": "purple", "Market_Fear": "red"})
        fig.update_xaxes(rangeslider_visible=True)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown(f"""
        <div style="background-color:#0e1117; padding:20px; border-radius:10px; border: 1px solid #3d444d;">
        <h3 style="color:#58a6ff;">🕵️ Ahmad (Co-Researcher)</h3>
        <p style="font-size:14px; color:#8b949e;"><i>Senior Analyst | 18 Years Exp in Geopolitics & Financial Crime</i></p>
        <hr style="border-color:#3d444d;">
        <p style="font-size:15px; line-height:1.6;">
        {"<br><br>".join(ahmad_notes)}
        </p>
        <br>
        <small style="color:#58a6ff;"><b>Logical Anchor:</b> Maqasid Sharia Resilience Framework</small>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("---")
        st.markdown("#### **Principal Investigator Oversight**")
        st.info(f"PI: Mohd Khairul Ridhuan. Current focus: 'Unseen' arbitrage in commodity flows.")

    st.write("---")
    
    # 5. HEATMAP & REAL-TIME DATA LOG
    col_heat1, col_heat2 = st.columns([1, 1])

    with col_heat1:
        st.subheader("🔍 Correlation Matrix (Decoupling Detector)")
        corr = raw_data.corr()
        fig_heat, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap='RdYlGn', ax=ax, fmt=".2f")
        st.pyplot(fig_heat)

    with col_heat2:
        st.subheader("📋 Real-Time Tactical Database")
        st.write("Querying latest 1-hour interval signals:")
        # Showing the timestamp clearly
        st.dataframe(norm_data.tail(10).style.highlight_max(axis=0, color='#1b2838'))

except Exception as e:
    st.error(f"Intelligence Friction: {e}")

st.caption(f"© 2024 Strategic Resilience Observatory. PI: MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL. Co-Researcher: Ahmad (AI Analyst).")

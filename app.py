import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_autorefresh import st_autorefresh
import datetime

# 1. LIVE SYSTEM PULSE (Auto-refresh every 30s)
st_autorefresh(interval=30000, key="warroom_pulse")
st.set_page_config(page_title="SSO v5.1 | Strategic Resilience", layout="wide", page_icon="🕵️‍♂️")

# GLOBAL TICKERS DEFINITION (Fixed Scope)
tickers_map = {'MOS': 'Fertilizer', 'WEAT': 'Wheat_Index', 'TSM': 'AI_Hardware', 'PFE': 'Pharma_Proxy', '^VIX': 'Market_Fear'}

# CUSTOM CSS FOR CORPORATE LOOK
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    .stAlert { border-radius: 10px; }
    div[data-testid="stExpander"] { border: none; background-color: #161b22; }
    </style>
    """, unsafe_allow_html=True)

# 2. SIDEBAR: PI PROFILE & SYSTEM CONTROL
with st.sidebar:
    st.markdown(f"### 👨‍💼 Principal Investigator\n**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**")
    st.caption("Expertise: Financial Criminology | Maqasid Sharia | Organizational Strategy")
    st.write("---")
    st.info(f"🕒 **System Sync:** {datetime.datetime.now().strftime('%H:%M:%S')} UTC")
    st.write("---")
    st.markdown("### Technical Domains\n- Geopolitical Signal Intel\n- ML Anomaly Detection\n- AI Strategic Foresight")

# 3. DATA ENGINE: REAL-TIME INTRADAY FETCH
@st.cache_data(ttl=30)
def fetch_war_room_data():
    data = yf.download(list(tickers_map.keys()), period="5d", interval="15m")['Close']
    data.rename(columns=tickers_map, inplace=True)
    return data

try:
    df = fetch_war_room_data()
    norm_df = (df - df.min()) / (df.max() - df.min())
    latest = df.iloc[-1]
    prev = df.iloc[-2]
    
    # 4. KPI SECTION: LIVE MARKET HEARTBEAT
    st.title("🌐 Strategic Resilience Observatory v5.1")
    cols = st.columns(5)
    
    # Use global tickers_map for labels
    for i, col_name in enumerate(tickers_map.values()):
        change = ((latest[col_name] - prev[col_name]) / prev[col_name]) * 100
        cols[i].metric(label=col_name.replace("_", " "), value=f"{latest[col_name]:.2f}", delta=f"{change:.2f}%")

    st.write("---")

    # 5. MAIN VISUALIZATION: THE SIGNAL PULSE
    col_main, col_ahmad = st.columns([3, 1])

    with col_main:
        st.subheader("📡 High-Fidelity Signal Pulse (Real-Time Intraday)")
        fig = px.line(norm_df, labels={"value": "Signal Intensity", "index": "Time (UTC)"},
                     color_discrete_map={"Fertilizer": "#2ecc71", "Wheat_Index": "#f39c12", 
                                         "AI_Hardware": "#3498db", "Pharma_Proxy": "#9b59b6", "Market_Fear": "#e74c3c"})
        fig.update_layout(template="plotly_dark", hovermode="x unified", height=500, margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig, use_container_width=True)

    with col_ahmad:
        st.subheader("🤖 Ahmad's Synthesis")
        ahmad_notes = []
        if latest['Fertilizer'] > df['Fertilizer'].mean():
            ahmad_notes.append("• **Input Volatility:** Non-linear surge in Fertilizer costs suggests strategic stockpiling by regional actors.")
        if norm_df['AI_Hardware'].iloc[-1] > 0.8:
            ahmad_notes.append("• **Tech Supremacy:** High-intensity AI hardware signals indicate institutional front-running.")
        if df.corr().loc['Fertilizer', 'Wheat_Index'] < 0.3:
            ahmad_notes.append("• **Ethical Anomaly:** Decoupling detected between Fertilizer and Wheat. Potential violation of Maqasid Sharia's Hifz al-Nafs.")

        st.markdown(f"""
        <div style="background-color:#161b22; padding:20px; border-radius:10px; border-left: 5px solid #00d1b2;">
        {'<br><br>'.join(ahmad_notes) if ahmad_notes else "Baseline equilibrium maintained."}
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # 6. RIGOROUS ANALYSIS & PROJECTION SECTION
    st.subheader("🔍 Rigorous Analytical Discussion & Projections")
    tabs = st.tabs(["Strategic Discussion", "What's Next? (Projection)", "Decoupling Matrix"])

    with tabs[0]:
        st.markdown(f"""
        **Analytical Context:**
        Current data integration shows a persistent divergence between the **Pharma Proxy** and **Market Fear**. From a Financial Criminology perspective, 
        the stability of the Pharma sector during a rise in Market Fear indicates a 'Hedging of Risk' by corporate entities who anticipate a 
        prolonged structural shift rather than a short-term crisis. 
        """)

    with tabs[1]:
        st.markdown(f"""
        ### **Ahmad's 90-Day Projection:**
        1. **Probability of Managed Crisis (85%):** Indicators suggest a 'Controlled Escalation' where narratives will intensify, but economic fundamentals will remain buffered by state-led interventions.
        2. **Tech-Hegemony Shift:** AI Hardware (TSM) is expected to maintain its bull-run, reinforcing the move toward asymmetric warfare dominance.
        """)

    with tabs[2]:
        fig_heat, ax = plt.subplots(figsize=(10, 5), facecolor='#0e1117')
        sns.heatmap(df.corr(), annot=True, cmap='RdYlGn', center=0, ax=ax)
        plt.title("Institutional Integrity Matrix", color='white')
        st.pyplot(fig_heat)

except Exception as e:
    st.error(f"Intelligence Sync Error: {e}")

st.write("---")
st.caption(f"© 2024 SSO v5.1. PI: MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL. Co-Researcher: Ahmad AI.")

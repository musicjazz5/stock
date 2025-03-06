import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 設定頁面配置
st.set_page_config(page_title="股票分析儀表板", layout="wide")

# 標題
st.title("📊 股票分析儀表板")

# ========== 價格目標 & 情境分析 ==========
st.subheader("📈 價格目標 & 情境分析")

scenarios = pd.DataFrame({
    "Scenario": ["Bull Case", "Base Case", "Bear Case", "Current Price"],
    "Price ($)": [500, 250, 100, 280],  # 你可以根據最新數據調整
})

fig = px.bar(scenarios, x="Scenario", y="Price ($)", text="Price ($)", color="Scenario")
st.plotly_chart(fig, use_container_width=True)

# ========== 技術分析 ==========
st.subheader("📉 技術分析")

# 模擬股票價格趨勢
stock_data = pd.DataFrame({
    "Month": ["Jan", "Mar", "May", "Jul", "Sep", "Nov"],
    "Stock Price": [220, 250, 230, 290, 270, 280],
    "50-day SMA": [215, 240, 235, 270, 265, 275],
    "200-day SMA": [200, 210, 220, 230, 240, 250],
})

fig = go.Figure()
fig.add_trace(go.Scatter(x=stock_data["Month"], y=stock_data["Stock Price"], mode='lines+markers', name='Stock Price'))
fig.add_trace(go.Scatter(x=stock_data["Month"], y=stock_data["50-day SMA"], mode='lines', name='50-day SMA', line=dict(dash="dash")))
fig.add_trace(go.Scatter(x=stock_data["Month"], y=stock_data["200-day SMA"], mode='lines', name='200-day SMA', line=dict(dash="dot")))

st.plotly_chart(fig, use_container_width=True)

# 顯示技術指標
st.metric(label="RSI (14)", value="59.31", delta="Neutral")
st.metric(label="MACD", value="26.02", delta="Bullish")
st.metric(label="Key Support", value="$175.79")
st.metric(label="Key Resistance", value="$381.59")

# ========== 估值分析 ==========
st.subheader("📊 估值分析")
valuation_data = pd.DataFrame({
    "Scenario": ["Bull Case", "Base Case", "Bear Case", "Current Price"],
    "Price per Share ($)": [300, 200, 50, 280],
})

fig = px.bar(valuation_data, x="Scenario", y="Price per Share ($)", text="Price per Share ($)", color="Scenario")
st.plotly_chart(fig, use_container_width=True)

# 顯示估值指標
st.metric(label="P/E Ratio", value="80.2x", delta="Industry: 10.3x")
st.metric(label="P/S Ratio", value="9.3x", delta="Industry: 0.8x")
st.metric(label="EV/EBITDA", value="44.5x", delta="Industry: 8.2x")

# ========== 財務表現 ==========
st.subheader("💰 財務表現")

financials = pd.DataFrame({
    "Year": [2019, 2020, 2021, 2022, 2023],
    "Revenue ($B)": [24, 31, 53, 81, 90],
    "Net Income ($B)": [1, 2, 5, 7, 8],
})

fig = px.bar(financials, x="Year", y=["Revenue ($B)", "Net Income ($B)"], barmode="group")
st.plotly_chart(fig, use_container_width=True)

st.metric(label="Revenue CAGR (5Y)", value="42.3%")
st.metric(label="Gross Margin (2023)", value="19.0%")
st.metric(label="Operating Margin (2023)", value="9.6%")
st.metric(label="Net Margin (2023)", value="8.2%")

# ========== SWOT 分析 ==========
st.subheader("📌 SWOT 分析")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🟢 Strengths")
    st.write("- Brand Strength & Customer Loyalty")
    st.write("- Technology Leadership")
    st.write("- Manufacturing Scale & Efficiency")
    st.write("- Supercharger Network")
    st.write("- Software & OTA Updates")
    st.write("- Energy Business Integration")
    st.write("- Direct Sales Model")

with col2:
    st.markdown("### 🔴 Weaknesses")
    st.write("- Premium Pricing")
    st.write("- Limited Model Range")
    st.write("- Service Network Limitations")
    st.write("- Quality Control Issues")
    st.write("- Regulatory Challenges")
    st.write("- Executive Dependency")
    st.write("- Margin Pressure")

col3, col4 = st.columns(2)
with col3:
    st.markdown("### 🔵 Opportunities")
    st.write("- Global EV Market Growth")
    st.write("- Government Incentives")
    st.write("- Expansion into New Markets")
    st.write("- Autonomous Driving Development")

with col4:
    st.markdown("### 🟠 Threats")
    st.write("- Increased Competition")
    st.write("- Supply Chain Disruptions")
    st.write("- Regulatory Uncertainty")
    st.write("- Economic Downturns")

st.success("📌 這是一個基本的 Streamlit 股票分析儀表板，你可以根據需要修改數據和視覺化內容！")
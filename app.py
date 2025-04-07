import streamlit as st
import pandas as pd
from utils.ai_engine import get_ai_insight

# Load data
portfolio = pd.read_csv('data/portfolio.csv')
credit = pd.read_csv('data/credit_watchlist.csv')

# Sidebar
st.sidebar.title("AI Risk Analyst")
section = st.sidebar.radio("Navigate", ["Dashboard", "Credit Risk", "Scenarios", "Compliance"])

# Dashboard
if section == "Dashboard":
    st.title("Market Risk Dashboard")
    st.metric("Portfolio VaR", "18%", delta="+3.2%")
    st.metric("Downgrade Alerts", "3 Issuers")
    st.metric("Limit Breaches", "1 Active")

    st.subheader("AI Risk Insight")
    prompt = "Summarize today's main risk drivers based on VaR and exposure data."
    ai_text = get_ai_insight(prompt)
    st.write(ai_text)

# Credit Risk Watchlist
elif section == "Credit Risk":
    st.title("Credit Risk Watchlist")
    st.dataframe(credit)

# Scenario Analysis
elif section == "Scenarios":
    st.title("Macro Scenario Simulator")
    scenario = st.selectbox("Select a scenario", ["Fed Hike +50bps", "China Slowdown", "Oil Shock"])
    st.write(f"Simulated impact of {scenario} coming soon...")

# Compliance
elif section == "Compliance":
    st.title("Compliance Alerts")
    st.warning("Limit breach: EM exposure exceeds 25%")
    st.info("AI Audit Trail: Exposure rose due to Brazil HY bond spike")

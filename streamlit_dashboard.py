import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Path Ledger - Content Money Machine", layout="wide")
st.title("🚀 Path Ledger Content Money Machine")

st.success("✅ System Live • Path Ledger Active")

st.metric("Active Brand", "Path Ledger", "Personal Finance")
st.metric("Total Est. Monthly Revenue", "$0 — Building momentum")

st.subheader("Recent Activity")
st.write("Last content generation:", datetime.now().strftime("%Y-%m-%d"))

st.caption("Educational content only. Not financial advice. Dashboard refreshes automatically.")

import streamlit as st
import os
from datetime import datetime

st.set_page_config(page_title="Path Ledger", layout="wide")
st.title("🚀 Path Ledger - Content Money Machine")

st.success("✅ App is successfully deployed and running!")

st.write("**Time:**", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if os.getenv("GROQ_API_KEY"):
    st.success("✅ GROQ Key is correctly loaded")
else:
    st.error("❌ GROQ_API_KEY not found. Check Railway Variables.")

st.info("✅ This is the minimal working version. We'll add full content generation next.")

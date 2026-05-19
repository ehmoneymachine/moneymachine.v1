import streamlit as st
import os
from datetime import datetime

st.set_page_config(page_title="Path Ledger", layout="wide")
st.title("🚀 Path Ledger - Content Money Machine")

st.success("✅ App is Running on Railway!")

st.write("Current Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if os.getenv("GROQ_API_KEY"):
    st.success("✅ GROQ Key is loaded correctly")
else:
    st.error("❌ GROQ_API_KEY is missing - check Railway Variables")

st.info("Test successful! Next step is adding content generation.")

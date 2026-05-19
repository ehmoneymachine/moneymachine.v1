import streamlit as st
import os
from datetime import datetime
from groq import Groq

st.set_page_config(page_title="Path Ledger", layout="wide")
st.title("🚀 Path Ledger - Content Money Machine")
st.success("✅ App is Running Successfully on Railway!")

st.write("**Current Time:**", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Check API Key
if os.getenv("GROQ_API_KEY"):
    st.success("✅ GROQ Key Loaded")
else:
    st.error("❌ GROQ_API_KEY is missing")

# Content Generation Button
if st.button("🟢 Generate New Path Ledger Script", type="primary"):
    with st.spinner("Generating educational finance content..."):
        try:
            groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
            response = groq.chat.completions.create(
                messages=[{
                    "role": "user", 
                    "content": "Write a clear, educational 5-7 minute script for Path Ledger about beginner budgeting in 2026. Use a calm, trustworthy tone. End with a strong disclaimer: This is educational only, not financial advice."
                }],
                model="llama3-70b-8192"
            )
            script = response.choices[0].message.content
            st.success("✅ Script Generated!")
            st.write(script)
        except Exception as e:
            st.error(f"Error generating script: {e}")

st.caption("Path Ledger • Educational Personal Finance Content")

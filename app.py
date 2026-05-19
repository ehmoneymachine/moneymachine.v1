import streamlit as st
import os
from datetime import datetime
from groq import Groq

st.set_page_config(page_title="Path Ledger", layout="wide")
st.title("🚀 Path Ledger - Content Money Machine")

st.success("✅ Connected to Railway")

# Check keys
if os.getenv("GROQ_API_KEY"):
    st.success("✅ GROQ Key Detected")
else:
    st.error("❌ GROQ_API_KEY not found in Railway Variables")

if st.button("Generate Test Script"):
    try:
        groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
        response = groq.chat.completions.create(
            messages=[{"role": "user", "content": "Write a short educational script on budgeting for Path Ledger. Include disclaimer."}],
            model="llama3-70b-8192"
        )
        st.write(response.choices[0].message.content)
    except Exception as e:
        st.error(f"Error: {str(e)}")

st.caption("Path Ledger Dashboard • " + datetime.now().strftime("%Y-%m-%d %H:%M"))

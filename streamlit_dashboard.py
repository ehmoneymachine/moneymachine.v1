import streamlit as st
import os
from datetime import datetime
from groq import Groq
from elevenlabs.client import ElevenLabs

st.set_page_config(page_title="Path Ledger Dashboard", layout="wide")
st.title("🚀 Path Ledger - Content Money Machine")

# === Secure API Key Check ===
groq_key = os.getenv("GROQ_API_KEY")
eleven_key = os.getenv("ELEVENLABS_API_KEY")

if not groq_key:
    st.error("❌ GROQ_API_KEY is missing. Add it in Railway Variables tab.")
    st.stop()

if not eleven_key:
    st.warning("⚠️ ELEVENLABS_API_KEY is missing (optional for now).")

st.success("✅ All keys detected!")

# Initialize clients safely
groq = Groq(api_key=groq_key)
eleven = ElevenLabs(api_key=eleven_key) if eleven_key else None

st.metric("Active Brand", "Path Ledger", "Personal Finance")

if st.button("🟢 Generate New Path Ledger Content", type="primary"):
    with st.spinner("Generating educational script..."):
        try:
            response = groq.chat.completions.create(
                messages=[{"role": "user", "content": "Write a clear, educational 5-7 minute script on beginner budgeting in 2026 for Path Ledger. Calm tone. End with strong disclaimer."}],
                model="llama3-70b-8192"
            )
            script = response.choices[0].message.content
            st.success("✅ Script Generated Successfully!")
            st.write(script)
        except Exception as e:
            st.error(f"Error: {e}")

st.caption("Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M"))

import streamlit as st
import os
from groq import Groq
from elevenlabs.client import ElevenLabs

st.title("Path Ledger - Content Engine")

groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
eleven = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

if st.button("🟢 Generate Path Ledger Content Now"):
    with st.spinner("Creating educational finance script..."):
        response = groq.chat.completions.create(
            messages=[{"role": "user", "content": "Write a clear, educational 5-7 minute script about beginner budgeting in 2026 for Path Ledger. Use calm, trustworthy tone. End with strong disclaimer: This is educational only, not financial advice."}],
            model="llama3-70b-8192"
        )
        script = response.choices[0].message.content
        st.success("✅ Script Generated for Path Ledger!")
        st.write(script)

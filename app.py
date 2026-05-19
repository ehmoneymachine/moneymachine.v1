from flask import Flask, request
import os
from datetime import datetime
from groq import Groq

app = Flask(__name__)

@app.route("/")
def home():
    groq_status = "✅ Loaded" if os.getenv("GROQ_API_KEY") else "❌ Missing"
    
    html = f"""
    <h1>🚀 Path Ledger - Content Money Machine</h1>
    <p><strong>Status:</strong> Running Successfully on Railway</p>
    <p><strong>Time:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    <p><strong>GROQ Key:</strong> {groq_status}</p>
    <hr>
    <h2>Test Content Generation</h2>
    <p>Click the button below to generate a sample script (this will be expanded later).</p>
    """
    return html

@app.route("/generate")
def generate():
    try:
        groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
        response = groq.chat.completions.create(
            messages=[{"role": "user", "content": "Write a short educational script for Path Ledger about beginner budgeting in 2026. Calm tone. Include disclaimer: This is educational only, not financial advice."}],
            model="llama3-70b-8192"
        )
        script = response.choices[0].message.content
        return f"<h2>Generated Script:</h2><p>{script}</p><p><a href='/'>← Back</a></p>"
    except Exception as e:
        return f"<h2>Error:</h2><p>{str(e)}</p><p><a href='/'>← Back</a></p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

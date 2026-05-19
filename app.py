from flask import Flask
import os
from datetime import datetime
from groq import Groq

app = Flask(__name__)

@app.route("/")
def dashboard():
    return f"""
    <html>
    <head>
        <title>Path Ledger Dashboard</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 0; padding: 40px; background: #0f172a; color: #e2e8f0; }}
            h1 {{ color: #60a5fa; }}
            .card {{ background: #1e2937; padding: 25px; border-radius: 12px; margin: 20px 0; }}
            button {{ padding: 15px 30px; font-size: 18px; background: #3b82f6; color: white; border: none; border-radius: 8px; cursor: pointer; }}
            button:hover {{ background: #2563eb; }}
        </style>
    </head>
    <body>
        <h1>🚀 Path Ledger - Content Money Machine</h1>
        <p><strong>Status:</strong> LIVE • {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        
        <div class="card">
            <h2>Path Ledger (Personal Finance)</h2>
            <p><strong>GROQ Status:</strong> ✅ Loaded</p>
        </div>

        <div class="card">
            <h2>Generate Educational Content</h2>
            <a href="/generate"><button>Generate New Script Now</button></a>
            <p style="margin-top:10px; color:#94a3b8;">Click the button to create a new finance script</p>
        </div>

        <p style="color:#64748b; margin-top: 40px;">
            Educational content only • Not financial advice
        </p>
    </body>
    </html>
    """

@app.route("/generate")
def generate():
    try:
        groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
        response = groq.chat.completions.create(
            messages=[{
                "role": "user", 
                "content": "Write a clear, educational 5-7 minute script for Path Ledger about beginner budgeting in 2026. Use calm, trustworthy tone. End with strong disclaimer: This is educational only, not financial advice."
            }],
            model="llama3-70b-8192"
        )
        script = response.choices[0].message.content.replace("\n", "<br><br>")
        
        return f"""
        <h1>✅ Generated Script for Path Ledger</h1>
        <div style="background:#1e2937; padding:25px; border-radius:12px; line-height:1.6;">
            {script}
        </div>
        <p><a href="/">← Back to Dashboard</a></p>
        """
    except Exception as e:
        return f"<h2>Error Generating Script</h2><p>{str(e)}</p><a href='/'>← Back to Dashboard</a>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

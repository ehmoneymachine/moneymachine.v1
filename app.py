from flask import Flask, request
import os
from datetime import datetime
from groq import Groq

app = Flask(__name__)

@app.route("/")
def dashboard():
    groq_status = "✅ Loaded" if os.getenv("GROQ_API_KEY") else "❌ Missing"
    
    html = f"""
    <html>
    <head><title>Path Ledger Dashboard</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #0f172a; color: #e2e8f0; }}
        h1 {{ color: #60a5fa; }}
        .card {{ background: #1e2937; padding: 20px; border-radius: 12px; margin: 15px 0; }}
        button {{ padding: 12px 24px; font-size: 16px; background: #3b82f6; color: white; border: none; border-radius: 8px; cursor: pointer; }}
    </style>
    </head>
    <body>
        <h1>🚀 Path Ledger - Content Money Machine</h1>
        <p><strong>Status:</strong> Running on Railway • {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
        
        <div class="card">
            <h2>Path Ledger (Personal Finance)</h2>
            <p><strong>GROQ Status:</strong> {groq_status}</p>
        </div>

        <div class="card">
            <h2>Generate New Content</h2>
            <a href="/generate"><button>Generate Educational Script</button></a>
        </div>

        <p style="color:#94a3b8; margin-top: 30px;">
            Educational content only. Not financial advice.<br>
            This is your live dashboard.
        </p>
    </body>
    </html>
    """
    return html


@app.route("/generate")
def generate():
    try:
        groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
        response = groq.chat.completions.create(
            messages=[{
                "role": "user",
                "content": "Write a clear, educational 5-7 minute script for Path Ledger about beginner budgeting in 2026. Calm, trustworthy tone. End with strong disclaimer."
            }],
            model="llama3-70b-8192"
        )
        script = response.choices[0].message.content.replace("\n", "<br>")
        
        return f"""
        <h1>✅ Generated Script</h1>
        <div style="background:#1e2937; padding:20px; border-radius:12px; white-space: pre-wrap;">
            {script}
        </div>
        <p><a href="/">← Back to Dashboard</a></p>
        """
    except Exception as e:
        return f"<h2>Error:</h2><p>{str(e)}</p><p><a href='/'>← Back</a></p>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

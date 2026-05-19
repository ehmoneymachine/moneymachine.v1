from flask import Flask
import os
from datetime import datetime
from groq import Groq

app = Flask(__name__)

@app.route("/")
def dashboard():
    return f"""
    <html>
    <head><title>Path Ledger Dashboard</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #0f172a; color: #e2e8f0; }}
        h1 {{ color: #60a5fa; }}
        .card {{ background: #1e2937; padding: 25px; border-radius: 12px; margin: 20px 0; }}
        button {{ padding: 15px 30px; font-size: 18px; background: #3b82f6; color: white; border: none; border-radius: 8px; }}
    </style>
    </head>
    <body>
        <h1>🚀 Path Ledger - Content Money Machine</h1>
        <p><strong>Status:</strong> LIVE & UPDATED</p>
        <p><strong>Time:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        
        <div class="card">
            <h2>Path Ledger (Personal Finance)</h2>
            <p>GROQ Status: ✅ Loaded</p>
        </div>

        <div class="card">
            <h2>Generate Content</h2>
            <a href="/generate"><button>Generate New Educational Script</button></a>
        </div>
    </body>
    </html>
    """

@app.route("/generate")
def generate():
    try:
        groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
        response = groq.chat.completions.create(
            messages=[{"role": "user", "content": "Write a clear educational script for Path Ledger about beginner budgeting in 2026. Calm tone. Include disclaimer."}],
            model="llama3-70b-8192"
        )
        script = response.choices[0].message.content.replace("\n", "<br><br>")
        return f"<h2>✅ Generated Script</h2><div style='background:#1e2937;padding:20px;border-radius:10px;'>{script}</div><br><a href='/'>← Back to Dashboard</a>"
    except Exception as e:
        return f"<h2>Error:</h2><p>{str(e)}</p><a href='/'>← Back</a>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

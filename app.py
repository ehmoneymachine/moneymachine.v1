from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>🚀 Path Ledger - Content Money Machine</h1>
    <p>✅ App is running successfully on Railway!</p>
    <p>Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    <p>GROQ Key Loaded: {'✅ Yes' if os.getenv("GROQ_API_KEY") else '❌ No'}</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

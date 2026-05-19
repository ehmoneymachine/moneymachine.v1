import os
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Path Ledger – Content Money Machine</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0A2540;
      color: #f0f4f8;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 2rem;
    }}
    .card {{
      background: #112240;
      border: 1px solid #1e3a5f;
      border-radius: 12px;
      padding: 2.5rem 3rem;
      max-width: 560px;
      width: 100%;
      box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    }}
    h1 {{ font-size: 1.75rem; color: #D4AF37; margin-bottom: 0.5rem; }}
    .badge {{
      display: inline-block;
      background: #0d3b2e;
      color: #4ade80;
      border: 1px solid #166534;
      border-radius: 999px;
      font-size: 0.8rem;
      padding: 0.2rem 0.75rem;
      margin-bottom: 1.5rem;
    }}
    .row {{ margin-bottom: 0.75rem; font-size: 0.95rem; }}
    .label {{ color: #94a3b8; margin-right: 0.4rem; }}
    .value {{ color: #e2e8f0; }}
    .ok  {{ color: #4ade80; }}
    .err {{ color: #f87171; }}
    footer {{
      margin-top: 2rem;
      font-size: 0.78rem;
      color: #475569;
      border-top: 1px solid #1e3a5f;
      padding-top: 1rem;
    }}
  </style>
</head>
<body>
  <div class="card">
    <h1>🚀 Path Ledger</h1>
    <span class="badge">✅ HTTP server is running</span>

    <div class="row">
      <span class="label">Time:</span>
      <span class="value">{timestamp}</span>
    </div>
    <div class="row">
      <span class="label">Port:</span>
      <span class="value">{port}</span>
    </div>
    <div class="row">
      <span class="label">GROQ_API_KEY:</span>
      <span class="{groq_class}">{groq_status}</span>
    </div>

    <footer>Minimal HTTP layer is live. Streamlit UI will be layered on once networking is verified.</footer>
  </div>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        logger.info("REQUEST %s - %s", self.address_string(), fmt % args)

    def do_GET(self):
        groq_key = os.environ.get("GROQ_API_KEY")
        groq_ok = bool(groq_key)

        body = HTML_TEMPLATE.format(
            timestamp=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
            port=PORT,
            groq_class="ok" if groq_ok else "err",
            groq_status="✅ Loaded" if groq_ok else "❌ Missing – set GROQ_API_KEY in Railway Variables",
        ).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    logger.info("Listening on 0.0.0.0:%d", PORT)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Shutting down")
        server.server_close()

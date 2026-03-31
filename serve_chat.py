"""
serve_chat.py — Serves chat.html on http://localhost:3000
Run this AFTER uvicorn is already running on port 8000.

    python serve_chat.py
"""
import http.server
import socketserver
import os
import webbrowser
import threading

PORT = 3000
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def log_message(self, format, *args):
        pass  # silence request logs

def open_browser():
    import time
    time.sleep(0.5)
    webbrowser.open(f"http://localhost:{PORT}/chat.html")

print(f"✅ Serving chat.html at http://localhost:{PORT}/chat.html")
print("   Press Ctrl+C to stop.\n")

threading.Thread(target=open_browser, daemon=True).start()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()




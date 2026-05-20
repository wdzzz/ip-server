import http.server
import urllib.request
import threading
import time

EXTERNAL_IP = None
LAST_FETCH = 0
CACHE_TTL = 300  # 5 min cache

def fetch_external_ip():
    global EXTERNAL_IP, LAST_FETCH
    now = time.time()
    if EXTERNAL_IP and now - LAST_FETCH < CACHE_TTL:
        return EXTERNAL_IP
    try:
        req = urllib.request.urlopen("http://checkip.amazonaws.com", timeout=10)
        EXTERNAL_IP = req.read().decode().strip()
        LAST_FETCH = now
    except Exception:
        if not EXTERNAL_IP:
            EXTERNAL_IP = "0.0.0.0"
    return EXTERNAL_IP

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        ip = fetch_external_ip()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(ip.encode())

    def log_message(self, format, *args):
        pass  # keep logs clean

if __name__ == "__main__":
    port = 5056
    srv = http.server.HTTPServer(("0.0.0.0", port), Handler)
    srv.serve_forever()

"""Dev-only static server with a /save/<name> POST endpoint so the Browser
pane can persist a screenshot data URL to disk. Not part of the shipped
feature -- used only to capture tier-2 evidence for this task."""

import base64
import http.server
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS = os.path.abspath(os.path.join(ROOT, "..", ".artifacts", "web-ui-evidence-demo1"))
os.makedirs(ARTIFACTS, exist_ok=True)


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_POST(self):
        if not self.path.startswith("/save/"):
            self.send_response(404)
            self.end_headers()
            return
        name = os.path.basename(self.path[len("/save/"):])
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        prefix = "data:image/png;base64,"
        if body.startswith(prefix):
            body = body[len(prefix):]
        data = base64.b64decode(body)
        out_path = os.path.join(ARTIFACTS, name)
        with open(out_path, "wb") as f:
            f.write(data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"saved {len(data)} bytes to {out_path}".encode("utf-8"))


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8743
    http.server.HTTPServer(("localhost", port), Handler).serve_forever()

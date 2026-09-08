"""Dev-only static server with a /save/<name> POST endpoint so the Browser
pane can persist a screenshot data URL to disk. Not part of the shipped
feature -- used only to capture tier-2 evidence for this task."""

import base64
import binascii
import http.server
import os
import sys
from urllib.parse import urlsplit

ROOT = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS = os.path.abspath(os.path.join(ROOT, "..", ".artifacts", "web-ui-evidence-demo1"))
os.makedirs(ARTIFACTS, exist_ok=True)

# Screenshots from this page are well under 1MB as PNG; 10MB base64-encoded
# is generous headroom without leaving the read effectively unbounded.
MAX_UPLOAD_BYTES = 10 * 1024 * 1024


class Handler(http.server.SimpleHTTPRequestHandler):
    """Same-origin only: the page and this server share localhost:<port>,
    so no CORS headers are needed and none are sent."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        super().end_headers()

    def _respond(self, code, message):
        self.send_response(code)
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def do_POST(self):
        path = urlsplit(self.path).path
        if not path.startswith("/save/"):
            self.send_response(404)
            self.end_headers()
            return
        name = os.path.basename(path[len("/save/"):])
        if not name:
            self._respond(400, "missing filename")
            return
        raw_length = self.headers.get("Content-Length")
        if raw_length is None or not raw_length.isdigit():
            self._respond(400, "missing or invalid Content-Length")
            return
        length = int(raw_length)
        if length == 0 or length > MAX_UPLOAD_BYTES:
            self._respond(400, f"Content-Length must be 1..{MAX_UPLOAD_BYTES} bytes")
            return
        body = self.rfile.read(length).decode("utf-8")
        prefix = "data:image/png;base64,"
        if body.startswith(prefix):
            body = body[len(prefix):]
        try:
            data = base64.b64decode(body, validate=True)
        except binascii.Error as e:
            self._respond(400, f"invalid base64 body: {e}")
            return
        out_path = os.path.join(ARTIFACTS, name)
        with open(out_path, "wb") as f:
            f.write(data)
        self._respond(200, f"saved {len(data)} bytes to {out_path}")


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8743
    http.server.HTTPServer(("localhost", port), Handler).serve_forever()

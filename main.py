from __future__ import annotations

import http.server
import os
import socketserver
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
WEB_ROOT = PROJECT_ROOT / "web"
PORT = int(os.environ.get("PORT", "8000"))


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def run() -> None:
    if not WEB_ROOT.exists():
        raise SystemExit("The 'web' directory does not exist. Build the app assets first.")

    handler = lambda *args, **kwargs: http.server.SimpleHTTPRequestHandler(  # noqa: E731
        *args,
        directory=str(WEB_ROOT),
        **kwargs,
    )

    with ReusableTCPServer(("", PORT), handler) as httpd:
        print(f"Structural Math Calculator available at http://localhost:{PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    run()

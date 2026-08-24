"""Local dev server for the deck that disables all caching, so every edit
shows up on a plain reload instead of requiring a hard refresh."""
import http.server
import functools


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == "__main__":
    handler = functools.partial(NoCacheHandler, directory=".")
    port = 8000
    print(f"Serving on http://localhost:{port} (no-cache)")
    http.server.HTTPServer(("", port), handler).serve_forever()

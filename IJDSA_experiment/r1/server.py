"""Only four HTML endpoints; gold, directory listings and other paths are never served."""
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.parse import urlsplit, unquote
from .common import ROOT

class SnapshotHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = unquote(urlsplit(self.path).path)
        allowed = {f'/{s}/{suffix}':ROOT/'snapshots'/s/'index.html' for s in ('site_01','site_02','site_03','site_04') for suffix in ('','index.html')}
        if path not in allowed:
            self.send_error(404); return
        data = allowed[path].read_bytes()
        self.send_response(200)
        self.send_header('Content-Type','text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control','no-store')
        self.send_header('Content-Security-Policy', "default-src 'none'; script-src 'none'; style-src 'unsafe-inline'; img-src data:; font-src data:; connect-src 'none'; frame-src 'none'; base-uri 'none'; form-action 'none'")
        self.end_headers()
        self.wfile.write(data)
    def log_message(self,*args): pass

@contextmanager
def serve(port=8000):
    server = ThreadingHTTPServer(('127.0.0.1', port), SnapshotHandler)
    thread = Thread(target=server.serve_forever, daemon=True); thread.start()
    try: yield f'http://127.0.0.1:{server.server_port}'
    finally:
        server.shutdown(); server.server_close(); thread.join(timeout=3)

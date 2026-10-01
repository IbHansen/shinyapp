"""Serve site/ locally with the file types Shinylive needs.

Plain "python -m http.server" takes the types from the Windows registry, which
can give .js as text/plain; the browser then refuses to run Shinylive.
"""
import functools
import http.server
import webbrowser
from pathlib import Path

PORT = 8008
SITE = Path(__file__).parent / 'site'


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        '.js': 'text/javascript',
        '.mjs': 'text/javascript',
        '.wasm': 'application/wasm',
        '.json': 'application/json',
        '.css': 'text/css',
        '.html': 'text/html',
    }


if __name__ == '__main__':
    if not SITE.exists():
        raise SystemExit(f'{SITE} does not exist, run build.cmd first')
    server = http.server.ThreadingHTTPServer(('localhost', PORT), functools.partial(Handler, directory=str(SITE)))
    url = f'http://localhost:{PORT}/'
    print(f'Serving {SITE} on {url}  (Ctrl+C to stop)')
    webbrowser.open(url)
    server.serve_forever()

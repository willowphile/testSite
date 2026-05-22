import http.server
import json
import re
from pathlib import Path

SKIP = {'index.html', 'navbar.html'}

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/files':
            files = []
            for f in sorted(Path('.').glob('*.html')):
                if f.name in SKIP:
                    continue
                label = f.name
                try:
                    content = f.read_text(encoding='utf-8', errors='ignore')
                    match = re.search(r'<title[^>]*>([^<]+)</title>', content, re.IGNORECASE)
                    if match:
                        t = match.group(1).strip()
                        if t and t != 'Page Title':
                            label = t
                except Exception:
                    pass
                files.append({'href': f.name, 'label': label})

            body = json.dumps(files).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            super().do_GET()

    def log_message(self, fmt, *args):
        pass  # suppress request noise

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    print(f'Serving at http://localhost:{port}')
    http.server.test(HandlerClass=Handler, port=port, bind='localhost')

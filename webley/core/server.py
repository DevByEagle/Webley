from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from typing import Dict, Any
from webley.http import HttpRequest, HttpResponse

ROUTES: Dict[str, Any] = {}

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        request = HttpRequest()
        # Automatically populate HttpRequest fields
        request.path = urlparse(self.path).path
        request.method = self.command
        
        handler_func = ROUTES.get(request.path)
        if handler_func:
            response = handler_func(request) # user returns HttpResponse
        else:
            response = HttpResponse(b"<h1>404 Not Found</h1>", status_code=404)
        response.send(self)

def route(path):
    def decorator(func):
        ROUTES[path] = func
        return func
    return decorator

def run(address="127.0.0.1", port=8000):
    server = HTTPServer((address, port), ServerHandler)
    print(f"Server running at http://{address}:{port}")
    server.serve_forever()

__all__ = [
    "route",
    "run"
]
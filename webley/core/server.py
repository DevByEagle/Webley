from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Callable, Dict
from urllib.parse import urlparse
from webley.http import HttpRequest, HttpResponse

ROUTES: Dict[str, Callable[[HttpRequest], HttpResponse]] = {}

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        request = HttpRequest()
        request.path = urlparse(self.path).path
        request.method = self.command

        handler_func = ROUTES.get(request.path)
        if handler_func:
            response = handler_func(request)
        else:
            response = HttpResponse(
                b"<h1>404 Not Found</h1>", status_code=404
            )
        
        response.send(self)

def route(path: str):
    def decorator(func: Callable[[HttpRequest], HttpResponse]) -> Callable:
        ROUTES[path] = func
        return func
    return decorator

def run(address="127.0.0.1", port=8000):
    server = HTTPServer((address, port), ServerHandler)
    print(f"Server running at http://{address}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()

__all__ = ["route", "run"]
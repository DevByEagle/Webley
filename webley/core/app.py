from typing import Any, Callable, Dict
from wsgiref.simple_server import make_server
from webley.router import Router
from webley.http import HttpRequest, HttpResponse

class Webley:
    def __init__(self):
        self.router = Router()

    def route(self, path: str):
        def decorator(func: Callable[[HttpRequest], HttpResponse]):
            self.router.add_route(path, func)
            return func
        return decorator
    
    def _handle_request(self, raw: Dict[str, Any]) -> HttpResponse:
        request = HttpRequest()
        request.path = raw.get("path", "")
        request.method = raw.get("method", "GET")

        handler = self.router.get_handler(request.path)
        if handler:
            response = handler(request)
        else:
            response = HttpResponse(b"<h1>404 Not Found</h1>", status_code=404)
        return response
    
    def run(self, host='127.0.0.1', port=8000):
        def wsgi_app(environ, start_response):
            raw = {
                "method": environ["REQUEST_METHOD"],
                "path": environ["PATH_INFO"],
                "headers": {k: v for k, v in environ.items()},
                "body": environ["wsgi.input"].read(),
            }
            response = self._handle_request(raw)
            # start_response(
            #     str(response.status_code),
            #     list(response.headers.items())
            # )
            return [response.content]

        server = make_server(host, port, wsgi_app)
        print(f"Running on http://{host}:{port}")
        server.serve_forever()
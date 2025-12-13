from typing import Any, Callable, Dict
from wsgiref.simple_server import make_server

from webley.router import Router
from webley.http import HttpRequest, HttpResponse

class Webley:
    def __init__(self):
        self.router = Router()

    def route(self, path: str, *, method: str = "GET"):
        def decorator(func: Callable[[HttpRequest], HttpResponse]):
            self.router.add(
                path=path,
                handler=func,
                method=method,
            )
            return func
        return decorator
    
    def _handle_request(self, raw: Dict[str, Any]) -> HttpResponse:
        request = HttpRequest()
        
        try:
            handler, params = self.router.resolve(
                request.path,
                request.method
            )

            response = handler(request)
        
        except LookupError:
            response = HttpResponse(
                b"<h1>404 Not Found</h1>",
                status_code=404
            )
        
        except Exception as exc:
            response = HttpResponse(
                f"<h1>500 Internal Server Error</h1><pre>{exc}</pre>".encode(),
                status_code=500,
                )
        
        return response

    def run(self):
        pass
from wsgiref import simple_server

from webley.core.router import Router
from webley.http import HttpRequest, HttpResponse

class Webley:
    def __init__(self):
        self._router = Router()

    def route(self, path: str):
        def decorator(func):
            self._router.add(path, func)
            return func
        return decorator

    def __call__(self, environ=None, start_response=None):
        if environ is None or start_response is None:
            raise RuntimeError(
                "Direct calls to Webley instances are not allowed. Use run() instead."
            )
        
        req = HttpRequest()
        req.path = environ.get("PATH_INFO", "/")
        req.method = environ.get("REQUEST_METHOD", "GET")

        try:
            handler, params = self._router.resolve(req.path, req.method)
            req.content_params = params
            res = handler(req)
        except Exception as err:
            res = HttpResponse(f"{err}") # Just for now
        
        start_response(res._get_status_code_as_string(), list(res.headers.items()))
        return [res.content]

    def run(self, host="127.0.0.1", port=8000):
        try:
            with simple_server.make_server(host, port, self) as server:
                print(f"Running on http://{host}:{port}")
                server.serve_forever()
        except Exception as err:
            return

__all__ = ["Webley"]
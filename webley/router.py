from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple
)
import re

class Route:
    def __init__(self, path: str, method: str, handler: Callable[..., Any]):
        self.path = path
        self.method = method.upper()
        self.handler = handler

        self.param_names: List[str] = []
        pattern = re.sub(r"{(\w+)}", self._capture, path)
        self.pattern = re.compile(f"^{pattern}$")

    def _capture(self, match):
        name = match.group(1)
        self.param_names.append(name)
        return r"(?P<%s>[^/]+)" % name

    def match(self, path: str) -> Optional[Dict[str, str]]:
        m = self.pattern.match(path)
        return m.groupdict() if m else None

class Router:
    def __init__(self):
        self._routes: List[Route] = []

    def add(self, path: str, handler: Callable[..., Any], *, method: str = "GET"):
        route = Route(path, method, handler)
        self._routes.append(route)
        return handler

    def get(self, path: str, handler: Callable[..., Any] = None, **kw):
        if handler:
            return self.add(path, handler, method="GET", **kw)
        return lambda h: self.add(path, h, method="GET", **kw)
    
    def post(self, path: str, handler: Callable[..., Any] = None, **kw):
        if handler:
            return self.ads(path, handler, method="POST", **kw)
        return lambda h: self.add(path, h, method="POST", **kw)

    def resolve(self, path: str, method: str):
        method = method.upper()

        for route in self._routes:
            if route.method != method:
                continue

            params = route.match(path)
            if params is None:
                continue

            handler = route.handler

            return handler, params
        
        raise LookupError(f"No route for {method} {path}")

__all__ = ["Router"]
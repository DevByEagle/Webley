import re
from typing import Any, Callable, Dict, List, Optional, Tuple

from webley.http import HttpResponse

class Route:
    def __init__(self, path: str, method: str, handler: Callable[..., HttpResponse]):
        self.path = path
        self.method = method.upper()
        self.handler = handler

        self.param_names: List[str] = re.findall(r"{(\w+)}", path)
        pattern = re.sub(r"{\w+}", r"([^/]+)", path)
        self.pattern = re.compile(f"^{pattern}$")

    def match(self, path: str) -> Optional[Dict[str, str]]:
        """Return a dict of parameters if path matches, else None."""
        match = self.pattern.match(path)
        if not match:
            return None
        return {name: value for name, value in zip(self.param_names, match.groups())}

class Router:
    def __init__(self):
        self._routes: List[Route] = []

    def add(self, path: str, handler: Callable[..., HttpResponse], *, method: str = "GET"):
        route = Route(path, method, handler)
        self._routes.append(route)
    
    def resolve(self, path: str, method: str) -> Tuple[Optional[Callable[..., HttpResponse]], Optional[Dict[str, str]]]:
        method = method.upper()
        for route in self._routes:
            if route.method != method:
                continue
            params = route.match(path)
            if params is not None:
                return route.handler, params
        return None, None

__all__ = ['Router']
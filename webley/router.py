from typing import Dict, Callable

class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, func):
        self.routes[path] = func
    
    def get_handler(self, path):
        return self.routes.get(path)
    
__all__ = [
    'Router'
]
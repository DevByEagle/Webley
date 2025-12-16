from wsgiref import simple_server
from typing import Optional, Protocol

from webley.http import HttpRequest, HttpResponse

class AppConfig(Protocol):
    DEBUG: bool = False

class Webley:
    def __init__(self, *, config: Optional[AppConfig] = None):
        self.config = config

    def route(self, path: str):
        pass

    def run(self, host, port):
        pass

__all__ = [
    'AppConfig',
    'Webley'
]
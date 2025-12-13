from typing import (
    Any,
    Callable,
    Dict
)
import re

class Route:
    def __init__(self, path: str, method: str):
        self.path = path
        self.method = method.upper()

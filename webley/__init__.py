"""
"""

__version__ = "1.1.0.dev0"

from . import core
from .core import (
    AppConfig,
    Webley
)

from . import http
from .http import HttpRequest, HttpResponse

__all__ = list(
    {"exceptions", "http"} |
    set(core.__all__) |
    {"__version__"}
)

def __getattr__(attr):
    pass

def __dir__():
    pass

# Clean up namespace and remove standard library and package references.
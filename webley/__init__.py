"""
"""

__version__ = "1.1.0"

from .core.app import Webley

from . import auth
# from .auth import ()

from . import http
# from .http import ()

from . import router
from .router import Router

__all__ = list(
    {"auth", "http", "router"} |
    set(http.__all__)
)

def __getattr__(attr):
    pass

# Clean up namespace and remove standard library and package references.

"""
"""
import warnings

__version__ = "1.1.0.dev0"

from . import http

__all__ = list(
    {"http"} |
    set(http.__all__) |
    {"__version__"}
)


def __getattr__(attr):
    if attr == "http":
        import webley.http as http
        return http
    raise AttributeError(f"module {__name__!r} has no attribute {attr!r}")

def __dir__():
    pass

# Clean up namespace and remove standard library and package references.
del warnings
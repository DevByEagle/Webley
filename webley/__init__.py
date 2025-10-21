"""
"""
import warnings

__version__ = "1.1.0.dev0"

__all__ = list(
    {"__version__"}
)

def __getattr__(attr):
    if attr == "http":
        pass
    raise AttributeError(f"module {__name__!r} has no attribute {attr!r}")

def __dir__():
    pass

# Clean up namespace and remove standard library and package references.
del warnings
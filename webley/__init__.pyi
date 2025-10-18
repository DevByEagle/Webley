from typing import Final, LiteralString

from webley import (
    http
)

from webley.core.server import (
    route,
    run as run
)

__all__ = [
    # Submodules
    "http",

    # core.__all__
    "route", "run"
    # __init__.__all__
    "__version__",
]

# Public API
__version__: Final[LiteralString] = ...
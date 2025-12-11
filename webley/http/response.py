from typing import Any, Dict

class HttpResponse:

    status_code: int

    def __init__(self, content=b"", *args, **kwargs):
        self.status_code = kwargs.get("status_code", 200)
        self.headers: Dict[str, str] = {}
        self.content = content
        # default content-type
        if isinstance(content, (str, bytes)):
            self.headers.setdefault("Content-Type", "text/html")

    def __repr__(self):
        return ""
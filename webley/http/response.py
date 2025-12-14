from typing import Any, Dict

class HttpResponse:

    status_code = 200

    def __init__(self, content=b"", *args, **kwargs):
        self.headers: Dict[str, str] = {}
        self.content = content
        # default content-type
        if isinstance(content, (str, bytes)):
            self.headers.setdefault("Content-Type", "text/html")

    def __repr__(self):
        return ""
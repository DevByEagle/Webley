from typing import Any, Dict

class HttpResponse:
    def __init__(self, content=b"", *args, **kwargs):
        self.status_code: int = kwargs.get("status_code", 200)
        self.headers: Dict[str, str] = {}
        self.content = content
    
    def __repr__(self):
        pass

    def text(self):
        return self.content.decode()
    
    # TODO: Remove this function
    def send(self, handler: Any):
        handler.send_response(self.status_code)
        for key, value in self.headers.items():
            handler.send_header(key, value)
        handler.send_header("Content-Length", str(len(self.content)))
        handler.end_headers()
        handler.wfile.write(self.content)
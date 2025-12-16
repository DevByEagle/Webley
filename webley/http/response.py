class HttpResponse:

    status_code = 200

    def __init__(self, content=b"", *args, **kwargs):
        self.headers = {"Content-Type": kwargs.get("content_type", "text/html")}
        self.content = content
    
    @property
    def text(self):
        return self.content.decode("utf-8")
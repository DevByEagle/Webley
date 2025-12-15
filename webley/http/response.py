class HttpResponse:

    status_code = 200

    def __init__(self, content=b"", *args, **kwargs):
        self.headers = {}
        if "Content-Type" not in self.headers:
            if kwargs.get("content_type") is None:
                content_type = "text/html"
            self.headers["Content-Type"] = content_type
        self.content = content

    def __repr__(self):
        pass

    @property
    def text(self):
        return self.content.decode("utf-8")
    
    def _get_status_code_as_string(self):
        reason_phrases = {
            200: "OK",
            201: "Created",
            204: "No Content",
            301: "Moved Permanently",
            302: "Found",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            500: "Internal Server Error",
        }
        reason = reason_phrases.get(self.status_code, "Unknown Status")
        return f"{self.status_code} {reason}"
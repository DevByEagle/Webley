import webley as wb

@wb.route("/")
def index(request):
    return wb.http.HttpResponse(b"<h1>Hello, World</h1>", content_type="text/html")

if __name__ == "__main__":
    wb.run()
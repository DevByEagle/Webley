import webley as wb

@wb.route("/")
def index(request):
    content = wb.http.HttpResponse(b"""
        <h1>Hello, World!</h1>
    """, content_type="text/html")
    return content

wb.run()
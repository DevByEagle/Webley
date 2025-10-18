import webley as wb

@wb.route("/")
def home(request):
    return wb.http.HttpResponse(b"<h1>Hello, World</h1>")

@wb.route("/about")
def about(request):
    print(request.path)
    return wb.http.HttpResponse(b"<h1>About</h1>")

wb.run()
import webley as wb

@wb.route("/")
def home(request):
    return wb.http.HttpResponse(b"<h1>Hello, Webley!</h1>")

wb.run()

Exception
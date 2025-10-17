import webley as wb

@wb.route("/")
def home(request):
    return wb.http.HttpResponse(b"""
        <h1>Hello From Webley!</h1>
        <p>Boo</p>
    """)

@wb.route("/about")
def about(request):
    return wb.http.HttpResponse(b"""
        <h1>About Page</h1>
    """)

wb.run()
import webley as wb

app = wb.Webley()

@app.route("/")
def main(req: wb.HttpRequest):
    return wb.HttpResponse(b"Hello, Webley!")

app.run()
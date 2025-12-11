import webley as wb

app = wb.Webley()

@app.route('/')
def home(req: wb.http.HttpRequest):
    name = "Tom"
    return wb.http.HttpResponse(f"<h1>Hello {name}</h1>")

if __name__ == "__main__":
    app.run(port=4000)
import webley as wb

@wb.route("/")
def index(request):
    content = b"""
    <!DOCTYPE html>
    <h1>Hello, World!</h1>    
    """
    return wb.http.HttpResponse(content, content_type="text/json")

if __name__ == "__main__":
    wb.run()
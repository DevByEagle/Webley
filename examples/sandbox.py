import webley
from webley.auth import User

def login_user():
    user = User("John", "john@exmaple.com")
    user.login()

@webley.route("/")
def index(request):
    button = f'<button type="submit" onClick={login_user}>login</button>'
    content = button.encode()
    return webley.http.HttpResponse(content)

webley.run()
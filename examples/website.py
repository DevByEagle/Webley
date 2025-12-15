import webley as wb

app = wb.Webley()

@app.route("/users/{id}")
def get_user(id: int):
    return wb.HttpResponse(f"user_id: {id}", content_type="text/json")

app.run()
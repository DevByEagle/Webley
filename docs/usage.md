---
icon: material/toolbox-outline
---

After installing Webley, building and customizing web applications is straightforward.

For installation instructions, see [Installation].

!!! note
    Refer to the [API Reference] for complete details on Webley’s classes, methods, and utilities, and learn how to leverage Webley’s full capabilities.

    [Installation]: installation.md
    [API Reference]: api-reference.md

### Customization

Webley offers extensive flexibility through configuration options, allowing you to tailor routing, responses, middleware, and more to your project’s needs.

Some configurable features include:

* Route parameters and URL parsing

These are just a few examples—more options can be found in the [API Reference].

### Defining Routes

Webley makes it simple to define routes and return HTTP responses. Here’s a quick example that responds with "Hello, Webley!" when visiting the root URL:

```python title="Hello Webley App"
import webley as wb

@wb.route("/")
def home(request):
    return wb.http.HttpResponse(b"<h1>Hello, Webley!</h1>")

wb.run()
```

For a detailed overview of Webley classes like `HttpRequest` and `HttpResponse`, along with routing, middleware, and response options, see the [API Reference].
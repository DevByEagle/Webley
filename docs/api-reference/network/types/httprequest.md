<h1 class="webley-api-header" markdown>
    <!-- <span class="webley-api-icon" markdown>:octicons-note-24:</span>  -->
    <span class="webley-api-name">HttpRequest</span> 
</h1>

```python
class HttpRequest:
    method: str
    path: str
```

Represents an HTTP request in Webley.
Contains all the metadata and body of the incoming HTTP request.

---

## Members

<h3 markdown> method <span class="webley-api-type"> : str </span> </h3>

The HTTP method of the request (e.g., GET, POST).

<h3 markdown> path <span class="webley-api-type"> : str </span> </h3>

The path part of the requested URL.

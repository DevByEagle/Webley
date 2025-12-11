<h1 class="webley-api-header" markdown> 
    <!-- <span class="webley-api-icon" markdown>:octicons-note-24:</span>  -->
    <span class="webley-api-name">HttpResponse</span> 
</h1>

```python
class HttpResponse:
    status_code: int
    headers: dict[str, str]
    content: bytes
```

Represents an HTTP response in Webley.
Contains status, headers, and body of the response.

---

## Members

<h3 markdown> status_code <span class="webley-api-type"> : int </span> </h3>

The HTTP status code to return (e.g., 200, 404).

<h3 markdown> headers <span class="webley-api-type"> : dict[str, str] </span> </h3>

Key-value map of headers to include in the response.

<h3 markdown> content <span class="webley-api-type"> : str </span> </h3>

The body of the response.

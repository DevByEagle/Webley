<h1 class="webley-api-header" markdown>
    <span class="webley-api-name">Webley</span>
</h1>

```python
class Webley:
    router: Router;
```

The main application object in the Webley framework.
Handles routing and the running of a web server.

---

## Fields

<h3 markdown>router
    <span class="webley-api-type"> 
        : <a href="../../network/types/router.md"> Router</a>
    </span>
</h3>

The router instance responsible for storing all route handlers.
Used internally by the Webley framework to match incoming requests.

---

## Methods

<h3 markdown>
    run
    <span class="webley-api-type">
        -> None
    </span>
</h3>

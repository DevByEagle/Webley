<h1 class="webley-api-header" markdown>
    <span class="webley-api-name">Webley</span>
</h1>

```python
class Webley:
    router: Router
    def run(self, host: str = "127.0.0.1", port: int = 8000) -> None: ...
```

The main application object in the Webley framework.
Handles routing and the running of a web server.

---

## Fields

<h3 markdown>
    router
    <span class="webley-api-type">
        : <a href="../../../network/types/router">Router</a>
    </span>
</h3>

The router instance that stores all route handlers. Use it via `route` decorator or directly.

---

## Methods

<h3 markdown>
    route
    <span class="webley-api-type">
        -> Callable
    </span>
</h3>

```python
def Webley.route(self, path: str) -> Callable: ...
```

<h3 markdown>
    run
    <span class="webley-api-type">
        -> None
    </span>
</h3>

```python
def Webley.run(self, host: str = "127.0.0.1", port: int = 8000) -> None: ...
```

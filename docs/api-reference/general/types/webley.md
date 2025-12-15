<h1 class="webley-api-header" markdown>
    <span class="webley-api-name">Webley</span>
</h1>

```ts
class Webley = {
    router: Router;
    run: (self, host: string, port: int) => None;
}
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

---

## Methods

<h3 markdown>
    run
    <span class="webley-api-type">
        -> None
    </span>
</h3>

```python
def Webley.run(self, host: str, port: int) -> None: ...
```

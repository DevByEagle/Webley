<h1 class="webley-api-header" markdown>
    <!-- <span class="webley-api-icon" markdown>:octicons-note-24:</span> -->
    <span class="webley-api-name">Webley</span>
</h1>

```python
class Webley:
    router: Router
```

The main application object in the Webley framework.
Handles routing and the running of a web server.

---

## Members

<h3 markdown>router
    <span class="webley-api-type"> 
        : <a href="../../network/types/router.md"> Router</a>
    </span>
</h3>

The router instance responsible for storing all route handlers.
Used internally by the Webley framework to match incoming requests.

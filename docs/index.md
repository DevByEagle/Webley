---
  template: home.html
  hide:
    - toc
    - navigation
---

<div id="webley-home" markdown>
<section id="webley-home-main">
<section id="webley-home-main-inner">
<h1>Build websites that feel effortless.</h1>
<p>
</p>
<p>
Webley helps you build web applications without fighting complexity.
It provides a minimalistic but powerful foundation — letting you focus on
your logic, not framework overhead.
</p>
<nav>
<a href="./getting-started/">Getting started</a>
</nav>
</section>
</section>

<aside id="webley-scroll">
    Scroll down to learn more
</aside>

<section id="webley-home-belowfold" markdown>

<h2>Explicit by design</h2>

Webley favors clarity and simplicity. Your routes and logic are always explicit, making your code predictable and easy to maintain.

```python
import webley as wb

app = wb.Webley()

@app.route("/")
def ping():
    return wb.HttpResponse(b"Hello, World!")
```

---

<h2>Readable Routing</h2>

Webley's routing is straightforward and readable. Dynamic parameters are explicit and typed — no surprises or hidden behavior.

```python
@app.route("/users/{id}")
def get_user(id: int):
    return wb.HttpResponse(f"user_id: {id}", content_type="text/json")
```

---

<h2>Minimal, Powerful, Flexible</h2>

Webley doesn't get in your way. Its minimal design ensures you only write what you need, while the framework still provides the essential tools for building robust web apps.

</section>

---
icon: material/function
---

<style>
    .md-typeset__table {
      width: 100%;
    }

    .md-typeset__table table:not([class]) {
      display: table
    }
</style>


## **Module: [`webley`]** {#webley data-toc-label="webley"}

| Function | Description |
| :-- | :-- |
| run(address: string, port: int): `None` | Starts the Webley development server at the specified address and port. |
| route(path: string): [`Callable`]() | A decorator that registers a function as a route handler for the given path. |


## **Module: [`webley.http`]** {#webley-http data-toc-label="webley.http"}

### Class: `HttpRequest` {#webley-http-request data-toc-label="HttpRequest"}

#### Methods

##### `text`

Returns the content of the response as a UTF-8 decoded string.

**Returns:**

<table>
  <tr>
    <td><code>str</code></td>
  </tr>
</table>
---
icon: material/cube-outline
---

### `HttpRequest`

Represents an HTTP request received by the Webley server. It encapsulates request data such as the path, HTTP method, headers, query parameters, and body.

```ts linenums="0"
interface HttpRequest {
    path: string;
    method: string;
}
```

##### Properties

| Attribute | Description | Default |
| :-- | :-- | :-- |
| `path` | The URL path of the request (e.g., `"/"`, `"/users"`). | `""` |
| `method` | The HTTP method used for the request (e.g., `"GET"`, `"POST"`). | `None` |

### `HttpResponse`

Represents an HTTP response returned to the client. Allows setting the status code, headers, and content.

```ts linenums="0"
interface HttpResponse {
    status_code: number;
    headers: Dictionary<string, string>;
    content: bytes;
}
```

##### Properties

| Attribute | Description | Default |
| :-- | :-- | :-- |
| `status_code` | The HTTP status code (e.g., `200`, `404`, `500`). | `"200"` |
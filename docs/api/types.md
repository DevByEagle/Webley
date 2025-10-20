---
icon: material/cube-outline
---

## `HttpRequest`

Represents an HTTP request received by the Webley server. It encapsulates all request data, including the URL path, HTTP method, headers and more.

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
| `method` | The HTTP method used (e.g., `"GET"`, `"POST"`). | `"GET"` |

### Methods

## `HttpResponse`

Represents an HTTP response returned to the client. Allows configuration of the status code, headers, and body content.

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
| `status_code` | The HTTP status code (e.g., `200`, `404`, `500`). | `200` |
| `content` | Response body as bytes. | `b""` |

### Methods

| text(): [`string`]() |
| :-- |
| Returns the content of the response as a UTF-8 decoded string. |
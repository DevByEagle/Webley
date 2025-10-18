---
icon: material/book-outline
---

## Summary

### Packages

| Package | Description |
| :-- | :-- |
| `webley.http` | Core HTTP request and response classes. |

### Types

#### `HttpRequest`

Represents an HTTP request received by the Webley server.

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

#### `HttpResponse`

Represents an HTTP response returned to the client.


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
| `headers` | The response headers included in the reply. | `{}` |
| `content` | The response body, sent as bytes. | `b""` |

### Methods / Functions

#### Module: [`webley`] {#webley data-toc-label="Webley"}

| run(address: string, port: int): [`None`]() |
| :-- |
| Starts the Webley development server at the specified address and port. |

| route(path: string): [`Callable`]() | 
| :-- |
| A decorator that registers a function as a route handler for the given path. |

#### Module: [`webley.http.HttpResponse`] {#webley-http-reponse data-toc-label="HttpResponse"}


| text(): [`string`]() |
| :-- |
| Returns the content of the response as a UTF-8 decoded string. |

## Methods

### `HttpResponse.text`

Returns the content of the response as a UTF-8 decoded string.

#### Returns

<table>
    <tr>
        <td><a href="">string</a></td>
    </tr>
</table>
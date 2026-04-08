## Upload

`$ ant beta:files upload`

**post** `/v1/files`

Upload File

### Parameters

- `--file: string`

  Body param: The file to upload

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `file_metadata: object { id, created_at, filename, 5 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: string`

    RFC 3339 datetime string representing when the file was created.

  - `filename: string`

    Original filename of the uploaded file.

  - `mime_type: string`

    MIME type of the file.

  - `size_bytes: number`

    Size of the file in bytes.

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

  - `scope: optional object { id, type }`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

### Example

```cli
ant beta:files upload \
  --api-key my-anthropic-api-key \
  --file 'Example data'
```

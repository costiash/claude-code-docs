## List

`$ ant beta:files list`

**get** `/v1/files`

List Files

### Parameters

- `--after-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `--scope-id: optional string`

  Query param: Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaFileListResponse: object { data, first_id, has_more, last_id }`

  - `data: array of FileMetadata`

    List of file metadata objects.

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

  - `first_id: optional string`

    ID of the first file in this page of results.

  - `has_more: optional boolean`

    Whether there are more results available.

  - `last_id: optional string`

    ID of the last file in this page of results.

### Example

```cli
ant beta:files list \
  --api-key my-anthropic-api-key
```

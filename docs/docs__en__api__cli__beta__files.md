# Files

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

## Download

`$ ant beta:files download`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `unnamed_schema_0: file path`

### Example

```cli
ant beta:files download \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

## Retrieve Metadata

`$ ant beta:files retrieve-metadata`

**get** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

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
ant beta:files retrieve-metadata \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

## Delete

`$ ant beta:files delete`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `deleted_file: object { id, type }`

  - `id: string`

    ID of the deleted file.

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### Example

```cli
ant beta:files delete \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

## Domain Types

### Beta File Scope

- `beta_file_scope: object { id, type }`

  - `id: string`

    The ID of the scoping resource (e.g., the session ID).

  - `type: "session"`

    The type of scope (e.g., `"session"`).

### Deleted File

- `deleted_file: object { id, type }`

  - `id: string`

    ID of the deleted file.

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### File Metadata

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

# Files

## Retrieve

**get** `/v1/compliance/apps/chats/files/{claude_file_id}`

Retrieves metadata for a file referenced in chat messages, without
downloading the file content. Use the sibling `/content` endpoint to
download the bytes.

### Path Parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  File ID

- `created_at: string`

  File creation timestamp

- `filename: string`

  Display name of the file, if set

- `message_ids: array of string`

  Chat message IDs this file is attached to. A file can be referenced by multiple messages.

- `mime_type: string`

  MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

- `size_bytes: number`

  Size in bytes of the file's preferred downloadable variant, if known

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Delete

**delete** `/v1/compliance/apps/chats/files/{claude_file_id}`

Permanently deletes a specific file. This is a destructive
operation that cannot be undone.

### Path Parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the file that was deleted

- `type: optional "claude_file_deleted"`

  Constant string confirming deletion

  - `"claude_file_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Content

**get** `/v1/compliance/apps/chats/files/{claude_file_id}/content`

Downloads the binary content of a file referenced in chat messages.

### Path Parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### File Retrieve Response

- `FileRetrieveResponse = object { id, created_at, filename, 3 more }`

  File metadata for GET /v1/compliance/apps/chats/files/{claude_file_id}.

  Returns metadata only. Use the sibling `/content` endpoint to download
  the file bytes.

  - `id: string`

    File ID

  - `created_at: string`

    File creation timestamp

  - `filename: string`

    Display name of the file, if set

  - `message_ids: array of string`

    Chat message IDs this file is attached to. A file can be referenced by multiple messages.

  - `mime_type: string`

    MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

  - `size_bytes: number`

    Size in bytes of the file's preferred downloadable variant, if known

### File Delete Response

- `FileDeleteResponse = object { id, type }`

  Response for deleting a compliance file.

  - `id: string`

    The ID of the file that was deleted

  - `type: optional "claude_file_deleted"`

    Constant string confirming deletion

    - `"claude_file_deleted"`

### File Content Response

- `FileContentResponse = unknown`

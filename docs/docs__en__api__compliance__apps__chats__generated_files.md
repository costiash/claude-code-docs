# Generated Files

## Get Claude-generated file metadata

**get** `/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}`

Returns metadata for a file the assistant created via tool use.

Metadata is read from Filestore (the durable backing store for
per-conversation tool outputs). Use the sibling `/content` endpoint to
download the bytes.

### Path Parameters

- `claude_gen_file_id: string`

  The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Opaque generated-file id, e.g. 'claude_gen_file_abc123'.

- `claude_chat_id: string`

  The chat this generated file belongs to

- `created_at: string`

  File creation timestamp from Filestore

- `filename: string`

  Display name of the generated file

- `md5: string`

  Lowercase hex MD5 of the stored file, as recorded by Filestore. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

- `mime_type: string`

  MIME type as recorded by Filestore, when available

- `size_bytes: number`

  Size in bytes of the stored file, when available

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "id",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "mime_type",
  "size_bytes": 0
}
```

## Download a Claude-generated file

**get** `/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`

Downloads the binary content of a file the assistant created via tool use.

### Path Parameters

- `claude_gen_file_id: string`

  The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.

### Header Parameters

- `"x-api-key": optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Generated File Retrieve Response

- `GeneratedFileRetrieveResponse object { id, claude_chat_id, created_at, 4 more }`

  Metadata for GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}.

  Returns metadata only. Use the sibling `/content` endpoint to download
  the bytes. The owning chat is included since the id is opaque; to find the
  specific message that produced the file, fetch
  `/v1/compliance/apps/chats/{claude_chat_id}/messages` and match on
  `generated_files[].id`.

  - `id: string`

    Opaque generated-file id, e.g. 'claude_gen_file_abc123'.

  - `claude_chat_id: string`

    The chat this generated file belongs to

  - `created_at: string`

    File creation timestamp from Filestore

  - `filename: string`

    Display name of the generated file

  - `md5: string`

    Lowercase hex MD5 of the stored file, as recorded by Filestore. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

  - `mime_type: string`

    MIME type as recorded by Filestore, when available

  - `size_bytes: number`

    Size in bytes of the stored file, when available

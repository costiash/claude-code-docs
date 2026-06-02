# Apps

# Chats

## List chats

**get** `/v1/compliance/apps/chats`

Lists chat metadata with filtering capabilities for targeted
compliance review. Results are sorted chronologically (time ascending)
by created_at, with ties broken by id.

### Query Parameters

- `user_ids: array of string`

  Filter to chats created by specific users. **Required**; pass 1–10 user IDs per request. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

- `after_id: optional string`

  Pagination cursor for retrieving the next page of results (heading backwards in time). To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `before_id: optional string`

  Pagination cursor for retrieving the previous page of results (heading forwards in time). To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `created_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter chats created after this time (RFC 3339 format)

  - `gte: optional string`

    Filter chats created at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter chats created before this time (RFC 3339 format)

  - `lte: optional string`

    Filter chats created at or before this time (RFC 3339 format)

- `limit: optional number`

  Maximum results (default: 100, max: 1000)

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

- `project_ids: optional array of string`

  Filter by project IDs (accepts `claude_proj_...`). Enumerate IDs via `GET /v1/compliance/apps/projects`.

- `updated_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter chats updated after this time (RFC 3339 format)

  - `gte: optional string`

    Filter chats updated at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter chats updated before this time (RFC 3339 format)

  - `lte: optional string`

    Filter chats updated at or before this time (RFC 3339 format)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, deleted_at, 8 more }`

  List of chat metadata sorted chronologically by created_at, tie break by id

  - `id: string`

    Chat ID

  - `created_at: string`

    Creation timestamp

  - `deleted_at: string`

    Deletion timestamp if deleted

  - `href: string`

    URL to view this chat in claude.ai

  - `model: string`

    Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

  - `name: string`

    Chat name/title

  - `organization_id: string`

    Organization ID this chat belongs to

  - `organization_uuid: string`

    Organization UUID this chat belongs to

  - `project_id: string`

    Project ID this chat belongs to

  - `updated_at: string`

    Last update timestamp

  - `user: object { id, email_address }`

    User information for the chat creator

    - `id: string`

      User identifier

    - `email_address: string`

      User's email address

- `first_id: string`

  First chat ID in the current result set. To get the previous page, use this as before_id in your next request

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `last_id: string`

  Last chat ID in the current result set. To get the next page, use this as after_id in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "id": "claude_chat_abc123",
      "name": "Product Requirements Discussion",
      "created_at": "2025-06-07T08:09:10Z",
      "updated_at": "2025-06-07T09:10:11Z",
      "organization_id": "org_abc123",
      "organization_uuid": "abcdef0123-4567-89ab-cdef-0123456789ab",
      "project_id": "claude_proj_xyz789",
      "model": "claude-opus-4-7",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      },
      "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789"
    }
  ],
  "has_more": false,
  "first_id": "claude_chat_abc123",
  "last_id": "claude_chat_abc123"
}
```

## Delete chat

**delete** `/v1/compliance/apps/chats/{claude_chat_id}`

Permanently deletes a chat and all associated messages and
files. This is a destructive operation that cannot be undone.

### Path Parameters

- `claude_chat_id: string`

  The chat ID (tagged ID, e.g., claude_chat_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the Claude chat that was deleted

- `type: optional "claude_chat_deleted"`

  Constant string confirming deletion

  - `"claude_chat_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "claude_chat_abc123",
  "type": "claude_chat_deleted"
}
```

## Domain Types

### Chat List Response

- `ChatListResponse object { id, created_at, deleted_at, 8 more }`

  Chat metadata for listing chats (without messages).

  - `id: string`

    Chat ID

  - `created_at: string`

    Creation timestamp

  - `deleted_at: string`

    Deletion timestamp if deleted

  - `href: string`

    URL to view this chat in claude.ai

  - `model: string`

    Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

  - `name: string`

    Chat name/title

  - `organization_id: string`

    Organization ID this chat belongs to

  - `organization_uuid: string`

    Organization UUID this chat belongs to

  - `project_id: string`

    Project ID this chat belongs to

  - `updated_at: string`

    Last update timestamp

  - `user: object { id, email_address }`

    User information for the chat creator

    - `id: string`

      User identifier

    - `email_address: string`

      User's email address

### Chat Delete Response

- `ChatDeleteResponse object { id, type }`

  Response for deleting a Claude chat.

  - `id: string`

    The ID of the Claude chat that was deleted

  - `type: optional "claude_chat_deleted"`

    Constant string confirming deletion

    - `"claude_chat_deleted"`

# Messages

## Get chat messages

**get** `/v1/compliance/apps/chats/{claude_chat_id}/messages`

Retrieves message history and file metadata for a specific chat.

### Path Parameters

- `claude_chat_id: string`

  The chat ID (tagged ID, e.g., claude_chat_abc123)

### Query Parameters

- `after_id: optional string`

  Pagination cursor for retrieving the next page of results (heading backwards in time). To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `before_id: optional string`

  Pagination cursor for retrieving the previous page of results (heading forwards in time). To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `created_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter messages created after this time (RFC 3339 format)

  - `gte: optional string`

    Filter messages created at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter messages created before this time (RFC 3339 format)

  - `lte: optional string`

    Filter messages created at or before this time (RFC 3339 format)

- `limit: optional number`

  Maximum results (max: 1000). When omitted, the full result set is returned in one response.

- `order: optional "asc" or "desc"`

  Sort direction for messages within the response. `asc` (the default) returns oldest-first; `desc` returns newest-first.

  - `"asc"`

  - `"desc"`

- `tool_result_max_chars: optional number`

  Maximum characters returned per tool-result text item. Items longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

- `tool_use_input_max_chars: optional number`

  Maximum characters of JSON-encoded tool input returned per tool_use block. Inputs longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

- `updated_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter messages updated after this time (RFC 3339 format)

  - `gte: optional string`

    Filter messages updated at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter messages updated before this time (RFC 3339 format)

  - `lte: optional string`

    Filter messages updated at or before this time (RFC 3339 format)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Chat ID

- `chat_messages: array of object { id, artifacts, content, 4 more }`

  Array of chat messages in order of created_at

  - `id: string`

    Unique identifier for the message e.g. 'claude_chat_msg_abcd1234'

  - `artifacts: array of object { id, artifact_type, title, version_id }`

    Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.

    - `id: string`

      Artifact ID e.g. 'claude_artifact_abc123'

    - `artifact_type: string`

      MIME-like artifact type e.g. 'application/vnd.ant.code'

    - `title: string`

      Artifact title

    - `version_id: string`

      Artifact version ID e.g. 'claude_artifact_version_abc123'

  - `content: array of object { text, type }  or object { id, input, integration_name, 4 more }  or object { content, integration_name, is_error, 5 more }`

    Content blocks within the message

    - `Text object { text, type }`

      Text content block.

      - `text: string`

        Text content from human or assistant

      - `type: "text"`

        - `"text"`

    - `ToolUse object { id, input, integration_name, 4 more }`

      Tool invocation requested by the assistant.

      - `id: string`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

      - `integration_name: string`

        Name of the integration that provides this tool, when applicable

      - `mcp_server_url: string`

        Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass tool_use_input_max_chars=-1 to disable the limit

      - `type: "tool_use"`

        - `"tool_use"`

    - `ToolResult object { content, integration_name, is_error, 5 more }`

      Result returned by a tool invocation.

      - `content: array of object { text, type }`

        Text content returned by the tool. Generated files are surfaced via the message's `generated_files` list; other non-text item types (including images and links) are omitted.

        - `text: string`

          Text returned by the tool

        - `type: "text"`

          - `"text"`

      - `integration_name: string`

        Name of the integration that provides this tool, when applicable

      - `is_error: boolean`

        True when the tool reported an error

      - `mcp_server_url: string`

        Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened. Pass tool_result_max_chars=-1 to retrieve full content.

      - `type: "tool_result"`

        - `"tool_result"`

  - `created_at: string`

    Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

  - `files: array of object { id, filename, mime_type }`

    Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

    - `id: string`

      File ID

    - `filename: string`

      Display name of the file

    - `mime_type: string`

      MIME type of the file when it was uploaded (e.g. 'application/pdf')

  - `generated_files: array of object { id, filename, mime_type }`

    Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`.

    - `id: string`

      Opaque generated-file id, e.g. 'claude_gen_file_abc123'. Treat as an opaque string; the encoding may change without notice.

    - `filename: string`

      Display name of the generated file

    - `mime_type: string`

      MIME type reported by the tool that produced the file

  - `role: "assistant" or "user"`

    Message sender (user or assistant)

    - `"assistant"`

    - `"user"`

- `created_at: string`

  Creation timestamp

- `deleted_at: string`

  Deletion timestamp if deleted

- `first_id: string`

  Opaque pagination cursor for the first message in the current result set. Pass as `before_id` on the next request to page backwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `has_more: boolean`

  Whether more chat messages exist beyond the current result set. Use `last_id` as `after_id` in a follow-up request to page forward.

- `href: string`

  URL to view this chat in claude.ai

- `last_id: string`

  Opaque pagination cursor for the last message in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `model: string`

  Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

- `name: string`

  Chat name

- `organization_id: string`

  Organization ID this chat belongs to

- `organization_uuid: string`

  Organization UUID this chat belongs to

- `project_id: string`

  Project ID this chat belongs to

- `updated_at: string`

  Last update timestamp

- `user: object { id, email_address }`

  User information

  - `id: string`

    User identifier

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID/messages \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "claude_chat_abc123",
  "name": "Product Requirements Discussion",
  "created_at": "2025-06-07T08:09:10Z",
  "updated_at": "2025-06-07T08:09:11Z",
  "organization_id": "org_abc123",
  "organization_uuid": "abcdef0123-4567-89ab-cdef-0123456789ab",
  "project_id": "claude_proj_xyz789",
  "model": "claude-opus-4-7",
  "user": {
    "id": "user_xyz456",
    "email_address": "user@example.com"
  },
  "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789",
  "chat_messages": [
    {
      "id": "claude_chat_msg_abc123",
      "role": "user",
      "created_at": "2025-06-07T08:09:10Z",
      "content": [
        {
          "type": "text",
          "text": "Can you help me draft requirements for our new dashboard feature?"
        }
      ],
      "files": [
        {
          "id": "claude_file_xyz789",
          "filename": "dashboard_mockup_v1.pdf",
          "mime_type": "application/pdf"
        }
      ]
    },
    {
      "id": "claude_chat_msg_def456",
      "role": "assistant",
      "created_at": "2025-06-07T08:09:11Z",
      "content": [
        {
          "type": "text",
          "text": "I'd be happy to help you draft requirements for your dashboard feature..."
        }
      ],
      "artifacts": [
        {
          "id": "claude_artifact_abc123",
          "version_id": "claude_artifact_version_xyz789",
          "title": "Dashboard Requirements Draft",
          "artifact_type": "text/markdown"
        }
      ]
    }
  ],
  "has_more": false,
  "first_id": "eyJtc2dfdXVpZCI6ICIwZjcwYjA2Ni0uLi4ifQ==",
  "last_id": "eyJtc2dfdXVpZCI6ICJhNGUwYjE3Mi0uLi4ifQ=="
}
```

## Domain Types

### Message List Response

- `MessageListResponse object { id, artifacts, content, 4 more }`

  A single message in a chat conversation.

  - `id: string`

    Unique identifier for the message e.g. 'claude_chat_msg_abcd1234'

  - `artifacts: array of object { id, artifact_type, title, version_id }`

    Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.

    - `id: string`

      Artifact ID e.g. 'claude_artifact_abc123'

    - `artifact_type: string`

      MIME-like artifact type e.g. 'application/vnd.ant.code'

    - `title: string`

      Artifact title

    - `version_id: string`

      Artifact version ID e.g. 'claude_artifact_version_abc123'

  - `content: array of object { text, type }  or object { id, input, integration_name, 4 more }  or object { content, integration_name, is_error, 5 more }`

    Content blocks within the message

    - `Text object { text, type }`

      Text content block.

      - `text: string`

        Text content from human or assistant

      - `type: "text"`

        - `"text"`

    - `ToolUse object { id, input, integration_name, 4 more }`

      Tool invocation requested by the assistant.

      - `id: string`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

      - `integration_name: string`

        Name of the integration that provides this tool, when applicable

      - `mcp_server_url: string`

        Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass tool_use_input_max_chars=-1 to disable the limit

      - `type: "tool_use"`

        - `"tool_use"`

    - `ToolResult object { content, integration_name, is_error, 5 more }`

      Result returned by a tool invocation.

      - `content: array of object { text, type }`

        Text content returned by the tool. Generated files are surfaced via the message's `generated_files` list; other non-text item types (including images and links) are omitted.

        - `text: string`

          Text returned by the tool

        - `type: "text"`

          - `"text"`

      - `integration_name: string`

        Name of the integration that provides this tool, when applicable

      - `is_error: boolean`

        True when the tool reported an error

      - `mcp_server_url: string`

        Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened. Pass tool_result_max_chars=-1 to retrieve full content.

      - `type: "tool_result"`

        - `"tool_result"`

  - `created_at: string`

    Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

  - `files: array of object { id, filename, mime_type }`

    Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

    - `id: string`

      File ID

    - `filename: string`

      Display name of the file

    - `mime_type: string`

      MIME type of the file when it was uploaded (e.g. 'application/pdf')

  - `generated_files: array of object { id, filename, mime_type }`

    Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`.

    - `id: string`

      Opaque generated-file id, e.g. 'claude_gen_file_abc123'. Treat as an opaque string; the encoding may change without notice.

    - `filename: string`

      Display name of the generated file

    - `mime_type: string`

      MIME type reported by the tool that produced the file

  - `role: "assistant" or "user"`

    Message sender (user or assistant)

    - `"assistant"`

    - `"user"`

# Files

## Get file metadata

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

- `claude_chat_ids: array of string`

  Chats this file is attached to. A file can be referenced by messages across multiple chats.

- `created_at: string`

  File creation timestamp

- `filename: string`

  Display name of the file, if set

- `md5: string`

  Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes; when the two disagree, the header is authoritative.

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

#### Response

```json
{
  "id": "claude_file_xyz789",
  "filename": "quarterly_report.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1048576,
  "md5": "5d41402abc4b2a76b9719d911017c592",
  "created_at": "2024-01-15T10:30:00Z",
  "message_ids": [
    "claude_chat_msg_abc123"
  ],
  "claude_chat_ids": [
    "claude_chat_def456"
  ]
}
```

## Delete file

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

#### Response

```json
{
  "id": "claude_file_xyz789",
  "type": "claude_file_deleted"
}
```

## Download file content

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

- `FileRetrieveResponse object { id, claude_chat_ids, created_at, 5 more }`

  File metadata for GET /v1/compliance/apps/chats/files/{claude_file_id}.

  Returns metadata only. Use the sibling `/content` endpoint to download
  the file bytes.

  - `id: string`

    File ID

  - `claude_chat_ids: array of string`

    Chats this file is attached to. A file can be referenced by messages across multiple chats.

  - `created_at: string`

    File creation timestamp

  - `filename: string`

    Display name of the file, if set

  - `md5: string`

    Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes; when the two disagree, the header is authoritative.

  - `message_ids: array of string`

    Chat message IDs this file is attached to. A file can be referenced by multiple messages.

  - `mime_type: string`

    MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

  - `size_bytes: number`

    Size in bytes of the file's preferred downloadable variant, if known

### File Delete Response

- `FileDeleteResponse object { id, type }`

  Response for deleting a compliance file.

  - `id: string`

    The ID of the file that was deleted

  - `type: optional "claude_file_deleted"`

    Constant string confirming deletion

    - `"claude_file_deleted"`

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

# Projects

## List projects

**get** `/v1/compliance/apps/projects`

Lists project metadata with filtering capabilities. Results
are sorted chronologically (time ascending) by created_at.

### Query Parameters

- `created_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter projects created after this time (RFC 3339 format)

  - `gte: optional string`

    Filter projects created at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter projects created before this time (RFC 3339 format)

  - `lte: optional string`

    Filter projects created at or before this time (RFC 3339 format)

- `limit: optional number`

  Maximum results (default: 20, max: 100)

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `user_ids: optional array of string`

  Filter by user IDs. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, deleted_at, 6 more }`

  List of projects sorted by creation date ascending

  - `id: string`

    Project identifier (tagged ID)

  - `created_at: string`

    Project creation timestamp

  - `deleted_at: string`

    Timestamp when the project was deleted by an end user, or null otherwise

  - `is_private: boolean`

    If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

  - `name: string`

    Project name

  - `organization_id: string`

    Organization identifier (tagged ID)

  - `organization_uuid: string`

    Organization UUID this project belongs to

  - `updated_at: string`

    Project last update timestamp

  - `user: object { id, email_address }`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of any organization
    under the parent organization.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "id": "claude_proj_abc123",
      "name": "Q4 Product Planning",
      "created_at": "2025-06-01T10:00:00Z",
      "updated_at": "2025-06-15T14:30:00Z",
      "is_private": true,
      "organization_id": "org_abc123",
      "organization_uuid": "abc12345-6789-0abc-def0-123456789abc",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      }
    }
  ],
  "has_more": true,
  "next_page": "page_eyJjcmVhdGVkX2F0IjoiMjAyNS0wNi0wMVQxMDowMDowMFoiLCJ1dWlkIjoiYWJjMTIzIn0="
}
```

## Get project details

**get** `/v1/compliance/apps/projects/{project_id}`

Get detailed information for a specific project.

### Path Parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Project identifier (tagged ID)

- `attachments_count: number`

  Number of attachments contained within this project

- `chats_count: number`

  Number of chats contained within this project

- `created_at: string`

  Project creation timestamp

- `deleted_at: string`

  Timestamp when the project was deleted by an end user, or null otherwise

- `description: string`

  Project description

- `instructions: string`

  Project's custom instructions / prompt

- `is_private: boolean`

  If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

- `name: string`

  Project name

- `organization_id: string`

  Organization identifier (tagged ID)

- `organization_uuid: string`

  Organization UUID this project belongs to

- `updated_at: string`

  Project last update timestamp

- `user: object { id, email_address }`

  The user who created a project or project document.

  Fields that reference this type are null when the creator's account has
  been deleted or the creator is no longer a member of any organization
  under the parent organization.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "id",
  "attachments_count": 0,
  "chats_count": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "instructions": "instructions",
  "is_private": true,
  "name": "name",
  "organization_id": "organization_id",
  "organization_uuid": "organization_uuid",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "user": {
    "id": "id",
    "email_address": "email_address"
  }
}
```

## Delete project

**delete** `/v1/compliance/apps/projects/{project_id}`

Delete a project for compliance purposes.

Hard-deletes the project and all its associated data including:

- All project documents and files
- All role assignments
- Knowledge base (if RAG is enabled)
- Sync sources

Project must have no attached chats - returns 409 if chats exist.

### Path Parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the Claude project that was deleted

- `type: optional "claude_project_deleted"`

  Constant string confirming deletion.

  - `"claude_project_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "id",
  "type": "claude_project_deleted"
}
```

## Domain Types

### Project List Response

- `ProjectListResponse object { id, created_at, deleted_at, 6 more }`

  Project information for compliance responses.

  - `id: string`

    Project identifier (tagged ID)

  - `created_at: string`

    Project creation timestamp

  - `deleted_at: string`

    Timestamp when the project was deleted by an end user, or null otherwise

  - `is_private: boolean`

    If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

  - `name: string`

    Project name

  - `organization_id: string`

    Organization identifier (tagged ID)

  - `organization_uuid: string`

    Organization UUID this project belongs to

  - `updated_at: string`

    Project last update timestamp

  - `user: object { id, email_address }`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of any organization
    under the parent organization.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

### Project Retrieve Response

- `ProjectRetrieveResponse object { id, attachments_count, chats_count, 10 more }`

  Detailed project information for compliance responses.

  - `id: string`

    Project identifier (tagged ID)

  - `attachments_count: number`

    Number of attachments contained within this project

  - `chats_count: number`

    Number of chats contained within this project

  - `created_at: string`

    Project creation timestamp

  - `deleted_at: string`

    Timestamp when the project was deleted by an end user, or null otherwise

  - `description: string`

    Project description

  - `instructions: string`

    Project's custom instructions / prompt

  - `is_private: boolean`

    If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

  - `name: string`

    Project name

  - `organization_id: string`

    Organization identifier (tagged ID)

  - `organization_uuid: string`

    Organization UUID this project belongs to

  - `updated_at: string`

    Project last update timestamp

  - `user: object { id, email_address }`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of any organization
    under the parent organization.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

### Project Delete Response

- `ProjectDeleteResponse object { id, type }`

  Response for deleting a Claude project.

  - `id: string`

    The ID of the Claude project that was deleted

  - `type: optional "claude_project_deleted"`

    Constant string confirming deletion.

    - `"claude_project_deleted"`

# Attachments

## List project attachments

**get** `/v1/compliance/apps/projects/{project_id}/attachments`

List files and documents attached to a project.

List files and project documents attached to the project referenced by project_id.
This includes the IDs of attached files, and attached project documents.

The raw binary content of attached files can be downloaded using the
GET /v1/compliance/apps/chats/files/{claude_file_id}/content endpoint.

The text content of attached project documents can be fetched using the
GET /v1/compliance/apps/projects/documents/{claude_proj_doc_id} endpoint.

### Path Parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

### Query Parameters

- `limit: optional number`

  Maximum results (default: 20, max: 100)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, filename, 2 more }  or object { id, created_at, filename, 2 more }`

  List of attachments sorted chronologically by created_at, tie break by id

  - `ComplianceProjectFileReference object { id, created_at, filename, 2 more }`

    File attachment reference for compliance responses.

    - `id: string`

      File identifier (e.g., 'claude_file_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

    - `filename: string`

      Display name of the file (e.g., 'document.pdf')

    - `mime_type: string`

      MIME type of the file when it was uploaded (e.g., 'application/pdf')

    - `type: "project_file"`

      Discriminator marking this as a binary file

      - `"project_file"`

  - `ComplianceProjectDocReference object { id, created_at, filename, 2 more }`

    Project document attachment reference for compliance responses.

    - `id: string`

      Project document identifier (e.g., 'claude_proj_doc_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

    - `filename: string`

      Display name of the document (e.g., 'document.txt')

    - `mime_type: "text/plain"`

      MIME type of the project document, always set to plain text

      - `"text/plain"`

    - `type: "project_doc"`

      Discriminator marking this as a plain text document

      - `"project_doc"`

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  To get the next page, use the 'next_page' from the current response as the 'page' in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/attachments \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "filename": "filename",
      "mime_type": "mime_type",
      "type": "project_file"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

## Domain Types

### Attachment List Response

- `AttachmentListResponse = object { id, created_at, filename, 2 more }  or object { id, created_at, filename, 2 more }`

  File attachment reference for compliance responses.

  - `ComplianceProjectFileReference object { id, created_at, filename, 2 more }`

    File attachment reference for compliance responses.

    - `id: string`

      File identifier (e.g., 'claude_file_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

    - `filename: string`

      Display name of the file (e.g., 'document.pdf')

    - `mime_type: string`

      MIME type of the file when it was uploaded (e.g., 'application/pdf')

    - `type: "project_file"`

      Discriminator marking this as a binary file

      - `"project_file"`

  - `ComplianceProjectDocReference object { id, created_at, filename, 2 more }`

    Project document attachment reference for compliance responses.

    - `id: string`

      Project document identifier (e.g., 'claude_proj_doc_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

    - `filename: string`

      Display name of the document (e.g., 'document.txt')

    - `mime_type: "text/plain"`

      MIME type of the project document, always set to plain text

      - `"text/plain"`

    - `type: "project_doc"`

      Discriminator marking this as a plain text document

      - `"project_doc"`

# Documents

## Get project document content

**get** `/v1/compliance/apps/projects/documents/{document_id}`

Get detailed information for a specific project document.

### Path Parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Project document identifier (tagged ID)

- `content: string`

  Document text content

- `created_at: string`

  Document creation timestamp

- `filename: string`

  Document filename

- `user: object { id, email_address }`

  The user who created a project or project document.

  Fields that reference this type are null when the creator's account has
  been deleted or the creator is no longer a member of any organization
  under the parent organization.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "id",
  "content": "content",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "user": {
    "id": "id",
    "email_address": "email_address"
  }
}
```

## Get project document metadata

**get** `/v1/compliance/apps/projects/documents/{document_id}/metadata`

Returns metadata for a project document, without the content body.

Use the sibling `GET /v1/compliance/apps/projects/documents/{document_id}`
endpoint to fetch the document text. The `md5` and `size_bytes`
fields here are computed over the UTF-8 encoding of that text, so a DLP
consumer can dedupe or match hashes without downloading every document.

### Path Parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Project document identifier (tagged ID)

- `claude_project_id: string`

  The project this document belongs to

- `created_at: string`

  Document creation timestamp

- `filename: string`

  Document filename

- `md5: string`

  Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.

- `mime_type: "text/plain"`

  MIME type of the document content, always plain text

  - `"text/plain"`

- `size_bytes: number`

  Size in bytes of the document content (UTF-8 encoded)

- `user: object { id, email_address }`

  The user who created a project or project document.

  Fields that reference this type are null when the creator's account has
  been deleted or the creator is no longer a member of any organization
  under the parent organization.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID/metadata \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "id",
  "claude_project_id": "claude_project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "text/plain",
  "size_bytes": 0,
  "user": {
    "id": "id",
    "email_address": "email_address"
  }
}
```

## Delete project document

**delete** `/v1/compliance/apps/projects/documents/{document_id}`

Delete a project document for compliance purposes.

Hard-deletes the project document permanently.

### Path Parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the project document that was deleted

- `type: "claude_project_document_deleted"`

  Constant string confirming deletion.

  - `"claude_project_document_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "id",
  "type": "claude_project_document_deleted"
}
```

## Domain Types

### Document Retrieve Response

- `DocumentRetrieveResponse object { id, content, created_at, 2 more }`

  Project document information for compliance responses.

  - `id: string`

    Project document identifier (tagged ID)

  - `content: string`

    Document text content

  - `created_at: string`

    Document creation timestamp

  - `filename: string`

    Document filename

  - `user: object { id, email_address }`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of any organization
    under the parent organization.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

### Document Metadata Response

- `DocumentMetadataResponse object { id, claude_project_id, created_at, 5 more }`

  Project document metadata for GET /v1/compliance/apps/projects/documents/{document_id}/metadata.

  Returns metadata only. Use the sibling endpoint (without `/metadata`)
  to fetch the document text content.

  - `id: string`

    Project document identifier (tagged ID)

  - `claude_project_id: string`

    The project this document belongs to

  - `created_at: string`

    Document creation timestamp

  - `filename: string`

    Document filename

  - `md5: string`

    Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.

  - `mime_type: "text/plain"`

    MIME type of the document content, always plain text

    - `"text/plain"`

  - `size_bytes: number`

    Size in bytes of the document content (UTF-8 encoded)

  - `user: object { id, email_address }`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of any organization
    under the parent organization.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

### Document Delete Response

- `DocumentDeleteResponse object { id, type }`

  Response for deleting a project document.

  - `id: string`

    The ID of the project document that was deleted

  - `type: "claude_project_document_deleted"`

    Constant string confirming deletion.

    - `"claude_project_document_deleted"`

# Artifacts

## Get artifact metadata

**get** `/v1/compliance/apps/artifacts/{artifact_version_id}`

Returns metadata for an artifact version, without the content body.

Use the sibling `/content` endpoint to fetch the artifact text. The
`md5` and `size_bytes` fields here are computed over the UTF-8
encoding of that text, so a DLP consumer can dedupe or match hashes
without downloading every artifact.

### Path Parameters

- `artifact_version_id: string`

  The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Artifact ID e.g. 'claude_artifact_abc123'

- `artifact_type: string`

  MIME-like artifact type e.g. 'application/vnd.ant.code'

- `claude_chat_id: string`

  The chat this artifact belongs to

- `created_at: string`

  Artifact version creation timestamp

- `md5: string`

  Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

- `size_bytes: number`

  Size in bytes of the artifact content (UTF-8 encoded)

- `title: string`

  Artifact title

- `version_id: string`

  Artifact version ID e.g. 'claude_artifact_version_abc123'

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "id",
  "artifact_type": "artifact_type",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "md5": "md5",
  "size_bytes": 0,
  "title": "title",
  "version_id": "version_id"
}
```

## Download artifact content

**get** `/v1/compliance/apps/artifacts/{artifact_version_id}/content`

Download the content of an artifact version for compliance purposes.

Returns the full text content of the artifact version.

### Path Parameters

- `artifact_version_id: string`

  The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Artifact Retrieve Response

- `ArtifactRetrieveResponse object { id, artifact_type, claude_chat_id, 5 more }`

  Artifact version metadata for GET /v1/compliance/apps/artifacts/{artifact_version_id}.

  Returns metadata only. Use the sibling `/content` endpoint to fetch the
  artifact body.

  - `id: string`

    Artifact ID e.g. 'claude_artifact_abc123'

  - `artifact_type: string`

    MIME-like artifact type e.g. 'application/vnd.ant.code'

  - `claude_chat_id: string`

    The chat this artifact belongs to

  - `created_at: string`

    Artifact version creation timestamp

  - `md5: string`

    Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

  - `size_bytes: number`

    Size in bytes of the artifact content (UTF-8 encoded)

  - `title: string`

    Artifact title

  - `version_id: string`

    Artifact version ID e.g. 'claude_artifact_version_abc123'

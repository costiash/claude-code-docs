## Messages

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

- `limit: optional number`

  Maximum results (max: 1000). When omitted, the full result set is returned in one response.

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

    Artifacts generated or updated by this message

    - `id: string`

      Artifact ID e.g. 'claude_artifact_abc123'

    - `artifact_type: string`

      MIME-like artifact type e.g. 'application/vnd.ant.code'

    - `title: string`

      Artifact title

    - `version_id: string`

      Artifact version ID e.g. 'claude_artifact_version_abc123'

  - `content: array of object { text, type }`

    Content blocks within the message

    - `text: string`

      Text content from human or assistant

    - `type: "text"`

      - `"text"`

  - `created_at: string`

    Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

  - `files: array of object { id, filename, mime_type }`

    File attachments

    - `id: string`

      File ID

    - `filename: string`

      Display name of the file

    - `mime_type: string`

      MIME type of the file when it was uploaded (e.g. 'application/pdf')

  - `generated_files: array of object { id, filename, mime_type }`

    Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message.

    - `id: string`

      Opaque generated-file id, e.g. 'claude_gen_file_abc123'. Treat as an opaque string; the encoding may change without notice.

    - `filename: string`

      Display name of the generated file

    - `mime_type: string`

      MIME type reported by the tool that produced the file

  - `role: "user" or "assistant"`

    Message sender (user or assistant)

    - `"user"`

    - `"assistant"`

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

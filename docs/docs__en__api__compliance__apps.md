# Apps

# Chats

## List

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

## Delete

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

## Domain Types

### Chat List Response

- `ChatListResponse = object { id, created_at, deleted_at, 8 more }`

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

- `ChatDeleteResponse = object { id, type }`

  Response for deleting a Claude chat.

  - `id: string`

    The ID of the Claude chat that was deleted

  - `type: optional "claude_chat_deleted"`

    Constant string confirming deletion

    - `"claude_chat_deleted"`

### Chat Messages Response

- `ChatMessagesResponse = object { id, chat_messages, created_at, 12 more }`

  Complete chat conversation data for compliance purposes.

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

# Generated Files

## Content

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

### Generated File Content Response

- `GeneratedFileContentResponse = unknown`

# Projects

## List

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

- `data: array of object { id, created_at, is_private, 4 more }`

  List of projects sorted by creation date ascending

  - `id: string`

    Project identifier (tagged ID)

  - `created_at: string`

    Project creation timestamp

  - `is_private: boolean`

    If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

  - `name: string`

    Project name

  - `organization_id: string`

    Organization identifier (tagged ID)

  - `updated_at: string`

    Project last update timestamp

  - `user: object { id, email_address }`

    User information for project creator.

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

## Retrieve

**get** `/v1/compliance/apps/projects/{project_id}`

Get detailed information for a specific project.

Returns:
Detailed project information including description, instructions, and counts

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

- `updated_at: string`

  Project last update timestamp

- `user: object { id, email_address }`

  User information for project creator.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Delete

**delete** `/v1/compliance/apps/projects/{project_id}`

Delete a project for compliance purposes.

Hard-deletes the project and all its associated data including:

- All project documents and files
- All role assignments
- Knowledge base (if RAG is enabled)
- Sync sources

Project must have no attached chats - returns 409 if chats exist.

Returns:
ClaudeProjectDeleteResponse confirming the deletion

Raises:
ConflictException: If project has chats attached
NotFoundException: If project doesn't exist or already deleted

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

## Attachments

**get** `/v1/compliance/apps/projects/{project_id}/attachments`

List files and documents attached to a project.

List files and project documents attached to the project referenced by project_id.
This includes the IDs of attached files, and attached project documents.

The raw binary content of attached files can be downloaded using the
GET /v1/compliance/apps/chats/files/{claude_file_id}/content endpoint.

The text content of attached project documents can be fetched using the
GET /v1/compliance/apps/projects/documents/{claude_proj_doc_id} endpoint.

Returns:
List of project attachments with pagination info

Raises:
NotFoundException: If project doesn't exist or project_id format is invalid

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

  - `ComplianceProjectFileReference = object { id, created_at, filename, 2 more }`

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

  - `ComplianceProjectDocReference = object { id, created_at, filename, 2 more }`

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

## Domain Types

### Project List Response

- `ProjectListResponse = object { id, created_at, is_private, 4 more }`

  Project information for compliance responses.

  - `id: string`

    Project identifier (tagged ID)

  - `created_at: string`

    Project creation timestamp

  - `is_private: boolean`

    If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

  - `name: string`

    Project name

  - `organization_id: string`

    Organization identifier (tagged ID)

  - `updated_at: string`

    Project last update timestamp

  - `user: object { id, email_address }`

    User information for project creator.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

### Project Retrieve Response

- `ProjectRetrieveResponse = object { id, attachments_count, chats_count, 8 more }`

  Detailed project information for compliance responses.

  - `id: string`

    Project identifier (tagged ID)

  - `attachments_count: number`

    Number of attachments contained within this project

  - `chats_count: number`

    Number of chats contained within this project

  - `created_at: string`

    Project creation timestamp

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

  - `updated_at: string`

    Project last update timestamp

  - `user: object { id, email_address }`

    User information for project creator.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

### Project Delete Response

- `ProjectDeleteResponse = object { id, type }`

  Response for deleting a Claude project.

  - `id: string`

    The ID of the Claude project that was deleted

  - `type: optional "claude_project_deleted"`

    Constant string confirming deletion.

    - `"claude_project_deleted"`

### Project Attachments Response

- `ProjectAttachmentsResponse = object { data, has_more, next_page }`

  List of project attachments with pagination info.

  - `data: array of object { id, created_at, filename, 2 more }  or object { id, created_at, filename, 2 more }`

    List of attachments sorted chronologically by created_at, tie break by id

    - `ComplianceProjectFileReference = object { id, created_at, filename, 2 more }`

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

    - `ComplianceProjectDocReference = object { id, created_at, filename, 2 more }`

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

# Documents

## Retrieve

**get** `/v1/compliance/apps/projects/documents/{document_id}`

Get detailed information for a specific project document.

Returns:
Project document information including content and metadata

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

  User information for project creator.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Delete

**delete** `/v1/compliance/apps/projects/documents/{document_id}`

Delete a project document for compliance purposes.

Hard-deletes the project document permanently.

Returns:
ComplianceProjectDocumentDeleteResponse confirming the deletion

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

## Domain Types

### Document Retrieve Response

- `DocumentRetrieveResponse = object { id, content, created_at, 2 more }`

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

    User information for project creator.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

### Document Delete Response

- `DocumentDeleteResponse = object { id, type }`

  Response for deleting a project document.

  - `id: string`

    The ID of the project document that was deleted

  - `type: "claude_project_document_deleted"`

    Constant string confirming deletion.

    - `"claude_project_document_deleted"`

# Artifacts

## Content

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

### Artifact Content Response

- `ArtifactContentResponse = unknown`

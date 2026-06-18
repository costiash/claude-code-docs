## List chats

**get** `/v1/compliance/apps/chats`

Lists chat metadata with filtering capabilities for targeted
compliance review. Results are sorted chronologically (time ascending)
by created_at, with ties broken by id.

### Query Parameters

- `after_id: optional string`

  Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `before_id: optional string`

  Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

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

  Filter by project IDs (accepts `claude_proj_...`). Enumerate IDs via `GET /v1/compliance/apps/projects`. Requires user_ids[]; not supported for org-wide queries.

- `updated_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter chats updated after this time (RFC 3339 format). Requires user_ids[]; not supported for org-wide queries.

  - `gte: optional string`

    Filter chats updated at or after this time (RFC 3339 format). Requires user_ids[]; not supported for org-wide queries.

  - `lt: optional string`

    Filter chats updated before this time (RFC 3339 format). Requires user_ids[]; not supported for org-wide queries.

  - `lte: optional string`

    Filter chats updated at or before this time (RFC 3339 format). Requires user_ids[]; not supported for org-wide queries.

- `user_ids: optional array of string`

  Filter to chats created by specific users (max 10 per request). Omit for an org-wide query. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

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

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

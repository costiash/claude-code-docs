## List

**get** `/v1/compliance/groups`

List Compliance Groups

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `name_prefix: optional string`

  Filter groups by name prefix

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, description, 4 more }`

  List of groups

  - `id: string`

    Group identifier (tagged ID)

  - `created_at: string`

    Group creation timestamp (ISO 8601)

  - `description: string`

    Group description

  - `name: string`

    Group name

  - `roles: array of string`

    Role IDs assigned to this group.

  - `source_type: string`

    How the group was created ('direct' or 'scim')

  - `updated_at: string`

    Group last-updated timestamp (ISO 8601)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/groups \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## List

**get** `/v1/compliance/organizations/{org_uuid}/users`

List current user members of an organization.

Returns:
List of user members with pagination info

### Path Parameters

- `org_uuid: string`

  The organization UUID

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, email, full_name }`

  List of current organization members sorted by account creation date ascending

  - `id: string`

    User identifier (tagged ID)

  - `created_at: string`

    User account creation timestamp

  - `email: string`

    User's current email address

  - `full_name: string`

    User's current full name

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/users \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

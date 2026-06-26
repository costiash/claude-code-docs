## List Compliance Roles

**get** `/v1/compliance/organizations/{org_uuid}/roles`

List Compliance Roles

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

- `data: array of object { id, created_at, description, 2 more }`

  List of roles

  - `id: string`

    Role identifier (tagged ID)

  - `created_at: string`

    Role creation timestamp (ISO 8601)

  - `description: string`

    Role description

  - `name: string`

    Role name

  - `updated_at: string`

    Role last-updated timestamp (ISO 8601)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
      "created_at": "2025-03-12T18:22:41.123456",
      "description": "Full administrative access to organization settings and members",
      "name": "Organization Admin",
      "updated_at": "2025-03-14T09:05:17.456789"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

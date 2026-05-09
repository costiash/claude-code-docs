# Members

## List

**get** `/v1/compliance/groups/{group_id}/members`

List Compliance Group Members

### Path Parameters

- `group_id: string`

  The group ID (tagged ID, e.g., rbac_group_abc123)

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { created_at, email, updated_at, user_id }`

  List of group members

  - `created_at: string`

    Membership creation timestamp (ISO 8601)

  - `email: string`

    Member email address

  - `updated_at: string`

    Membership last-updated timestamp (ISO 8601)

  - `user_id: string`

    Member user identifier (tagged ID)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID/members \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Member List Response

- `MemberListResponse = object { created_at, email, updated_at, user_id }`

  Group member for compliance responses.

  - `created_at: string`

    Membership creation timestamp (ISO 8601)

  - `email: string`

    Member email address

  - `updated_at: string`

    Membership last-updated timestamp (ISO 8601)

  - `user_id: string`

    Member user identifier (tagged ID)

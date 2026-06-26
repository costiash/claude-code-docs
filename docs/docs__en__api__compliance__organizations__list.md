## List organizations

**get** `/v1/compliance/organizations`

List organizations under the parent organization.

Returns organizations sorted by creation date in ascending order. Use
`limit` and `page` to paginate: each response includes `has_more` and a
`next_page` token to pass on the next request.

### Query Parameters

- `limit: optional number`

  Maximum results (default: 1000, max: 1000)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { created_at, name, uuid }`

  List of organizations sorted by creation date, ascending

  - `created_at: string`

    Organization creation time (RFC 3339 format)

  - `name: string`

    Organization name

  - `uuid: string`

    Unique identifier for the organization (UUID format)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: optional string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "created_at": "2025-03-12T18:22:41.123456+00:00",
      "name": "Acme Corp",
      "uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

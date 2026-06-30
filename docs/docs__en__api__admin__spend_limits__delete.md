## Delete Spend Limit

**delete** `/v1/organizations/spend_limits/{spend_limit_id}`

Delete a per-user spend limit override.

The member falls back to any inherited spend limit at that period.
Seat-tier, group, and organization-level rows cannot be deleted via
this endpoint.

### Path Parameters

- `spend_limit_id: string`

  ID of the Spend Limit.

### Returns

- `id: string`

- `type: "spend_limit_deleted"`

  - `"spend_limit_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/spend_limits/$SPEND_LIMIT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "id",
  "type": "spend_limit_deleted"
}
```

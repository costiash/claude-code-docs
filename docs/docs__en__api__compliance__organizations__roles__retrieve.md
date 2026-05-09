## Retrieve

**get** `/v1/compliance/organizations/{org_uuid}/roles/{role_id}`

Get Compliance Role

### Path Parameters

- `org_uuid: string`

  The organization UUID

- `role_id: string`

  The role ID (tagged ID, e.g., rbac_role_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

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

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

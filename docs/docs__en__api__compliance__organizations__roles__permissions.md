# Permissions

## List

**get** `/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions`

List Compliance Role Permissions

### Path Parameters

- `org_uuid: string`

  The organization UUID

- `role_id: string`

  The role ID (tagged ID, e.g., rbac_role_abc123)

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { action, resource_id, resource_type }`

  List of permissions

  - `action: string`

    Action permitted on the resource

  - `resource_id: string`

    Identifier of the resource the permission applies to

  - `resource_type: string`

    Type of resource the permission applies to

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID/permissions \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Permission List Response

- `PermissionListResponse = object { action, resource_id, resource_type }`

  Permission granted by a role.

  - `action: string`

    Action permitted on the resource

  - `resource_id: string`

    Identifier of the resource the permission applies to

  - `resource_type: string`

    Type of resource the permission applies to

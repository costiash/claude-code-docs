# Organizations

## List

**get** `/v1/compliance/organizations`

List organizations under the parent organization.

Returns a list of organizations sorted by creation date in ascending order.
This endpoint does not support pagination and will return an error if the
response would exceed 1,000 organizations.

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

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Organization List Response

- `OrganizationListResponse = object { data }`

  List of organizations under a parent organization.

  - `data: array of object { created_at, name, uuid }`

    List of organizations sorted by creation date, ascending

    - `created_at: string`

      Organization creation time (RFC 3339 format)

    - `name: string`

      Organization name

    - `uuid: string`

      Unique identifier for the organization (UUID format)

# Users

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

## Domain Types

### User List Response

- `UserListResponse = object { id, created_at, email, full_name }`

  User member information for compliance responses.

  - `id: string`

    User identifier (tagged ID)

  - `created_at: string`

    User account creation timestamp

  - `email: string`

    User's current email address

  - `full_name: string`

    User's current full name

# Roles

## List

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

## Domain Types

### Role List Response

- `RoleListResponse = object { id, created_at, description, 2 more }`

  Role information for compliance responses.

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

### Role Retrieve Response

- `RoleRetrieveResponse = object { id, created_at, description, 2 more }`

  Role information for compliance responses.

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

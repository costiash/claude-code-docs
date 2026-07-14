## Get RBAC Role

**get** `/v1/organizations/rbac_roles/{role_id}`

Retrieve an RBAC Role by ID.

The RBAC Roles API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

### Path Parameters

- `role_id: string`

  ID of the RBAC Role.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `RbacRole object { id, created_at, name, 2 more }`

  - `id: string`

    ID of the RBAC Role.

  - `created_at: string`

    RFC 3339 datetime string indicating when the RBAC Role was created.

  - `name: string`

    Name of the RBAC Role.

  - `type: "rbac_role"`

    Object type.

    For RBAC Roles, this is always `"rbac_role"`.

    - `"rbac_role"`

  - `updated_at: string`

    RFC 3339 datetime string indicating when the RBAC Role was last updated.

### Example

```http
curl https://api.anthropic.com/v1/organizations/rbac_roles/$ROLE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Project Editor",
  "type": "rbac_role",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

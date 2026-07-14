## Create RBAC Group

**post** `/v1/organizations/rbac_groups`

Create an RBAC Group in the Claude Enterprise tenant. Groups created via the API have source type `"direct"`.

The RBAC Groups API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `name: string`

  Name of the RBAC Group. Not uniqueness-enforced.

### Returns

- `RbacGroup object { id, created_at, name, 4 more }`

  - `id: string`

    ID of the RBAC Group.

  - `created_at: string`

    RFC 3339 timestamp of when the RBAC Group was created.

  - `name: string`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `roles: array of string`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `source_type: "direct" or "scim"`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `"direct"`

    - `"scim"`

  - `type: "rbac_group"`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

    - `"rbac_group"`

  - `updated_at: string`

    RFC 3339 timestamp of when the RBAC Group was last updated.

### Example

```http
curl https://api.anthropic.com/v1/organizations/rbac_groups \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "name": "Engineering"
        }'
```

#### Response

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Engineering",
  "roles": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "source_type": "direct",
  "type": "rbac_group",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

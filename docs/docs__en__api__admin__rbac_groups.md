# RBAC Groups

## List RBAC Groups

**get** `/v1/organizations/rbac_groups`

List RBAC Groups in the Claude Enterprise tenant.

The RBAC Groups API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

### Query Parameters

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `data: array of RbacGroup`

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

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `next_page: string`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```http
curl https://api.anthropic.com/v1/organizations/rbac_groups \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
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
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

## Get RBAC Group

**get** `/v1/organizations/rbac_groups/{group_id}`

Retrieve an RBAC Group by ID.

The RBAC Groups API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

### Path Parameters

- `group_id: string`

  ID of the RBAC Group.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

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
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
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

## Update RBAC Group

**post** `/v1/organizations/rbac_groups/{group_id}`

Update an RBAC Group's name. Groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API.

The RBAC Groups API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

### Path Parameters

- `group_id: string`

  ID of the RBAC Group.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `name: optional string`

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
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID \
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

## Delete RBAC Group

**delete** `/v1/organizations/rbac_groups/{group_id}`

Delete an RBAC Group. Groups provisioned by an identity provider (source type `"scim"`) cannot be deleted via the API.

The RBAC Groups API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

### Path Parameters

- `group_id: string`

  ID of the RBAC Group.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `RbacGroupDeleted object { id, type }`

  - `id: string`

    ID of the RBAC Group.

  - `type: "rbac_group_deleted"`

    Deleted object type.

    For RBAC Groups, this is always `"rbac_group_deleted"`.

    - `"rbac_group_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_deleted"
}
```

## Domain Types

### Rbac Group

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

### Rbac Group Deleted

- `RbacGroupDeleted object { id, type }`

  - `id: string`

    ID of the RBAC Group.

  - `type: "rbac_group_deleted"`

    Deleted object type.

    For RBAC Groups, this is always `"rbac_group_deleted"`.

    - `"rbac_group_deleted"`

# Members

## List RBAC Group Members

**get** `/v1/organizations/rbac_groups/{group_id}/members`

List members of an RBAC Group.

The RBAC Groups API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

### Path Parameters

- `group_id: string`

  ID of the RBAC Group.

### Query Parameters

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `data: array of RbacGroupMember`

  - `created_at: string`

    RFC 3339 timestamp of when the User was added to the RBAC Group.

  - `email: string`

    Email of the User.

  - `group_id: string`

    ID of the RBAC Group.

  - `type: "rbac_group_member"`

    Object type.

    For RBAC Group Members, this is always `"rbac_group_member"`.

    - `"rbac_group_member"`

  - `user_id: string`

    ID of the User.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `next_page: string`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```http
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID/members \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "type": "rbac_group_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

## Add RBAC Group Member

**post** `/v1/organizations/rbac_groups/{group_id}/members`

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API.

The RBAC Groups API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

### Path Parameters

- `group_id: string`

  ID of the RBAC Group.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `user_id: string`

  ID of the User.

### Returns

- `RbacGroupMember object { created_at, email, group_id, 2 more }`

  - `created_at: string`

    RFC 3339 timestamp of when the User was added to the RBAC Group.

  - `email: string`

    Email of the User.

  - `group_id: string`

    ID of the RBAC Group.

  - `type: "rbac_group_member"`

    Object type.

    For RBAC Group Members, this is always `"rbac_group_member"`.

    - `"rbac_group_member"`

  - `user_id: string`

    ID of the User.

### Example

```http
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID/members \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        }'
```

#### Response

```json
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
}
```

## Remove RBAC Group Member

**delete** `/v1/organizations/rbac_groups/{group_id}/members/{user_id}`

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API.

The RBAC Groups API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

### Path Parameters

- `group_id: string`

  ID of the RBAC Group.

- `user_id: string`

  ID of the User.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `RbacGroupMemberDeleted object { group_id, type, user_id }`

  - `group_id: string`

    ID of the RBAC Group.

  - `type: "rbac_group_member_deleted"`

    Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

    - `"rbac_group_member_deleted"`

  - `user_id: string`

    ID of the User.

### Example

```http
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID/members/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
}
```

## Domain Types

### Rbac Group Member

- `RbacGroupMember object { created_at, email, group_id, 2 more }`

  - `created_at: string`

    RFC 3339 timestamp of when the User was added to the RBAC Group.

  - `email: string`

    Email of the User.

  - `group_id: string`

    ID of the RBAC Group.

  - `type: "rbac_group_member"`

    Object type.

    For RBAC Group Members, this is always `"rbac_group_member"`.

    - `"rbac_group_member"`

  - `user_id: string`

    ID of the User.

### Rbac Group Member Deleted

- `RbacGroupMemberDeleted object { group_id, type, user_id }`

  - `group_id: string`

    ID of the RBAC Group.

  - `type: "rbac_group_member_deleted"`

    Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

    - `"rbac_group_member_deleted"`

  - `user_id: string`

    ID of the User.

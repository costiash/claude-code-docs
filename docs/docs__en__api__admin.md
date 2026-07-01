# Admin

# Organizations

## Get Current Organization

**get** `/v1/organizations/me`

Retrieve information about the organization associated with the authenticated API key.

### Returns

- `Organization object { id, name, type }`

  - `id: string`

    ID of the Organization.

  - `name: string`

    Name of the Organization.

  - `type: "organization"`

    Object type.

    For Organizations, this is always `"organization"`.

    - `"organization"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/me \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "12345678-1234-5678-1234-567812345678",
  "name": "Organization Name",
  "type": "organization"
}
```

## Domain Types

### Organization

- `Organization object { id, name, type }`

  - `id: string`

    ID of the Organization.

  - `name: string`

    Name of the Organization.

  - `type: "organization"`

    Object type.

    For Organizations, this is always `"organization"`.

    - `"organization"`

# Invites

## Create Invite

**post** `/v1/organizations/invites`

Create Invite

### Body Parameters

- `email: string`

  Email of the User.

- `role: "billing" or "claude_code_user" or "developer" or "user"`

  Role for the invited User. Cannot be "admin".

  - `"billing"`

  - `"claude_code_user"`

  - `"developer"`

  - `"user"`

### Returns

- `Invite object { id, email, expires_at, 4 more }`

  - `id: string`

    ID of the Invite.

  - `email: string`

    Email of the User being invited.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the Invite expires.

  - `invited_at: string`

    RFC 3339 datetime string indicating when the Invite was created.

  - `role: "admin" or "billing" or "claude_code_user" or 2 more`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"user"`

  - `status: "accepted" or "deleted" or "expired" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"deleted"`

    - `"expired"`

    - `"pending"`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

    - `"invite"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/invites \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "email": "user@emaildomain.com",
          "role": "user"
        }'
```

#### Response

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "role": "user",
  "status": "pending",
  "type": "invite"
}
```

## Get Invite

**get** `/v1/organizations/invites/{invite_id}`

Get Invite

### Path Parameters

- `invite_id: string`

  ID of the Invite.

### Returns

- `Invite object { id, email, expires_at, 4 more }`

  - `id: string`

    ID of the Invite.

  - `email: string`

    Email of the User being invited.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the Invite expires.

  - `invited_at: string`

    RFC 3339 datetime string indicating when the Invite was created.

  - `role: "admin" or "billing" or "claude_code_user" or 2 more`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"user"`

  - `status: "accepted" or "deleted" or "expired" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"deleted"`

    - `"expired"`

    - `"pending"`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

    - `"invite"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "role": "user",
  "status": "pending",
  "type": "invite"
}
```

## List Invites

**get** `/v1/organizations/invites`

List Invites

### Query Parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

### Returns

- `data: array of Invite`

  - `id: string`

    ID of the Invite.

  - `email: string`

    Email of the User being invited.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the Invite expires.

  - `invited_at: string`

    RFC 3339 datetime string indicating when the Invite was created.

  - `role: "admin" or "billing" or "claude_code_user" or 2 more`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"user"`

  - `status: "accepted" or "deleted" or "expired" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"deleted"`

    - `"expired"`

    - `"pending"`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

    - `"invite"`

- `first_id: string`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```http
curl https://api.anthropic.com/v1/organizations/invites \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
      "email": "user@emaildomain.com",
      "expires_at": "2024-11-20T23:58:27.427722Z",
      "invited_at": "2024-10-30T23:58:27.427722Z",
      "role": "user",
      "status": "pending",
      "type": "invite"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Delete Invite

**delete** `/v1/organizations/invites/{invite_id}`

Delete Invite

### Path Parameters

- `invite_id: string`

  ID of the Invite.

### Returns

- `id: string`

  ID of the Invite.

- `type: "invite_deleted"`

  Deleted object type.

  For Invites, this is always `"invite_deleted"`.

  - `"invite_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "type": "invite_deleted"
}
```

## Domain Types

### Invite

- `Invite object { id, email, expires_at, 4 more }`

  - `id: string`

    ID of the Invite.

  - `email: string`

    Email of the User being invited.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the Invite expires.

  - `invited_at: string`

    RFC 3339 datetime string indicating when the Invite was created.

  - `role: "admin" or "billing" or "claude_code_user" or 2 more`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"user"`

  - `status: "accepted" or "deleted" or "expired" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"deleted"`

    - `"expired"`

    - `"pending"`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

    - `"invite"`

### Invite Delete Response

- `InviteDeleteResponse object { id, type }`

  - `id: string`

    ID of the Invite.

  - `type: "invite_deleted"`

    Deleted object type.

    For Invites, this is always `"invite_deleted"`.

    - `"invite_deleted"`

# Users

## Get User

**get** `/v1/organizations/users/{user_id}`

Get User

### Path Parameters

- `user_id: string`

  ID of the User.

### Returns

- `User object { id, added_at, email, 3 more }`

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: "admin" or "billing" or "claude_code_user" or 2 more`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"user"`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    - `"user"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "user",
  "type": "user"
}
```

## List Users

**get** `/v1/organizations/users`

List Users

### Query Parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `email: optional string`

  Filter by user email.

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

### Returns

- `data: array of User`

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: "admin" or "billing" or "claude_code_user" or 2 more`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"user"`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    - `"user"`

- `first_id: string`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```http
curl https://api.anthropic.com/v1/organizations/users \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "added_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "name": "Jane Doe",
      "role": "user",
      "type": "user"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Update User

**post** `/v1/organizations/users/{user_id}`

Update User

### Path Parameters

- `user_id: string`

  ID of the User.

### Body Parameters

- `role: "billing" or "claude_code_user" or "developer" or "user"`

  New role for the User. Cannot be "admin".

  - `"billing"`

  - `"claude_code_user"`

  - `"developer"`

  - `"user"`

### Returns

- `User object { id, added_at, email, 3 more }`

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: "admin" or "billing" or "claude_code_user" or 2 more`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"user"`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    - `"user"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "role": "user"
        }'
```

#### Response

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "user",
  "type": "user"
}
```

## Remove User

**delete** `/v1/organizations/users/{user_id}`

Remove User

### Path Parameters

- `user_id: string`

  ID of the User.

### Returns

- `id: string`

  ID of the User.

- `type: "user_deleted"`

  Deleted object type.

  For Users, this is always `"user_deleted"`.

  - `"user_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "type": "user_deleted"
}
```

## Domain Types

### User

- `User object { id, added_at, email, 3 more }`

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: "admin" or "billing" or "claude_code_user" or 2 more`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"user"`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    - `"user"`

### User Delete Response

- `UserDeleteResponse object { id, type }`

  - `id: string`

    ID of the User.

  - `type: "user_deleted"`

    Deleted object type.

    For Users, this is always `"user_deleted"`.

    - `"user_deleted"`

# Workspaces

## Create Workspace

**post** `/v1/organizations/workspaces`

Create Workspace

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `name: string`

  Name of the Workspace.

- `data_residency: optional object { allowed_inference_geos, default_inference_geo, workspace_geo }`

  Data residency configuration for the workspace. If omitted, defaults to workspace_geo=`"us"`, allowed_inference_geos=`"unrestricted"`, and default_inference_geo=`"global"`.

  - `allowed_inference_geos: optional array of string or "unrestricted"`

    Permitted inference geo values. Defaults to 'unrestricted' if omitted, which allows all geos. Use the string 'unrestricted' to allow all geos, or a list of specific geos.

    - `array of string`

    - `"unrestricted"`

      - `"unrestricted"`

  - `default_inference_geo: optional string`

    Default inference geo applied when requests omit the parameter. Defaults to 'global' if omitted. Must be a member of allowed_inference_geos unless allowed_inference_geos is `"unrestricted"`.

  - `workspace_geo: optional string`

    Geographic region for workspace data storage. Immutable after creation. Defaults to 'us' if omitted.

- `external_key_id: optional string`

  ID of the customer-managed encryption key (CMEK) configuration to use for this
  Workspace. Setting this field requires CMEK to be enabled for your
  organization. When set, data stored for this Workspace is encrypted with the
  referenced key. Create key configurations with the External Keys API. This
  field is write-once: once a key is attached to a Workspace it cannot be
  detached or replaced. To rotate key material, rotate the underlying key on
  your cloud KMS; the `external_key_id` stays the same.

- `tags: optional map[string]`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

### Returns

- `Workspace object { id, archived_at, compartment_id, 7 more }`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK), reference this value in your cloud
    provider's key configuration — an AWS KMS key-policy condition or an Azure Key
    Vault tag — so the key is scoped to this compartment. See the CMEK integration
    guide for the required key configuration, including the value used during key
    validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

  - `data_residency: object { allowed_inference_geos, default_inference_geo, workspace_geo }`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `array of string`

      - `"unrestricted"`

        - `"unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    - `"workspace"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "name": "x",
          "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
          "tags": {
            "env": "prod",
            "team": "platform"
          }
        }'
```

#### Response

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

## Get Workspace

**get** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

### Path Parameters

- `workspace_id: string`

  ID of the Workspace.

### Returns

- `Workspace object { id, archived_at, compartment_id, 7 more }`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK), reference this value in your cloud
    provider's key configuration — an AWS KMS key-policy condition or an Azure Key
    Vault tag — so the key is scoped to this compartment. See the CMEK integration
    guide for the required key configuration, including the value used during key
    validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

  - `data_residency: object { allowed_inference_geos, default_inference_geo, workspace_geo }`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `array of string`

      - `"unrestricted"`

        - `"unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    - `"workspace"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

## List Workspaces

**get** `/v1/organizations/workspaces`

List Workspaces

### Query Parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `include_archived: optional boolean`

  Whether to include Workspaces that have been archived in the response

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

### Returns

- `data: array of Workspace`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK), reference this value in your cloud
    provider's key configuration — an AWS KMS key-policy condition or an Azure Key
    Vault tag — so the key is scoped to this compartment. See the CMEK integration
    guide for the required key configuration, including the value used during key
    validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

  - `data_residency: object { allowed_inference_geos, default_inference_geo, workspace_geo }`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `array of string`

      - `"unrestricted"`

        - `"unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    - `"workspace"`

- `first_id: string`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "data_residency": {
        "allowed_inference_geos": "unrestricted",
        "default_inference_geo": "default_inference_geo",
        "workspace_geo": "workspace_geo"
      },
      "display_color": "#6C5BB9",
      "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "name": "Workspace Name",
      "tags": {
        "env": "prod",
        "team": "platform"
      },
      "type": "workspace"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Update Workspace

**post** `/v1/organizations/workspaces/{workspace_id}`

Update Workspace

### Path Parameters

- `workspace_id: string`

### Body Parameters

- `data_residency: optional object { allowed_inference_geos, default_inference_geo }`

  Data residency configuration for the workspace.

  - `allowed_inference_geos: optional array of string or "unrestricted"`

    Permitted inference geo values. Use 'unrestricted' to allow all geos, or a list of specific geos.

    - `array of string`

    - `"unrestricted"`

      - `"unrestricted"`

  - `default_inference_geo: optional string`

    Default inference geo applied when requests omit the parameter. Must be a member of allowed_inference_geos unless allowed_inference_geos is `"unrestricted"`.

- `external_key_id: optional string`

  ID of the customer-managed encryption key (CMEK) configuration to use for this
  Workspace. Setting this field requires CMEK to be enabled for your
  organization. When set, data stored for this Workspace is encrypted with the
  referenced key. Create key configurations with the External Keys API. This
  field is write-once: once a key is attached to a Workspace it cannot be
  detached or replaced. To rotate key material, rotate the underlying key on
  your cloud KMS; the `external_key_id` stays the same.

- `name: optional string`

  Name of the Workspace.

- `tags: optional map[string]`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

### Returns

- `Workspace object { id, archived_at, compartment_id, 7 more }`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK), reference this value in your cloud
    provider's key configuration — an AWS KMS key-policy condition or an Azure Key
    Vault tag — so the key is scoped to this compartment. See the CMEK integration
    guide for the required key configuration, including the value used during key
    validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

  - `data_residency: object { allowed_inference_geos, default_inference_geo, workspace_geo }`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `array of string`

      - `"unrestricted"`

        - `"unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    - `"workspace"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
          "tags": {
            "env": "prod",
            "team": "platform"
          }
        }'
```

#### Response

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

## Archive Workspace

**post** `/v1/organizations/workspaces/{workspace_id}/archive`

Archive Workspace

### Path Parameters

- `workspace_id: string`

### Returns

- `Workspace object { id, archived_at, compartment_id, 7 more }`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK), reference this value in your cloud
    provider's key configuration — an AWS KMS key-policy condition or an Azure Key
    Vault tag — so the key is scoped to this compartment. See the CMEK integration
    guide for the required key configuration, including the value used during key
    validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

  - `data_residency: object { allowed_inference_geos, default_inference_geo, workspace_geo }`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `array of string`

      - `"unrestricted"`

        - `"unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    - `"workspace"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

# Members

## Create Workspace Member

**post** `/v1/organizations/workspaces/{workspace_id}/members`

Create Workspace Member

### Path Parameters

- `workspace_id: string`

  ID of the Workspace.

### Body Parameters

- `user_id: string`

  ID of the User.

- `workspace_role: "workspace_admin" or "workspace_developer" or "workspace_restricted_developer" or "workspace_user"`

  Role of the new Workspace Member. Cannot be "workspace_billing".

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

### Returns

- `WorkspaceMember object { type, user_id, workspace_id, workspace_role }`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    - `"workspace_member"`

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "workspace_role": "workspace_admin"
        }'
```

#### Response

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_user"
}
```

## Get Workspace Member

**get** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Get Workspace Member

### Path Parameters

- `workspace_id: string`

  ID of the Workspace.

- `user_id: string`

  ID of the User.

### Returns

- `WorkspaceMember object { type, user_id, workspace_id, workspace_role }`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    - `"workspace_member"`

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_user"
}
```

## List Workspace Members

**get** `/v1/organizations/workspaces/{workspace_id}/members`

List Workspace Members

### Path Parameters

- `workspace_id: string`

  ID of the Workspace.

### Query Parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

### Returns

- `data: array of WorkspaceMember`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    - `"workspace_member"`

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

- `first_id: string`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "type": "workspace_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "workspace_role": "workspace_user"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Update Workspace Member

**post** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Update Workspace Member

### Path Parameters

- `workspace_id: string`

  ID of the Workspace.

- `user_id: string`

  ID of the User.

### Body Parameters

- `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

  New workspace role for the User.

  - `"workspace_admin"`

  - `"workspace_billing"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

### Returns

- `WorkspaceMember object { type, user_id, workspace_id, workspace_role }`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    - `"workspace_member"`

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "workspace_role": "workspace_admin"
        }'
```

#### Response

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_user"
}
```

## Delete Workspace Member

**delete** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Delete Workspace Member

### Path Parameters

- `workspace_id: string`

  ID of the Workspace.

- `user_id: string`

  ID of the User.

### Returns

- `type: "workspace_member_deleted"`

  Deleted object type.

  For Workspace Members, this is always `"workspace_member_deleted"`.

  - `"workspace_member_deleted"`

- `user_id: string`

  ID of the User.

- `workspace_id: string`

  ID of the Workspace.

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "type": "workspace_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## Domain Types

### Workspace Member

- `WorkspaceMember object { type, user_id, workspace_id, workspace_role }`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    - `"workspace_member"`

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

### Member Delete Response

- `MemberDeleteResponse object { type, user_id, workspace_id }`

  - `type: "workspace_member_deleted"`

    Deleted object type.

    For Workspace Members, this is always `"workspace_member_deleted"`.

    - `"workspace_member_deleted"`

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

# Rate Limits

## List Workspace Rate Limits

**get** `/v1/organizations/workspaces/{workspace_id}/rate_limits`

List rate-limit overrides configured for a workspace.

Returns only the groups and limiter types that have a workspace-level
override. Groups without overrides inherit the organization limits and
are not listed; use `GET /v1/organizations/rate_limits` to see those.

### Path Parameters

- `workspace_id: string`

  The ID of the workspace.

### Query Parameters

- `group_type: optional "batch" or "files" or "model_group" or 3 more`

  Filter by group type.

  - `"batch"`

  - `"files"`

  - `"model_group"`

  - `"skills"`

  - `"token_count"`

  - `"web_search"`

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Returns

- `data: array of object { group_type, limits, models, type }`

  Rate-limit entries for the workspace, one per group that has at least one override.

  - `group_type: "batch" or "files" or "model_group" or 3 more`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `"batch"`

    - `"files"`

    - `"model_group"`

    - `"skills"`

    - `"token_count"`

    - `"web_search"`

  - `limits: array of object { org_limit, type, value }`

    The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

    - `org_limit: number`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `type: string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `value: number`

      The workspace-level override value for this limiter type.

  - `models: array of string`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `type: "workspace_rate_limit"`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

    - `"workspace_rate_limit"`

- `next_page: string`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "group_type": "batch",
      "limits": [
        {
          "org_limit": 0,
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "type": "workspace_rate_limit"
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Rate Limit List Response

- `RateLimitListResponse object { data, next_page }`

  - `data: array of object { group_type, limits, models, type }`

    Rate-limit entries for the workspace, one per group that has at least one override.

    - `group_type: "batch" or "files" or "model_group" or 3 more`

      The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

      - `"batch"`

      - `"files"`

      - `"model_group"`

      - `"skills"`

      - `"token_count"`

      - `"web_search"`

    - `limits: array of object { org_limit, type, value }`

      The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

      - `org_limit: number`

        The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

      - `type: string`

        The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

      - `value: number`

        The workspace-level override value for this limiter type.

    - `models: array of string`

      Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

    - `type: "workspace_rate_limit"`

      Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

      - `"workspace_rate_limit"`

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

# Service Accounts

## Create Service Account Workspace Member

**post** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

Add a service account to a workspace with the given `workspace_role`.

The role determines what the service account can do in the workspace and
which workspace-scoped permissions it can be granted when authenticating
through federation. Every service account is already an implicit
`workspace_user` member of the default workspace; adding it explicitly
assigns a chosen role. If the service account is already an explicit
member of the workspace, its `workspace_role` is replaced with the
value supplied here. Archived workspaces return 400. Archived service
accounts cannot be added and are rejected. Requires an OAuth bearer or
Console session; Admin API keys are not accepted.

### Path Parameters

- `workspace_id: string`

  ID of the workspace.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `service_account_id: string`

  Tagged service account ID to add.

- `workspace_role: "workspace_admin" or "workspace_developer" or "workspace_restricted_developer" or "workspace_user"`

  Role to assign to the service account in this workspace.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

### Returns

- `created_by_actor_id: string`

  Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

- `implicit: boolean`

  True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

- `service_account_id: string`

  Tagged service account ID (`svac_...`).

- `type: "service_account_workspace_member"`

  - `"service_account_workspace_member"`

- `workspace_id: string`

  Tagged workspace ID (`wrkspc_...`).

- `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

  Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

  - `"workspace_admin"`

  - `"workspace_billing"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "service_account_id": "service_account_id",
          "workspace_role": "workspace_admin"
        }'
```

#### Response

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

## Get Service Account Workspace Member

**get** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

Retrieve a service account's membership in a workspace.

Returns the membership record, including the service account's
`workspace_role` in this workspace. Archived workspaces return 400. For
the default workspace, returns the implicit (`implicit: true`)
membership when no explicit membership exists; an explicitly added
membership is returned with its assigned role. An archived service
account returns 404.

### Path Parameters

- `workspace_id: string`

  ID of the workspace.

- `service_account_id: string`

  ID of the service account.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `created_by_actor_id: string`

  Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

- `implicit: boolean`

  True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

- `service_account_id: string`

  Tagged service account ID (`svac_...`).

- `type: "service_account_workspace_member"`

  - `"service_account_workspace_member"`

- `workspace_id: string`

  Tagged workspace ID (`wrkspc_...`).

- `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

  Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

  - `"workspace_admin"`

  - `"workspace_billing"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

## List Service Account Workspace Members

**get** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

List the service accounts that are members of a workspace.

Each entry includes the service account's `workspace_role`. Use `limit`
and the `next_page` cursor to paginate. Archived workspaces return 400;
use `GET /service_accounts/{id}/workspaces` to audit memberships of an
archived workspace. The implicit default-workspace membership is not
included in this list. Memberships of archived service accounts are
omitted from the results.

### Path Parameters

- `workspace_id: string`

  ID of the workspace.

### Query Parameters

- `limit: optional number`

  Number of results per page.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `data: array of object { created_by_actor_id, implicit, service_account_id, 3 more }`

  - `created_by_actor_id: string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    - `"service_account_workspace_member"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

- `next_page: string`

  Opaque cursor for the next page, or null if no more results.

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
    }
  ],
  "next_page": "next_page"
}
```

## Update Service Account Workspace Member

**post** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

Change a service account's role in a workspace.

The new `workspace_role` replaces the current one. Only explicit
memberships can be updated; to set a role on the implicit
default-workspace membership, add the service account explicitly with
`POST /workspaces/{workspace_id}/service_accounts`. Archived workspaces
return 400. Archived service accounts cannot be updated and are
rejected. Requires an OAuth bearer or Console session; Admin API keys
are not accepted.

### Path Parameters

- `workspace_id: string`

  ID of the workspace.

- `service_account_id: string`

  ID of the service account.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `workspace_role: "workspace_admin" or "workspace_developer" or "workspace_restricted_developer" or "workspace_user"`

  New role for the service account in this workspace.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

### Returns

- `created_by_actor_id: string`

  Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

- `implicit: boolean`

  True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

- `service_account_id: string`

  Tagged service account ID (`svac_...`).

- `type: "service_account_workspace_member"`

  - `"service_account_workspace_member"`

- `workspace_id: string`

  Tagged workspace ID (`wrkspc_...`).

- `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

  Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

  - `"workspace_admin"`

  - `"workspace_billing"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "workspace_role": "workspace_admin"
        }'
```

#### Response

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

## Delete Service Account Workspace Member

**delete** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

Remove a service account from a workspace.

Removal is idempotent (returns 200 even if the membership was already
removed). A DELETE against the implicit default-workspace membership
returns 200 but is a no-op and the membership persists; deleting an
explicit default-workspace row reverts to the implicit `workspace_user`
membership. Archived workspaces return 400. Requires an OAuth bearer or
Console session; Admin API keys are not accepted.

### Path Parameters

- `workspace_id: string`

  ID of the workspace.

- `service_account_id: string`

  ID of the service account.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `service_account_id: string`

  Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

- `type: "service_account_workspace_member_deleted"`

  - `"service_account_workspace_member_deleted"`

- `workspace_id: string`

  Tagged workspace ID (`wrkspc_...`) named in the delete request.

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts/$SERVICE_ACCOUNT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
}
```

## Domain Types

### Service Account Create Response

- `ServiceAccountCreateResponse object { created_by_actor_id, implicit, service_account_id, 3 more }`

  - `created_by_actor_id: string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    - `"service_account_workspace_member"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

### Service Account Retrieve Response

- `ServiceAccountRetrieveResponse object { created_by_actor_id, implicit, service_account_id, 3 more }`

  - `created_by_actor_id: string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    - `"service_account_workspace_member"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

### Service Account List Response

- `ServiceAccountListResponse object { created_by_actor_id, implicit, service_account_id, 3 more }`

  - `created_by_actor_id: string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    - `"service_account_workspace_member"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

### Service Account Update Response

- `ServiceAccountUpdateResponse object { created_by_actor_id, implicit, service_account_id, 3 more }`

  - `created_by_actor_id: string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    - `"service_account_workspace_member"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

### Service Account Delete Response

- `ServiceAccountDeleteResponse object { service_account_id, type, workspace_id }`

  - `service_account_id: string`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `type: "service_account_workspace_member_deleted"`

    - `"service_account_workspace_member_deleted"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

# API Keys

## Get API Key

**get** `/v1/organizations/api_keys/{api_key_id}`

Get API Key

### Path Parameters

- `api_key_id: string`

  ID of the API key.

### Returns

- `APIKey object { id, created_at, created_by, 6 more }`

  - `id: string`

    ID of the API key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the API Key was created.

  - `created_by: object { id, type }`

    The ID and type of the actor that created the API key.

    - `id: string`

      ID of the actor that created the object.

    - `type: string`

      Type of the actor that created the object.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

  - `name: string`

    Name of the API key.

  - `partial_key_hint: string`

    Partially redacted hint for the API key.

  - `status: "active" or "archived" or "expired" or "inactive"`

    Status of the API key.

    - `"active"`

    - `"archived"`

    - `"expired"`

    - `"inactive"`

  - `type: "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

    - `"api_key"`

  - `workspace_id: string`

    ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace.

### Example

```http
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## List API Keys

**get** `/v1/organizations/api_keys`

List API Keys

### Query Parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `created_by_user_id: optional string`

  Filter by the ID of the User who created the object.

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `status: optional "active" or "archived" or "expired" or "inactive"`

  Filter by API key status.

  - `"active"`

  - `"archived"`

  - `"expired"`

  - `"inactive"`

- `workspace_id: optional string`

  Filter by Workspace ID.

### Returns

- `data: array of APIKey`

  - `id: string`

    ID of the API key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the API Key was created.

  - `created_by: object { id, type }`

    The ID and type of the actor that created the API key.

    - `id: string`

      ID of the actor that created the object.

    - `type: string`

      Type of the actor that created the object.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

  - `name: string`

    Name of the API key.

  - `partial_key_hint: string`

    Partially redacted hint for the API key.

  - `status: "active" or "archived" or "expired" or "inactive"`

    Status of the API key.

    - `"active"`

    - `"archived"`

    - `"expired"`

    - `"inactive"`

  - `type: "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

    - `"api_key"`

  - `workspace_id: string`

    ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace.

- `first_id: string`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```http
curl https://api.anthropic.com/v1/organizations/api_keys \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "type": "user"
      },
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "name": "Developer Key",
      "partial_key_hint": "sk-ant-api03-R2D...igAA",
      "status": "active",
      "type": "api_key",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Update API Key

**post** `/v1/organizations/api_keys/{api_key_id}`

Update API Key

### Path Parameters

- `api_key_id: string`

  ID of the API key.

### Body Parameters

- `name: optional string`

  Name of the API key.

- `status: optional "active" or "archived" or "inactive"`

  Status of the API key.

  - `"active"`

  - `"archived"`

  - `"inactive"`

### Returns

- `APIKey object { id, created_at, created_by, 6 more }`

  - `id: string`

    ID of the API key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the API Key was created.

  - `created_by: object { id, type }`

    The ID and type of the actor that created the API key.

    - `id: string`

      ID of the actor that created the object.

    - `type: string`

      Type of the actor that created the object.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

  - `name: string`

    Name of the API key.

  - `partial_key_hint: string`

    Partially redacted hint for the API key.

  - `status: "active" or "archived" or "expired" or "inactive"`

    Status of the API key.

    - `"active"`

    - `"archived"`

    - `"expired"`

    - `"inactive"`

  - `type: "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

    - `"api_key"`

  - `workspace_id: string`

    ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace.

### Example

```http
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

#### Response

```json
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

# External Keys

## Create External Key

**post** `/v1/organizations/external_keys`

Create an external key config owned by the caller's organization.

### Body Parameters

- `provider_config: object { kms_arn, type, region, role_arn }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

  KMS provider identity and auth coordinates.

  - `Aws object { kms_arn, type, region, role_arn }`

    - `kms_arn: string`

      Full ARN of the AWS KMS key.

    - `type: "aws"`

      - `"aws"`

    - `region: optional string`

      AWS region. Derived from kms_arn if omitted.

    - `role_arn: optional string`

      IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

  - `Gcp object { key_name, type }`

    - `key_name: string`

      Full resource name of the Cloud KMS key.

    - `type: "gcp"`

      - `"gcp"`

  - `Azure object { key_name, tenant_id, type, 2 more }`

    - `key_name: string`

      Name of the key within the vault.

    - `tenant_id: string`

      Azure AD tenant ID.

    - `type: "azure"`

      - `"azure"`

    - `vault_uri: string`

      Key Vault URI.

    - `client_id: optional string`

      Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

- `display_name: optional string`

  Human-friendly display name.

- `geo: optional "us"`

  Data residency geo. Only `us` is supported.

  - `"us"`

### Returns

- `id: string`

  Tagged ID of the external key config.

- `created_at: string`

- `display_name: string`

  Human-friendly display name. Null if none was set.

- `geo: string`

  Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

- `provider_config: object { kms_arn, type, region, role_arn }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

  KMS provider identity and auth coordinates.

  - `Aws object { kms_arn, type, region, role_arn }`

    - `kms_arn: string`

      Full ARN of the AWS KMS key.

    - `type: "aws"`

      - `"aws"`

    - `region: optional string`

      AWS region. Derived from kms_arn if omitted.

    - `role_arn: optional string`

      IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

  - `Gcp object { key_name, type }`

    - `key_name: string`

      Full resource name of the Cloud KMS key.

    - `type: "gcp"`

      - `"gcp"`

  - `Azure object { key_name, tenant_id, type, 2 more }`

    - `key_name: string`

      Name of the key within the vault.

    - `tenant_id: string`

      Azure AD tenant ID.

    - `type: "azure"`

      - `"azure"`

    - `vault_uri: string`

      Key Vault URI.

    - `client_id: optional string`

      Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

- `type: "external_key"`

  - `"external_key"`

- `updated_at: string`

### Example

```http
curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "provider_config": {
            "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
            "type": "aws"
          }
        }'
```

#### Response

```json
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

## List External Keys

**get** `/v1/organizations/external_keys`

List external key configs in the caller's organization.

Results are ordered by creation time (newest first). Use the
`next_page` cursor from the response to fetch subsequent pages.

### Query Parameters

- `limit: optional number`

  Number of results per page.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Returns

- `data: array of object { id, created_at, display_name, 4 more }`

  - `id: string`

    Tagged ID of the external key config.

  - `created_at: string`

  - `display_name: string`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: object { kms_arn, type, region, role_arn }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

    KMS provider identity and auth coordinates.

    - `Aws object { kms_arn, type, region, role_arn }`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

      - `type: "aws"`

        - `"aws"`

      - `region: optional string`

        AWS region. Derived from kms_arn if omitted.

      - `role_arn: optional string`

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `Gcp object { key_name, type }`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

      - `type: "gcp"`

        - `"gcp"`

    - `Azure object { key_name, tenant_id, type, 2 more }`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `type: "azure"`

        - `"azure"`

      - `vault_uri: string`

        Key Vault URI.

      - `client_id: optional string`

        Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    - `"external_key"`

  - `updated_at: string`

- `next_page: string`

  Opaque cursor for the next page, or null if no more results. Pass as `?page=` to fetch the next page.

### Example

```http
curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "prod-us-key",
      "geo": "us",
      "provider_config": {
        "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
        "type": "aws",
        "region": "us-east-1",
        "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
      },
      "type": "external_key",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "next_page": "next_page"
}
```

## Get External Key

**get** `/v1/organizations/external_keys/{external_key_id}`

Retrieve a single external key config in the caller's organization by ID.

### Path Parameters

- `external_key_id: string`

  ID of the External Key.

### Returns

- `id: string`

  Tagged ID of the external key config.

- `created_at: string`

- `display_name: string`

  Human-friendly display name. Null if none was set.

- `geo: string`

  Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

- `provider_config: object { kms_arn, type, region, role_arn }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

  KMS provider identity and auth coordinates.

  - `Aws object { kms_arn, type, region, role_arn }`

    - `kms_arn: string`

      Full ARN of the AWS KMS key.

    - `type: "aws"`

      - `"aws"`

    - `region: optional string`

      AWS region. Derived from kms_arn if omitted.

    - `role_arn: optional string`

      IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

  - `Gcp object { key_name, type }`

    - `key_name: string`

      Full resource name of the Cloud KMS key.

    - `type: "gcp"`

      - `"gcp"`

  - `Azure object { key_name, tenant_id, type, 2 more }`

    - `key_name: string`

      Name of the key within the vault.

    - `tenant_id: string`

      Azure AD tenant ID.

    - `type: "azure"`

      - `"azure"`

    - `vault_uri: string`

      Key Vault URI.

    - `client_id: optional string`

      Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

- `type: "external_key"`

  - `"external_key"`

- `updated_at: string`

### Example

```http
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

## Update External Key

**post** `/v1/organizations/external_keys/{external_key_id}`

Partially update an external key config. Omitted fields are left unchanged.

`display_name` is always editable. `geo` and `provider_config` cannot
be changed once any workspace references this config, because previously
encrypted data requires the original key identity to decrypt.

### Path Parameters

- `external_key_id: string`

  ID of the External Key to update.

### Body Parameters

- `display_name: optional string`

  Human-friendly display name.

- `geo: optional "us"`

  Data residency geo. Only `us` is supported.

  - `"us"`

- `provider_config: optional object { kms_arn, type, region, role_arn }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

  KMS provider identity and auth coordinates.

  - `Aws object { kms_arn, type, region, role_arn }`

    - `kms_arn: string`

      Full ARN of the AWS KMS key.

    - `type: "aws"`

      - `"aws"`

    - `region: optional string`

      AWS region. Derived from kms_arn if omitted.

    - `role_arn: optional string`

      IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

  - `Gcp object { key_name, type }`

    - `key_name: string`

      Full resource name of the Cloud KMS key.

    - `type: "gcp"`

      - `"gcp"`

  - `Azure object { key_name, tenant_id, type, 2 more }`

    - `key_name: string`

      Name of the key within the vault.

    - `tenant_id: string`

      Azure AD tenant ID.

    - `type: "azure"`

      - `"azure"`

    - `vault_uri: string`

      Key Vault URI.

    - `client_id: optional string`

      Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

### Returns

- `id: string`

  Tagged ID of the external key config.

- `created_at: string`

- `display_name: string`

  Human-friendly display name. Null if none was set.

- `geo: string`

  Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

- `provider_config: object { kms_arn, type, region, role_arn }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

  KMS provider identity and auth coordinates.

  - `Aws object { kms_arn, type, region, role_arn }`

    - `kms_arn: string`

      Full ARN of the AWS KMS key.

    - `type: "aws"`

      - `"aws"`

    - `region: optional string`

      AWS region. Derived from kms_arn if omitted.

    - `role_arn: optional string`

      IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

  - `Gcp object { key_name, type }`

    - `key_name: string`

      Full resource name of the Cloud KMS key.

    - `type: "gcp"`

      - `"gcp"`

  - `Azure object { key_name, tenant_id, type, 2 more }`

    - `key_name: string`

      Name of the key within the vault.

    - `tenant_id: string`

      Azure AD tenant ID.

    - `type: "azure"`

      - `"azure"`

    - `vault_uri: string`

      Key Vault URI.

    - `client_id: optional string`

      Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

- `type: "external_key"`

  - `"external_key"`

- `updated_at: string`

### Example

```http
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

#### Response

```json
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

## Delete External Key

**delete** `/v1/organizations/external_keys/{external_key_id}`

Delete an external key config.

The request is rejected if any workspace still references this config.

### Path Parameters

- `external_key_id: string`

  ID of the External Key to delete.

### Returns

- `id: string`

  ID of the deleted External Key.

- `type: "external_key_deleted"`

  - `"external_key_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"
}
```

## Validate External Key

**post** `/v1/organizations/external_keys/{external_key_id}/validate`

Validate an external key config against the customer's KMS.

Anthropic performs an encrypt/decrypt roundtrip against the configured
KMS key and waits up to 30 seconds for the result. The response status is
`success` if the roundtrip succeeded, or `failure` with an error
message if it failed or timed out.

### Path Parameters

- `external_key_id: string`

  ID of the External Key to validate.

### Returns

- `error: string`

  Error message when status is `failure`. Null otherwise.

- `status: "failure" or "success"`

  `success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

  - `"failure"`

  - `"success"`

- `type: "external_key_validation"`

  - `"external_key_validation"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID/validate \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "error": null,
  "status": "success",
  "type": "external_key_validation"
}
```

## Domain Types

### External Key Create Response

- `ExternalKeyCreateResponse object { id, created_at, display_name, 4 more }`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Tagged ID of the external key config.

  - `created_at: string`

  - `display_name: string`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: object { kms_arn, type, region, role_arn }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

    KMS provider identity and auth coordinates.

    - `Aws object { kms_arn, type, region, role_arn }`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

      - `type: "aws"`

        - `"aws"`

      - `region: optional string`

        AWS region. Derived from kms_arn if omitted.

      - `role_arn: optional string`

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `Gcp object { key_name, type }`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

      - `type: "gcp"`

        - `"gcp"`

    - `Azure object { key_name, tenant_id, type, 2 more }`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `type: "azure"`

        - `"azure"`

      - `vault_uri: string`

        Key Vault URI.

      - `client_id: optional string`

        Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    - `"external_key"`

  - `updated_at: string`

### External Key List Response

- `ExternalKeyListResponse object { id, created_at, display_name, 4 more }`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Tagged ID of the external key config.

  - `created_at: string`

  - `display_name: string`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: object { kms_arn, type, region, role_arn }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

    KMS provider identity and auth coordinates.

    - `Aws object { kms_arn, type, region, role_arn }`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

      - `type: "aws"`

        - `"aws"`

      - `region: optional string`

        AWS region. Derived from kms_arn if omitted.

      - `role_arn: optional string`

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `Gcp object { key_name, type }`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

      - `type: "gcp"`

        - `"gcp"`

    - `Azure object { key_name, tenant_id, type, 2 more }`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `type: "azure"`

        - `"azure"`

      - `vault_uri: string`

        Key Vault URI.

      - `client_id: optional string`

        Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    - `"external_key"`

  - `updated_at: string`

### External Key Retrieve Response

- `ExternalKeyRetrieveResponse object { id, created_at, display_name, 4 more }`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Tagged ID of the external key config.

  - `created_at: string`

  - `display_name: string`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: object { kms_arn, type, region, role_arn }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

    KMS provider identity and auth coordinates.

    - `Aws object { kms_arn, type, region, role_arn }`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

      - `type: "aws"`

        - `"aws"`

      - `region: optional string`

        AWS region. Derived from kms_arn if omitted.

      - `role_arn: optional string`

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `Gcp object { key_name, type }`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

      - `type: "gcp"`

        - `"gcp"`

    - `Azure object { key_name, tenant_id, type, 2 more }`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `type: "azure"`

        - `"azure"`

      - `vault_uri: string`

        Key Vault URI.

      - `client_id: optional string`

        Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    - `"external_key"`

  - `updated_at: string`

### External Key Update Response

- `ExternalKeyUpdateResponse object { id, created_at, display_name, 4 more }`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Tagged ID of the external key config.

  - `created_at: string`

  - `display_name: string`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: object { kms_arn, type, region, role_arn }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

    KMS provider identity and auth coordinates.

    - `Aws object { kms_arn, type, region, role_arn }`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

      - `type: "aws"`

        - `"aws"`

      - `region: optional string`

        AWS region. Derived from kms_arn if omitted.

      - `role_arn: optional string`

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `Gcp object { key_name, type }`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

      - `type: "gcp"`

        - `"gcp"`

    - `Azure object { key_name, tenant_id, type, 2 more }`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `type: "azure"`

        - `"azure"`

      - `vault_uri: string`

        Key Vault URI.

      - `client_id: optional string`

        Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    - `"external_key"`

  - `updated_at: string`

### External Key Delete Response

- `ExternalKeyDeleteResponse object { id, type }`

  - `id: string`

    ID of the deleted External Key.

  - `type: "external_key_deleted"`

    - `"external_key_deleted"`

### External Key Validate Response

- `ExternalKeyValidateResponse object { error, status, type }`

  Result of a validation roundtrip against the customer's KMS.

  HTTP 200 for both outcomes — the operation completed; `status` says
  whether the key works.

  - `error: string`

    Error message when status is `failure`. Null otherwise.

  - `status: "failure" or "success"`

    `success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

    - `"failure"`

    - `"success"`

  - `type: "external_key_validation"`

    - `"external_key_validation"`

# Usage Report

## Get Messages Usage Report

**get** `/v1/organizations/usage_report/messages`

Get Messages Usage Report

### Query Parameters

- `starting_at: string`

  Time buckets that start on or after this RFC 3339 timestamp will be returned.
  Each time bucket will be snapped to the start of the minute/hour/day in UTC.

- `account_ids: optional array of string`

  Restrict usage returned to the specified user account ID(s).

- `api_key_ids: optional array of string`

  Restrict usage returned to the specified API key ID(s).

- `bucket_width: optional "1d" or "1h" or "1m"`

  Time granularity of the response data.

  - `"1d"`

  - `"1h"`

  - `"1m"`

- `context_window: optional array of "0-200k" or "200k-1M"`

  Restrict usage returned to the specified context window(s).

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  Time buckets that end before this RFC 3339 timestamp will be returned.

- `group_by: optional array of "account_id" or "api_key_id" or "context_window" or 6 more`

  Group by any subset of the available options. Grouping by `speed` requires the `fast-mode-2026-02-01` beta header.

  - `"account_id"`

  - `"api_key_id"`

  - `"context_window"`

  - `"inference_geo"`

  - `"model"`

  - `"service_account_id"`

  - `"service_tier"`

  - `"speed"`

  - `"workspace_id"`

- `inference_geos: optional array of "global" or "not_available" or "us"`

  Restrict usage returned to the specified inference geo(s). Use `not_available` for models that do not support specifying `inference_geo`.

  - `"global"`

  - `"not_available"`

  - `"us"`

- `limit: optional number`

  Maximum number of time buckets to return in the response.

  The default and max limits depend on `bucket_width`:
  • `"1d"`: Default of 7 days, maximum of 31 days
  • `"1h"`: Default of 24 hours, maximum of 168 hours
  • `"1m"`: Default of 60 minutes, maximum of 1440 minutes

- `models: optional array of string`

  Restrict usage returned to the specified model(s).

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

- `service_account_ids: optional array of string`

  Restrict usage returned to the specified service account ID(s).

- `service_tiers: optional array of "batch" or "flex" or "flex_discount" or 3 more`

  Restrict usage returned to the specified service tier(s).

  - `"batch"`

  - `"flex"`

  - `"flex_discount"`

  - `"priority"`

  - `"priority_on_demand"`

  - `"standard"`

- `speeds: optional array of "fast" or "standard"`

  Restrict usage returned to the specified speed(s) (Claude Code research preview).
  Requires the `fast-mode-2026-02-01` beta header.

  - `"fast"`

  - `"standard"`

- `workspace_ids: optional array of string`

  Restrict usage returned to the specified workspace ID(s).

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `MessagesUsageReport object { data, has_more, next_page }`

  - `data: array of object { ending_at, results, starting_at }`

    - `ending_at: string`

      End of the time bucket (exclusive) in RFC 3339 format.

    - `results: array of object { account_id, api_key_id, cache_creation, 10 more }`

      List of usage items for this time bucket.  There may be multiple items if one or more `group_by[]` parameters are specified.

      - `account_id: string`

        ID of the user account that made the request. `null` if not grouping by account or for non-OAuth requests.

      - `api_key_id: string`

        ID of the API key used. `null` if not grouping by API key or for usage in the Anthropic Console.

      - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

        The number of input tokens for cache creation.

        - `ephemeral_1h_input_tokens: number`

          The number of input tokens used to create the 1 hour cache entry.

        - `ephemeral_5m_input_tokens: number`

          The number of input tokens used to create the 5 minute cache entry.

      - `cache_read_input_tokens: number`

        The number of input tokens read from the cache.

      - `context_window: "0-200k" or "200k-1M"`

        Context window used. `null` if not grouping by context window.

        - `"0-200k"`

        - `"200k-1M"`

      - `inference_geo: string`

        Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`.
        For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

      - `model: string`

        Model used. `null` if not grouping by model.

      - `output_tokens: number`

        The number of output tokens generated.

      - `server_tool_use: object { web_search_requests }`

        Server-side tool usage metrics.

        - `web_search_requests: number`

          The number of web search requests made.

      - `service_account_id: string`

        ID of the service account that made the request. `null` if not grouping by service account or for non-OIDC-federation requests.

      - `service_tier: "batch" or "flex" or "flex_discount" or 3 more`

        Service tier used. `null` if not grouping by service tier.

        - `"batch"`

        - `"flex"`

        - `"flex_discount"`

        - `"priority"`

        - `"priority_on_demand"`

        - `"standard"`

      - `uncached_input_tokens: number`

        The number of uncached input tokens processed.

      - `workspace_id: string`

        ID of the Workspace used. `null` if not grouping by workspace or for the default workspace.

    - `starting_at: string`

      Start of the time bucket (inclusive) in RFC 3339 format.

  - `has_more: boolean`

    Indicates if there are more results.

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```http
curl https://api.anthropic.com/v1/organizations/usage_report/messages \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
        {
          "account_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 200,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "output_tokens": 500,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "service_account_id": "svac_01Hk3R9TWxq7CfQak00OiVw4",
          "service_tier": "standard",
          "uncached_input_tokens": 1500,
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
        }
      ],
      "starting_at": "2025-08-01T00:00:00Z"
    }
  ],
  "has_more": true,
  "next_page": "2019-12-27T18:11:19.117Z"
}
```

## Get Claude Code Usage Report

**get** `/v1/organizations/usage_report/claude_code`

Retrieve daily aggregated usage metrics for Claude Code users.
Enables organizations to analyze developer productivity and build custom dashboards.

### Query Parameters

- `starting_at: string`

  UTC date in YYYY-MM-DD format. Returns metrics for this single day only.

- `limit: optional number`

  Number of records per page (default: 20, max: 1000).

- `page: optional string`

  Opaque cursor token from previous response's `next_page` field.

### Returns

- `ClaudeCodeUsageReport object { data, has_more, next_page }`

  - `data: array of object { actor, core_metrics, customer_type, 6 more }`

    List of Claude Code usage records for the requested date.

    - `actor: object { email_address, type }  or object { api_key_name, type }`

      The user or API key that performed the Claude Code actions.

      - `UserActor object { email_address, type }`

        - `email_address: string`

          Email address of the user who performed Claude Code actions.

        - `type: "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_name, type }`

        - `api_key_name: string`

          Name of the API key used to perform Claude Code actions.

        - `type: "api_actor"`

          - `"api_actor"`

    - `core_metrics: object { commits_by_claude_code, lines_of_code, num_sessions, pull_requests_by_claude_code }`

      Core productivity metrics measuring Claude Code usage and impact.

      - `commits_by_claude_code: number`

        Number of git commits created through Claude Code's commit functionality.

      - `lines_of_code: object { added, removed }`

        Statistics on code changes made through Claude Code.

        - `added: number`

          Total number of lines of code added across all files by Claude Code.

        - `removed: number`

          Total number of lines of code removed across all files by Claude Code.

      - `num_sessions: number`

        Number of distinct Claude Code sessions initiated by this actor.

      - `pull_requests_by_claude_code: number`

        Number of pull requests created through Claude Code's PR functionality.

    - `customer_type: "api" or "subscription"`

      Type of customer account (api for API customers, subscription for Pro/Team customers).

      - `"api"`

      - `"subscription"`

    - `date: string`

      UTC date for the usage metrics in YYYY-MM-DD format.

    - `model_breakdown: array of object { estimated_cost, model, tokens }`

      Token usage and cost breakdown by AI model used.

      - `estimated_cost: object { amount, currency }`

        Estimated cost for using this model

        - `amount: number`

          Estimated cost amount in minor currency units (e.g., cents for USD).

        - `currency: string`

          Currency code for the estimated cost (e.g., 'USD').

      - `model: string`

        Name of the AI model used for Claude Code interactions.

      - `tokens: object { cache_creation, cache_read, input, output }`

        Token usage breakdown for this model

        - `cache_creation: number`

          Number of cache creation tokens consumed by this model.

        - `cache_read: number`

          Number of cache read tokens consumed by this model.

        - `input: number`

          Number of input tokens consumed by this model.

        - `output: number`

          Number of output tokens generated by this model.

    - `organization_id: string`

      ID of the organization that owns the Claude Code usage.

    - `terminal_type: string`

      Type of terminal or environment where Claude Code was used.

    - `tool_actions: map[object { accepted, rejected } ]`

      Breakdown of tool action acceptance and rejection rates by tool type.

      - `accepted: number`

        Number of tool action proposals that the user accepted.

      - `rejected: number`

        Number of tool action proposals that the user rejected.

    - `subscription_type: optional "enterprise" or "team"`

      Subscription tier for subscription customers. `null` for API customers.

      - `"enterprise"`

      - `"team"`

  - `has_more: boolean`

    True if there are more records available beyond the current page.

  - `next_page: string`

    Opaque cursor token for fetching the next page of results, or null if no more pages are available.

### Example

```http
curl https://api.anthropic.com/v1/organizations/usage_report/claude_code \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "actor": {
        "email_address": "user@emaildomain.com",
        "type": "user_actor"
      },
      "core_metrics": {
        "commits_by_claude_code": 8,
        "lines_of_code": {
          "added": 342,
          "removed": 128
        },
        "num_sessions": 15,
        "pull_requests_by_claude_code": 2
      },
      "customer_type": "api",
      "date": "2025-08-08T00:00:00Z",
      "model_breakdown": [
        {
          "estimated_cost": {
            "amount": 186,
            "currency": "USD"
          },
          "model": "claude-sonnet-4-20250514",
          "tokens": {
            "cache_creation": 2340,
            "cache_read": 8790,
            "input": 45230,
            "output": 12450
          }
        },
        {
          "estimated_cost": {
            "amount": 42,
            "currency": "USD"
          },
          "model": "claude-3-5-haiku-20241022",
          "tokens": {
            "cache_creation": 890,
            "cache_read": 3420,
            "input": 23100,
            "output": 5680
          }
        }
      ],
      "organization_id": "12345678-1234-5678-1234-567812345678",
      "terminal_type": "iTerm.app",
      "tool_actions": {
        "edit_tool": {
          "accepted": 25,
          "rejected": 3
        },
        "multi_edit_tool": {
          "accepted": 12,
          "rejected": 1
        },
        "notebook_edit_tool": {
          "accepted": 5,
          "rejected": 2
        },
        "write_tool": {
          "accepted": 8,
          "rejected": 0
        }
      },
      "subscription_type": "enterprise"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Domain Types

### Claude Code Usage Report

- `ClaudeCodeUsageReport object { data, has_more, next_page }`

  - `data: array of object { actor, core_metrics, customer_type, 6 more }`

    List of Claude Code usage records for the requested date.

    - `actor: object { email_address, type }  or object { api_key_name, type }`

      The user or API key that performed the Claude Code actions.

      - `UserActor object { email_address, type }`

        - `email_address: string`

          Email address of the user who performed Claude Code actions.

        - `type: "user_actor"`

          - `"user_actor"`

      - `APIActor object { api_key_name, type }`

        - `api_key_name: string`

          Name of the API key used to perform Claude Code actions.

        - `type: "api_actor"`

          - `"api_actor"`

    - `core_metrics: object { commits_by_claude_code, lines_of_code, num_sessions, pull_requests_by_claude_code }`

      Core productivity metrics measuring Claude Code usage and impact.

      - `commits_by_claude_code: number`

        Number of git commits created through Claude Code's commit functionality.

      - `lines_of_code: object { added, removed }`

        Statistics on code changes made through Claude Code.

        - `added: number`

          Total number of lines of code added across all files by Claude Code.

        - `removed: number`

          Total number of lines of code removed across all files by Claude Code.

      - `num_sessions: number`

        Number of distinct Claude Code sessions initiated by this actor.

      - `pull_requests_by_claude_code: number`

        Number of pull requests created through Claude Code's PR functionality.

    - `customer_type: "api" or "subscription"`

      Type of customer account (api for API customers, subscription for Pro/Team customers).

      - `"api"`

      - `"subscription"`

    - `date: string`

      UTC date for the usage metrics in YYYY-MM-DD format.

    - `model_breakdown: array of object { estimated_cost, model, tokens }`

      Token usage and cost breakdown by AI model used.

      - `estimated_cost: object { amount, currency }`

        Estimated cost for using this model

        - `amount: number`

          Estimated cost amount in minor currency units (e.g., cents for USD).

        - `currency: string`

          Currency code for the estimated cost (e.g., 'USD').

      - `model: string`

        Name of the AI model used for Claude Code interactions.

      - `tokens: object { cache_creation, cache_read, input, output }`

        Token usage breakdown for this model

        - `cache_creation: number`

          Number of cache creation tokens consumed by this model.

        - `cache_read: number`

          Number of cache read tokens consumed by this model.

        - `input: number`

          Number of input tokens consumed by this model.

        - `output: number`

          Number of output tokens generated by this model.

    - `organization_id: string`

      ID of the organization that owns the Claude Code usage.

    - `terminal_type: string`

      Type of terminal or environment where Claude Code was used.

    - `tool_actions: map[object { accepted, rejected } ]`

      Breakdown of tool action acceptance and rejection rates by tool type.

      - `accepted: number`

        Number of tool action proposals that the user accepted.

      - `rejected: number`

        Number of tool action proposals that the user rejected.

    - `subscription_type: optional "enterprise" or "team"`

      Subscription tier for subscription customers. `null` for API customers.

      - `"enterprise"`

      - `"team"`

  - `has_more: boolean`

    True if there are more records available beyond the current page.

  - `next_page: string`

    Opaque cursor token for fetching the next page of results, or null if no more pages are available.

### Messages Usage Report

- `MessagesUsageReport object { data, has_more, next_page }`

  - `data: array of object { ending_at, results, starting_at }`

    - `ending_at: string`

      End of the time bucket (exclusive) in RFC 3339 format.

    - `results: array of object { account_id, api_key_id, cache_creation, 10 more }`

      List of usage items for this time bucket.  There may be multiple items if one or more `group_by[]` parameters are specified.

      - `account_id: string`

        ID of the user account that made the request. `null` if not grouping by account or for non-OAuth requests.

      - `api_key_id: string`

        ID of the API key used. `null` if not grouping by API key or for usage in the Anthropic Console.

      - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

        The number of input tokens for cache creation.

        - `ephemeral_1h_input_tokens: number`

          The number of input tokens used to create the 1 hour cache entry.

        - `ephemeral_5m_input_tokens: number`

          The number of input tokens used to create the 5 minute cache entry.

      - `cache_read_input_tokens: number`

        The number of input tokens read from the cache.

      - `context_window: "0-200k" or "200k-1M"`

        Context window used. `null` if not grouping by context window.

        - `"0-200k"`

        - `"200k-1M"`

      - `inference_geo: string`

        Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`.
        For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

      - `model: string`

        Model used. `null` if not grouping by model.

      - `output_tokens: number`

        The number of output tokens generated.

      - `server_tool_use: object { web_search_requests }`

        Server-side tool usage metrics.

        - `web_search_requests: number`

          The number of web search requests made.

      - `service_account_id: string`

        ID of the service account that made the request. `null` if not grouping by service account or for non-OIDC-federation requests.

      - `service_tier: "batch" or "flex" or "flex_discount" or 3 more`

        Service tier used. `null` if not grouping by service tier.

        - `"batch"`

        - `"flex"`

        - `"flex_discount"`

        - `"priority"`

        - `"priority_on_demand"`

        - `"standard"`

      - `uncached_input_tokens: number`

        The number of uncached input tokens processed.

      - `workspace_id: string`

        ID of the Workspace used. `null` if not grouping by workspace or for the default workspace.

    - `starting_at: string`

      Start of the time bucket (inclusive) in RFC 3339 format.

  - `has_more: boolean`

    Indicates if there are more results.

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

# Cost Report

## Get Cost Report

**get** `/v1/organizations/cost_report`

Get Cost Report

### Query Parameters

- `starting_at: string`

  Time buckets that start on or after this RFC 3339 timestamp will be returned.
  Each time bucket will be snapped to the start of the minute/hour/day in UTC.

- `bucket_width: optional "1d"`

  Time granularity of the response data.

  - `"1d"`

- `ending_at: optional string`

  Time buckets that end before this RFC 3339 timestamp will be returned.

- `group_by: optional array of "description" or "workspace_id"`

  Group by any subset of the available options.

  - `"description"`

  - `"workspace_id"`

- `limit: optional number`

  Maximum number of time buckets to return in the response.

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `CostReport object { data, has_more, next_page }`

  - `data: array of object { ending_at, results, starting_at }`

    - `ending_at: string`

      End of the time bucket (exclusive) in RFC 3339 format.

    - `results: array of object { amount, context_window, cost_type, 7 more }`

      List of cost items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.

      - `amount: string`

        Cost amount in lowest currency units (e.g. cents) as a decimal string. For example, `"123.45"` in `"USD"` represents `$1.23`.

      - `context_window: "0-200k" or "200k-1M"`

        Input context window used. `null` if not grouping by description or for non-token costs.

        - `"0-200k"`

        - `"200k-1M"`

      - `cost_type: "code_execution" or "session_usage" or "tokens" or "web_search"`

        Type of cost. `null` if not grouping by description.

        - `"code_execution"`

        - `"session_usage"`

        - `"tokens"`

        - `"web_search"`

      - `currency: string`

        Currency code for the cost amount. Currently always `"USD"`.

      - `description: string`

        Description of the cost item. `null` if not grouping by description.

      - `inference_geo: string`

        Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`.
        For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

      - `model: string`

        Model name used. `null` if not grouping by description or for non-token costs.

      - `service_tier: "batch" or "standard"`

        Service tier used. `null` if not grouping by description or for non-token costs.

        - `"batch"`

        - `"standard"`

      - `token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more`

        Type of token. `null` if not grouping by description or for non-token costs.

        - `"cache_creation.ephemeral_1h_input_tokens"`

        - `"cache_creation.ephemeral_5m_input_tokens"`

        - `"cache_read_input_tokens"`

        - `"output_tokens"`

        - `"uncached_input_tokens"`

      - `workspace_id: string`

        ID of the Workspace this cost is associated with. `null` if not grouping by workspace or for the default workspace.

    - `starting_at: string`

      Start of the time bucket (inclusive) in RFC 3339 format.

  - `has_more: boolean`

    Indicates if there are more results.

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```http
curl https://api.anthropic.com/v1/organizations/cost_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
        {
          "amount": "123.78912",
          "context_window": "0-200k",
          "cost_type": "tokens",
          "currency": "USD",
          "description": "Claude Sonnet 4 Usage - Input Tokens",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "service_tier": "standard",
          "token_type": "uncached_input_tokens",
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
        }
      ],
      "starting_at": "2025-08-01T00:00:00Z"
    }
  ],
  "has_more": true,
  "next_page": "2019-12-27T18:11:19.117Z"
}
```

## Domain Types

### Cost Report

- `CostReport object { data, has_more, next_page }`

  - `data: array of object { ending_at, results, starting_at }`

    - `ending_at: string`

      End of the time bucket (exclusive) in RFC 3339 format.

    - `results: array of object { amount, context_window, cost_type, 7 more }`

      List of cost items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.

      - `amount: string`

        Cost amount in lowest currency units (e.g. cents) as a decimal string. For example, `"123.45"` in `"USD"` represents `$1.23`.

      - `context_window: "0-200k" or "200k-1M"`

        Input context window used. `null` if not grouping by description or for non-token costs.

        - `"0-200k"`

        - `"200k-1M"`

      - `cost_type: "code_execution" or "session_usage" or "tokens" or "web_search"`

        Type of cost. `null` if not grouping by description.

        - `"code_execution"`

        - `"session_usage"`

        - `"tokens"`

        - `"web_search"`

      - `currency: string`

        Currency code for the cost amount. Currently always `"USD"`.

      - `description: string`

        Description of the cost item. `null` if not grouping by description.

      - `inference_geo: string`

        Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`.
        For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

      - `model: string`

        Model name used. `null` if not grouping by description or for non-token costs.

      - `service_tier: "batch" or "standard"`

        Service tier used. `null` if not grouping by description or for non-token costs.

        - `"batch"`

        - `"standard"`

      - `token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more`

        Type of token. `null` if not grouping by description or for non-token costs.

        - `"cache_creation.ephemeral_1h_input_tokens"`

        - `"cache_creation.ephemeral_5m_input_tokens"`

        - `"cache_read_input_tokens"`

        - `"output_tokens"`

        - `"uncached_input_tokens"`

      - `workspace_id: string`

        ID of the Workspace this cost is associated with. `null` if not grouping by workspace or for the default workspace.

    - `starting_at: string`

      Start of the time bucket (inclusive) in RFC 3339 format.

  - `has_more: boolean`

    Indicates if there are more results.

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

# Analytics

## Get Activity Summaries

**get** `/v1/organizations/analytics/summaries`

Get organization-wide activity summaries for a date range.

Returns one entry per day in [starting_date, ending_date). Data is
typically available with a 1-day lag and may be revised by a few percent
over the following days: when ending_date is omitted it defaults to the
most recent available day + 1, so the last entry covers the most recent
available day. Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

### Query Parameters

- `starting_date: string`

  UTC date in YYYY-MM-DD format. Start of the date range (inclusive). Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive). Data is typically available with a 1-day lag, so this can be at most today — which is also the default when omitted, making the last entry cover the most recent available day. Data may be revised by a few percent over the following days. The range may span at most 366 days.

- `filter: optional array of string`

  Filters as 'dimension:value'. Only rbac_group_id is supported (e.g. filter[]=rbac_group_id:<id>); repeat the param to OR across groups. Scopes the whole day series to members of the matching group(s), re-aggregated from member-level activity — org-wide seat/invite fields and the adoption rates derived from them are null on scoped rows. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each UTC day (time-of-usage attribution). At most 100 entries.

### Returns

- `ActivitySummary object { summaries }`

  Response for GET /v1/organizations/analytics/summaries.

  - `summaries: array of object { assigned_seat_count, cowork_daily_active_user_count, cowork_monthly_active_user_count, 26 more }`

    - `assigned_seat_count: number`

      Number of seats currently assigned to members. Null when the response is scoped to an RBAC group — seat assignment is org-wide and has no per-group analogue.

    - `cowork_daily_active_user_count: number`

      Number of users with Cowork activity on the requested day

    - `cowork_monthly_active_user_count: number`

      Number of users with Cowork activity in the 30-day rolling window

    - `cowork_weekly_active_user_count: number`

      Number of users with Cowork activity in the 7-day rolling window

    - `daily_active_user_count: number`

      Number of users with token consumption on the requested day

    - `daily_adoption_rate: number`

      Percentage of assigned seats with activity on the requested day (DAU / assigned_seat_count * 100). Null when the response is scoped to an RBAC group.

    - `ending_at: string`

      End time in UTC of aggregation period (e.g. 2026-01-16T00:00:00Z)

    - `monthly_active_user_count: number`

      Number of users with token consumption in the 30-day rolling window

    - `monthly_adoption_rate: number`

      Percentage of assigned seats with activity in the 30-day rolling window (MAU / assigned_seat_count * 100). Null when the response is scoped to an RBAC group.

    - `pending_invite_count: number`

      Number of pending invitations to join the organization. Null when the response is scoped to an RBAC group.

    - `starting_at: string`

      Start time in UTC of aggregation period (e.g. 2026-01-15T00:00:00Z)

    - `weekly_active_user_count: number`

      Number of users with token consumption in the 7-day rolling window

    - `weekly_adoption_rate: number`

      Percentage of assigned seats with activity in the 7-day rolling window (WAU / assigned_seat_count * 100). Null when the response is scoped to an RBAC group.

    - `chat_daily_active_user_count: optional number`

      Number of users with claude.ai (chat) activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `chat_monthly_active_user_count: optional number`

      Number of users with claude.ai (chat) activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `chat_weekly_active_user_count: optional number`

      Number of users with claude.ai (chat) activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_code_daily_active_user_count: optional number`

      Number of users with Claude Code activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_code_monthly_active_user_count: optional number`

      Number of users with Claude Code activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_code_weekly_active_user_count: optional number`

      Number of users with Claude Code activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_design_daily_active_user_count: optional number`

      Number of users with Claude Design activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_design_monthly_active_user_count: optional number`

      Number of users with Claude Design activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_design_weekly_active_user_count: optional number`

      Number of users with Claude Design activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `office_agent_daily_active_user_count: optional number`

      Number of users with Claude in Office activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `office_agent_monthly_active_user_count: optional number`

      Number of users with Claude in Office activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `office_agent_weekly_active_user_count: optional number`

      Number of users with Claude in Office activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_daily_active_user_count: optional number`

      Number of users with Claude Science activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_entitled_user_count: optional number`

      Number of users with a Claude Science seat entitlement (per-seat RBAC) at the time of the daily snapshot. The funnel top; independent of the org-level Claude Science toggle. Null when the response is scoped to an RBAC group — entitlement is org-wide and has no per-group analogue. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_monthly_active_user_count: optional number`

      Number of users with Claude Science activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_weekly_active_user_count: optional number`

      Number of users with Claude Science activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/summaries \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "summaries": [
    {
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "ending_at",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "starting_at",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0,
      "chat_daily_active_user_count": 0,
      "chat_monthly_active_user_count": 0,
      "chat_weekly_active_user_count": 0,
      "claude_code_daily_active_user_count": 0,
      "claude_code_monthly_active_user_count": 0,
      "claude_code_weekly_active_user_count": 0,
      "claude_design_daily_active_user_count": 0,
      "claude_design_monthly_active_user_count": 0,
      "claude_design_weekly_active_user_count": 0,
      "office_agent_daily_active_user_count": 0,
      "office_agent_monthly_active_user_count": 0,
      "office_agent_weekly_active_user_count": 0,
      "science_daily_active_user_count": 0,
      "science_entitled_user_count": 0,
      "science_monthly_active_user_count": 0,
      "science_weekly_active_user_count": 0
    }
  ]
}
```

## Domain Types

### Activity Summary

- `ActivitySummary object { summaries }`

  Response for GET /v1/organizations/analytics/summaries.

  - `summaries: array of object { assigned_seat_count, cowork_daily_active_user_count, cowork_monthly_active_user_count, 26 more }`

    - `assigned_seat_count: number`

      Number of seats currently assigned to members. Null when the response is scoped to an RBAC group — seat assignment is org-wide and has no per-group analogue.

    - `cowork_daily_active_user_count: number`

      Number of users with Cowork activity on the requested day

    - `cowork_monthly_active_user_count: number`

      Number of users with Cowork activity in the 30-day rolling window

    - `cowork_weekly_active_user_count: number`

      Number of users with Cowork activity in the 7-day rolling window

    - `daily_active_user_count: number`

      Number of users with token consumption on the requested day

    - `daily_adoption_rate: number`

      Percentage of assigned seats with activity on the requested day (DAU / assigned_seat_count * 100). Null when the response is scoped to an RBAC group.

    - `ending_at: string`

      End time in UTC of aggregation period (e.g. 2026-01-16T00:00:00Z)

    - `monthly_active_user_count: number`

      Number of users with token consumption in the 30-day rolling window

    - `monthly_adoption_rate: number`

      Percentage of assigned seats with activity in the 30-day rolling window (MAU / assigned_seat_count * 100). Null when the response is scoped to an RBAC group.

    - `pending_invite_count: number`

      Number of pending invitations to join the organization. Null when the response is scoped to an RBAC group.

    - `starting_at: string`

      Start time in UTC of aggregation period (e.g. 2026-01-15T00:00:00Z)

    - `weekly_active_user_count: number`

      Number of users with token consumption in the 7-day rolling window

    - `weekly_adoption_rate: number`

      Percentage of assigned seats with activity in the 7-day rolling window (WAU / assigned_seat_count * 100). Null when the response is scoped to an RBAC group.

    - `chat_daily_active_user_count: optional number`

      Number of users with claude.ai (chat) activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `chat_monthly_active_user_count: optional number`

      Number of users with claude.ai (chat) activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `chat_weekly_active_user_count: optional number`

      Number of users with claude.ai (chat) activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_code_daily_active_user_count: optional number`

      Number of users with Claude Code activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_code_monthly_active_user_count: optional number`

      Number of users with Claude Code activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_code_weekly_active_user_count: optional number`

      Number of users with Claude Code activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_design_daily_active_user_count: optional number`

      Number of users with Claude Design activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_design_monthly_active_user_count: optional number`

      Number of users with Claude Design activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_design_weekly_active_user_count: optional number`

      Number of users with Claude Design activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `office_agent_daily_active_user_count: optional number`

      Number of users with Claude in Office activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `office_agent_monthly_active_user_count: optional number`

      Number of users with Claude in Office activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `office_agent_weekly_active_user_count: optional number`

      Number of users with Claude in Office activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_daily_active_user_count: optional number`

      Number of users with Claude Science activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_entitled_user_count: optional number`

      Number of users with a Claude Science seat entitlement (per-seat RBAC) at the time of the daily snapshot. The funnel top; independent of the org-level Claude Science toggle. Null when the response is scoped to an RBAC group — entitlement is org-wide and has no per-group analogue. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_monthly_active_user_count: optional number`

      Number of users with Claude Science activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_weekly_active_user_count: optional number`

      Number of users with Claude Science activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

### Analytics User

- `AnalyticsUser object { id, email_address }`

  User identifier.

  - `id: string`

    Tagged user identifier (e.g. user_...)

  - `email_address: string`

    Email address of the user

### Analytics User Actor

- `AnalyticsUserActor object { user_id, deleted, email, 2 more }`

  - `user_id: string`

    Tagged user ID.

  - `deleted: optional boolean`

    True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

  - `email: optional string`

    The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

  - `name: optional string`

    The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

  - `type: optional "user_actor"`

    - `"user_actor"`

### Connector Office Product Metrics

- `ConnectorOfficeProductMetrics object { distinct_session_connector_used_count }`

  Office Agent activity metrics for a single connector on a given day within one Office product.

  - `distinct_session_connector_used_count: number`

    Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Office Product Metrics

- `OfficeProductMetrics object { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more }`

  Office Agent activity metrics for a single user on a given day within one Office product.

  - `connectors_used_count: number`

    Number of MCP connector invocations

  - `distinct_connectors_used_count: number`

    Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_session_count: number`

    Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_skills_used_count: number`

    Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `message_count: number`

    Number of messages sent

  - `skills_used_count: number`

    Number of skill invocations

### Skill Office Product Metrics

- `SkillOfficeProductMetrics object { distinct_session_skill_used_count }`

  Office Agent activity metrics for a single skill on a given day within one Office product.

  - `distinct_session_skill_used_count: number`

    Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Tool Action Counts

- `ToolActionCounts object { accepted_count, rejected_count }`

  Accepted/rejected counts for a single Claude Code tool type.

  - `accepted_count: number`

    Number of tool proposals accepted

  - `rejected_count: number`

    Number of tool proposals rejected

# Usage

## Get Token Usage Over Time

**get** `/v1/organizations/analytics/usage_report`

Get token usage over time across a date range.

Returns token usage bucketed by minute, hour, or day, optionally broken
down by product, model, context window, inference region, or speed.
Available to organizations on a Claude Enterprise plan. Requires an API
key with the `read:analytics` scope.

### Query Parameters

- `starting_at: string`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

- `bucket_width: optional "1d" or "1h" or "1m"`

  Time bucket granularity.

  - `"1d"`

  - `"1h"`

  - `"1m"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `group_by: optional array of "context_window" or "inference_geo" or "model" or 3 more`

  Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket). Each bucket reports at most its top 100 groups; a group beyond that cap has no row in that bucket (there is no remainder row), so grouped buckets are not exhaustive when a dimension has more than 100 distinct values.

  - `"context_window"`

  - `"inference_geo"`

  - `"model"`

  - `"product"`

  - `"rbac_group_id"`

  - `"speed"`

- `inference_geos: optional array of "global" or "not_available" or "us"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"not_available"`

  - `"us"`

- `limit: optional number`

  Maximum number of time buckets per page. Defaults and caps vary by bucket_width (1d: default 7, max 31; 1h: default 24, max 168; 1m: default 60, max 256).

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design".

- `rbac_group_ids: optional array of string`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

- `speeds: optional array of "fast" or "standard"`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  - `"fast"`

  - `"standard"`

- `user_ids: optional array of string`

  Filter to specific users by tagged user ID.

### Returns

- `UsageBucket object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { ending_at, results, starting_at }`

    - `ending_at: string`

    - `results: array of object { cache_creation, cache_read_input_tokens, context_window, 9 more }`

      - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

        - `ephemeral_1h_input_tokens: number`

          The number of input tokens used to create the 1 hour cache entry.

        - `ephemeral_5m_input_tokens: number`

          The number of input tokens used to create the 5 minute cache entry.

      - `cache_read_input_tokens: number`

        The number of input tokens read from the cache.

      - `context_window: "0-200k" or "200k-1M"`

        - `"0-200k"`

        - `"200k-1M"`

      - `inference_geo: "global" or "us"`

        - `"global"`

        - `"us"`

      - `model: string`

      - `output_tokens: number`

        The number of output tokens generated.

      - `product: string`

        Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

      - `rbac_group_id: string`

        RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

      - `requests: number`

        Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

      - `server_tool_use: object { web_search_requests }`

        - `web_search_requests: number`

          The number of web search requests made.

      - `speed: "fast" or "standard"`

        - `"fast"`

        - `"standard"`

      - `uncached_input_tokens: number`

        The number of uncached input tokens processed.

    - `starting_at: string`

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/usage_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
        {
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 0,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "model",
          "output_tokens": 0,
          "product": "product",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "speed": "fast",
          "uncached_input_tokens": 0
        }
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Get Per-User Token Usage

**get** `/v1/organizations/analytics/user_usage_report`

Get per-user token usage across a date range.

Returns one row per user, ranked by the chosen token metric. Use this to
see which users consume the most tokens. Only usage attributable to a
seat user is included; for organization-wide totals including direct
API-key and automation traffic, use the bucketed
`/v1/organizations/analytics/usage_report` endpoint. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

### Query Parameters

- `starting_at: string`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

- `bucket_width: optional "1d" or "1h" or "1m"`

  Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

  - `"1d"`

  - `"1h"`

  - `"1m"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `exclude_deleted_users: optional boolean`

  If true, omit rows for deleted accounts. Pages may return fewer than `limit` rows when deleted users were filtered.

- `group_by: optional array of "context_window" or "inference_geo" or "model" or 3 more`

  Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/usage_report` endpoint. `limit` bounds (actor × time bucket × dimension) rows — with dimensions or `bucket_width` present, one actor may span several rows.

  - `"context_window"`

  - `"inference_geo"`

  - `"model"`

  - `"product"`

  - `"rbac_group_id"`

  - `"speed"`

- `inference_geos: optional array of "global" or "not_available" or "us"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"not_available"`

  - `"us"`

- `limit: optional number`

  Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `order: optional "asc" or "desc"`

  Sort direction. Defaults to `desc`.

  - `"asc"`

  - `"desc"`

- `order_by: optional "output_tokens" or "requests" or "total_tokens" or "uncached_input_tokens"`

  Metric to rank actors by. Defaults to `total_tokens`.

  - `"output_tokens"`

  - `"requests"`

  - `"total_tokens"`

  - `"uncached_input_tokens"`

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design".

- `rbac_group_ids: optional array of string`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

- `speeds: optional array of "fast" or "standard"`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  - `"fast"`

  - `"standard"`

- `user_ids: optional array of string`

  Filter to specific users by tagged user ID.

### Returns

- `UserUsage object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { actor, cache_creation, cache_read_input_tokens, 13 more }`

    - `actor: AnalyticsUserActor`

      - `user_id: string`

        Tagged user ID.

      - `deleted: optional boolean`

        True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

      - `email: optional string`

        The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

      - `name: optional string`

        The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

      - `ephemeral_1h_input_tokens: number`

        The number of input tokens used to create the 1 hour cache entry.

      - `ephemeral_5m_input_tokens: number`

        The number of input tokens used to create the 5 minute cache entry.

    - `cache_read_input_tokens: number`

      The number of input tokens read from the cache.

    - `context_window: "0-200k" or "200k-1M"`

      - `"0-200k"`

      - `"200k-1M"`

    - `ending_at: string`

    - `inference_geo: "global" or "us"`

      - `"global"`

      - `"us"`

    - `model: string`

    - `output_tokens: number`

      The number of output tokens generated.

    - `product: string`

      Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

    - `rbac_group_id: string`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

    - `requests: number`

      Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `server_tool_use: object { web_search_requests }`

      - `web_search_requests: number`

        The number of web search requests made.

    - `speed: "fast" or "standard"`

      - `"fast"`

      - `"standard"`

    - `starting_at: string`

    - `total_tokens: number`

      Total token count across all token types. This is the value the default order_by='total_tokens' sorts on.

    - `uncached_input_tokens: number`

      The number of uncached input tokens processed.

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/user_usage_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "actor": {
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt",
        "deleted": true,
        "email": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor"
      },
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1000,
        "ephemeral_5m_input_tokens": 500
      },
      "cache_read_input_tokens": 3200000,
      "context_window": "0-200k",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "model": "model",
      "output_tokens": 891000,
      "product": "product",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "server_tool_use": {
        "web_search_requests": 10
      },
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "total_tokens": 5377000,
      "uncached_input_tokens": 1284500
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Domain Types

### Usage Bucket

- `UsageBucket object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { ending_at, results, starting_at }`

    - `ending_at: string`

    - `results: array of object { cache_creation, cache_read_input_tokens, context_window, 9 more }`

      - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

        - `ephemeral_1h_input_tokens: number`

          The number of input tokens used to create the 1 hour cache entry.

        - `ephemeral_5m_input_tokens: number`

          The number of input tokens used to create the 5 minute cache entry.

      - `cache_read_input_tokens: number`

        The number of input tokens read from the cache.

      - `context_window: "0-200k" or "200k-1M"`

        - `"0-200k"`

        - `"200k-1M"`

      - `inference_geo: "global" or "us"`

        - `"global"`

        - `"us"`

      - `model: string`

      - `output_tokens: number`

        The number of output tokens generated.

      - `product: string`

        Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

      - `rbac_group_id: string`

        RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

      - `requests: number`

        Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

      - `server_tool_use: object { web_search_requests }`

        - `web_search_requests: number`

          The number of web search requests made.

      - `speed: "fast" or "standard"`

        - `"fast"`

        - `"standard"`

      - `uncached_input_tokens: number`

        The number of uncached input tokens processed.

    - `starting_at: string`

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

### User Usage

- `UserUsage object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { actor, cache_creation, cache_read_input_tokens, 13 more }`

    - `actor: AnalyticsUserActor`

      - `user_id: string`

        Tagged user ID.

      - `deleted: optional boolean`

        True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

      - `email: optional string`

        The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

      - `name: optional string`

        The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

      - `ephemeral_1h_input_tokens: number`

        The number of input tokens used to create the 1 hour cache entry.

      - `ephemeral_5m_input_tokens: number`

        The number of input tokens used to create the 5 minute cache entry.

    - `cache_read_input_tokens: number`

      The number of input tokens read from the cache.

    - `context_window: "0-200k" or "200k-1M"`

      - `"0-200k"`

      - `"200k-1M"`

    - `ending_at: string`

    - `inference_geo: "global" or "us"`

      - `"global"`

      - `"us"`

    - `model: string`

    - `output_tokens: number`

      The number of output tokens generated.

    - `product: string`

      Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

    - `rbac_group_id: string`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

    - `requests: number`

      Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `server_tool_use: object { web_search_requests }`

      - `web_search_requests: number`

        The number of web search requests made.

    - `speed: "fast" or "standard"`

      - `"fast"`

      - `"standard"`

    - `starting_at: string`

    - `total_tokens: number`

      Total token count across all token types. This is the value the default order_by='total_tokens' sorts on.

    - `uncached_input_tokens: number`

      The number of uncached input tokens processed.

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

# Cost

## Get Cost Over Time

**get** `/v1/organizations/analytics/cost_report`

Get cost in USD over time across a date range.

Returns cost bucketed by minute, hour, or day, optionally broken down by
product, model, context window, inference region, speed, cost type, or
token type. Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

### Query Parameters

- `starting_at: string`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

- `bucket_width: optional "1d" or "1h" or "1m"`

  Time bucket granularity.

  - `"1d"`

  - `"1h"`

  - `"1m"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `group_by: optional array of "context_window" or "cost_type" or "inference_geo" or 5 more`

  Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket). Each bucket reports at most its top 100 groups; a group beyond that cap has no row in that bucket (there is no remainder row), so grouped buckets are not exhaustive when a dimension has more than 100 distinct values.

  - `"context_window"`

  - `"cost_type"`

  - `"inference_geo"`

  - `"model"`

  - `"product"`

  - `"rbac_group_id"`

  - `"speed"`

  - `"token_type"`

- `inference_geos: optional array of "global" or "not_available" or "us"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"not_available"`

  - `"us"`

- `limit: optional number`

  Maximum number of time buckets per page. Defaults and caps vary by bucket_width (1d: default 7, max 31; 1h: default 24, max 168; 1m: default 60, max 256).

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design".

- `rbac_group_ids: optional array of string`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

- `speeds: optional array of "fast" or "standard"`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  - `"fast"`

  - `"standard"`

- `user_ids: optional array of string`

  Filter to specific users by tagged user ID.

### Returns

- `CostBucket object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { ending_at, results, starting_at }`

    - `ending_at: string`

    - `results: array of object { amount, context_window, cost_type, 9 more }`

      - `amount: string`

        Amount (post-discount, pre-credit) in fractional cents.

      - `context_window: "0-200k" or "200k-1M"`

        - `"0-200k"`

        - `"200k-1M"`

      - `cost_type: "code_execution" or "tokens" or "web_search"`

        Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).

        - `"code_execution"`

        - `"tokens"`

        - `"web_search"`

      - `currency: "USD"`

        - `"USD"`

      - `inference_geo: "global" or "us"`

        - `"global"`

        - `"us"`

      - `list_amount: string`

        List-price amount (pre-discount) in fractional cents.

      - `model: string`

      - `product: string`

        Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

      - `rbac_group_id: string`

        RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

      - `requests: number`

        Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

      - `speed: "fast" or "standard"`

        - `"fast"`

        - `"standard"`

      - `token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more`

        Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.

        - `"cache_creation.ephemeral_1h_input_tokens"`

        - `"cache_creation.ephemeral_5m_input_tokens"`

        - `"cache_read_input_tokens"`

        - `"output_tokens"`

        - `"uncached_input_tokens"`

    - `starting_at: string`

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/cost_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
        {
          "amount": "amount",
          "context_window": "0-200k",
          "cost_type": "code_execution",
          "currency": "USD",
          "inference_geo": "global",
          "list_amount": "list_amount",
          "model": "model",
          "product": "product",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "speed": "fast",
          "token_type": "cache_creation.ephemeral_1h_input_tokens"
        }
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Get Per-User Cost

**get** `/v1/organizations/analytics/user_cost_report`

Get per-user cost in USD across a date range.

Returns one row per user, ranked by spend. Use this to see which users
account for the most cost. Only cost attributable to a seat user is
included; for organization-wide totals including direct API-key and
automation traffic, use the bucketed
`/v1/organizations/analytics/cost_report` endpoint. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

### Query Parameters

- `starting_at: string`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

- `bucket_width: optional "1d" or "1h" or "1m"`

  Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

  - `"1d"`

  - `"1h"`

  - `"1m"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `exclude_deleted_users: optional boolean`

  If true, omit rows for deleted accounts. Pages may return fewer than `limit` rows when deleted users were filtered.

- `group_by: optional array of "context_window" or "cost_type" or "inference_geo" or 5 more`

  Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/cost_report` endpoint. The `product`, `model`, `context_window`, `inference_geo`, and `speed` dimensions — and the time bucket, when `bucket_width` is set — count toward `limit`. `cost_type` and `token_type` do not: `cost_type` returns one row per cost component (tokens, web search, code execution); `token_type` returns one row per token type, each with `cost_type: "tokens"`; combining both returns the per-token-type rows plus the web-search and code-execution rows. A page can therefore contain more rows than `limit` when `cost_type` or `token_type` is requested.

  - `"context_window"`

  - `"cost_type"`

  - `"inference_geo"`

  - `"model"`

  - `"product"`

  - `"rbac_group_id"`

  - `"speed"`

  - `"token_type"`

- `inference_geos: optional array of "global" or "not_available" or "us"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"not_available"`

  - `"us"`

- `limit: optional number`

  Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `order: optional "asc" or "desc"`

  Sort direction. Defaults to `desc`.

  - `"asc"`

  - `"desc"`

- `order_by: optional "amount" or "list_amount"`

  Metric to rank actors by. Defaults to `amount`.

  - `"amount"`

  - `"list_amount"`

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design".

- `rbac_group_ids: optional array of string`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

- `speeds: optional array of "fast" or "standard"`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  - `"fast"`

  - `"standard"`

- `user_ids: optional array of string`

  Filter to specific users by tagged user ID.

### Returns

- `UserCost object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { actor, amount, context_window, 12 more }`

    - `actor: AnalyticsUserActor`

      - `user_id: string`

        Tagged user ID.

      - `deleted: optional boolean`

        True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

      - `email: optional string`

        The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

      - `name: optional string`

        The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `amount: string`

      Amount (post-discount, pre-credit) in fractional cents (minor units).

    - `context_window: "0-200k" or "200k-1M"`

      - `"0-200k"`

      - `"200k-1M"`

    - `cost_type: "code_execution" or "tokens" or "web_search"`

      Cost component breakdown; null when returning the combined total.

      - `"code_execution"`

      - `"tokens"`

      - `"web_search"`

    - `currency: "USD"`

      - `"USD"`

    - `ending_at: string`

    - `inference_geo: "global" or "us"`

      - `"global"`

      - `"us"`

    - `list_amount: string`

      List-price amount (pre-discount) in fractional cents.

    - `model: string`

    - `product: string`

      Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

    - `rbac_group_id: string`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

    - `requests: number`

      Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `speed: "fast" or "standard"`

      - `"fast"`

      - `"standard"`

    - `starting_at: string`

    - `token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more`

      Token type when cost_type=tokens; null otherwise.

      - `"cache_creation.ephemeral_1h_input_tokens"`

      - `"cache_creation.ephemeral_5m_input_tokens"`

      - `"cache_read_input_tokens"`

      - `"output_tokens"`

      - `"uncached_input_tokens"`

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/user_cost_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "actor": {
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt",
        "deleted": true,
        "email": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor"
      },
      "amount": "41280.000000",
      "context_window": "0-200k",
      "cost_type": "code_execution",
      "currency": "USD",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "list_amount": "51600.000000",
      "model": "model",
      "product": "product",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "token_type": "cache_creation.ephemeral_1h_input_tokens"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Domain Types

### Cost Bucket

- `CostBucket object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { ending_at, results, starting_at }`

    - `ending_at: string`

    - `results: array of object { amount, context_window, cost_type, 9 more }`

      - `amount: string`

        Amount (post-discount, pre-credit) in fractional cents.

      - `context_window: "0-200k" or "200k-1M"`

        - `"0-200k"`

        - `"200k-1M"`

      - `cost_type: "code_execution" or "tokens" or "web_search"`

        Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).

        - `"code_execution"`

        - `"tokens"`

        - `"web_search"`

      - `currency: "USD"`

        - `"USD"`

      - `inference_geo: "global" or "us"`

        - `"global"`

        - `"us"`

      - `list_amount: string`

        List-price amount (pre-discount) in fractional cents.

      - `model: string`

      - `product: string`

        Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

      - `rbac_group_id: string`

        RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

      - `requests: number`

        Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

      - `speed: "fast" or "standard"`

        - `"fast"`

        - `"standard"`

      - `token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more`

        Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.

        - `"cache_creation.ephemeral_1h_input_tokens"`

        - `"cache_creation.ephemeral_5m_input_tokens"`

        - `"cache_read_input_tokens"`

        - `"output_tokens"`

        - `"uncached_input_tokens"`

    - `starting_at: string`

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

### User Cost

- `UserCost object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { actor, amount, context_window, 12 more }`

    - `actor: AnalyticsUserActor`

      - `user_id: string`

        Tagged user ID.

      - `deleted: optional boolean`

        True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

      - `email: optional string`

        The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

      - `name: optional string`

        The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `amount: string`

      Amount (post-discount, pre-credit) in fractional cents (minor units).

    - `context_window: "0-200k" or "200k-1M"`

      - `"0-200k"`

      - `"200k-1M"`

    - `cost_type: "code_execution" or "tokens" or "web_search"`

      Cost component breakdown; null when returning the combined total.

      - `"code_execution"`

      - `"tokens"`

      - `"web_search"`

    - `currency: "USD"`

      - `"USD"`

    - `ending_at: string`

    - `inference_geo: "global" or "us"`

      - `"global"`

      - `"us"`

    - `list_amount: string`

      List-price amount (pre-discount) in fractional cents.

    - `model: string`

    - `product: string`

      Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

    - `rbac_group_id: string`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

    - `requests: number`

      Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `speed: "fast" or "standard"`

      - `"fast"`

      - `"standard"`

    - `starting_at: string`

    - `token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more`

      Token type when cost_type=tokens; null otherwise.

      - `"cache_creation.ephemeral_1h_input_tokens"`

      - `"cache_creation.ephemeral_5m_input_tokens"`

      - `"cache_read_input_tokens"`

      - `"output_tokens"`

      - `"uncached_input_tokens"`

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

# Users

## List User Activity

**get** `/v1/organizations/analytics/users`

Get per-user activity for a given day, with cursor-based pagination.

Returns activity metrics for each user in the organization, sorted by email
address. Available to organizations on a Claude Enterprise plan. Requires
an API key with the `read:analytics` scope.

### Query Parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get user activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting_date.

- `filter: optional array of string`

  Filters as 'dimension:value', e.g. filter[]=rbac_group_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

- `group_by: optional array of string`

  Dimensions to break results out by, e.g. group_by[]=rbac_group_id. Supported dimensions vary by endpoint; an unsupported dimension returns 400. Grouped responses paginate like ungrouped ones via next_page. rbac_group_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `order: optional "asc" or "desc"`

  Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order_by names a metric (a top-N ranking). Applies to order_by, or to the endpoint's default sort field when order_by is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column, plus — in date-range mode (starting_date/ending_date) — the endpoint's rankable metrics (metrics default to descending).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

### Returns

- `UserActivity object { data, next_page }`

  Response for GET /v1/organizations/analytics/users.

  - `data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 9 more }`

    - `chat_metrics: object { connectors_used_count, distinct_artifacts_created_count, distinct_connectors_used_count, 9 more }`

      Claude.ai activity metrics for a single user on a given day.

      - `connectors_used_count: number`

        Number of MCP connector invocations.

      - `distinct_artifacts_created_count: number`

        Number of distinct artifacts created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_connectors_used_count: number`

        Distinct claude.ai connectors this user used. Excludes calls whose connector could not be identified and all calls from organizations with zero data retention. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_conversation_count: number`

        Number of distinct conversations the user participated in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_files_uploaded_count: number`

        Number of distinct files uploaded. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_projects_created_count: number`

        Number of distinct projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_projects_used_count: number`

        Number of distinct projects used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_shared_artifacts_viewed_count: number`

        Number of distinct shared artifacts the user viewed. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number`

        Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent

      - `shared_conversations_viewed_count: number`

        Number of times the user opened a shared conversation in a project

      - `thinking_message_count: number`

        Number of messages that used extended thinking

    - `claude_code_metrics: object { core_metrics, tool_actions }`

      Claude Code activity metrics for a single user on a given day.

      - `core_metrics: object { commit_count, distinct_session_count, lines_of_code, pull_request_count }`

        Core Claude Code activity metrics for a single user on a given day.

        - `commit_count: number`

          Number of commits made via Claude Code

        - `distinct_session_count: number`

          Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.

        - `lines_of_code: object { added_count, removed_count }`

          Lines of code added and removed via Claude Code.

          - `added_count: number`

            Lines of code added

          - `removed_count: number`

            Lines of code removed

        - `pull_request_count: number`

          Number of pull requests created via Claude Code

      - `tool_actions: object { edit_tool, multi_edit_tool, notebook_edit_tool, write_tool }`

        Per-tool accepted/rejected counts for Claude Code file modification tools.

        - `edit_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

          - `accepted_count: number`

            Number of tool proposals accepted

          - `rejected_count: number`

            Number of tool proposals rejected

        - `multi_edit_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

        - `notebook_edit_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

        - `write_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

    - `cowork_metrics: object { action_count, connectors_used_count, dispatch_turn_count, 13 more }`

      Cowork activity metrics for a single user on a given day.

      - `action_count: number`

        Number of tool actions completed in Cowork sessions

      - `connectors_used_count: number`

        Total number of connector invocations in Cowork sessions

      - `dispatch_turn_count: number`

        Number of Dispatch (background agent) turns completed

      - `distinct_connectors_used_count: number`

        Number of distinct connectors used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number`

        Number of distinct Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number`

        Number of distinct skills used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Cowork sessions

      - `skills_used_count: number`

        Total number of skill invocations in Cowork sessions

      - `distinct_plugins_used_count: optional number`

        Number of distinct plugins used in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `edit_tool_count: optional number`

        Number of successful Edit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

      - `file_edit_count: optional number`

        Number of successful file-edit tool calls (Edit, MultiEdit, Write, NotebookEdit) in Cowork sessions. Null, never 0, while the file-edit metrics are not enabled for this organization.

      - `multi_edit_tool_count: optional number`

        Number of successful MultiEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

      - `notebook_edit_tool_count: optional number`

        Number of successful NotebookEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

      - `plugins_used_count: optional number`

        Total number of plugin invocations in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization.

      - `sessions_with_file_edits_count: optional number`

        Number of distinct Cowork sessions with at least one successful file-edit tool call. Null while the file-edit metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `write_tool_count: optional number`

        Number of successful Write tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `design_metrics: object { distinct_projects_created_count, distinct_projects_used_count, distinct_session_count, message_count }`

      Claude Design activity metrics for a single user on a given day.

      - `distinct_projects_created_count: number`

        Number of distinct Claude Design projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_projects_used_count: number`

        Number of distinct Claude Design projects the user worked in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number`

        Number of distinct Claude Design sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Claude Design sessions

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single user on a given day, broken out by Office product.

      - `excel: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

        - `connectors_used_count: number`

          Number of MCP connector invocations

        - `distinct_connectors_used_count: number`

          Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

        - `distinct_session_count: number`

          Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

        - `distinct_skills_used_count: number`

          Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

        - `message_count: number`

          Number of messages sent

        - `skills_used_count: number`

          Number of skill invocations

      - `outlook: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

      - `powerpoint: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

      - `word: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

    - `science_metrics: object { delegation_count, distinct_session_count, message_count, 2 more }`

      Claude Science activity metrics for a single user on a given day.

      - `delegation_count: number`

        Number of delegations (handoffs to a specialized agent) in Claude Science sessions

      - `distinct_session_count: number`

        Number of distinct Claude Science sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Claude Science sessions

      - `remote_compute_job_count: number`

        Number of remote compute jobs launched from Claude Science sessions

      - `skills_used_count: number`

        Total number of skill invocations in Claude Science sessions

    - `web_search_count: number`

      Number of web searches performed

    - `distinct_user_count: optional number`

      Number of distinct active users represented by this row. Only set for grouped rollups (group_by[]); null for per-user rows. In date-range mode, recomputed as an exact distinct count of the group's active members over the requested window, never a sum of per-day values.

    - `last_activity_date: optional string`

      Most recent UTC day (YYYY-MM-DD) on which the user had any counted activity, within the requested window: equal to the requested date in single-day mode, and to the latest active day in [starting_date, ending_date) in date-range rollup mode — never a day earlier than the window start. On filtered requests (filter[]) only days matching the filter count: with filter[]=rbac_group_id it is the last day the user was active while a member of that group, consistent with the row's other metrics. Null on grouped (group_by[]) rows. Omitted from the response while last-activity reporting is not enabled for this organization.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user: optional AnalyticsUser`

      User identifier.

      - `id: string`

        Tagged user identifier (e.g. user_...)

      - `email_address: string`

        Email address of the user

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/users \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "chat_metrics": {
        "connectors_used_count": 0,
        "distinct_artifacts_created_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_conversation_count": 0,
        "distinct_files_uploaded_count": 0,
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_shared_artifacts_viewed_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "shared_conversations_viewed_count": 0,
        "thinking_message_count": 0
      },
      "claude_code_metrics": {
        "core_metrics": {
          "commit_count": 0,
          "distinct_session_count": 0,
          "lines_of_code": {
            "added_count": 0,
            "removed_count": 0
          },
          "pull_request_count": 0
        },
        "tool_actions": {
          "edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "multi_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "notebook_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "write_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          }
        }
      },
      "cowork_metrics": {
        "action_count": 0,
        "connectors_used_count": 0,
        "dispatch_turn_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_session_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "skills_used_count": 0,
        "distinct_plugins_used_count": 0,
        "edit_tool_count": 0,
        "file_edit_count": 0,
        "multi_edit_tool_count": 0,
        "notebook_edit_tool_count": 0,
        "plugins_used_count": 0,
        "sessions_with_file_edits_count": 0,
        "write_tool_count": 0
      },
      "design_metrics": {
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_session_count": 0,
        "message_count": 0
      },
      "office_metrics": {
        "excel": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "outlook": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "powerpoint": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "word": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        }
      },
      "science_metrics": {
        "delegation_count": 0,
        "distinct_session_count": 0,
        "message_count": 0,
        "remote_compute_job_count": 0,
        "skills_used_count": 0
      },
      "web_search_count": 0,
      "distinct_user_count": 0,
      "last_activity_date": "last_activity_date",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user": {
        "id": "id",
        "email_address": "email_address"
      }
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### User Activity

- `UserActivity object { data, next_page }`

  Response for GET /v1/organizations/analytics/users.

  - `data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 9 more }`

    - `chat_metrics: object { connectors_used_count, distinct_artifacts_created_count, distinct_connectors_used_count, 9 more }`

      Claude.ai activity metrics for a single user on a given day.

      - `connectors_used_count: number`

        Number of MCP connector invocations.

      - `distinct_artifacts_created_count: number`

        Number of distinct artifacts created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_connectors_used_count: number`

        Distinct claude.ai connectors this user used. Excludes calls whose connector could not be identified and all calls from organizations with zero data retention. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_conversation_count: number`

        Number of distinct conversations the user participated in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_files_uploaded_count: number`

        Number of distinct files uploaded. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_projects_created_count: number`

        Number of distinct projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_projects_used_count: number`

        Number of distinct projects used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_shared_artifacts_viewed_count: number`

        Number of distinct shared artifacts the user viewed. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number`

        Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent

      - `shared_conversations_viewed_count: number`

        Number of times the user opened a shared conversation in a project

      - `thinking_message_count: number`

        Number of messages that used extended thinking

    - `claude_code_metrics: object { core_metrics, tool_actions }`

      Claude Code activity metrics for a single user on a given day.

      - `core_metrics: object { commit_count, distinct_session_count, lines_of_code, pull_request_count }`

        Core Claude Code activity metrics for a single user on a given day.

        - `commit_count: number`

          Number of commits made via Claude Code

        - `distinct_session_count: number`

          Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.

        - `lines_of_code: object { added_count, removed_count }`

          Lines of code added and removed via Claude Code.

          - `added_count: number`

            Lines of code added

          - `removed_count: number`

            Lines of code removed

        - `pull_request_count: number`

          Number of pull requests created via Claude Code

      - `tool_actions: object { edit_tool, multi_edit_tool, notebook_edit_tool, write_tool }`

        Per-tool accepted/rejected counts for Claude Code file modification tools.

        - `edit_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

          - `accepted_count: number`

            Number of tool proposals accepted

          - `rejected_count: number`

            Number of tool proposals rejected

        - `multi_edit_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

        - `notebook_edit_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

        - `write_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

    - `cowork_metrics: object { action_count, connectors_used_count, dispatch_turn_count, 13 more }`

      Cowork activity metrics for a single user on a given day.

      - `action_count: number`

        Number of tool actions completed in Cowork sessions

      - `connectors_used_count: number`

        Total number of connector invocations in Cowork sessions

      - `dispatch_turn_count: number`

        Number of Dispatch (background agent) turns completed

      - `distinct_connectors_used_count: number`

        Number of distinct connectors used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number`

        Number of distinct Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number`

        Number of distinct skills used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Cowork sessions

      - `skills_used_count: number`

        Total number of skill invocations in Cowork sessions

      - `distinct_plugins_used_count: optional number`

        Number of distinct plugins used in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `edit_tool_count: optional number`

        Number of successful Edit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

      - `file_edit_count: optional number`

        Number of successful file-edit tool calls (Edit, MultiEdit, Write, NotebookEdit) in Cowork sessions. Null, never 0, while the file-edit metrics are not enabled for this organization.

      - `multi_edit_tool_count: optional number`

        Number of successful MultiEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

      - `notebook_edit_tool_count: optional number`

        Number of successful NotebookEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

      - `plugins_used_count: optional number`

        Total number of plugin invocations in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization.

      - `sessions_with_file_edits_count: optional number`

        Number of distinct Cowork sessions with at least one successful file-edit tool call. Null while the file-edit metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `write_tool_count: optional number`

        Number of successful Write tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `design_metrics: object { distinct_projects_created_count, distinct_projects_used_count, distinct_session_count, message_count }`

      Claude Design activity metrics for a single user on a given day.

      - `distinct_projects_created_count: number`

        Number of distinct Claude Design projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_projects_used_count: number`

        Number of distinct Claude Design projects the user worked in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number`

        Number of distinct Claude Design sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Claude Design sessions

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single user on a given day, broken out by Office product.

      - `excel: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

        - `connectors_used_count: number`

          Number of MCP connector invocations

        - `distinct_connectors_used_count: number`

          Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

        - `distinct_session_count: number`

          Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

        - `distinct_skills_used_count: number`

          Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

        - `message_count: number`

          Number of messages sent

        - `skills_used_count: number`

          Number of skill invocations

      - `outlook: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

      - `powerpoint: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

      - `word: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

    - `science_metrics: object { delegation_count, distinct_session_count, message_count, 2 more }`

      Claude Science activity metrics for a single user on a given day.

      - `delegation_count: number`

        Number of delegations (handoffs to a specialized agent) in Claude Science sessions

      - `distinct_session_count: number`

        Number of distinct Claude Science sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Claude Science sessions

      - `remote_compute_job_count: number`

        Number of remote compute jobs launched from Claude Science sessions

      - `skills_used_count: number`

        Total number of skill invocations in Claude Science sessions

    - `web_search_count: number`

      Number of web searches performed

    - `distinct_user_count: optional number`

      Number of distinct active users represented by this row. Only set for grouped rollups (group_by[]); null for per-user rows. In date-range mode, recomputed as an exact distinct count of the group's active members over the requested window, never a sum of per-day values.

    - `last_activity_date: optional string`

      Most recent UTC day (YYYY-MM-DD) on which the user had any counted activity, within the requested window: equal to the requested date in single-day mode, and to the latest active day in [starting_date, ending_date) in date-range rollup mode — never a day earlier than the window start. On filtered requests (filter[]) only days matching the filter count: with filter[]=rbac_group_id it is the last day the user was active while a member of that group, consistent with the row's other metrics. Null on grouped (group_by[]) rows. Omitted from the response while last-activity reporting is not enabled for this organization.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user: optional AnalyticsUser`

      User identifier.

      - `id: string`

        Tagged user identifier (e.g. user_...)

      - `email_address: string`

        Email address of the user

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

# Skills

## Get Skill Usage

**get** `/v1/organizations/analytics/skills`

Get per-skill usage for a given day, with cursor-based pagination.

Returns skill usage metrics for the organization, sorted by skill name.
Available to organizations on a Claude Enterprise plan. Requires an API
key with the `read:analytics` scope.

### Query Parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get skill usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting_date.

- `filter: optional array of string`

  Filters as 'dimension:value', e.g. filter[]=rbac_group_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

- `group_by: optional array of string`

  Dimensions to break results out by, e.g. group_by[]=rbac_group_id. Supported dimensions vary by endpoint; an unsupported dimension returns 400. Grouped responses paginate like ungrouped ones via next_page. rbac_group_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `order: optional "asc" or "desc"`

  Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order_by names a metric (a top-N ranking). Applies to order_by, or to the endpoint's default sort field when order_by is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column, plus — in date-range mode (starting_date/ending_date) — the endpoint's rankable metrics (metrics default to descending).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

### Returns

- `SkillUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/skills.

  - `data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 14 more }`

    - `chat_metrics: object { distinct_conversation_skill_used_count }`

      Claude.ai activity metrics for a single skill on a given day.

      - `distinct_conversation_skill_used_count: number`

        Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `claude_code_metrics: object { distinct_session_skill_used_count }`

      Claude Code activity metrics for a single skill on a given day.

      - `distinct_session_skill_used_count: number`

        Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `cowork_metrics: object { distinct_session_skill_used_count }`

      Cowork activity metrics for a single skill on a given day.

      - `distinct_session_skill_used_count: number`

        Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users who used the skill on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted.

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single skill on a given day, broken out by Office product.

      - `excel: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

        - `distinct_session_skill_used_count: number`

          Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `outlook: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

      - `powerpoint: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

      - `word: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

    - `skill_name: string`

      Name of the skill

    - `attributed_list_price: optional string`

      List-price (rate-card) value of the member requests attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD), from Claude Code, Cowork, and Office Agent request-level attribution — the value of requests that INVOLVED the skill, not the skill's incremental cost. Unlike estimated_overage_spend this reflects usage value regardless of how it was funded — seat-covered usage counts — but it is undiscounted and does NOT tie to billed spend or the organization's spend reporting. claude.ai chat usage carries no request-level attribution and contributes nothing: the field is null on chat product rows and on office_agent product cuts dated before 2026-06-18 (the Office Agent attribution data-start), and on ungrouped rows it covers the Claude Code + Cowork + Office Agent share only (null when no attributable usage exists). Also null under the same conditions as estimated_overage_spend (spend reporting not enabled for this organization, data unavailable). "0" means attributable usage existed but none was attributed to this skill. Addable across days: date-range rollup mode returns the window's sum.

    - `currency: optional "USD"`

      Currency for this row's monetary fields (estimated_overage_spend and attributed_list_price), as an uppercase ISO-4217 code. Always "USD" when either amount is populated; null whenever both amounts are null.

      - `"USD"`

    - `enable_count: optional number`

      Distinct accounts that enabled this skill on the requested day (claude.ai only — the skill analog of plugin install_count). The count is org-wide: null when enable reporting is not enabled for this organization, when the request scopes to user_id / rbac_group_id / product via group_by[] or filter[] (an org-wide count would be misleading on per-cut rows), or when enable data is temporarily unavailable. A distinct count, not an event count: summing across days double-counts members who enable the skill on more than one day, so it is also null in date-range rollup mode (starting_date/ending_date).

    - `estimated_overage_spend: optional string`

      Estimated OVERAGE spend attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD; "1250" is $12.50, fractional cents possible) — an allocation of each member's daily post-discount, pre-credit metered overage spend (the same cost basis as the organization's spend reporting and the Cost & Usage API, so per-skill figures are directly comparable; spend with no skill attribution — including any member-day without skill invocations — is not represented, so skill rows sum to at most those totals) across the skills the member used. Overage only: usage covered by included seat allowances bills nothing and allocates $0 here — see attributed_list_price for the funding-independent usage-value companion. Claude Code, Cowork, and Office Agent spend use request-level skill attribution; claude.ai chat spend is approximated proportionally to skill-invoking messages. An estimate, not a billing number — and the cost of the requests/messages that INVOLVED the skill, not the skill's incremental cost (the same request would still have cost something without the skill active). "0" means no overage spend was attributed; null when spend reporting is not enabled for this organization, on office_agent product cuts dated before 2026-06-18 (the Office Agent attribution data-start), or when spend data is temporarily unavailable. Addable across days: date-range rollup mode (starting_date/ending_date) returns the window's sum. With group_by[]=user_id each row carries the user's own attributed spend.

    - `invocation_count: optional number`

      Total number of times this skill was invoked on the requested day (the skill analog of plugin invocation_count). Unlike distinct_user_count — which answers '\# of users' — this is the true '# of uses'. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Null when invocation reporting is not enabled for this organization. Sum across a date range for total uses in the window — date-range rollup mode (starting_date/ending_date) returns this sum directly.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `share_status: optional string`

      Skill share status (claude.ai only): one of 'private', 'organization', or 'public'. Null for skills used only in Claude Code or Office (no per-skill share-status concept) and when share-status reporting is not yet available for the organization. Filterable via filter[]=share_status:<value>.

    - `skill_display_name: optional string`

      Human-readable display name for rows whose skill_name is an opaque skill id (user/organization skill types — user-defined names are withheld from the analytics pipeline). Only organization-shared skills resolve; the literal 'unknown' bucket row also gets a fixed 'Unknown skill' label. Null for private (user-defined) skills — their names are not disclosed to analytics-key holders — and null when skill_name is already a display name, when the skill was deleted, or when display-name resolution is not enabled for this organization.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/skills \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "chat_metrics": {
        "distinct_conversation_skill_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_skill_used_count": 0
        },
        "outlook": {
          "distinct_session_skill_used_count": 0
        },
        "powerpoint": {
          "distinct_session_skill_used_count": 0
        },
        "word": {
          "distinct_session_skill_used_count": 0
        }
      },
      "skill_name": "skill_name",
      "attributed_list_price": "attributed_list_price",
      "currency": "USD",
      "enable_count": 0,
      "estimated_overage_spend": "estimated_overage_spend",
      "invocation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "share_status": "share_status",
      "skill_display_name": "skill_display_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Skill Usage

- `SkillUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/skills.

  - `data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 14 more }`

    - `chat_metrics: object { distinct_conversation_skill_used_count }`

      Claude.ai activity metrics for a single skill on a given day.

      - `distinct_conversation_skill_used_count: number`

        Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `claude_code_metrics: object { distinct_session_skill_used_count }`

      Claude Code activity metrics for a single skill on a given day.

      - `distinct_session_skill_used_count: number`

        Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `cowork_metrics: object { distinct_session_skill_used_count }`

      Cowork activity metrics for a single skill on a given day.

      - `distinct_session_skill_used_count: number`

        Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users who used the skill on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted.

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single skill on a given day, broken out by Office product.

      - `excel: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

        - `distinct_session_skill_used_count: number`

          Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `outlook: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

      - `powerpoint: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

      - `word: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

    - `skill_name: string`

      Name of the skill

    - `attributed_list_price: optional string`

      List-price (rate-card) value of the member requests attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD), from Claude Code, Cowork, and Office Agent request-level attribution — the value of requests that INVOLVED the skill, not the skill's incremental cost. Unlike estimated_overage_spend this reflects usage value regardless of how it was funded — seat-covered usage counts — but it is undiscounted and does NOT tie to billed spend or the organization's spend reporting. claude.ai chat usage carries no request-level attribution and contributes nothing: the field is null on chat product rows and on office_agent product cuts dated before 2026-06-18 (the Office Agent attribution data-start), and on ungrouped rows it covers the Claude Code + Cowork + Office Agent share only (null when no attributable usage exists). Also null under the same conditions as estimated_overage_spend (spend reporting not enabled for this organization, data unavailable). "0" means attributable usage existed but none was attributed to this skill. Addable across days: date-range rollup mode returns the window's sum.

    - `currency: optional "USD"`

      Currency for this row's monetary fields (estimated_overage_spend and attributed_list_price), as an uppercase ISO-4217 code. Always "USD" when either amount is populated; null whenever both amounts are null.

      - `"USD"`

    - `enable_count: optional number`

      Distinct accounts that enabled this skill on the requested day (claude.ai only — the skill analog of plugin install_count). The count is org-wide: null when enable reporting is not enabled for this organization, when the request scopes to user_id / rbac_group_id / product via group_by[] or filter[] (an org-wide count would be misleading on per-cut rows), or when enable data is temporarily unavailable. A distinct count, not an event count: summing across days double-counts members who enable the skill on more than one day, so it is also null in date-range rollup mode (starting_date/ending_date).

    - `estimated_overage_spend: optional string`

      Estimated OVERAGE spend attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD; "1250" is $12.50, fractional cents possible) — an allocation of each member's daily post-discount, pre-credit metered overage spend (the same cost basis as the organization's spend reporting and the Cost & Usage API, so per-skill figures are directly comparable; spend with no skill attribution — including any member-day without skill invocations — is not represented, so skill rows sum to at most those totals) across the skills the member used. Overage only: usage covered by included seat allowances bills nothing and allocates $0 here — see attributed_list_price for the funding-independent usage-value companion. Claude Code, Cowork, and Office Agent spend use request-level skill attribution; claude.ai chat spend is approximated proportionally to skill-invoking messages. An estimate, not a billing number — and the cost of the requests/messages that INVOLVED the skill, not the skill's incremental cost (the same request would still have cost something without the skill active). "0" means no overage spend was attributed; null when spend reporting is not enabled for this organization, on office_agent product cuts dated before 2026-06-18 (the Office Agent attribution data-start), or when spend data is temporarily unavailable. Addable across days: date-range rollup mode (starting_date/ending_date) returns the window's sum. With group_by[]=user_id each row carries the user's own attributed spend.

    - `invocation_count: optional number`

      Total number of times this skill was invoked on the requested day (the skill analog of plugin invocation_count). Unlike distinct_user_count — which answers '\# of users' — this is the true '# of uses'. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Null when invocation reporting is not enabled for this organization. Sum across a date range for total uses in the window — date-range rollup mode (starting_date/ending_date) returns this sum directly.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `share_status: optional string`

      Skill share status (claude.ai only): one of 'private', 'organization', or 'public'. Null for skills used only in Claude Code or Office (no per-skill share-status concept) and when share-status reporting is not yet available for the organization. Filterable via filter[]=share_status:<value>.

    - `skill_display_name: optional string`

      Human-readable display name for rows whose skill_name is an opaque skill id (user/organization skill types — user-defined names are withheld from the analytics pipeline). Only organization-shared skills resolve; the literal 'unknown' bucket row also gets a fixed 'Unknown skill' label. Null for private (user-defined) skills — their names are not disclosed to analytics-key holders — and null when skill_name is already a display name, when the skill was deleted, or when display-name resolution is not enabled for this organization.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

# Connectors

## Get Connector Usage

**get** `/v1/organizations/analytics/connectors`

Get per-connector usage for a given day, with cursor-based pagination.

Returns connector usage metrics for the organization, sorted by connector
name. Connector names are normalized from their various sources — for
example, "Atlassian MCP server" and "mcp-atlassian" both appear as
"atlassian". Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

### Query Parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get connector usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting_date.

- `filter: optional array of string`

  Filters as 'dimension:value', e.g. filter[]=rbac_group_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

- `group_by: optional array of string`

  Dimensions to break results out by, e.g. group_by[]=rbac_group_id. Supported dimensions vary by endpoint; an unsupported dimension returns 400. Grouped responses paginate like ungrouped ones via next_page. rbac_group_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `order: optional "asc" or "desc"`

  Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order_by names a metric (a top-N ranking). Applies to order_by, or to the endpoint's default sort field when order_by is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column, plus — in date-range mode (starting_date/ending_date) — the endpoint's rankable metrics (metrics default to descending).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

### Returns

- `ConnectorUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/connectors.

  - `data: array of object { chat_metrics, claude_code_metrics, connector_name, 10 more }`

    - `chat_metrics: object { distinct_conversation_connector_used_count }`

      Claude.ai activity metrics for a single connector on a given day.

      - `distinct_conversation_connector_used_count: number`

        Number of distinct conversations in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `claude_code_metrics: object { distinct_session_connector_used_count }`

      Claude Code activity metrics for a single connector on a given day.

      - `distinct_session_connector_used_count: number`

        Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `connector_name: string`

      Name of the connector

    - `cowork_metrics: object { distinct_session_connector_used_count }`

      Cowork activity metrics for a single connector on a given day.

      - `distinct_session_connector_used_count: number`

        Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users who used the connector on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single connector on a given day, broken out by Office product.

      - `excel: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

        - `distinct_session_connector_used_count: number`

          Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `outlook: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

      - `powerpoint: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

      - `word: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `read_call_count: optional number`

      Number of connector tool calls on the requested day whose trusted read-only annotation marked them read-only. Call count, not distinct users. Every call recorded on a classified surface lands in exactly one of read_call_count, write_call_count, or unclassified_call_count, so the three sum to the day's classified calls. Classification is forward-only per surface: claude.ai from 2026-06-01, Claude Code from 2026-05-30, Claude in Office from 2026-05-29, Cowork from 2026-06-02 (Cowork clients predating annotation forwarding land in unclassified_call_count). Null, never 0, when the value cannot be stated: the read/write split is not enabled for this organization, or the day predates 2026-05-29. For a date-range total, sum the per-day values, but treat a window that extends before 2026-05-29 as null rather than summing only its covered days — date-range rollup mode (starting_date/ending_date) applies both rules server-side.

    - `unclassified_call_count: optional number`

      Number of connector tool calls on the requested day with no trusted read-only annotation — the annotation is optional in the MCP spec and is discarded when connector access controls are active, so unclassified calls are common. This field shows how much of the day's classified activity the read/write split actually covers. Call count, not distinct users. One of the three call-classification buckets; see read_call_count for the per-surface data-start dates, null conditions, and date-range guidance.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

    - `write_call_count: optional number`

      Number of connector tool calls on the requested day whose trusted read-only annotation marked them not read-only. Call count, not distinct users. One of the three call-classification buckets; see read_call_count for the per-surface data-start dates, null conditions, and date-range guidance.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/connectors \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "chat_metrics": {
        "distinct_conversation_connector_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "connector_name": "connector_name",
      "cowork_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_connector_used_count": 0
        },
        "outlook": {
          "distinct_session_connector_used_count": 0
        },
        "powerpoint": {
          "distinct_session_connector_used_count": 0
        },
        "word": {
          "distinct_session_connector_used_count": 0
        }
      },
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "read_call_count": 0,
      "unclassified_call_count": 0,
      "user_id": "user_id",
      "write_call_count": 0
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Connector Usage

- `ConnectorUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/connectors.

  - `data: array of object { chat_metrics, claude_code_metrics, connector_name, 10 more }`

    - `chat_metrics: object { distinct_conversation_connector_used_count }`

      Claude.ai activity metrics for a single connector on a given day.

      - `distinct_conversation_connector_used_count: number`

        Number of distinct conversations in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `claude_code_metrics: object { distinct_session_connector_used_count }`

      Claude Code activity metrics for a single connector on a given day.

      - `distinct_session_connector_used_count: number`

        Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `connector_name: string`

      Name of the connector

    - `cowork_metrics: object { distinct_session_connector_used_count }`

      Cowork activity metrics for a single connector on a given day.

      - `distinct_session_connector_used_count: number`

        Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users who used the connector on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single connector on a given day, broken out by Office product.

      - `excel: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

        - `distinct_session_connector_used_count: number`

          Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `outlook: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

      - `powerpoint: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

      - `word: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `read_call_count: optional number`

      Number of connector tool calls on the requested day whose trusted read-only annotation marked them read-only. Call count, not distinct users. Every call recorded on a classified surface lands in exactly one of read_call_count, write_call_count, or unclassified_call_count, so the three sum to the day's classified calls. Classification is forward-only per surface: claude.ai from 2026-06-01, Claude Code from 2026-05-30, Claude in Office from 2026-05-29, Cowork from 2026-06-02 (Cowork clients predating annotation forwarding land in unclassified_call_count). Null, never 0, when the value cannot be stated: the read/write split is not enabled for this organization, or the day predates 2026-05-29. For a date-range total, sum the per-day values, but treat a window that extends before 2026-05-29 as null rather than summing only its covered days — date-range rollup mode (starting_date/ending_date) applies both rules server-side.

    - `unclassified_call_count: optional number`

      Number of connector tool calls on the requested day with no trusted read-only annotation — the annotation is optional in the MCP spec and is discarded when connector access controls are active, so unclassified calls are common. This field shows how much of the day's classified activity the read/write split actually covers. Call count, not distinct users. One of the three call-classification buckets; see read_call_count for the per-surface data-start dates, null conditions, and date-range guidance.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

    - `write_call_count: optional number`

      Number of connector tool calls on the requested day whose trusted read-only annotation marked them not read-only. Call count, not distinct users. One of the three call-classification buckets; see read_call_count for the per-surface data-start dates, null conditions, and date-range guidance.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

# Chat Projects

## Get Chat Project Usage

**get** `/v1/organizations/analytics/apps/chat/projects`

Get per-project activity for a given day, with cursor-based pagination.

Returns activity metrics for each project in the organization, sorted by
project ID. Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

### Query Parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get project activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting_date.

- `filter: optional array of string`

  Filters as 'dimension:value', e.g. filter[]=rbac_group_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

- `group_by: optional array of string`

  Dimensions to break results out by, e.g. group_by[]=rbac_group_id. Supported dimensions vary by endpoint; an unsupported dimension returns 400. Grouped responses paginate like ungrouped ones via next_page. rbac_group_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `order: optional "asc" or "desc"`

  Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order_by names a metric (a top-N ranking). Applies to order_by, or to the endpoint's default sort field when order_by is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column, plus — in date-range mode (starting_date/ending_date) — the endpoint's rankable metrics (metrics default to descending).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

### Returns

- `ChatProjectUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/apps/chat/projects.

  - `data: array of object { distinct_user_count, message_count, project_id, 8 more }`

    - `distinct_user_count: number`

      Number of distinct users who used the project on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `message_count: number`

      Number of messages sent in the project on the requested day

    - `project_id: string`

      Tagged project identifier (e.g. claude_proj_...)

    - `project_name: string`

      Name of the project

    - `created_at: optional string`

      Project creation timestamp, RFC 3339. Null if the project was deleted before attribution was recorded.

    - `created_by: optional AnalyticsUser`

      User identifier.

      - `id: string`

        Tagged user identifier (e.g. user_...)

      - `email_address: string`

        Email address of the user

    - `distinct_conversation_count: optional number`

      Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/apps/chat/projects \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "created_at": "created_at",
      "created_by": {
        "id": "id",
        "email_address": "email_address"
      },
      "distinct_conversation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Chat Project Usage

- `ChatProjectUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/apps/chat/projects.

  - `data: array of object { distinct_user_count, message_count, project_id, 8 more }`

    - `distinct_user_count: number`

      Number of distinct users who used the project on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `message_count: number`

      Number of messages sent in the project on the requested day

    - `project_id: string`

      Tagged project identifier (e.g. claude_proj_...)

    - `project_name: string`

      Name of the project

    - `created_at: optional string`

      Project creation timestamp, RFC 3339. Null if the project was deleted before attribution was recorded.

    - `created_by: optional AnalyticsUser`

      User identifier.

      - `id: string`

        Tagged user identifier (e.g. user_...)

      - `email_address: string`

        Email address of the user

    - `distinct_conversation_count: optional number`

      Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

# Plugins

## Get Plugin Usage

**get** `/v1/organizations/analytics/plugins`

Get per-plugin install + invocation usage for a given day, with pagination.

Returns plugin usage metrics for the organization across Cowork and Claude
Code, sorted by plugin name. The `plugin_name` value `third-party` is
an aggregate bucket, not a plugin: it collects plugin activity, from
either surface, for which the reporting client did not provide a plugin
name — so an organization's own plugins can contribute both to their own
named rows and to this bucket. Requires an API key with the
`read:analytics` scope. `starting_date` / `ending_date` select
range-rollup mode like /skills.

### Query Parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get plugin usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting_date.

- `filter: optional array of string`

  Filters as 'dimension:value', e.g. filter[]=rbac_group_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

- `group_by: optional array of string`

  Dimensions to break results out by, e.g. group_by[]=rbac_group_id. Supported dimensions vary by endpoint; an unsupported dimension returns 400. Grouped responses paginate like ungrouped ones via next_page. rbac_group_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `order: optional "asc" or "desc"`

  Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order_by names a metric (a top-N ranking). Applies to order_by, or to the endpoint's default sort field when order_by is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column, plus — in date-range mode (starting_date/ending_date) — the endpoint's rankable metrics (metrics default to descending).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

### Returns

- `PluginUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/plugins.

  - `data: array of object { claude_code_metrics, cowork_metrics, distinct_user_count, 8 more }`

    - `claude_code_metrics: object { distinct_session_plugin_used_count }`

      Claude Code activity metrics for a single plugin on a given day.

      - `distinct_session_plugin_used_count: number`

        Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

    - `cowork_metrics: object { distinct_session_plugin_used_count }`

      Cowork activity metrics for a single plugin on a given day.

      - `distinct_session_plugin_used_count: number`

        Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users with recorded install or invocation activity for the plugin on the requested day (install-only users count), or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `install_count: number`

      Number of distinct users who installed the plugin on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `invocation_count: number`

      Number of plugin invocations on the requested day

    - `plugin_name: string`

      Name of the plugin

    - `plugin_id: optional string`

      Stable plugin identifier when available (e.g. serena@claude-plugins-official). Null for third-party Claude Code plugins (redacted at the source) and Cowork slash commands that carry only a hashed id.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/plugins \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "claude_code_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "distinct_user_count": 0,
      "install_count": 0,
      "invocation_count": 0,
      "plugin_name": "plugin_name",
      "plugin_id": "plugin_id",
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Plugin Usage

- `PluginUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/plugins.

  - `data: array of object { claude_code_metrics, cowork_metrics, distinct_user_count, 8 more }`

    - `claude_code_metrics: object { distinct_session_plugin_used_count }`

      Claude Code activity metrics for a single plugin on a given day.

      - `distinct_session_plugin_used_count: number`

        Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

    - `cowork_metrics: object { distinct_session_plugin_used_count }`

      Cowork activity metrics for a single plugin on a given day.

      - `distinct_session_plugin_used_count: number`

        Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users with recorded install or invocation activity for the plugin on the requested day (install-only users count), or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `install_count: number`

      Number of distinct users who installed the plugin on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `invocation_count: number`

      Number of plugin invocations on the requested day

    - `plugin_name: string`

      Name of the plugin

    - `plugin_id: optional string`

      Stable plugin identifier when available (e.g. serena@claude-plugins-official). Null for third-party Claude Code plugins (redacted at the source) and Cowork slash commands that carry only a hashed id.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

# Artifacts

## Get Artifact Activity

**get** `/v1/organizations/analytics/artifacts`

Get artifact-creation activity for a given day, broken out by MIME type.

Returns the full (artifact_type, is_shared) cube for the organization;
`next_page` is null except for grouped queries, which paginate. Requires
an API key with the `read:analytics` scope.

### Query Parameters

- `date: string`

  UTC date in YYYY-MM-DD format. The day to get artifact activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `filter: optional array of string`

  Filters as 'dimension:value', e.g. filter[]=rbac_group_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

- `group_by: optional array of string`

  Dimensions to break results out by: user_id and/or rbac_group_id. The ungrouped artifact-type cube is finite and returned in full; grouped queries multiply the cube and paginate via next_page. rbac_group_id attributes a user to every group they held at any point during the requested UTC day, so grouped rows are not an exclusive partition. At most 100 entries.

- `limit: optional number`

  Maximum rows to return (1-1000, default 100). The ungrouped artifact-type cube is finite and returned in full; limit is the page size only when group_by[] multiplies the cube.

- `page: optional string`

  Opaque cursor from a previous response's next_page field. Only valid with group_by[] — the ungrouped cube is never paginated.

### Returns

- `ArtifactUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/artifacts.

  `next_page` is null on ungrouped queries — the artifact-type cube is
  finite and returned in full. Grouped queries (group_by[] on user_id /
  rbac_group_id) multiply the cube and paginate like the other analytics
  list endpoints.

  - `data: array of object { artifact_type, artifacts_created_count, distinct_user_count, 6 more }`

    - `artifact_type: string`

      Canonical artifact MIME type (e.g. text/markdown, application/vnd.ant.react, image/svg+xml), or 'other'.

    - `artifacts_created_count: number`

      Number of artifacts created in this bucket on the requested day

    - `distinct_user_count: number`

      Number of distinct users who created artifacts in this bucket on the requested day

    - `is_shared: boolean`

      Whether the artifacts in this bucket have ever been shared.

    - `published_artifacts_created_count: number`

      Number of those artifacts that have been published

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: optional string`

    Cursor for the next page of a grouped query; always null for the ungrouped artifact-type cube, which is returned in full.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/artifacts \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "artifact_type": "artifact_type",
      "artifacts_created_count": 0,
      "distinct_user_count": 0,
      "is_shared": true,
      "published_artifacts_created_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Artifact Usage

- `ArtifactUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/artifacts.

  `next_page` is null on ungrouped queries — the artifact-type cube is
  finite and returned in full. Grouped queries (group_by[] on user_id /
  rbac_group_id) multiply the cube and paginate like the other analytics
  list endpoints.

  - `data: array of object { artifact_type, artifacts_created_count, distinct_user_count, 6 more }`

    - `artifact_type: string`

      Canonical artifact MIME type (e.g. text/markdown, application/vnd.ant.react, image/svg+xml), or 'other'.

    - `artifacts_created_count: number`

      Number of artifacts created in this bucket on the requested day

    - `distinct_user_count: number`

      Number of distinct users who created artifacts in this bucket on the requested day

    - `is_shared: boolean`

      Whether the artifacts in this bucket have ever been shared.

    - `published_artifacts_created_count: number`

      Number of those artifacts that have been published

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: optional string`

    Cursor for the next page of a grouped query; always null for the ungrouped artifact-type cube, which is returned in full.

# Spend Limits

## Set Spend Limit

**post** `/v1/organizations/spend_limits`

Set a per-user spend limit override.

Upsert keyed on (scope, period): setting a limit that already exists
overwrites it in place. Only `scope.type: "user"` is accepted; seat-tier,
group, and organization-level defaults are configured in claude.ai.

### Body Parameters

- `amount: string`

- `scope: object { type, user_id }`

  - `type: "user"`

    - `"user"`

  - `user_id: string`

- `period: optional "daily" or "monthly" or "weekly"`

  - `"daily"`

  - `"monthly"`

  - `"weekly"`

### Returns

- `SpendLimit object { id, amount, created_at, 5 more }`

  - `id: string`

  - `amount: string`

  - `created_at: string`

  - `currency: string`

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `scope: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

    - `User object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `SeatTier object { seat_tier, type }`

      - `seat_tier: string`

      - `type: "seat_tier"`

        - `"seat_tier"`

    - `RbacGroup object { rbac_group_id, type }`

      - `rbac_group_id: string`

      - `type: "rbac_group"`

        - `"rbac_group"`

    - `OrganizationService object { service, type }`

      - `service: string`

      - `type: "organization_service"`

        - `"organization_service"`

    - `Organization object { type }`

      - `type: "organization"`

        - `"organization"`

  - `type: "spend_limit"`

    - `"spend_limit"`

  - `updated_at: string`

### Example

```http
curl https://api.anthropic.com/v1/organizations/spend_limits \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "amount": "50000",
          "scope": {
            "type": "user",
            "user_id": "user_id"
          },
          "period": "monthly"
        }'
```

#### Response

```json
{
  "id": "id",
  "amount": "50000",
  "created_at": "2019-12-27T18:11:19.117Z",
  "currency": "USD",
  "period": "monthly",
  "scope": {
    "type": "user",
    "user_id": "user_id"
  },
  "type": "spend_limit",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Get Spend Limit

**get** `/v1/organizations/spend_limits/{spend_limit_id}`

Retrieve a spend limit by ID.

### Path Parameters

- `spend_limit_id: string`

  ID of the Spend Limit.

### Returns

- `SpendLimit object { id, amount, created_at, 5 more }`

  - `id: string`

  - `amount: string`

  - `created_at: string`

  - `currency: string`

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `scope: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

    - `User object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `SeatTier object { seat_tier, type }`

      - `seat_tier: string`

      - `type: "seat_tier"`

        - `"seat_tier"`

    - `RbacGroup object { rbac_group_id, type }`

      - `rbac_group_id: string`

      - `type: "rbac_group"`

        - `"rbac_group"`

    - `OrganizationService object { service, type }`

      - `service: string`

      - `type: "organization_service"`

        - `"organization_service"`

    - `Organization object { type }`

      - `type: "organization"`

        - `"organization"`

  - `type: "spend_limit"`

    - `"spend_limit"`

  - `updated_at: string`

### Example

```http
curl https://api.anthropic.com/v1/organizations/spend_limits/$SPEND_LIMIT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "id",
  "amount": "50000",
  "created_at": "2019-12-27T18:11:19.117Z",
  "currency": "USD",
  "period": "monthly",
  "scope": {
    "type": "user",
    "user_id": "user_id"
  },
  "type": "spend_limit",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

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

## List Effective Spend Limits

**get** `/v1/organizations/spend_limits/effective`

List each member's effective spend limit and period-to-date spend.

Returns one row per (member, period) the member resolves a spend limit
for, with the `source` scope the spend limit was inherited from.
Paginates by member, so a member's periods never split across pages.

### Query Parameters

- `limit: optional number`

- `page: optional string`

- `period: optional array of string`

- `user_ids: optional array of string`

### Returns

- `data: array of SpendSummary`

  - `actor: object { deleted, email_address, name, 2 more }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `deleted: boolean`

    - `email_address: string`

    - `name: string`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

  - `amount: string`

  - `currency: string`

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `period_to_date_spend: string`

  - `scope: object { type, user_id }`

    - `type: "user"`

      - `"user"`

    - `user_id: string`

  - `source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

    - `User object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `SeatTier object { seat_tier, type }`

      - `seat_tier: string`

      - `type: "seat_tier"`

        - `"seat_tier"`

    - `RbacGroup object { rbac_group_id, type }`

      - `rbac_group_id: string`

      - `type: "rbac_group"`

        - `"rbac_group"`

    - `OrganizationService object { service, type }`

      - `service: string`

      - `type: "organization_service"`

        - `"organization_service"`

    - `Organization object { type }`

      - `type: "organization"`

        - `"organization"`

  - `spend_limit_id: string`

- `next_page: string`

### Example

```http
curl https://api.anthropic.com/v1/organizations/spend_limits/effective \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_id"
      },
      "amount": "50000",
      "currency": "USD",
      "period": "monthly",
      "period_to_date_spend": "period_to_date_spend",
      "scope": {
        "type": "user",
        "user_id": "user_id"
      },
      "source": {
        "type": "user",
        "user_id": "user_id"
      },
      "spend_limit_id": "spend_limit_id"
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Spend Limit

- `SpendLimit object { id, amount, created_at, 5 more }`

  - `id: string`

  - `amount: string`

  - `created_at: string`

  - `currency: string`

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `scope: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

    - `User object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `SeatTier object { seat_tier, type }`

      - `seat_tier: string`

      - `type: "seat_tier"`

        - `"seat_tier"`

    - `RbacGroup object { rbac_group_id, type }`

      - `rbac_group_id: string`

      - `type: "rbac_group"`

        - `"rbac_group"`

    - `OrganizationService object { service, type }`

      - `service: string`

      - `type: "organization_service"`

        - `"organization_service"`

    - `Organization object { type }`

      - `type: "organization"`

        - `"organization"`

  - `type: "spend_limit"`

    - `"spend_limit"`

  - `updated_at: string`

### Spend Summary

- `SpendSummary object { actor, amount, currency, 5 more }`

  Per-member effective-limit report row (GET /spend_limits/effective).

  - `actor: object { deleted, email_address, name, 2 more }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `deleted: boolean`

    - `email_address: string`

    - `name: string`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

  - `amount: string`

  - `currency: string`

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `period_to_date_spend: string`

  - `scope: object { type, user_id }`

    - `type: "user"`

      - `"user"`

    - `user_id: string`

  - `source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

    - `User object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `SeatTier object { seat_tier, type }`

      - `seat_tier: string`

      - `type: "seat_tier"`

        - `"seat_tier"`

    - `RbacGroup object { rbac_group_id, type }`

      - `rbac_group_id: string`

      - `type: "rbac_group"`

        - `"rbac_group"`

    - `OrganizationService object { service, type }`

      - `service: string`

      - `type: "organization_service"`

        - `"organization_service"`

    - `Organization object { type }`

      - `type: "organization"`

        - `"organization"`

  - `spend_limit_id: string`

### Spend Limit Delete Response

- `SpendLimitDeleteResponse object { id, type }`

  - `id: string`

  - `type: "spend_limit_deleted"`

    - `"spend_limit_deleted"`

# Increase Requests

## List Spend Limit Increase Requests

**get** `/v1/organizations/spend_limit_increase_requests`

List spend limit increase requests, most recent first.

Pending requests include a live `spend_summary` for the requester.
Requests whose requester is no longer a member are excluded.

### Query Parameters

- `actor_ids: optional array of string`

  Filter by requester, as `user_...` tagged IDs.

- `limit: optional number`

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

- `status: optional array of "approved" or "denied" or "pending"`

  Filter by status. Omit to return all.

  - `"approved"`

  - `"denied"`

  - `"pending"`

### Returns

- `data: array of SpendLimitIncreaseRequest`

  - `id: string`

  - `actor: object { deleted, email_address, name, 2 more }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `deleted: boolean`

    - `email_address: string`

    - `name: string`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

  - `created_at: string`

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `resolved_at: string`

  - `resolved_by: object { deleted, email_address, name, 2 more }  or object { scoped_api_key_id, type }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `UserActor object { deleted, email_address, name, 2 more }`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `deleted: boolean`

      - `email_address: string`

      - `name: string`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

    - `ScopedAPIKeyActor object { scoped_api_key_id, type }`

      A scoped Admin API key acting on behalf of the organization.

      - `scoped_api_key_id: string`

      - `type: "scoped_api_key_actor"`

        - `"scoped_api_key_actor"`

  - `spend_summary: SpendSummary`

    Per-member effective-limit report row (GET /spend_limits/effective).

    - `actor: object { deleted, email_address, name, 2 more }`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `deleted: boolean`

      - `email_address: string`

      - `name: string`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

    - `amount: string`

    - `currency: string`

    - `period: "daily" or "monthly" or "weekly"`

      - `"daily"`

      - `"monthly"`

      - `"weekly"`

    - `period_to_date_spend: string`

    - `scope: object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

      - `User object { type, user_id }`

        - `type: "user"`

          - `"user"`

        - `user_id: string`

      - `SeatTier object { seat_tier, type }`

        - `seat_tier: string`

        - `type: "seat_tier"`

          - `"seat_tier"`

      - `RbacGroup object { rbac_group_id, type }`

        - `rbac_group_id: string`

        - `type: "rbac_group"`

          - `"rbac_group"`

      - `OrganizationService object { service, type }`

        - `service: string`

        - `type: "organization_service"`

          - `"organization_service"`

      - `Organization object { type }`

        - `type: "organization"`

          - `"organization"`

    - `spend_limit_id: string`

  - `status: "approved" or "denied" or "pending"`

    - `"approved"`

    - `"denied"`

    - `"pending"`

  - `type: "spend_limit_increase_request"`

    - `"spend_limit_increase_request"`

- `next_page: string`

### Example

```http
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_id"
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "period": "monthly",
      "resolved_at": "2019-12-27T18:11:19.117Z",
      "resolved_by": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_id"
      },
      "spend_summary": {
        "actor": {
          "deleted": true,
          "email_address": "email_address",
          "name": "name",
          "type": "user_actor",
          "user_id": "user_id"
        },
        "amount": "50000",
        "currency": "USD",
        "period": "monthly",
        "period_to_date_spend": "period_to_date_spend",
        "scope": {
          "type": "user",
          "user_id": "user_id"
        },
        "source": {
          "type": "user",
          "user_id": "user_id"
        },
        "spend_limit_id": "spend_limit_id"
      },
      "status": "approved",
      "type": "spend_limit_increase_request"
    }
  ],
  "next_page": "next_page"
}
```

## Get Spend Limit Increase Request

**get** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}`

Retrieve a spend limit increase request.

While `pending`, the response includes a live `spend_summary` for the
requester at the request's period.

### Path Parameters

- `spend_limit_increase_request_id: string`

  ID of the spend limit increase request.

### Returns

- `SpendLimitIncreaseRequest object { id, actor, created_at, 6 more }`

  - `id: string`

  - `actor: object { deleted, email_address, name, 2 more }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `deleted: boolean`

    - `email_address: string`

    - `name: string`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

  - `created_at: string`

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `resolved_at: string`

  - `resolved_by: object { deleted, email_address, name, 2 more }  or object { scoped_api_key_id, type }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `UserActor object { deleted, email_address, name, 2 more }`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `deleted: boolean`

      - `email_address: string`

      - `name: string`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

    - `ScopedAPIKeyActor object { scoped_api_key_id, type }`

      A scoped Admin API key acting on behalf of the organization.

      - `scoped_api_key_id: string`

      - `type: "scoped_api_key_actor"`

        - `"scoped_api_key_actor"`

  - `spend_summary: SpendSummary`

    Per-member effective-limit report row (GET /spend_limits/effective).

    - `actor: object { deleted, email_address, name, 2 more }`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `deleted: boolean`

      - `email_address: string`

      - `name: string`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

    - `amount: string`

    - `currency: string`

    - `period: "daily" or "monthly" or "weekly"`

      - `"daily"`

      - `"monthly"`

      - `"weekly"`

    - `period_to_date_spend: string`

    - `scope: object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

      - `User object { type, user_id }`

        - `type: "user"`

          - `"user"`

        - `user_id: string`

      - `SeatTier object { seat_tier, type }`

        - `seat_tier: string`

        - `type: "seat_tier"`

          - `"seat_tier"`

      - `RbacGroup object { rbac_group_id, type }`

        - `rbac_group_id: string`

        - `type: "rbac_group"`

          - `"rbac_group"`

      - `OrganizationService object { service, type }`

        - `service: string`

        - `type: "organization_service"`

          - `"organization_service"`

      - `Organization object { type }`

        - `type: "organization"`

          - `"organization"`

    - `spend_limit_id: string`

  - `status: "approved" or "denied" or "pending"`

    - `"approved"`

    - `"denied"`

    - `"pending"`

  - `type: "spend_limit_increase_request"`

    - `"spend_limit_increase_request"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "monthly",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_id"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "monthly",
    "period_to_date_spend": "period_to_date_spend",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    },
    "source": {
      "type": "user",
      "user_id": "user_id"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

## Approve Spend Limit Increase Request

**post** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve`

Approve a pending spend limit increase request.

Writes a per-user spend limit at `amount` for the requester and
transitions the request to `approved`. `period` defaults to the period
the member was blocked on. Anthropic emails the requester unless
`suppress_notification` is set.

### Path Parameters

- `spend_limit_increase_request_id: string`

  ID of the spend limit increase request.

### Body Parameters

- `amount: string`

  New per-user spend limit as a non-negative integer decimal string (minor units).

- `period: optional "daily" or "monthly" or "weekly"`

  - `"daily"`

  - `"monthly"`

  - `"weekly"`

- `suppress_notification: optional boolean`

### Returns

- `id: string`

- `actor: object { deleted, email_address, name, 2 more }`

  A user within the organization. `name` and `email_address` are
  null when the underlying account is unavailable or has been deleted;
  `deleted` is true only for deleted accounts.

  - `deleted: boolean`

  - `email_address: string`

  - `name: string`

  - `type: "user_actor"`

    - `"user_actor"`

  - `user_id: string`

- `created_at: string`

- `period: "daily" or "monthly" or "weekly"`

  - `"daily"`

  - `"monthly"`

  - `"weekly"`

- `resolved_at: string`

- `resolved_by: object { deleted, email_address, name, 2 more }  or object { scoped_api_key_id, type }`

  A user within the organization. `name` and `email_address` are
  null when the underlying account is unavailable or has been deleted;
  `deleted` is true only for deleted accounts.

  - `UserActor object { deleted, email_address, name, 2 more }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `deleted: boolean`

    - `email_address: string`

    - `name: string`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

  - `ScopedAPIKeyActor object { scoped_api_key_id, type }`

    A scoped Admin API key acting on behalf of the organization.

    - `scoped_api_key_id: string`

    - `type: "scoped_api_key_actor"`

      - `"scoped_api_key_actor"`

- `spend_limit: SpendLimit`

  - `id: string`

  - `amount: string`

  - `created_at: string`

  - `currency: string`

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `scope: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

    - `User object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `SeatTier object { seat_tier, type }`

      - `seat_tier: string`

      - `type: "seat_tier"`

        - `"seat_tier"`

    - `RbacGroup object { rbac_group_id, type }`

      - `rbac_group_id: string`

      - `type: "rbac_group"`

        - `"rbac_group"`

    - `OrganizationService object { service, type }`

      - `service: string`

      - `type: "organization_service"`

        - `"organization_service"`

    - `Organization object { type }`

      - `type: "organization"`

        - `"organization"`

  - `type: "spend_limit"`

    - `"spend_limit"`

  - `updated_at: string`

- `spend_summary: SpendSummary`

  Per-member effective-limit report row (GET /spend_limits/effective).

  - `actor: object { deleted, email_address, name, 2 more }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `deleted: boolean`

    - `email_address: string`

    - `name: string`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

  - `amount: string`

  - `currency: string`

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `period_to_date_spend: string`

  - `scope: object { type, user_id }`

    - `type: "user"`

      - `"user"`

    - `user_id: string`

  - `source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

    - `User object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `SeatTier object { seat_tier, type }`

      - `seat_tier: string`

      - `type: "seat_tier"`

        - `"seat_tier"`

    - `RbacGroup object { rbac_group_id, type }`

      - `rbac_group_id: string`

      - `type: "rbac_group"`

        - `"rbac_group"`

    - `OrganizationService object { service, type }`

      - `service: string`

      - `type: "organization_service"`

        - `"organization_service"`

    - `Organization object { type }`

      - `type: "organization"`

        - `"organization"`

  - `spend_limit_id: string`

- `status: "approved" or "denied" or "pending"`

  - `"approved"`

  - `"denied"`

  - `"pending"`

- `type: "spend_limit_increase_request"`

  - `"spend_limit_increase_request"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/approve \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "amount": "50000",
          "period": "monthly"
        }'
```

#### Response

```json
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "monthly",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  },
  "spend_limit": {
    "id": "id",
    "amount": "50000",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "USD",
    "period": "monthly",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    },
    "type": "spend_limit",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_id"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "monthly",
    "period_to_date_spend": "period_to_date_spend",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    },
    "source": {
      "type": "user",
      "user_id": "user_id"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

## Deny Spend Limit Increase Request

**post** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny`

Deny a pending spend limit increase request.

Idempotent on `denied`; denying an already-`approved` request returns
400. Anthropic emails the requester unless `suppress_notification` is set.

### Path Parameters

- `spend_limit_increase_request_id: string`

  ID of the spend limit increase request.

### Body Parameters

- `suppress_notification: optional boolean`

### Returns

- `SpendLimitIncreaseRequest object { id, actor, created_at, 6 more }`

  - `id: string`

  - `actor: object { deleted, email_address, name, 2 more }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `deleted: boolean`

    - `email_address: string`

    - `name: string`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

  - `created_at: string`

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `resolved_at: string`

  - `resolved_by: object { deleted, email_address, name, 2 more }  or object { scoped_api_key_id, type }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `UserActor object { deleted, email_address, name, 2 more }`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `deleted: boolean`

      - `email_address: string`

      - `name: string`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

    - `ScopedAPIKeyActor object { scoped_api_key_id, type }`

      A scoped Admin API key acting on behalf of the organization.

      - `scoped_api_key_id: string`

      - `type: "scoped_api_key_actor"`

        - `"scoped_api_key_actor"`

  - `spend_summary: SpendSummary`

    Per-member effective-limit report row (GET /spend_limits/effective).

    - `actor: object { deleted, email_address, name, 2 more }`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `deleted: boolean`

      - `email_address: string`

      - `name: string`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

    - `amount: string`

    - `currency: string`

    - `period: "daily" or "monthly" or "weekly"`

      - `"daily"`

      - `"monthly"`

      - `"weekly"`

    - `period_to_date_spend: string`

    - `scope: object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

      - `User object { type, user_id }`

        - `type: "user"`

          - `"user"`

        - `user_id: string`

      - `SeatTier object { seat_tier, type }`

        - `seat_tier: string`

        - `type: "seat_tier"`

          - `"seat_tier"`

      - `RbacGroup object { rbac_group_id, type }`

        - `rbac_group_id: string`

        - `type: "rbac_group"`

          - `"rbac_group"`

      - `OrganizationService object { service, type }`

        - `service: string`

        - `type: "organization_service"`

          - `"organization_service"`

      - `Organization object { type }`

        - `type: "organization"`

          - `"organization"`

    - `spend_limit_id: string`

  - `status: "approved" or "denied" or "pending"`

    - `"approved"`

    - `"denied"`

    - `"pending"`

  - `type: "spend_limit_increase_request"`

    - `"spend_limit_increase_request"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/deny \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

#### Response

```json
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "monthly",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_id"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "monthly",
    "period_to_date_spend": "period_to_date_spend",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    },
    "source": {
      "type": "user",
      "user_id": "user_id"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

## Domain Types

### Spend Limit Increase Request

- `SpendLimitIncreaseRequest object { id, actor, created_at, 6 more }`

  - `id: string`

  - `actor: object { deleted, email_address, name, 2 more }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `deleted: boolean`

    - `email_address: string`

    - `name: string`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

  - `created_at: string`

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `resolved_at: string`

  - `resolved_by: object { deleted, email_address, name, 2 more }  or object { scoped_api_key_id, type }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `UserActor object { deleted, email_address, name, 2 more }`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `deleted: boolean`

      - `email_address: string`

      - `name: string`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

    - `ScopedAPIKeyActor object { scoped_api_key_id, type }`

      A scoped Admin API key acting on behalf of the organization.

      - `scoped_api_key_id: string`

      - `type: "scoped_api_key_actor"`

        - `"scoped_api_key_actor"`

  - `spend_summary: SpendSummary`

    Per-member effective-limit report row (GET /spend_limits/effective).

    - `actor: object { deleted, email_address, name, 2 more }`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `deleted: boolean`

      - `email_address: string`

      - `name: string`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

    - `amount: string`

    - `currency: string`

    - `period: "daily" or "monthly" or "weekly"`

      - `"daily"`

      - `"monthly"`

      - `"weekly"`

    - `period_to_date_spend: string`

    - `scope: object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

      - `User object { type, user_id }`

        - `type: "user"`

          - `"user"`

        - `user_id: string`

      - `SeatTier object { seat_tier, type }`

        - `seat_tier: string`

        - `type: "seat_tier"`

          - `"seat_tier"`

      - `RbacGroup object { rbac_group_id, type }`

        - `rbac_group_id: string`

        - `type: "rbac_group"`

          - `"rbac_group"`

      - `OrganizationService object { service, type }`

        - `service: string`

        - `type: "organization_service"`

          - `"organization_service"`

      - `Organization object { type }`

        - `type: "organization"`

          - `"organization"`

    - `spend_limit_id: string`

  - `status: "approved" or "denied" or "pending"`

    - `"approved"`

    - `"denied"`

    - `"pending"`

  - `type: "spend_limit_increase_request"`

    - `"spend_limit_increase_request"`

### Increase Request Approve Response

- `IncreaseRequestApproveResponse object { id, actor, created_at, 7 more }`

  - `id: string`

  - `actor: object { deleted, email_address, name, 2 more }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `deleted: boolean`

    - `email_address: string`

    - `name: string`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

  - `created_at: string`

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `resolved_at: string`

  - `resolved_by: object { deleted, email_address, name, 2 more }  or object { scoped_api_key_id, type }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `UserActor object { deleted, email_address, name, 2 more }`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `deleted: boolean`

      - `email_address: string`

      - `name: string`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

    - `ScopedAPIKeyActor object { scoped_api_key_id, type }`

      A scoped Admin API key acting on behalf of the organization.

      - `scoped_api_key_id: string`

      - `type: "scoped_api_key_actor"`

        - `"scoped_api_key_actor"`

  - `spend_limit: SpendLimit`

    - `id: string`

    - `amount: string`

    - `created_at: string`

    - `currency: string`

    - `period: "daily" or "monthly" or "weekly"`

      - `"daily"`

      - `"monthly"`

      - `"weekly"`

    - `scope: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

      - `User object { type, user_id }`

        - `type: "user"`

          - `"user"`

        - `user_id: string`

      - `SeatTier object { seat_tier, type }`

        - `seat_tier: string`

        - `type: "seat_tier"`

          - `"seat_tier"`

      - `RbacGroup object { rbac_group_id, type }`

        - `rbac_group_id: string`

        - `type: "rbac_group"`

          - `"rbac_group"`

      - `OrganizationService object { service, type }`

        - `service: string`

        - `type: "organization_service"`

          - `"organization_service"`

      - `Organization object { type }`

        - `type: "organization"`

          - `"organization"`

    - `type: "spend_limit"`

      - `"spend_limit"`

    - `updated_at: string`

  - `spend_summary: SpendSummary`

    Per-member effective-limit report row (GET /spend_limits/effective).

    - `actor: object { deleted, email_address, name, 2 more }`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `deleted: boolean`

      - `email_address: string`

      - `name: string`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

    - `amount: string`

    - `currency: string`

    - `period: "daily" or "monthly" or "weekly"`

      - `"daily"`

      - `"monthly"`

      - `"weekly"`

    - `period_to_date_spend: string`

    - `scope: object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

      - `User object { type, user_id }`

        - `type: "user"`

          - `"user"`

        - `user_id: string`

      - `SeatTier object { seat_tier, type }`

        - `seat_tier: string`

        - `type: "seat_tier"`

          - `"seat_tier"`

      - `RbacGroup object { rbac_group_id, type }`

        - `rbac_group_id: string`

        - `type: "rbac_group"`

          - `"rbac_group"`

      - `OrganizationService object { service, type }`

        - `service: string`

        - `type: "organization_service"`

          - `"organization_service"`

      - `Organization object { type }`

        - `type: "organization"`

          - `"organization"`

    - `spend_limit_id: string`

  - `status: "approved" or "denied" or "pending"`

    - `"approved"`

    - `"denied"`

    - `"pending"`

  - `type: "spend_limit_increase_request"`

    - `"spend_limit_increase_request"`

# Rate Limits

## List Organization Rate Limits

**get** `/v1/organizations/rate_limits`

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

### Query Parameters

- `group_type: optional "batch" or "files" or "model_group" or 3 more`

  Filter by group type.

  - `"batch"`

  - `"files"`

  - `"model_group"`

  - `"skills"`

  - `"token_count"`

  - `"web_search"`

- `model: optional string`

  Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Returns

- `data: array of object { group_type, limits, models, type }`

  Rate-limit entries for the organization, one per group.

  - `group_type: "batch" or "files" or "model_group" or 3 more`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `"batch"`

    - `"files"`

    - `"model_group"`

    - `"skills"`

    - `"token_count"`

    - `"web_search"`

  - `limits: array of object { type, value }`

    The limiter values that apply to this group.

    - `type: string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `value: number`

      The configured limit value for this limiter type.

  - `models: array of string`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `type: "rate_limit"`

    Object type. Always `rate_limit` for organization rate-limit entries.

    - `"rate_limit"`

- `next_page: string`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```http
curl https://api.anthropic.com/v1/organizations/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "group_type": "batch",
      "limits": [
        {
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "type": "rate_limit"
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Rate Limit List Response

- `RateLimitListResponse object { data, next_page }`

  - `data: array of object { group_type, limits, models, type }`

    Rate-limit entries for the organization, one per group.

    - `group_type: "batch" or "files" or "model_group" or 3 more`

      The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

      - `"batch"`

      - `"files"`

      - `"model_group"`

      - `"skills"`

      - `"token_count"`

      - `"web_search"`

    - `limits: array of object { type, value }`

      The limiter values that apply to this group.

      - `type: string`

        The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

      - `value: number`

        The configured limit value for this limiter type.

    - `models: array of string`

      Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

    - `type: "rate_limit"`

      Object type. Always `rate_limit` for organization rate-limit entries.

      - `"rate_limit"`

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

# Service Accounts

## Create Service Account

**post** `/v1/organizations/service_accounts`

Create a service account.

A service account is a named workload identity that federation rules
target. `organization_role` is `developer` (default) or `admin`; a rule
may only be created or retargeted to grant `org:admin` scope when the
target's `organization_role` is `admin`. Requires an OAuth bearer (user
or WIF-minted service account token) or a Console session; Admin API
keys are not accepted. Creating an `admin`-role service account requires
an interactive credential (a user OAuth token or a Console session) — a
workload may only create `developer`-role service accounts.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `name: string`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

- `description: optional string`

  Optional free-text description.

- `organization_role: optional "admin" or "developer"`

  Org-level role. Defaults to `developer`.

  - `"admin"`

  - `"developer"`

### Returns

- `ServiceAccount object { id, archived_at, archived_by_actor_id, 8 more }`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string`

    If set, this service account is archived.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

    - `"service_account"`

  - `updated_at: string`

    When this service account was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

### Example

```http
curl https://api.anthropic.com/v1/organizations/service_accounts \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "name": "ci-deploy-bot"
        }'
```

#### Response

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## Get Service Account

**get** `/v1/organizations/service_accounts/{service_account_id}`

Retrieve a service account by its ID (`svac_...`).

### Path Parameters

- `service_account_id: string`

  ID of the service account.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `ServiceAccount object { id, archived_at, archived_by_actor_id, 8 more }`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string`

    If set, this service account is archived.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

    - `"service_account"`

  - `updated_at: string`

    When this service account was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

### Example

```http
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## List Service Accounts

**get** `/v1/organizations/service_accounts`

List service accounts in the caller's organization.

Results are ordered by creation time, newest first. Use `limit` and the
`next_page` cursor to paginate; set `include_archived=true` to include
archived service accounts.

### Query Parameters

- `include_archived: optional boolean`

  Include archived resources. Defaults to false.

- `limit: optional number`

  Number of results per page.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `data: array of ServiceAccount`

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string`

    If set, this service account is archived.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

    - `"service_account"`

  - `updated_at: string`

    When this service account was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

- `next_page: string`

  Opaque cursor for the next page, or null if no more results.

### Example

```http
curl https://api.anthropic.com/v1/organizations/service_accounts \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "name": "ci-deploy-bot",
      "organization_role": "admin",
      "type": "service_account",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```

## Update Service Account

**post** `/v1/organizations/service_accounts/{service_account_id}`

Update a service account.

Only `description` and `organization_role` are mutable; `name` cannot be
changed. Archived service accounts cannot be updated; this returns 400.
Setting `organization_role` to `admin` (even when unchanged) requires an
interactive credential (a user OAuth token or a Console session). Admin
API keys are not accepted.

### Path Parameters

- `service_account_id: string`

  ID of the service account to update.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `description: optional string`

  Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

- `organization_role: optional "admin" or "developer"`

  Replaces the org-level role. Omit or send `null` to leave unchanged.

  - `"admin"`

  - `"developer"`

### Returns

- `ServiceAccount object { id, archived_at, archived_by_actor_id, 8 more }`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string`

    If set, this service account is archived.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

    - `"service_account"`

  - `updated_at: string`

    When this service account was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

### Example

```http
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

#### Response

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## Archive Service Account

**post** `/v1/organizations/service_accounts/{service_account_id}/archive`

Archive a service account.

Idempotent; re-archiving returns the service account with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still targets this service account, same as issuer archival; archive
those rules first or change their target to another service account.

Requires an OAuth bearer or Console session; Admin API keys are not
accepted.

### Path Parameters

- `service_account_id: string`

  ID of the service account to archive.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `ServiceAccount object { id, archived_at, archived_by_actor_id, 8 more }`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string`

    If set, this service account is archived.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

    - `"service_account"`

  - `updated_at: string`

    When this service account was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

### Example

```http
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## Domain Types

### Service Account

- `ServiceAccount object { id, archived_at, archived_by_actor_id, 8 more }`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string`

    If set, this service account is archived.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

    - `"service_account"`

  - `updated_at: string`

    When this service account was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

# Workspaces

## Add Workspace To Service Account

**post** `/v1/organizations/service_accounts/{service_account_id}/workspaces`

Add a service account to a workspace with the given `workspace_role`.

Mirror of `POST /workspaces/{workspace_id}/service_accounts`, addressed
from the service-account side; both create the same membership. If the
service account is already an explicit member of the workspace, its
`workspace_role` is replaced with the value supplied here. Archived
workspaces return 400. Archived service accounts cannot be added and are
rejected. Requires an OAuth bearer or Console session; Admin API keys
are not accepted.

### Path Parameters

- `service_account_id: string`

  ID of the service account.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `workspace_id: string`

  Tagged workspace ID to add the service account to.

- `workspace_role: "workspace_admin" or "workspace_developer" or "workspace_restricted_developer" or "workspace_user"`

  Role to assign to the service account in this workspace.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

### Returns

- `created_by_actor_id: string`

  Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

- `implicit: boolean`

  True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

- `service_account_id: string`

  Tagged service account ID (`svac_...`).

- `type: "service_account_workspace_member"`

  - `"service_account_workspace_member"`

- `workspace_id: string`

  Tagged workspace ID (`wrkspc_...`).

- `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

  Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

  - `"workspace_admin"`

  - `"workspace_billing"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "workspace_id": "workspace_id",
          "workspace_role": "workspace_admin"
        }'
```

#### Response

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

## List Workspaces For Service Account

**get** `/v1/organizations/service_accounts/{service_account_id}/workspaces`

List the workspaces a service account is a member of.

Each entry includes the service account's `workspace_role` in that
workspace. Use `limit` and the `next_page` cursor to paginate. When the
service account has no explicit default-workspace membership, the
implicit (`implicit: true`) membership is returned as the first entry on
the first page; with `limit=1` the first page may return up to 2 entries
(the implicit entry plus one explicit membership) so a pagination cursor
can be derived. Memberships are returned only while
the service account is active; an archived service account returns an
empty list.

### Path Parameters

- `service_account_id: string`

  ID of the service account.

### Query Parameters

- `limit: optional number`

  Number of results per page.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `data: array of object { created_by_actor_id, implicit, service_account_id, 3 more }`

  - `created_by_actor_id: string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    - `"service_account_workspace_member"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

- `next_page: string`

  Opaque cursor for the next page, or null if no more results.

### Example

```http
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
    }
  ],
  "next_page": "next_page"
}
```

## Remove Workspace From Service Account

**delete** `/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}`

Remove a service account from a workspace.

Mirror of `DELETE /workspaces/{workspace_id}/service_accounts/{service_account_id}`,
addressed from the service-account side. Removal is idempotent (returns
200 even if the membership was already removed). A DELETE against the
implicit default-workspace membership returns 200 but is a no-op and the
membership persists; deleting an explicit default-workspace row reverts
to the implicit `workspace_user` membership. Archived workspaces return
400. Requires an OAuth bearer or Console session; Admin API keys are not
accepted.

### Path Parameters

- `service_account_id: string`

  ID of the service account.

- `workspace_id: string`

  ID of the workspace.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `service_account_id: string`

  Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

- `type: "service_account_workspace_member_deleted"`

  - `"service_account_workspace_member_deleted"`

- `workspace_id: string`

  Tagged workspace ID (`wrkspc_...`) named in the delete request.

### Example

```http
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces/$WORKSPACE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
}
```

## Domain Types

### Workspace Create Response

- `WorkspaceCreateResponse object { created_by_actor_id, implicit, service_account_id, 3 more }`

  - `created_by_actor_id: string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    - `"service_account_workspace_member"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

### Workspace List Response

- `WorkspaceListResponse object { created_by_actor_id, implicit, service_account_id, 3 more }`

  - `created_by_actor_id: string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace_user and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    - `"service_account_workspace_member"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: "workspace_admin" or "workspace_billing" or "workspace_developer" or 2 more`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

### Workspace Delete Response

- `WorkspaceDeleteResponse object { service_account_id, type, workspace_id }`

  - `service_account_id: string`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `type: "service_account_workspace_member_deleted"`

    - `"service_account_workspace_member_deleted"`

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

# Federation Issuers

## Create Federation Issuer

**post** `/v1/organizations/federation_issuers`

Register an OIDC issuer that Anthropic will trust for workload identity
federation in your organization.

The `jwks` field controls how the issuer's signing keys are obtained and
takes one of three shapes selected by `type`: `discovery` (resolve keys
through OIDC discovery), `explicit_url` (fetch keys from a fixed JWKS
URL), or `inline` (provide a static key set). When `jwks.type` is
`discovery` and no `discovery_base` is set, the issuer URL must be
publicly reachable over HTTPS so Anthropic can fetch the discovery
document; for `explicit_url` and `inline` modes the issuer URL is only
matched as the JWT's `iss` claim and is not fetched.

Requires an OAuth bearer or Console session; Admin API keys are not
accepted.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `issuer_url: string`

  The `iss` claim value to match against.

- `name: string`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

- `check_jti: optional boolean`

  Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Defaults to true. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

- `jwks: optional object { type, ca_cert_pem, discovery_base }  or object { type, url, ca_cert_pem }  or object { keys, type }`

  How signing keys are obtained. Defaults to OIDC discovery.

  - `Discovery object { type, ca_cert_pem, discovery_base }`

    JWKS via the issuer's OIDC discovery document.

    - `type: "discovery"`

      - `"discovery"`

    - `ca_cert_pem: optional string`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

    - `discovery_base: optional string`

      Set when the discovery URL differs from `issuer_url`.

  - `ExplicitURL object { type, url, ca_cert_pem }`

    JWKS fetched from a fixed endpoint.

    - `type: "explicit_url"`

      - `"explicit_url"`

    - `url: string`

      JWKS endpoint.

    - `ca_cert_pem: optional string`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

  - `Inline object { keys, type }`

    JWKS supplied directly; no network fetch.

    - `keys: array of map[unknown]`

      Inline JWK objects.

    - `type: "inline"`

      - `"inline"`

- `max_jwt_lifetime_seconds: optional number`

  Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Defaults to 3600 (1h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

### Returns

- `FederationIssuer object { id, archived_at, archived_by_actor_id, 12 more }`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string`

    If set, all rules referencing this issuer reject token exchange.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: object { type, ca_cert_pem, discovery_base }  or object { type, url, ca_cert_pem }  or object { keys, type }`

    How signing keys are obtained for signature verification.

    - `Discovery object { type, ca_cert_pem, discovery_base }`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

        - `"discovery"`

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      - `discovery_base: optional string`

        Set when the discovery URL differs from `issuer_url`.

    - `ExplicitURL object { type, url, ca_cert_pem }`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

        - `"explicit_url"`

      - `url: string`

        JWKS endpoint.

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

    - `Inline object { keys, type }`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

      - `type: "inline"`

        - `"inline"`

  - `jwks_polling_disabled_at: string`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: object { consecutive_failures, last_fetched_at, next_poll_at }`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string`

      When the last successful fetch completed.

    - `next_poll_at: string`

      When the next fetch is scheduled. Null if paused.

  - `type: "federation_issuer"`

    - `"federation_issuer"`

  - `updated_at: string`

    When this issuer was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_issuers \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "issuer_url": "x",
          "name": "x"
        }'
```

#### Response

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## Get Federation Issuer

**get** `/v1/organizations/federation_issuers/{federation_issuer_id}`

Retrieve a federation issuer by its ID (`fdis_...`).

### Path Parameters

- `federation_issuer_id: string`

  ID of the federation issuer.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `FederationIssuer object { id, archived_at, archived_by_actor_id, 12 more }`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string`

    If set, all rules referencing this issuer reject token exchange.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: object { type, ca_cert_pem, discovery_base }  or object { type, url, ca_cert_pem }  or object { keys, type }`

    How signing keys are obtained for signature verification.

    - `Discovery object { type, ca_cert_pem, discovery_base }`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

        - `"discovery"`

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      - `discovery_base: optional string`

        Set when the discovery URL differs from `issuer_url`.

    - `ExplicitURL object { type, url, ca_cert_pem }`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

        - `"explicit_url"`

      - `url: string`

        JWKS endpoint.

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

    - `Inline object { keys, type }`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

      - `type: "inline"`

        - `"inline"`

  - `jwks_polling_disabled_at: string`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: object { consecutive_failures, last_fetched_at, next_poll_at }`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string`

      When the last successful fetch completed.

    - `next_poll_at: string`

      When the next fetch is scheduled. Null if paused.

  - `type: "federation_issuer"`

    - `"federation_issuer"`

  - `updated_at: string`

    When this issuer was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## List Federation Issuers

**get** `/v1/organizations/federation_issuers`

List federation issuers in your organization.

Archived issuers are excluded unless `include_archived=true`.

### Query Parameters

- `include_archived: optional boolean`

  Include archived resources. Defaults to false.

- `limit: optional number`

  Number of results per page.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `data: array of FederationIssuer`

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string`

    If set, all rules referencing this issuer reject token exchange.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: object { type, ca_cert_pem, discovery_base }  or object { type, url, ca_cert_pem }  or object { keys, type }`

    How signing keys are obtained for signature verification.

    - `Discovery object { type, ca_cert_pem, discovery_base }`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

        - `"discovery"`

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      - `discovery_base: optional string`

        Set when the discovery URL differs from `issuer_url`.

    - `ExplicitURL object { type, url, ca_cert_pem }`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

        - `"explicit_url"`

      - `url: string`

        JWKS endpoint.

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

    - `Inline object { keys, type }`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

      - `type: "inline"`

        - `"inline"`

  - `jwks_polling_disabled_at: string`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: object { consecutive_failures, last_fetched_at, next_poll_at }`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string`

      When the last successful fetch completed.

    - `next_poll_at: string`

      When the next fetch is scheduled. Null if paused.

  - `type: "federation_issuer"`

    - `"federation_issuer"`

  - `updated_at: string`

    When this issuer was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

- `next_page: string`

  Opaque cursor for the next page, or null if no more results.

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_issuers \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "check_jti": true,
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "issuer_url": "https://token.actions.githubusercontent.com",
      "jwks": {
        "type": "discovery",
        "ca_cert_pem": "ca_cert_pem",
        "discovery_base": "discovery_base"
      },
      "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
      "max_jwt_lifetime_seconds": 0,
      "name": "github-actions",
      "poll_status": {
        "consecutive_failures": 0,
        "last_fetched_at": "2019-12-27T18:11:19.117Z",
        "next_poll_at": "2019-12-27T18:11:19.117Z"
      },
      "type": "federation_issuer",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```

## Update Federation Issuer

**post** `/v1/organizations/federation_issuers/{federation_issuer_id}`

Partially update a federation issuer.

Setting `jwks` replaces the full JWKS shape at once. Archived issuers
cannot be updated; this returns 400. Create a new issuer instead.

Updating an issuer that backs a rule with a scope outside
`workspace:developer` or `workspace:inference` requires a Console
session. Requires an OAuth bearer or Console session; Admin API keys
are not accepted.

### Path Parameters

- `federation_issuer_id: string`

  ID of the federation issuer to update.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `check_jti: optional boolean`

  Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

- `issuer_url: optional string`

  Replaces the `iss` claim value to match against. For discovery-mode issuers without a `discovery_base`, this is also the URL Anthropic fetches the OIDC discovery document and signing keys from, so changing it repoints the JWKS source. Changing the issuer URL to a well-known shared platform is rejected while any live rule under this issuer would not constrain tenant identity.

- `jwks: optional object { type, ca_cert_pem, discovery_base }  or object { type, url, ca_cert_pem }  or object { keys, type }`

  Replaces the entire JWKS configuration.

  - `Discovery object { type, ca_cert_pem, discovery_base }`

    JWKS via the issuer's OIDC discovery document.

    - `type: "discovery"`

      - `"discovery"`

    - `ca_cert_pem: optional string`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

    - `discovery_base: optional string`

      Set when the discovery URL differs from `issuer_url`.

  - `ExplicitURL object { type, url, ca_cert_pem }`

    JWKS fetched from a fixed endpoint.

    - `type: "explicit_url"`

      - `"explicit_url"`

    - `url: string`

      JWKS endpoint.

    - `ca_cert_pem: optional string`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

  - `Inline object { keys, type }`

    JWKS supplied directly; no network fetch.

    - `keys: array of map[unknown]`

      Inline JWK objects.

    - `type: "inline"`

      - `"inline"`

- `jwks_polling_disabled: optional boolean`

  Only `false` is accepted, to re-enable polling after the system pauses it. Polling is paused automatically; sending `true` is rejected.

- `max_jwt_lifetime_seconds: optional number`

  Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

- `name: optional string`

  Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

### Returns

- `FederationIssuer object { id, archived_at, archived_by_actor_id, 12 more }`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string`

    If set, all rules referencing this issuer reject token exchange.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: object { type, ca_cert_pem, discovery_base }  or object { type, url, ca_cert_pem }  or object { keys, type }`

    How signing keys are obtained for signature verification.

    - `Discovery object { type, ca_cert_pem, discovery_base }`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

        - `"discovery"`

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      - `discovery_base: optional string`

        Set when the discovery URL differs from `issuer_url`.

    - `ExplicitURL object { type, url, ca_cert_pem }`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

        - `"explicit_url"`

      - `url: string`

        JWKS endpoint.

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

    - `Inline object { keys, type }`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

      - `type: "inline"`

        - `"inline"`

  - `jwks_polling_disabled_at: string`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: object { consecutive_failures, last_fetched_at, next_poll_at }`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string`

      When the last successful fetch completed.

    - `next_poll_at: string`

      When the next fetch is scheduled. Null if paused.

  - `type: "federation_issuer"`

    - `"federation_issuer"`

  - `updated_at: string`

    When this issuer was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

#### Response

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## Archive Federation Issuer

**post** `/v1/organizations/federation_issuers/{federation_issuer_id}/archive`

Archive a federation issuer.

Idempotent; re-archiving returns the issuer with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still references the issuer; archive those rules first (a rule's
issuer cannot be changed), or recreate them against another issuer.

Requires an OAuth bearer or Console session; Admin API keys are not
accepted.

### Path Parameters

- `federation_issuer_id: string`

  ID of the federation issuer to archive.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `FederationIssuer object { id, archived_at, archived_by_actor_id, 12 more }`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string`

    If set, all rules referencing this issuer reject token exchange.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: object { type, ca_cert_pem, discovery_base }  or object { type, url, ca_cert_pem }  or object { keys, type }`

    How signing keys are obtained for signature verification.

    - `Discovery object { type, ca_cert_pem, discovery_base }`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

        - `"discovery"`

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      - `discovery_base: optional string`

        Set when the discovery URL differs from `issuer_url`.

    - `ExplicitURL object { type, url, ca_cert_pem }`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

        - `"explicit_url"`

      - `url: string`

        JWKS endpoint.

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

    - `Inline object { keys, type }`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

      - `type: "inline"`

        - `"inline"`

  - `jwks_polling_disabled_at: string`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: object { consecutive_failures, last_fetched_at, next_poll_at }`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string`

      When the last successful fetch completed.

    - `next_poll_at: string`

      When the next fetch is scheduled. Null if paused.

  - `type: "federation_issuer"`

    - `"federation_issuer"`

  - `updated_at: string`

    When this issuer was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## Domain Types

### Federation Issuer

- `FederationIssuer object { id, archived_at, archived_by_actor_id, 12 more }`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string`

    If set, all rules referencing this issuer reject token exchange.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: object { type, ca_cert_pem, discovery_base }  or object { type, url, ca_cert_pem }  or object { keys, type }`

    How signing keys are obtained for signature verification.

    - `Discovery object { type, ca_cert_pem, discovery_base }`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

        - `"discovery"`

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      - `discovery_base: optional string`

        Set when the discovery URL differs from `issuer_url`.

    - `ExplicitURL object { type, url, ca_cert_pem }`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

        - `"explicit_url"`

      - `url: string`

        JWKS endpoint.

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

    - `Inline object { keys, type }`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

      - `type: "inline"`

        - `"inline"`

  - `jwks_polling_disabled_at: string`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: object { consecutive_failures, last_fetched_at, next_poll_at }`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string`

      When the last successful fetch completed.

    - `next_poll_at: string`

      When the next fetch is scheduled. Null if paused.

  - `type: "federation_issuer"`

    - `"federation_issuer"`

  - `updated_at: string`

    When this issuer was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

# Federation Rules

## Create Federation Rule

**post** `/v1/organizations/federation_rules`

Create a federation rule owned by your organization.

The referenced issuer and the target service account must already exist
in the same organization; invalid references are rejected with a 400
error. The workspace reference is validated. Membership is not checked
at rule creation: token exchange resolves a single enabled workspace per
call and is rejected unless the target service account is a member of
that workspace (it is implicitly a member of the default workspace).
Rules on well-known shared issuers (GitHub Actions, GitLab, Buildkite,
Terraform Cloud, Google) must constrain tenant identity via an
identity-bearing claim, a tenant-pinning subject prefix (such as
`repo:YOUR_ORG/...`), or a CEL condition referencing one of those
identity claims (e.g. `claims.repository_owner`). OAuth callers may only
manage rules whose `oauth_scope` is `workspace:developer` or
`workspace:inference`; other scopes require a Console session. Admin API
keys are not accepted.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `issuer_id: string`

  Tagged ID of the federation issuer.

- `match: object { audience, claims, condition, subject_prefix }`

  Conditions the verified JWT must satisfy for this rule to apply. At least one of `subject_prefix` (other than a wildcard-only value like `*`), `claims`, or `condition` is required; `audience` alone is not sufficient.

  - `audience: optional string`

    Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

  - `claims: optional map[string]`

    Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

  - `condition: optional string`

    CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

  - `subject_prefix: optional string`

    Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

- `name: string`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

- `oauth_scope: string`

  Space-separated OAuth scopes. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

- `target: object { service_account_id, type, service_account_name }`

  Identity that tokens minted via this rule act as. Currently always a `service_account` target.

  - `service_account_id: string`

    Tagged ID of the service account to mint tokens for.

  - `type: "service_account"`

    - `"service_account"`

  - `service_account_name: optional string`

    Service account's display name at read time. Ignored on writes.

- `applies_to_all_workspaces: optional boolean`

  When true, enable this rule for every workspace in the org (including workspaces created later).

- `attributes: optional map[string]`

  CEL expressions `{name: expr}` extracting named values from claims. Not yet supported; any non-empty value is rejected with 400.

- `description: optional string`

  Optional free-text description.

- `token_lifetime_seconds: optional number`

  Lifetime in seconds for access tokens minted via this rule (60-86400). Defaults to 3600 (1h). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

- `workspace_id: optional string`

  Tagged ID of the workspace to enable this rule for. Required unless `applies_to_all_workspaces` is true. Additional workspaces can be added via the `/federation_rules/{federation_rule_id}/workspaces` sub-resource.

### Returns

- `FederationRule object { id, applies_to_all_workspaces, archived_at, 17 more }`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string`

    If set, this rule is archived and rejects token exchange.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string`

    Issuer's display name at read time.

  - `match: object { audience, claims, condition, subject_prefix }`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

    - `claims: optional map[string]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

    - `subject_prefix: optional string`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: object { service_account_id, type, service_account_name }`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

      - `"service_account"`

    - `service_account_name: optional string`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    - `"federation_rule"`

  - `updated_at: string`

    When this rule was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_rules \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "issuer_id": "issuer_id",
          "match": {},
          "name": "x",
          "oauth_scope": "x",
          "target": {
            "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
            "type": "service_account"
          }
        }'
```

#### Response

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

## Get Federation Rule

**get** `/v1/organizations/federation_rules/{federation_rule_id}`

Retrieve a federation rule by its ID (`fdrl_...`).

### Path Parameters

- `federation_rule_id: string`

  ID of the federation rule.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `FederationRule object { id, applies_to_all_workspaces, archived_at, 17 more }`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string`

    If set, this rule is archived and rejects token exchange.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string`

    Issuer's display name at read time.

  - `match: object { audience, claims, condition, subject_prefix }`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

    - `claims: optional map[string]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

    - `subject_prefix: optional string`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: object { service_account_id, type, service_account_name }`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

      - `"service_account"`

    - `service_account_name: optional string`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    - `"federation_rule"`

  - `updated_at: string`

    When this rule was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

## List Federation Rules

**get** `/v1/organizations/federation_rules`

List federation rules in your organization.

Optionally filter by issuer with `issuer_id`. Archived rules are excluded
unless `include_archived=true`.

### Query Parameters

- `include_archived: optional boolean`

  Include archived resources. Defaults to false.

- `issuer_id: optional string`

  Filter to rules referencing this federation issuer.

- `limit: optional number`

  Number of results per page.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `data: array of FederationRule`

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string`

    If set, this rule is archived and rejects token exchange.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string`

    Issuer's display name at read time.

  - `match: object { audience, claims, condition, subject_prefix }`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

    - `claims: optional map[string]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

    - `subject_prefix: optional string`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: object { service_account_id, type, service_account_name }`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

      - `"service_account"`

    - `service_account_name: optional string`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    - `"federation_rule"`

  - `updated_at: string`

    When this rule was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

- `next_page: string`

  Opaque cursor for the next page, or null if no more results.

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_rules \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
      "applies_to_all_workspaces": true,
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "attributes": {
        "foo": "string"
      },
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "issuer_id": "issuer_id",
      "issuer_name": "issuer_name",
      "match": {
        "audience": "audience",
        "claims": {
          "foo": "string"
        },
        "condition": "condition",
        "subject_prefix": "subject_prefix"
      },
      "name": "prod-deploy-pipeline",
      "oauth_scope": "oauth_scope",
      "target": {
        "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
        "type": "service_account",
        "service_account_name": "service_account_name"
      },
      "token_lifetime_seconds": 0,
      "type": "federation_rule",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id",
      "workspace_id": "workspace_id",
      "workspace_ids": [
        "string"
      ]
    }
  ],
  "next_page": "next_page"
}
```

## Update Federation Rule

**post** `/v1/organizations/federation_rules/{federation_rule_id}`

Partially update a federation rule.

`issuer_id` is immutable. `match` and `target` are replaced as whole
objects when set. Referenced service accounts and workspaces must exist
in your organization; invalid references are rejected with a 400 error.
Archived rules cannot be updated; this returns 400. Create a new rule
instead. Rules on well-known shared issuers (GitHub Actions, GitLab,
Buildkite, Terraform Cloud, Google) must constrain tenant identity via
an identity-bearing claim, a tenant-pinning subject prefix (such as
`repo:YOUR_ORG/...`), or a CEL condition referencing one of those
identity claims (e.g. `claims.repository_owner`). On these issuers the
requirement is re-checked on every update; if an existing rule's stored
match does not yet constrain tenant identity, any update (even a rename
or description change) must also supply a conforming `match` in the same
request. OAuth callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session. Admin API keys are not accepted.

### Path Parameters

- `federation_rule_id: string`

  ID of the federation rule to update.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `applies_to_all_workspaces: optional boolean`

  When true, enables this rule for every workspace in the org (including workspaces created later). Setting `false` is rejected with 400 if no workspace would remain enabled; a rule with only a legacy `workspace_id` binding continues to mint.

- `attributes: optional map[string]`

  Replaces the CEL expressions `{name: expr}` extracting named values from claims. Send null to clear them. Not yet supported; any non-empty value is rejected with 400.

- `description: optional string`

  Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

- `match: optional object { audience, claims, condition, subject_prefix }`

  Does the incoming JWT qualify?

  All populated fields must pass; omitted fields are skipped. At least one
  of `subject_prefix` (other than a wildcard-only value like `*`), `claims`,
  or `condition` is required; `audience` alone is not sufficient.

  - `audience: optional string`

    Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

  - `claims: optional map[string]`

    Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

  - `condition: optional string`

    CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

  - `subject_prefix: optional string`

    Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

- `name: optional string`

  Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

- `oauth_scope: optional string`

  Replaces the space-separated OAuth scopes granted on minted tokens. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

- `target: optional object { service_account_id, type, service_account_name }`

  Bind to a fixed service account by ID.

  - `service_account_id: string`

    Tagged ID of the service account to mint tokens for.

  - `type: "service_account"`

    - `"service_account"`

  - `service_account_name: optional string`

    Service account's display name at read time. Ignored on writes.

- `token_lifetime_seconds: optional number`

  Replaces the lifetime in seconds for access tokens minted via this rule (60-86400). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

- `workspace_id: optional string`

  Replaces the existing single workspace enablement (the previous one is removed). Rejected with 400 if the rule is enabled for more than one workspace; use the `/federation_rules/{federation_rule_id}/workspaces` sub-resource instead.

### Returns

- `FederationRule object { id, applies_to_all_workspaces, archived_at, 17 more }`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string`

    If set, this rule is archived and rejects token exchange.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string`

    Issuer's display name at read time.

  - `match: object { audience, claims, condition, subject_prefix }`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

    - `claims: optional map[string]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

    - `subject_prefix: optional string`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: object { service_account_id, type, service_account_name }`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

      - `"service_account"`

    - `service_account_name: optional string`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    - `"federation_rule"`

  - `updated_at: string`

    When this rule was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

#### Response

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

## Archive Federation Rule

**post** `/v1/organizations/federation_rules/{federation_rule_id}/archive`

Archive a federation rule.

Token exchange through this rule stops immediately. Idempotent;
re-archiving returns the rule with its original `archived_at`. Archiving
clears the rule's workspace targeting (`workspace_id` and
`workspace_ids` are emptied). Tokens already minted before archive
remain valid until they expire. OAuth callers may only manage rules
whose `oauth_scope` is `workspace:developer` or `workspace:inference`;
other scopes require a Console session. Admin API keys are not accepted.

### Path Parameters

- `federation_rule_id: string`

  ID of the federation rule to archive.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `FederationRule object { id, applies_to_all_workspaces, archived_at, 17 more }`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string`

    If set, this rule is archived and rejects token exchange.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string`

    Issuer's display name at read time.

  - `match: object { audience, claims, condition, subject_prefix }`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

    - `claims: optional map[string]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

    - `subject_prefix: optional string`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: object { service_account_id, type, service_account_name }`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

      - `"service_account"`

    - `service_account_name: optional string`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    - `"federation_rule"`

  - `updated_at: string`

    When this rule was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

## Domain Types

### Federation Rule

- `FederationRule object { id, applies_to_all_workspaces, archived_at, 17 more }`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string`

    If set, this rule is archived and rejects token exchange.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string`

    Issuer's display name at read time.

  - `match: object { audience, claims, condition, subject_prefix }`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

    - `claims: optional map[string]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

    - `subject_prefix: optional string`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: object { service_account_id, type, service_account_name }`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

      - `"service_account"`

    - `service_account_name: optional string`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    - `"federation_rule"`

  - `updated_at: string`

    When this rule was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

# Workspaces

## List Federation Rule Workspaces

**get** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

List workspaces where this federation rule is enabled.

Returns all workspace enablements in a single response; the `limit` and
`page` parameters are accepted but have no effect, and `next_page` is
always `null`. Returns explicit per-workspace enablements only; for
rules with `applies_to_all_workspaces` or a legacy single
`workspace_id`, check those fields on the rule itself.

### Path Parameters

- `federation_rule_id: string`

  ID of the federation rule.

### Query Parameters

- `limit: optional number`

  Number of results per page.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `data: array of object { created_at, created_by_actor_id, federation_rule_id, 3 more }`

  - `created_at: string`

    When this workspace was enabled for the rule.

  - `created_by_actor_id: string`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: string`

    Tagged ID of the federation rule.

  - `type: "federation_rule_workspace"`

    - `"federation_rule_workspace"`

  - `workspace_id: string`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: string`

    Workspace display name. Populated when listing; null in the enable response.

- `next_page: string`

  Opaque cursor for the next page; null when there are no more results.

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
    }
  ],
  "next_page": "next_page"
}
```

## Add Federation Rule Workspace

**post** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

Enable a federation rule for a workspace.

Idempotent; re-enabling returns the existing enablement. The rule and
workspace must both belong to your organization. Membership of the
rule's target service account in this workspace is not checked at
enablement: token exchange into this workspace is rejected unless the
target is a member (it is implicitly a member of the default workspace).
Archived rules are rejected with 400. OAuth callers may only manage rules whose
`oauth_scope` is `workspace:developer` or `workspace:inference`; other
scopes require a Console session. Admin API keys are not accepted.

### Path Parameters

- `federation_rule_id: string`

  ID of the federation rule.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Body Parameters

- `workspace_id: string`

  Tagged ID of the workspace to enable this rule for.

### Returns

- `created_at: string`

  When this workspace was enabled for the rule.

- `created_by_actor_id: string`

  Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

- `federation_rule_id: string`

  Tagged ID of the federation rule.

- `type: "federation_rule_workspace"`

  - `"federation_rule_workspace"`

- `workspace_id: string`

  Tagged ID of the workspace this rule is enabled for.

- `workspace_name: string`

  Workspace display name. Populated when listing; null in the enable response.

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "workspace_id": "workspace_id"
        }'
```

#### Response

```json
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace",
  "workspace_id": "workspace_id",
  "workspace_name": "workspace_name"
}
```

## Remove Federation Rule Workspace

**delete** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}`

Disable a federation rule for a workspace.

Idempotent; succeeds even if the enablement was already removed. OAuth
callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session. Admin API keys are not accepted.

### Path Parameters

- `federation_rule_id: string`

  ID of the federation rule.

- `workspace_id: string`

  ID of the workspace to disable for.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `federation_rule_id: string`

  Tagged ID of the federation rule.

- `type: "federation_rule_workspace_deleted"`

  - `"federation_rule_workspace_deleted"`

- `workspace_id: string`

  Tagged ID of the workspace named in the delete request. Removal is idempotent.

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces/$WORKSPACE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace_deleted",
  "workspace_id": "workspace_id"
}
```

## Domain Types

### Workspace List Response

- `WorkspaceListResponse object { created_at, created_by_actor_id, federation_rule_id, 3 more }`

  - `created_at: string`

    When this workspace was enabled for the rule.

  - `created_by_actor_id: string`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: string`

    Tagged ID of the federation rule.

  - `type: "federation_rule_workspace"`

    - `"federation_rule_workspace"`

  - `workspace_id: string`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: string`

    Workspace display name. Populated when listing; null in the enable response.

### Workspace Create Response

- `WorkspaceCreateResponse object { created_at, created_by_actor_id, federation_rule_id, 3 more }`

  - `created_at: string`

    When this workspace was enabled for the rule.

  - `created_by_actor_id: string`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: string`

    Tagged ID of the federation rule.

  - `type: "federation_rule_workspace"`

    - `"federation_rule_workspace"`

  - `workspace_id: string`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: string`

    Workspace display name. Populated when listing; null in the enable response.

### Workspace Delete Response

- `WorkspaceDeleteResponse object { federation_rule_id, type, workspace_id }`

  - `federation_rule_id: string`

    Tagged ID of the federation rule.

  - `type: "federation_rule_workspace_deleted"`

    - `"federation_rule_workspace_deleted"`

  - `workspace_id: string`

    Tagged ID of the workspace named in the delete request. Removal is idempotent.

# MCP Tunnels

## Get Tunnel

**get** `/v1/organizations/tunnels/{tunnel_id}`

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Retrieve a single tunnel in the caller's organization by ID.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `id: string`

  ID of the Tunnel.

- `archived_at: string`

  RFC 3339 datetime string indicating when the Tunnel was archived, or
  `null` if it is not archived.

- `created_at: string`

  RFC 3339 datetime string indicating when the Tunnel was created.

- `display_name: string`

  Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

- `domain: string`

  Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
  subdomain of this value are routed through the Tunnel. Globally unique and
  never reused, even after the Tunnel is archived.

- `type: "tunnel"`

  Object type. Always `tunnel` for Tunnels.

  - `"tunnel"`

- `workspace_id: string`

  ID of the Workspace this Tunnel belongs to, or `null` for the default
  Workspace. Immutable after creation.

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "Production",
  "domain": "a1b2c3d4.tunnel.anthropic.com",
  "type": "tunnel",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## List Tunnels

**get** `/v1/organizations/tunnels`

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

List the organization's tunnels.

Results span the caller's organization, ordered by creation time
(newest first). Use `workspace_id` to filter to a single workspace;
archived tunnels are excluded unless `include_archived` is set.

### Query Parameters

- `include_archived: optional boolean`

  Include archived tunnels in the results. Archived tunnels are excluded by
  default.

- `limit: optional number`

  Maximum number of tunnels to return in a single page.

- `page: optional string`

  Opaque pagination cursor from a previous response's `next_page`. Omit to
  fetch the first page.

- `workspace_id: optional string`

  Return only tunnels in this Workspace. Accepts a `wrkspc_`-prefixed
  Workspace ID; omit to list tunnels across all Workspaces.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `data: array of object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Tunnel was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Tunnel was created.

  - `display_name: string`

    Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

  - `domain: string`

    Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
    subdomain of this value are routed through the Tunnel. Globally unique and
    never reused, even after the Tunnel is archived.

  - `type: "tunnel"`

    Object type. Always `tunnel` for Tunnels.

    - `"tunnel"`

  - `workspace_id: string`

    ID of the Workspace this Tunnel belongs to, or `null` for the default
    Workspace. Immutable after creation.

- `next_page: string`

  Opaque cursor for the next page, or `null` if there are no more results.

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "Production",
      "domain": "a1b2c3d4.tunnel.anthropic.com",
      "type": "tunnel",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Reveal Tunnel Token

**post** `/v1/organizations/tunnels/{tunnel_id}/reveal_token`

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Return the tunnel's current connection token.

The value is fetched live on each call; Anthropic does not store it.
Repeated calls return the same value until the token is rotated.
Exposed as `POST` so the token does not appear in intermediary
access logs.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `id: string`

  Stable identifier for the current token value. Changes when the token is
  rotated.

- `tunnel_token: string`

  The tunnel's connection token.

- `type: "tunnel_token"`

  Object type. Always `tunnel_token` for Tunnel Tokens.

  - `"tunnel_token"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/reveal_token \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "ttkn_bb97000eaec162831399ca9b6684a4fdf5be49ace5683057b017aab5c87e19e0",
  "tunnel_token": "eyJhIjoiRVhBTVBMRSIsInQiOiJFWEFNUExFIiwicyI6IkVYQU1QTEUifQ==",
  "type": "tunnel_token"
}
```

## Rotate Tunnel Token

**post** `/v1/organizations/tunnels/{tunnel_id}/rotate_token`

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Invalidate the tunnel's current token for new connections and return a fresh value.

Established connections are not severed by rotation; a connector
restarted after rotation must use the new value. An optional
`reason` is captured for operational context.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Body Parameters

- `reason: optional string`

  Optional free-text reason for the rotation, recorded for audit.

### Returns

- `id: string`

  Stable identifier for the current token value. Changes when the token is
  rotated.

- `tunnel_token: string`

  The tunnel's connection token.

- `type: "tunnel_token"`

  Object type. Always `tunnel_token` for Tunnel Tokens.

  - `"tunnel_token"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/rotate_token \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "ttkn_bb97000eaec162831399ca9b6684a4fdf5be49ace5683057b017aab5c87e19e0",
  "tunnel_token": "eyJhIjoiRVhBTVBMRSIsInQiOiJFWEFNUExFIiwicyI6IkVYQU1QTEUifQ==",
  "type": "tunnel_token"
}
```

## Archive Tunnel

**post** `/v1/organizations/tunnels/{tunnel_id}/archive`

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Archive a tunnel. Archival is irreversible.

Every non-archived certificate on the tunnel is archived in the same
operation, the hostname is retired and never re-allocated, and the
tunnel token is invalidated. Retrying against an already-archived
tunnel returns the existing record unchanged.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `id: string`

  ID of the Tunnel.

- `archived_at: string`

  RFC 3339 datetime string indicating when the Tunnel was archived, or
  `null` if it is not archived.

- `created_at: string`

  RFC 3339 datetime string indicating when the Tunnel was created.

- `display_name: string`

  Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

- `domain: string`

  Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
  subdomain of this value are routed through the Tunnel. Globally unique and
  never reused, even after the Tunnel is archived.

- `type: "tunnel"`

  Object type. Always `tunnel` for Tunnels.

  - `"tunnel"`

- `workspace_id: string`

  ID of the Workspace this Tunnel belongs to, or `null` for the default
  Workspace. Immutable after creation.

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "Production",
  "domain": "a1b2c3d4.tunnel.anthropic.com",
  "type": "tunnel",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## Domain Types

### MCP Tunnel Retrieve Response

- `MCPTunnelRetrieveResponse object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Tunnel was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Tunnel was created.

  - `display_name: string`

    Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

  - `domain: string`

    Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
    subdomain of this value are routed through the Tunnel. Globally unique and
    never reused, even after the Tunnel is archived.

  - `type: "tunnel"`

    Object type. Always `tunnel` for Tunnels.

    - `"tunnel"`

  - `workspace_id: string`

    ID of the Workspace this Tunnel belongs to, or `null` for the default
    Workspace. Immutable after creation.

### MCP Tunnel List Response

- `MCPTunnelListResponse object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Tunnel was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Tunnel was created.

  - `display_name: string`

    Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

  - `domain: string`

    Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
    subdomain of this value are routed through the Tunnel. Globally unique and
    never reused, even after the Tunnel is archived.

  - `type: "tunnel"`

    Object type. Always `tunnel` for Tunnels.

    - `"tunnel"`

  - `workspace_id: string`

    ID of the Workspace this Tunnel belongs to, or `null` for the default
    Workspace. Immutable after creation.

### MCP Tunnel Reveal Token Response

- `MCPTunnelRevealTokenResponse object { id, tunnel_token, type }`

  - `id: string`

    Stable identifier for the current token value. Changes when the token is
    rotated.

  - `tunnel_token: string`

    The tunnel's connection token.

  - `type: "tunnel_token"`

    Object type. Always `tunnel_token` for Tunnel Tokens.

    - `"tunnel_token"`

### MCP Tunnel Rotate Token Response

- `MCPTunnelRotateTokenResponse object { id, tunnel_token, type }`

  - `id: string`

    Stable identifier for the current token value. Changes when the token is
    rotated.

  - `tunnel_token: string`

    The tunnel's connection token.

  - `type: "tunnel_token"`

    Object type. Always `tunnel_token` for Tunnel Tokens.

    - `"tunnel_token"`

### MCP Tunnel Archive Response

- `MCPTunnelArchiveResponse object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Tunnel was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Tunnel was created.

  - `display_name: string`

    Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

  - `domain: string`

    Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
    subdomain of this value are routed through the Tunnel. Globally unique and
    never reused, even after the Tunnel is archived.

  - `type: "tunnel"`

    Object type. Always `tunnel` for Tunnels.

    - `"tunnel"`

  - `workspace_id: string`

    ID of the Workspace this Tunnel belongs to, or `null` for the default
    Workspace. Immutable after creation.

# Tunnel Certificates

## Create Tunnel Certificate

**post** `/v1/organizations/tunnels/{tunnel_id}/certificates`

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Register a public CA certificate for the tunnel.

Anthropic verifies the gateway's server certificate against this CA
when it terminates the inner TLS session. The PEM body must contain
exactly one X.509 certificate and no private-key material. A tunnel
holds at most two non-archived certificates.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Body Parameters

- `ca_certificate_pem: string`

  PEM-encoded X.509 CA certificate. Must contain exactly one certificate and
  no private-key material.

### Returns

- `id: string`

  ID of the Tunnel Certificate.

- `archived_at: string`

  RFC 3339 datetime string indicating when the certificate was archived, or
  `null` if it is not archived.

- `created_at: string`

  RFC 3339 datetime string indicating when the certificate was registered.

- `expires_at: string`

  RFC 3339 datetime string indicating when the certificate expires, or
  `null` if it does not expire.

- `fingerprint: string`

  The certificate's SHA-256 fingerprint, as a lowercase hex string.

- `tunnel_id: string`

  ID of the Tunnel this certificate is registered against.

- `type: "tunnel_certificate"`

  Object type. Always `tunnel_certificate` for Tunnel Certificates.

  - `"tunnel_certificate"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "ca_certificate_pem": "-----BEGIN CERTIFICATE-----\\nMIIBexampleEXAMPLEexampleEXAMPLEexampleEXAMPLEexampleEXAMPLEexa\\n...illustrative placeholder, not a real certificate...\\n-----END CERTIFICATE-----\\n"
        }'
```

#### Response

```json
{
  "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "type": "tunnel_certificate"
}
```

## Get Tunnel Certificate

**get** `/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}`

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Retrieve a single certificate registered on a tunnel by ID.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

- `certificate_id: string`

  ID of the Tunnel Certificate.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `id: string`

  ID of the Tunnel Certificate.

- `archived_at: string`

  RFC 3339 datetime string indicating when the certificate was archived, or
  `null` if it is not archived.

- `created_at: string`

  RFC 3339 datetime string indicating when the certificate was registered.

- `expires_at: string`

  RFC 3339 datetime string indicating when the certificate expires, or
  `null` if it does not expire.

- `fingerprint: string`

  The certificate's SHA-256 fingerprint, as a lowercase hex string.

- `tunnel_id: string`

  ID of the Tunnel this certificate is registered against.

- `type: "tunnel_certificate"`

  Object type. Always `tunnel_certificate` for Tunnel Certificates.

  - `"tunnel_certificate"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates/$CERTIFICATE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "type": "tunnel_certificate"
}
```

## List Tunnel Certificates

**get** `/v1/organizations/tunnels/{tunnel_id}/certificates`

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

List the certificates registered on a tunnel.

Archived certificates are excluded unless `include_archived` is set.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Query Parameters

- `include_archived: optional boolean`

  Include archived certificates in the results. Archived certificates are
  excluded by default.

- `limit: optional number`

  Maximum number of certificates to return.

- `page: optional string`

  A tunnel has at most two active certificates, so this list is not
  paginated.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `data: array of object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    - `"tunnel_certificate"`

- `next_page: string`

  Opaque cursor for the next page, or `null` if there are no more results.

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
      "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
      "type": "tunnel_certificate"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Archive Tunnel Certificate

**post** `/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Archive a certificate, removing it from the set Anthropic trusts for this tunnel.

The certificate record is retained. Archiving the last non-archived
certificate is permitted; the tunnel rejects MCP traffic until a new
certificate is added.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

- `certificate_id: string`

  ID of the Tunnel Certificate.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `id: string`

  ID of the Tunnel Certificate.

- `archived_at: string`

  RFC 3339 datetime string indicating when the certificate was archived, or
  `null` if it is not archived.

- `created_at: string`

  RFC 3339 datetime string indicating when the certificate was registered.

- `expires_at: string`

  RFC 3339 datetime string indicating when the certificate expires, or
  `null` if it does not expire.

- `fingerprint: string`

  The certificate's SHA-256 fingerprint, as a lowercase hex string.

- `tunnel_id: string`

  ID of the Tunnel this certificate is registered against.

- `type: "tunnel_certificate"`

  Object type. Always `tunnel_certificate` for Tunnel Certificates.

  - `"tunnel_certificate"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates/$CERTIFICATE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "type": "tunnel_certificate"
}
```

## Domain Types

### Tunnel Certificate Create Response

- `TunnelCertificateCreateResponse object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    - `"tunnel_certificate"`

### Tunnel Certificate Retrieve Response

- `TunnelCertificateRetrieveResponse object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    - `"tunnel_certificate"`

### Tunnel Certificate List Response

- `TunnelCertificateListResponse object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    - `"tunnel_certificate"`

### Tunnel Certificate Archive Response

- `TunnelCertificateArchiveResponse object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    - `"tunnel_certificate"`

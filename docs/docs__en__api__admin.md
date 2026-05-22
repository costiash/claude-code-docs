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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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

- `role: "user" or "developer" or "billing" or "claude_code_user"`

  Role for the invited User. Cannot be "admin".

  - `"user"`

  - `"developer"`

  - `"billing"`

  - `"claude_code_user"`

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

  - `role: "user" or "developer" or "billing" or 2 more`

    Organization role of the User.

    - `"user"`

    - `"developer"`

    - `"billing"`

    - `"admin"`

    - `"claude_code_user"`

  - `status: "accepted" or "expired" or "deleted" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"expired"`

    - `"deleted"`

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
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

  - `role: "user" or "developer" or "billing" or 2 more`

    Organization role of the User.

    - `"user"`

    - `"developer"`

    - `"billing"`

    - `"admin"`

    - `"claude_code_user"`

  - `status: "accepted" or "expired" or "deleted" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"expired"`

    - `"deleted"`

    - `"pending"`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

    - `"invite"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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

  - `role: "user" or "developer" or "billing" or 2 more`

    Organization role of the User.

    - `"user"`

    - `"developer"`

    - `"billing"`

    - `"admin"`

    - `"claude_code_user"`

  - `status: "accepted" or "expired" or "deleted" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"expired"`

    - `"deleted"`

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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

  - `role: "user" or "developer" or "billing" or 2 more`

    Organization role of the User.

    - `"user"`

    - `"developer"`

    - `"billing"`

    - `"admin"`

    - `"claude_code_user"`

  - `status: "accepted" or "expired" or "deleted" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"expired"`

    - `"deleted"`

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

  - `role: "user" or "developer" or "billing" or 2 more`

    Organization role of the User.

    - `"user"`

    - `"developer"`

    - `"billing"`

    - `"admin"`

    - `"claude_code_user"`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    - `"user"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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

  - `role: "user" or "developer" or "billing" or 2 more`

    Organization role of the User.

    - `"user"`

    - `"developer"`

    - `"billing"`

    - `"admin"`

    - `"claude_code_user"`

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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

- `role: "user" or "developer" or "billing" or "claude_code_user"`

  New role for the User. Cannot be "admin".

  - `"user"`

  - `"developer"`

  - `"billing"`

  - `"claude_code_user"`

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

  - `role: "user" or "developer" or "billing" or 2 more`

    Organization role of the User.

    - `"user"`

    - `"developer"`

    - `"billing"`

    - `"admin"`

    - `"claude_code_user"`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    - `"user"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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

  - `role: "user" or "developer" or "billing" or 2 more`

    Organization role of the User.

    - `"user"`

    - `"developer"`

    - `"billing"`

    - `"admin"`

    - `"claude_code_user"`

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

- `tags: optional map[string]`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

### Returns

- `Workspace object { id, archived_at, created_at, 5 more }`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
          "name": "x",
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
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
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

- `Workspace object { id, archived_at, created_at, 5 more }`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

#### Response

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "data_residency": {
        "allowed_inference_geos": "unrestricted",
        "default_inference_geo": "default_inference_geo",
        "workspace_geo": "workspace_geo"
      },
      "display_color": "#6C5BB9",
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

- `name: optional string`

  Name of the Workspace.

- `tags: optional map[string]`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

### Returns

- `Workspace object { id, archived_at, created_at, 5 more }`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
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
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
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

- `Workspace object { id, archived_at, created_at, 5 more }`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

#### Response

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
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

- `workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or "workspace_admin"`

  Role of the new Workspace Member. Cannot be "workspace_billing".

  - `"workspace_user"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_admin"`

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

  - `workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more`

    Role of the Workspace Member.

    - `"workspace_user"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_admin"`

    - `"workspace_billing"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "workspace_role": "workspace_user"
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

  - `workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more`

    Role of the Workspace Member.

    - `"workspace_user"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_admin"`

    - `"workspace_billing"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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

  - `workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more`

    Role of the Workspace Member.

    - `"workspace_user"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_admin"`

    - `"workspace_billing"`

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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

- `workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more`

  New workspace role for the User.

  - `"workspace_user"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_admin"`

  - `"workspace_billing"`

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

  - `workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more`

    Role of the Workspace Member.

    - `"workspace_user"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_admin"`

    - `"workspace_billing"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
          "workspace_role": "workspace_user"
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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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

  - `workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more`

    Role of the Workspace Member.

    - `"workspace_user"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_admin"`

    - `"workspace_billing"`

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

- `group_type: optional "model_group" or "batch" or "token_count" or 3 more`

  Filter by group type.

  - `"model_group"`

  - `"batch"`

  - `"token_count"`

  - `"files"`

  - `"skills"`

  - `"web_search"`

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Returns

- `data: array of object { group_type, limits, models, type }`

  Rate-limit entries for the workspace, one per group that has at least one override.

  - `group_type: "model_group" or "batch" or "token_count" or 3 more`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `"model_group"`

    - `"batch"`

    - `"token_count"`

    - `"files"`

    - `"skills"`

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "group_type": "model_group",
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

    - `group_type: "model_group" or "batch" or "token_count" or 3 more`

      The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

      - `"model_group"`

      - `"batch"`

      - `"token_count"`

      - `"files"`

      - `"skills"`

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

  - `status: "active" or "inactive" or "archived" or "expired"`

    Status of the API key.

    - `"active"`

    - `"inactive"`

    - `"archived"`

    - `"expired"`

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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

- `status: optional "active" or "inactive" or "archived" or "expired"`

  Filter by API key status.

  - `"active"`

  - `"inactive"`

  - `"archived"`

  - `"expired"`

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

  - `status: "active" or "inactive" or "archived" or "expired"`

    Status of the API key.

    - `"active"`

    - `"inactive"`

    - `"archived"`

    - `"expired"`

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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

- `status: optional "active" or "inactive" or "archived"`

  Status of the API key.

  - `"active"`

  - `"inactive"`

  - `"archived"`

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

  - `status: "active" or "inactive" or "archived" or "expired"`

    Status of the API key.

    - `"active"`

    - `"inactive"`

    - `"archived"`

    - `"expired"`

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
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

- `bucket_width: optional "1d" or "1m" or "1h"`

  Time granularity of the response data.

  - `"1d"`

  - `"1m"`

  - `"1h"`

- `context_window: optional array of "0-200k" or "200k-1M"`

  Restrict usage returned to the specified context window(s).

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  Time buckets that end before this RFC 3339 timestamp will be returned.

- `group_by: optional array of "api_key_id" or "workspace_id" or "model" or 6 more`

  Group by any subset of the available options. Grouping by `speed` requires the `fast-mode-2026-02-01` beta header.

  - `"api_key_id"`

  - `"workspace_id"`

  - `"model"`

  - `"service_tier"`

  - `"context_window"`

  - `"inference_geo"`

  - `"speed"`

  - `"account_id"`

  - `"service_account_id"`

- `inference_geos: optional array of "global" or "us" or "not_available"`

  Restrict usage returned to the specified inference geo(s). Use `not_available` for models that do not support specifying `inference_geo`.

  - `"global"`

  - `"us"`

  - `"not_available"`

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

- `service_tiers: optional array of "standard" or "batch" or "priority" or 3 more`

  Restrict usage returned to the specified service tier(s).

  - `"standard"`

  - `"batch"`

  - `"priority"`

  - `"priority_on_demand"`

  - `"flex"`

  - `"flex_discount"`

- `speeds: optional array of "standard" or "fast"`

  Restrict usage returned to the specified speed(s) (Claude Code research preview).
  Requires the `fast-mode-2026-02-01` beta header.

  - `"standard"`

  - `"fast"`

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

      - `service_tier: "standard" or "batch" or "priority" or 3 more`

        Service tier used. `null` if not grouping by service tier.

        - `"standard"`

        - `"batch"`

        - `"priority"`

        - `"priority_on_demand"`

        - `"flex"`

        - `"flex_discount"`

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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

      - `service_tier: "standard" or "batch" or "priority" or 3 more`

        Service tier used. `null` if not grouping by service tier.

        - `"standard"`

        - `"batch"`

        - `"priority"`

        - `"priority_on_demand"`

        - `"flex"`

        - `"flex_discount"`

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

- `group_by: optional array of "workspace_id" or "description"`

  Group by any subset of the available options.

  - `"workspace_id"`

  - `"description"`

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

      - `cost_type: "tokens" or "web_search" or "code_execution" or "session_usage"`

        Type of cost. `null` if not grouping by description.

        - `"tokens"`

        - `"web_search"`

        - `"code_execution"`

        - `"session_usage"`

      - `currency: string`

        Currency code for the cost amount. Currently always `"USD"`.

      - `description: string`

        Description of the cost item. `null` if not grouping by description.

      - `inference_geo: string`

        Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`.
        For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

      - `model: string`

        Model name used. `null` if not grouping by description or for non-token costs.

      - `service_tier: "standard" or "batch"`

        Service tier used. `null` if not grouping by description or for non-token costs.

        - `"standard"`

        - `"batch"`

      - `token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more`

        Type of token. `null` if not grouping by description or for non-token costs.

        - `"uncached_input_tokens"`

        - `"output_tokens"`

        - `"cache_read_input_tokens"`

        - `"cache_creation.ephemeral_1h_input_tokens"`

        - `"cache_creation.ephemeral_5m_input_tokens"`

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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

      - `cost_type: "tokens" or "web_search" or "code_execution" or "session_usage"`

        Type of cost. `null` if not grouping by description.

        - `"tokens"`

        - `"web_search"`

        - `"code_execution"`

        - `"session_usage"`

      - `currency: string`

        Currency code for the cost amount. Currently always `"USD"`.

      - `description: string`

        Description of the cost item. `null` if not grouping by description.

      - `inference_geo: string`

        Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`.
        For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

      - `model: string`

        Model name used. `null` if not grouping by description or for non-token costs.

      - `service_tier: "standard" or "batch"`

        Service tier used. `null` if not grouping by description or for non-token costs.

        - `"standard"`

        - `"batch"`

      - `token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more`

        Type of token. `null` if not grouping by description or for non-token costs.

        - `"uncached_input_tokens"`

        - `"output_tokens"`

        - `"cache_read_input_tokens"`

        - `"cache_creation.ephemeral_1h_input_tokens"`

        - `"cache_creation.ephemeral_5m_input_tokens"`

      - `workspace_id: string`

        ID of the Workspace this cost is associated with. `null` if not grouping by workspace or for the default workspace.

    - `starting_at: string`

      Start of the time bucket (inclusive) in RFC 3339 format.

  - `has_more: boolean`

    Indicates if there are more results.

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

# Rate Limits

## List Organization Rate Limits

**get** `/v1/organizations/rate_limits`

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

### Query Parameters

- `group_type: optional "model_group" or "batch" or "token_count" or 3 more`

  Filter by group type.

  - `"model_group"`

  - `"batch"`

  - `"token_count"`

  - `"files"`

  - `"skills"`

  - `"web_search"`

- `model: optional string`

  Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Returns

- `data: array of object { group_type, limits, models, type }`

  Rate-limit entries for the organization, one per group.

  - `group_type: "model_group" or "batch" or "token_count" or 3 more`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `"model_group"`

    - `"batch"`

    - `"token_count"`

    - `"files"`

    - `"skills"`

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
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "group_type": "model_group",
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

    - `group_type: "model_group" or "batch" or "token_count" or 3 more`

      The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

      - `"model_group"`

      - `"batch"`

      - `"token_count"`

      - `"files"`

      - `"skills"`

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

# MCP Tunnels

## Get Tunnel

**get** `/v1/organizations/tunnels/{tunnel_id}`

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
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
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
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
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
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
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
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
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
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
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

- `MCPTunnelListResponse object { data, next_page }`

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
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN" \
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
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
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
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
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
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
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

- `TunnelCertificateListResponse object { data, next_page }`

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

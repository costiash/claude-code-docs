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

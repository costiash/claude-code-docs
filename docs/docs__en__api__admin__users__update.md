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

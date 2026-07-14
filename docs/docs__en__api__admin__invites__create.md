## Create Invite

**post** `/v1/organizations/invites`

For Claude Enterprise organizations, this endpoint's availability is in beta.

On plans that draw members from a finite pool of purchased seats, the invite automatically consumes a seat from the lowest tier with availability; there is no seat-tier parameter. When no seat is free the request fails with a 400 error rather than purchasing a seat.

### Body Parameters

- `email: string`

  Email of the User.

- `role: "billing" or "claude_code_user" or "developer" or 2 more`

  Role for the invited User.

  The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations (beta) accept `user` and `managed`.

  - `"billing"`

  - `"claude_code_user"`

  - `"developer"`

  - `"managed"`

  - `"user"`

- `rbac_group_ids: optional array of string`

  RBAC group IDs to assign to the User when the Invite is accepted. A non-empty array is accepted only for a Claude Enterprise organization with RBAC groups (beta), and requires the key to carry the `write:rbac_groups` scope.

### Returns

- `Invite object { id, accepted_at, email, 6 more }`

  - `id: string`

    ID of the Invite.

  - `accepted_at: string`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

  - `email: string`

    Email of the User being invited.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the Invite expires.

  - `invited_at: string`

    RFC 3339 datetime string indicating when the Invite was created.

  - `rbac_group_ids: array of string`

    RBAC group IDs recorded on the Invite (beta, Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `role: "admin" or "billing" or "claude_code_user" or 6 more`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

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
  "accepted_at": "2019-12-27T18:11:19.117Z",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "rbac_group_ids": [
    "string"
  ],
  "role": "user",
  "status": "pending",
  "type": "invite"
}
```

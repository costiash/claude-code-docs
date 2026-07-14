## Delete Invite

**delete** `/v1/organizations/invites/{invite_id}`

For Claude Enterprise organizations, this endpoint's availability is in beta.

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

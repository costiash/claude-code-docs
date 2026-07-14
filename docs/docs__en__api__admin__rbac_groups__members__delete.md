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

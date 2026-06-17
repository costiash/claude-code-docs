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

- `workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or "workspace_admin"`

  New role for the service account in this workspace.

  - `"workspace_user"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_admin"`

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

- `workspace_role: "workspace_user" or "workspace_developer" or "workspace_restricted_developer" or 2 more`

  Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

  - `"workspace_user"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_admin"`

  - `"workspace_billing"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "workspace_role": "workspace_user"
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
  "workspace_role": "workspace_user"
}
```

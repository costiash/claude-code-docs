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

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

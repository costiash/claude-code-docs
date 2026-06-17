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

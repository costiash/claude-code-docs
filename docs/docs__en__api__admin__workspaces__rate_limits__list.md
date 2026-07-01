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

- `group_type: optional "batch" or "files" or "model_group" or 3 more`

  Filter by group type.

  - `"batch"`

  - `"files"`

  - `"model_group"`

  - `"skills"`

  - `"token_count"`

  - `"web_search"`

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Returns

- `data: array of object { group_type, limits, models, type }`

  Rate-limit entries for the workspace, one per group that has at least one override.

  - `group_type: "batch" or "files" or "model_group" or 3 more`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `"batch"`

    - `"files"`

    - `"model_group"`

    - `"skills"`

    - `"token_count"`

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
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "group_type": "batch",
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

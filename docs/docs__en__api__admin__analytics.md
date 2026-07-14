# Analytics

## Get Activity Summaries

**get** `/v1/organizations/analytics/summaries`

Get organization-wide activity summaries for a date range.

Returns one entry per day in [starting_date, ending_date). Data is
typically available with a 1-day lag and may be revised by a few percent
over the following days: when ending_date is omitted it defaults to the
most recent available day + 1, so the last entry covers the most recent
available day. Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

### Query Parameters

- `starting_date: string`

  UTC date in YYYY-MM-DD format. Start of the date range (inclusive). Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive). Data is typically available with a 1-day lag, so this can be at most today — which is also the default when omitted, making the last entry cover the most recent available day. Data may be revised by a few percent over the following days. The range may span at most 366 days.

- `filter: optional array of string`

  Filters as 'dimension:value'. Only rbac_group_id is supported (e.g. filter[]=rbac_group_id:<id>); repeat the param to OR across groups. Scopes the whole day series to members of the matching group(s), re-aggregated from member-level activity — org-wide seat/invite fields and the adoption rates derived from them are null on scoped rows. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each UTC day (time-of-usage attribution). At most 100 entries.

### Returns

- `ActivitySummary object { summaries }`

  Response for GET /v1/organizations/analytics/summaries.

  - `summaries: array of object { assigned_seat_count, cowork_daily_active_user_count, cowork_monthly_active_user_count, 26 more }`

    - `assigned_seat_count: number`

      Number of seats currently assigned to members. Null when the response is scoped to an RBAC group — seat assignment is org-wide and has no per-group analogue.

    - `cowork_daily_active_user_count: number`

      Number of users with Cowork activity on the requested day

    - `cowork_monthly_active_user_count: number`

      Number of users with Cowork activity in the 30-day rolling window

    - `cowork_weekly_active_user_count: number`

      Number of users with Cowork activity in the 7-day rolling window

    - `daily_active_user_count: number`

      Number of users with token consumption on the requested day

    - `daily_adoption_rate: number`

      Percentage of assigned seats with activity on the requested day (DAU / assigned_seat_count * 100). Null when the response is scoped to an RBAC group.

    - `ending_at: string`

      End time in UTC of aggregation period (e.g. 2026-01-16T00:00:00Z)

    - `monthly_active_user_count: number`

      Number of users with token consumption in the 30-day rolling window

    - `monthly_adoption_rate: number`

      Percentage of assigned seats with activity in the 30-day rolling window (MAU / assigned_seat_count * 100). Null when the response is scoped to an RBAC group.

    - `pending_invite_count: number`

      Number of pending invitations to join the organization. Null when the response is scoped to an RBAC group.

    - `starting_at: string`

      Start time in UTC of aggregation period (e.g. 2026-01-15T00:00:00Z)

    - `weekly_active_user_count: number`

      Number of users with token consumption in the 7-day rolling window

    - `weekly_adoption_rate: number`

      Percentage of assigned seats with activity in the 7-day rolling window (WAU / assigned_seat_count * 100). Null when the response is scoped to an RBAC group.

    - `chat_daily_active_user_count: optional number`

      Number of users with claude.ai (chat) activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `chat_monthly_active_user_count: optional number`

      Number of users with claude.ai (chat) activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `chat_weekly_active_user_count: optional number`

      Number of users with claude.ai (chat) activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_code_daily_active_user_count: optional number`

      Number of users with Claude Code activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_code_monthly_active_user_count: optional number`

      Number of users with Claude Code activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_code_weekly_active_user_count: optional number`

      Number of users with Claude Code activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_design_daily_active_user_count: optional number`

      Number of users with Claude Design activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_design_monthly_active_user_count: optional number`

      Number of users with Claude Design activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_design_weekly_active_user_count: optional number`

      Number of users with Claude Design activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `office_agent_daily_active_user_count: optional number`

      Number of users with Claude in Office activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `office_agent_monthly_active_user_count: optional number`

      Number of users with Claude in Office activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `office_agent_weekly_active_user_count: optional number`

      Number of users with Claude in Office activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_daily_active_user_count: optional number`

      Number of users with Claude Science activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_entitled_user_count: optional number`

      Number of users with a Claude Science seat entitlement (per-seat RBAC) at the time of the daily snapshot. The funnel top; independent of the org-level Claude Science toggle. Null when the response is scoped to an RBAC group — entitlement is org-wide and has no per-group analogue. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_monthly_active_user_count: optional number`

      Number of users with Claude Science activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_weekly_active_user_count: optional number`

      Number of users with Claude Science activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/summaries \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "summaries": [
    {
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "ending_at",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "starting_at",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0,
      "chat_daily_active_user_count": 0,
      "chat_monthly_active_user_count": 0,
      "chat_weekly_active_user_count": 0,
      "claude_code_daily_active_user_count": 0,
      "claude_code_monthly_active_user_count": 0,
      "claude_code_weekly_active_user_count": 0,
      "claude_design_daily_active_user_count": 0,
      "claude_design_monthly_active_user_count": 0,
      "claude_design_weekly_active_user_count": 0,
      "office_agent_daily_active_user_count": 0,
      "office_agent_monthly_active_user_count": 0,
      "office_agent_weekly_active_user_count": 0,
      "science_daily_active_user_count": 0,
      "science_entitled_user_count": 0,
      "science_monthly_active_user_count": 0,
      "science_weekly_active_user_count": 0
    }
  ]
}
```

## Domain Types

### Activity Summary

- `ActivitySummary object { summaries }`

  Response for GET /v1/organizations/analytics/summaries.

  - `summaries: array of object { assigned_seat_count, cowork_daily_active_user_count, cowork_monthly_active_user_count, 26 more }`

    - `assigned_seat_count: number`

      Number of seats currently assigned to members. Null when the response is scoped to an RBAC group — seat assignment is org-wide and has no per-group analogue.

    - `cowork_daily_active_user_count: number`

      Number of users with Cowork activity on the requested day

    - `cowork_monthly_active_user_count: number`

      Number of users with Cowork activity in the 30-day rolling window

    - `cowork_weekly_active_user_count: number`

      Number of users with Cowork activity in the 7-day rolling window

    - `daily_active_user_count: number`

      Number of users with token consumption on the requested day

    - `daily_adoption_rate: number`

      Percentage of assigned seats with activity on the requested day (DAU / assigned_seat_count * 100). Null when the response is scoped to an RBAC group.

    - `ending_at: string`

      End time in UTC of aggregation period (e.g. 2026-01-16T00:00:00Z)

    - `monthly_active_user_count: number`

      Number of users with token consumption in the 30-day rolling window

    - `monthly_adoption_rate: number`

      Percentage of assigned seats with activity in the 30-day rolling window (MAU / assigned_seat_count * 100). Null when the response is scoped to an RBAC group.

    - `pending_invite_count: number`

      Number of pending invitations to join the organization. Null when the response is scoped to an RBAC group.

    - `starting_at: string`

      Start time in UTC of aggregation period (e.g. 2026-01-15T00:00:00Z)

    - `weekly_active_user_count: number`

      Number of users with token consumption in the 7-day rolling window

    - `weekly_adoption_rate: number`

      Percentage of assigned seats with activity in the 7-day rolling window (WAU / assigned_seat_count * 100). Null when the response is scoped to an RBAC group.

    - `chat_daily_active_user_count: optional number`

      Number of users with claude.ai (chat) activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `chat_monthly_active_user_count: optional number`

      Number of users with claude.ai (chat) activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `chat_weekly_active_user_count: optional number`

      Number of users with claude.ai (chat) activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_code_daily_active_user_count: optional number`

      Number of users with Claude Code activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_code_monthly_active_user_count: optional number`

      Number of users with Claude Code activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_code_weekly_active_user_count: optional number`

      Number of users with Claude Code activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_design_daily_active_user_count: optional number`

      Number of users with Claude Design activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_design_monthly_active_user_count: optional number`

      Number of users with Claude Design activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `claude_design_weekly_active_user_count: optional number`

      Number of users with Claude Design activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `office_agent_daily_active_user_count: optional number`

      Number of users with Claude in Office activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `office_agent_monthly_active_user_count: optional number`

      Number of users with Claude in Office activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `office_agent_weekly_active_user_count: optional number`

      Number of users with Claude in Office activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_daily_active_user_count: optional number`

      Number of users with Claude Science activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_entitled_user_count: optional number`

      Number of users with a Claude Science seat entitlement (per-seat RBAC) at the time of the daily snapshot. The funnel top; independent of the org-level Claude Science toggle. Null when the response is scoped to an RBAC group — entitlement is org-wide and has no per-group analogue. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_monthly_active_user_count: optional number`

      Number of users with Claude Science activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

    - `science_weekly_active_user_count: optional number`

      Number of users with Claude Science activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

### Analytics User

- `AnalyticsUser object { id, email_address }`

  User identifier.

  - `id: string`

    Tagged user identifier (e.g. user_...)

  - `email_address: string`

    Email address of the user

### Analytics User Actor

- `AnalyticsUserActor object { user_id, deleted, email, 2 more }`

  - `user_id: string`

    Tagged user ID.

  - `deleted: optional boolean`

    True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

  - `email: optional string`

    The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

  - `name: optional string`

    The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

  - `type: optional "user_actor"`

    - `"user_actor"`

### Connector Office Product Metrics

- `ConnectorOfficeProductMetrics object { distinct_session_connector_used_count }`

  Office Agent activity metrics for a single connector on a given day within one Office product.

  - `distinct_session_connector_used_count: number`

    Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Office Product Metrics

- `OfficeProductMetrics object { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more }`

  Office Agent activity metrics for a single user on a given day within one Office product.

  - `connectors_used_count: number`

    Number of MCP connector invocations

  - `distinct_connectors_used_count: number`

    Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_session_count: number`

    Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_skills_used_count: number`

    Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `message_count: number`

    Number of messages sent

  - `skills_used_count: number`

    Number of skill invocations

### Skill Office Product Metrics

- `SkillOfficeProductMetrics object { distinct_session_skill_used_count }`

  Office Agent activity metrics for a single skill on a given day within one Office product.

  - `distinct_session_skill_used_count: number`

    Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Tool Action Counts

- `ToolActionCounts object { accepted_count, rejected_count }`

  Accepted/rejected counts for a single Claude Code tool type.

  - `accepted_count: number`

    Number of tool proposals accepted

  - `rejected_count: number`

    Number of tool proposals rejected

# Usage

## Get Token Usage Over Time

**get** `/v1/organizations/analytics/usage_report`

Get token usage over time across a date range.

Returns token usage bucketed by minute, hour, or day, optionally broken
down by product, model, context window, inference region, or speed.
Available to organizations on a Claude Enterprise plan. Requires an API
key with the `read:analytics` scope.

### Query Parameters

- `starting_at: string`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

- `bucket_width: optional "1d" or "1h" or "1m"`

  Time bucket granularity.

  - `"1d"`

  - `"1h"`

  - `"1m"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `group_by: optional array of "context_window" or "inference_geo" or "model" or 3 more`

  Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket). Each bucket reports at most its top 100 groups; a group beyond that cap has no row in that bucket (there is no remainder row), so grouped buckets are not exhaustive when a dimension has more than 100 distinct values.

  - `"context_window"`

  - `"inference_geo"`

  - `"model"`

  - `"product"`

  - `"rbac_group_id"`

  - `"speed"`

- `inference_geos: optional array of "global" or "not_available" or "us"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"not_available"`

  - `"us"`

- `limit: optional number`

  Maximum number of time buckets per page. Defaults and caps vary by bucket_width (1d: default 7, max 31; 1h: default 24, max 168; 1m: default 60, max 256).

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it.

- `rbac_group_ids: optional array of string`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

- `speeds: optional array of "fast" or "standard"`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  - `"fast"`

  - `"standard"`

- `user_ids: optional array of string`

  Filter to specific users by tagged user ID.

### Returns

- `UsageBucket object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { ending_at, results, starting_at }`

    - `ending_at: string`

    - `results: array of object { cache_creation, cache_read_input_tokens, context_window, 9 more }`

      - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

        - `ephemeral_1h_input_tokens: number`

          The number of input tokens used to create the 1 hour cache entry.

        - `ephemeral_5m_input_tokens: number`

          The number of input tokens used to create the 5 minute cache entry.

      - `cache_read_input_tokens: number`

        The number of input tokens read from the cache.

      - `context_window: "0-200k" or "200k-1M"`

        - `"0-200k"`

        - `"200k-1M"`

      - `inference_geo: "global" or "us"`

        - `"global"`

        - `"us"`

      - `model: string`

      - `output_tokens: number`

        The number of output tokens generated.

      - `product: string`

        Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

      - `rbac_group_id: string`

        RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

      - `requests: number`

        Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

      - `server_tool_use: object { web_search_requests }`

        - `web_search_requests: number`

          The number of web search requests made.

      - `speed: "fast" or "standard"`

        - `"fast"`

        - `"standard"`

      - `uncached_input_tokens: number`

        The number of uncached input tokens processed.

    - `starting_at: string`

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/usage_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
        {
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 0,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "model",
          "output_tokens": 0,
          "product": "product",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "speed": "fast",
          "uncached_input_tokens": 0
        }
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Get Per-User Token Usage

**get** `/v1/organizations/analytics/user_usage_report`

Get per-user token usage across a date range.

Returns one row per user, ranked by the chosen token metric. Use this to
see which users consume the most tokens. Only usage attributable to a
seat user is included; for organization-wide totals including direct
API-key and automation traffic, use the bucketed
`/v1/organizations/analytics/usage_report` endpoint. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

### Query Parameters

- `starting_at: string`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

- `bucket_width: optional "1d" or "1h" or "1m"`

  Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

  - `"1d"`

  - `"1h"`

  - `"1m"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `exclude_deleted_users: optional boolean`

  If true, omit rows for deleted accounts. Pages may return fewer than `limit` rows when deleted users were filtered.

- `group_by: optional array of "context_window" or "inference_geo" or "model" or 3 more`

  Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/usage_report` endpoint. `limit` bounds (actor × time bucket × dimension) rows — with dimensions or `bucket_width` present, one actor may span several rows.

  - `"context_window"`

  - `"inference_geo"`

  - `"model"`

  - `"product"`

  - `"rbac_group_id"`

  - `"speed"`

- `inference_geos: optional array of "global" or "not_available" or "us"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"not_available"`

  - `"us"`

- `limit: optional number`

  Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `order: optional "asc" or "desc"`

  Sort direction. Defaults to `desc`.

  - `"asc"`

  - `"desc"`

- `order_by: optional "output_tokens" or "requests" or "total_tokens" or "uncached_input_tokens"`

  Metric to rank actors by. Defaults to `total_tokens`.

  - `"output_tokens"`

  - `"requests"`

  - `"total_tokens"`

  - `"uncached_input_tokens"`

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it.

- `rbac_group_ids: optional array of string`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

- `speeds: optional array of "fast" or "standard"`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  - `"fast"`

  - `"standard"`

- `user_ids: optional array of string`

  Filter to specific users by tagged user ID.

### Returns

- `UserUsage object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { actor, cache_creation, cache_read_input_tokens, 13 more }`

    - `actor: AnalyticsUserActor`

      - `user_id: string`

        Tagged user ID.

      - `deleted: optional boolean`

        True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

      - `email: optional string`

        The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

      - `name: optional string`

        The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

      - `ephemeral_1h_input_tokens: number`

        The number of input tokens used to create the 1 hour cache entry.

      - `ephemeral_5m_input_tokens: number`

        The number of input tokens used to create the 5 minute cache entry.

    - `cache_read_input_tokens: number`

      The number of input tokens read from the cache.

    - `context_window: "0-200k" or "200k-1M"`

      - `"0-200k"`

      - `"200k-1M"`

    - `ending_at: string`

    - `inference_geo: "global" or "us"`

      - `"global"`

      - `"us"`

    - `model: string`

    - `output_tokens: number`

      The number of output tokens generated.

    - `product: string`

      Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

    - `rbac_group_id: string`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

    - `requests: number`

      Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `server_tool_use: object { web_search_requests }`

      - `web_search_requests: number`

        The number of web search requests made.

    - `speed: "fast" or "standard"`

      - `"fast"`

      - `"standard"`

    - `starting_at: string`

    - `total_tokens: number`

      Total token count across all token types. This is the value the default order_by='total_tokens' sorts on.

    - `uncached_input_tokens: number`

      The number of uncached input tokens processed.

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/user_usage_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "actor": {
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt",
        "deleted": true,
        "email": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor"
      },
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1000,
        "ephemeral_5m_input_tokens": 500
      },
      "cache_read_input_tokens": 3200000,
      "context_window": "0-200k",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "model": "model",
      "output_tokens": 891000,
      "product": "product",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "server_tool_use": {
        "web_search_requests": 10
      },
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "total_tokens": 5377000,
      "uncached_input_tokens": 1284500
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Domain Types

### Usage Bucket

- `UsageBucket object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { ending_at, results, starting_at }`

    - `ending_at: string`

    - `results: array of object { cache_creation, cache_read_input_tokens, context_window, 9 more }`

      - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

        - `ephemeral_1h_input_tokens: number`

          The number of input tokens used to create the 1 hour cache entry.

        - `ephemeral_5m_input_tokens: number`

          The number of input tokens used to create the 5 minute cache entry.

      - `cache_read_input_tokens: number`

        The number of input tokens read from the cache.

      - `context_window: "0-200k" or "200k-1M"`

        - `"0-200k"`

        - `"200k-1M"`

      - `inference_geo: "global" or "us"`

        - `"global"`

        - `"us"`

      - `model: string`

      - `output_tokens: number`

        The number of output tokens generated.

      - `product: string`

        Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

      - `rbac_group_id: string`

        RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

      - `requests: number`

        Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

      - `server_tool_use: object { web_search_requests }`

        - `web_search_requests: number`

          The number of web search requests made.

      - `speed: "fast" or "standard"`

        - `"fast"`

        - `"standard"`

      - `uncached_input_tokens: number`

        The number of uncached input tokens processed.

    - `starting_at: string`

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

### User Usage

- `UserUsage object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { actor, cache_creation, cache_read_input_tokens, 13 more }`

    - `actor: AnalyticsUserActor`

      - `user_id: string`

        Tagged user ID.

      - `deleted: optional boolean`

        True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

      - `email: optional string`

        The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

      - `name: optional string`

        The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

      - `ephemeral_1h_input_tokens: number`

        The number of input tokens used to create the 1 hour cache entry.

      - `ephemeral_5m_input_tokens: number`

        The number of input tokens used to create the 5 minute cache entry.

    - `cache_read_input_tokens: number`

      The number of input tokens read from the cache.

    - `context_window: "0-200k" or "200k-1M"`

      - `"0-200k"`

      - `"200k-1M"`

    - `ending_at: string`

    - `inference_geo: "global" or "us"`

      - `"global"`

      - `"us"`

    - `model: string`

    - `output_tokens: number`

      The number of output tokens generated.

    - `product: string`

      Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

    - `rbac_group_id: string`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

    - `requests: number`

      Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `server_tool_use: object { web_search_requests }`

      - `web_search_requests: number`

        The number of web search requests made.

    - `speed: "fast" or "standard"`

      - `"fast"`

      - `"standard"`

    - `starting_at: string`

    - `total_tokens: number`

      Total token count across all token types. This is the value the default order_by='total_tokens' sorts on.

    - `uncached_input_tokens: number`

      The number of uncached input tokens processed.

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

# Cost

## Get Cost Over Time

**get** `/v1/organizations/analytics/cost_report`

Get cost in USD over time across a date range.

Returns cost bucketed by minute, hour, or day, optionally broken down by
product, model, context window, inference region, speed, cost type, or
token type. Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

### Query Parameters

- `starting_at: string`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

- `bucket_width: optional "1d" or "1h" or "1m"`

  Time bucket granularity.

  - `"1d"`

  - `"1h"`

  - `"1m"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `group_by: optional array of "context_window" or "cost_type" or "inference_geo" or 5 more`

  Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket). Each bucket reports at most its top 100 groups; a group beyond that cap has no row in that bucket (there is no remainder row), so grouped buckets are not exhaustive when a dimension has more than 100 distinct values.

  - `"context_window"`

  - `"cost_type"`

  - `"inference_geo"`

  - `"model"`

  - `"product"`

  - `"rbac_group_id"`

  - `"speed"`

  - `"token_type"`

- `inference_geos: optional array of "global" or "not_available" or "us"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"not_available"`

  - `"us"`

- `limit: optional number`

  Maximum number of time buckets per page. Defaults and caps vary by bucket_width (1d: default 7, max 31; 1h: default 24, max 168; 1m: default 60, max 256).

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it.

- `rbac_group_ids: optional array of string`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

- `speeds: optional array of "fast" or "standard"`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  - `"fast"`

  - `"standard"`

- `user_ids: optional array of string`

  Filter to specific users by tagged user ID.

### Returns

- `CostBucket object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { ending_at, results, starting_at }`

    - `ending_at: string`

    - `results: array of object { amount, context_window, cost_type, 9 more }`

      - `amount: string`

        Amount (post-discount, pre-credit) in fractional cents.

      - `context_window: "0-200k" or "200k-1M"`

        - `"0-200k"`

        - `"200k-1M"`

      - `cost_type: "code_execution" or "tokens" or "web_search"`

        Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).

        - `"code_execution"`

        - `"tokens"`

        - `"web_search"`

      - `currency: "USD"`

        - `"USD"`

      - `inference_geo: "global" or "us"`

        - `"global"`

        - `"us"`

      - `list_amount: string`

        List-price amount (pre-discount) in fractional cents.

      - `model: string`

      - `product: string`

        Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

      - `rbac_group_id: string`

        RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

      - `requests: number`

        Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

      - `speed: "fast" or "standard"`

        - `"fast"`

        - `"standard"`

      - `token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more`

        Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.

        - `"cache_creation.ephemeral_1h_input_tokens"`

        - `"cache_creation.ephemeral_5m_input_tokens"`

        - `"cache_read_input_tokens"`

        - `"output_tokens"`

        - `"uncached_input_tokens"`

    - `starting_at: string`

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/cost_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
        {
          "amount": "amount",
          "context_window": "0-200k",
          "cost_type": "code_execution",
          "currency": "USD",
          "inference_geo": "global",
          "list_amount": "list_amount",
          "model": "model",
          "product": "product",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "speed": "fast",
          "token_type": "cache_creation.ephemeral_1h_input_tokens"
        }
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Get Per-User Cost

**get** `/v1/organizations/analytics/user_cost_report`

Get per-user cost in USD across a date range.

Returns one row per user, ranked by spend. Use this to see which users
account for the most cost. Only cost attributable to a seat user is
included; for organization-wide totals including direct API-key and
automation traffic, use the bucketed
`/v1/organizations/analytics/cost_report` endpoint. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

### Query Parameters

- `starting_at: string`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

- `bucket_width: optional "1d" or "1h" or "1m"`

  Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

  - `"1d"`

  - `"1h"`

  - `"1m"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `exclude_deleted_users: optional boolean`

  If true, omit rows for deleted accounts. Pages may return fewer than `limit` rows when deleted users were filtered.

- `group_by: optional array of "context_window" or "cost_type" or "inference_geo" or 5 more`

  Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/cost_report` endpoint. The `product`, `model`, `context_window`, `inference_geo`, and `speed` dimensions — and the time bucket, when `bucket_width` is set — count toward `limit`. `cost_type` and `token_type` do not: `cost_type` returns one row per cost component (tokens, web search, code execution); `token_type` returns one row per token type, each with `cost_type: "tokens"`; combining both returns the per-token-type rows plus the web-search and code-execution rows. A page can therefore contain more rows than `limit` when `cost_type` or `token_type` is requested.

  - `"context_window"`

  - `"cost_type"`

  - `"inference_geo"`

  - `"model"`

  - `"product"`

  - `"rbac_group_id"`

  - `"speed"`

  - `"token_type"`

- `inference_geos: optional array of "global" or "not_available" or "us"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"not_available"`

  - `"us"`

- `limit: optional number`

  Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `order: optional "asc" or "desc"`

  Sort direction. Defaults to `desc`.

  - `"asc"`

  - `"desc"`

- `order_by: optional "amount" or "list_amount"`

  Metric to rank actors by. Defaults to `amount`.

  - `"amount"`

  - `"list_amount"`

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it.

- `rbac_group_ids: optional array of string`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

- `speeds: optional array of "fast" or "standard"`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  - `"fast"`

  - `"standard"`

- `user_ids: optional array of string`

  Filter to specific users by tagged user ID.

### Returns

- `UserCost object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { actor, amount, context_window, 12 more }`

    - `actor: AnalyticsUserActor`

      - `user_id: string`

        Tagged user ID.

      - `deleted: optional boolean`

        True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

      - `email: optional string`

        The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

      - `name: optional string`

        The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `amount: string`

      Amount (post-discount, pre-credit) in fractional cents (minor units).

    - `context_window: "0-200k" or "200k-1M"`

      - `"0-200k"`

      - `"200k-1M"`

    - `cost_type: "code_execution" or "tokens" or "web_search"`

      Cost component breakdown; null when returning the combined total.

      - `"code_execution"`

      - `"tokens"`

      - `"web_search"`

    - `currency: "USD"`

      - `"USD"`

    - `ending_at: string`

    - `inference_geo: "global" or "us"`

      - `"global"`

      - `"us"`

    - `list_amount: string`

      List-price amount (pre-discount) in fractional cents.

    - `model: string`

    - `product: string`

      Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

    - `rbac_group_id: string`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

    - `requests: number`

      Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `speed: "fast" or "standard"`

      - `"fast"`

      - `"standard"`

    - `starting_at: string`

    - `token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more`

      Token type when cost_type=tokens; null otherwise.

      - `"cache_creation.ephemeral_1h_input_tokens"`

      - `"cache_creation.ephemeral_5m_input_tokens"`

      - `"cache_read_input_tokens"`

      - `"output_tokens"`

      - `"uncached_input_tokens"`

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/user_cost_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "actor": {
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt",
        "deleted": true,
        "email": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor"
      },
      "amount": "41280.000000",
      "context_window": "0-200k",
      "cost_type": "code_execution",
      "currency": "USD",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "list_amount": "51600.000000",
      "model": "model",
      "product": "product",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "token_type": "cache_creation.ephemeral_1h_input_tokens"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Domain Types

### Cost Bucket

- `CostBucket object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { ending_at, results, starting_at }`

    - `ending_at: string`

    - `results: array of object { amount, context_window, cost_type, 9 more }`

      - `amount: string`

        Amount (post-discount, pre-credit) in fractional cents.

      - `context_window: "0-200k" or "200k-1M"`

        - `"0-200k"`

        - `"200k-1M"`

      - `cost_type: "code_execution" or "tokens" or "web_search"`

        Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).

        - `"code_execution"`

        - `"tokens"`

        - `"web_search"`

      - `currency: "USD"`

        - `"USD"`

      - `inference_geo: "global" or "us"`

        - `"global"`

        - `"us"`

      - `list_amount: string`

        List-price amount (pre-discount) in fractional cents.

      - `model: string`

      - `product: string`

        Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

      - `rbac_group_id: string`

        RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

      - `requests: number`

        Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

      - `speed: "fast" or "standard"`

        - `"fast"`

        - `"standard"`

      - `token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more`

        Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.

        - `"cache_creation.ephemeral_1h_input_tokens"`

        - `"cache_creation.ephemeral_5m_input_tokens"`

        - `"cache_read_input_tokens"`

        - `"output_tokens"`

        - `"uncached_input_tokens"`

    - `starting_at: string`

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

### User Cost

- `UserCost object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { actor, amount, context_window, 12 more }`

    - `actor: AnalyticsUserActor`

      - `user_id: string`

        Tagged user ID.

      - `deleted: optional boolean`

        True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

      - `email: optional string`

        The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

      - `name: optional string`

        The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `amount: string`

      Amount (post-discount, pre-credit) in fractional cents (minor units).

    - `context_window: "0-200k" or "200k-1M"`

      - `"0-200k"`

      - `"200k-1M"`

    - `cost_type: "code_execution" or "tokens" or "web_search"`

      Cost component breakdown; null when returning the combined total.

      - `"code_execution"`

      - `"tokens"`

      - `"web_search"`

    - `currency: "USD"`

      - `"USD"`

    - `ending_at: string`

    - `inference_geo: "global" or "us"`

      - `"global"`

      - `"us"`

    - `list_amount: string`

      List-price amount (pre-discount) in fractional cents.

    - `model: string`

    - `product: string`

      Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

    - `rbac_group_id: string`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

    - `requests: number`

      Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `speed: "fast" or "standard"`

      - `"fast"`

      - `"standard"`

    - `starting_at: string`

    - `token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more`

      Token type when cost_type=tokens; null otherwise.

      - `"cache_creation.ephemeral_1h_input_tokens"`

      - `"cache_creation.ephemeral_5m_input_tokens"`

      - `"cache_read_input_tokens"`

      - `"output_tokens"`

      - `"uncached_input_tokens"`

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

# Users

## List User Activity

**get** `/v1/organizations/analytics/users`

Get per-user activity for a given day, with cursor-based pagination.

Returns activity metrics for each user in the organization, sorted by email
address. Available to organizations on a Claude Enterprise plan. Requires
an API key with the `read:analytics` scope.

### Query Parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get user activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting_date.

- `filter: optional array of string`

  Filters as 'dimension:value', e.g. filter[]=rbac_group_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

- `group_by: optional array of string`

  Dimensions to break results out by, e.g. group_by[]=rbac_group_id. Supported dimensions vary by endpoint; an unsupported dimension returns 400. Grouped responses paginate like ungrouped ones via next_page. rbac_group_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `order: optional "asc" or "desc"`

  Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order_by names a metric (a top-N ranking). Applies to order_by, or to the endpoint's default sort field when order_by is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

### Returns

- `UserActivity object { data, next_page }`

  Response for GET /v1/organizations/analytics/users.

  - `data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 9 more }`

    - `chat_metrics: object { connectors_used_count, distinct_artifacts_created_count, distinct_connectors_used_count, 9 more }`

      Claude.ai activity metrics for a single user on a given day.

      - `connectors_used_count: number`

        Number of MCP connector invocations.

      - `distinct_artifacts_created_count: number`

        Number of distinct artifacts created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_connectors_used_count: number`

        Distinct claude.ai connectors this user used. Excludes calls whose connector could not be identified and all calls from organizations with zero data retention. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_conversation_count: number`

        Number of distinct conversations the user participated in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_files_uploaded_count: number`

        Number of distinct files uploaded. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_projects_created_count: number`

        Number of distinct projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_projects_used_count: number`

        Number of distinct projects used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_shared_artifacts_viewed_count: number`

        Number of distinct shared artifacts the user viewed. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number`

        Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent

      - `shared_conversations_viewed_count: number`

        Number of times the user opened a shared conversation in a project

      - `thinking_message_count: number`

        Number of messages that used extended thinking

    - `claude_code_metrics: object { core_metrics, tool_actions }`

      Claude Code activity metrics for a single user on a given day.

      - `core_metrics: object { commit_count, distinct_session_count, lines_of_code, pull_request_count }`

        Core Claude Code activity metrics for a single user on a given day.

        - `commit_count: number`

          Number of commits made via Claude Code

        - `distinct_session_count: number`

          Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.

        - `lines_of_code: object { added_count, removed_count }`

          Lines of code added and removed via Claude Code.

          - `added_count: number`

            Lines of code added

          - `removed_count: number`

            Lines of code removed

        - `pull_request_count: number`

          Number of pull requests created via Claude Code

      - `tool_actions: object { edit_tool, multi_edit_tool, notebook_edit_tool, write_tool }`

        Per-tool accepted/rejected counts for Claude Code file modification tools.

        - `edit_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

          - `accepted_count: number`

            Number of tool proposals accepted

          - `rejected_count: number`

            Number of tool proposals rejected

        - `multi_edit_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

        - `notebook_edit_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

        - `write_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

    - `cowork_metrics: object { action_count, connectors_used_count, dispatch_turn_count, 13 more }`

      Cowork activity metrics for a single user on a given day.

      - `action_count: number`

        Number of tool actions completed in Cowork sessions

      - `connectors_used_count: number`

        Total number of connector invocations in Cowork sessions

      - `dispatch_turn_count: number`

        Number of Dispatch (background agent) turns completed

      - `distinct_connectors_used_count: number`

        Number of distinct connectors used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number`

        Number of distinct Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number`

        Number of distinct skills used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Cowork sessions

      - `skills_used_count: number`

        Total number of skill invocations in Cowork sessions

      - `distinct_plugins_used_count: optional number`

        Number of distinct plugins used in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `edit_tool_count: optional number`

        Number of successful Edit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

      - `file_edit_count: optional number`

        Number of successful file-edit tool calls (Edit, MultiEdit, Write, NotebookEdit) in Cowork sessions. Null, never 0, while the file-edit metrics are not enabled for this organization.

      - `multi_edit_tool_count: optional number`

        Number of successful MultiEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

      - `notebook_edit_tool_count: optional number`

        Number of successful NotebookEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

      - `plugins_used_count: optional number`

        Total number of plugin invocations in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization.

      - `sessions_with_file_edits_count: optional number`

        Number of distinct Cowork sessions with at least one successful file-edit tool call. Null while the file-edit metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `write_tool_count: optional number`

        Number of successful Write tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `design_metrics: object { distinct_projects_created_count, distinct_projects_used_count, distinct_session_count, message_count }`

      Claude Design activity metrics for a single user on a given day.

      - `distinct_projects_created_count: number`

        Number of distinct Claude Design projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_projects_used_count: number`

        Number of distinct Claude Design projects the user worked in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number`

        Number of distinct Claude Design sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Claude Design sessions

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single user on a given day, broken out by Office product.

      - `excel: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

        - `connectors_used_count: number`

          Number of MCP connector invocations

        - `distinct_connectors_used_count: number`

          Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

        - `distinct_session_count: number`

          Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

        - `distinct_skills_used_count: number`

          Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

        - `message_count: number`

          Number of messages sent

        - `skills_used_count: number`

          Number of skill invocations

      - `outlook: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

      - `powerpoint: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

      - `word: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

    - `science_metrics: object { delegation_count, distinct_session_count, message_count, 2 more }`

      Claude Science activity metrics for a single user on a given day.

      - `delegation_count: number`

        Number of delegations (handoffs to a specialized agent) in Claude Science sessions

      - `distinct_session_count: number`

        Number of distinct Claude Science sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Claude Science sessions

      - `remote_compute_job_count: number`

        Number of remote compute jobs launched from Claude Science sessions

      - `skills_used_count: number`

        Total number of skill invocations in Claude Science sessions

    - `web_search_count: number`

      Number of web searches performed

    - `distinct_user_count: optional number`

      Number of distinct active users represented by this row. Only set for grouped rollups (group_by[]); null for per-user rows. In date-range mode, recomputed as an exact distinct count of the group's active members over the requested window, never a sum of per-day values.

    - `last_activity_date: optional string`

      Most recent UTC day (YYYY-MM-DD) on which the user had any counted activity, within the requested window: equal to the requested date in single-day mode, and to the latest active day in [starting_date, ending_date) in date-range rollup mode — never a day earlier than the window start. On filtered requests (filter[]) only days matching the filter count: with filter[]=rbac_group_id it is the last day the user was active while a member of that group, consistent with the row's other metrics. Null on grouped (group_by[]) rows. Omitted from the response while last-activity reporting is not enabled for this organization.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user: optional AnalyticsUser`

      User identifier.

      - `id: string`

        Tagged user identifier (e.g. user_...)

      - `email_address: string`

        Email address of the user

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/users \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "chat_metrics": {
        "connectors_used_count": 0,
        "distinct_artifacts_created_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_conversation_count": 0,
        "distinct_files_uploaded_count": 0,
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_shared_artifacts_viewed_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "shared_conversations_viewed_count": 0,
        "thinking_message_count": 0
      },
      "claude_code_metrics": {
        "core_metrics": {
          "commit_count": 0,
          "distinct_session_count": 0,
          "lines_of_code": {
            "added_count": 0,
            "removed_count": 0
          },
          "pull_request_count": 0
        },
        "tool_actions": {
          "edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "multi_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "notebook_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "write_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          }
        }
      },
      "cowork_metrics": {
        "action_count": 0,
        "connectors_used_count": 0,
        "dispatch_turn_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_session_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "skills_used_count": 0,
        "distinct_plugins_used_count": 0,
        "edit_tool_count": 0,
        "file_edit_count": 0,
        "multi_edit_tool_count": 0,
        "notebook_edit_tool_count": 0,
        "plugins_used_count": 0,
        "sessions_with_file_edits_count": 0,
        "write_tool_count": 0
      },
      "design_metrics": {
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_session_count": 0,
        "message_count": 0
      },
      "office_metrics": {
        "excel": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "outlook": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "powerpoint": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "word": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        }
      },
      "science_metrics": {
        "delegation_count": 0,
        "distinct_session_count": 0,
        "message_count": 0,
        "remote_compute_job_count": 0,
        "skills_used_count": 0
      },
      "web_search_count": 0,
      "distinct_user_count": 0,
      "last_activity_date": "last_activity_date",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user": {
        "id": "id",
        "email_address": "email_address"
      }
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### User Activity

- `UserActivity object { data, next_page }`

  Response for GET /v1/organizations/analytics/users.

  - `data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 9 more }`

    - `chat_metrics: object { connectors_used_count, distinct_artifacts_created_count, distinct_connectors_used_count, 9 more }`

      Claude.ai activity metrics for a single user on a given day.

      - `connectors_used_count: number`

        Number of MCP connector invocations.

      - `distinct_artifacts_created_count: number`

        Number of distinct artifacts created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_connectors_used_count: number`

        Distinct claude.ai connectors this user used. Excludes calls whose connector could not be identified and all calls from organizations with zero data retention. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_conversation_count: number`

        Number of distinct conversations the user participated in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_files_uploaded_count: number`

        Number of distinct files uploaded. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_projects_created_count: number`

        Number of distinct projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_projects_used_count: number`

        Number of distinct projects used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_shared_artifacts_viewed_count: number`

        Number of distinct shared artifacts the user viewed. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number`

        Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent

      - `shared_conversations_viewed_count: number`

        Number of times the user opened a shared conversation in a project

      - `thinking_message_count: number`

        Number of messages that used extended thinking

    - `claude_code_metrics: object { core_metrics, tool_actions }`

      Claude Code activity metrics for a single user on a given day.

      - `core_metrics: object { commit_count, distinct_session_count, lines_of_code, pull_request_count }`

        Core Claude Code activity metrics for a single user on a given day.

        - `commit_count: number`

          Number of commits made via Claude Code

        - `distinct_session_count: number`

          Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.

        - `lines_of_code: object { added_count, removed_count }`

          Lines of code added and removed via Claude Code.

          - `added_count: number`

            Lines of code added

          - `removed_count: number`

            Lines of code removed

        - `pull_request_count: number`

          Number of pull requests created via Claude Code

      - `tool_actions: object { edit_tool, multi_edit_tool, notebook_edit_tool, write_tool }`

        Per-tool accepted/rejected counts for Claude Code file modification tools.

        - `edit_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

          - `accepted_count: number`

            Number of tool proposals accepted

          - `rejected_count: number`

            Number of tool proposals rejected

        - `multi_edit_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

        - `notebook_edit_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

        - `write_tool: ToolActionCounts`

          Accepted/rejected counts for a single Claude Code tool type.

    - `cowork_metrics: object { action_count, connectors_used_count, dispatch_turn_count, 13 more }`

      Cowork activity metrics for a single user on a given day.

      - `action_count: number`

        Number of tool actions completed in Cowork sessions

      - `connectors_used_count: number`

        Total number of connector invocations in Cowork sessions

      - `dispatch_turn_count: number`

        Number of Dispatch (background agent) turns completed

      - `distinct_connectors_used_count: number`

        Number of distinct connectors used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number`

        Number of distinct Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number`

        Number of distinct skills used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Cowork sessions

      - `skills_used_count: number`

        Total number of skill invocations in Cowork sessions

      - `distinct_plugins_used_count: optional number`

        Number of distinct plugins used in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `edit_tool_count: optional number`

        Number of successful Edit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

      - `file_edit_count: optional number`

        Number of successful file-edit tool calls (Edit, MultiEdit, Write, NotebookEdit) in Cowork sessions. Null, never 0, while the file-edit metrics are not enabled for this organization.

      - `multi_edit_tool_count: optional number`

        Number of successful MultiEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

      - `notebook_edit_tool_count: optional number`

        Number of successful NotebookEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

      - `plugins_used_count: optional number`

        Total number of plugin invocations in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization.

      - `sessions_with_file_edits_count: optional number`

        Number of distinct Cowork sessions with at least one successful file-edit tool call. Null while the file-edit metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `write_tool_count: optional number`

        Number of successful Write tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `design_metrics: object { distinct_projects_created_count, distinct_projects_used_count, distinct_session_count, message_count }`

      Claude Design activity metrics for a single user on a given day.

      - `distinct_projects_created_count: number`

        Number of distinct Claude Design projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_projects_used_count: number`

        Number of distinct Claude Design projects the user worked in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number`

        Number of distinct Claude Design sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Claude Design sessions

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single user on a given day, broken out by Office product.

      - `excel: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

        - `connectors_used_count: number`

          Number of MCP connector invocations

        - `distinct_connectors_used_count: number`

          Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

        - `distinct_session_count: number`

          Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

        - `distinct_skills_used_count: number`

          Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

        - `message_count: number`

          Number of messages sent

        - `skills_used_count: number`

          Number of skill invocations

      - `outlook: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

      - `powerpoint: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

      - `word: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

    - `science_metrics: object { delegation_count, distinct_session_count, message_count, 2 more }`

      Claude Science activity metrics for a single user on a given day.

      - `delegation_count: number`

        Number of delegations (handoffs to a specialized agent) in Claude Science sessions

      - `distinct_session_count: number`

        Number of distinct Claude Science sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Claude Science sessions

      - `remote_compute_job_count: number`

        Number of remote compute jobs launched from Claude Science sessions

      - `skills_used_count: number`

        Total number of skill invocations in Claude Science sessions

    - `web_search_count: number`

      Number of web searches performed

    - `distinct_user_count: optional number`

      Number of distinct active users represented by this row. Only set for grouped rollups (group_by[]); null for per-user rows. In date-range mode, recomputed as an exact distinct count of the group's active members over the requested window, never a sum of per-day values.

    - `last_activity_date: optional string`

      Most recent UTC day (YYYY-MM-DD) on which the user had any counted activity, within the requested window: equal to the requested date in single-day mode, and to the latest active day in [starting_date, ending_date) in date-range rollup mode — never a day earlier than the window start. On filtered requests (filter[]) only days matching the filter count: with filter[]=rbac_group_id it is the last day the user was active while a member of that group, consistent with the row's other metrics. Null on grouped (group_by[]) rows. Omitted from the response while last-activity reporting is not enabled for this organization.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user: optional AnalyticsUser`

      User identifier.

      - `id: string`

        Tagged user identifier (e.g. user_...)

      - `email_address: string`

        Email address of the user

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

# Skills

## Get Skill Usage

**get** `/v1/organizations/analytics/skills`

Get per-skill usage for a given day, with cursor-based pagination.

Returns skill usage metrics for the organization, sorted by skill name.
Available to organizations on a Claude Enterprise plan. Requires an API
key with the `read:analytics` scope.

### Query Parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get skill usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting_date.

- `filter: optional array of string`

  Filters as 'dimension:value', e.g. filter[]=rbac_group_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

- `group_by: optional array of string`

  Dimensions to break results out by, e.g. group_by[]=rbac_group_id. Supported dimensions vary by endpoint; an unsupported dimension returns 400. Grouped responses paginate like ungrouped ones via next_page. rbac_group_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `order: optional "asc" or "desc"`

  Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order_by names a metric (a top-N ranking). Applies to order_by, or to the endpoint's default sort field when order_by is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

### Returns

- `SkillUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/skills.

  - `data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 14 more }`

    - `chat_metrics: object { distinct_conversation_skill_used_count }`

      Claude.ai activity metrics for a single skill on a given day.

      - `distinct_conversation_skill_used_count: number`

        Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `claude_code_metrics: object { distinct_session_skill_used_count }`

      Claude Code activity metrics for a single skill on a given day.

      - `distinct_session_skill_used_count: number`

        Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `cowork_metrics: object { distinct_session_skill_used_count }`

      Cowork activity metrics for a single skill on a given day.

      - `distinct_session_skill_used_count: number`

        Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users who used the skill on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted.

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single skill on a given day, broken out by Office product.

      - `excel: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

        - `distinct_session_skill_used_count: number`

          Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `outlook: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

      - `powerpoint: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

      - `word: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

    - `skill_name: string`

      Name of the skill

    - `attributed_list_price: optional string`

      List-price (rate-card) value of the member requests attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD), from Claude Code, Cowork, and Office Agent request-level attribution — the value of requests that INVOLVED the skill, not the skill's incremental cost. Unlike estimated_overage_spend this reflects usage value regardless of how it was funded — seat-covered usage counts — but it is undiscounted and does NOT tie to billed spend or the organization's spend reporting. claude.ai chat usage carries no request-level attribution and contributes nothing: the field is null on chat product rows and on office_agent product cuts dated before 2026-06-18 (the Office Agent attribution data-start), and on ungrouped rows it covers the Claude Code + Cowork + Office Agent share only (null when no attributable usage exists). Also null under the same conditions as estimated_overage_spend (spend reporting not enabled for this organization, office_agent product cuts before the 2026-06-18 data-start). "0" means attributable usage existed but none was attributed to this skill. Addable across days: date-range rollup mode returns the window's sum. On group_by[] and filter[] shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

    - `currency: optional "USD"`

      Currency for this row's monetary fields (estimated_overage_spend and attributed_list_price), as an uppercase ISO-4217 code. Always "USD" when either amount is populated; null whenever both amounts are null.

      - `"USD"`

    - `enable_count: optional number`

      Distinct accounts that enabled this skill on the requested day (claude.ai only — the skill analog of plugin install_count). The count is org-wide: null when enable reporting is not enabled for this organization, or when the request scopes to user_id / rbac_group_id / product via group_by[] or filter[] (an org-wide count would be misleading on per-cut rows). A distinct count, not an event count: summing across days double-counts members who enable the skill on more than one day, so it is also null in date-range rollup mode (starting_date/ending_date).

    - `estimated_overage_spend: optional string`

      Estimated OVERAGE spend attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD; "1250" is $12.50, fractional cents possible) — an allocation of each member's daily post-discount, pre-credit metered overage spend (the same cost basis as the organization's spend reporting and the Cost & Usage API, so per-skill figures are directly comparable; spend with no skill attribution — including any member-day without skill invocations — is not represented, so skill rows sum to at most those totals) across the skills the member used. Overage only: usage covered by included seat allowances bills nothing and allocates $0 here — see attributed_list_price for the funding-independent usage-value companion. Claude Code, Cowork, and Office Agent spend use request-level skill attribution; claude.ai chat spend is approximated proportionally to skill-invoking messages. An estimate, not a billing number — and the cost of the requests/messages that INVOLVED the skill, not the skill's incremental cost (the same request would still have cost something without the skill active). "0" means no overage spend was attributed; null when spend reporting is not enabled for this organization, on office_agent product cuts dated before 2026-06-18 (the Office Agent attribution data-start). Addable across days: date-range rollup mode (starting_date/ending_date) returns the window's sum. With group_by[]=user_id each row carries the user's own attributed spend. On group_by[] and filter[] shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

    - `invocation_count: optional number`

      Total number of times this skill was invoked on the requested day (the skill analog of plugin invocation_count). Unlike distinct_user_count — which answers '\# of users' — this is the true '# of uses'. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Null when invocation reporting is not enabled for this organization. Sum across a date range for total uses in the window — date-range rollup mode (starting_date/ending_date) returns this sum directly.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `share_status: optional string`

      Skill share status (claude.ai only): one of 'private', 'organization', or 'public'. Null for skills used only in Claude Code or Office (no per-skill share-status concept) and when share-status reporting is not yet available for the organization. Filterable via filter[]=share_status:<value>.

    - `skill_display_name: optional string`

      Human-readable display name for rows whose skill_name is an opaque skill id (user/organization skill types — user-defined names are withheld from the analytics pipeline). Only organization-shared skills resolve; the literal 'unknown' bucket row also gets a fixed 'Unknown skill' label. Null for private (user-defined) skills — their names are not disclosed to analytics-key holders — and null when skill_name is already a display name, when the skill was deleted, or when display-name resolution is not enabled for this organization.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/skills \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "chat_metrics": {
        "distinct_conversation_skill_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_skill_used_count": 0
        },
        "outlook": {
          "distinct_session_skill_used_count": 0
        },
        "powerpoint": {
          "distinct_session_skill_used_count": 0
        },
        "word": {
          "distinct_session_skill_used_count": 0
        }
      },
      "skill_name": "skill_name",
      "attributed_list_price": "attributed_list_price",
      "currency": "USD",
      "enable_count": 0,
      "estimated_overage_spend": "estimated_overage_spend",
      "invocation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "share_status": "share_status",
      "skill_display_name": "skill_display_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Skill Usage

- `SkillUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/skills.

  - `data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 14 more }`

    - `chat_metrics: object { distinct_conversation_skill_used_count }`

      Claude.ai activity metrics for a single skill on a given day.

      - `distinct_conversation_skill_used_count: number`

        Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `claude_code_metrics: object { distinct_session_skill_used_count }`

      Claude Code activity metrics for a single skill on a given day.

      - `distinct_session_skill_used_count: number`

        Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `cowork_metrics: object { distinct_session_skill_used_count }`

      Cowork activity metrics for a single skill on a given day.

      - `distinct_session_skill_used_count: number`

        Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users who used the skill on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted.

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single skill on a given day, broken out by Office product.

      - `excel: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

        - `distinct_session_skill_used_count: number`

          Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `outlook: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

      - `powerpoint: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

      - `word: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

    - `skill_name: string`

      Name of the skill

    - `attributed_list_price: optional string`

      List-price (rate-card) value of the member requests attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD), from Claude Code, Cowork, and Office Agent request-level attribution — the value of requests that INVOLVED the skill, not the skill's incremental cost. Unlike estimated_overage_spend this reflects usage value regardless of how it was funded — seat-covered usage counts — but it is undiscounted and does NOT tie to billed spend or the organization's spend reporting. claude.ai chat usage carries no request-level attribution and contributes nothing: the field is null on chat product rows and on office_agent product cuts dated before 2026-06-18 (the Office Agent attribution data-start), and on ungrouped rows it covers the Claude Code + Cowork + Office Agent share only (null when no attributable usage exists). Also null under the same conditions as estimated_overage_spend (spend reporting not enabled for this organization, office_agent product cuts before the 2026-06-18 data-start). "0" means attributable usage existed but none was attributed to this skill. Addable across days: date-range rollup mode returns the window's sum. On group_by[] and filter[] shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

    - `currency: optional "USD"`

      Currency for this row's monetary fields (estimated_overage_spend and attributed_list_price), as an uppercase ISO-4217 code. Always "USD" when either amount is populated; null whenever both amounts are null.

      - `"USD"`

    - `enable_count: optional number`

      Distinct accounts that enabled this skill on the requested day (claude.ai only — the skill analog of plugin install_count). The count is org-wide: null when enable reporting is not enabled for this organization, or when the request scopes to user_id / rbac_group_id / product via group_by[] or filter[] (an org-wide count would be misleading on per-cut rows). A distinct count, not an event count: summing across days double-counts members who enable the skill on more than one day, so it is also null in date-range rollup mode (starting_date/ending_date).

    - `estimated_overage_spend: optional string`

      Estimated OVERAGE spend attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD; "1250" is $12.50, fractional cents possible) — an allocation of each member's daily post-discount, pre-credit metered overage spend (the same cost basis as the organization's spend reporting and the Cost & Usage API, so per-skill figures are directly comparable; spend with no skill attribution — including any member-day without skill invocations — is not represented, so skill rows sum to at most those totals) across the skills the member used. Overage only: usage covered by included seat allowances bills nothing and allocates $0 here — see attributed_list_price for the funding-independent usage-value companion. Claude Code, Cowork, and Office Agent spend use request-level skill attribution; claude.ai chat spend is approximated proportionally to skill-invoking messages. An estimate, not a billing number — and the cost of the requests/messages that INVOLVED the skill, not the skill's incremental cost (the same request would still have cost something without the skill active). "0" means no overage spend was attributed; null when spend reporting is not enabled for this organization, on office_agent product cuts dated before 2026-06-18 (the Office Agent attribution data-start). Addable across days: date-range rollup mode (starting_date/ending_date) returns the window's sum. With group_by[]=user_id each row carries the user's own attributed spend. On group_by[] and filter[] shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

    - `invocation_count: optional number`

      Total number of times this skill was invoked on the requested day (the skill analog of plugin invocation_count). Unlike distinct_user_count — which answers '\# of users' — this is the true '# of uses'. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Null when invocation reporting is not enabled for this organization. Sum across a date range for total uses in the window — date-range rollup mode (starting_date/ending_date) returns this sum directly.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `share_status: optional string`

      Skill share status (claude.ai only): one of 'private', 'organization', or 'public'. Null for skills used only in Claude Code or Office (no per-skill share-status concept) and when share-status reporting is not yet available for the organization. Filterable via filter[]=share_status:<value>.

    - `skill_display_name: optional string`

      Human-readable display name for rows whose skill_name is an opaque skill id (user/organization skill types — user-defined names are withheld from the analytics pipeline). Only organization-shared skills resolve; the literal 'unknown' bucket row also gets a fixed 'Unknown skill' label. Null for private (user-defined) skills — their names are not disclosed to analytics-key holders — and null when skill_name is already a display name, when the skill was deleted, or when display-name resolution is not enabled for this organization.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

# Connectors

## Get Connector Usage

**get** `/v1/organizations/analytics/connectors`

Get per-connector usage for a given day, with cursor-based pagination.

Returns connector usage metrics for the organization, sorted by connector
name. Connector names are normalized from their various sources — for
example, "Atlassian MCP server" and "mcp-atlassian" both appear as
"atlassian". Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

### Query Parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get connector usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting_date.

- `filter: optional array of string`

  Filters as 'dimension:value', e.g. filter[]=rbac_group_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

- `group_by: optional array of string`

  Dimensions to break results out by, e.g. group_by[]=rbac_group_id. Supported dimensions vary by endpoint; an unsupported dimension returns 400. Grouped responses paginate like ungrouped ones via next_page. rbac_group_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `order: optional "asc" or "desc"`

  Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order_by names a metric (a top-N ranking). Applies to order_by, or to the endpoint's default sort field when order_by is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

### Returns

- `ConnectorUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/connectors.

  - `data: array of object { chat_metrics, claude_code_metrics, connector_name, 10 more }`

    - `chat_metrics: object { distinct_conversation_connector_used_count }`

      Claude.ai activity metrics for a single connector on a given day.

      - `distinct_conversation_connector_used_count: number`

        Number of distinct conversations in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `claude_code_metrics: object { distinct_session_connector_used_count }`

      Claude Code activity metrics for a single connector on a given day.

      - `distinct_session_connector_used_count: number`

        Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `connector_name: string`

      Name of the connector

    - `cowork_metrics: object { distinct_session_connector_used_count }`

      Cowork activity metrics for a single connector on a given day.

      - `distinct_session_connector_used_count: number`

        Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users who used the connector on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single connector on a given day, broken out by Office product.

      - `excel: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

        - `distinct_session_connector_used_count: number`

          Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `outlook: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

      - `powerpoint: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

      - `word: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `read_call_count: optional number`

      Number of connector tool calls on the requested day whose trusted read-only annotation marked them read-only. Call count, not distinct users. Every call recorded on a classified surface lands in exactly one of read_call_count, write_call_count, or unclassified_call_count, so the three sum to the day's classified calls. Classification is forward-only per surface: claude.ai from 2026-06-01, Claude Code from 2026-05-30, Claude in Office from 2026-05-29, Cowork from 2026-06-02 (Cowork clients predating annotation forwarding land in unclassified_call_count). Null, never 0, when the value cannot be stated: the read/write split is not enabled for this organization, or the day predates 2026-05-29. For a date-range total, sum the per-day values, but treat a window that extends before 2026-05-29 as null rather than summing only its covered days — date-range rollup mode (starting_date/ending_date) applies both rules server-side.

    - `unclassified_call_count: optional number`

      Number of connector tool calls on the requested day with no trusted read-only annotation — the annotation is optional in the MCP spec and is discarded when connector access controls are active, so unclassified calls are common. This field shows how much of the day's classified activity the read/write split actually covers. Call count, not distinct users. One of the three call-classification buckets; see read_call_count for the per-surface data-start dates, null conditions, and date-range guidance.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

    - `write_call_count: optional number`

      Number of connector tool calls on the requested day whose trusted read-only annotation marked them not read-only. Call count, not distinct users. One of the three call-classification buckets; see read_call_count for the per-surface data-start dates, null conditions, and date-range guidance.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/connectors \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "chat_metrics": {
        "distinct_conversation_connector_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "connector_name": "connector_name",
      "cowork_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_connector_used_count": 0
        },
        "outlook": {
          "distinct_session_connector_used_count": 0
        },
        "powerpoint": {
          "distinct_session_connector_used_count": 0
        },
        "word": {
          "distinct_session_connector_used_count": 0
        }
      },
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "read_call_count": 0,
      "unclassified_call_count": 0,
      "user_id": "user_id",
      "write_call_count": 0
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Connector Usage

- `ConnectorUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/connectors.

  - `data: array of object { chat_metrics, claude_code_metrics, connector_name, 10 more }`

    - `chat_metrics: object { distinct_conversation_connector_used_count }`

      Claude.ai activity metrics for a single connector on a given day.

      - `distinct_conversation_connector_used_count: number`

        Number of distinct conversations in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `claude_code_metrics: object { distinct_session_connector_used_count }`

      Claude Code activity metrics for a single connector on a given day.

      - `distinct_session_connector_used_count: number`

        Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `connector_name: string`

      Name of the connector

    - `cowork_metrics: object { distinct_session_connector_used_count }`

      Cowork activity metrics for a single connector on a given day.

      - `distinct_session_connector_used_count: number`

        Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users who used the connector on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single connector on a given day, broken out by Office product.

      - `excel: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

        - `distinct_session_connector_used_count: number`

          Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `outlook: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

      - `powerpoint: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

      - `word: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `read_call_count: optional number`

      Number of connector tool calls on the requested day whose trusted read-only annotation marked them read-only. Call count, not distinct users. Every call recorded on a classified surface lands in exactly one of read_call_count, write_call_count, or unclassified_call_count, so the three sum to the day's classified calls. Classification is forward-only per surface: claude.ai from 2026-06-01, Claude Code from 2026-05-30, Claude in Office from 2026-05-29, Cowork from 2026-06-02 (Cowork clients predating annotation forwarding land in unclassified_call_count). Null, never 0, when the value cannot be stated: the read/write split is not enabled for this organization, or the day predates 2026-05-29. For a date-range total, sum the per-day values, but treat a window that extends before 2026-05-29 as null rather than summing only its covered days — date-range rollup mode (starting_date/ending_date) applies both rules server-side.

    - `unclassified_call_count: optional number`

      Number of connector tool calls on the requested day with no trusted read-only annotation — the annotation is optional in the MCP spec and is discarded when connector access controls are active, so unclassified calls are common. This field shows how much of the day's classified activity the read/write split actually covers. Call count, not distinct users. One of the three call-classification buckets; see read_call_count for the per-surface data-start dates, null conditions, and date-range guidance.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

    - `write_call_count: optional number`

      Number of connector tool calls on the requested day whose trusted read-only annotation marked them not read-only. Call count, not distinct users. One of the three call-classification buckets; see read_call_count for the per-surface data-start dates, null conditions, and date-range guidance.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

# Chat Projects

## Get Chat Project Usage

**get** `/v1/organizations/analytics/apps/chat/projects`

Get per-project activity for a given day, with cursor-based pagination.

Returns activity metrics for each project in the organization, sorted by
project ID. Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

### Query Parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get project activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting_date.

- `filter: optional array of string`

  Filters as 'dimension:value', e.g. filter[]=rbac_group_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

- `group_by: optional array of string`

  Dimensions to break results out by, e.g. group_by[]=rbac_group_id. Supported dimensions vary by endpoint; an unsupported dimension returns 400. Grouped responses paginate like ungrouped ones via next_page. rbac_group_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `order: optional "asc" or "desc"`

  Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order_by names a metric (a top-N ranking). Applies to order_by, or to the endpoint's default sort field when order_by is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

### Returns

- `ChatProjectUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/apps/chat/projects.

  - `data: array of object { distinct_user_count, message_count, project_id, 8 more }`

    - `distinct_user_count: number`

      Number of distinct users who used the project on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `message_count: number`

      Number of messages sent in the project on the requested day

    - `project_id: string`

      Tagged project identifier (e.g. claude_proj_...)

    - `project_name: string`

      Name of the project

    - `created_at: optional string`

      Project creation timestamp, RFC 3339. Null if the project was deleted before attribution was recorded.

    - `created_by: optional AnalyticsUser`

      User identifier.

      - `id: string`

        Tagged user identifier (e.g. user_...)

      - `email_address: string`

        Email address of the user

    - `distinct_conversation_count: optional number`

      Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/apps/chat/projects \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "created_at": "created_at",
      "created_by": {
        "id": "id",
        "email_address": "email_address"
      },
      "distinct_conversation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Chat Project Usage

- `ChatProjectUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/apps/chat/projects.

  - `data: array of object { distinct_user_count, message_count, project_id, 8 more }`

    - `distinct_user_count: number`

      Number of distinct users who used the project on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `message_count: number`

      Number of messages sent in the project on the requested day

    - `project_id: string`

      Tagged project identifier (e.g. claude_proj_...)

    - `project_name: string`

      Name of the project

    - `created_at: optional string`

      Project creation timestamp, RFC 3339. Null if the project was deleted before attribution was recorded.

    - `created_by: optional AnalyticsUser`

      User identifier.

      - `id: string`

        Tagged user identifier (e.g. user_...)

      - `email_address: string`

        Email address of the user

    - `distinct_conversation_count: optional number`

      Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

# Plugins

## Get Plugin Usage

**get** `/v1/organizations/analytics/plugins`

Get per-plugin install + invocation usage for a given day, with pagination.

Returns plugin usage metrics for the organization across Cowork and Claude
Code, sorted by plugin name. The `plugin_name` value `third-party` is
an aggregate bucket, not a plugin: it collects plugin activity, from
either surface, for which the reporting client did not provide a plugin
name — so an organization's own plugins can contribute both to their own
named rows and to this bucket. Requires an API key with the
`read:analytics` scope. `starting_date` / `ending_date` select
range-rollup mode like /skills.

### Query Parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get plugin usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with starting_date. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after starting_date.

- `filter: optional array of string`

  Filters as 'dimension:value', e.g. filter[]=rbac_group_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

- `group_by: optional array of string`

  Dimensions to break results out by, e.g. group_by[]=rbac_group_id. Supported dimensions vary by endpoint; an unsupported dimension returns 400. Grouped responses paginate like ungrouped ones via next_page. rbac_group_id attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `order: optional "asc" or "desc"`

  Sort direction: 'asc' or 'desc'. Defaults to 'asc' for the endpoint's sort column and to 'desc' when order_by names a metric (a top-N ranking). Applies to order_by, or to the endpoint's default sort field when order_by is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either date or starting_date, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

### Returns

- `PluginUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/plugins.

  - `data: array of object { claude_code_metrics, cowork_metrics, distinct_user_count, 8 more }`

    - `claude_code_metrics: object { distinct_session_plugin_used_count }`

      Claude Code activity metrics for a single plugin on a given day.

      - `distinct_session_plugin_used_count: number`

        Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

    - `cowork_metrics: object { distinct_session_plugin_used_count }`

      Cowork activity metrics for a single plugin on a given day.

      - `distinct_session_plugin_used_count: number`

        Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users with recorded install or invocation activity for the plugin on the requested day (install-only users count), or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `install_count: number`

      Number of distinct users who installed the plugin on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `invocation_count: number`

      Number of plugin invocations on the requested day

    - `plugin_name: string`

      Name of the plugin

    - `plugin_id: optional string`

      Stable plugin identifier when available (e.g. serena@claude-plugins-official). Null for third-party Claude Code plugins (redacted at the source) and Cowork slash commands that carry only a hashed id.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/plugins \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "claude_code_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "distinct_user_count": 0,
      "install_count": 0,
      "invocation_count": 0,
      "plugin_name": "plugin_name",
      "plugin_id": "plugin_id",
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Plugin Usage

- `PluginUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/plugins.

  - `data: array of object { claude_code_metrics, cowork_metrics, distinct_user_count, 8 more }`

    - `claude_code_metrics: object { distinct_session_plugin_used_count }`

      Claude Code activity metrics for a single plugin on a given day.

      - `distinct_session_plugin_used_count: number`

        Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

    - `cowork_metrics: object { distinct_session_plugin_used_count }`

      Cowork activity metrics for a single plugin on a given day.

      - `distinct_session_plugin_used_count: number`

        Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users with recorded install or invocation activity for the plugin on the requested day (install-only users count), or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `install_count: number`

      Number of distinct users who installed the plugin on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

    - `invocation_count: number`

      Number of plugin invocations on the requested day

    - `plugin_name: string`

      Name of the plugin

    - `plugin_id: optional string`

      Stable plugin identifier when available (e.g. serena@claude-plugins-official). Null for third-party Claude Code plugins (redacted at the source) and Cowork slash commands that carry only a hashed id.

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

# Artifacts

## Get Artifact Activity

**get** `/v1/organizations/analytics/artifacts`

Get artifact-creation activity for a given day, broken out by MIME type.

Returns the full (artifact_type, is_shared) cube for the organization;
`next_page` is null except for grouped queries, which paginate. Requires
an API key with the `read:analytics` scope.

### Query Parameters

- `date: string`

  UTC date in YYYY-MM-DD format. The day to get artifact activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

- `filter: optional array of string`

  Filters as 'dimension:value', e.g. filter[]=rbac_group_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac_group_id accepts the tagged id (rbac_group_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

- `group_by: optional array of string`

  Dimensions to break results out by: user_id and/or rbac_group_id. The ungrouped artifact-type cube is finite and returned in full; grouped queries multiply the cube and paginate via next_page. rbac_group_id attributes a user to every group they held at any point during the requested UTC day, so grouped rows are not an exclusive partition. At most 100 entries.

- `limit: optional number`

  Maximum rows to return (1-1000, default 100). The ungrouped artifact-type cube is finite and returned in full; limit is the page size only when group_by[] multiplies the cube.

- `page: optional string`

  Opaque cursor from a previous response's next_page field. Only valid with group_by[] — the ungrouped cube is never paginated.

### Returns

- `ArtifactUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/artifacts.

  `next_page` is null on ungrouped queries — the artifact-type cube is
  finite and returned in full. Grouped queries (group_by[] on user_id /
  rbac_group_id) multiply the cube and paginate like the other analytics
  list endpoints.

  - `data: array of object { artifact_type, artifacts_created_count, distinct_user_count, 6 more }`

    - `artifact_type: string`

      Canonical artifact MIME type (e.g. text/markdown, application/vnd.ant.react, image/svg+xml), or 'other'.

    - `artifacts_created_count: number`

      Number of artifacts created in this bucket on the requested day

    - `distinct_user_count: number`

      Number of distinct users who created artifacts in this bucket on the requested day

    - `is_shared: boolean`

      Whether the artifacts in this bucket have ever been shared.

    - `published_artifacts_created_count: number`

      Number of those artifacts that have been published

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: optional string`

    Cursor for the next page of a grouped query; always null for the ungrouped artifact-type cube, which is returned in full.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/artifacts \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "artifact_type": "artifact_type",
      "artifacts_created_count": 0,
      "distinct_user_count": 0,
      "is_shared": true,
      "published_artifacts_created_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Artifact Usage

- `ArtifactUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/artifacts.

  `next_page` is null on ungrouped queries — the artifact-type cube is
  finite and returned in full. Grouped queries (group_by[] on user_id /
  rbac_group_id) multiply the cube and paginate like the other analytics
  list endpoints.

  - `data: array of object { artifact_type, artifacts_created_count, distinct_user_count, 6 more }`

    - `artifact_type: string`

      Canonical artifact MIME type (e.g. text/markdown, application/vnd.ant.react, image/svg+xml), or 'other'.

    - `artifacts_created_count: number`

      Number of artifacts created in this bucket on the requested day

    - `distinct_user_count: number`

      Number of distinct users who created artifacts in this bucket on the requested day

    - `is_shared: boolean`

      Whether the artifacts in this bucket have ever been shared.

    - `published_artifacts_created_count: number`

      Number of those artifacts that have been published

    - `product: optional string`

      Product that produced this row's activity: one of chat, claude_code, cowork, or office_agent (the canonical Cost & Usage product naming; an office_agent row's per-surface breakdown is in its office_metrics). On /plugins only cowork and claude_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group_by[] or filter[] there is rejected). Present only when the request grouped by product.

    - `rbac_group_id: optional string`

      Tagged RBAC group identifier (rbac_group_...), matching the spend-limits API spelling. Present only when the request grouped by rbac_group_id.

    - `rbac_group_name: optional string`

      Resolved RBAC group display name, alongside rbac_group_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac_group_id remains the stable key.

    - `user_id: optional string`

      Tagged user identifier (e.g. user_...). Present only when the request grouped by user_id.

  - `next_page: optional string`

    Cursor for the next page of a grouped query; always null for the ungrouped artifact-type cube, which is returned in full.

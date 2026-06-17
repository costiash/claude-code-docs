# Analytics

## Get Activity Summaries

**get** `/v1/organizations/analytics/summaries`

Get organization-wide activity summaries for a date range.

Returns one entry per day in [starting_date, ending_date). Data is
finalized with a 3-day lag: when ending_date is omitted it defaults to
2 days before today, so the last entry covers the most recent day with
finalized data. Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

### Query Parameters

- `starting_date: string`

  UTC date in YYYY-MM-DD format. Start of the date range (inclusive). Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive). Data is finalized with a 3-day lag, so this can be at most 2 days before today — which is also the default when omitted, making the last entry cover the most recent day with finalized data. The range may span at most 366 days.

### Returns

- `ActivitySummary object { summaries }`

  Response for GET /v1/organizations/analytics/summaries.

  - `summaries: array of object { assigned_seat_count, cowork_daily_active_user_count, cowork_monthly_active_user_count, 10 more }`

    - `assigned_seat_count: number`

      Number of seats currently assigned to members

    - `cowork_daily_active_user_count: number`

      Number of users with Cowork activity on the requested day

    - `cowork_monthly_active_user_count: number`

      Number of users with Cowork activity in the 30-day rolling window

    - `cowork_weekly_active_user_count: number`

      Number of users with Cowork activity in the 7-day rolling window

    - `daily_active_user_count: number`

      Number of users with token consumption on the requested day

    - `daily_adoption_rate: number`

      Percentage of assigned seats with activity on the requested day (DAU / assigned_seat_count * 100)

    - `ending_at: string`

      End time in UTC of aggregation period (e.g. 2026-01-16T00:00:00Z)

    - `monthly_active_user_count: number`

      Number of users with token consumption in the 30-day rolling window

    - `monthly_adoption_rate: number`

      Percentage of assigned seats with activity in the 30-day rolling window (MAU / assigned_seat_count * 100)

    - `pending_invite_count: number`

      Number of pending invitations to join the organization

    - `starting_at: string`

      Start time in UTC of aggregation period (e.g. 2026-01-15T00:00:00Z)

    - `weekly_active_user_count: number`

      Number of users with token consumption in the 7-day rolling window

    - `weekly_adoption_rate: number`

      Percentage of assigned seats with activity in the 7-day rolling window (WAU / assigned_seat_count * 100)

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
      "weekly_adoption_rate": 0
    }
  ]
}
```

## Domain Types

### Activity Summary

- `ActivitySummary object { summaries }`

  Response for GET /v1/organizations/analytics/summaries.

  - `summaries: array of object { assigned_seat_count, cowork_daily_active_user_count, cowork_monthly_active_user_count, 10 more }`

    - `assigned_seat_count: number`

      Number of seats currently assigned to members

    - `cowork_daily_active_user_count: number`

      Number of users with Cowork activity on the requested day

    - `cowork_monthly_active_user_count: number`

      Number of users with Cowork activity in the 30-day rolling window

    - `cowork_weekly_active_user_count: number`

      Number of users with Cowork activity in the 7-day rolling window

    - `daily_active_user_count: number`

      Number of users with token consumption on the requested day

    - `daily_adoption_rate: number`

      Percentage of assigned seats with activity on the requested day (DAU / assigned_seat_count * 100)

    - `ending_at: string`

      End time in UTC of aggregation period (e.g. 2026-01-16T00:00:00Z)

    - `monthly_active_user_count: number`

      Number of users with token consumption in the 30-day rolling window

    - `monthly_adoption_rate: number`

      Percentage of assigned seats with activity in the 30-day rolling window (MAU / assigned_seat_count * 100)

    - `pending_invite_count: number`

      Number of pending invitations to join the organization

    - `starting_at: string`

      Start time in UTC of aggregation period (e.g. 2026-01-15T00:00:00Z)

    - `weekly_active_user_count: number`

      Number of users with token consumption in the 7-day rolling window

    - `weekly_adoption_rate: number`

      Percentage of assigned seats with activity in the 7-day rolling window (WAU / assigned_seat_count * 100)

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

    Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

### Office Product Metrics

- `OfficeProductMetrics object { connectors_used_count, distinct_connectors_used_count, distinct_session_count, 3 more }`

  Office Agent activity metrics for a single user on a given day within one Office product.

  - `connectors_used_count: number`

    Number of MCP connector invocations

  - `distinct_connectors_used_count: number`

    Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_session_count: number`

    Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_skills_used_count: number`

    Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

  - `message_count: number`

    Number of messages sent

  - `skills_used_count: number`

    Number of skill invocations

### Skill Office Product Metrics

- `SkillOfficeProductMetrics object { distinct_session_skill_used_count }`

  Office Agent activity metrics for a single skill on a given day within one Office product.

  - `distinct_session_skill_used_count: number`

    Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.

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

- `bucket_width: optional "1m" or "1h" or "1d"`

  Time bucket granularity.

  - `"1m"`

  - `"1h"`

  - `"1d"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `group_by: optional array of "product" or "model" or "context_window" or 2 more`

  Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket).

  - `"product"`

  - `"model"`

  - `"context_window"`

  - `"inference_geo"`

  - `"speed"`

- `inference_geos: optional array of "global" or "us" or "not_available"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"us"`

  - `"not_available"`

- `limit: optional number`

  Maximum number of time buckets per page. Defaults and caps vary by bucket_width (1d: default 7, max 31; 1h: default 24, max 168; 1m: default 60, max 256).

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design".

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

    - `results: array of object { cache_creation, cache_read_input_tokens, context_window, 8 more }`

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

        Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

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
see which users consume the most tokens. Available to organizations on
a Claude Enterprise plan. Requires an API key with the `read:analytics`
scope.

### Query Parameters

- `starting_at: string`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

- `bucket_width: optional "1m" or "1h" or "1d"`

  Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

  - `"1m"`

  - `"1h"`

  - `"1d"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `exclude_deleted_users: optional boolean`

  If true, omit rows for deleted accounts. Pages may return fewer than `limit` rows when deleted users were filtered.

- `group_by: optional array of "product" or "model" or "context_window" or 2 more`

  Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/usage_report` endpoint. `limit` bounds (actor × time bucket × dimension) rows — with dimensions or `bucket_width` present, one actor may span several rows.

  - `"product"`

  - `"model"`

  - `"context_window"`

  - `"inference_geo"`

  - `"speed"`

- `inference_geos: optional array of "global" or "us" or "not_available"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"us"`

  - `"not_available"`

- `limit: optional number`

  Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `order: optional "desc" or "asc"`

  Sort direction. Defaults to `desc`.

  - `"desc"`

  - `"asc"`

- `order_by: optional "output_tokens" or "uncached_input_tokens" or "total_tokens" or "requests"`

  Metric to rank actors by. Defaults to `total_tokens`.

  - `"output_tokens"`

  - `"uncached_input_tokens"`

  - `"total_tokens"`

  - `"requests"`

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design".

- `speeds: optional array of "fast" or "standard"`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  - `"fast"`

  - `"standard"`

- `user_ids: optional array of string`

  Filter to specific users by tagged user ID.

### Returns

- `UserUsage object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { actor, cache_creation, cache_read_input_tokens, 12 more }`

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

      Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

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

    - `results: array of object { cache_creation, cache_read_input_tokens, context_window, 8 more }`

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

        Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

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

  - `data: array of object { actor, cache_creation, cache_read_input_tokens, 12 more }`

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

      Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

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

- `bucket_width: optional "1m" or "1h" or "1d"`

  Time bucket granularity.

  - `"1m"`

  - `"1h"`

  - `"1d"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `group_by: optional array of "product" or "model" or "context_window" or 4 more`

  Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket).

  - `"product"`

  - `"model"`

  - `"context_window"`

  - `"inference_geo"`

  - `"speed"`

  - `"cost_type"`

  - `"token_type"`

- `inference_geos: optional array of "global" or "us" or "not_available"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"us"`

  - `"not_available"`

- `limit: optional number`

  Maximum number of time buckets per page. Defaults and caps vary by bucket_width (1d: default 7, max 31; 1h: default 24, max 168; 1m: default 60, max 256).

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design".

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

    - `results: array of object { amount, context_window, cost_type, 8 more }`

      - `amount: string`

        Amount (post-discount, pre-credit) in fractional cents.

      - `context_window: "0-200k" or "200k-1M"`

        - `"0-200k"`

        - `"200k-1M"`

      - `cost_type: "tokens" or "web_search" or "code_execution"`

        Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).

        - `"tokens"`

        - `"web_search"`

        - `"code_execution"`

      - `currency: "USD"`

        - `"USD"`

      - `inference_geo: "global" or "us"`

        - `"global"`

        - `"us"`

      - `list_amount: string`

        List-price amount (pre-discount) in fractional cents.

      - `model: string`

      - `product: string`

        Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

      - `requests: number`

        Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

      - `speed: "fast" or "standard"`

        - `"fast"`

        - `"standard"`

      - `token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more`

        Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.

        - `"uncached_input_tokens"`

        - `"output_tokens"`

        - `"cache_read_input_tokens"`

        - `"cache_creation.ephemeral_1h_input_tokens"`

        - `"cache_creation.ephemeral_5m_input_tokens"`

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
          "cost_type": "tokens",
          "currency": "USD",
          "inference_geo": "global",
          "list_amount": "list_amount",
          "model": "model",
          "product": "product",
          "requests": 0,
          "speed": "fast",
          "token_type": "uncached_input_tokens"
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
account for the most cost. Available to organizations on a Claude
Enterprise plan. Requires an API key with the `read:analytics` scope.

### Query Parameters

- `starting_at: string`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

- `bucket_width: optional "1m" or "1h" or "1d"`

  Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

  - `"1m"`

  - `"1h"`

  - `"1d"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `exclude_deleted_users: optional boolean`

  If true, omit rows for deleted accounts. Pages may return fewer than `limit` rows when deleted users were filtered.

- `group_by: optional array of "product" or "model" or "context_window" or 4 more`

  Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/cost_report` endpoint. The `product`, `model`, `context_window`, `inference_geo`, and `speed` dimensions — and the time bucket, when `bucket_width` is set — count toward `limit`. `cost_type` and `token_type` do not: `cost_type` returns one row per cost component (tokens, web search, code execution); `token_type` returns one row per token type, each with `cost_type: "tokens"`; combining both returns the per-token-type rows plus the web-search and code-execution rows. A page can therefore contain more rows than `limit` when `cost_type` or `token_type` is requested.

  - `"product"`

  - `"model"`

  - `"context_window"`

  - `"inference_geo"`

  - `"speed"`

  - `"cost_type"`

  - `"token_type"`

- `inference_geos: optional array of "global" or "us" or "not_available"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"us"`

  - `"not_available"`

- `limit: optional number`

  Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `order: optional "desc" or "asc"`

  Sort direction. Defaults to `desc`.

  - `"desc"`

  - `"asc"`

- `order_by: optional "amount" or "list_amount"`

  Metric to rank actors by. Defaults to `amount`.

  - `"amount"`

  - `"list_amount"`

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design".

- `speeds: optional array of "fast" or "standard"`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  - `"fast"`

  - `"standard"`

- `user_ids: optional array of string`

  Filter to specific users by tagged user ID.

### Returns

- `UserCost object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { actor, amount, context_window, 11 more }`

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

    - `cost_type: "tokens" or "web_search" or "code_execution"`

      Cost component breakdown; null when returning the combined total.

      - `"tokens"`

      - `"web_search"`

      - `"code_execution"`

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

      Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

    - `requests: number`

      Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `speed: "fast" or "standard"`

      - `"fast"`

      - `"standard"`

    - `starting_at: string`

    - `token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more`

      Token type when cost_type=tokens; null otherwise.

      - `"uncached_input_tokens"`

      - `"output_tokens"`

      - `"cache_read_input_tokens"`

      - `"cache_creation.ephemeral_1h_input_tokens"`

      - `"cache_creation.ephemeral_5m_input_tokens"`

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
      "cost_type": "tokens",
      "currency": "USD",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "list_amount": "51600.000000",
      "model": "model",
      "product": "product",
      "requests": 128,
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "token_type": "uncached_input_tokens"
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

    - `results: array of object { amount, context_window, cost_type, 8 more }`

      - `amount: string`

        Amount (post-discount, pre-credit) in fractional cents.

      - `context_window: "0-200k" or "200k-1M"`

        - `"0-200k"`

        - `"200k-1M"`

      - `cost_type: "tokens" or "web_search" or "code_execution"`

        Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).

        - `"tokens"`

        - `"web_search"`

        - `"code_execution"`

      - `currency: "USD"`

        - `"USD"`

      - `inference_geo: "global" or "us"`

        - `"global"`

        - `"us"`

      - `list_amount: string`

        List-price amount (pre-discount) in fractional cents.

      - `model: string`

      - `product: string`

        Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

      - `requests: number`

        Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

      - `speed: "fast" or "standard"`

        - `"fast"`

        - `"standard"`

      - `token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more`

        Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.

        - `"uncached_input_tokens"`

        - `"output_tokens"`

        - `"cache_read_input_tokens"`

        - `"cache_creation.ephemeral_1h_input_tokens"`

        - `"cache_creation.ephemeral_5m_input_tokens"`

    - `starting_at: string`

  - `data_refreshed_at: string`

    RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

  - `next_page: string`

  - `organization_id: string`

    ID of the Organization.

### User Cost

- `UserCost object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { actor, amount, context_window, 11 more }`

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

    - `cost_type: "tokens" or "web_search" or "code_execution"`

      Cost component breakdown; null when returning the combined total.

      - `"tokens"`

      - `"web_search"`

      - `"code_execution"`

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

      Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

    - `requests: number`

      Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `speed: "fast" or "standard"`

      - `"fast"`

      - `"standard"`

    - `starting_at: string`

    - `token_type: "uncached_input_tokens" or "output_tokens" or "cache_read_input_tokens" or 2 more`

      Token type when cost_type=tokens; null otherwise.

      - `"uncached_input_tokens"`

      - `"output_tokens"`

      - `"cache_read_input_tokens"`

      - `"cache_creation.ephemeral_1h_input_tokens"`

      - `"cache_creation.ephemeral_5m_input_tokens"`

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

- `date: string`

  UTC date in YYYY-MM-DD format. The day to get user activity for. Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

### Returns

- `UserActivity object { data, next_page }`

  Response for GET /v1/organizations/analytics/users.

  - `data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 4 more }`

    - `chat_metrics: object { connectors_used_count, distinct_artifacts_created_count, distinct_conversation_count, 8 more }`

      Claude.ai activity metrics for a single user on a given day.

      - `connectors_used_count: number`

        Number of MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_artifacts_created_count: number`

        Number of distinct artifacts created

      - `distinct_conversation_count: number`

        Number of distinct conversations the user participated in. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_files_uploaded_count: number`

        Number of distinct files uploaded. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_projects_created_count: number`

        Number of distinct projects created

      - `distinct_projects_used_count: number`

        Number of distinct projects used. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_shared_artifacts_viewed_count: number`

        Number of distinct shared artifacts the user viewed. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number`

        Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

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

          Number of distinct Claude Code sessions. Null on aggregated rows where a distinct count cannot be computed.

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

    - `cowork_metrics: object { action_count, connectors_used_count, dispatch_turn_count, 5 more }`

      Cowork activity metrics for a single user on a given day.

      - `action_count: number`

        Number of tool actions completed in Cowork sessions

      - `connectors_used_count: number`

        Total number of connector invocations in Cowork sessions

      - `dispatch_turn_count: number`

        Number of Dispatch (background agent) turns completed

      - `distinct_connectors_used_count: number`

        Number of distinct connectors used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number`

        Number of distinct Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number`

        Number of distinct skills used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Cowork sessions

      - `skills_used_count: number`

        Total number of skill invocations in Cowork sessions

    - `design_metrics: object { distinct_projects_created_count, distinct_projects_used_count, distinct_session_count, message_count }`

      Claude Design activity metrics for a single user on a given day.

      - `distinct_projects_created_count: number`

        Number of distinct Claude Design projects created

      - `distinct_projects_used_count: number`

        Number of distinct Claude Design projects the user worked in. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number`

        Number of distinct Claude Design sessions. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Claude Design sessions

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single user on a given day, broken out by Office product.

      - `excel: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

        - `connectors_used_count: number`

          Number of MCP connector invocations

        - `distinct_connectors_used_count: number`

          Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

        - `distinct_session_count: number`

          Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.

        - `distinct_skills_used_count: number`

          Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

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

    - `web_search_count: number`

      Number of web searches performed

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
        "skills_used_count": 0
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
      "web_search_count": 0,
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

  - `data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 4 more }`

    - `chat_metrics: object { connectors_used_count, distinct_artifacts_created_count, distinct_conversation_count, 8 more }`

      Claude.ai activity metrics for a single user on a given day.

      - `connectors_used_count: number`

        Number of MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_artifacts_created_count: number`

        Number of distinct artifacts created

      - `distinct_conversation_count: number`

        Number of distinct conversations the user participated in. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_files_uploaded_count: number`

        Number of distinct files uploaded. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_projects_created_count: number`

        Number of distinct projects created

      - `distinct_projects_used_count: number`

        Number of distinct projects used. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_shared_artifacts_viewed_count: number`

        Number of distinct shared artifacts the user viewed. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number`

        Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

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

          Number of distinct Claude Code sessions. Null on aggregated rows where a distinct count cannot be computed.

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

    - `cowork_metrics: object { action_count, connectors_used_count, dispatch_turn_count, 5 more }`

      Cowork activity metrics for a single user on a given day.

      - `action_count: number`

        Number of tool actions completed in Cowork sessions

      - `connectors_used_count: number`

        Total number of connector invocations in Cowork sessions

      - `dispatch_turn_count: number`

        Number of Dispatch (background agent) turns completed

      - `distinct_connectors_used_count: number`

        Number of distinct connectors used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number`

        Number of distinct Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number`

        Number of distinct skills used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Cowork sessions

      - `skills_used_count: number`

        Total number of skill invocations in Cowork sessions

    - `design_metrics: object { distinct_projects_created_count, distinct_projects_used_count, distinct_session_count, message_count }`

      Claude Design activity metrics for a single user on a given day.

      - `distinct_projects_created_count: number`

        Number of distinct Claude Design projects created

      - `distinct_projects_used_count: number`

        Number of distinct Claude Design projects the user worked in. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number`

        Number of distinct Claude Design sessions. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent in Claude Design sessions

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single user on a given day, broken out by Office product.

      - `excel: OfficeProductMetrics`

        Office Agent activity metrics for a single user on a given day within one Office product.

        - `connectors_used_count: number`

          Number of MCP connector invocations

        - `distinct_connectors_used_count: number`

          Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

        - `distinct_session_count: number`

          Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.

        - `distinct_skills_used_count: number`

          Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

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

    - `web_search_count: number`

      Number of web searches performed

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

- `date: string`

  UTC date in YYYY-MM-DD format. The day to get skill usage for. Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

### Returns

- `SkillUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/skills.

  - `data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 3 more }`

    - `chat_metrics: object { distinct_conversation_skill_used_count }`

      Claude.ai activity metrics for a single skill on a given day.

      - `distinct_conversation_skill_used_count: number`

        Number of distinct conversations in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.

    - `claude_code_metrics: object { distinct_session_skill_used_count }`

      Claude Code activity metrics for a single skill on a given day.

      - `distinct_session_skill_used_count: number`

        Number of distinct Claude Code sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.

    - `cowork_metrics: object { distinct_session_skill_used_count }`

      Cowork activity metrics for a single skill on a given day.

      - `distinct_session_skill_used_count: number`

        Number of distinct Cowork sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users who used the skill on the requested day

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single skill on a given day, broken out by Office product.

      - `excel: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

        - `distinct_session_skill_used_count: number`

          Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.

      - `outlook: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

      - `powerpoint: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

      - `word: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

    - `skill_name: string`

      Name of the skill

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
      "skill_name": "skill_name"
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Skill Usage

- `SkillUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/skills.

  - `data: array of object { chat_metrics, claude_code_metrics, cowork_metrics, 3 more }`

    - `chat_metrics: object { distinct_conversation_skill_used_count }`

      Claude.ai activity metrics for a single skill on a given day.

      - `distinct_conversation_skill_used_count: number`

        Number of distinct conversations in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.

    - `claude_code_metrics: object { distinct_session_skill_used_count }`

      Claude Code activity metrics for a single skill on a given day.

      - `distinct_session_skill_used_count: number`

        Number of distinct Claude Code sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.

    - `cowork_metrics: object { distinct_session_skill_used_count }`

      Cowork activity metrics for a single skill on a given day.

      - `distinct_session_skill_used_count: number`

        Number of distinct Cowork sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users who used the skill on the requested day

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single skill on a given day, broken out by Office product.

      - `excel: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

        - `distinct_session_skill_used_count: number`

          Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.

      - `outlook: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

      - `powerpoint: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

      - `word: SkillOfficeProductMetrics`

        Office Agent activity metrics for a single skill on a given day within one Office product.

    - `skill_name: string`

      Name of the skill

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

- `date: string`

  UTC date in YYYY-MM-DD format. The day to get connector usage for. Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

### Returns

- `ConnectorUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/connectors.

  - `data: array of object { chat_metrics, claude_code_metrics, connector_name, 3 more }`

    - `chat_metrics: object { distinct_conversation_connector_used_count }`

      Claude.ai activity metrics for a single connector on a given day.

      - `distinct_conversation_connector_used_count: number`

        Number of distinct conversations in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

    - `claude_code_metrics: object { distinct_session_connector_used_count }`

      Claude Code activity metrics for a single connector on a given day.

      - `distinct_session_connector_used_count: number`

        Number of distinct Claude Code sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

    - `connector_name: string`

      Name of the connector

    - `cowork_metrics: object { distinct_session_connector_used_count }`

      Cowork activity metrics for a single connector on a given day.

      - `distinct_session_connector_used_count: number`

        Number of distinct Cowork sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users who used the connector on the requested day

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single connector on a given day, broken out by Office product.

      - `excel: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

        - `distinct_session_connector_used_count: number`

          Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

      - `outlook: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

      - `powerpoint: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

      - `word: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

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
      }
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Connector Usage

- `ConnectorUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/connectors.

  - `data: array of object { chat_metrics, claude_code_metrics, connector_name, 3 more }`

    - `chat_metrics: object { distinct_conversation_connector_used_count }`

      Claude.ai activity metrics for a single connector on a given day.

      - `distinct_conversation_connector_used_count: number`

        Number of distinct conversations in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

    - `claude_code_metrics: object { distinct_session_connector_used_count }`

      Claude Code activity metrics for a single connector on a given day.

      - `distinct_session_connector_used_count: number`

        Number of distinct Claude Code sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

    - `connector_name: string`

      Name of the connector

    - `cowork_metrics: object { distinct_session_connector_used_count }`

      Cowork activity metrics for a single connector on a given day.

      - `distinct_session_connector_used_count: number`

        Number of distinct Cowork sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_user_count: number`

      Number of distinct users who used the connector on the requested day

    - `office_metrics: object { excel, outlook, powerpoint, word }`

      Office Agent activity metrics for a single connector on a given day, broken out by Office product.

      - `excel: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

        - `distinct_session_connector_used_count: number`

          Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

      - `outlook: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

      - `powerpoint: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

      - `word: ConnectorOfficeProductMetrics`

        Office Agent activity metrics for a single connector on a given day within one Office product.

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

- `date: string`

  UTC date in YYYY-MM-DD format. The day to get project activity for. Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.

- `limit: optional number`

  Number of results per page (1-1000, default 100).

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

### Returns

- `ChatProjectUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/apps/chat/projects.

  - `data: array of object { distinct_conversation_count, distinct_user_count, message_count, 4 more }`

    - `distinct_conversation_count: number`

      Number of distinct conversations in the project on the requested day

    - `distinct_user_count: number`

      Number of distinct users who used the project on the requested day

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
      "distinct_conversation_count": 0,
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "created_at": "created_at",
      "created_by": {
        "id": "id",
        "email_address": "email_address"
      }
    }
  ],
  "next_page": "next_page"
}
```

## Domain Types

### Chat Project Usage

- `ChatProjectUsage object { data, next_page }`

  Response for GET /v1/organizations/analytics/apps/chat/projects.

  - `data: array of object { distinct_conversation_count, distinct_user_count, message_count, 4 more }`

    - `distinct_conversation_count: number`

      Number of distinct conversations in the project on the requested day

    - `distinct_user_count: number`

      Number of distinct users who used the project on the requested day

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

  - `next_page: string`

    Opaque cursor for the next page, or null if no more results

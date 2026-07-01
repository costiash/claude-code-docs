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

  Product surfaces to include. Defaults to all products. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design".

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

      Product surface that produced the usage or cost. Null unless product is in group_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", and "claude_design". Some unattributed usage is reported as "other".

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

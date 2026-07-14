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

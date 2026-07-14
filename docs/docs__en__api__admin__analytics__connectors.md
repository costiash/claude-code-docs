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

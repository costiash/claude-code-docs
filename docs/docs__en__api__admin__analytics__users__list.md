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

  Sort field. Restricted to the endpoint's sort column, plus — in date-range mode (starting_date/ending_date) — the endpoint's rankable metrics (metrics default to descending).

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

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

  - `data: array of object { distinct_user_count, message_count, project_id, 4 more }`

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

    - `distinct_conversation_count: optional number`

      Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

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
      "distinct_conversation_count": 0
    }
  ],
  "next_page": "next_page"
}
```

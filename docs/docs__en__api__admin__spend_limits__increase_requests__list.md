## List Spend Limit Increase Requests

**get** `/v1/organizations/spend_limit_increase_requests`

List spend limit increase requests, most recent first.

Pending requests include a live `spend_summary` for the requester.
Requests whose requester is no longer a member are excluded.

### Query Parameters

- `actor_ids: optional array of string`

  Filter by requester, as `user_...` tagged IDs.

- `limit: optional number`

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

- `status: optional array of "pending" or "approved" or "denied"`

  Filter by status. Omit to return all.

  - `"pending"`

  - `"approved"`

  - `"denied"`

### Returns

- `data: array of SpendLimitIncreaseRequest`

  - `id: string`

  - `actor: object { deleted, email_address, name, 2 more }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `deleted: boolean`

    - `email_address: string`

    - `name: string`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

  - `created_at: string`

  - `period: "monthly" or "daily" or "weekly"`

    - `"monthly"`

    - `"daily"`

    - `"weekly"`

  - `resolved_at: string`

  - `resolved_by: object { deleted, email_address, name, 2 more }  or object { scoped_api_key_id, type }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `UserActor object { deleted, email_address, name, 2 more }`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `deleted: boolean`

      - `email_address: string`

      - `name: string`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

    - `ScopedAPIKeyActor object { scoped_api_key_id, type }`

      A scoped Admin API key acting on behalf of the organization.

      - `scoped_api_key_id: string`

      - `type: "scoped_api_key_actor"`

        - `"scoped_api_key_actor"`

  - `spend_summary: SpendSummary`

    Per-member effective-limit report row (GET /spend_limits/effective).

    - `actor: object { deleted, email_address, name, 2 more }`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `deleted: boolean`

      - `email_address: string`

      - `name: string`

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

    - `amount: string`

    - `currency: string`

    - `period: "monthly" or "daily" or "weekly"`

      - `"monthly"`

      - `"daily"`

      - `"weekly"`

    - `period_to_date_spend: string`

    - `scope: object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

      - `User object { type, user_id }`

        - `type: "user"`

          - `"user"`

        - `user_id: string`

      - `SeatTier object { seat_tier, type }`

        - `seat_tier: string`

        - `type: "seat_tier"`

          - `"seat_tier"`

      - `RbacGroup object { rbac_group_id, type }`

        - `rbac_group_id: string`

        - `type: "rbac_group"`

          - `"rbac_group"`

      - `OrganizationService object { service, type }`

        - `service: string`

        - `type: "organization_service"`

          - `"organization_service"`

      - `Organization object { type }`

        - `type: "organization"`

          - `"organization"`

    - `spend_limit_id: string`

  - `status: "pending" or "approved" or "denied"`

    - `"pending"`

    - `"approved"`

    - `"denied"`

  - `type: "spend_limit_increase_request"`

    - `"spend_limit_increase_request"`

- `next_page: string`

### Example

```http
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_id"
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "period": "monthly",
      "resolved_at": "2019-12-27T18:11:19.117Z",
      "resolved_by": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_id"
      },
      "spend_summary": {
        "actor": {
          "deleted": true,
          "email_address": "email_address",
          "name": "name",
          "type": "user_actor",
          "user_id": "user_id"
        },
        "amount": "50000",
        "currency": "USD",
        "period": "monthly",
        "period_to_date_spend": "period_to_date_spend",
        "scope": {
          "type": "user",
          "user_id": "user_id"
        },
        "source": {
          "type": "user",
          "user_id": "user_id"
        },
        "spend_limit_id": "spend_limit_id"
      },
      "status": "pending",
      "type": "spend_limit_increase_request"
    }
  ],
  "next_page": "next_page"
}
```

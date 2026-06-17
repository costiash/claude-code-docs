## Approve Spend Limit Increase Request

**post** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve`

Approve a pending spend limit increase request.

Writes a per-user spend limit at `amount` for the requester and
transitions the request to `approved`. `period` defaults to the period
the member was blocked on. Anthropic emails the requester unless
`suppress_notification` is set.

### Path Parameters

- `spend_limit_increase_request_id: string`

  ID of the spend limit increase request.

### Body Parameters

- `amount: string`

  New per-user cap as a non-negative integer decimal string (minor units).

- `period: optional "monthly" or "daily" or "weekly"`

  - `"monthly"`

  - `"daily"`

  - `"weekly"`

- `suppress_notification: optional boolean`

### Returns

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

- `spend_limit: SpendLimit`

  - `id: string`

  - `amount: string`

  - `created_at: string`

  - `currency: string`

  - `period: "monthly" or "daily" or "weekly"`

    - `"monthly"`

    - `"daily"`

    - `"weekly"`

  - `scope: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

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

  - `type: "spend_limit"`

    - `"spend_limit"`

  - `updated_at: string`

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

### Example

```http
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/approve \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "amount": "amount"
        }'
```

#### Response

```json
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
  "spend_limit": {
    "id": "id",
    "amount": "amount",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "currency",
    "period": "monthly",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    },
    "type": "spend_limit",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_id"
    },
    "amount": "amount",
    "currency": "currency",
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
```

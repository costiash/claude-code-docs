## Set Spend Limit

**post** `/v1/organizations/spend_limits`

Set a per-user spend limit override.

Upsert keyed on (scope, period): setting a limit that already exists
overwrites it in place. Only `scope.type: "user"` is accepted; seat-tier,
group, and organization-level defaults are configured in claude.ai.

### Body Parameters

- `amount: string`

- `scope: object { type, user_id }`

  - `type: "user"`

    - `"user"`

  - `user_id: string`

- `period: optional "monthly" or "daily" or "weekly"`

  - `"monthly"`

  - `"daily"`

  - `"weekly"`

### Returns

- `SpendLimit object { id, amount, created_at, 5 more }`

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

### Example

```http
curl https://api.anthropic.com/v1/organizations/spend_limits \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "amount": "50000",
          "scope": {
            "type": "user",
            "user_id": "user_id"
          }
        }'
```

#### Response

```json
{
  "id": "id",
  "amount": "50000",
  "created_at": "2019-12-27T18:11:19.117Z",
  "currency": "USD",
  "period": "monthly",
  "scope": {
    "type": "user",
    "user_id": "user_id"
  },
  "type": "spend_limit",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

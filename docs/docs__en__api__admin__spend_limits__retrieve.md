## Get Spend Limit

**get** `/v1/organizations/spend_limits/{spend_limit_id}`

Retrieve a spend limit by ID.

### Path Parameters

- `spend_limit_id: string`

  ID of the Spend Limit.

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
curl https://api.anthropic.com/v1/organizations/spend_limits/$SPEND_LIMIT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
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
}
```

# Rate Limits

## List

**get** `/v1/organizations/rate_limits`

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

### Query Parameters

- `group_type: optional "model_group" or "batch" or "token_count" or 3 more`

  Filter by group type.

  - `"model_group"`

  - `"batch"`

  - `"token_count"`

  - `"files"`

  - `"skills"`

  - `"web_search"`

- `model: optional string`

  Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Returns

- `data: array of object { group_type, limits, models, type }`

  Rate-limit entries for the organization, one per group.

  - `group_type: "model_group" or "batch" or "token_count" or 3 more`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `"model_group"`

    - `"batch"`

    - `"token_count"`

    - `"files"`

    - `"skills"`

    - `"web_search"`

  - `limits: array of object { type, value }`

    The limiter values that apply to this group.

    - `type: string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `value: number`

      The configured limit value for this limiter type.

  - `models: array of string`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `type: "rate_limit"`

    Object type. Always `rate_limit` for organization rate-limit entries.

    - `"rate_limit"`

- `next_page: string`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```http
curl https://api.anthropic.com/v1/organizations/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

## Domain Types

### Rate Limit List Response

- `RateLimitListResponse = object { data, next_page }`

  - `data: array of object { group_type, limits, models, type }`

    Rate-limit entries for the organization, one per group.

    - `group_type: "model_group" or "batch" or "token_count" or 3 more`

      The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

      - `"model_group"`

      - `"batch"`

      - `"token_count"`

      - `"files"`

      - `"skills"`

      - `"web_search"`

    - `limits: array of object { type, value }`

      The limiter values that apply to this group.

      - `type: string`

        The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

      - `value: number`

        The configured limit value for this limiter type.

    - `models: array of string`

      Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

    - `type: "rate_limit"`

      Object type. Always `rate_limit` for organization rate-limit entries.

      - `"rate_limit"`

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

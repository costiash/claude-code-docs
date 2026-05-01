## List

`$ ant beta:user-profiles list`

**get** `/v1/user_profiles`

List User Profiles

### Parameters

- `--limit: optional number`

  Query param: Query parameter for limit

- `--order: optional "asc" or "desc"`

  Query param: Query parameter for order

- `--page: optional string`

  Query param: Query parameter for page

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaListUserProfilesResponse: object { data, next_page }`

  - `data: array of BetaUserProfile`

    User profiles on this page.

    - `id: string`

      Unique identifier for this user profile, prefixed `uprof_`.

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `metadata: map[string]`

      Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

    - `trust_grants: map[BetaUserProfileTrustGrant]`

      Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

      - `status: "active" or "pending" or "rejected"`

        Status of the trust grant.

        - `"active"`

        - `"pending"`

        - `"rejected"`

    - `type: "user_profile"`

      Object type. Always `user_profile`.

      - `"user_profile"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `external_id: optional string`

      Platform's own identifier for this user. Not enforced unique.

  - `next_page: string`

    Cursor for the next page, or `null` when there are no more results.

### Example

```cli
ant beta:user-profiles list \
  --api-key my-anthropic-api-key
```

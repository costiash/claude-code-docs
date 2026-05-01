## Create

`$ ant beta:user-profiles create`

**post** `/v1/user_profiles`

Create User Profile

### Parameters

- `--external-id: optional string`

  Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

- `--metadata: optional map[string]`

  Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_user_profile: object { id, created_at, metadata, 4 more }`

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

### Example

```cli
ant beta:user-profiles create \
  --api-key my-anthropic-api-key
```

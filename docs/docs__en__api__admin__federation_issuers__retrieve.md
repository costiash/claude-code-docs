## Get Federation Issuer

**get** `/v1/organizations/federation_issuers/{federation_issuer_id}`

Retrieve a federation issuer by its ID (`fdis_...`).

### Path Parameters

- `federation_issuer_id: string`

  ID of the federation issuer.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `FederationIssuer object { id, archived_at, archived_by_actor_id, 12 more }`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string`

    If set, all rules referencing this issuer reject token exchange.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: object { type, ca_cert_pem, discovery_base }  or object { type, url, ca_cert_pem }  or object { keys, type }`

    How signing keys are obtained for signature verification.

    - `Discovery object { type, ca_cert_pem, discovery_base }`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

        - `"discovery"`

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      - `discovery_base: optional string`

        Set when the discovery URL differs from `issuer_url`.

    - `ExplicitURL object { type, url, ca_cert_pem }`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

        - `"explicit_url"`

      - `url: string`

        JWKS endpoint.

      - `ca_cert_pem: optional string`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

    - `Inline object { keys, type }`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

      - `type: "inline"`

        - `"inline"`

  - `jwks_polling_disabled_at: string`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: object { consecutive_failures, last_fetched_at, next_poll_at }`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string`

      When the last successful fetch completed.

    - `next_poll_at: string`

      When the next fetch is scheduled. Null if paused.

  - `type: "federation_issuer"`

    - `"federation_issuer"`

  - `updated_at: string`

    When this issuer was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

### Example

```http
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

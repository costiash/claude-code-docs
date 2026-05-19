# MCP Tunnels

## Retrieve

**get** `/v1/organizations/tunnels/{tunnel_id}`

Retrieve a single tunnel in the caller's organization by ID.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `id: string`

  ID of the Tunnel.

- `archived_at: string`

  RFC 3339 datetime string indicating when the Tunnel was archived, or
  `null` if it is not archived.

- `created_at: string`

  RFC 3339 datetime string indicating when the Tunnel was created.

- `display_name: string`

  Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

- `domain: string`

  Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
  subdomain of this value are routed through the Tunnel. Globally unique and
  never reused, even after the Tunnel is archived.

- `type: "tunnel"`

  Object type. Always `tunnel` for Tunnels.

  - `"tunnel"`

- `workspace_id: string`

  ID of the Workspace this Tunnel belongs to, or `null` for the default
  Workspace. Immutable after creation.

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
```

## List

**get** `/v1/organizations/tunnels`

List the organization's tunnels.

Results span the caller's organization, ordered by creation time
(newest first). Use `workspace_id` to filter to a single workspace;
archived tunnels are excluded unless `include_archived` is set.

### Query Parameters

- `include_archived: optional boolean`

  Include archived tunnels in the results. Archived tunnels are excluded by
  default.

- `limit: optional number`

  Maximum number of tunnels to return in a single page.

- `page: optional string`

  Opaque pagination cursor from a previous response's `next_page`. Omit to
  fetch the first page.

- `workspace_id: optional string`

  Return only tunnels in this Workspace. Accepts a `wrkspc_`-prefixed
  Workspace ID; omit to list tunnels across all Workspaces.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `data: array of object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Tunnel was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Tunnel was created.

  - `display_name: string`

    Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

  - `domain: string`

    Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
    subdomain of this value are routed through the Tunnel. Globally unique and
    never reused, even after the Tunnel is archived.

  - `type: "tunnel"`

    Object type. Always `tunnel` for Tunnels.

    - `"tunnel"`

  - `workspace_id: string`

    ID of the Workspace this Tunnel belongs to, or `null` for the default
    Workspace. Immutable after creation.

- `next_page: string`

  Opaque cursor for the next page, or `null` if there are no more results.

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
```

## Reveal Token

**post** `/v1/organizations/tunnels/{tunnel_id}/reveal_token`

Return the tunnel's current connection token.

The value is fetched live on each call; Anthropic does not store it.
Repeated calls return the same value until the token is rotated.
Exposed as `POST` so the token does not appear in intermediary
access logs.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `id: string`

  Stable identifier for the current token value. Changes when the token is
  rotated.

- `tunnel_token: string`

  The tunnel's connection token.

- `type: "tunnel_token"`

  Object type. Always `tunnel_token` for Tunnel Tokens.

  - `"tunnel_token"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/reveal_token \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
```

## Rotate Token

**post** `/v1/organizations/tunnels/{tunnel_id}/rotate_token`

Invalidate the tunnel's current token for new connections and return a fresh value.

Established connections are not severed by rotation; a connector
restarted after rotation must use the new value. An optional
`reason` is captured for operational context.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Body Parameters

- `reason: optional string`

  Optional free-text reason for the rotation, recorded for audit.

### Returns

- `id: string`

  Stable identifier for the current token value. Changes when the token is
  rotated.

- `tunnel_token: string`

  The tunnel's connection token.

- `type: "tunnel_token"`

  Object type. Always `tunnel_token` for Tunnel Tokens.

  - `"tunnel_token"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/rotate_token \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
```

## Archive

**post** `/v1/organizations/tunnels/{tunnel_id}/archive`

Archive a tunnel. Archival is irreversible.

Every non-archived certificate on the tunnel is archived in the same
operation, the hostname is retired and never re-allocated, and the
tunnel token is invalidated. Retrying against an already-archived
tunnel returns the existing record unchanged.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `id: string`

  ID of the Tunnel.

- `archived_at: string`

  RFC 3339 datetime string indicating when the Tunnel was archived, or
  `null` if it is not archived.

- `created_at: string`

  RFC 3339 datetime string indicating when the Tunnel was created.

- `display_name: string`

  Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

- `domain: string`

  Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
  subdomain of this value are routed through the Tunnel. Globally unique and
  never reused, even after the Tunnel is archived.

- `type: "tunnel"`

  Object type. Always `tunnel` for Tunnels.

  - `"tunnel"`

- `workspace_id: string`

  ID of the Workspace this Tunnel belongs to, or `null` for the default
  Workspace. Immutable after creation.

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
```

## Domain Types

### MCP Tunnel Retrieve Response

- `MCPTunnelRetrieveResponse = object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Tunnel was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Tunnel was created.

  - `display_name: string`

    Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

  - `domain: string`

    Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
    subdomain of this value are routed through the Tunnel. Globally unique and
    never reused, even after the Tunnel is archived.

  - `type: "tunnel"`

    Object type. Always `tunnel` for Tunnels.

    - `"tunnel"`

  - `workspace_id: string`

    ID of the Workspace this Tunnel belongs to, or `null` for the default
    Workspace. Immutable after creation.

### MCP Tunnel List Response

- `MCPTunnelListResponse = object { data, next_page }`

  - `data: array of object { id, archived_at, created_at, 4 more }`

    - `id: string`

      ID of the Tunnel.

    - `archived_at: string`

      RFC 3339 datetime string indicating when the Tunnel was archived, or
      `null` if it is not archived.

    - `created_at: string`

      RFC 3339 datetime string indicating when the Tunnel was created.

    - `display_name: string`

      Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

    - `domain: string`

      Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
      subdomain of this value are routed through the Tunnel. Globally unique and
      never reused, even after the Tunnel is archived.

    - `type: "tunnel"`

      Object type. Always `tunnel` for Tunnels.

      - `"tunnel"`

    - `workspace_id: string`

      ID of the Workspace this Tunnel belongs to, or `null` for the default
      Workspace. Immutable after creation.

  - `next_page: string`

    Opaque cursor for the next page, or `null` if there are no more results.

### MCP Tunnel Reveal Token Response

- `MCPTunnelRevealTokenResponse = object { id, tunnel_token, type }`

  - `id: string`

    Stable identifier for the current token value. Changes when the token is
    rotated.

  - `tunnel_token: string`

    The tunnel's connection token.

  - `type: "tunnel_token"`

    Object type. Always `tunnel_token` for Tunnel Tokens.

    - `"tunnel_token"`

### MCP Tunnel Rotate Token Response

- `MCPTunnelRotateTokenResponse = object { id, tunnel_token, type }`

  - `id: string`

    Stable identifier for the current token value. Changes when the token is
    rotated.

  - `tunnel_token: string`

    The tunnel's connection token.

  - `type: "tunnel_token"`

    Object type. Always `tunnel_token` for Tunnel Tokens.

    - `"tunnel_token"`

### MCP Tunnel Archive Response

- `MCPTunnelArchiveResponse = object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the Tunnel was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Tunnel was created.

  - `display_name: string`

    Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

  - `domain: string`

    Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
    subdomain of this value are routed through the Tunnel. Globally unique and
    never reused, even after the Tunnel is archived.

  - `type: "tunnel"`

    Object type. Always `tunnel` for Tunnels.

    - `"tunnel"`

  - `workspace_id: string`

    ID of the Workspace this Tunnel belongs to, or `null` for the default
    Workspace. Immutable after creation.

# Tunnel Certificates

## Create

**post** `/v1/organizations/tunnels/{tunnel_id}/certificates`

Register a public CA certificate for the tunnel.

Anthropic verifies the gateway's server certificate against this CA
when it terminates the inner TLS session. The PEM body must contain
exactly one X.509 certificate and no private-key material. A tunnel
holds at most two non-archived certificates.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Body Parameters

- `ca_certificate_pem: string`

  PEM-encoded X.509 CA certificate. Must contain exactly one certificate and
  no private-key material.

### Returns

- `id: string`

  ID of the Tunnel Certificate.

- `archived_at: string`

  RFC 3339 datetime string indicating when the certificate was archived, or
  `null` if it is not archived.

- `created_at: string`

  RFC 3339 datetime string indicating when the certificate was registered.

- `expires_at: string`

  RFC 3339 datetime string indicating when the certificate expires, or
  `null` if it does not expire.

- `fingerprint: string`

  The certificate's SHA-256 fingerprint, as a lowercase hex string.

- `tunnel_id: string`

  ID of the Tunnel this certificate is registered against.

- `type: "tunnel_certificate"`

  Object type. Always `tunnel_certificate` for Tunnel Certificates.

  - `"tunnel_certificate"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN" \
    -d '{
          "ca_certificate_pem": "-----BEGIN CERTIFICATE-----\\nMIIBexampleEXAMPLEexampleEXAMPLEexampleEXAMPLEexampleEXAMPLEexa\\n...illustrative placeholder, not a real certificate...\\n-----END CERTIFICATE-----\\n"
        }'
```

## Retrieve

**get** `/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}`

Retrieve a single certificate registered on a tunnel by ID.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

- `certificate_id: string`

  ID of the Tunnel Certificate.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `id: string`

  ID of the Tunnel Certificate.

- `archived_at: string`

  RFC 3339 datetime string indicating when the certificate was archived, or
  `null` if it is not archived.

- `created_at: string`

  RFC 3339 datetime string indicating when the certificate was registered.

- `expires_at: string`

  RFC 3339 datetime string indicating when the certificate expires, or
  `null` if it does not expire.

- `fingerprint: string`

  The certificate's SHA-256 fingerprint, as a lowercase hex string.

- `tunnel_id: string`

  ID of the Tunnel this certificate is registered against.

- `type: "tunnel_certificate"`

  Object type. Always `tunnel_certificate` for Tunnel Certificates.

  - `"tunnel_certificate"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates/$CERTIFICATE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
```

## List

**get** `/v1/organizations/tunnels/{tunnel_id}/certificates`

List the certificates registered on a tunnel.

Archived certificates are excluded unless `include_archived` is set.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Query Parameters

- `include_archived: optional boolean`

  Include archived certificates in the results. Archived certificates are
  excluded by default.

- `limit: optional number`

  Maximum number of certificates to return.

- `page: optional string`

  A tunnel has at most two active certificates, so this list is not
  paginated.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `data: array of object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    - `"tunnel_certificate"`

- `next_page: string`

  Opaque cursor for the next page, or `null` if there are no more results.

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
```

## Archive

**post** `/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

Archive a certificate, removing it from the set Anthropic trusts for this tunnel.

The certificate record is retained. Archiving the last non-archived
certificate is permitted; the tunnel rejects MCP traffic until a new
certificate is added.

### Path Parameters

- `tunnel_id: string`

  ID of the Tunnel.

- `certificate_id: string`

  ID of the Tunnel Certificate.

### Header Parameters

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

  - `"mcp-tunnels-2026-05-19"`

### Returns

- `id: string`

  ID of the Tunnel Certificate.

- `archived_at: string`

  RFC 3339 datetime string indicating when the certificate was archived, or
  `null` if it is not archived.

- `created_at: string`

  RFC 3339 datetime string indicating when the certificate was registered.

- `expires_at: string`

  RFC 3339 datetime string indicating when the certificate expires, or
  `null` if it does not expire.

- `fingerprint: string`

  The certificate's SHA-256 fingerprint, as a lowercase hex string.

- `tunnel_id: string`

  ID of the Tunnel this certificate is registered against.

- `type: "tunnel_certificate"`

  Object type. Always `tunnel_certificate` for Tunnel Certificates.

  - `"tunnel_certificate"`

### Example

```http
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates/$CERTIFICATE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_WIF_BEARER_TOKEN"
```

## Domain Types

### Tunnel Certificate Create Response

- `TunnelCertificateCreateResponse = object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    - `"tunnel_certificate"`

### Tunnel Certificate Retrieve Response

- `TunnelCertificateRetrieveResponse = object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    - `"tunnel_certificate"`

### Tunnel Certificate List Response

- `TunnelCertificateListResponse = object { data, next_page }`

  - `data: array of object { id, archived_at, created_at, 4 more }`

    - `id: string`

      ID of the Tunnel Certificate.

    - `archived_at: string`

      RFC 3339 datetime string indicating when the certificate was archived, or
      `null` if it is not archived.

    - `created_at: string`

      RFC 3339 datetime string indicating when the certificate was registered.

    - `expires_at: string`

      RFC 3339 datetime string indicating when the certificate expires, or
      `null` if it does not expire.

    - `fingerprint: string`

      The certificate's SHA-256 fingerprint, as a lowercase hex string.

    - `tunnel_id: string`

      ID of the Tunnel this certificate is registered against.

    - `type: "tunnel_certificate"`

      Object type. Always `tunnel_certificate` for Tunnel Certificates.

      - `"tunnel_certificate"`

  - `next_page: string`

    Opaque cursor for the next page, or `null` if there are no more results.

### Tunnel Certificate Archive Response

- `TunnelCertificateArchiveResponse = object { id, archived_at, created_at, 4 more }`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    - `"tunnel_certificate"`

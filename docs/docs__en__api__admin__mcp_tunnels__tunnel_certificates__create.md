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

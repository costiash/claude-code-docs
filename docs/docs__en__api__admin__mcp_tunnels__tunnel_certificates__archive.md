## Archive Tunnel Certificate

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
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "type": "tunnel_certificate"
}
```

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

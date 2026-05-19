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

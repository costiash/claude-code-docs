## List Tunnels

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Query Parameters

- `include_archived: optional boolean`

  Whether to include archived tunnels in the results. Defaults to false.

- `limit: optional number`

  Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

- `page: optional string`

  Opaque pagination cursor from a previous `list_tunnels` response.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"fallback-credit-2026-06-01"`

### Returns

- `data: array of BetaTunnel`

  List of tunnels, ordered by created_at descending.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

    - `"tunnel"`

- `next_page: string`

  Pagination cursor for the next page, or null if no more results.

### Example

```http
curl https://api.anthropic.com/v1/tunnels \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: mcp-tunnels-2026-06-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "display_name": "display_name",
      "domain": "domain",
      "type": "tunnel"
    }
  ],
  "next_page": "next_page"
}
```

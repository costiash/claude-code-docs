## List

**get** `/v1/environments`

List environments with pagination support.

### Query Parameters

- `include_archived: optional boolean`

  Include archived environments in the response

- `limit: optional number`

  Maximum number of environments to return

- `page: optional string`

  Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 18 more`

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

### Cookie Parameters

- `sessionKey: optional string`

### Returns

- `data: array of BetaEnvironment`

  List of environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig`

    `cloud` environment configuration.

    - `networking: BetaUnrestrictedNetwork or BetaLimitedNetwork`

      Network configuration policy.

      - `BetaUnrestrictedNetwork = object { type }`

        Unrestricted network access.

        - `type: "unrestricted"`

          Network policy type

          - `"unrestricted"`

      - `BetaLimitedNetwork = object { allow_mcp_servers, allow_package_managers, allowed_hosts, type }`

        Limited network access.

        - `allow_mcp_servers: boolean`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

        - `allow_package_managers: boolean`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

        - `allowed_hosts: array of string`

          Specifies domains the container can reach.

        - `type: "limited"`

          Network policy type

          - `"limited"`

    - `packages: BetaPackages`

      Package manager configuration.

      - `apt: array of string`

        Ubuntu/Debian packages to install

      - `cargo: array of string`

        Rust packages to install

      - `gem: array of string`

        Ruby packages to install

      - `go: array of string`

        Go packages to install

      - `npm: array of string`

        Node.js packages to install

      - `pip: array of string`

        Python packages to install

      - `type: optional "packages"`

        Package configuration type

        - `"packages"`

    - `type: "cloud"`

      Environment type

      - `"cloud"`

  - `created_at: string`

    RFC 3339 timestamp when environment was created

  - `description: string`

    User-provided description for the environment

  - `metadata: map[string]`

    User-provided metadata key-value pairs

  - `name: string`

    Human-readable name for the environment

  - `type: "environment"`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: string`

    RFC 3339 timestamp when environment was last updated

- `next_page: string`

  Token for fetching the next page of results. If `null`, there are no more results available. Pass this value to the `page` parameter in the next request.

### Example

```http
curl https://api.anthropic.com/v1/environments \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## List

`$ ant beta:environments list`

**get** `/v1/environments`

List environments with pagination support.

### Parameters

- `--include-archived: optional boolean`

  Query param: Include archived environments in the response

- `--limit: optional number`

  Query param: Maximum number of environments to return

- `--page: optional string`

  Query param: Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaEnvironmentListResponse: object { data, next_page }`

  Response when listing environments.

  This response model uses opaque cursor-based pagination. Use the `page`
  query parameter with the value from `next_page` to fetch the next page.

  - `data: array of BetaEnvironment`

    List of environments.

    - `id: string`

      Environment identifier (e.g., 'env_...')

    - `archived_at: string`

      RFC 3339 timestamp when environment was archived, or null if not archived

    - `config: object { networking, packages, type }`

      `cloud` environment configuration.

      - `networking: BetaUnrestrictedNetwork or BetaLimitedNetwork`

        Network configuration policy.

        - `beta_unrestricted_network: object { type }`

          Unrestricted network access.

          - `type: "unrestricted"`

            Network policy type

        - `beta_limited_network: object { allow_mcp_servers, allow_package_managers, allowed_hosts, type }`

          Limited network access.

          - `allow_mcp_servers: boolean`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `allow_package_managers: boolean`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `allowed_hosts: array of string`

            Specifies domains the container can reach.

          - `type: "limited"`

            Network policy type

      - `packages: object { apt, cargo, gem, 4 more }`

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

    - `updated_at: string`

      RFC 3339 timestamp when environment was last updated

  - `next_page: string`

    Token for fetching the next page of results. If `null`, there are no more results available. Pass this value to the `page` parameter in the next request.

### Example

```cli
ant beta:environments list \
  --api-key my-anthropic-api-key
```

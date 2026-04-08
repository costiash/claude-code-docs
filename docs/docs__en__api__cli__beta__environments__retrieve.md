## Retrieve

`$ ant beta:environments retrieve`

**get** `/v1/environments/{environment_id}`

Retrieve a specific environment by ID.

### Parameters

- `--environment-id: string`

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_environment: object { id, archived_at, config, 6 more }`

  Unified Environment resource for both cloud and BYOC environments.

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

### Example

```cli
ant beta:environments retrieve \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

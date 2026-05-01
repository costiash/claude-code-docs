## List

`beta.environments.list(**kwargs) -> PageCursor<BetaEnvironment>`

**get** `/v1/environments`

List environments with pagination support.

### Parameters

- `include_archived: bool`

  Include archived environments in the response

- `limit: Integer`

  Maximum number of environments to return

- `page: String`

  Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 20 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

### Returns

- `class BetaEnvironment`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: String`

    Environment identifier (e.g., 'env_...')

  - `archived_at: String`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig`

    `cloud` environment configuration.

    - `networking: BetaUnrestrictedNetwork | BetaLimitedNetwork`

      Network configuration policy.

      - `class BetaUnrestrictedNetwork`

        Unrestricted network access.

        - `type: :unrestricted`

          Network policy type

          - `:unrestricted`

      - `class BetaLimitedNetwork`

        Limited network access.

        - `allow_mcp_servers: bool`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

        - `allow_package_managers: bool`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

        - `allowed_hosts: Array[String]`

          Specifies domains the container can reach.

        - `type: :limited`

          Network policy type

          - `:limited`

    - `packages: BetaPackages`

      Package manager configuration.

      - `apt: Array[String]`

        Ubuntu/Debian packages to install

      - `cargo: Array[String]`

        Rust packages to install

      - `gem_: Array[String]`

        Ruby packages to install

      - `go: Array[String]`

        Go packages to install

      - `npm: Array[String]`

        Node.js packages to install

      - `pip: Array[String]`

        Python packages to install

      - `type: :packages`

        Package configuration type

        - `:packages`

    - `type: :cloud`

      Environment type

      - `:cloud`

  - `created_at: String`

    RFC 3339 timestamp when environment was created

  - `description: String`

    User-provided description for the environment

  - `metadata: Hash[Symbol, String]`

    User-provided metadata key-value pairs

  - `name: String`

    Human-readable name for the environment

  - `type: :environment`

    The type of object (always 'environment')

    - `:environment`

  - `updated_at: String`

    RFC 3339 timestamp when environment was last updated

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.environments.list

puts(page)
```

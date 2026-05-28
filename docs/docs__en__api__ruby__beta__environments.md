# Environments

## Create Environment

`beta.environments.create(**kwargs) -> BetaEnvironment`

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `name: String`

  Human-readable name for the environment

- `config: BetaCloudConfigParams | BetaSelfHostedConfigParams`

  Environment configuration

  - `class BetaCloudConfigParams`

    Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

    - `type: :cloud`

      Environment type

      - `:cloud`

    - `networking: BetaUnrestrictedNetwork | BetaLimitedNetworkParams`

      Network configuration policy. Omit on update to preserve the existing value.

      - `class BetaUnrestrictedNetwork`

        Unrestricted network access.

        - `type: :unrestricted`

          Network policy type

          - `:unrestricted`

      - `class BetaLimitedNetworkParams`

        Limited network request params.

        Fields default to null; on update, omitted fields preserve the
        existing value.

        - `type: :limited`

          Network policy type

          - `:limited`

        - `allow_mcp_servers: bool`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allow_package_managers: bool`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allowed_hosts: Array[String]`

          Specifies domains the container can reach.

    - `packages: BetaPackagesParams`

      Specify packages (and optionally their versions) available in this environment.

      When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

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

  - `class BetaSelfHostedConfigParams`

    Request params for `self_hosted` environment configuration.

    - `type: :self_hosted`

      Environment type

      - `:self_hosted`

- `description: String`

  Optional description of the environment

- `metadata: Hash[Symbol, String]`

  User-provided metadata key-value pairs

- `scope: :organization | :account`

  The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. Only applicable for self-hosted environments. If not specified, defaults based on organization type.

  - `:organization`

  - `:account`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

### Returns

- `class BetaEnvironment`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: String`

    Environment identifier (e.g., 'env_...')

  - `archived_at: String`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig | BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig`

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

    - `class BetaSelfHostedConfig`

      Configuration for self-hosted environments.

      - `type: :self_hosted`

        Environment type

        - `:self_hosted`

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

  - `scope: :organization | :account`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `:organization`

    - `:account`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_environment = anthropic.beta.environments.create(name: "python-data-analysis")

puts(beta_environment)
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## List Environments

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

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

### Returns

- `class BetaEnvironment`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: String`

    Environment identifier (e.g., 'env_...')

  - `archived_at: String`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig | BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig`

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

    - `class BetaSelfHostedConfig`

      Configuration for self-hosted environments.

      - `type: :self_hosted`

        Environment type

        - `:self_hosted`

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

  - `scope: :organization | :account`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `:organization`

    - `:account`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.environments.list

puts(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "archived_at": null,
      "config": {
        "networking": {
          "allow_mcp_servers": false,
          "allow_package_managers": true,
          "allowed_hosts": [
            "api.example.com"
          ],
          "type": "limited"
        },
        "packages": {
          "apt": [
            "string"
          ],
          "cargo": [
            "string"
          ],
          "gem": [
            "string"
          ],
          "go": [
            "string"
          ],
          "npm": [
            "string"
          ],
          "pip": [
            "pandas",
            "numpy"
          ],
          "type": "packages"
        },
        "type": "cloud"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Python environment with data-analysis packages.",
      "metadata": {},
      "name": "python-data-analysis",
      "type": "environment",
      "updated_at": "2026-03-15T10:00:00Z",
      "scope": "organization"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Environment

`beta.environments.retrieve(environment_id, **kwargs) -> BetaEnvironment`

**get** `/v1/environments/{environment_id}`

Retrieve a specific environment by ID.

### Parameters

- `environment_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

### Returns

- `class BetaEnvironment`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: String`

    Environment identifier (e.g., 'env_...')

  - `archived_at: String`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig | BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig`

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

    - `class BetaSelfHostedConfig`

      Configuration for self-hosted environments.

      - `type: :self_hosted`

        Environment type

        - `:self_hosted`

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

  - `scope: :organization | :account`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `:organization`

    - `:account`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_environment = anthropic.beta.environments.retrieve("env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_environment)
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Update Environment

`beta.environments.update(environment_id, **kwargs) -> BetaEnvironment`

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `environment_id: String`

- `config: BetaCloudConfigParams | BetaSelfHostedConfigParams`

  Updated environment configuration

  - `class BetaCloudConfigParams`

    Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

    - `type: :cloud`

      Environment type

      - `:cloud`

    - `networking: BetaUnrestrictedNetwork | BetaLimitedNetworkParams`

      Network configuration policy. Omit on update to preserve the existing value.

      - `class BetaUnrestrictedNetwork`

        Unrestricted network access.

        - `type: :unrestricted`

          Network policy type

          - `:unrestricted`

      - `class BetaLimitedNetworkParams`

        Limited network request params.

        Fields default to null; on update, omitted fields preserve the
        existing value.

        - `type: :limited`

          Network policy type

          - `:limited`

        - `allow_mcp_servers: bool`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allow_package_managers: bool`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allowed_hosts: Array[String]`

          Specifies domains the container can reach.

    - `packages: BetaPackagesParams`

      Specify packages (and optionally their versions) available in this environment.

      When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

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

  - `class BetaSelfHostedConfigParams`

    Request params for `self_hosted` environment configuration.

    - `type: :self_hosted`

      Environment type

      - `:self_hosted`

- `description: String`

  Updated description of the environment

- `metadata: Hash[Symbol, String]`

  User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

- `name: String`

  Updated name for the environment

- `scope: :organization | :account`

  The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only.

  - `:organization`

  - `:account`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

### Returns

- `class BetaEnvironment`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: String`

    Environment identifier (e.g., 'env_...')

  - `archived_at: String`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig | BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig`

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

    - `class BetaSelfHostedConfig`

      Configuration for self-hosted environments.

      - `type: :self_hosted`

        Environment type

        - `:self_hosted`

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

  - `scope: :organization | :account`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `:organization`

    - `:account`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_environment = anthropic.beta.environments.update("env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_environment)
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Delete Environment

`beta.environments.delete(environment_id, **kwargs) -> BetaEnvironmentDeleteResponse`

**delete** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Parameters

- `environment_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

### Returns

- `class BetaEnvironmentDeleteResponse`

  Response after deleting an environment.

  - `id: String`

    Environment identifier

  - `type: :environment_deleted`

    The type of response

    - `:environment_deleted`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_environment_delete_response = anthropic.beta.environments.delete("env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_environment_delete_response)
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```

## Archive Environment

`beta.environments.archive(environment_id, **kwargs) -> BetaEnvironment`

**post** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Parameters

- `environment_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

### Returns

- `class BetaEnvironment`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: String`

    Environment identifier (e.g., 'env_...')

  - `archived_at: String`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig | BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig`

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

    - `class BetaSelfHostedConfig`

      Configuration for self-hosted environments.

      - `type: :self_hosted`

        Environment type

        - `:self_hosted`

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

  - `scope: :organization | :account`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `:organization`

    - `:account`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_environment = anthropic.beta.environments.archive("env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_environment)
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Domain Types

### Beta Cloud Config

- `class BetaCloudConfig`

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

### Beta Cloud Config Params

- `class BetaCloudConfigParams`

  Request params for `cloud` environment configuration.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `type: :cloud`

    Environment type

    - `:cloud`

  - `networking: BetaUnrestrictedNetwork | BetaLimitedNetworkParams`

    Network configuration policy. Omit on update to preserve the existing value.

    - `class BetaUnrestrictedNetwork`

      Unrestricted network access.

      - `type: :unrestricted`

        Network policy type

        - `:unrestricted`

    - `class BetaLimitedNetworkParams`

      Limited network request params.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `type: :limited`

        Network policy type

        - `:limited`

      - `allow_mcp_servers: bool`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `allow_package_managers: bool`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `allowed_hosts: Array[String]`

        Specifies domains the container can reach.

  - `packages: BetaPackagesParams`

    Specify packages (and optionally their versions) available in this environment.

    When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

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

### Beta Environment

- `class BetaEnvironment`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: String`

    Environment identifier (e.g., 'env_...')

  - `archived_at: String`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig | BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig`

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

    - `class BetaSelfHostedConfig`

      Configuration for self-hosted environments.

      - `type: :self_hosted`

        Environment type

        - `:self_hosted`

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

  - `scope: :organization | :account`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `:organization`

    - `:account`

### Beta Environment Delete Response

- `class BetaEnvironmentDeleteResponse`

  Response after deleting an environment.

  - `id: String`

    Environment identifier

  - `type: :environment_deleted`

    The type of response

    - `:environment_deleted`

### Beta Limited Network

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

### Beta Limited Network Params

- `class BetaLimitedNetworkParams`

  Limited network request params.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `type: :limited`

    Network policy type

    - `:limited`

  - `allow_mcp_servers: bool`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `allow_package_managers: bool`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `allowed_hosts: Array[String]`

    Specifies domains the container can reach.

### Beta Packages

- `class BetaPackages`

  Packages (and their versions) available in this environment.

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

### Beta Packages Params

- `class BetaPackagesParams`

  Specify packages (and optionally their versions) available in this environment.

  When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

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

### Beta Self Hosted Config

- `class BetaSelfHostedConfig`

  Configuration for self-hosted environments.

  - `type: :self_hosted`

    Environment type

    - `:self_hosted`

### Beta Self Hosted Config Params

- `class BetaSelfHostedConfigParams`

  Request params for `self_hosted` environment configuration.

  - `type: :self_hosted`

    Environment type

    - `:self_hosted`

### Beta Unrestricted Network

- `class BetaUnrestrictedNetwork`

  Unrestricted network access.

  - `type: :unrestricted`

    Network policy type

    - `:unrestricted`

# Work

## Get Work Item

`beta.environments.work.retrieve(work_id, **kwargs) -> BetaSelfHostedWork`

**get** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

### Parameters

- `environment_id: String`

- `work_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

### Returns

- `class BetaSelfHostedWork`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: String`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: String`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: String`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: String`

      Session identifier (e.g., 'session_...')

    - `type: :session`

      Type of work data

      - `:session`

  - `environment_id: String`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: String`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Hash[Symbol, String]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: String`

    RFC 3339 timestamp when work execution started

  - `state: :queued | :starting | :active | 2 more`

    Current state of the work item

    - `:queued`

    - `:starting`

    - `:active`

    - `:stopping`

    - `:stopped`

  - `stop_requested_at: String`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: String`

    RFC 3339 timestamp when work execution stopped

  - `type: :work`

    The type of object (always 'work')

    - `:work`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_self_hosted_work = anthropic.beta.environments.work.retrieve("work_id", environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_self_hosted_work)
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Poll for Work

`beta.environments.work.poll(environment_id, **kwargs) -> BetaSelfHostedWork`

**get** `/v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

### Parameters

- `environment_id: String`

- `block_ms: Integer`

  How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

- `reclaim_older_than_ms: Integer`

  Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

- `anthropic_worker_id: String`

  Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

### Returns

- `class BetaSelfHostedWork`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: String`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: String`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: String`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: String`

      Session identifier (e.g., 'session_...')

    - `type: :session`

      Type of work data

      - `:session`

  - `environment_id: String`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: String`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Hash[Symbol, String]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: String`

    RFC 3339 timestamp when work execution started

  - `state: :queued | :starting | :active | 2 more`

    Current state of the work item

    - `:queued`

    - `:starting`

    - `:active`

    - `:stopping`

    - `:stopped`

  - `stop_requested_at: String`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: String`

    RFC 3339 timestamp when work execution stopped

  - `type: :work`

    The type of object (always 'work')

    - `:work`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_self_hosted_work = anthropic.beta.environments.work.poll("env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_self_hosted_work)
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Acknowledge Work

`beta.environments.work.ack(work_id, **kwargs) -> BetaSelfHostedWork`

**post** `/v1/environments/{environment_id}/work/{work_id}/ack`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Acknowledge receipt of a work item, transitioning it from 'queued' to 'starting' and removing it from the queue.

### Parameters

- `environment_id: String`

- `work_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

### Returns

- `class BetaSelfHostedWork`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: String`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: String`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: String`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: String`

      Session identifier (e.g., 'session_...')

    - `type: :session`

      Type of work data

      - `:session`

  - `environment_id: String`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: String`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Hash[Symbol, String]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: String`

    RFC 3339 timestamp when work execution started

  - `state: :queued | :starting | :active | 2 more`

    Current state of the work item

    - `:queued`

    - `:starting`

    - `:active`

    - `:stopping`

    - `:stopped`

  - `stop_requested_at: String`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: String`

    RFC 3339 timestamp when work execution stopped

  - `type: :work`

    The type of object (always 'work')

    - `:work`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_self_hosted_work = anthropic.beta.environments.work.ack("work_id", environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_self_hosted_work)
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Record Heartbeat

`beta.environments.work.heartbeat(work_id, **kwargs) -> BetaSelfHostedWorkHeartbeatResponse`

**post** `/v1/environments/{environment_id}/work/{work_id}/heartbeat`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

### Parameters

- `environment_id: String`

- `work_id: String`

- `desired_ttl_seconds: Integer`

  Desired TTL in seconds

- `expected_last_heartbeat: String`

  Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

### Returns

- `class BetaSelfHostedWorkHeartbeatResponse`

  Response after recording a heartbeat for a work item.

  - `last_heartbeat: String`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `lease_extended: bool`

    Whether the heartbeat succeeded in extending the lease

  - `state: :queued | :starting | :active | 2 more`

    Current state of the work item (active/stopping/stopped)

    - `:queued`

    - `:starting`

    - `:active`

    - `:stopping`

    - `:stopped`

  - `ttl_seconds: Integer`

    Effective TTL applied to the lease

  - `type: :work_heartbeat`

    The type of response

    - `:work_heartbeat`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_self_hosted_work_heartbeat_response = anthropic.beta.environments.work.heartbeat("work_id", environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_self_hosted_work_heartbeat_response)
```

#### Response

```json
{
  "last_heartbeat": "last_heartbeat",
  "lease_extended": true,
  "state": "queued",
  "ttl_seconds": 0,
  "type": "work_heartbeat"
}
```

## Stop Work

`beta.environments.work.stop(work_id, **kwargs) -> BetaSelfHostedWork`

**post** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

### Parameters

- `environment_id: String`

- `work_id: String`

- `force: bool`

  If true, immediately stop work without graceful shutdown

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

### Returns

- `class BetaSelfHostedWork`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: String`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: String`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: String`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: String`

      Session identifier (e.g., 'session_...')

    - `type: :session`

      Type of work data

      - `:session`

  - `environment_id: String`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: String`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Hash[Symbol, String]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: String`

    RFC 3339 timestamp when work execution started

  - `state: :queued | :starting | :active | 2 more`

    Current state of the work item

    - `:queued`

    - `:starting`

    - `:active`

    - `:stopping`

    - `:stopped`

  - `stop_requested_at: String`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: String`

    RFC 3339 timestamp when work execution stopped

  - `type: :work`

    The type of object (always 'work')

    - `:work`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_self_hosted_work = anthropic.beta.environments.work.stop("work_id", environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_self_hosted_work)
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## List Work Items

`beta.environments.work.list(environment_id, **kwargs) -> PageCursor<BetaSelfHostedWork>`

**get** `/v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

### Parameters

- `environment_id: String`

- `limit: Integer`

  Maximum number of work items to return

- `page: String`

  Opaque cursor from previous response for pagination

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

### Returns

- `class BetaSelfHostedWork`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: String`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: String`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: String`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: String`

      Session identifier (e.g., 'session_...')

    - `type: :session`

      Type of work data

      - `:session`

  - `environment_id: String`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: String`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Hash[Symbol, String]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: String`

    RFC 3339 timestamp when work execution started

  - `state: :queued | :starting | :active | 2 more`

    Current state of the work item

    - `:queued`

    - `:starting`

    - `:active`

    - `:stopping`

    - `:stopped`

  - `stop_requested_at: String`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: String`

    RFC 3339 timestamp when work execution stopped

  - `type: :work`

    The type of object (always 'work')

    - `:work`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.environments.work.list("env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "acknowledged_at": "acknowledged_at",
      "created_at": "created_at",
      "data": {
        "id": "id",
        "type": "session"
      },
      "environment_id": "environment_id",
      "latest_heartbeat_at": "latest_heartbeat_at",
      "metadata": {
        "foo": "string"
      },
      "started_at": "started_at",
      "state": "queued",
      "stop_requested_at": "stop_requested_at",
      "stopped_at": "stopped_at",
      "type": "work"
    }
  ],
  "next_page": "next_page"
}
```

## Update Work Item

`beta.environments.work.update(work_id, **kwargs) -> BetaSelfHostedWork`

**post** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

### Parameters

- `environment_id: String`

- `work_id: String`

- `metadata: Hash[Symbol, String]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

### Returns

- `class BetaSelfHostedWork`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: String`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: String`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: String`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: String`

      Session identifier (e.g., 'session_...')

    - `type: :session`

      Type of work data

      - `:session`

  - `environment_id: String`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: String`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Hash[Symbol, String]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: String`

    RFC 3339 timestamp when work execution started

  - `state: :queued | :starting | :active | 2 more`

    Current state of the work item

    - `:queued`

    - `:starting`

    - `:active`

    - `:stopping`

    - `:stopped`

  - `stop_requested_at: String`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: String`

    RFC 3339 timestamp when work execution stopped

  - `type: :work`

    The type of object (always 'work')

    - `:work`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_self_hosted_work = anthropic.beta.environments.work.update(
  "work_id",
  environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW",
  metadata: {foo: "string"}
)

puts(beta_self_hosted_work)
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Get Queue Statistics

`beta.environments.work.stats(environment_id, **kwargs) -> BetaSelfHostedWorkQueueStats`

**get** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

### Parameters

- `environment_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 23 more`

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

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"thinking-token-count-2026-05-13"`

### Returns

- `class BetaSelfHostedWorkQueueStats`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `depth: Integer`

    Number of work items waiting to be picked up (lag from consumer group)

  - `oldest_queued_at: String`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `pending: Integer`

    Number of work items being processed (polled but not acknowledged)

  - `type: :work_queue_stats`

    The type of object

    - `:work_queue_stats`

  - `workers_polling: Integer`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_self_hosted_work_queue_stats = anthropic.beta.environments.work.stats("env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_self_hosted_work_queue_stats)
```

#### Response

```json
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```

## Domain Types

### Beta Self Hosted Work

- `class BetaSelfHostedWork`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: String`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: String`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: String`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: String`

      Session identifier (e.g., 'session_...')

    - `type: :session`

      Type of work data

      - `:session`

  - `environment_id: String`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: String`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Hash[Symbol, String]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: String`

    RFC 3339 timestamp when work execution started

  - `state: :queued | :starting | :active | 2 more`

    Current state of the work item

    - `:queued`

    - `:starting`

    - `:active`

    - `:stopping`

    - `:stopped`

  - `stop_requested_at: String`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: String`

    RFC 3339 timestamp when work execution stopped

  - `type: :work`

    The type of object (always 'work')

    - `:work`

### Beta Self Hosted Work Heartbeat Response

- `class BetaSelfHostedWorkHeartbeatResponse`

  Response after recording a heartbeat for a work item.

  - `last_heartbeat: String`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `lease_extended: bool`

    Whether the heartbeat succeeded in extending the lease

  - `state: :queued | :starting | :active | 2 more`

    Current state of the work item (active/stopping/stopped)

    - `:queued`

    - `:starting`

    - `:active`

    - `:stopping`

    - `:stopped`

  - `ttl_seconds: Integer`

    Effective TTL applied to the lease

  - `type: :work_heartbeat`

    The type of response

    - `:work_heartbeat`

### Beta Self Hosted Work List Response

- `class BetaSelfHostedWorkListResponse`

  Response when listing work items with cursor-based pagination.

  - `data: Array[BetaSelfHostedWork]`

    List of work items

    - `id: String`

      Work identifier (e.g., 'work_...')

    - `acknowledged_at: String`

      RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

    - `created_at: String`

      RFC 3339 timestamp when work was created

    - `data: BetaSessionWorkData`

      The actual work to be performed

      - `id: String`

        Session identifier (e.g., 'session_...')

      - `type: :session`

        Type of work data

        - `:session`

    - `environment_id: String`

      Environment identifier this work belongs to (e.g., `env_...`)

    - `latest_heartbeat_at: String`

      RFC 3339 timestamp of the most recent heartbeat

    - `metadata: Hash[Symbol, String]`

      User-provided metadata key-value pairs associated with this work item

    - `started_at: String`

      RFC 3339 timestamp when work execution started

    - `state: :queued | :starting | :active | 2 more`

      Current state of the work item

      - `:queued`

      - `:starting`

      - `:active`

      - `:stopping`

      - `:stopped`

    - `stop_requested_at: String`

      RFC 3339 timestamp when stop was requested

    - `stopped_at: String`

      RFC 3339 timestamp when work execution stopped

    - `type: :work`

      The type of object (always 'work')

      - `:work`

  - `next_page: String`

    Opaque cursor for fetching the next page of results

### Beta Self Hosted Work Queue Stats

- `class BetaSelfHostedWorkQueueStats`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `depth: Integer`

    Number of work items waiting to be picked up (lag from consumer group)

  - `oldest_queued_at: String`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `pending: Integer`

    Number of work items being processed (polled but not acknowledged)

  - `type: :work_queue_stats`

    The type of object

    - `:work_queue_stats`

  - `workers_polling: Integer`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Beta Self Hosted Work Stop Request

- `class BetaSelfHostedWorkStopRequest`

  Request to stop a work item.

  - `force: bool`

    If true, immediately stop work without graceful shutdown

### Beta Self Hosted Work Update Request

- `class BetaSelfHostedWorkUpdateRequest`

  Request to update work item metadata.

  - `metadata: Hash[Symbol, String]`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

### Beta Session Work Data

- `class BetaSessionWorkData`

  Work data for session work items.

  This resource type is used when work represents a session that needs to be executed
  in a self-hosted environment.

  - `id: String`

    Session identifier (e.g., 'session_...')

  - `type: :session`

    Type of work data

    - `:session`

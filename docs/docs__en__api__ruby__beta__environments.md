# Environments

## Create

`beta.environments.create(**kwargs) -> BetaEnvironment`

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `name: String`

  Human-readable name for the environment

- `config: BetaCloudConfigParams`

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

- `description: String`

  Optional description of the environment

- `metadata: Hash[Symbol, String]`

  User-provided metadata key-value pairs

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

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

### Returns

- `class BetaEnvironment`

  Unified Environment resource for both cloud and BYOC environments.

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

beta_environment = anthropic.beta.environments.create(name: "python-data-analysis")

puts(beta_environment)
```

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

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

### Returns

- `class BetaEnvironment`

  Unified Environment resource for both cloud and BYOC environments.

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

## Retrieve

`beta.environments.retrieve(environment_id, **kwargs) -> BetaEnvironment`

**get** `/v1/environments/{environment_id}`

Retrieve a specific environment by ID.

### Parameters

- `environment_id: String`

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

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

### Returns

- `class BetaEnvironment`

  Unified Environment resource for both cloud and BYOC environments.

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

beta_environment = anthropic.beta.environments.retrieve("env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_environment)
```

## Update

`beta.environments.update(environment_id, **kwargs) -> BetaEnvironment`

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `environment_id: String`

- `config: BetaCloudConfigParams`

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

- `description: String`

  Updated description of the environment

- `metadata: Hash[Symbol, String]`

  User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

- `name: String`

  Updated name for the environment

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

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

### Returns

- `class BetaEnvironment`

  Unified Environment resource for both cloud and BYOC environments.

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

beta_environment = anthropic.beta.environments.update("env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_environment)
```

## Delete

`beta.environments.delete(environment_id, **kwargs) -> BetaEnvironmentDeleteResponse`

**delete** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Parameters

- `environment_id: String`

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

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

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

## Archive

`beta.environments.archive(environment_id, **kwargs) -> BetaEnvironment`

**post** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Parameters

- `environment_id: String`

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

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

### Returns

- `class BetaEnvironment`

  Unified Environment resource for both cloud and BYOC environments.

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

beta_environment = anthropic.beta.environments.archive("env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_environment)
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

  Unified Environment resource for both cloud and BYOC environments.

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

### Beta Unrestricted Network

- `class BetaUnrestrictedNetwork`

  Unrestricted network access.

  - `type: :unrestricted`

    Network policy type

    - `:unrestricted`

# Environments

## Create

`$ ant beta:environments create`

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `--name: string`

  Body param: Human-readable name for the environment

- `--config: optional BetaCloudConfigParams or BetaSelfHostedConfigParams`

  Body param: Environment configuration

- `--description: optional string`

  Body param: Optional description of the environment

- `--metadata: optional map[string]`

  Body param: User-provided metadata key-value pairs

- `--scope: optional "organization" or "account"`

  Body param: The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. Only applicable for self-hosted environments. If not specified, defaults based on organization type.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_environment: object { id, archived_at, config, 7 more }`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig or BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `beta_cloud_config: object { networking, packages, type }`

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

    - `beta_self_hosted_config: object { type }`

      Configuration for self-hosted environments.

      - `type: "self_hosted"`

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

  - `scope: optional "organization" or "account"`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```cli
ant beta:environments create \
  --api-key my-anthropic-api-key \
  --name python-data-analysis
```

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

    - `config: BetaCloudConfig or BetaSelfHostedConfig`

      Environment configuration (either Anthropic Cloud or self-hosted)

      - `beta_cloud_config: object { networking, packages, type }`

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

      - `beta_self_hosted_config: object { type }`

        Configuration for self-hosted environments.

        - `type: "self_hosted"`

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

    - `scope: optional "organization" or "account"`

      The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

      - `"organization"`

      - `"account"`

  - `next_page: string`

    Token for fetching the next page of results. If `null`, there are no more results available. Pass this value to the `page` parameter in the next request.

### Example

```cli
ant beta:environments list \
  --api-key my-anthropic-api-key
```

## Retrieve

`$ ant beta:environments retrieve`

**get** `/v1/environments/{environment_id}`

Retrieve a specific environment by ID.

### Parameters

- `--environment-id: string`

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_environment: object { id, archived_at, config, 7 more }`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig or BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `beta_cloud_config: object { networking, packages, type }`

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

    - `beta_self_hosted_config: object { type }`

      Configuration for self-hosted environments.

      - `type: "self_hosted"`

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

  - `scope: optional "organization" or "account"`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```cli
ant beta:environments retrieve \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

## Update

`$ ant beta:environments update`

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `--environment-id: string`

  Path param

- `--config: optional BetaCloudConfigParams or BetaSelfHostedConfigParams`

  Body param: Updated environment configuration

- `--description: optional string`

  Body param: Updated description of the environment

- `--metadata: optional map[string]`

  Body param: User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

- `--name: optional string`

  Body param: Updated name for the environment

- `--scope: optional "organization" or "account"`

  Body param: The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_environment: object { id, archived_at, config, 7 more }`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig or BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `beta_cloud_config: object { networking, packages, type }`

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

    - `beta_self_hosted_config: object { type }`

      Configuration for self-hosted environments.

      - `type: "self_hosted"`

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

  - `scope: optional "organization" or "account"`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```cli
ant beta:environments update \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

## Delete

`$ ant beta:environments delete`

**delete** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Parameters

- `--environment-id: string`

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_environment_delete_response: object { id, type }`

  Response after deleting an environment.

  - `id: string`

    Environment identifier

  - `type: "environment_deleted"`

    The type of response

### Example

```cli
ant beta:environments delete \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

## Archive

`$ ant beta:environments archive`

**post** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Parameters

- `--environment-id: string`

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_environment: object { id, archived_at, config, 7 more }`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig or BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `beta_cloud_config: object { networking, packages, type }`

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

    - `beta_self_hosted_config: object { type }`

      Configuration for self-hosted environments.

      - `type: "self_hosted"`

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

  - `scope: optional "organization" or "account"`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```cli
ant beta:environments archive \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

## Domain Types

### Beta Cloud Config

- `beta_cloud_config: object { networking, packages, type }`

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

### Beta Cloud Config Params

- `beta_cloud_config_params: object { type, networking, packages }`

  Request params for `cloud` environment configuration.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `type: "cloud"`

    Environment type

  - `networking: optional BetaUnrestrictedNetwork or BetaLimitedNetworkParams`

    Network configuration policy. Omit on update to preserve the existing value.

    - `beta_unrestricted_network: object { type }`

      Unrestricted network access.

      - `type: "unrestricted"`

        Network policy type

    - `beta_limited_network_params: object { type, allow_mcp_servers, allow_package_managers, allowed_hosts }`

      Limited network request params.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `type: "limited"`

        Network policy type

      - `allow_mcp_servers: optional boolean`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `allow_package_managers: optional boolean`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `allowed_hosts: optional array of string`

        Specifies domains the container can reach.

  - `packages: optional object { apt, cargo, gem, 4 more }`

    Specify packages (and optionally their versions) available in this environment.

    When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

    - `apt: optional array of string`

      Ubuntu/Debian packages to install

    - `cargo: optional array of string`

      Rust packages to install

    - `gem: optional array of string`

      Ruby packages to install

    - `go: optional array of string`

      Go packages to install

    - `npm: optional array of string`

      Node.js packages to install

    - `pip: optional array of string`

      Python packages to install

    - `type: optional "packages"`

      Package configuration type

      - `"packages"`

### Beta Environment

- `beta_environment: object { id, archived_at, config, 7 more }`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig or BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `beta_cloud_config: object { networking, packages, type }`

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

    - `beta_self_hosted_config: object { type }`

      Configuration for self-hosted environments.

      - `type: "self_hosted"`

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

  - `scope: optional "organization" or "account"`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Beta Environment Delete Response

- `beta_environment_delete_response: object { id, type }`

  Response after deleting an environment.

  - `id: string`

    Environment identifier

  - `type: "environment_deleted"`

    The type of response

### Beta Limited Network

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

### Beta Limited Network Params

- `beta_limited_network_params: object { type, allow_mcp_servers, allow_package_managers, allowed_hosts }`

  Limited network request params.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `type: "limited"`

    Network policy type

  - `allow_mcp_servers: optional boolean`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `allow_package_managers: optional boolean`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `allowed_hosts: optional array of string`

    Specifies domains the container can reach.

### Beta Packages

- `beta_packages: object { apt, cargo, gem, 4 more }`

  Packages (and their versions) available in this environment.

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

### Beta Packages Params

- `beta_packages_params: object { apt, cargo, gem, 4 more }`

  Specify packages (and optionally their versions) available in this environment.

  When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

  - `apt: optional array of string`

    Ubuntu/Debian packages to install

  - `cargo: optional array of string`

    Rust packages to install

  - `gem: optional array of string`

    Ruby packages to install

  - `go: optional array of string`

    Go packages to install

  - `npm: optional array of string`

    Node.js packages to install

  - `pip: optional array of string`

    Python packages to install

  - `type: optional "packages"`

    Package configuration type

    - `"packages"`

### Beta Self Hosted Config

- `beta_self_hosted_config: object { type }`

  Configuration for self-hosted environments.

  - `type: "self_hosted"`

    Environment type

### Beta Self Hosted Config Params

- `beta_self_hosted_config_params: object { type }`

  Request params for `self_hosted` environment configuration.

  - `type: "self_hosted"`

    Environment type

### Beta Unrestricted Network

- `beta_unrestricted_network: object { type }`

  Unrestricted network access.

  - `type: "unrestricted"`

    Network policy type

# Work

## Retrieve

`$ ant beta:environments:work retrieve`

**get** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

### Parameters

- `--environment-id: string`

  Path param

- `--work-id: string`

  Path param

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_self_hosted_work: object { id, acknowledged_at, created_at, 9 more }`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: string`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: string`

    RFC 3339 timestamp when work was created

  - `data: object { id, type }`

    The actual work to be performed

    - `id: string`

      Session identifier (e.g., 'session_...')

    - `type: "session"`

      Type of work data

  - `environment_id: string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: string`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: map[string]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: string`

    RFC 3339 timestamp when work execution started

  - `state: "queued" or "starting" or "active" or 2 more`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: string`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: string`

    RFC 3339 timestamp when work execution stopped

  - `type: "work"`

    The type of object (always 'work')

### Example

```cli
ant beta:environments:work retrieve \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW \
  --work-id work_id
```

## Poll

`$ ant beta:environments:work poll`

**get** `/v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

### Parameters

- `--environment-id: string`

  Path param

- `--block-ms: optional number`

  Query param: How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

- `--reclaim-older-than-ms: optional number`

  Query param: Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--anthropic-worker-id: optional string`

  Header param: Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

### Returns

- `beta_self_hosted_work: object { id, acknowledged_at, created_at, 9 more }`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: string`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: string`

    RFC 3339 timestamp when work was created

  - `data: object { id, type }`

    The actual work to be performed

    - `id: string`

      Session identifier (e.g., 'session_...')

    - `type: "session"`

      Type of work data

  - `environment_id: string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: string`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: map[string]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: string`

    RFC 3339 timestamp when work execution started

  - `state: "queued" or "starting" or "active" or 2 more`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: string`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: string`

    RFC 3339 timestamp when work execution stopped

  - `type: "work"`

    The type of object (always 'work')

### Example

```cli
ant beta:environments:work poll \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

## Ack

`$ ant beta:environments:work ack`

**post** `/v1/environments/{environment_id}/work/{work_id}/ack`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Acknowledge receipt of a work item, transitioning it from 'queued' to 'starting' and removing it from the queue.

### Parameters

- `--environment-id: string`

  Path param

- `--work-id: string`

  Path param

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_self_hosted_work: object { id, acknowledged_at, created_at, 9 more }`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: string`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: string`

    RFC 3339 timestamp when work was created

  - `data: object { id, type }`

    The actual work to be performed

    - `id: string`

      Session identifier (e.g., 'session_...')

    - `type: "session"`

      Type of work data

  - `environment_id: string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: string`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: map[string]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: string`

    RFC 3339 timestamp when work execution started

  - `state: "queued" or "starting" or "active" or 2 more`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: string`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: string`

    RFC 3339 timestamp when work execution stopped

  - `type: "work"`

    The type of object (always 'work')

### Example

```cli
ant beta:environments:work ack \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW \
  --work-id work_id
```

## Heartbeat

`$ ant beta:environments:work heartbeat`

**post** `/v1/environments/{environment_id}/work/{work_id}/heartbeat`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

### Parameters

- `--environment-id: string`

  Path param

- `--work-id: string`

  Path param

- `--desired-ttl-seconds: optional number`

  Query param: Desired TTL in seconds

- `--expected-last-heartbeat: optional string`

  Query param: Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_self_hosted_work_heartbeat_response: object { last_heartbeat, lease_extended, state, 2 more }`

  Response after recording a heartbeat for a work item.

  - `last_heartbeat: string`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `lease_extended: boolean`

    Whether the heartbeat succeeded in extending the lease

  - `state: "queued" or "starting" or "active" or 2 more`

    Current state of the work item (active/stopping/stopped)

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `ttl_seconds: number`

    Effective TTL applied to the lease

  - `type: "work_heartbeat"`

    The type of response

### Example

```cli
ant beta:environments:work heartbeat \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW \
  --work-id work_id
```

## Stop

`$ ant beta:environments:work stop`

**post** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

### Parameters

- `--environment-id: string`

  Path param

- `--work-id: string`

  Path param

- `--force: optional boolean`

  Body param: If true, immediately stop work without graceful shutdown

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_self_hosted_work: object { id, acknowledged_at, created_at, 9 more }`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: string`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: string`

    RFC 3339 timestamp when work was created

  - `data: object { id, type }`

    The actual work to be performed

    - `id: string`

      Session identifier (e.g., 'session_...')

    - `type: "session"`

      Type of work data

  - `environment_id: string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: string`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: map[string]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: string`

    RFC 3339 timestamp when work execution started

  - `state: "queued" or "starting" or "active" or 2 more`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: string`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: string`

    RFC 3339 timestamp when work execution stopped

  - `type: "work"`

    The type of object (always 'work')

### Example

```cli
ant beta:environments:work stop \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW \
  --work-id work_id
```

## List

`$ ant beta:environments:work list`

**get** `/v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

### Parameters

- `--environment-id: string`

  Path param

- `--limit: optional number`

  Query param: Maximum number of work items to return

- `--page: optional string`

  Query param: Opaque cursor from previous response for pagination

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_self_hosted_work_list_response: object { data, next_page }`

  Response when listing work items with cursor-based pagination.

  - `data: array of BetaSelfHostedWork`

    List of work items

    - `id: string`

      Work identifier (e.g., 'work_...')

    - `acknowledged_at: string`

      RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

    - `created_at: string`

      RFC 3339 timestamp when work was created

    - `data: object { id, type }`

      The actual work to be performed

      - `id: string`

        Session identifier (e.g., 'session_...')

      - `type: "session"`

        Type of work data

    - `environment_id: string`

      Environment identifier this work belongs to (e.g., `env_...`)

    - `latest_heartbeat_at: string`

      RFC 3339 timestamp of the most recent heartbeat

    - `metadata: map[string]`

      User-provided metadata key-value pairs associated with this work item

    - `started_at: string`

      RFC 3339 timestamp when work execution started

    - `state: "queued" or "starting" or "active" or 2 more`

      Current state of the work item

      - `"queued"`

      - `"starting"`

      - `"active"`

      - `"stopping"`

      - `"stopped"`

    - `stop_requested_at: string`

      RFC 3339 timestamp when stop was requested

    - `stopped_at: string`

      RFC 3339 timestamp when work execution stopped

    - `type: "work"`

      The type of object (always 'work')

  - `next_page: string`

    Opaque cursor for fetching the next page of results

### Example

```cli
ant beta:environments:work list \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

## Update

`$ ant beta:environments:work update`

**post** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

### Parameters

- `--environment-id: string`

  Path param

- `--work-id: string`

  Path param

- `--metadata: map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_self_hosted_work: object { id, acknowledged_at, created_at, 9 more }`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: string`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: string`

    RFC 3339 timestamp when work was created

  - `data: object { id, type }`

    The actual work to be performed

    - `id: string`

      Session identifier (e.g., 'session_...')

    - `type: "session"`

      Type of work data

  - `environment_id: string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: string`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: map[string]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: string`

    RFC 3339 timestamp when work execution started

  - `state: "queued" or "starting" or "active" or 2 more`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: string`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: string`

    RFC 3339 timestamp when work execution stopped

  - `type: "work"`

    The type of object (always 'work')

### Example

```cli
ant beta:environments:work update \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW \
  --work-id work_id \
  --metadata '{foo: string}'
```

## Stats

`$ ant beta:environments:work stats`

**get** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

### Parameters

- `--environment-id: string`

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_self_hosted_work_queue_stats: object { depth, oldest_queued_at, pending, 2 more }`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `depth: number`

    Number of work items waiting to be picked up (lag from consumer group)

  - `oldest_queued_at: string`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `pending: number`

    Number of work items being processed (polled but not acknowledged)

  - `type: "work_queue_stats"`

    The type of object

  - `workers_polling: number`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Example

```cli
ant beta:environments:work stats \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

## Domain Types

### Beta Self Hosted Work

- `beta_self_hosted_work: object { id, acknowledged_at, created_at, 9 more }`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: string`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: string`

    RFC 3339 timestamp when work was created

  - `data: object { id, type }`

    The actual work to be performed

    - `id: string`

      Session identifier (e.g., 'session_...')

    - `type: "session"`

      Type of work data

  - `environment_id: string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: string`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: map[string]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: string`

    RFC 3339 timestamp when work execution started

  - `state: "queued" or "starting" or "active" or 2 more`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: string`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: string`

    RFC 3339 timestamp when work execution stopped

  - `type: "work"`

    The type of object (always 'work')

### Beta Self Hosted Work Heartbeat Response

- `beta_self_hosted_work_heartbeat_response: object { last_heartbeat, lease_extended, state, 2 more }`

  Response after recording a heartbeat for a work item.

  - `last_heartbeat: string`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `lease_extended: boolean`

    Whether the heartbeat succeeded in extending the lease

  - `state: "queued" or "starting" or "active" or 2 more`

    Current state of the work item (active/stopping/stopped)

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `ttl_seconds: number`

    Effective TTL applied to the lease

  - `type: "work_heartbeat"`

    The type of response

### Beta Self Hosted Work List Response

- `beta_self_hosted_work_list_response: object { data, next_page }`

  Response when listing work items with cursor-based pagination.

  - `data: array of BetaSelfHostedWork`

    List of work items

    - `id: string`

      Work identifier (e.g., 'work_...')

    - `acknowledged_at: string`

      RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

    - `created_at: string`

      RFC 3339 timestamp when work was created

    - `data: object { id, type }`

      The actual work to be performed

      - `id: string`

        Session identifier (e.g., 'session_...')

      - `type: "session"`

        Type of work data

    - `environment_id: string`

      Environment identifier this work belongs to (e.g., `env_...`)

    - `latest_heartbeat_at: string`

      RFC 3339 timestamp of the most recent heartbeat

    - `metadata: map[string]`

      User-provided metadata key-value pairs associated with this work item

    - `started_at: string`

      RFC 3339 timestamp when work execution started

    - `state: "queued" or "starting" or "active" or 2 more`

      Current state of the work item

      - `"queued"`

      - `"starting"`

      - `"active"`

      - `"stopping"`

      - `"stopped"`

    - `stop_requested_at: string`

      RFC 3339 timestamp when stop was requested

    - `stopped_at: string`

      RFC 3339 timestamp when work execution stopped

    - `type: "work"`

      The type of object (always 'work')

  - `next_page: string`

    Opaque cursor for fetching the next page of results

### Beta Self Hosted Work Queue Stats

- `beta_self_hosted_work_queue_stats: object { depth, oldest_queued_at, pending, 2 more }`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `depth: number`

    Number of work items waiting to be picked up (lag from consumer group)

  - `oldest_queued_at: string`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `pending: number`

    Number of work items being processed (polled but not acknowledged)

  - `type: "work_queue_stats"`

    The type of object

  - `workers_polling: number`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Beta Self Hosted Work Stop Request

- `beta_self_hosted_work_stop_request: object { force }`

  Request to stop a work item.

  - `force: optional boolean`

    If true, immediately stop work without graceful shutdown

### Beta Self Hosted Work Update Request

- `beta_self_hosted_work_update_request: object { metadata }`

  Request to update work item metadata.

  - `metadata: map[string]`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

### Beta Session Work Data

- `beta_session_work_data: object { id, type }`

  Work data for session work items.

  This resource type is used when work represents a session that needs to be executed
  in a self-hosted environment.

  - `id: string`

    Session identifier (e.g., 'session_...')

  - `type: "session"`

    Type of work data

# Environments

## Create

`$ ant beta:environments create`

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `--name: string`

  Body param: Human-readable name for the environment

- `--config: optional object { type, networking, packages }`

  Body param: Request params for `cloud` environment configuration.

  Fields default to null; on update, omitted fields preserve the
  existing value.

- `--description: optional string`

  Body param: Optional description of the environment

- `--metadata: optional map[string]`

  Body param: User-provided metadata key-value pairs

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

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

## Update

`$ ant beta:environments update`

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `--environment-id: string`

  Path param

- `--config: optional object { type, networking, packages }`

  Body param: Request params for `cloud` environment configuration.

  Fields default to null; on update, omitted fields preserve the
  existing value.

- `--description: optional string`

  Body param: Updated description of the environment

- `--metadata: optional map[string]`

  Body param: User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

- `--name: optional string`

  Body param: Updated name for the environment

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

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

### Beta Unrestricted Network

- `beta_unrestricted_network: object { type }`

  Unrestricted network access.

  - `type: "unrestricted"`

    Network policy type

# Environments

## Create Environment

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

### Body Parameters

- `name: string`

  Human-readable name for the environment

- `config: optional BetaCloudConfigParams or BetaSelfHostedConfigParams`

  Environment configuration

  - `BetaCloudConfigParams object { type, networking, packages }`

    Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

    - `type: "cloud"`

      Environment type

      - `"cloud"`

    - `networking: optional BetaUnrestrictedNetwork or BetaLimitedNetworkParams`

      Network configuration policy. Omit on update to preserve the existing value.

      - `BetaUnrestrictedNetwork object { type }`

        Unrestricted network access.

        - `type: "unrestricted"`

          Network policy type

          - `"unrestricted"`

      - `BetaLimitedNetworkParams object { type, allow_mcp_servers, allow_package_managers, allowed_hosts }`

        Limited network request params.

        Fields default to null; on update, omitted fields preserve the
        existing value.

        - `type: "limited"`

          Network policy type

          - `"limited"`

        - `allow_mcp_servers: optional boolean`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allow_package_managers: optional boolean`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allowed_hosts: optional array of string`

          Specifies domains the container can reach.

    - `packages: optional BetaPackagesParams`

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

  - `BetaSelfHostedConfigParams object { type }`

    Request params for `self_hosted` environment configuration.

    - `type: "self_hosted"`

      Environment type

      - `"self_hosted"`

- `description: optional string`

  Optional description of the environment

- `metadata: optional map[string]`

  User-provided metadata key-value pairs

- `scope: optional "organization" or "account"`

  The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. Only applicable for self-hosted environments. If not specified, defaults based on organization type.

  - `"organization"`

  - `"account"`

### Returns

- `BetaEnvironment object { id, archived_at, config, 7 more }`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig or BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `BetaCloudConfig object { networking, packages, type }`

      `cloud` environment configuration.

      - `networking: BetaUnrestrictedNetwork or BetaLimitedNetwork`

        Network configuration policy.

        - `BetaUnrestrictedNetwork object { type }`

          Unrestricted network access.

          - `type: "unrestricted"`

            Network policy type

            - `"unrestricted"`

        - `BetaLimitedNetwork object { allow_mcp_servers, allow_package_managers, allowed_hosts, type }`

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

    - `BetaSelfHostedConfig object { type }`

      Configuration for self-hosted environments.

      - `type: "self_hosted"`

        Environment type

        - `"self_hosted"`

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

  - `scope: optional "organization" or "account"`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```http
curl https://api.anthropic.com/v1/environments \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "name": "python-data-analysis",
          "config": {
            "type": "cloud",
            "networking": {
              "type": "limited",
              "allow_package_managers": true,
              "allowed_hosts": [
                "api.example.com"
              ]
            },
            "packages": {
              "pip": [
                "pandas",
                "numpy"
              ]
            }
          },
          "description": "Python environment with data-analysis packages."
        }'
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

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

### Returns

- `data: array of BetaEnvironment`

  List of environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig or BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `BetaCloudConfig object { networking, packages, type }`

      `cloud` environment configuration.

      - `networking: BetaUnrestrictedNetwork or BetaLimitedNetwork`

        Network configuration policy.

        - `BetaUnrestrictedNetwork object { type }`

          Unrestricted network access.

          - `type: "unrestricted"`

            Network policy type

            - `"unrestricted"`

        - `BetaLimitedNetwork object { allow_mcp_servers, allow_package_managers, allowed_hosts, type }`

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

    - `BetaSelfHostedConfig object { type }`

      Configuration for self-hosted environments.

      - `type: "self_hosted"`

        Environment type

        - `"self_hosted"`

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

  - `scope: optional "organization" or "account"`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

- `next_page: string`

  Token for fetching the next page of results. If `null`, there are no more results available. Pass this value to the `page` parameter in the next request.

### Example

```http
curl https://api.anthropic.com/v1/environments \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/environments/{environment_id}`

Retrieve a specific environment by ID.

### Path Parameters

- `environment_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

### Returns

- `BetaEnvironment object { id, archived_at, config, 7 more }`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig or BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `BetaCloudConfig object { networking, packages, type }`

      `cloud` environment configuration.

      - `networking: BetaUnrestrictedNetwork or BetaLimitedNetwork`

        Network configuration policy.

        - `BetaUnrestrictedNetwork object { type }`

          Unrestricted network access.

          - `type: "unrestricted"`

            Network policy type

            - `"unrestricted"`

        - `BetaLimitedNetwork object { allow_mcp_servers, allow_package_managers, allowed_hosts, type }`

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

    - `BetaSelfHostedConfig object { type }`

      Configuration for self-hosted environments.

      - `type: "self_hosted"`

        Environment type

        - `"self_hosted"`

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

  - `scope: optional "organization" or "account"`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```http
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Path Parameters

- `environment_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

### Body Parameters

- `config: optional BetaCloudConfigParams or BetaSelfHostedConfigParams`

  Updated environment configuration

  - `BetaCloudConfigParams object { type, networking, packages }`

    Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

    - `type: "cloud"`

      Environment type

      - `"cloud"`

    - `networking: optional BetaUnrestrictedNetwork or BetaLimitedNetworkParams`

      Network configuration policy. Omit on update to preserve the existing value.

      - `BetaUnrestrictedNetwork object { type }`

        Unrestricted network access.

        - `type: "unrestricted"`

          Network policy type

          - `"unrestricted"`

      - `BetaLimitedNetworkParams object { type, allow_mcp_servers, allow_package_managers, allowed_hosts }`

        Limited network request params.

        Fields default to null; on update, omitted fields preserve the
        existing value.

        - `type: "limited"`

          Network policy type

          - `"limited"`

        - `allow_mcp_servers: optional boolean`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allow_package_managers: optional boolean`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allowed_hosts: optional array of string`

          Specifies domains the container can reach.

    - `packages: optional BetaPackagesParams`

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

  - `BetaSelfHostedConfigParams object { type }`

    Request params for `self_hosted` environment configuration.

    - `type: "self_hosted"`

      Environment type

      - `"self_hosted"`

- `description: optional string`

  Updated description of the environment

- `metadata: optional map[string]`

  User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

- `name: optional string`

  Updated name for the environment

- `scope: optional "organization" or "account"`

  The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only.

  - `"organization"`

  - `"account"`

### Returns

- `BetaEnvironment object { id, archived_at, config, 7 more }`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig or BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `BetaCloudConfig object { networking, packages, type }`

      `cloud` environment configuration.

      - `networking: BetaUnrestrictedNetwork or BetaLimitedNetwork`

        Network configuration policy.

        - `BetaUnrestrictedNetwork object { type }`

          Unrestricted network access.

          - `type: "unrestricted"`

            Network policy type

            - `"unrestricted"`

        - `BetaLimitedNetwork object { allow_mcp_servers, allow_package_managers, allowed_hosts, type }`

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

    - `BetaSelfHostedConfig object { type }`

      Configuration for self-hosted environments.

      - `type: "self_hosted"`

        Environment type

        - `"self_hosted"`

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

  - `scope: optional "organization" or "account"`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```http
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "description": "Python environment with data-analysis packages."
        }'
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

**delete** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Path Parameters

- `environment_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

### Returns

- `BetaEnvironmentDeleteResponse object { id, type }`

  Response after deleting an environment.

  - `id: string`

    Environment identifier

  - `type: "environment_deleted"`

    The type of response

    - `"environment_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```

## Archive Environment

**post** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Path Parameters

- `environment_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

### Returns

- `BetaEnvironment object { id, archived_at, config, 7 more }`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig or BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `BetaCloudConfig object { networking, packages, type }`

      `cloud` environment configuration.

      - `networking: BetaUnrestrictedNetwork or BetaLimitedNetwork`

        Network configuration policy.

        - `BetaUnrestrictedNetwork object { type }`

          Unrestricted network access.

          - `type: "unrestricted"`

            Network policy type

            - `"unrestricted"`

        - `BetaLimitedNetwork object { allow_mcp_servers, allow_package_managers, allowed_hosts, type }`

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

    - `BetaSelfHostedConfig object { type }`

      Configuration for self-hosted environments.

      - `type: "self_hosted"`

        Environment type

        - `"self_hosted"`

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

  - `scope: optional "organization" or "account"`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```http
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaCloudConfig object { networking, packages, type }`

  `cloud` environment configuration.

  - `networking: BetaUnrestrictedNetwork or BetaLimitedNetwork`

    Network configuration policy.

    - `BetaUnrestrictedNetwork object { type }`

      Unrestricted network access.

      - `type: "unrestricted"`

        Network policy type

        - `"unrestricted"`

    - `BetaLimitedNetwork object { allow_mcp_servers, allow_package_managers, allowed_hosts, type }`

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

### Beta Cloud Config Params

- `BetaCloudConfigParams object { type, networking, packages }`

  Request params for `cloud` environment configuration.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `type: "cloud"`

    Environment type

    - `"cloud"`

  - `networking: optional BetaUnrestrictedNetwork or BetaLimitedNetworkParams`

    Network configuration policy. Omit on update to preserve the existing value.

    - `BetaUnrestrictedNetwork object { type }`

      Unrestricted network access.

      - `type: "unrestricted"`

        Network policy type

        - `"unrestricted"`

    - `BetaLimitedNetworkParams object { type, allow_mcp_servers, allow_package_managers, allowed_hosts }`

      Limited network request params.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `type: "limited"`

        Network policy type

        - `"limited"`

      - `allow_mcp_servers: optional boolean`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `allow_package_managers: optional boolean`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `allowed_hosts: optional array of string`

        Specifies domains the container can reach.

  - `packages: optional BetaPackagesParams`

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

- `BetaEnvironment object { id, archived_at, config, 7 more }`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig or BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `BetaCloudConfig object { networking, packages, type }`

      `cloud` environment configuration.

      - `networking: BetaUnrestrictedNetwork or BetaLimitedNetwork`

        Network configuration policy.

        - `BetaUnrestrictedNetwork object { type }`

          Unrestricted network access.

          - `type: "unrestricted"`

            Network policy type

            - `"unrestricted"`

        - `BetaLimitedNetwork object { allow_mcp_servers, allow_package_managers, allowed_hosts, type }`

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

    - `BetaSelfHostedConfig object { type }`

      Configuration for self-hosted environments.

      - `type: "self_hosted"`

        Environment type

        - `"self_hosted"`

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

  - `scope: optional "organization" or "account"`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Beta Environment Delete Response

- `BetaEnvironmentDeleteResponse object { id, type }`

  Response after deleting an environment.

  - `id: string`

    Environment identifier

  - `type: "environment_deleted"`

    The type of response

    - `"environment_deleted"`

### Beta Limited Network

- `BetaLimitedNetwork object { allow_mcp_servers, allow_package_managers, allowed_hosts, type }`

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

### Beta Limited Network Params

- `BetaLimitedNetworkParams object { type, allow_mcp_servers, allow_package_managers, allowed_hosts }`

  Limited network request params.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `type: "limited"`

    Network policy type

    - `"limited"`

  - `allow_mcp_servers: optional boolean`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `allow_package_managers: optional boolean`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `allowed_hosts: optional array of string`

    Specifies domains the container can reach.

### Beta Packages

- `BetaPackages object { apt, cargo, gem, 4 more }`

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

- `BetaPackagesParams object { apt, cargo, gem, 4 more }`

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

- `BetaSelfHostedConfig object { type }`

  Configuration for self-hosted environments.

  - `type: "self_hosted"`

    Environment type

    - `"self_hosted"`

### Beta Self Hosted Config Params

- `BetaSelfHostedConfigParams object { type }`

  Request params for `self_hosted` environment configuration.

  - `type: "self_hosted"`

    Environment type

    - `"self_hosted"`

### Beta Unrestricted Network

- `BetaUnrestrictedNetwork object { type }`

  Unrestricted network access.

  - `type: "unrestricted"`

    Network policy type

    - `"unrestricted"`

# Work

## Get Work Item

**get** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

### Path Parameters

- `environment_id: string`

- `work_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

### Returns

- `BetaSelfHostedWork object { id, acknowledged_at, created_at, 9 more }`

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

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: string`

      Session identifier (e.g., 'session_...')

    - `type: "session"`

      Type of work data

      - `"session"`

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

    - `"work"`

### Example

```http
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID/work/$WORK_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**get** `/v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

### Path Parameters

- `environment_id: string`

### Query Parameters

- `block_ms: optional number`

  How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

- `reclaim_older_than_ms: optional number`

  Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

- `"Anthropic-Worker-ID": optional string`

  Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

### Returns

- `BetaSelfHostedWork object { id, acknowledged_at, created_at, 9 more }`

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

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: string`

      Session identifier (e.g., 'session_...')

    - `type: "session"`

      Type of work data

      - `"session"`

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

    - `"work"`

### Example

```http
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID/work/poll \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/environments/{environment_id}/work/{work_id}/ack`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Acknowledge receipt of a work item, transitioning it from 'queued' to 'starting' and removing it from the queue.

### Path Parameters

- `environment_id: string`

- `work_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

### Returns

- `BetaSelfHostedWork object { id, acknowledged_at, created_at, 9 more }`

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

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: string`

      Session identifier (e.g., 'session_...')

    - `type: "session"`

      Type of work data

      - `"session"`

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

    - `"work"`

### Example

```http
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID/work/$WORK_ID/ack \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/environments/{environment_id}/work/{work_id}/heartbeat`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

### Path Parameters

- `environment_id: string`

- `work_id: string`

### Query Parameters

- `desired_ttl_seconds: optional number`

  Desired TTL in seconds

- `expected_last_heartbeat: optional string`

  Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

### Returns

- `BetaSelfHostedWorkHeartbeatResponse object { last_heartbeat, lease_extended, state, 2 more }`

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

    - `"work_heartbeat"`

### Example

```http
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID/work/$WORK_ID/heartbeat \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

### Path Parameters

- `environment_id: string`

- `work_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

### Body Parameters

- `force: optional boolean`

  If true, immediately stop work without graceful shutdown

### Returns

- `BetaSelfHostedWork object { id, acknowledged_at, created_at, 9 more }`

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

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: string`

      Session identifier (e.g., 'session_...')

    - `type: "session"`

      Type of work data

      - `"session"`

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

    - `"work"`

### Example

```http
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID/work/$WORK_ID/stop \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
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

**get** `/v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

### Path Parameters

- `environment_id: string`

### Query Parameters

- `limit: optional number`

  Maximum number of work items to return

- `page: optional string`

  Opaque cursor from previous response for pagination

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

### Returns

- `BetaSelfHostedWorkListResponse object { data, next_page }`

  Response when listing work items with cursor-based pagination.

  - `data: array of BetaSelfHostedWork`

    List of work items

    - `id: string`

      Work identifier (e.g., 'work_...')

    - `acknowledged_at: string`

      RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

    - `created_at: string`

      RFC 3339 timestamp when work was created

    - `data: BetaSessionWorkData`

      The actual work to be performed

      - `id: string`

        Session identifier (e.g., 'session_...')

      - `type: "session"`

        Type of work data

        - `"session"`

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

      - `"work"`

  - `next_page: string`

    Opaque cursor for fetching the next page of results

### Example

```http
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID/work \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**post** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

### Path Parameters

- `environment_id: string`

- `work_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

### Body Parameters

- `metadata: map[string]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

### Returns

- `BetaSelfHostedWork object { id, acknowledged_at, created_at, 9 more }`

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

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: string`

      Session identifier (e.g., 'session_...')

    - `type: "session"`

      Type of work data

      - `"session"`

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

    - `"work"`

### Example

```http
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID/work/$WORK_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "metadata": {
            "foo": "string"
          }
        }'
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

**get** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

### Path Parameters

- `environment_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 23 more`

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

### Returns

- `BetaSelfHostedWorkQueueStats object { depth, oldest_queued_at, pending, 2 more }`

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

    - `"work_queue_stats"`

  - `workers_polling: number`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Example

```http
curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID/work/stats \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaSelfHostedWork object { id, acknowledged_at, created_at, 9 more }`

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

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: string`

      Session identifier (e.g., 'session_...')

    - `type: "session"`

      Type of work data

      - `"session"`

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

    - `"work"`

### Beta Self Hosted Work Heartbeat Response

- `BetaSelfHostedWorkHeartbeatResponse object { last_heartbeat, lease_extended, state, 2 more }`

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

    - `"work_heartbeat"`

### Beta Self Hosted Work List Response

- `BetaSelfHostedWorkListResponse object { data, next_page }`

  Response when listing work items with cursor-based pagination.

  - `data: array of BetaSelfHostedWork`

    List of work items

    - `id: string`

      Work identifier (e.g., 'work_...')

    - `acknowledged_at: string`

      RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

    - `created_at: string`

      RFC 3339 timestamp when work was created

    - `data: BetaSessionWorkData`

      The actual work to be performed

      - `id: string`

        Session identifier (e.g., 'session_...')

      - `type: "session"`

        Type of work data

        - `"session"`

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

      - `"work"`

  - `next_page: string`

    Opaque cursor for fetching the next page of results

### Beta Self Hosted Work Queue Stats

- `BetaSelfHostedWorkQueueStats object { depth, oldest_queued_at, pending, 2 more }`

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

    - `"work_queue_stats"`

  - `workers_polling: number`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Beta Self Hosted Work Stop Request

- `BetaSelfHostedWorkStopRequest object { force }`

  Request to stop a work item.

  - `force: optional boolean`

    If true, immediately stop work without graceful shutdown

### Beta Self Hosted Work Update Request

- `BetaSelfHostedWorkUpdateRequest object { metadata }`

  Request to update work item metadata.

  - `metadata: map[string]`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

### Beta Session Work Data

- `BetaSessionWorkData object { id, type }`

  Work data for session work items.

  This resource type is used when work represents a session that needs to be executed
  in a self-hosted environment.

  - `id: string`

    Session identifier (e.g., 'session_...')

  - `type: "session"`

    Type of work data

    - `"session"`

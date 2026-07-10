# Environments

## Create Environment

`beta.environments.create(EnvironmentCreateParams**kwargs)  -> BetaEnvironment`

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `name: str`

  Human-readable name for the environment

- `config: Optional[Config]`

  Environment configuration

  - `class BetaCloudConfigParams: …`

    Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

    - `type: Literal["cloud"]`

      Environment type

      - `"cloud"`

    - `networking: Optional[Networking]`

      Network configuration policy. Omit on update to preserve the existing value.

      - `class BetaUnrestrictedNetwork: …`

        Unrestricted network access.

        - `type: Literal["unrestricted"]`

          Network policy type

          - `"unrestricted"`

      - `class BetaLimitedNetworkParams: …`

        Limited network request params.

        Fields default to null; on update, omitted fields preserve the
        existing value.

        - `type: Literal["limited"]`

          Network policy type

          - `"limited"`

        - `allow_mcp_servers: Optional[bool]`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allow_package_managers: Optional[bool]`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allowed_hosts: Optional[List[str]]`

          Specifies domains the container can reach.

    - `packages: Optional[BetaPackagesParams]`

      Specify packages (and optionally their versions) available in this environment.

      When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

      - `apt: Optional[List[str]]`

        Ubuntu/Debian packages to install

      - `cargo: Optional[List[str]]`

        Rust packages to install

      - `gem: Optional[List[str]]`

        Ruby packages to install

      - `go: Optional[List[str]]`

        Go packages to install

      - `npm: Optional[List[str]]`

        Node.js packages to install

      - `pip: Optional[List[str]]`

        Python packages to install

      - `type: Optional[Literal["packages"]]`

        Package configuration type

        - `"packages"`

  - `class BetaSelfHostedConfigParams: …`

    Request params for `self_hosted` environment configuration.

    - `type: Literal["self_hosted"]`

      Environment type

      - `"self_hosted"`

- `description: Optional[str]`

  Optional description of the environment

- `metadata: Optional[Dict[str, str]]`

  User-provided metadata key-value pairs

- `scope: Optional[Literal["organization", "account"]]`

  The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. Only applicable for self-hosted environments. If not specified, defaults based on organization type.

  - `"organization"`

  - `"account"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaEnvironment: …`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: str`

    Environment identifier (e.g., 'env_...')

  - `archived_at: Optional[str]`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: Config`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig: …`

      `cloud` environment configuration.

      - `networking: Networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork: …`

          Unrestricted network access.

          - `type: Literal["unrestricted"]`

            Network policy type

            - `"unrestricted"`

        - `class BetaLimitedNetwork: …`

          Limited network access.

          - `allow_mcp_servers: bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `allow_package_managers: bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `allowed_hosts: List[str]`

            Specifies domains the container can reach.

          - `type: Literal["limited"]`

            Network policy type

            - `"limited"`

      - `packages: BetaPackages`

        Package manager configuration.

        - `apt: List[str]`

          Ubuntu/Debian packages to install

        - `cargo: List[str]`

          Rust packages to install

        - `gem: List[str]`

          Ruby packages to install

        - `go: List[str]`

          Go packages to install

        - `npm: List[str]`

          Node.js packages to install

        - `pip: List[str]`

          Python packages to install

        - `type: Optional[Literal["packages"]]`

          Package configuration type

          - `"packages"`

      - `type: Literal["cloud"]`

        Environment type

        - `"cloud"`

    - `class BetaSelfHostedConfig: …`

      Configuration for self-hosted environments.

      - `type: Literal["self_hosted"]`

        Environment type

        - `"self_hosted"`

  - `created_at: str`

    RFC 3339 timestamp when environment was created

  - `description: str`

    User-provided description for the environment

  - `metadata: Dict[str, str]`

    User-provided metadata key-value pairs

  - `name: str`

    Human-readable name for the environment

  - `type: Literal["environment"]`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: str`

    RFC 3339 timestamp when environment was last updated

  - `scope: Optional[Literal["organization", "account"]]`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_environment = client.beta.environments.create(
    name="python-data-analysis",
)
print(beta_environment.id)
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

`beta.environments.list(EnvironmentListParams**kwargs)  -> SyncPageCursor[BetaEnvironment]`

**get** `/v1/environments`

List environments with pagination support.

### Parameters

- `include_archived: Optional[bool]`

  Include archived environments in the response

- `limit: Optional[int]`

  Maximum number of environments to return

- `page: Optional[str]`

  Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaEnvironment: …`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: str`

    Environment identifier (e.g., 'env_...')

  - `archived_at: Optional[str]`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: Config`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig: …`

      `cloud` environment configuration.

      - `networking: Networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork: …`

          Unrestricted network access.

          - `type: Literal["unrestricted"]`

            Network policy type

            - `"unrestricted"`

        - `class BetaLimitedNetwork: …`

          Limited network access.

          - `allow_mcp_servers: bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `allow_package_managers: bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `allowed_hosts: List[str]`

            Specifies domains the container can reach.

          - `type: Literal["limited"]`

            Network policy type

            - `"limited"`

      - `packages: BetaPackages`

        Package manager configuration.

        - `apt: List[str]`

          Ubuntu/Debian packages to install

        - `cargo: List[str]`

          Rust packages to install

        - `gem: List[str]`

          Ruby packages to install

        - `go: List[str]`

          Go packages to install

        - `npm: List[str]`

          Node.js packages to install

        - `pip: List[str]`

          Python packages to install

        - `type: Optional[Literal["packages"]]`

          Package configuration type

          - `"packages"`

      - `type: Literal["cloud"]`

        Environment type

        - `"cloud"`

    - `class BetaSelfHostedConfig: …`

      Configuration for self-hosted environments.

      - `type: Literal["self_hosted"]`

        Environment type

        - `"self_hosted"`

  - `created_at: str`

    RFC 3339 timestamp when environment was created

  - `description: str`

    User-provided description for the environment

  - `metadata: Dict[str, str]`

    User-provided metadata key-value pairs

  - `name: str`

    Human-readable name for the environment

  - `type: Literal["environment"]`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: str`

    RFC 3339 timestamp when environment was last updated

  - `scope: Optional[Literal["organization", "account"]]`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.environments.list()
page = page.data[0]
print(page.id)
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

`beta.environments.retrieve(strenvironment_id, EnvironmentRetrieveParams**kwargs)  -> BetaEnvironment`

**get** `/v1/environments/{environment_id}`

Retrieve a specific environment by ID.

### Parameters

- `environment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaEnvironment: …`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: str`

    Environment identifier (e.g., 'env_...')

  - `archived_at: Optional[str]`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: Config`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig: …`

      `cloud` environment configuration.

      - `networking: Networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork: …`

          Unrestricted network access.

          - `type: Literal["unrestricted"]`

            Network policy type

            - `"unrestricted"`

        - `class BetaLimitedNetwork: …`

          Limited network access.

          - `allow_mcp_servers: bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `allow_package_managers: bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `allowed_hosts: List[str]`

            Specifies domains the container can reach.

          - `type: Literal["limited"]`

            Network policy type

            - `"limited"`

      - `packages: BetaPackages`

        Package manager configuration.

        - `apt: List[str]`

          Ubuntu/Debian packages to install

        - `cargo: List[str]`

          Rust packages to install

        - `gem: List[str]`

          Ruby packages to install

        - `go: List[str]`

          Go packages to install

        - `npm: List[str]`

          Node.js packages to install

        - `pip: List[str]`

          Python packages to install

        - `type: Optional[Literal["packages"]]`

          Package configuration type

          - `"packages"`

      - `type: Literal["cloud"]`

        Environment type

        - `"cloud"`

    - `class BetaSelfHostedConfig: …`

      Configuration for self-hosted environments.

      - `type: Literal["self_hosted"]`

        Environment type

        - `"self_hosted"`

  - `created_at: str`

    RFC 3339 timestamp when environment was created

  - `description: str`

    User-provided description for the environment

  - `metadata: Dict[str, str]`

    User-provided metadata key-value pairs

  - `name: str`

    Human-readable name for the environment

  - `type: Literal["environment"]`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: str`

    RFC 3339 timestamp when environment was last updated

  - `scope: Optional[Literal["organization", "account"]]`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_environment = client.beta.environments.retrieve(
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_environment.id)
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

`beta.environments.update(strenvironment_id, EnvironmentUpdateParams**kwargs)  -> BetaEnvironment`

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `environment_id: str`

- `config: Optional[Config]`

  Updated environment configuration

  - `class BetaCloudConfigParams: …`

    Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

    - `type: Literal["cloud"]`

      Environment type

      - `"cloud"`

    - `networking: Optional[Networking]`

      Network configuration policy. Omit on update to preserve the existing value.

      - `class BetaUnrestrictedNetwork: …`

        Unrestricted network access.

        - `type: Literal["unrestricted"]`

          Network policy type

          - `"unrestricted"`

      - `class BetaLimitedNetworkParams: …`

        Limited network request params.

        Fields default to null; on update, omitted fields preserve the
        existing value.

        - `type: Literal["limited"]`

          Network policy type

          - `"limited"`

        - `allow_mcp_servers: Optional[bool]`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allow_package_managers: Optional[bool]`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allowed_hosts: Optional[List[str]]`

          Specifies domains the container can reach.

    - `packages: Optional[BetaPackagesParams]`

      Specify packages (and optionally their versions) available in this environment.

      When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

      - `apt: Optional[List[str]]`

        Ubuntu/Debian packages to install

      - `cargo: Optional[List[str]]`

        Rust packages to install

      - `gem: Optional[List[str]]`

        Ruby packages to install

      - `go: Optional[List[str]]`

        Go packages to install

      - `npm: Optional[List[str]]`

        Node.js packages to install

      - `pip: Optional[List[str]]`

        Python packages to install

      - `type: Optional[Literal["packages"]]`

        Package configuration type

        - `"packages"`

  - `class BetaSelfHostedConfigParams: …`

    Request params for `self_hosted` environment configuration.

    - `type: Literal["self_hosted"]`

      Environment type

      - `"self_hosted"`

- `description: Optional[str]`

  Updated description of the environment

- `metadata: Optional[Dict[str, Optional[str]]]`

  User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

- `name: Optional[str]`

  Updated name for the environment

- `scope: Optional[Literal["organization", "account"]]`

  The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only.

  - `"organization"`

  - `"account"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaEnvironment: …`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: str`

    Environment identifier (e.g., 'env_...')

  - `archived_at: Optional[str]`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: Config`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig: …`

      `cloud` environment configuration.

      - `networking: Networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork: …`

          Unrestricted network access.

          - `type: Literal["unrestricted"]`

            Network policy type

            - `"unrestricted"`

        - `class BetaLimitedNetwork: …`

          Limited network access.

          - `allow_mcp_servers: bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `allow_package_managers: bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `allowed_hosts: List[str]`

            Specifies domains the container can reach.

          - `type: Literal["limited"]`

            Network policy type

            - `"limited"`

      - `packages: BetaPackages`

        Package manager configuration.

        - `apt: List[str]`

          Ubuntu/Debian packages to install

        - `cargo: List[str]`

          Rust packages to install

        - `gem: List[str]`

          Ruby packages to install

        - `go: List[str]`

          Go packages to install

        - `npm: List[str]`

          Node.js packages to install

        - `pip: List[str]`

          Python packages to install

        - `type: Optional[Literal["packages"]]`

          Package configuration type

          - `"packages"`

      - `type: Literal["cloud"]`

        Environment type

        - `"cloud"`

    - `class BetaSelfHostedConfig: …`

      Configuration for self-hosted environments.

      - `type: Literal["self_hosted"]`

        Environment type

        - `"self_hosted"`

  - `created_at: str`

    RFC 3339 timestamp when environment was created

  - `description: str`

    User-provided description for the environment

  - `metadata: Dict[str, str]`

    User-provided metadata key-value pairs

  - `name: str`

    Human-readable name for the environment

  - `type: Literal["environment"]`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: str`

    RFC 3339 timestamp when environment was last updated

  - `scope: Optional[Literal["organization", "account"]]`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_environment = client.beta.environments.update(
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_environment.id)
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

`beta.environments.delete(strenvironment_id, EnvironmentDeleteParams**kwargs)  -> BetaEnvironmentDeleteResponse`

**delete** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Parameters

- `environment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaEnvironmentDeleteResponse: …`

  Response after deleting an environment.

  - `id: str`

    Environment identifier

  - `type: Literal["environment_deleted"]`

    The type of response

    - `"environment_deleted"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_environment_delete_response = client.beta.environments.delete(
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_environment_delete_response.id)
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```

## Archive Environment

`beta.environments.archive(strenvironment_id, EnvironmentArchiveParams**kwargs)  -> BetaEnvironment`

**post** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Parameters

- `environment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaEnvironment: …`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: str`

    Environment identifier (e.g., 'env_...')

  - `archived_at: Optional[str]`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: Config`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig: …`

      `cloud` environment configuration.

      - `networking: Networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork: …`

          Unrestricted network access.

          - `type: Literal["unrestricted"]`

            Network policy type

            - `"unrestricted"`

        - `class BetaLimitedNetwork: …`

          Limited network access.

          - `allow_mcp_servers: bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `allow_package_managers: bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `allowed_hosts: List[str]`

            Specifies domains the container can reach.

          - `type: Literal["limited"]`

            Network policy type

            - `"limited"`

      - `packages: BetaPackages`

        Package manager configuration.

        - `apt: List[str]`

          Ubuntu/Debian packages to install

        - `cargo: List[str]`

          Rust packages to install

        - `gem: List[str]`

          Ruby packages to install

        - `go: List[str]`

          Go packages to install

        - `npm: List[str]`

          Node.js packages to install

        - `pip: List[str]`

          Python packages to install

        - `type: Optional[Literal["packages"]]`

          Package configuration type

          - `"packages"`

      - `type: Literal["cloud"]`

        Environment type

        - `"cloud"`

    - `class BetaSelfHostedConfig: …`

      Configuration for self-hosted environments.

      - `type: Literal["self_hosted"]`

        Environment type

        - `"self_hosted"`

  - `created_at: str`

    RFC 3339 timestamp when environment was created

  - `description: str`

    User-provided description for the environment

  - `metadata: Dict[str, str]`

    User-provided metadata key-value pairs

  - `name: str`

    Human-readable name for the environment

  - `type: Literal["environment"]`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: str`

    RFC 3339 timestamp when environment was last updated

  - `scope: Optional[Literal["organization", "account"]]`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_environment = client.beta.environments.archive(
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_environment.id)
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

- `class BetaCloudConfig: …`

  `cloud` environment configuration.

  - `networking: Networking`

    Network configuration policy.

    - `class BetaUnrestrictedNetwork: …`

      Unrestricted network access.

      - `type: Literal["unrestricted"]`

        Network policy type

        - `"unrestricted"`

    - `class BetaLimitedNetwork: …`

      Limited network access.

      - `allow_mcp_servers: bool`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

      - `allow_package_managers: bool`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

      - `allowed_hosts: List[str]`

        Specifies domains the container can reach.

      - `type: Literal["limited"]`

        Network policy type

        - `"limited"`

  - `packages: BetaPackages`

    Package manager configuration.

    - `apt: List[str]`

      Ubuntu/Debian packages to install

    - `cargo: List[str]`

      Rust packages to install

    - `gem: List[str]`

      Ruby packages to install

    - `go: List[str]`

      Go packages to install

    - `npm: List[str]`

      Node.js packages to install

    - `pip: List[str]`

      Python packages to install

    - `type: Optional[Literal["packages"]]`

      Package configuration type

      - `"packages"`

  - `type: Literal["cloud"]`

    Environment type

    - `"cloud"`

### Beta Cloud Config Params

- `class BetaCloudConfigParams: …`

  Request params for `cloud` environment configuration.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `type: Literal["cloud"]`

    Environment type

    - `"cloud"`

  - `networking: Optional[Networking]`

    Network configuration policy. Omit on update to preserve the existing value.

    - `class BetaUnrestrictedNetwork: …`

      Unrestricted network access.

      - `type: Literal["unrestricted"]`

        Network policy type

        - `"unrestricted"`

    - `class BetaLimitedNetworkParams: …`

      Limited network request params.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `type: Literal["limited"]`

        Network policy type

        - `"limited"`

      - `allow_mcp_servers: Optional[bool]`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `allow_package_managers: Optional[bool]`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `allowed_hosts: Optional[List[str]]`

        Specifies domains the container can reach.

  - `packages: Optional[BetaPackagesParams]`

    Specify packages (and optionally their versions) available in this environment.

    When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

    - `apt: Optional[List[str]]`

      Ubuntu/Debian packages to install

    - `cargo: Optional[List[str]]`

      Rust packages to install

    - `gem: Optional[List[str]]`

      Ruby packages to install

    - `go: Optional[List[str]]`

      Go packages to install

    - `npm: Optional[List[str]]`

      Node.js packages to install

    - `pip: Optional[List[str]]`

      Python packages to install

    - `type: Optional[Literal["packages"]]`

      Package configuration type

      - `"packages"`

### Beta Environment

- `class BetaEnvironment: …`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: str`

    Environment identifier (e.g., 'env_...')

  - `archived_at: Optional[str]`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: Config`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig: …`

      `cloud` environment configuration.

      - `networking: Networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork: …`

          Unrestricted network access.

          - `type: Literal["unrestricted"]`

            Network policy type

            - `"unrestricted"`

        - `class BetaLimitedNetwork: …`

          Limited network access.

          - `allow_mcp_servers: bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `allow_package_managers: bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `allowed_hosts: List[str]`

            Specifies domains the container can reach.

          - `type: Literal["limited"]`

            Network policy type

            - `"limited"`

      - `packages: BetaPackages`

        Package manager configuration.

        - `apt: List[str]`

          Ubuntu/Debian packages to install

        - `cargo: List[str]`

          Rust packages to install

        - `gem: List[str]`

          Ruby packages to install

        - `go: List[str]`

          Go packages to install

        - `npm: List[str]`

          Node.js packages to install

        - `pip: List[str]`

          Python packages to install

        - `type: Optional[Literal["packages"]]`

          Package configuration type

          - `"packages"`

      - `type: Literal["cloud"]`

        Environment type

        - `"cloud"`

    - `class BetaSelfHostedConfig: …`

      Configuration for self-hosted environments.

      - `type: Literal["self_hosted"]`

        Environment type

        - `"self_hosted"`

  - `created_at: str`

    RFC 3339 timestamp when environment was created

  - `description: str`

    User-provided description for the environment

  - `metadata: Dict[str, str]`

    User-provided metadata key-value pairs

  - `name: str`

    Human-readable name for the environment

  - `type: Literal["environment"]`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: str`

    RFC 3339 timestamp when environment was last updated

  - `scope: Optional[Literal["organization", "account"]]`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Beta Environment Delete Response

- `class BetaEnvironmentDeleteResponse: …`

  Response after deleting an environment.

  - `id: str`

    Environment identifier

  - `type: Literal["environment_deleted"]`

    The type of response

    - `"environment_deleted"`

### Beta Limited Network

- `class BetaLimitedNetwork: …`

  Limited network access.

  - `allow_mcp_servers: bool`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

  - `allow_package_managers: bool`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

  - `allowed_hosts: List[str]`

    Specifies domains the container can reach.

  - `type: Literal["limited"]`

    Network policy type

    - `"limited"`

### Beta Limited Network Params

- `class BetaLimitedNetworkParams: …`

  Limited network request params.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `type: Literal["limited"]`

    Network policy type

    - `"limited"`

  - `allow_mcp_servers: Optional[bool]`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `allow_package_managers: Optional[bool]`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `allowed_hosts: Optional[List[str]]`

    Specifies domains the container can reach.

### Beta Packages

- `class BetaPackages: …`

  Packages (and their versions) available in this environment.

  - `apt: List[str]`

    Ubuntu/Debian packages to install

  - `cargo: List[str]`

    Rust packages to install

  - `gem: List[str]`

    Ruby packages to install

  - `go: List[str]`

    Go packages to install

  - `npm: List[str]`

    Node.js packages to install

  - `pip: List[str]`

    Python packages to install

  - `type: Optional[Literal["packages"]]`

    Package configuration type

    - `"packages"`

### Beta Packages Params

- `class BetaPackagesParams: …`

  Specify packages (and optionally their versions) available in this environment.

  When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

  - `apt: Optional[List[str]]`

    Ubuntu/Debian packages to install

  - `cargo: Optional[List[str]]`

    Rust packages to install

  - `gem: Optional[List[str]]`

    Ruby packages to install

  - `go: Optional[List[str]]`

    Go packages to install

  - `npm: Optional[List[str]]`

    Node.js packages to install

  - `pip: Optional[List[str]]`

    Python packages to install

  - `type: Optional[Literal["packages"]]`

    Package configuration type

    - `"packages"`

### Beta Self Hosted Config

- `class BetaSelfHostedConfig: …`

  Configuration for self-hosted environments.

  - `type: Literal["self_hosted"]`

    Environment type

    - `"self_hosted"`

### Beta Self Hosted Config Params

- `class BetaSelfHostedConfigParams: …`

  Request params for `self_hosted` environment configuration.

  - `type: Literal["self_hosted"]`

    Environment type

    - `"self_hosted"`

### Beta Unrestricted Network

- `class BetaUnrestrictedNetwork: …`

  Unrestricted network access.

  - `type: Literal["unrestricted"]`

    Network policy type

    - `"unrestricted"`

# Work

## Get Work Item

`beta.environments.work.retrieve(strwork_id, WorkRetrieveParams**kwargs)  -> BetaSelfHostedWork`

**get** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

### Parameters

- `environment_id: str`

- `work_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaSelfHostedWork: …`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: str`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: Optional[str]`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: str`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: str`

      Session identifier (e.g., 'session_...')

    - `type: Literal["session"]`

      Type of work data

      - `"session"`

  - `environment_id: str`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: Optional[str]`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Dict[str, str]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: Optional[str]`

    RFC 3339 timestamp when work execution started

  - `state: Literal["queued", "starting", "active", 2 more]`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: Optional[str]`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: Optional[str]`

    RFC 3339 timestamp when work execution stopped

  - `type: Literal["work"]`

    The type of object (always 'work')

    - `"work"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_self_hosted_work = client.beta.environments.work.retrieve(
    work_id="work_id",
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_self_hosted_work.id)
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

`beta.environments.work.poll(strenvironment_id, WorkPollParams**kwargs)  -> BetaSelfHostedWork`

**get** `/v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

### Parameters

- `environment_id: str`

- `block_ms: Optional[int]`

  How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

- `reclaim_older_than_ms: Optional[int]`

  Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

- `anthropic_worker_id: Optional[str]`

  Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

### Returns

- `class BetaSelfHostedWork: …`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: str`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: Optional[str]`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: str`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: str`

      Session identifier (e.g., 'session_...')

    - `type: Literal["session"]`

      Type of work data

      - `"session"`

  - `environment_id: str`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: Optional[str]`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Dict[str, str]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: Optional[str]`

    RFC 3339 timestamp when work execution started

  - `state: Literal["queued", "starting", "active", 2 more]`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: Optional[str]`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: Optional[str]`

    RFC 3339 timestamp when work execution stopped

  - `type: Literal["work"]`

    The type of object (always 'work')

    - `"work"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_self_hosted_work = client.beta.environments.work.poll(
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_self_hosted_work.id)
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

`beta.environments.work.ack(strwork_id, WorkAckParams**kwargs)  -> BetaSelfHostedWork`

**post** `/v1/environments/{environment_id}/work/{work_id}/ack`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Acknowledge receipt of a work item, transitioning it from 'queued' to 'starting' and removing it from the queue.

### Parameters

- `environment_id: str`

- `work_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaSelfHostedWork: …`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: str`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: Optional[str]`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: str`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: str`

      Session identifier (e.g., 'session_...')

    - `type: Literal["session"]`

      Type of work data

      - `"session"`

  - `environment_id: str`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: Optional[str]`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Dict[str, str]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: Optional[str]`

    RFC 3339 timestamp when work execution started

  - `state: Literal["queued", "starting", "active", 2 more]`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: Optional[str]`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: Optional[str]`

    RFC 3339 timestamp when work execution stopped

  - `type: Literal["work"]`

    The type of object (always 'work')

    - `"work"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_self_hosted_work = client.beta.environments.work.ack(
    work_id="work_id",
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_self_hosted_work.id)
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

`beta.environments.work.heartbeat(strwork_id, WorkHeartbeatParams**kwargs)  -> BetaSelfHostedWorkHeartbeatResponse`

**post** `/v1/environments/{environment_id}/work/{work_id}/heartbeat`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

### Parameters

- `environment_id: str`

- `work_id: str`

- `desired_ttl_seconds: Optional[int]`

  Desired TTL in seconds

- `expected_last_heartbeat: Optional[str]`

  Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaSelfHostedWorkHeartbeatResponse: …`

  Response after recording a heartbeat for a work item.

  - `last_heartbeat: str`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `lease_extended: bool`

    Whether the heartbeat succeeded in extending the lease

  - `state: Literal["queued", "starting", "active", 2 more]`

    Current state of the work item (active/stopping/stopped)

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `ttl_seconds: int`

    Effective TTL applied to the lease

  - `type: Literal["work_heartbeat"]`

    The type of response

    - `"work_heartbeat"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_self_hosted_work_heartbeat_response = client.beta.environments.work.heartbeat(
    work_id="work_id",
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_self_hosted_work_heartbeat_response.last_heartbeat)
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

`beta.environments.work.stop(strwork_id, WorkStopParams**kwargs)  -> BetaSelfHostedWork`

**post** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

### Parameters

- `environment_id: str`

- `work_id: str`

- `force: Optional[bool]`

  If true, immediately stop work without graceful shutdown

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaSelfHostedWork: …`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: str`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: Optional[str]`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: str`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: str`

      Session identifier (e.g., 'session_...')

    - `type: Literal["session"]`

      Type of work data

      - `"session"`

  - `environment_id: str`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: Optional[str]`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Dict[str, str]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: Optional[str]`

    RFC 3339 timestamp when work execution started

  - `state: Literal["queued", "starting", "active", 2 more]`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: Optional[str]`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: Optional[str]`

    RFC 3339 timestamp when work execution stopped

  - `type: Literal["work"]`

    The type of object (always 'work')

    - `"work"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_self_hosted_work = client.beta.environments.work.stop(
    work_id="work_id",
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_self_hosted_work.id)
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

`beta.environments.work.list(strenvironment_id, WorkListParams**kwargs)  -> SyncPageCursor[BetaSelfHostedWork]`

**get** `/v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

### Parameters

- `environment_id: str`

- `limit: Optional[int]`

  Maximum number of work items to return

- `page: Optional[str]`

  Opaque cursor from previous response for pagination

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaSelfHostedWork: …`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: str`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: Optional[str]`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: str`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: str`

      Session identifier (e.g., 'session_...')

    - `type: Literal["session"]`

      Type of work data

      - `"session"`

  - `environment_id: str`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: Optional[str]`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Dict[str, str]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: Optional[str]`

    RFC 3339 timestamp when work execution started

  - `state: Literal["queued", "starting", "active", 2 more]`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: Optional[str]`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: Optional[str]`

    RFC 3339 timestamp when work execution stopped

  - `type: Literal["work"]`

    The type of object (always 'work')

    - `"work"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.environments.work.list(
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
page = page.data[0]
print(page.id)
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

`beta.environments.work.update(strwork_id, WorkUpdateParams**kwargs)  -> BetaSelfHostedWork`

**post** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

### Parameters

- `environment_id: str`

- `work_id: str`

- `metadata: Dict[str, Optional[str]]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaSelfHostedWork: …`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: str`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: Optional[str]`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: str`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: str`

      Session identifier (e.g., 'session_...')

    - `type: Literal["session"]`

      Type of work data

      - `"session"`

  - `environment_id: str`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: Optional[str]`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Dict[str, str]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: Optional[str]`

    RFC 3339 timestamp when work execution started

  - `state: Literal["queued", "starting", "active", 2 more]`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: Optional[str]`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: Optional[str]`

    RFC 3339 timestamp when work execution stopped

  - `type: Literal["work"]`

    The type of object (always 'work')

    - `"work"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_self_hosted_work = client.beta.environments.work.update(
    work_id="work_id",
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
    metadata={
        "foo": "string"
    },
)
print(beta_self_hosted_work.id)
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

`beta.environments.work.stats(strenvironment_id, WorkStatsParams**kwargs)  -> BetaSelfHostedWorkQueueStats`

**get** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

### Parameters

- `environment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]`

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

    - `"agent-memory-2026-07-22"`

### Returns

- `class BetaSelfHostedWorkQueueStats: …`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `depth: int`

    Number of work items waiting to be picked up (lag from consumer group)

  - `oldest_queued_at: Optional[str]`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `pending: int`

    Number of work items being processed (polled but not acknowledged)

  - `type: Literal["work_queue_stats"]`

    The type of object

    - `"work_queue_stats"`

  - `workers_polling: Optional[int]`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_self_hosted_work_queue_stats = client.beta.environments.work.stats(
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_self_hosted_work_queue_stats.depth)
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

- `class BetaSelfHostedWork: …`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `id: str`

    Work identifier (e.g., 'work_...')

  - `acknowledged_at: Optional[str]`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `created_at: str`

    RFC 3339 timestamp when work was created

  - `data: BetaSessionWorkData`

    The actual work to be performed

    - `id: str`

      Session identifier (e.g., 'session_...')

    - `type: Literal["session"]`

      Type of work data

      - `"session"`

  - `environment_id: str`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `latest_heartbeat_at: Optional[str]`

    RFC 3339 timestamp of the most recent heartbeat

  - `metadata: Dict[str, str]`

    User-provided metadata key-value pairs associated with this work item

  - `started_at: Optional[str]`

    RFC 3339 timestamp when work execution started

  - `state: Literal["queued", "starting", "active", 2 more]`

    Current state of the work item

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `stop_requested_at: Optional[str]`

    RFC 3339 timestamp when stop was requested

  - `stopped_at: Optional[str]`

    RFC 3339 timestamp when work execution stopped

  - `type: Literal["work"]`

    The type of object (always 'work')

    - `"work"`

### Beta Self Hosted Work Heartbeat Response

- `class BetaSelfHostedWorkHeartbeatResponse: …`

  Response after recording a heartbeat for a work item.

  - `last_heartbeat: str`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `lease_extended: bool`

    Whether the heartbeat succeeded in extending the lease

  - `state: Literal["queued", "starting", "active", 2 more]`

    Current state of the work item (active/stopping/stopped)

    - `"queued"`

    - `"starting"`

    - `"active"`

    - `"stopping"`

    - `"stopped"`

  - `ttl_seconds: int`

    Effective TTL applied to the lease

  - `type: Literal["work_heartbeat"]`

    The type of response

    - `"work_heartbeat"`

### Beta Self Hosted Work List Response

- `class BetaSelfHostedWorkListResponse: …`

  Response when listing work items with cursor-based pagination.

  - `data: List[BetaSelfHostedWork]`

    List of work items

    - `id: str`

      Work identifier (e.g., 'work_...')

    - `acknowledged_at: Optional[str]`

      RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

    - `created_at: str`

      RFC 3339 timestamp when work was created

    - `data: BetaSessionWorkData`

      The actual work to be performed

      - `id: str`

        Session identifier (e.g., 'session_...')

      - `type: Literal["session"]`

        Type of work data

        - `"session"`

    - `environment_id: str`

      Environment identifier this work belongs to (e.g., `env_...`)

    - `latest_heartbeat_at: Optional[str]`

      RFC 3339 timestamp of the most recent heartbeat

    - `metadata: Dict[str, str]`

      User-provided metadata key-value pairs associated with this work item

    - `started_at: Optional[str]`

      RFC 3339 timestamp when work execution started

    - `state: Literal["queued", "starting", "active", 2 more]`

      Current state of the work item

      - `"queued"`

      - `"starting"`

      - `"active"`

      - `"stopping"`

      - `"stopped"`

    - `stop_requested_at: Optional[str]`

      RFC 3339 timestamp when stop was requested

    - `stopped_at: Optional[str]`

      RFC 3339 timestamp when work execution stopped

    - `type: Literal["work"]`

      The type of object (always 'work')

      - `"work"`

  - `next_page: Optional[str]`

    Opaque cursor for fetching the next page of results

### Beta Self Hosted Work Queue Stats

- `class BetaSelfHostedWorkQueueStats: …`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `depth: int`

    Number of work items waiting to be picked up (lag from consumer group)

  - `oldest_queued_at: Optional[str]`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `pending: int`

    Number of work items being processed (polled but not acknowledged)

  - `type: Literal["work_queue_stats"]`

    The type of object

    - `"work_queue_stats"`

  - `workers_polling: Optional[int]`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Beta Self Hosted Work Stop Request

- `class BetaSelfHostedWorkStopRequest: …`

  Request to stop a work item.

  - `force: Optional[bool]`

    If true, immediately stop work without graceful shutdown

### Beta Self Hosted Work Update Request

- `class BetaSelfHostedWorkUpdateRequest: …`

  Request to update work item metadata.

  - `metadata: Dict[str, Optional[str]]`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

### Beta Session Work Data

- `class BetaSessionWorkData: …`

  Work data for session work items.

  This resource type is used when work represents a session that needs to be executed
  in a self-hosted environment.

  - `id: str`

    Session identifier (e.g., 'session_...')

  - `type: Literal["session"]`

    Type of work data

    - `"session"`

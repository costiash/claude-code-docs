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

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 23 more]`

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

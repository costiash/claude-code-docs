## Archive

`beta.environments.archive(strenvironment_id, EnvironmentArchiveParams**kwargs)  -> BetaEnvironment`

**post** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Parameters

- `environment_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]`

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

    - `"advisor-tool-2026-03-01"`

    - `"user-profiles-2026-03-24"`

### Returns

- `class BetaEnvironment: …`

  Unified Environment resource for both cloud and BYOC environments.

  - `id: str`

    Environment identifier (e.g., 'env_...')

  - `archived_at: Optional[str]`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig`

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

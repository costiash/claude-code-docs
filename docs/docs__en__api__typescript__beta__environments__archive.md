## Archive Environment

`client.beta.environments.archive(stringenvironmentID, EnvironmentArchiveParamsparams?, RequestOptionsoptions?): BetaEnvironment`

**post** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Parameters

- `environmentID: string`

- `params: EnvironmentArchiveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 23 more`

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

- `BetaEnvironment`

  Unified Environment resource for both cloud and self-hosted environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string | null`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig | BetaSelfHostedConfig`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `BetaCloudConfig`

      `cloud` environment configuration.

      - `networking: BetaUnrestrictedNetwork | BetaLimitedNetwork`

        Network configuration policy.

        - `BetaUnrestrictedNetwork`

          Unrestricted network access.

          - `type: "unrestricted"`

            Network policy type

            - `"unrestricted"`

        - `BetaLimitedNetwork`

          Limited network access.

          - `allow_mcp_servers: boolean`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `allow_package_managers: boolean`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `allowed_hosts: Array<string>`

            Specifies domains the container can reach.

          - `type: "limited"`

            Network policy type

            - `"limited"`

      - `packages: BetaPackages`

        Package manager configuration.

        - `apt: Array<string>`

          Ubuntu/Debian packages to install

        - `cargo: Array<string>`

          Rust packages to install

        - `gem: Array<string>`

          Ruby packages to install

        - `go: Array<string>`

          Go packages to install

        - `npm: Array<string>`

          Node.js packages to install

        - `pip: Array<string>`

          Python packages to install

        - `type?: "packages"`

          Package configuration type

          - `"packages"`

      - `type: "cloud"`

        Environment type

        - `"cloud"`

    - `BetaSelfHostedConfig`

      Configuration for self-hosted environments.

      - `type: "self_hosted"`

        Environment type

        - `"self_hosted"`

  - `created_at: string`

    RFC 3339 timestamp when environment was created

  - `description: string`

    User-provided description for the environment

  - `metadata: Record<string, string>`

    User-provided metadata key-value pairs

  - `name: string`

    Human-readable name for the environment

  - `type: "environment"`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: string`

    RFC 3339 timestamp when environment was last updated

  - `scope?: "organization" | "account"`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"`

    - `"account"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaEnvironment = await client.beta.environments.archive('env_011CZkZ9X2dpNyB7HsEFoRfW');

console.log(betaEnvironment.id);
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

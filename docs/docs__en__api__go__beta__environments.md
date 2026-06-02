# Environments

## Create Environment

`client.Beta.Environments.New(ctx, params) (*BetaEnvironment, error)`

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `params BetaEnvironmentNewParams`

  - `Name param.Field[string]`

    Body param: Human-readable name for the environment

  - `Config param.Field[BetaEnvironmentNewParamsConfigUnion]`

    Body param: Environment configuration

    - `type BetaCloudConfigParamsResp struct{…}`

      Request params for `cloud` environment configuration.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `Type Cloud`

        Environment type

        - `const CloudCloud Cloud = "cloud"`

      - `Networking BetaCloudConfigParamsNetworkingUnionResp`

        Network configuration policy. Omit on update to preserve the existing value.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type BetaLimitedNetworkParamsResp struct{…}`

          Limited network request params.

          Fields default to null; on update, omitted fields preserve the
          existing value.

          - `Type Limited`

            Network policy type

            - `const LimitedLimited Limited = "limited"`

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

      - `Packages BetaPackagesParamsResp`

        Specify packages (and optionally their versions) available in this environment.

        When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesParamsType`

          Package configuration type

          - `const BetaPackagesParamsTypePackages BetaPackagesParamsType = "packages"`

    - `type BetaSelfHostedConfigParamsResp struct{…}`

      Request params for `self_hosted` environment configuration.

      - `Type SelfHosted`

        Environment type

        - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

  - `Description param.Field[string]`

    Body param: Optional description of the environment

  - `Metadata param.Field[map[string, string]]`

    Body param: User-provided metadata key-value pairs

  - `Scope param.Field[BetaEnvironmentNewParamsScope]`

    Body param: The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. Only applicable for self-hosted environments. If not specified, defaults based on organization type.

    - `const BetaEnvironmentNewParamsScopeOrganization BetaEnvironmentNewParamsScope = "organization"`

    - `const BetaEnvironmentNewParamsScopeAccount BetaEnvironmentNewParamsScope = "account"`

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaEnvironmentConfigUnion`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `type BetaCloudConfig struct{…}`

      `cloud` environment configuration.

      - `Networking BetaCloudConfigNetworkingUnion`

        Network configuration policy.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type BetaLimitedNetwork struct{…}`

          Limited network access.

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

          - `Type Limited`

            Network policy type

            - `const LimitedLimited Limited = "limited"`

      - `Packages BetaPackages`

        Package manager configuration.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesType`

          Package configuration type

          - `const BetaPackagesTypePackages BetaPackagesType = "packages"`

      - `Type Cloud`

        Environment type

        - `const CloudCloud Cloud = "cloud"`

    - `type BetaSelfHostedConfig struct{…}`

      Configuration for self-hosted environments.

      - `Type SelfHosted`

        Environment type

        - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

  - `CreatedAt string`

    RFC 3339 timestamp when environment was created

  - `Description string`

    User-provided description for the environment

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs

  - `Name string`

    Human-readable name for the environment

  - `Type Environment`

    The type of object (always 'environment')

    - `const EnvironmentEnvironment Environment = "environment"`

  - `UpdatedAt string`

    RFC 3339 timestamp when environment was last updated

  - `Scope BetaEnvironmentScope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"`

    - `const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaEnvironment, err := client.Beta.Environments.New(context.TODO(), anthropic.BetaEnvironmentNewParams{
    Name: "python-data-analysis",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaEnvironment.ID)
}
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

`client.Beta.Environments.List(ctx, params) (*PageCursor[BetaEnvironment], error)`

**get** `/v1/environments`

List environments with pagination support.

### Parameters

- `params BetaEnvironmentListParams`

  - `IncludeArchived param.Field[bool]`

    Query param: Include archived environments in the response

  - `Limit param.Field[int64]`

    Query param: Maximum number of environments to return

  - `Page param.Field[string]`

    Query param: Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaEnvironmentConfigUnion`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `type BetaCloudConfig struct{…}`

      `cloud` environment configuration.

      - `Networking BetaCloudConfigNetworkingUnion`

        Network configuration policy.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type BetaLimitedNetwork struct{…}`

          Limited network access.

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

          - `Type Limited`

            Network policy type

            - `const LimitedLimited Limited = "limited"`

      - `Packages BetaPackages`

        Package manager configuration.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesType`

          Package configuration type

          - `const BetaPackagesTypePackages BetaPackagesType = "packages"`

      - `Type Cloud`

        Environment type

        - `const CloudCloud Cloud = "cloud"`

    - `type BetaSelfHostedConfig struct{…}`

      Configuration for self-hosted environments.

      - `Type SelfHosted`

        Environment type

        - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

  - `CreatedAt string`

    RFC 3339 timestamp when environment was created

  - `Description string`

    User-provided description for the environment

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs

  - `Name string`

    Human-readable name for the environment

  - `Type Environment`

    The type of object (always 'environment')

    - `const EnvironmentEnvironment Environment = "environment"`

  - `UpdatedAt string`

    RFC 3339 timestamp when environment was last updated

  - `Scope BetaEnvironmentScope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"`

    - `const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.Environments.List(context.TODO(), anthropic.BetaEnvironmentListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
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

`client.Beta.Environments.Get(ctx, environmentID, query) (*BetaEnvironment, error)`

**get** `/v1/environments/{environment_id}`

Retrieve a specific environment by ID.

### Parameters

- `environmentID string`

- `query BetaEnvironmentGetParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaEnvironmentConfigUnion`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `type BetaCloudConfig struct{…}`

      `cloud` environment configuration.

      - `Networking BetaCloudConfigNetworkingUnion`

        Network configuration policy.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type BetaLimitedNetwork struct{…}`

          Limited network access.

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

          - `Type Limited`

            Network policy type

            - `const LimitedLimited Limited = "limited"`

      - `Packages BetaPackages`

        Package manager configuration.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesType`

          Package configuration type

          - `const BetaPackagesTypePackages BetaPackagesType = "packages"`

      - `Type Cloud`

        Environment type

        - `const CloudCloud Cloud = "cloud"`

    - `type BetaSelfHostedConfig struct{…}`

      Configuration for self-hosted environments.

      - `Type SelfHosted`

        Environment type

        - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

  - `CreatedAt string`

    RFC 3339 timestamp when environment was created

  - `Description string`

    User-provided description for the environment

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs

  - `Name string`

    Human-readable name for the environment

  - `Type Environment`

    The type of object (always 'environment')

    - `const EnvironmentEnvironment Environment = "environment"`

  - `UpdatedAt string`

    RFC 3339 timestamp when environment was last updated

  - `Scope BetaEnvironmentScope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"`

    - `const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaEnvironment, err := client.Beta.Environments.Get(
    context.TODO(),
    "env_011CZkZ9X2dpNyB7HsEFoRfW",
    anthropic.BetaEnvironmentGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaEnvironment.ID)
}
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

`client.Beta.Environments.Update(ctx, environmentID, params) (*BetaEnvironment, error)`

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `environmentID string`

- `params BetaEnvironmentUpdateParams`

  - `Config param.Field[BetaEnvironmentUpdateParamsConfigUnion]`

    Body param: Updated environment configuration

    - `type BetaCloudConfigParamsResp struct{…}`

      Request params for `cloud` environment configuration.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `Type Cloud`

        Environment type

        - `const CloudCloud Cloud = "cloud"`

      - `Networking BetaCloudConfigParamsNetworkingUnionResp`

        Network configuration policy. Omit on update to preserve the existing value.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type BetaLimitedNetworkParamsResp struct{…}`

          Limited network request params.

          Fields default to null; on update, omitted fields preserve the
          existing value.

          - `Type Limited`

            Network policy type

            - `const LimitedLimited Limited = "limited"`

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

      - `Packages BetaPackagesParamsResp`

        Specify packages (and optionally their versions) available in this environment.

        When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesParamsType`

          Package configuration type

          - `const BetaPackagesParamsTypePackages BetaPackagesParamsType = "packages"`

    - `type BetaSelfHostedConfigParamsResp struct{…}`

      Request params for `self_hosted` environment configuration.

      - `Type SelfHosted`

        Environment type

        - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

  - `Description param.Field[string]`

    Body param: Updated description of the environment

  - `Metadata param.Field[map[string, string]]`

    Body param: User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

  - `Name param.Field[string]`

    Body param: Updated name for the environment

  - `Scope param.Field[BetaEnvironmentUpdateParamsScope]`

    Body param: The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only.

    - `const BetaEnvironmentUpdateParamsScopeOrganization BetaEnvironmentUpdateParamsScope = "organization"`

    - `const BetaEnvironmentUpdateParamsScopeAccount BetaEnvironmentUpdateParamsScope = "account"`

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaEnvironmentConfigUnion`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `type BetaCloudConfig struct{…}`

      `cloud` environment configuration.

      - `Networking BetaCloudConfigNetworkingUnion`

        Network configuration policy.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type BetaLimitedNetwork struct{…}`

          Limited network access.

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

          - `Type Limited`

            Network policy type

            - `const LimitedLimited Limited = "limited"`

      - `Packages BetaPackages`

        Package manager configuration.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesType`

          Package configuration type

          - `const BetaPackagesTypePackages BetaPackagesType = "packages"`

      - `Type Cloud`

        Environment type

        - `const CloudCloud Cloud = "cloud"`

    - `type BetaSelfHostedConfig struct{…}`

      Configuration for self-hosted environments.

      - `Type SelfHosted`

        Environment type

        - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

  - `CreatedAt string`

    RFC 3339 timestamp when environment was created

  - `Description string`

    User-provided description for the environment

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs

  - `Name string`

    Human-readable name for the environment

  - `Type Environment`

    The type of object (always 'environment')

    - `const EnvironmentEnvironment Environment = "environment"`

  - `UpdatedAt string`

    RFC 3339 timestamp when environment was last updated

  - `Scope BetaEnvironmentScope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"`

    - `const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaEnvironment, err := client.Beta.Environments.Update(
    context.TODO(),
    "env_011CZkZ9X2dpNyB7HsEFoRfW",
    anthropic.BetaEnvironmentUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaEnvironment.ID)
}
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

`client.Beta.Environments.Delete(ctx, environmentID, body) (*BetaEnvironmentDeleteResponse, error)`

**delete** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Parameters

- `environmentID string`

- `body BetaEnvironmentDeleteParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

### Returns

- `type BetaEnvironmentDeleteResponse struct{…}`

  Response after deleting an environment.

  - `ID string`

    Environment identifier

  - `Type EnvironmentDeleted`

    The type of response

    - `const EnvironmentDeletedEnvironmentDeleted EnvironmentDeleted = "environment_deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaEnvironmentDeleteResponse, err := client.Beta.Environments.Delete(
    context.TODO(),
    "env_011CZkZ9X2dpNyB7HsEFoRfW",
    anthropic.BetaEnvironmentDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaEnvironmentDeleteResponse.ID)
}
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```

## Archive Environment

`client.Beta.Environments.Archive(ctx, environmentID, body) (*BetaEnvironment, error)`

**post** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Parameters

- `environmentID string`

- `body BetaEnvironmentArchiveParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaEnvironmentConfigUnion`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `type BetaCloudConfig struct{…}`

      `cloud` environment configuration.

      - `Networking BetaCloudConfigNetworkingUnion`

        Network configuration policy.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type BetaLimitedNetwork struct{…}`

          Limited network access.

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

          - `Type Limited`

            Network policy type

            - `const LimitedLimited Limited = "limited"`

      - `Packages BetaPackages`

        Package manager configuration.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesType`

          Package configuration type

          - `const BetaPackagesTypePackages BetaPackagesType = "packages"`

      - `Type Cloud`

        Environment type

        - `const CloudCloud Cloud = "cloud"`

    - `type BetaSelfHostedConfig struct{…}`

      Configuration for self-hosted environments.

      - `Type SelfHosted`

        Environment type

        - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

  - `CreatedAt string`

    RFC 3339 timestamp when environment was created

  - `Description string`

    User-provided description for the environment

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs

  - `Name string`

    Human-readable name for the environment

  - `Type Environment`

    The type of object (always 'environment')

    - `const EnvironmentEnvironment Environment = "environment"`

  - `UpdatedAt string`

    RFC 3339 timestamp when environment was last updated

  - `Scope BetaEnvironmentScope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"`

    - `const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaEnvironment, err := client.Beta.Environments.Archive(
    context.TODO(),
    "env_011CZkZ9X2dpNyB7HsEFoRfW",
    anthropic.BetaEnvironmentArchiveParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaEnvironment.ID)
}
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

- `type BetaCloudConfig struct{…}`

  `cloud` environment configuration.

  - `Networking BetaCloudConfigNetworkingUnion`

    Network configuration policy.

    - `type BetaUnrestrictedNetwork struct{…}`

      Unrestricted network access.

      - `Type Unrestricted`

        Network policy type

        - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

    - `type BetaLimitedNetwork struct{…}`

      Limited network access.

      - `AllowMCPServers bool`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

      - `AllowPackageManagers bool`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

      - `AllowedHosts []string`

        Specifies domains the container can reach.

      - `Type Limited`

        Network policy type

        - `const LimitedLimited Limited = "limited"`

  - `Packages BetaPackages`

    Package manager configuration.

    - `Apt []string`

      Ubuntu/Debian packages to install

    - `Cargo []string`

      Rust packages to install

    - `Gem []string`

      Ruby packages to install

    - `Go []string`

      Go packages to install

    - `Npm []string`

      Node.js packages to install

    - `Pip []string`

      Python packages to install

    - `Type BetaPackagesType`

      Package configuration type

      - `const BetaPackagesTypePackages BetaPackagesType = "packages"`

  - `Type Cloud`

    Environment type

    - `const CloudCloud Cloud = "cloud"`

### Beta Cloud Config Params

- `type BetaCloudConfigParamsResp struct{…}`

  Request params for `cloud` environment configuration.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `Type Cloud`

    Environment type

    - `const CloudCloud Cloud = "cloud"`

  - `Networking BetaCloudConfigParamsNetworkingUnionResp`

    Network configuration policy. Omit on update to preserve the existing value.

    - `type BetaUnrestrictedNetwork struct{…}`

      Unrestricted network access.

      - `Type Unrestricted`

        Network policy type

        - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

    - `type BetaLimitedNetworkParamsResp struct{…}`

      Limited network request params.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `Type Limited`

        Network policy type

        - `const LimitedLimited Limited = "limited"`

      - `AllowMCPServers bool`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `AllowPackageManagers bool`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `AllowedHosts []string`

        Specifies domains the container can reach.

  - `Packages BetaPackagesParamsResp`

    Specify packages (and optionally their versions) available in this environment.

    When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

    - `Apt []string`

      Ubuntu/Debian packages to install

    - `Cargo []string`

      Rust packages to install

    - `Gem []string`

      Ruby packages to install

    - `Go []string`

      Go packages to install

    - `Npm []string`

      Node.js packages to install

    - `Pip []string`

      Python packages to install

    - `Type BetaPackagesParamsType`

      Package configuration type

      - `const BetaPackagesParamsTypePackages BetaPackagesParamsType = "packages"`

### Beta Environment

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaEnvironmentConfigUnion`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `type BetaCloudConfig struct{…}`

      `cloud` environment configuration.

      - `Networking BetaCloudConfigNetworkingUnion`

        Network configuration policy.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type BetaLimitedNetwork struct{…}`

          Limited network access.

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

          - `Type Limited`

            Network policy type

            - `const LimitedLimited Limited = "limited"`

      - `Packages BetaPackages`

        Package manager configuration.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesType`

          Package configuration type

          - `const BetaPackagesTypePackages BetaPackagesType = "packages"`

      - `Type Cloud`

        Environment type

        - `const CloudCloud Cloud = "cloud"`

    - `type BetaSelfHostedConfig struct{…}`

      Configuration for self-hosted environments.

      - `Type SelfHosted`

        Environment type

        - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

  - `CreatedAt string`

    RFC 3339 timestamp when environment was created

  - `Description string`

    User-provided description for the environment

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs

  - `Name string`

    Human-readable name for the environment

  - `Type Environment`

    The type of object (always 'environment')

    - `const EnvironmentEnvironment Environment = "environment"`

  - `UpdatedAt string`

    RFC 3339 timestamp when environment was last updated

  - `Scope BetaEnvironmentScope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"`

    - `const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"`

### Beta Environment Delete Response

- `type BetaEnvironmentDeleteResponse struct{…}`

  Response after deleting an environment.

  - `ID string`

    Environment identifier

  - `Type EnvironmentDeleted`

    The type of response

    - `const EnvironmentDeletedEnvironmentDeleted EnvironmentDeleted = "environment_deleted"`

### Beta Limited Network

- `type BetaLimitedNetwork struct{…}`

  Limited network access.

  - `AllowMCPServers bool`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

  - `AllowPackageManagers bool`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

  - `AllowedHosts []string`

    Specifies domains the container can reach.

  - `Type Limited`

    Network policy type

    - `const LimitedLimited Limited = "limited"`

### Beta Limited Network Params

- `type BetaLimitedNetworkParamsResp struct{…}`

  Limited network request params.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `Type Limited`

    Network policy type

    - `const LimitedLimited Limited = "limited"`

  - `AllowMCPServers bool`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `AllowPackageManagers bool`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `AllowedHosts []string`

    Specifies domains the container can reach.

### Beta Packages

- `type BetaPackages struct{…}`

  Packages (and their versions) available in this environment.

  - `Apt []string`

    Ubuntu/Debian packages to install

  - `Cargo []string`

    Rust packages to install

  - `Gem []string`

    Ruby packages to install

  - `Go []string`

    Go packages to install

  - `Npm []string`

    Node.js packages to install

  - `Pip []string`

    Python packages to install

  - `Type BetaPackagesType`

    Package configuration type

    - `const BetaPackagesTypePackages BetaPackagesType = "packages"`

### Beta Packages Params

- `type BetaPackagesParamsResp struct{…}`

  Specify packages (and optionally their versions) available in this environment.

  When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

  - `Apt []string`

    Ubuntu/Debian packages to install

  - `Cargo []string`

    Rust packages to install

  - `Gem []string`

    Ruby packages to install

  - `Go []string`

    Go packages to install

  - `Npm []string`

    Node.js packages to install

  - `Pip []string`

    Python packages to install

  - `Type BetaPackagesParamsType`

    Package configuration type

    - `const BetaPackagesParamsTypePackages BetaPackagesParamsType = "packages"`

### Beta Self Hosted Config

- `type BetaSelfHostedConfig struct{…}`

  Configuration for self-hosted environments.

  - `Type SelfHosted`

    Environment type

    - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

### Beta Self Hosted Config Params

- `type BetaSelfHostedConfigParamsResp struct{…}`

  Request params for `self_hosted` environment configuration.

  - `Type SelfHosted`

    Environment type

    - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

### Beta Unrestricted Network

- `type BetaUnrestrictedNetwork struct{…}`

  Unrestricted network access.

  - `Type Unrestricted`

    Network policy type

    - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

# Work

## Get Work Item

`client.Beta.Environments.Work.Get(ctx, workID, params) (*BetaSelfHostedWork, error)`

**get** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

### Parameters

- `workID string`

- `params BetaEnvironmentWorkGetParams`

  - `EnvironmentID param.Field[string]`

    Path param

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

### Returns

- `type BetaSelfHostedWork struct{…}`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `ID string`

    Work identifier (e.g., 'work_...')

  - `AcknowledgedAt string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `CreatedAt string`

    RFC 3339 timestamp when work was created

  - `Data BetaSessionWorkData`

    The actual work to be performed

    - `ID string`

      Session identifier (e.g., 'session_...')

    - `Type Session`

      Type of work data

      - `const SessionSession Session = "session"`

  - `EnvironmentID string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `LatestHeartbeatAt string`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs associated with this work item

  - `StartedAt string`

    RFC 3339 timestamp when work execution started

  - `State BetaSelfHostedWorkState`

    Current state of the work item

    - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

    - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

    - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

    - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

    - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

  - `StopRequestedAt string`

    RFC 3339 timestamp when stop was requested

  - `StoppedAt string`

    RFC 3339 timestamp when work execution stopped

  - `Type Work`

    The type of object (always 'work')

    - `const WorkWork Work = "work"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaSelfHostedWork, err := client.Beta.Environments.Work.Get(
    context.TODO(),
    "work_id",
    anthropic.BetaEnvironmentWorkGetParams{
      EnvironmentID: "env_011CZkZ9X2dpNyB7HsEFoRfW",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaSelfHostedWork.ID)
}
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

`client.Beta.Environments.Work.Poll(ctx, environmentID, params) (*BetaSelfHostedWork, error)`

**get** `/v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

### Parameters

- `environmentID string`

- `params BetaEnvironmentWorkPollParams`

  - `BlockMs param.Field[int64]`

    Query param: How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

  - `ReclaimOlderThanMs param.Field[int64]`

    Query param: Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

  - `AnthropicWorkerID param.Field[string]`

    Header param: Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

### Returns

- `type BetaSelfHostedWork struct{…}`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `ID string`

    Work identifier (e.g., 'work_...')

  - `AcknowledgedAt string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `CreatedAt string`

    RFC 3339 timestamp when work was created

  - `Data BetaSessionWorkData`

    The actual work to be performed

    - `ID string`

      Session identifier (e.g., 'session_...')

    - `Type Session`

      Type of work data

      - `const SessionSession Session = "session"`

  - `EnvironmentID string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `LatestHeartbeatAt string`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs associated with this work item

  - `StartedAt string`

    RFC 3339 timestamp when work execution started

  - `State BetaSelfHostedWorkState`

    Current state of the work item

    - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

    - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

    - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

    - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

    - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

  - `StopRequestedAt string`

    RFC 3339 timestamp when stop was requested

  - `StoppedAt string`

    RFC 3339 timestamp when work execution stopped

  - `Type Work`

    The type of object (always 'work')

    - `const WorkWork Work = "work"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaSelfHostedWork, err := client.Beta.Environments.Work.Poll(
    context.TODO(),
    "env_011CZkZ9X2dpNyB7HsEFoRfW",
    anthropic.BetaEnvironmentWorkPollParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaSelfHostedWork.ID)
}
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

`client.Beta.Environments.Work.Ack(ctx, workID, params) (*BetaSelfHostedWork, error)`

**post** `/v1/environments/{environment_id}/work/{work_id}/ack`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Acknowledge receipt of a work item, transitioning it from 'queued' to 'starting' and removing it from the queue.

### Parameters

- `workID string`

- `params BetaEnvironmentWorkAckParams`

  - `EnvironmentID param.Field[string]`

    Path param

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

### Returns

- `type BetaSelfHostedWork struct{…}`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `ID string`

    Work identifier (e.g., 'work_...')

  - `AcknowledgedAt string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `CreatedAt string`

    RFC 3339 timestamp when work was created

  - `Data BetaSessionWorkData`

    The actual work to be performed

    - `ID string`

      Session identifier (e.g., 'session_...')

    - `Type Session`

      Type of work data

      - `const SessionSession Session = "session"`

  - `EnvironmentID string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `LatestHeartbeatAt string`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs associated with this work item

  - `StartedAt string`

    RFC 3339 timestamp when work execution started

  - `State BetaSelfHostedWorkState`

    Current state of the work item

    - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

    - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

    - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

    - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

    - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

  - `StopRequestedAt string`

    RFC 3339 timestamp when stop was requested

  - `StoppedAt string`

    RFC 3339 timestamp when work execution stopped

  - `Type Work`

    The type of object (always 'work')

    - `const WorkWork Work = "work"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaSelfHostedWork, err := client.Beta.Environments.Work.Ack(
    context.TODO(),
    "work_id",
    anthropic.BetaEnvironmentWorkAckParams{
      EnvironmentID: "env_011CZkZ9X2dpNyB7HsEFoRfW",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaSelfHostedWork.ID)
}
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

`client.Beta.Environments.Work.Heartbeat(ctx, workID, params) (*BetaSelfHostedWorkHeartbeatResponse, error)`

**post** `/v1/environments/{environment_id}/work/{work_id}/heartbeat`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

### Parameters

- `workID string`

- `params BetaEnvironmentWorkHeartbeatParams`

  - `EnvironmentID param.Field[string]`

    Path param

  - `DesiredTTLSeconds param.Field[int64]`

    Query param: Desired TTL in seconds

  - `ExpectedLastHeartbeat param.Field[string]`

    Query param: Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

### Returns

- `type BetaSelfHostedWorkHeartbeatResponse struct{…}`

  Response after recording a heartbeat for a work item.

  - `LastHeartbeat string`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `LeaseExtended bool`

    Whether the heartbeat succeeded in extending the lease

  - `State BetaSelfHostedWorkHeartbeatResponseState`

    Current state of the work item (active/stopping/stopped)

    - `const BetaSelfHostedWorkHeartbeatResponseStateQueued BetaSelfHostedWorkHeartbeatResponseState = "queued"`

    - `const BetaSelfHostedWorkHeartbeatResponseStateStarting BetaSelfHostedWorkHeartbeatResponseState = "starting"`

    - `const BetaSelfHostedWorkHeartbeatResponseStateActive BetaSelfHostedWorkHeartbeatResponseState = "active"`

    - `const BetaSelfHostedWorkHeartbeatResponseStateStopping BetaSelfHostedWorkHeartbeatResponseState = "stopping"`

    - `const BetaSelfHostedWorkHeartbeatResponseStateStopped BetaSelfHostedWorkHeartbeatResponseState = "stopped"`

  - `TTLSeconds int64`

    Effective TTL applied to the lease

  - `Type WorkHeartbeat`

    The type of response

    - `const WorkHeartbeatWorkHeartbeat WorkHeartbeat = "work_heartbeat"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaSelfHostedWorkHeartbeatResponse, err := client.Beta.Environments.Work.Heartbeat(
    context.TODO(),
    "work_id",
    anthropic.BetaEnvironmentWorkHeartbeatParams{
      EnvironmentID: "env_011CZkZ9X2dpNyB7HsEFoRfW",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaSelfHostedWorkHeartbeatResponse.LastHeartbeat)
}
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

`client.Beta.Environments.Work.Stop(ctx, workID, params) (*BetaSelfHostedWork, error)`

**post** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

### Parameters

- `workID string`

- `params BetaEnvironmentWorkStopParams`

  - `EnvironmentID param.Field[string]`

    Path param

  - `BetaSelfHostedWorkStopRequest param.Field[BetaSelfHostedWorkStopRequest]`

    Body param: Request to stop a work item.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

### Returns

- `type BetaSelfHostedWork struct{…}`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `ID string`

    Work identifier (e.g., 'work_...')

  - `AcknowledgedAt string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `CreatedAt string`

    RFC 3339 timestamp when work was created

  - `Data BetaSessionWorkData`

    The actual work to be performed

    - `ID string`

      Session identifier (e.g., 'session_...')

    - `Type Session`

      Type of work data

      - `const SessionSession Session = "session"`

  - `EnvironmentID string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `LatestHeartbeatAt string`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs associated with this work item

  - `StartedAt string`

    RFC 3339 timestamp when work execution started

  - `State BetaSelfHostedWorkState`

    Current state of the work item

    - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

    - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

    - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

    - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

    - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

  - `StopRequestedAt string`

    RFC 3339 timestamp when stop was requested

  - `StoppedAt string`

    RFC 3339 timestamp when work execution stopped

  - `Type Work`

    The type of object (always 'work')

    - `const WorkWork Work = "work"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaSelfHostedWork, err := client.Beta.Environments.Work.Stop(
    context.TODO(),
    "work_id",
    anthropic.BetaEnvironmentWorkStopParams{
      EnvironmentID: "env_011CZkZ9X2dpNyB7HsEFoRfW",
      BetaSelfHostedWorkStopRequest: anthropic.BetaSelfHostedWorkStopRequestParam{

      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaSelfHostedWork.ID)
}
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

`client.Beta.Environments.Work.List(ctx, environmentID, params) (*PageCursor[BetaSelfHostedWork], error)`

**get** `/v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

### Parameters

- `environmentID string`

- `params BetaEnvironmentWorkListParams`

  - `Limit param.Field[int64]`

    Query param: Maximum number of work items to return

  - `Page param.Field[string]`

    Query param: Opaque cursor from previous response for pagination

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

### Returns

- `type BetaSelfHostedWork struct{…}`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `ID string`

    Work identifier (e.g., 'work_...')

  - `AcknowledgedAt string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `CreatedAt string`

    RFC 3339 timestamp when work was created

  - `Data BetaSessionWorkData`

    The actual work to be performed

    - `ID string`

      Session identifier (e.g., 'session_...')

    - `Type Session`

      Type of work data

      - `const SessionSession Session = "session"`

  - `EnvironmentID string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `LatestHeartbeatAt string`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs associated with this work item

  - `StartedAt string`

    RFC 3339 timestamp when work execution started

  - `State BetaSelfHostedWorkState`

    Current state of the work item

    - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

    - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

    - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

    - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

    - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

  - `StopRequestedAt string`

    RFC 3339 timestamp when stop was requested

  - `StoppedAt string`

    RFC 3339 timestamp when work execution stopped

  - `Type Work`

    The type of object (always 'work')

    - `const WorkWork Work = "work"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.Environments.Work.List(
    context.TODO(),
    "env_011CZkZ9X2dpNyB7HsEFoRfW",
    anthropic.BetaEnvironmentWorkListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
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

`client.Beta.Environments.Work.Update(ctx, workID, params) (*BetaSelfHostedWork, error)`

**post** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

### Parameters

- `workID string`

- `params BetaEnvironmentWorkUpdateParams`

  - `EnvironmentID param.Field[string]`

    Path param

  - `BetaSelfHostedWorkUpdateRequest param.Field[BetaSelfHostedWorkUpdateRequest]`

    Body param: Request to update work item metadata.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

### Returns

- `type BetaSelfHostedWork struct{…}`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `ID string`

    Work identifier (e.g., 'work_...')

  - `AcknowledgedAt string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `CreatedAt string`

    RFC 3339 timestamp when work was created

  - `Data BetaSessionWorkData`

    The actual work to be performed

    - `ID string`

      Session identifier (e.g., 'session_...')

    - `Type Session`

      Type of work data

      - `const SessionSession Session = "session"`

  - `EnvironmentID string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `LatestHeartbeatAt string`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs associated with this work item

  - `StartedAt string`

    RFC 3339 timestamp when work execution started

  - `State BetaSelfHostedWorkState`

    Current state of the work item

    - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

    - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

    - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

    - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

    - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

  - `StopRequestedAt string`

    RFC 3339 timestamp when stop was requested

  - `StoppedAt string`

    RFC 3339 timestamp when work execution stopped

  - `Type Work`

    The type of object (always 'work')

    - `const WorkWork Work = "work"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaSelfHostedWork, err := client.Beta.Environments.Work.Update(
    context.TODO(),
    "work_id",
    anthropic.BetaEnvironmentWorkUpdateParams{
      EnvironmentID: "env_011CZkZ9X2dpNyB7HsEFoRfW",
      BetaSelfHostedWorkUpdateRequest: anthropic.BetaSelfHostedWorkUpdateRequestParam{
        Metadata: map[string]string{
        "foo": "string",
        },
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaSelfHostedWork.ID)
}
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

`client.Beta.Environments.Work.Stats(ctx, environmentID, query) (*BetaSelfHostedWorkQueueStats, error)`

**get** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

### Parameters

- `environmentID string`

- `query BetaEnvironmentWorkStatsParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

### Returns

- `type BetaSelfHostedWorkQueueStats struct{…}`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `Depth int64`

    Number of work items waiting to be picked up (lag from consumer group)

  - `OldestQueuedAt string`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `Pending int64`

    Number of work items being processed (polled but not acknowledged)

  - `Type WorkQueueStats`

    The type of object

    - `const WorkQueueStatsWorkQueueStats WorkQueueStats = "work_queue_stats"`

  - `WorkersPolling int64`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaSelfHostedWorkQueueStats, err := client.Beta.Environments.Work.Stats(
    context.TODO(),
    "env_011CZkZ9X2dpNyB7HsEFoRfW",
    anthropic.BetaEnvironmentWorkStatsParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaSelfHostedWorkQueueStats.Depth)
}
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

- `type BetaSelfHostedWork struct{…}`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `ID string`

    Work identifier (e.g., 'work_...')

  - `AcknowledgedAt string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `CreatedAt string`

    RFC 3339 timestamp when work was created

  - `Data BetaSessionWorkData`

    The actual work to be performed

    - `ID string`

      Session identifier (e.g., 'session_...')

    - `Type Session`

      Type of work data

      - `const SessionSession Session = "session"`

  - `EnvironmentID string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `LatestHeartbeatAt string`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs associated with this work item

  - `StartedAt string`

    RFC 3339 timestamp when work execution started

  - `State BetaSelfHostedWorkState`

    Current state of the work item

    - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

    - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

    - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

    - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

    - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

  - `StopRequestedAt string`

    RFC 3339 timestamp when stop was requested

  - `StoppedAt string`

    RFC 3339 timestamp when work execution stopped

  - `Type Work`

    The type of object (always 'work')

    - `const WorkWork Work = "work"`

### Beta Self Hosted Work Heartbeat Response

- `type BetaSelfHostedWorkHeartbeatResponse struct{…}`

  Response after recording a heartbeat for a work item.

  - `LastHeartbeat string`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `LeaseExtended bool`

    Whether the heartbeat succeeded in extending the lease

  - `State BetaSelfHostedWorkHeartbeatResponseState`

    Current state of the work item (active/stopping/stopped)

    - `const BetaSelfHostedWorkHeartbeatResponseStateQueued BetaSelfHostedWorkHeartbeatResponseState = "queued"`

    - `const BetaSelfHostedWorkHeartbeatResponseStateStarting BetaSelfHostedWorkHeartbeatResponseState = "starting"`

    - `const BetaSelfHostedWorkHeartbeatResponseStateActive BetaSelfHostedWorkHeartbeatResponseState = "active"`

    - `const BetaSelfHostedWorkHeartbeatResponseStateStopping BetaSelfHostedWorkHeartbeatResponseState = "stopping"`

    - `const BetaSelfHostedWorkHeartbeatResponseStateStopped BetaSelfHostedWorkHeartbeatResponseState = "stopped"`

  - `TTLSeconds int64`

    Effective TTL applied to the lease

  - `Type WorkHeartbeat`

    The type of response

    - `const WorkHeartbeatWorkHeartbeat WorkHeartbeat = "work_heartbeat"`

### Beta Self Hosted Work List Response

- `type BetaSelfHostedWorkListResponse struct{…}`

  Response when listing work items with cursor-based pagination.

  - `Data []BetaSelfHostedWork`

    List of work items

    - `ID string`

      Work identifier (e.g., 'work_...')

    - `AcknowledgedAt string`

      RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

    - `CreatedAt string`

      RFC 3339 timestamp when work was created

    - `Data BetaSessionWorkData`

      The actual work to be performed

      - `ID string`

        Session identifier (e.g., 'session_...')

      - `Type Session`

        Type of work data

        - `const SessionSession Session = "session"`

    - `EnvironmentID string`

      Environment identifier this work belongs to (e.g., `env_...`)

    - `LatestHeartbeatAt string`

      RFC 3339 timestamp of the most recent heartbeat

    - `Metadata map[string, string]`

      User-provided metadata key-value pairs associated with this work item

    - `StartedAt string`

      RFC 3339 timestamp when work execution started

    - `State BetaSelfHostedWorkState`

      Current state of the work item

      - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

      - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

      - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

      - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

      - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

    - `StopRequestedAt string`

      RFC 3339 timestamp when stop was requested

    - `StoppedAt string`

      RFC 3339 timestamp when work execution stopped

    - `Type Work`

      The type of object (always 'work')

      - `const WorkWork Work = "work"`

  - `NextPage string`

    Opaque cursor for fetching the next page of results

### Beta Self Hosted Work Queue Stats

- `type BetaSelfHostedWorkQueueStats struct{…}`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `Depth int64`

    Number of work items waiting to be picked up (lag from consumer group)

  - `OldestQueuedAt string`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `Pending int64`

    Number of work items being processed (polled but not acknowledged)

  - `Type WorkQueueStats`

    The type of object

    - `const WorkQueueStatsWorkQueueStats WorkQueueStats = "work_queue_stats"`

  - `WorkersPolling int64`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Beta Self Hosted Work Stop Request

- `type BetaSelfHostedWorkStopRequest struct{…}`

  Request to stop a work item.

  - `Force bool`

    If true, immediately stop work without graceful shutdown

### Beta Self Hosted Work Update Request

- `type BetaSelfHostedWorkUpdateRequest struct{…}`

  Request to update work item metadata.

  - `Metadata map[string, string]`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

### Beta Session Work Data

- `type BetaSessionWorkData struct{…}`

  Work data for session work items.

  This resource type is used when work represents a session that needs to be executed
  in a self-hosted environment.

  - `ID string`

    Session identifier (e.g., 'session_...')

  - `Type Session`

    Type of work data

    - `const SessionSession Session = "session"`

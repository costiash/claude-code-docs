# Environments

## Create

`client.Beta.Environments.New(ctx, params) (*BetaEnvironment, error)`

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `params BetaEnvironmentNewParams`

  - `Name param.Field[string]`

    Body param: Human-readable name for the environment

  - `Config param.Field[BetaCloudConfigParamsResp]`

    Body param: Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

  - `Description param.Field[string]`

    Body param: Optional description of the environment

  - `Metadata param.Field[map[string, string]]`

    Body param: User-provided metadata key-value pairs

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

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaCloudConfig`

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

## List

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

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaCloudConfig`

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

## Retrieve

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

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaCloudConfig`

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

## Update

`client.Beta.Environments.Update(ctx, environmentID, params) (*BetaEnvironment, error)`

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `environmentID string`

- `params BetaEnvironmentUpdateParams`

  - `Config param.Field[BetaCloudConfigParamsResp]`

    Body param: Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

  - `Description param.Field[string]`

    Body param: Updated description of the environment

  - `Metadata param.Field[map[string, string]]`

    Body param: User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

  - `Name param.Field[string]`

    Body param: Updated name for the environment

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

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaCloudConfig`

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

## Delete

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

## Archive

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

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaCloudConfig`

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

  - `Config BetaCloudConfig`

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

### Beta Unrestricted Network

- `type BetaUnrestrictedNetwork struct{…}`

  Unrestricted network access.

  - `Type Unrestricted`

    Network policy type

    - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

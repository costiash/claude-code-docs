# Vaults

## Create

`client.Beta.Vaults.New(ctx, params) (*BetaManagedAgentsVault, error)`

**post** `/v1/vaults`

Create Vault

### Parameters

- `params BetaVaultNewParams`

  - `DisplayName param.Field[string]`

    Body param: Human-readable name for the vault. 1-255 characters.

  - `Metadata param.Field[map[string, string]]`

    Body param: Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

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

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsVault struct{…}`

  A vault that stores credentials for use by agents during sessions.

  - `ID string`

    Unique identifier for the vault.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the vault.

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the vault.

  - `Type BetaManagedAgentsVaultType`

    - `const BetaManagedAgentsVaultTypeVault BetaManagedAgentsVaultType = "vault"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

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
  betaManagedAgentsVault, err := client.Beta.Vaults.New(context.TODO(), anthropic.BetaVaultNewParams{
    DisplayName: "Example vault",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsVault.ID)
}
```

## List

`client.Beta.Vaults.List(ctx, params) (*PageCursor[BetaManagedAgentsVault], error)`

**get** `/v1/vaults`

List Vaults

### Parameters

- `params BetaVaultListParams`

  - `IncludeArchived param.Field[bool]`

    Query param: Whether to include archived vaults in the results.

  - `Limit param.Field[int64]`

    Query param: Maximum number of vaults to return per page. Defaults to 20, maximum 100.

  - `Page param.Field[string]`

    Query param: Opaque pagination token from a previous `list_vaults` response.

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

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsVault struct{…}`

  A vault that stores credentials for use by agents during sessions.

  - `ID string`

    Unique identifier for the vault.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the vault.

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the vault.

  - `Type BetaManagedAgentsVaultType`

    - `const BetaManagedAgentsVaultTypeVault BetaManagedAgentsVaultType = "vault"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

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
  page, err := client.Beta.Vaults.List(context.TODO(), anthropic.BetaVaultListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Retrieve

`client.Beta.Vaults.Get(ctx, vaultID, query) (*BetaManagedAgentsVault, error)`

**get** `/v1/vaults/{vault_id}`

Get Vault

### Parameters

- `vaultID string`

- `query BetaVaultGetParams`

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

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsVault struct{…}`

  A vault that stores credentials for use by agents during sessions.

  - `ID string`

    Unique identifier for the vault.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the vault.

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the vault.

  - `Type BetaManagedAgentsVaultType`

    - `const BetaManagedAgentsVaultTypeVault BetaManagedAgentsVaultType = "vault"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

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
  betaManagedAgentsVault, err := client.Beta.Vaults.Get(
    context.TODO(),
    "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    anthropic.BetaVaultGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsVault.ID)
}
```

## Update

`client.Beta.Vaults.Update(ctx, vaultID, params) (*BetaManagedAgentsVault, error)`

**post** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `vaultID string`

- `params BetaVaultUpdateParams`

  - `DisplayName param.Field[string]`

    Body param: Updated human-readable name for the vault. 1-255 characters.

  - `Metadata param.Field[map[string, string]]`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

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

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsVault struct{…}`

  A vault that stores credentials for use by agents during sessions.

  - `ID string`

    Unique identifier for the vault.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the vault.

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the vault.

  - `Type BetaManagedAgentsVaultType`

    - `const BetaManagedAgentsVaultTypeVault BetaManagedAgentsVaultType = "vault"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

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
  betaManagedAgentsVault, err := client.Beta.Vaults.Update(
    context.TODO(),
    "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    anthropic.BetaVaultUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsVault.ID)
}
```

## Delete

`client.Beta.Vaults.Delete(ctx, vaultID, body) (*BetaManagedAgentsDeletedVault, error)`

**delete** `/v1/vaults/{vault_id}`

Delete Vault

### Parameters

- `vaultID string`

- `body BetaVaultDeleteParams`

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

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsDeletedVault struct{…}`

  Confirmation of a deleted vault.

  - `ID string`

    Unique identifier of the deleted vault.

  - `Type BetaManagedAgentsDeletedVaultType`

    - `const BetaManagedAgentsDeletedVaultTypeVaultDeleted BetaManagedAgentsDeletedVaultType = "vault_deleted"`

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
  betaManagedAgentsDeletedVault, err := client.Beta.Vaults.Delete(
    context.TODO(),
    "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    anthropic.BetaVaultDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeletedVault.ID)
}
```

## Archive

`client.Beta.Vaults.Archive(ctx, vaultID, body) (*BetaManagedAgentsVault, error)`

**post** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Parameters

- `vaultID string`

- `body BetaVaultArchiveParams`

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

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsVault struct{…}`

  A vault that stores credentials for use by agents during sessions.

  - `ID string`

    Unique identifier for the vault.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the vault.

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the vault.

  - `Type BetaManagedAgentsVaultType`

    - `const BetaManagedAgentsVaultTypeVault BetaManagedAgentsVaultType = "vault"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

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
  betaManagedAgentsVault, err := client.Beta.Vaults.Archive(
    context.TODO(),
    "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    anthropic.BetaVaultArchiveParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsVault.ID)
}
```

## Domain Types

### Beta Managed Agents Deleted Vault

- `type BetaManagedAgentsDeletedVault struct{…}`

  Confirmation of a deleted vault.

  - `ID string`

    Unique identifier of the deleted vault.

  - `Type BetaManagedAgentsDeletedVaultType`

    - `const BetaManagedAgentsDeletedVaultTypeVaultDeleted BetaManagedAgentsDeletedVaultType = "vault_deleted"`

### Beta Managed Agents Vault

- `type BetaManagedAgentsVault struct{…}`

  A vault that stores credentials for use by agents during sessions.

  - `ID string`

    Unique identifier for the vault.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the vault.

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the vault.

  - `Type BetaManagedAgentsVaultType`

    - `const BetaManagedAgentsVaultTypeVault BetaManagedAgentsVaultType = "vault"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

# Credentials

## Create

`client.Beta.Vaults.Credentials.New(ctx, vaultID, params) (*BetaManagedAgentsCredential, error)`

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Parameters

- `vaultID string`

- `params BetaVaultCredentialNewParams`

  - `Auth param.Field[BetaVaultCredentialNewParamsAuthUnion]`

    Body param: Authentication details for creating a credential.

    - `type BetaManagedAgentsMCPOAuthCreateParamsResp struct{…}`

      Parameters for creating an MCP OAuth credential.

      - `AccessToken string`

        OAuth access token.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthCreateParamsType`

        - `const BetaManagedAgentsMCPOAuthCreateParamsTypeMCPOAuth BetaManagedAgentsMCPOAuthCreateParamsType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshParamsResp`

        OAuth refresh token parameters for creating a credential with refresh support.

        - `ClientID string`

          OAuth client ID.

        - `RefreshToken string`

          OAuth refresh token.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshParamsTokenEndpointAuthUnionResp`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneParamResp struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneParamType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneParamTypeNone BetaManagedAgentsTokenEndpointAuthNoneParamType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicParamResp struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `ClientSecret string`

              OAuth client secret.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicParamType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicParamType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostParamResp struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `ClientSecret string`

              OAuth client secret.

            - `Type BetaManagedAgentsTokenEndpointAuthPostParamType`

              - `const BetaManagedAgentsTokenEndpointAuthPostParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostParamType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerCreateParamsResp struct{…}`

      Parameters for creating a static bearer token credential.

      - `Token string`

        Static bearer token value.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerCreateParamsType`

        - `const BetaManagedAgentsStaticBearerCreateParamsTypeStaticBearer BetaManagedAgentsStaticBearerCreateParamsType = "static_bearer"`

  - `DisplayName param.Field[string]`

    Body param: Human-readable name for the credential. Up to 255 characters.

  - `Metadata param.Field[map[string, string]]`

    Body param: Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

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

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

        - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

        - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

    - `const BetaManagedAgentsCredentialTypeVaultCredential BetaManagedAgentsCredentialType = "vault_credential"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string`

    Human-readable name for the credential.

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
  betaManagedAgentsCredential, err := client.Beta.Vaults.Credentials.New(
    context.TODO(),
    "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    anthropic.BetaVaultCredentialNewParams{
      Auth: anthropic.BetaVaultCredentialNewParamsAuthUnion{
        OfStaticBearer: &anthropic.BetaManagedAgentsStaticBearerCreateParams{
          Token: "bearer_exampletoken",
          MCPServerURL: "https://example-server.modelcontextprotocol.io/sse",
          Type: anthropic.BetaManagedAgentsStaticBearerCreateParamsTypeStaticBearer,
        },
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsCredential.ID)
}
```

## List

`client.Beta.Vaults.Credentials.List(ctx, vaultID, params) (*PageCursor[BetaManagedAgentsCredential], error)`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `vaultID string`

- `params BetaVaultCredentialListParams`

  - `IncludeArchived param.Field[bool]`

    Query param: Whether to include archived credentials in the results.

  - `Limit param.Field[int64]`

    Query param: Maximum number of credentials to return per page. Defaults to 20, maximum 100.

  - `Page param.Field[string]`

    Query param: Opaque pagination token from a previous `list_credentials` response.

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

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

        - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

        - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

    - `const BetaManagedAgentsCredentialTypeVaultCredential BetaManagedAgentsCredentialType = "vault_credential"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string`

    Human-readable name for the credential.

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
  page, err := client.Beta.Vaults.Credentials.List(
    context.TODO(),
    "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    anthropic.BetaVaultCredentialListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Retrieve

`client.Beta.Vaults.Credentials.Get(ctx, credentialID, params) (*BetaManagedAgentsCredential, error)`

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Parameters

- `credentialID string`

- `params BetaVaultCredentialGetParams`

  - `VaultID param.Field[string]`

    Path param: Path parameter vault_id

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

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

        - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

        - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

    - `const BetaManagedAgentsCredentialTypeVaultCredential BetaManagedAgentsCredentialType = "vault_credential"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string`

    Human-readable name for the credential.

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
  betaManagedAgentsCredential, err := client.Beta.Vaults.Credentials.Get(
    context.TODO(),
    "vcrd_011CZkZEMt8gZan2iYOQfSkw",
    anthropic.BetaVaultCredentialGetParams{
      VaultID: "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsCredential.ID)
}
```

## Update

`client.Beta.Vaults.Credentials.Update(ctx, credentialID, params) (*BetaManagedAgentsCredential, error)`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `credentialID string`

- `params BetaVaultCredentialUpdateParams`

  - `VaultID param.Field[string]`

    Path param: Path parameter vault_id

  - `Auth param.Field[BetaVaultCredentialUpdateParamsAuthUnion]`

    Body param: Updated authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthUpdateParamsResp struct{…}`

      Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

      - `Type BetaManagedAgentsMCPOAuthUpdateParamsType`

        - `const BetaManagedAgentsMCPOAuthUpdateParamsTypeMCPOAuth BetaManagedAgentsMCPOAuthUpdateParamsType = "mcp_oauth"`

      - `AccessToken string`

        Updated OAuth access token.

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshUpdateParamsResp`

        Parameters for updating OAuth refresh token configuration.

        - `RefreshToken string`

          Updated OAuth refresh token.

        - `Scope string`

          Updated OAuth scope for the refresh request.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshUpdateParamsTokenEndpointAuthUnionResp`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamResp struct{…}`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicUpdateParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType = "client_secret_basic"`

            - `ClientSecret string`

              Updated OAuth client secret.

          - `type BetaManagedAgentsTokenEndpointAuthPostUpdateParamResp struct{…}`

            Updated POST body authentication parameters for the token endpoint.

            - `Type BetaManagedAgentsTokenEndpointAuthPostUpdateParamType`

              - `const BetaManagedAgentsTokenEndpointAuthPostUpdateParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostUpdateParamType = "client_secret_post"`

            - `ClientSecret string`

              Updated OAuth client secret.

    - `type BetaManagedAgentsStaticBearerUpdateParamsResp struct{…}`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `Type BetaManagedAgentsStaticBearerUpdateParamsType`

        - `const BetaManagedAgentsStaticBearerUpdateParamsTypeStaticBearer BetaManagedAgentsStaticBearerUpdateParamsType = "static_bearer"`

      - `Token string`

        Updated static bearer token value.

  - `DisplayName param.Field[string]`

    Body param: Updated human-readable name for the credential. 1-255 characters.

  - `Metadata param.Field[map[string, string]]`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

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

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

        - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

        - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

    - `const BetaManagedAgentsCredentialTypeVaultCredential BetaManagedAgentsCredentialType = "vault_credential"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string`

    Human-readable name for the credential.

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
  betaManagedAgentsCredential, err := client.Beta.Vaults.Credentials.Update(
    context.TODO(),
    "vcrd_011CZkZEMt8gZan2iYOQfSkw",
    anthropic.BetaVaultCredentialUpdateParams{
      VaultID: "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsCredential.ID)
}
```

## Delete

`client.Beta.Vaults.Credentials.Delete(ctx, credentialID, params) (*BetaManagedAgentsDeletedCredential, error)`

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `credentialID string`

- `params BetaVaultCredentialDeleteParams`

  - `VaultID param.Field[string]`

    Path param: Path parameter vault_id

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

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsDeletedCredential struct{…}`

  Confirmation of a deleted credential.

  - `ID string`

    Unique identifier of the deleted credential.

  - `Type BetaManagedAgentsDeletedCredentialType`

    - `const BetaManagedAgentsDeletedCredentialTypeVaultCredentialDeleted BetaManagedAgentsDeletedCredentialType = "vault_credential_deleted"`

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
  betaManagedAgentsDeletedCredential, err := client.Beta.Vaults.Credentials.Delete(
    context.TODO(),
    "vcrd_011CZkZEMt8gZan2iYOQfSkw",
    anthropic.BetaVaultCredentialDeleteParams{
      VaultID: "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeletedCredential.ID)
}
```

## Archive

`client.Beta.Vaults.Credentials.Archive(ctx, credentialID, params) (*BetaManagedAgentsCredential, error)`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `credentialID string`

- `params BetaVaultCredentialArchiveParams`

  - `VaultID param.Field[string]`

    Path param: Path parameter vault_id

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

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

        - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

        - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

    - `const BetaManagedAgentsCredentialTypeVaultCredential BetaManagedAgentsCredentialType = "vault_credential"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string`

    Human-readable name for the credential.

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
  betaManagedAgentsCredential, err := client.Beta.Vaults.Credentials.Archive(
    context.TODO(),
    "vcrd_011CZkZEMt8gZan2iYOQfSkw",
    anthropic.BetaVaultCredentialArchiveParams{
      VaultID: "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsCredential.ID)
}
```

## Domain Types

### Beta Managed Agents Credential

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

        - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

        - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

    - `const BetaManagedAgentsCredentialTypeVaultCredential BetaManagedAgentsCredentialType = "vault_credential"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string`

    Human-readable name for the credential.

### Beta Managed Agents Deleted Credential

- `type BetaManagedAgentsDeletedCredential struct{…}`

  Confirmation of a deleted credential.

  - `ID string`

    Unique identifier of the deleted credential.

  - `Type BetaManagedAgentsDeletedCredentialType`

    - `const BetaManagedAgentsDeletedCredentialTypeVaultCredentialDeleted BetaManagedAgentsDeletedCredentialType = "vault_credential_deleted"`

### Beta Managed Agents MCP OAuth Auth Response

- `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

  OAuth credential details for an MCP server.

  - `MCPServerURL string`

    URL of the MCP server this credential authenticates against.

  - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

    - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

    OAuth refresh token configuration returned in credential responses.

    - `ClientID string`

      OAuth client ID.

    - `TokenEndpoint string`

      Token endpoint URL used to refresh the access token.

    - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

      Token endpoint requires no client authentication.

      - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

        Token endpoint requires no client authentication.

        - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

          - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

      - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

          - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

      - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

        Token endpoint uses POST body authentication with client credentials.

        - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

          - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

    - `Resource string`

      OAuth resource indicator.

    - `Scope string`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Create Params

- `type BetaManagedAgentsMCPOAuthCreateParamsResp struct{…}`

  Parameters for creating an MCP OAuth credential.

  - `AccessToken string`

    OAuth access token.

  - `MCPServerURL string`

    URL of the MCP server this credential authenticates against.

  - `Type BetaManagedAgentsMCPOAuthCreateParamsType`

    - `const BetaManagedAgentsMCPOAuthCreateParamsTypeMCPOAuth BetaManagedAgentsMCPOAuthCreateParamsType = "mcp_oauth"`

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Refresh BetaManagedAgentsMCPOAuthRefreshParamsResp`

    OAuth refresh token parameters for creating a credential with refresh support.

    - `ClientID string`

      OAuth client ID.

    - `RefreshToken string`

      OAuth refresh token.

    - `TokenEndpoint string`

      Token endpoint URL used to refresh the access token.

    - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshParamsTokenEndpointAuthUnionResp`

      Token endpoint requires no client authentication.

      - `type BetaManagedAgentsTokenEndpointAuthNoneParamResp struct{…}`

        Token endpoint requires no client authentication.

        - `Type BetaManagedAgentsTokenEndpointAuthNoneParamType`

          - `const BetaManagedAgentsTokenEndpointAuthNoneParamTypeNone BetaManagedAgentsTokenEndpointAuthNoneParamType = "none"`

      - `type BetaManagedAgentsTokenEndpointAuthBasicParamResp struct{…}`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `ClientSecret string`

          OAuth client secret.

        - `Type BetaManagedAgentsTokenEndpointAuthBasicParamType`

          - `const BetaManagedAgentsTokenEndpointAuthBasicParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicParamType = "client_secret_basic"`

      - `type BetaManagedAgentsTokenEndpointAuthPostParamResp struct{…}`

        Token endpoint uses POST body authentication with client credentials.

        - `ClientSecret string`

          OAuth client secret.

        - `Type BetaManagedAgentsTokenEndpointAuthPostParamType`

          - `const BetaManagedAgentsTokenEndpointAuthPostParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostParamType = "client_secret_post"`

    - `Resource string`

      OAuth resource indicator.

    - `Scope string`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Params

- `type BetaManagedAgentsMCPOAuthRefreshParamsResp struct{…}`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `ClientID string`

    OAuth client ID.

  - `RefreshToken string`

    OAuth refresh token.

  - `TokenEndpoint string`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshParamsTokenEndpointAuthUnionResp`

    Token endpoint requires no client authentication.

    - `type BetaManagedAgentsTokenEndpointAuthNoneParamResp struct{…}`

      Token endpoint requires no client authentication.

      - `Type BetaManagedAgentsTokenEndpointAuthNoneParamType`

        - `const BetaManagedAgentsTokenEndpointAuthNoneParamTypeNone BetaManagedAgentsTokenEndpointAuthNoneParamType = "none"`

    - `type BetaManagedAgentsTokenEndpointAuthBasicParamResp struct{…}`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `ClientSecret string`

        OAuth client secret.

      - `Type BetaManagedAgentsTokenEndpointAuthBasicParamType`

        - `const BetaManagedAgentsTokenEndpointAuthBasicParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicParamType = "client_secret_basic"`

    - `type BetaManagedAgentsTokenEndpointAuthPostParamResp struct{…}`

      Token endpoint uses POST body authentication with client credentials.

      - `ClientSecret string`

        OAuth client secret.

      - `Type BetaManagedAgentsTokenEndpointAuthPostParamType`

        - `const BetaManagedAgentsTokenEndpointAuthPostParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostParamType = "client_secret_post"`

  - `Resource string`

    OAuth resource indicator.

  - `Scope string`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `type BetaManagedAgentsMCPOAuthRefreshResponse struct{…}`

  OAuth refresh token configuration returned in credential responses.

  - `ClientID string`

    OAuth client ID.

  - `TokenEndpoint string`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

    Token endpoint requires no client authentication.

    - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

      Token endpoint requires no client authentication.

      - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

        - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

    - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

        - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

    - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

      Token endpoint uses POST body authentication with client credentials.

      - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

        - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

  - `Resource string`

    OAuth resource indicator.

  - `Scope string`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `type BetaManagedAgentsMCPOAuthRefreshUpdateParamsResp struct{…}`

  Parameters for updating OAuth refresh token configuration.

  - `RefreshToken string`

    Updated OAuth refresh token.

  - `Scope string`

    Updated OAuth scope for the refresh request.

  - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshUpdateParamsTokenEndpointAuthUnionResp`

    Updated HTTP Basic authentication parameters for the token endpoint.

    - `type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamResp struct{…}`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `Type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType`

        - `const BetaManagedAgentsTokenEndpointAuthBasicUpdateParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType = "client_secret_basic"`

      - `ClientSecret string`

        Updated OAuth client secret.

    - `type BetaManagedAgentsTokenEndpointAuthPostUpdateParamResp struct{…}`

      Updated POST body authentication parameters for the token endpoint.

      - `Type BetaManagedAgentsTokenEndpointAuthPostUpdateParamType`

        - `const BetaManagedAgentsTokenEndpointAuthPostUpdateParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostUpdateParamType = "client_secret_post"`

      - `ClientSecret string`

        Updated OAuth client secret.

### Beta Managed Agents MCP OAuth Update Params

- `type BetaManagedAgentsMCPOAuthUpdateParamsResp struct{…}`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `Type BetaManagedAgentsMCPOAuthUpdateParamsType`

    - `const BetaManagedAgentsMCPOAuthUpdateParamsTypeMCPOAuth BetaManagedAgentsMCPOAuthUpdateParamsType = "mcp_oauth"`

  - `AccessToken string`

    Updated OAuth access token.

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Refresh BetaManagedAgentsMCPOAuthRefreshUpdateParamsResp`

    Parameters for updating OAuth refresh token configuration.

    - `RefreshToken string`

      Updated OAuth refresh token.

    - `Scope string`

      Updated OAuth scope for the refresh request.

    - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshUpdateParamsTokenEndpointAuthUnionResp`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamResp struct{…}`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `Type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType`

          - `const BetaManagedAgentsTokenEndpointAuthBasicUpdateParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType = "client_secret_basic"`

        - `ClientSecret string`

          Updated OAuth client secret.

      - `type BetaManagedAgentsTokenEndpointAuthPostUpdateParamResp struct{…}`

        Updated POST body authentication parameters for the token endpoint.

        - `Type BetaManagedAgentsTokenEndpointAuthPostUpdateParamType`

          - `const BetaManagedAgentsTokenEndpointAuthPostUpdateParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostUpdateParamType = "client_secret_post"`

        - `ClientSecret string`

          Updated OAuth client secret.

### Beta Managed Agents Static Bearer Auth Response

- `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

  Static bearer token credential details for an MCP server.

  - `MCPServerURL string`

    URL of the MCP server this credential authenticates against.

  - `Type BetaManagedAgentsStaticBearerAuthResponseType`

    - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

### Beta Managed Agents Static Bearer Create Params

- `type BetaManagedAgentsStaticBearerCreateParamsResp struct{…}`

  Parameters for creating a static bearer token credential.

  - `Token string`

    Static bearer token value.

  - `MCPServerURL string`

    URL of the MCP server this credential authenticates against.

  - `Type BetaManagedAgentsStaticBearerCreateParamsType`

    - `const BetaManagedAgentsStaticBearerCreateParamsTypeStaticBearer BetaManagedAgentsStaticBearerCreateParamsType = "static_bearer"`

### Beta Managed Agents Static Bearer Update Params

- `type BetaManagedAgentsStaticBearerUpdateParamsResp struct{…}`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `Type BetaManagedAgentsStaticBearerUpdateParamsType`

    - `const BetaManagedAgentsStaticBearerUpdateParamsTypeStaticBearer BetaManagedAgentsStaticBearerUpdateParamsType = "static_bearer"`

  - `Token string`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `type BetaManagedAgentsTokenEndpointAuthBasicParamResp struct{…}`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `ClientSecret string`

    OAuth client secret.

  - `Type BetaManagedAgentsTokenEndpointAuthBasicParamType`

    - `const BetaManagedAgentsTokenEndpointAuthBasicParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicParamType = "client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

    - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamResp struct{…}`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `Type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType`

    - `const BetaManagedAgentsTokenEndpointAuthBasicUpdateParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType = "client_secret_basic"`

  - `ClientSecret string`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `type BetaManagedAgentsTokenEndpointAuthNoneParamResp struct{…}`

  Token endpoint requires no client authentication.

  - `Type BetaManagedAgentsTokenEndpointAuthNoneParamType`

    - `const BetaManagedAgentsTokenEndpointAuthNoneParamTypeNone BetaManagedAgentsTokenEndpointAuthNoneParamType = "none"`

### Beta Managed Agents Token Endpoint Auth None Response

- `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

  Token endpoint requires no client authentication.

  - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

    - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

### Beta Managed Agents Token Endpoint Auth Post Param

- `type BetaManagedAgentsTokenEndpointAuthPostParamResp struct{…}`

  Token endpoint uses POST body authentication with client credentials.

  - `ClientSecret string`

    OAuth client secret.

  - `Type BetaManagedAgentsTokenEndpointAuthPostParamType`

    - `const BetaManagedAgentsTokenEndpointAuthPostParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostParamType = "client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Response

- `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

  Token endpoint uses POST body authentication with client credentials.

  - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

    - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `type BetaManagedAgentsTokenEndpointAuthPostUpdateParamResp struct{…}`

  Updated POST body authentication parameters for the token endpoint.

  - `Type BetaManagedAgentsTokenEndpointAuthPostUpdateParamType`

    - `const BetaManagedAgentsTokenEndpointAuthPostUpdateParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostUpdateParamType = "client_secret_post"`

  - `ClientSecret string`

    Updated OAuth client secret.

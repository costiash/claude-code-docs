# Memory Stores

## Create

`client.Beta.MemoryStores.New(ctx, params) (*BetaManagedAgentsMemoryStore, error)`

**post** `/v1/memory_stores`

CreateMemoryStore

### Parameters

- `params BetaMemoryStoreNewParams`

  - `Name param.Field[string]`

    Body param

  - `Description param.Field[string]`

    Body param

  - `Metadata param.Field[map[string, string]]`

    Body param

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

- `type BetaManagedAgentsMemoryStore struct{…}`

  - `ID string`

  - `Type BetaManagedAgentsMemoryStoreType`

    - `const BetaManagedAgentsMemoryStoreTypeMemoryStore BetaManagedAgentsMemoryStoreType = "memory_store"`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `Metadata map[string, string]`

  - `Name string`

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
  betaManagedAgentsMemoryStore, err := client.Beta.MemoryStores.New(context.TODO(), anthropic.BetaMemoryStoreNewParams{
    Name: "x",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemoryStore.ID)
}
```

## List

`client.Beta.MemoryStores.List(ctx, params) (*PageCursor[BetaManagedAgentsMemoryStore], error)`

**get** `/v1/memory_stores`

ListMemoryStores

### Parameters

- `params BetaMemoryStoreListParams`

  - `CreatedAtGte param.Field[Time]`

    Query param: Return stores created at or after this time (inclusive).

  - `CreatedAtLte param.Field[Time]`

    Query param: Return stores created at or before this time (inclusive).

  - `IncludeArchived param.Field[bool]`

    Query param: Query parameter for include_archived

  - `Limit param.Field[int64]`

    Query param: Query parameter for limit

  - `Page param.Field[string]`

    Query param: Query parameter for page

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

- `type BetaManagedAgentsMemoryStore struct{…}`

  - `ID string`

  - `Type BetaManagedAgentsMemoryStoreType`

    - `const BetaManagedAgentsMemoryStoreTypeMemoryStore BetaManagedAgentsMemoryStoreType = "memory_store"`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `Metadata map[string, string]`

  - `Name string`

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
  page, err := client.Beta.MemoryStores.List(context.TODO(), anthropic.BetaMemoryStoreListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Retrieve

`client.Beta.MemoryStores.Get(ctx, memoryStoreID, query) (*BetaManagedAgentsMemoryStore, error)`

**get** `/v1/memory_stores/{memory_store_id}`

GetMemoryStore

### Parameters

- `memoryStoreID string`

- `query BetaMemoryStoreGetParams`

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

- `type BetaManagedAgentsMemoryStore struct{…}`

  - `ID string`

  - `Type BetaManagedAgentsMemoryStoreType`

    - `const BetaManagedAgentsMemoryStoreTypeMemoryStore BetaManagedAgentsMemoryStoreType = "memory_store"`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `Metadata map[string, string]`

  - `Name string`

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
  betaManagedAgentsMemoryStore, err := client.Beta.MemoryStores.Get(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemoryStore.ID)
}
```

## Update

`client.Beta.MemoryStores.Update(ctx, memoryStoreID, params) (*BetaManagedAgentsMemoryStore, error)`

**post** `/v1/memory_stores/{memory_store_id}`

UpdateMemoryStore

### Parameters

- `memoryStoreID string`

- `params BetaMemoryStoreUpdateParams`

  - `Description param.Field[string]`

    Body param

  - `Metadata param.Field[map[string, string]]`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Name param.Field[string]`

    Body param

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

- `type BetaManagedAgentsMemoryStore struct{…}`

  - `ID string`

  - `Type BetaManagedAgentsMemoryStoreType`

    - `const BetaManagedAgentsMemoryStoreTypeMemoryStore BetaManagedAgentsMemoryStoreType = "memory_store"`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `Metadata map[string, string]`

  - `Name string`

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
  betaManagedAgentsMemoryStore, err := client.Beta.MemoryStores.Update(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemoryStore.ID)
}
```

## Delete

`client.Beta.MemoryStores.Delete(ctx, memoryStoreID, body) (*BetaManagedAgentsDeletedMemoryStore, error)`

**delete** `/v1/memory_stores/{memory_store_id}`

DeleteMemoryStore

### Parameters

- `memoryStoreID string`

- `body BetaMemoryStoreDeleteParams`

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

- `type BetaManagedAgentsDeletedMemoryStore struct{…}`

  - `ID string`

  - `Type BetaManagedAgentsDeletedMemoryStoreType`

    - `const BetaManagedAgentsDeletedMemoryStoreTypeMemoryStoreDeleted BetaManagedAgentsDeletedMemoryStoreType = "memory_store_deleted"`

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
  betaManagedAgentsDeletedMemoryStore, err := client.Beta.MemoryStores.Delete(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeletedMemoryStore.ID)
}
```

## Archive

`client.Beta.MemoryStores.Archive(ctx, memoryStoreID, body) (*BetaManagedAgentsMemoryStore, error)`

**post** `/v1/memory_stores/{memory_store_id}/archive`

ArchiveMemoryStore

### Parameters

- `memoryStoreID string`

- `body BetaMemoryStoreArchiveParams`

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

- `type BetaManagedAgentsMemoryStore struct{…}`

  - `ID string`

  - `Type BetaManagedAgentsMemoryStoreType`

    - `const BetaManagedAgentsMemoryStoreTypeMemoryStore BetaManagedAgentsMemoryStoreType = "memory_store"`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `Metadata map[string, string]`

  - `Name string`

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
  betaManagedAgentsMemoryStore, err := client.Beta.MemoryStores.Archive(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreArchiveParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemoryStore.ID)
}
```

## Domain Types

### Beta Managed Agents Deleted Memory Store

- `type BetaManagedAgentsDeletedMemoryStore struct{…}`

  - `ID string`

  - `Type BetaManagedAgentsDeletedMemoryStoreType`

    - `const BetaManagedAgentsDeletedMemoryStoreTypeMemoryStoreDeleted BetaManagedAgentsDeletedMemoryStoreType = "memory_store_deleted"`

### Beta Managed Agents Memory Store

- `type BetaManagedAgentsMemoryStore struct{…}`

  - `ID string`

  - `Type BetaManagedAgentsMemoryStoreType`

    - `const BetaManagedAgentsMemoryStoreTypeMemoryStore BetaManagedAgentsMemoryStoreType = "memory_store"`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `Metadata map[string, string]`

  - `Name string`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

# Memories

## Create

`client.Beta.MemoryStores.Memories.New(ctx, memoryStoreID, params) (*BetaManagedAgentsMemory, error)`

**post** `/v1/memory_stores/{memory_store_id}/memories`

CreateMemory

### Parameters

- `memoryStoreID string`

- `params BetaMemoryStoreMemoryNewParams`

  - `Content param.Field[string]`

    Body param

  - `Path param.Field[string]`

    Body param

  - `View param.Field[BetaManagedAgentsMemoryView]`

    Query param: Query parameter for view

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

- `type BetaManagedAgentsMemory struct{…}`

  - `ID string`

  - `ContentSha256 string`

  - `ContentSizeBytes int64`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryStoreID string`

  - `MemoryVersionID string`

  - `Path string`

  - `Type BetaManagedAgentsMemoryType`

    - `const BetaManagedAgentsMemoryTypeMemory BetaManagedAgentsMemoryType = "memory"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Content string`

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
  betaManagedAgentsMemory, err := client.Beta.MemoryStores.Memories.New(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreMemoryNewParams{
      Content: anthropic.String("content"),
      Path: "xx",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemory.ID)
}
```

## List

`client.Beta.MemoryStores.Memories.List(ctx, memoryStoreID, params) (*PageCursor[BetaManagedAgentsMemoryListItemUnion], error)`

**get** `/v1/memory_stores/{memory_store_id}/memories`

ListMemories

### Parameters

- `memoryStoreID string`

- `params BetaMemoryStoreMemoryListParams`

  - `Depth param.Field[int64]`

    Query param: Query parameter for depth

  - `Limit param.Field[int64]`

    Query param: Query parameter for limit

  - `Order param.Field[BetaMemoryStoreMemoryListParamsOrder]`

    Query param: Query parameter for order

    - `const BetaMemoryStoreMemoryListParamsOrderAsc BetaMemoryStoreMemoryListParamsOrder = "asc"`

    - `const BetaMemoryStoreMemoryListParamsOrderDesc BetaMemoryStoreMemoryListParamsOrder = "desc"`

  - `OrderBy param.Field[string]`

    Query param: Query parameter for order_by

  - `Page param.Field[string]`

    Query param: Query parameter for page

  - `PathPrefix param.Field[string]`

    Query param: Optional path prefix filter (raw string-prefix match; include a trailing slash for directory-scoped lists). This value appears in request URLs. Do not include secrets or personally identifiable information.

  - `View param.Field[BetaManagedAgentsMemoryView]`

    Query param: Query parameter for view

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

- `type BetaManagedAgentsMemoryListItemUnion interface{…}`

  - `type BetaManagedAgentsMemory struct{…}`

    - `ID string`

    - `ContentSha256 string`

    - `ContentSizeBytes int64`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `MemoryStoreID string`

    - `MemoryVersionID string`

    - `Path string`

    - `Type BetaManagedAgentsMemoryType`

      - `const BetaManagedAgentsMemoryTypeMemory BetaManagedAgentsMemoryType = "memory"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

    - `Content string`

  - `type BetaManagedAgentsMemoryPrefix struct{…}`

    - `Path string`

    - `Type BetaManagedAgentsMemoryPrefixType`

      - `const BetaManagedAgentsMemoryPrefixTypeMemoryPrefix BetaManagedAgentsMemoryPrefixType = "memory_prefix"`

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
  page, err := client.Beta.MemoryStores.Memories.List(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreMemoryListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Retrieve

`client.Beta.MemoryStores.Memories.Get(ctx, memoryID, params) (*BetaManagedAgentsMemory, error)`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

GetMemory

### Parameters

- `memoryID string`

- `params BetaMemoryStoreMemoryGetParams`

  - `MemoryStoreID param.Field[string]`

    Path param: Path parameter memory_store_id

  - `View param.Field[BetaManagedAgentsMemoryView]`

    Query param: Query parameter for view

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

- `type BetaManagedAgentsMemory struct{…}`

  - `ID string`

  - `ContentSha256 string`

  - `ContentSizeBytes int64`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryStoreID string`

  - `MemoryVersionID string`

  - `Path string`

  - `Type BetaManagedAgentsMemoryType`

    - `const BetaManagedAgentsMemoryTypeMemory BetaManagedAgentsMemoryType = "memory"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Content string`

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
  betaManagedAgentsMemory, err := client.Beta.MemoryStores.Memories.Get(
    context.TODO(),
    "memory_id",
    anthropic.BetaMemoryStoreMemoryGetParams{
      MemoryStoreID: "memory_store_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemory.ID)
}
```

## Update

`client.Beta.MemoryStores.Memories.Update(ctx, memoryID, params) (*BetaManagedAgentsMemory, error)`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

UpdateMemory

### Parameters

- `memoryID string`

- `params BetaMemoryStoreMemoryUpdateParams`

  - `MemoryStoreID param.Field[string]`

    Path param: Path parameter memory_store_id

  - `View param.Field[BetaManagedAgentsMemoryView]`

    Query param: Query parameter for view

  - `Content param.Field[string]`

    Body param

  - `Path param.Field[string]`

    Body param

  - `Precondition param.Field[BetaManagedAgentsPrecondition]`

    Body param

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

- `type BetaManagedAgentsMemory struct{…}`

  - `ID string`

  - `ContentSha256 string`

  - `ContentSizeBytes int64`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryStoreID string`

  - `MemoryVersionID string`

  - `Path string`

  - `Type BetaManagedAgentsMemoryType`

    - `const BetaManagedAgentsMemoryTypeMemory BetaManagedAgentsMemoryType = "memory"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Content string`

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
  betaManagedAgentsMemory, err := client.Beta.MemoryStores.Memories.Update(
    context.TODO(),
    "memory_id",
    anthropic.BetaMemoryStoreMemoryUpdateParams{
      MemoryStoreID: "memory_store_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemory.ID)
}
```

## Delete

`client.Beta.MemoryStores.Memories.Delete(ctx, memoryID, params) (*BetaManagedAgentsDeletedMemory, error)`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

DeleteMemory

### Parameters

- `memoryID string`

- `params BetaMemoryStoreMemoryDeleteParams`

  - `MemoryStoreID param.Field[string]`

    Path param: Path parameter memory_store_id

  - `ExpectedContentSha256 param.Field[string]`

    Query param: Query parameter for expected_content_sha256

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

- `type BetaManagedAgentsDeletedMemory struct{…}`

  - `ID string`

  - `Type BetaManagedAgentsDeletedMemoryType`

    - `const BetaManagedAgentsDeletedMemoryTypeMemoryDeleted BetaManagedAgentsDeletedMemoryType = "memory_deleted"`

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
  betaManagedAgentsDeletedMemory, err := client.Beta.MemoryStores.Memories.Delete(
    context.TODO(),
    "memory_id",
    anthropic.BetaMemoryStoreMemoryDeleteParams{
      MemoryStoreID: "memory_store_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeletedMemory.ID)
}
```

## Domain Types

### Beta Managed Agents Content Sha256 Precondition

- `type BetaManagedAgentsContentSha256Precondition struct{…}`

  - `Type BetaManagedAgentsContentSha256PreconditionType`

    - `const BetaManagedAgentsContentSha256PreconditionTypeContentSha256 BetaManagedAgentsContentSha256PreconditionType = "content_sha256"`

  - `ContentSha256 string`

### Beta Managed Agents Deleted Memory

- `type BetaManagedAgentsDeletedMemory struct{…}`

  - `ID string`

  - `Type BetaManagedAgentsDeletedMemoryType`

    - `const BetaManagedAgentsDeletedMemoryTypeMemoryDeleted BetaManagedAgentsDeletedMemoryType = "memory_deleted"`

### Beta Managed Agents Memory

- `type BetaManagedAgentsMemory struct{…}`

  - `ID string`

  - `ContentSha256 string`

  - `ContentSizeBytes int64`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryStoreID string`

  - `MemoryVersionID string`

  - `Path string`

  - `Type BetaManagedAgentsMemoryType`

    - `const BetaManagedAgentsMemoryTypeMemory BetaManagedAgentsMemoryType = "memory"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Content string`

### Beta Managed Agents Memory List Item

- `type BetaManagedAgentsMemoryListItemUnion interface{…}`

  - `type BetaManagedAgentsMemory struct{…}`

    - `ID string`

    - `ContentSha256 string`

    - `ContentSizeBytes int64`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `MemoryStoreID string`

    - `MemoryVersionID string`

    - `Path string`

    - `Type BetaManagedAgentsMemoryType`

      - `const BetaManagedAgentsMemoryTypeMemory BetaManagedAgentsMemoryType = "memory"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

    - `Content string`

  - `type BetaManagedAgentsMemoryPrefix struct{…}`

    - `Path string`

    - `Type BetaManagedAgentsMemoryPrefixType`

      - `const BetaManagedAgentsMemoryPrefixTypeMemoryPrefix BetaManagedAgentsMemoryPrefixType = "memory_prefix"`

### Beta Managed Agents Memory Path Conflict Error

- `type BetaManagedAgentsMemoryPathConflictError struct{…}`

  - `Type BetaManagedAgentsMemoryPathConflictErrorType`

    - `const BetaManagedAgentsMemoryPathConflictErrorTypeMemoryPathConflictError BetaManagedAgentsMemoryPathConflictErrorType = "memory_path_conflict_error"`

  - `ConflictingMemoryID string`

  - `ConflictingPath string`

  - `Message string`

### Beta Managed Agents Memory Precondition Failed Error

- `type BetaManagedAgentsMemoryPreconditionFailedError struct{…}`

  - `Type BetaManagedAgentsMemoryPreconditionFailedErrorType`

    - `const BetaManagedAgentsMemoryPreconditionFailedErrorTypeMemoryPreconditionFailedError BetaManagedAgentsMemoryPreconditionFailedErrorType = "memory_precondition_failed_error"`

  - `Message string`

### Beta Managed Agents Memory Prefix

- `type BetaManagedAgentsMemoryPrefix struct{…}`

  - `Path string`

  - `Type BetaManagedAgentsMemoryPrefixType`

    - `const BetaManagedAgentsMemoryPrefixTypeMemoryPrefix BetaManagedAgentsMemoryPrefixType = "memory_prefix"`

### Beta Managed Agents Memory View

- `type BetaManagedAgentsMemoryView string`

  MemoryView enum

  - `const BetaManagedAgentsMemoryViewBasic BetaManagedAgentsMemoryView = "basic"`

  - `const BetaManagedAgentsMemoryViewFull BetaManagedAgentsMemoryView = "full"`

### Beta Managed Agents Precondition

- `type BetaManagedAgentsPrecondition struct{…}`

  - `Type BetaManagedAgentsPreconditionType`

    - `const BetaManagedAgentsPreconditionTypeContentSha256 BetaManagedAgentsPreconditionType = "content_sha256"`

  - `ContentSha256 string`

# Memory Versions

## List

`client.Beta.MemoryStores.MemoryVersions.List(ctx, memoryStoreID, params) (*PageCursor[BetaManagedAgentsMemoryVersion], error)`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

ListMemoryVersions

### Parameters

- `memoryStoreID string`

- `params BetaMemoryStoreMemoryVersionListParams`

  - `APIKeyID param.Field[string]`

    Query param: Query parameter for api_key_id

  - `CreatedAtGte param.Field[Time]`

    Query param: Return versions created at or after this time (inclusive).

  - `CreatedAtLte param.Field[Time]`

    Query param: Return versions created at or before this time (inclusive).

  - `Limit param.Field[int64]`

    Query param: Query parameter for limit

  - `MemoryID param.Field[string]`

    Query param: Query parameter for memory_id

  - `Operation param.Field[BetaManagedAgentsMemoryVersionOperation]`

    Query param: Query parameter for operation

  - `Page param.Field[string]`

    Query param: Query parameter for page

  - `SessionID param.Field[string]`

    Query param: Query parameter for session_id

  - `View param.Field[BetaManagedAgentsMemoryView]`

    Query param: Query parameter for view

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

- `type BetaManagedAgentsMemoryVersion struct{…}`

  - `ID string`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryID string`

  - `MemoryStoreID string`

  - `Operation BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `const BetaManagedAgentsMemoryVersionOperationCreated BetaManagedAgentsMemoryVersionOperation = "created"`

    - `const BetaManagedAgentsMemoryVersionOperationModified BetaManagedAgentsMemoryVersionOperation = "modified"`

    - `const BetaManagedAgentsMemoryVersionOperationDeleted BetaManagedAgentsMemoryVersionOperation = "deleted"`

  - `Type BetaManagedAgentsMemoryVersionType`

    - `const BetaManagedAgentsMemoryVersionTypeMemoryVersion BetaManagedAgentsMemoryVersionType = "memory_version"`

  - `Content string`

  - `ContentSha256 string`

  - `ContentSizeBytes int64`

  - `CreatedBy BetaManagedAgentsActorUnion`

    - `type BetaManagedAgentsSessionActor struct{…}`

      - `SessionID string`

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      - `APIKeyID string`

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

  - `Path string`

  - `RedactedAt Time`

    A timestamp in RFC 3339 format

  - `RedactedBy BetaManagedAgentsActorUnion`

    - `type BetaManagedAgentsSessionActor struct{…}`

      - `SessionID string`

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      - `APIKeyID string`

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

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
  page, err := client.Beta.MemoryStores.MemoryVersions.List(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreMemoryVersionListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Retrieve

`client.Beta.MemoryStores.MemoryVersions.Get(ctx, memoryVersionID, params) (*BetaManagedAgentsMemoryVersion, error)`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

GetMemoryVersion

### Parameters

- `memoryVersionID string`

- `params BetaMemoryStoreMemoryVersionGetParams`

  - `MemoryStoreID param.Field[string]`

    Path param: Path parameter memory_store_id

  - `View param.Field[BetaManagedAgentsMemoryView]`

    Query param: Query parameter for view

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

- `type BetaManagedAgentsMemoryVersion struct{…}`

  - `ID string`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryID string`

  - `MemoryStoreID string`

  - `Operation BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `const BetaManagedAgentsMemoryVersionOperationCreated BetaManagedAgentsMemoryVersionOperation = "created"`

    - `const BetaManagedAgentsMemoryVersionOperationModified BetaManagedAgentsMemoryVersionOperation = "modified"`

    - `const BetaManagedAgentsMemoryVersionOperationDeleted BetaManagedAgentsMemoryVersionOperation = "deleted"`

  - `Type BetaManagedAgentsMemoryVersionType`

    - `const BetaManagedAgentsMemoryVersionTypeMemoryVersion BetaManagedAgentsMemoryVersionType = "memory_version"`

  - `Content string`

  - `ContentSha256 string`

  - `ContentSizeBytes int64`

  - `CreatedBy BetaManagedAgentsActorUnion`

    - `type BetaManagedAgentsSessionActor struct{…}`

      - `SessionID string`

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      - `APIKeyID string`

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

  - `Path string`

  - `RedactedAt Time`

    A timestamp in RFC 3339 format

  - `RedactedBy BetaManagedAgentsActorUnion`

    - `type BetaManagedAgentsSessionActor struct{…}`

      - `SessionID string`

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      - `APIKeyID string`

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

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
  betaManagedAgentsMemoryVersion, err := client.Beta.MemoryStores.MemoryVersions.Get(
    context.TODO(),
    "memory_version_id",
    anthropic.BetaMemoryStoreMemoryVersionGetParams{
      MemoryStoreID: "memory_store_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemoryVersion.ID)
}
```

## Redact

`client.Beta.MemoryStores.MemoryVersions.Redact(ctx, memoryVersionID, params) (*BetaManagedAgentsMemoryVersion, error)`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

RedactMemoryVersion

### Parameters

- `memoryVersionID string`

- `params BetaMemoryStoreMemoryVersionRedactParams`

  - `MemoryStoreID param.Field[string]`

    Path param: Path parameter memory_store_id

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

- `type BetaManagedAgentsMemoryVersion struct{…}`

  - `ID string`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryID string`

  - `MemoryStoreID string`

  - `Operation BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `const BetaManagedAgentsMemoryVersionOperationCreated BetaManagedAgentsMemoryVersionOperation = "created"`

    - `const BetaManagedAgentsMemoryVersionOperationModified BetaManagedAgentsMemoryVersionOperation = "modified"`

    - `const BetaManagedAgentsMemoryVersionOperationDeleted BetaManagedAgentsMemoryVersionOperation = "deleted"`

  - `Type BetaManagedAgentsMemoryVersionType`

    - `const BetaManagedAgentsMemoryVersionTypeMemoryVersion BetaManagedAgentsMemoryVersionType = "memory_version"`

  - `Content string`

  - `ContentSha256 string`

  - `ContentSizeBytes int64`

  - `CreatedBy BetaManagedAgentsActorUnion`

    - `type BetaManagedAgentsSessionActor struct{…}`

      - `SessionID string`

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      - `APIKeyID string`

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

  - `Path string`

  - `RedactedAt Time`

    A timestamp in RFC 3339 format

  - `RedactedBy BetaManagedAgentsActorUnion`

    - `type BetaManagedAgentsSessionActor struct{…}`

      - `SessionID string`

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      - `APIKeyID string`

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

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
  betaManagedAgentsMemoryVersion, err := client.Beta.MemoryStores.MemoryVersions.Redact(
    context.TODO(),
    "memory_version_id",
    anthropic.BetaMemoryStoreMemoryVersionRedactParams{
      MemoryStoreID: "memory_store_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemoryVersion.ID)
}
```

## Domain Types

### Beta Managed Agents Actor

- `type BetaManagedAgentsActorUnion interface{…}`

  - `type BetaManagedAgentsSessionActor struct{…}`

    - `SessionID string`

    - `Type BetaManagedAgentsSessionActorType`

      - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

  - `type BetaManagedAgentsAPIActor struct{…}`

    - `APIKeyID string`

    - `Type BetaManagedAgentsAPIActorType`

      - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

  - `type BetaManagedAgentsUserActor struct{…}`

    - `Type BetaManagedAgentsUserActorType`

      - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

    - `UserID string`

### Beta Managed Agents API Actor

- `type BetaManagedAgentsAPIActor struct{…}`

  - `APIKeyID string`

  - `Type BetaManagedAgentsAPIActorType`

    - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

### Beta Managed Agents Memory Version

- `type BetaManagedAgentsMemoryVersion struct{…}`

  - `ID string`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryID string`

  - `MemoryStoreID string`

  - `Operation BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `const BetaManagedAgentsMemoryVersionOperationCreated BetaManagedAgentsMemoryVersionOperation = "created"`

    - `const BetaManagedAgentsMemoryVersionOperationModified BetaManagedAgentsMemoryVersionOperation = "modified"`

    - `const BetaManagedAgentsMemoryVersionOperationDeleted BetaManagedAgentsMemoryVersionOperation = "deleted"`

  - `Type BetaManagedAgentsMemoryVersionType`

    - `const BetaManagedAgentsMemoryVersionTypeMemoryVersion BetaManagedAgentsMemoryVersionType = "memory_version"`

  - `Content string`

  - `ContentSha256 string`

  - `ContentSizeBytes int64`

  - `CreatedBy BetaManagedAgentsActorUnion`

    - `type BetaManagedAgentsSessionActor struct{…}`

      - `SessionID string`

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      - `APIKeyID string`

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

  - `Path string`

  - `RedactedAt Time`

    A timestamp in RFC 3339 format

  - `RedactedBy BetaManagedAgentsActorUnion`

    - `type BetaManagedAgentsSessionActor struct{…}`

      - `SessionID string`

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      - `APIKeyID string`

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

### Beta Managed Agents Memory Version Operation

- `type BetaManagedAgentsMemoryVersionOperation string`

  MemoryVersionOperation enum

  - `const BetaManagedAgentsMemoryVersionOperationCreated BetaManagedAgentsMemoryVersionOperation = "created"`

  - `const BetaManagedAgentsMemoryVersionOperationModified BetaManagedAgentsMemoryVersionOperation = "modified"`

  - `const BetaManagedAgentsMemoryVersionOperationDeleted BetaManagedAgentsMemoryVersionOperation = "deleted"`

### Beta Managed Agents Session Actor

- `type BetaManagedAgentsSessionActor struct{…}`

  - `SessionID string`

  - `Type BetaManagedAgentsSessionActorType`

    - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

### Beta Managed Agents User Actor

- `type BetaManagedAgentsUserActor struct{…}`

  - `Type BetaManagedAgentsUserActorType`

    - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

  - `UserID string`

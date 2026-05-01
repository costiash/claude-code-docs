# Resources

## Add

`client.Beta.Sessions.Resources.Add(ctx, sessionID, params) (*BetaManagedAgentsFileResource, error)`

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Parameters

- `sessionID string`

- `params BetaSessionResourceAddParams`

  - `BetaManagedAgentsFileResourceParams param.Field[BetaManagedAgentsFileResourceParamsResp]`

    Body param: Mount a file uploaded via the Files API into the session.

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

### Returns

- `type BetaManagedAgentsFileResource struct{…}`

  - `ID string`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `FileID string`

  - `MountPath string`

  - `Type BetaManagedAgentsFileResourceType`

    - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

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
  betaManagedAgentsFileResource, err := client.Beta.Sessions.Resources.Add(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionResourceAddParams{
      BetaManagedAgentsFileResourceParams: anthropic.BetaManagedAgentsFileResourceParams{
        FileID: "file_011CNha8iCJcU1wXNR6q4V8w",
        Type: anthropic.BetaManagedAgentsFileResourceParamsTypeFile,
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsFileResource.ID)
}
```

## List

`client.Beta.Sessions.Resources.List(ctx, sessionID, params) (*PageCursor[BetaManagedAgentsSessionResourceUnion], error)`

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Parameters

- `sessionID string`

- `params BetaSessionResourceListParams`

  - `Limit param.Field[int64]`

    Query param: Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

  - `Page param.Field[string]`

    Query param: Opaque cursor from a previous response's next_page field.

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

### Returns

- `type BetaManagedAgentsSessionResourceUnion interface{…}`

  A memory store attached to an agent session.

  - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `MountPath string`

    - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

    - `URL string`

    - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

      - `type BetaManagedAgentsBranchCheckout struct{…}`

        - `Name string`

          Branch name to check out.

        - `Type BetaManagedAgentsBranchCheckoutType`

          - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

      - `type BetaManagedAgentsCommitCheckout struct{…}`

        - `Sha string`

          Full commit SHA to check out.

        - `Type BetaManagedAgentsCommitCheckoutType`

          - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

  - `type BetaManagedAgentsFileResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `FileID string`

    - `MountPath string`

    - `Type BetaManagedAgentsFileResourceType`

      - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

  - `type BetaManagedAgentsMemoryStoreResource struct{…}`

    A memory store attached to an agent session.

    - `MemoryStoreID string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type BetaManagedAgentsMemoryStoreResourceType`

      - `const BetaManagedAgentsMemoryStoreResourceTypeMemoryStore BetaManagedAgentsMemoryStoreResourceType = "memory_store"`

    - `Access BetaManagedAgentsMemoryStoreResourceAccess`

      Access mode for an attached memory store.

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

    - `Description string`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `Instructions string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `MountPath string`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `Name string`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

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
  page, err := client.Beta.Sessions.Resources.List(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionResourceListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Retrieve

`client.Beta.Sessions.Resources.Get(ctx, resourceID, params) (*BetaSessionResourceGetResponseUnion, error)`

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `resourceID string`

- `params BetaSessionResourceGetParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

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

### Returns

- `type BetaSessionResourceGetResponseUnion interface{…}`

  The requested session resource.

  - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `MountPath string`

    - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

    - `URL string`

    - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

      - `type BetaManagedAgentsBranchCheckout struct{…}`

        - `Name string`

          Branch name to check out.

        - `Type BetaManagedAgentsBranchCheckoutType`

          - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

      - `type BetaManagedAgentsCommitCheckout struct{…}`

        - `Sha string`

          Full commit SHA to check out.

        - `Type BetaManagedAgentsCommitCheckoutType`

          - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

  - `type BetaManagedAgentsFileResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `FileID string`

    - `MountPath string`

    - `Type BetaManagedAgentsFileResourceType`

      - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

  - `type BetaManagedAgentsMemoryStoreResource struct{…}`

    A memory store attached to an agent session.

    - `MemoryStoreID string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type BetaManagedAgentsMemoryStoreResourceType`

      - `const BetaManagedAgentsMemoryStoreResourceTypeMemoryStore BetaManagedAgentsMemoryStoreResourceType = "memory_store"`

    - `Access BetaManagedAgentsMemoryStoreResourceAccess`

      Access mode for an attached memory store.

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

    - `Description string`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `Instructions string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `MountPath string`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `Name string`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

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
  resource, err := client.Beta.Sessions.Resources.Get(
    context.TODO(),
    "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    anthropic.BetaSessionResourceGetParams{
      SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", resource)
}
```

## Update

`client.Beta.Sessions.Resources.Update(ctx, resourceID, params) (*BetaSessionResourceUpdateResponseUnion, error)`

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Parameters

- `resourceID string`

- `params BetaSessionResourceUpdateParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

  - `AuthorizationToken param.Field[string]`

    Body param: New authorization token for the resource. Currently only `github_repository` resources support token rotation.

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

### Returns

- `type BetaSessionResourceUpdateResponseUnion interface{…}`

  The updated session resource.

  - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `MountPath string`

    - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

    - `URL string`

    - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

      - `type BetaManagedAgentsBranchCheckout struct{…}`

        - `Name string`

          Branch name to check out.

        - `Type BetaManagedAgentsBranchCheckoutType`

          - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

      - `type BetaManagedAgentsCommitCheckout struct{…}`

        - `Sha string`

          Full commit SHA to check out.

        - `Type BetaManagedAgentsCommitCheckoutType`

          - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

  - `type BetaManagedAgentsFileResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `FileID string`

    - `MountPath string`

    - `Type BetaManagedAgentsFileResourceType`

      - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

  - `type BetaManagedAgentsMemoryStoreResource struct{…}`

    A memory store attached to an agent session.

    - `MemoryStoreID string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type BetaManagedAgentsMemoryStoreResourceType`

      - `const BetaManagedAgentsMemoryStoreResourceTypeMemoryStore BetaManagedAgentsMemoryStoreResourceType = "memory_store"`

    - `Access BetaManagedAgentsMemoryStoreResourceAccess`

      Access mode for an attached memory store.

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

    - `Description string`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `Instructions string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `MountPath string`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `Name string`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

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
  resource, err := client.Beta.Sessions.Resources.Update(
    context.TODO(),
    "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    anthropic.BetaSessionResourceUpdateParams{
      SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
      AuthorizationToken: "ghp_exampletoken",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", resource)
}
```

## Delete

`client.Beta.Sessions.Resources.Delete(ctx, resourceID, params) (*BetaManagedAgentsDeleteSessionResource, error)`

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Parameters

- `resourceID string`

- `params BetaSessionResourceDeleteParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

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

### Returns

- `type BetaManagedAgentsDeleteSessionResource struct{…}`

  Confirmation of resource deletion.

  - `ID string`

  - `Type BetaManagedAgentsDeleteSessionResourceType`

    - `const BetaManagedAgentsDeleteSessionResourceTypeSessionResourceDeleted BetaManagedAgentsDeleteSessionResourceType = "session_resource_deleted"`

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
  betaManagedAgentsDeleteSessionResource, err := client.Beta.Sessions.Resources.Delete(
    context.TODO(),
    "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    anthropic.BetaSessionResourceDeleteParams{
      SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeleteSessionResource.ID)
}
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `type BetaManagedAgentsDeleteSessionResource struct{…}`

  Confirmation of resource deletion.

  - `ID string`

  - `Type BetaManagedAgentsDeleteSessionResourceType`

    - `const BetaManagedAgentsDeleteSessionResourceTypeSessionResourceDeleted BetaManagedAgentsDeleteSessionResourceType = "session_resource_deleted"`

### Beta Managed Agents File Resource

- `type BetaManagedAgentsFileResource struct{…}`

  - `ID string`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `FileID string`

  - `MountPath string`

  - `Type BetaManagedAgentsFileResourceType`

    - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

### Beta Managed Agents GitHub Repository Resource

- `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

  - `ID string`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MountPath string`

  - `Type BetaManagedAgentsGitHubRepositoryResourceType`

    - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `URL string`

  - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

    - `type BetaManagedAgentsBranchCheckout struct{…}`

      - `Name string`

        Branch name to check out.

      - `Type BetaManagedAgentsBranchCheckoutType`

        - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

    - `type BetaManagedAgentsCommitCheckout struct{…}`

      - `Sha string`

        Full commit SHA to check out.

      - `Type BetaManagedAgentsCommitCheckoutType`

        - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

### Beta Managed Agents Memory Store Resource

- `type BetaManagedAgentsMemoryStoreResource struct{…}`

  A memory store attached to an agent session.

  - `MemoryStoreID string`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `Type BetaManagedAgentsMemoryStoreResourceType`

    - `const BetaManagedAgentsMemoryStoreResourceTypeMemoryStore BetaManagedAgentsMemoryStoreResourceType = "memory_store"`

  - `Access BetaManagedAgentsMemoryStoreResourceAccess`

    Access mode for an attached memory store.

    - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

    - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

  - `Description string`

    Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

  - `Instructions string`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `MountPath string`

    Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

  - `Name string`

    Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Beta Managed Agents Session Resource

- `type BetaManagedAgentsSessionResourceUnion interface{…}`

  A memory store attached to an agent session.

  - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `MountPath string`

    - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

    - `URL string`

    - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

      - `type BetaManagedAgentsBranchCheckout struct{…}`

        - `Name string`

          Branch name to check out.

        - `Type BetaManagedAgentsBranchCheckoutType`

          - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

      - `type BetaManagedAgentsCommitCheckout struct{…}`

        - `Sha string`

          Full commit SHA to check out.

        - `Type BetaManagedAgentsCommitCheckoutType`

          - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

  - `type BetaManagedAgentsFileResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `FileID string`

    - `MountPath string`

    - `Type BetaManagedAgentsFileResourceType`

      - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

  - `type BetaManagedAgentsMemoryStoreResource struct{…}`

    A memory store attached to an agent session.

    - `MemoryStoreID string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type BetaManagedAgentsMemoryStoreResourceType`

      - `const BetaManagedAgentsMemoryStoreResourceTypeMemoryStore BetaManagedAgentsMemoryStoreResourceType = "memory_store"`

    - `Access BetaManagedAgentsMemoryStoreResourceAccess`

      Access mode for an attached memory store.

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

    - `Description string`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `Instructions string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `MountPath string`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `Name string`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

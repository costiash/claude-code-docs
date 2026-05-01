## Retrieve

`client.Beta.MemoryStores.MemoryVersions.Get(ctx, memoryVersionID, params) (*BetaManagedAgentsMemoryVersion, error)`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

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

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

### Returns

- `type BetaManagedAgentsMemoryVersion struct{…}`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `ID string`

    Unique identifier for this version (a `memver_...` value).

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryID string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `MemoryStoreID string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `Operation BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `const BetaManagedAgentsMemoryVersionOperationCreated BetaManagedAgentsMemoryVersionOperation = "created"`

    - `const BetaManagedAgentsMemoryVersionOperationModified BetaManagedAgentsMemoryVersionOperation = "modified"`

    - `const BetaManagedAgentsMemoryVersionOperationDeleted BetaManagedAgentsMemoryVersionOperation = "deleted"`

  - `Type BetaManagedAgentsMemoryVersionType`

    - `const BetaManagedAgentsMemoryVersionTypeMemoryVersion BetaManagedAgentsMemoryVersionType = "memory_version"`

  - `Content string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `ContentSha256 string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `ContentSizeBytes int64`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `CreatedBy BetaManagedAgentsActorUnion`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `type BetaManagedAgentsSessionActor struct{…}`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `SessionID string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      Attribution for a write made directly via the public API (outside of any session).

      - `APIKeyID string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      Attribution for a write made by a human user through the Anthropic Console.

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

        ID of the user who performed the write (a `user_...` value).

  - `Path string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `RedactedAt Time`

    A timestamp in RFC 3339 format

  - `RedactedBy BetaManagedAgentsActorUnion`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `type BetaManagedAgentsSessionActor struct{…}`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `SessionID string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      Attribution for a write made directly via the public API (outside of any session).

      - `APIKeyID string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      Attribution for a write made by a human user through the Anthropic Console.

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

        ID of the user who performed the write (a `user_...` value).

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

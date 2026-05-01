## Retrieve

`BetaManagedAgentsMemoryVersion Beta.MemoryStores.MemoryVersions.Retrieve(MemoryVersionRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

### Parameters

- `MemoryVersionRetrieveParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryVersionID`

    Path param: Path parameter memory_version_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `required string ID`

    Unique identifier for this version (a `memver_...` value).

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `required string MemoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `required BetaManagedAgentsMemoryVersionOperation Operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"Created`

    - `"modified"Modified`

    - `"deleted"Deleted`

  - `required Type Type`

    - `"memory_version"MemoryVersion`

  - `string? Content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `string? ContentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Int? ContentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `BetaManagedAgentsActor CreatedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `required string SessionID`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `required Type Type`

        - `"session_actor"SessionActor`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `required string ApiKeyID`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `required Type Type`

        - `"api_actor"ApiActor`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `required Type Type`

        - `"user_actor"UserActor`

      - `required string UserID`

        ID of the user who performed the write (a `user_...` value).

  - `string? Path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `DateTimeOffset? RedactedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsActor RedactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `required string SessionID`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `required Type Type`

        - `"session_actor"SessionActor`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `required string ApiKeyID`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `required Type Type`

        - `"api_actor"ApiActor`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `required Type Type`

        - `"user_actor"UserActor`

      - `required string UserID`

        ID of the user who performed the write (a `user_...` value).

### Example

```csharp
MemoryVersionRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryVersionID = "memory_version_id",
};

var betaManagedAgentsMemoryVersion = await client.Beta.MemoryStores.MemoryVersions.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemoryVersion);
```

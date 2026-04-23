## List

`MemoryVersionListPageResponse Beta.MemoryStores.MemoryVersions.List(MemoryVersionListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

ListMemoryVersions

### Parameters

- `MemoryVersionListParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `string apiKeyID`

    Query param: Query parameter for api_key_id

  - `DateTimeOffset createdAtGte`

    Query param: Return versions created at or after this time (inclusive).

  - `DateTimeOffset createdAtLte`

    Query param: Return versions created at or before this time (inclusive).

  - `Int limit`

    Query param: Query parameter for limit

  - `string memoryID`

    Query param: Query parameter for memory_id

  - `BetaManagedAgentsMemoryVersionOperation operation`

    Query param: Query parameter for operation

  - `string page`

    Query param: Query parameter for page

  - `string sessionID`

    Query param: Query parameter for session_id

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

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

### Returns

- `class MemoryVersionListPageResponse:`

  - `IReadOnlyList<BetaManagedAgentsMemoryVersion> Data`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string MemoryID`

    - `required string MemoryStoreID`

    - `required BetaManagedAgentsMemoryVersionOperation Operation`

      MemoryVersionOperation enum

      - `"created"Created`

      - `"modified"Modified`

      - `"deleted"Deleted`

    - `required Type Type`

      - `"memory_version"MemoryVersion`

    - `string? Content`

    - `string? ContentSha256`

    - `Int? ContentSizeBytes`

    - `BetaManagedAgentsActor CreatedBy`

      - `class BetaManagedAgentsSessionActor:`

        - `required string SessionID`

        - `required Type Type`

          - `"session_actor"SessionActor`

      - `class BetaManagedAgentsApiActor:`

        - `required string ApiKeyID`

        - `required Type Type`

          - `"api_actor"ApiActor`

      - `class BetaManagedAgentsUserActor:`

        - `required Type Type`

          - `"user_actor"UserActor`

        - `required string UserID`

    - `string? Path`

    - `DateTimeOffset? RedactedAt`

      A timestamp in RFC 3339 format

    - `BetaManagedAgentsActor RedactedBy`

      - `class BetaManagedAgentsSessionActor:`

        - `required string SessionID`

        - `required Type Type`

          - `"session_actor"SessionActor`

      - `class BetaManagedAgentsApiActor:`

        - `required string ApiKeyID`

        - `required Type Type`

          - `"api_actor"ApiActor`

      - `class BetaManagedAgentsUserActor:`

        - `required Type Type`

          - `"user_actor"UserActor`

        - `required string UserID`

  - `string? NextPage`

### Example

```csharp
MemoryVersionListParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var page = await client.Beta.MemoryStores.MemoryVersions.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

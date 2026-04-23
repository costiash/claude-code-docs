## Create

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Create(MemoryStoreCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores`

CreateMemoryStore

### Parameters

- `MemoryStoreCreateParams parameters`

  - `required string name`

    Body param

  - `string description`

    Body param

  - `IReadOnlyDictionary<string, string> metadata`

    Body param

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

- `class BetaManagedAgentsMemoryStore:`

  - `required string ID`

  - `required Type Type`

    - `"memory_store"MemoryStore`

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `string Description`

  - `IReadOnlyDictionary<string, string> Metadata`

  - `string Name`

  - `DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

### Example

```csharp
MemoryStoreCreateParams parameters = new() { Name = "x" };

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Create(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

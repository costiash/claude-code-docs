# Memory Stores

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

## List

`MemoryStoreListPageResponse Beta.MemoryStores.List(MemoryStoreListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores`

ListMemoryStores

### Parameters

- `MemoryStoreListParams parameters`

  - `DateTimeOffset createdAtGte`

    Query param: Return stores created at or after this time (inclusive).

  - `DateTimeOffset createdAtLte`

    Query param: Return stores created at or before this time (inclusive).

  - `Boolean includeArchived`

    Query param: Query parameter for include_archived

  - `Int limit`

    Query param: Query parameter for limit

  - `string page`

    Query param: Query parameter for page

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

- `class MemoryStoreListPageResponse:`

  - `IReadOnlyList<BetaManagedAgentsMemoryStore> Data`

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

  - `string? NextPage`

### Example

```csharp
MemoryStoreListParams parameters = new();

var page = await client.Beta.MemoryStores.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

## Retrieve

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Retrieve(MemoryStoreRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}`

GetMemoryStore

### Parameters

- `MemoryStoreRetrieveParams parameters`

  - `required string memoryStoreID`

    Path parameter memory_store_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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
MemoryStoreRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

## Update

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Update(MemoryStoreUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}`

UpdateMemoryStore

### Parameters

- `MemoryStoreUpdateParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `string? description`

    Body param

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `string? name`

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
MemoryStoreUpdateParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Update(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

## Delete

`BetaManagedAgentsDeletedMemoryStore Beta.MemoryStores.Delete(MemoryStoreDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/memory_stores/{memory_store_id}`

DeleteMemoryStore

### Parameters

- `MemoryStoreDeleteParams parameters`

  - `required string memoryStoreID`

    Path parameter memory_store_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

- `class BetaManagedAgentsDeletedMemoryStore:`

  - `required string ID`

  - `required Type Type`

    - `"memory_store_deleted"MemoryStoreDeleted`

### Example

```csharp
MemoryStoreDeleteParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsDeletedMemoryStore = await client.Beta.MemoryStores.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedMemoryStore);
```

## Archive

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Archive(MemoryStoreArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}/archive`

ArchiveMemoryStore

### Parameters

- `MemoryStoreArchiveParams parameters`

  - `required string memoryStoreID`

    Path parameter memory_store_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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
MemoryStoreArchiveParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Archive(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

## Domain Types

### Beta Managed Agents Deleted Memory Store

- `class BetaManagedAgentsDeletedMemoryStore:`

  - `required string ID`

  - `required Type Type`

    - `"memory_store_deleted"MemoryStoreDeleted`

### Beta Managed Agents Memory Store

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

# Memories

## Create

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Create(MemoryCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}/memories`

CreateMemory

### Parameters

- `MemoryCreateParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string? content`

    Body param

  - `required string path`

    Body param

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

- `class BetaManagedAgentsMemory:`

  - `required string ID`

  - `required string ContentSha256`

  - `required Int ContentSizeBytes`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryStoreID`

  - `required string MemoryVersionID`

  - `required string Path`

  - `required Type Type`

    - `"memory"Memory`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? Content`

### Example

```csharp
MemoryCreateParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    Content = "content",
    Path = "xx",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Create(parameters);

Console.WriteLine(betaManagedAgentsMemory);
```

## List

`MemoryListPageResponse Beta.MemoryStores.Memories.List(MemoryListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}/memories`

ListMemories

### Parameters

- `MemoryListParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `Int depth`

    Query param: Query parameter for depth

  - `Int limit`

    Query param: Query parameter for limit

  - `Order order`

    Query param: Query parameter for order

    - `"asc"Asc`

    - `"desc"Desc`

  - `string orderBy`

    Query param: Query parameter for order_by

  - `string page`

    Query param: Query parameter for page

  - `string pathPrefix`

    Query param: Optional path prefix filter (raw string-prefix match; include a trailing slash for directory-scoped lists). This value appears in request URLs. Do not include secrets or personally identifiable information.

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

- `class MemoryListPageResponse:`

  - `IReadOnlyList<BetaManagedAgentsMemoryListItem> Data`

    - `class BetaManagedAgentsMemory:`

      - `required string ID`

      - `required string ContentSha256`

      - `required Int ContentSizeBytes`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

      - `required string MemoryStoreID`

      - `required string MemoryVersionID`

      - `required string Path`

      - `required Type Type`

        - `"memory"Memory`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

      - `string? Content`

    - `class BetaManagedAgentsMemoryPrefix:`

      - `required string Path`

      - `required Type Type`

        - `"memory_prefix"MemoryPrefix`

  - `string? NextPage`

### Example

```csharp
MemoryListParams parameters = new() { MemoryStoreID = "memory_store_id" };

var page = await client.Beta.MemoryStores.Memories.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

## Retrieve

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Retrieve(MemoryRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

GetMemory

### Parameters

- `MemoryRetrieveParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryID`

    Path param: Path parameter memory_id

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

- `class BetaManagedAgentsMemory:`

  - `required string ID`

  - `required string ContentSha256`

  - `required Int ContentSizeBytes`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryStoreID`

  - `required string MemoryVersionID`

  - `required string Path`

  - `required Type Type`

    - `"memory"Memory`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? Content`

### Example

```csharp
MemoryRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemory);
```

## Update

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Update(MemoryUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

UpdateMemory

### Parameters

- `MemoryUpdateParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryID`

    Path param: Path parameter memory_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `string? content`

    Body param

  - `string? path`

    Body param

  - `BetaManagedAgentsPrecondition precondition`

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

- `class BetaManagedAgentsMemory:`

  - `required string ID`

  - `required string ContentSha256`

  - `required Int ContentSizeBytes`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryStoreID`

  - `required string MemoryVersionID`

  - `required string Path`

  - `required Type Type`

    - `"memory"Memory`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? Content`

### Example

```csharp
MemoryUpdateParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Update(parameters);

Console.WriteLine(betaManagedAgentsMemory);
```

## Delete

`BetaManagedAgentsDeletedMemory Beta.MemoryStores.Memories.Delete(MemoryDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

DeleteMemory

### Parameters

- `MemoryDeleteParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryID`

    Path param: Path parameter memory_id

  - `string expectedContentSha256`

    Query param: Query parameter for expected_content_sha256

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

- `class BetaManagedAgentsDeletedMemory:`

  - `required string ID`

  - `required Type Type`

    - `"memory_deleted"MemoryDeleted`

### Example

```csharp
MemoryDeleteParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsDeletedMemory = await client.Beta.MemoryStores.Memories.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedMemory);
```

## Domain Types

### Beta Managed Agents Content Sha256 Precondition

- `class BetaManagedAgentsContentSha256Precondition:`

  - `required Type Type`

    - `"content_sha256"ContentSha256`

  - `string ContentSha256`

### Beta Managed Agents Deleted Memory

- `class BetaManagedAgentsDeletedMemory:`

  - `required string ID`

  - `required Type Type`

    - `"memory_deleted"MemoryDeleted`

### Beta Managed Agents Memory

- `class BetaManagedAgentsMemory:`

  - `required string ID`

  - `required string ContentSha256`

  - `required Int ContentSizeBytes`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string MemoryStoreID`

  - `required string MemoryVersionID`

  - `required string Path`

  - `required Type Type`

    - `"memory"Memory`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? Content`

### Beta Managed Agents Memory List Item

- `class BetaManagedAgentsMemoryListItem: A class that can be one of several variants.union`

  - `class BetaManagedAgentsMemory:`

    - `required string ID`

    - `required string ContentSha256`

    - `required Int ContentSizeBytes`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string MemoryStoreID`

    - `required string MemoryVersionID`

    - `required string Path`

    - `required Type Type`

      - `"memory"Memory`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `string? Content`

  - `class BetaManagedAgentsMemoryPrefix:`

    - `required string Path`

    - `required Type Type`

      - `"memory_prefix"MemoryPrefix`

### Beta Managed Agents Memory Path Conflict Error

- `class BetaManagedAgentsMemoryPathConflictError:`

  - `required Type Type`

    - `"memory_path_conflict_error"MemoryPathConflictError`

  - `string ConflictingMemoryID`

  - `string ConflictingPath`

  - `string Message`

### Beta Managed Agents Memory Precondition Failed Error

- `class BetaManagedAgentsMemoryPreconditionFailedError:`

  - `required Type Type`

    - `"memory_precondition_failed_error"MemoryPreconditionFailedError`

  - `string Message`

### Beta Managed Agents Memory Prefix

- `class BetaManagedAgentsMemoryPrefix:`

  - `required string Path`

  - `required Type Type`

    - `"memory_prefix"MemoryPrefix`

### Beta Managed Agents Memory View

- `enum BetaManagedAgentsMemoryView:`

  MemoryView enum

  - `"basic"Basic`

  - `"full"Full`

### Beta Managed Agents Precondition

- `class BetaManagedAgentsPrecondition:`

  - `required Type Type`

    - `"content_sha256"ContentSha256`

  - `string ContentSha256`

# Memory Versions

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

## Retrieve

`BetaManagedAgentsMemoryVersion Beta.MemoryStores.MemoryVersions.Retrieve(MemoryVersionRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

GetMemoryVersion

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

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

### Returns

- `class BetaManagedAgentsMemoryVersion:`

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

## Redact

`BetaManagedAgentsMemoryVersion Beta.MemoryStores.MemoryVersions.Redact(MemoryVersionRedactParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

RedactMemoryVersion

### Parameters

- `MemoryVersionRedactParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryVersionID`

    Path param: Path parameter memory_version_id

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

- `class BetaManagedAgentsMemoryVersion:`

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

### Example

```csharp
MemoryVersionRedactParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryVersionID = "memory_version_id",
};

var betaManagedAgentsMemoryVersion = await client.Beta.MemoryStores.MemoryVersions.Redact(parameters);

Console.WriteLine(betaManagedAgentsMemoryVersion);
```

## Domain Types

### Beta Managed Agents Actor

- `class BetaManagedAgentsActor: A class that can be one of several variants.union`

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

### Beta Managed Agents API Actor

- `class BetaManagedAgentsApiActor:`

  - `required string ApiKeyID`

  - `required Type Type`

    - `"api_actor"ApiActor`

### Beta Managed Agents Memory Version

- `class BetaManagedAgentsMemoryVersion:`

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

### Beta Managed Agents Memory Version Operation

- `enum BetaManagedAgentsMemoryVersionOperation:`

  MemoryVersionOperation enum

  - `"created"Created`

  - `"modified"Modified`

  - `"deleted"Deleted`

### Beta Managed Agents Session Actor

- `class BetaManagedAgentsSessionActor:`

  - `required string SessionID`

  - `required Type Type`

    - `"session_actor"SessionActor`

### Beta Managed Agents User Actor

- `class BetaManagedAgentsUserActor:`

  - `required Type Type`

    - `"user_actor"UserActor`

  - `required string UserID`

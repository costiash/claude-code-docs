## Retrieve

`ResourceRetrieveResponse Beta.Sessions.Resources.Retrieve(ResourceRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `ResourceRetrieveParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string resourceID`

    Path param: Path parameter resource_id

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

- `class ResourceRetrieveResponse: A class that can be one of several variants.union`

  The requested session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string MountPath`

    - `required Type Type`

      - `"github_repository"GitHubRepository`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `required string Url`

    - `Checkout? Checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `required string Name`

          Branch name to check out.

        - `required Type Type`

          - `"branch"Branch`

      - `class BetaManagedAgentsCommitCheckout:`

        - `required string Sha`

          Full commit SHA to check out.

        - `required Type Type`

          - `"commit"Commit`

  - `class BetaManagedAgentsFileResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required string FileID`

    - `required string MountPath`

    - `required Type Type`

      - `"file"File`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsMemoryStoreResource:`

    A memory store attached to an agent session.

    - `required string MemoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `required Type Type`

      - `"memory_store"MemoryStore`

    - `Access? Access`

      Access mode for an attached memory store.

      - `"read_write"ReadWrite`

      - `"read_only"ReadOnly`

    - `string Description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `string? Instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `string? MountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `string? Name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```csharp
ResourceRetrieveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ResourceID = "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
};

var resource = await client.Beta.Sessions.Resources.Retrieve(parameters);

Console.WriteLine(resource);
```

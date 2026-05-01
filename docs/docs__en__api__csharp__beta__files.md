# Files

## Upload

`FileMetadata Beta.Files.Upload(FileUploadParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/files`

Upload File

### Parameters

- `FileUploadParams parameters`

  - `required string file`

    Body param: The file to upload

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

- `class FileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

  - `required string Filename`

    Original filename of the uploaded file.

  - `required string MimeType`

    MIME type of the file.

  - `required Long SizeBytes`

    Size of the file in bytes.

  - `JsonElement Type "file"constant`

    Object type.

    For files, this is always `"file"`.

  - `Boolean Downloadable`

    Whether the file can be downloaded.

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type "session"constant`

      The type of scope (e.g., `"session"`).

### Example

```csharp
FileUploadParams parameters = new()
{
    File = Encoding.UTF8.GetBytes("Example data")
};

var fileMetadata = await client.Beta.Files.Upload(parameters);

Console.WriteLine(fileMetadata);
```

## List

`FileListPageResponse Beta.Files.List(FileListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/files`

List Files

### Parameters

- `FileListParams parameters`

  - `string afterID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Long limit`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `string scopeID`

    Query param: Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

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

- `class FileListPageResponse:`

  - `required IReadOnlyList<FileMetadata> Data`

    List of file metadata objects.

    - `required string ID`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `required DateTimeOffset CreatedAt`

      RFC 3339 datetime string representing when the file was created.

    - `required string Filename`

      Original filename of the uploaded file.

    - `required string MimeType`

      MIME type of the file.

    - `required Long SizeBytes`

      Size of the file in bytes.

    - `JsonElement Type "file"constant`

      Object type.

      For files, this is always `"file"`.

    - `Boolean Downloadable`

      Whether the file can be downloaded.

    - `BetaFileScope? Scope`

      The scope of this file, indicating the context in which it was created (e.g., a session).

      - `required string ID`

        The ID of the scoping resource (e.g., the session ID).

      - `JsonElement Type "session"constant`

        The type of scope (e.g., `"session"`).

  - `string? FirstID`

    ID of the first file in this page of results.

  - `Boolean HasMore`

    Whether there are more results available.

  - `string? LastID`

    ID of the last file in this page of results.

### Example

```csharp
FileListParams parameters = new();

var page = await client.Beta.Files.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

## Download

`HttpResponse Beta.Files.Download(FileDownloadParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `FileDownloadParams parameters`

  - `required string fileID`

    ID of the File.

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

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

### Example

```csharp
FileDownloadParams parameters = new() { FileID = "file_id" };

var response = await client.Beta.Files.Download(parameters);

Console.WriteLine(response);
```

## Retrieve Metadata

`FileMetadata Beta.Files.RetrieveMetadata(FileRetrieveMetadataParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `FileRetrieveMetadataParams parameters`

  - `required string fileID`

    ID of the File.

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

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

### Returns

- `class FileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

  - `required string Filename`

    Original filename of the uploaded file.

  - `required string MimeType`

    MIME type of the file.

  - `required Long SizeBytes`

    Size of the file in bytes.

  - `JsonElement Type "file"constant`

    Object type.

    For files, this is always `"file"`.

  - `Boolean Downloadable`

    Whether the file can be downloaded.

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type "session"constant`

      The type of scope (e.g., `"session"`).

### Example

```csharp
FileRetrieveMetadataParams parameters = new() { FileID = "file_id" };

var fileMetadata = await client.Beta.Files.RetrieveMetadata(parameters);

Console.WriteLine(fileMetadata);
```

## Delete

`DeletedFile Beta.Files.Delete(FileDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `FileDeleteParams parameters`

  - `required string fileID`

    ID of the File.

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

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

### Returns

- `class DeletedFile:`

  - `required string ID`

    ID of the deleted file.

  - `Type Type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"FileDeleted`

### Example

```csharp
FileDeleteParams parameters = new() { FileID = "file_id" };

var deletedFile = await client.Beta.Files.Delete(parameters);

Console.WriteLine(deletedFile);
```

## Domain Types

### Beta File Scope

- `class BetaFileScope:`

  - `required string ID`

    The ID of the scoping resource (e.g., the session ID).

  - `JsonElement Type "session"constant`

    The type of scope (e.g., `"session"`).

### Deleted File

- `class DeletedFile:`

  - `required string ID`

    ID of the deleted file.

  - `Type Type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"FileDeleted`

### File Metadata

- `class FileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

  - `required string Filename`

    Original filename of the uploaded file.

  - `required string MimeType`

    MIME type of the file.

  - `required Long SizeBytes`

    Size of the file in bytes.

  - `JsonElement Type "file"constant`

    Object type.

    For files, this is always `"file"`.

  - `Boolean Downloadable`

    Whether the file can be downloaded.

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type "session"constant`

      The type of scope (e.g., `"session"`).

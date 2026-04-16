# Versions

## Create

`VersionCreateResponse Beta.Skills.Versions.Create(VersionCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Parameters

- `VersionCreateParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `IReadOnlyList<string>? files`

    Body param: Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

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

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

### Returns

- `class VersionCreateResponse:`

  - `required string ID`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `required string CreatedAt`

    ISO 8601 timestamp of when the skill version was created.

  - `required string Description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string Directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `required string Name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string SkillID`

    Identifier for the skill that this version belongs to.

  - `required string Type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `required string Version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```csharp
VersionCreateParams parameters = new() { SkillID = "skill_id" };

var version = await client.Beta.Skills.Versions.Create(parameters);

Console.WriteLine(version);
```

## List

`VersionListPageResponse Beta.Skills.Versions.List(VersionListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Parameters

- `VersionListParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Long? limit`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `string? page`

    Query param: Optionally set to the `next_page` token from the previous response.

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

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

### Returns

- `class VersionListPageResponse:`

  - `required IReadOnlyList<VersionListResponse> Data`

    List of skill versions.

    - `required string ID`

      Unique identifier for the skill version.

      The format and length of IDs may change over time.

    - `required string CreatedAt`

      ISO 8601 timestamp of when the skill version was created.

    - `required string Description`

      Description of the skill version.

      This is extracted from the SKILL.md file in the skill upload.

    - `required string Directory`

      Directory name of the skill version.

      This is the top-level directory name that was extracted from the uploaded files.

    - `required string Name`

      Human-readable name of the skill version.

      This is extracted from the SKILL.md file in the skill upload.

    - `required string SkillID`

      Identifier for the skill that this version belongs to.

    - `required string Type`

      Object type.

      For Skill Versions, this is always `"skill_version"`.

    - `required string Version`

      Version identifier for the skill.

      Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `required Boolean HasMore`

    Indicates if there are more results in the requested page direction.

  - `required string? NextPage`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```csharp
VersionListParams parameters = new() { SkillID = "skill_id" };

var page = await client.Beta.Skills.Versions.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

## Retrieve

`VersionRetrieveResponse Beta.Skills.Versions.Retrieve(VersionRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Parameters

- `VersionRetrieveParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string version`

    Path param: Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

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

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

### Returns

- `class VersionRetrieveResponse:`

  - `required string ID`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `required string CreatedAt`

    ISO 8601 timestamp of when the skill version was created.

  - `required string Description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string Directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `required string Name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string SkillID`

    Identifier for the skill that this version belongs to.

  - `required string Type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `required string Version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```csharp
VersionRetrieveParams parameters = new()
{
    SkillID = "skill_id",
    Version = "version",
};

var version = await client.Beta.Skills.Versions.Retrieve(parameters);

Console.WriteLine(version);
```

## Delete

`VersionDeleteResponse Beta.Skills.Versions.Delete(VersionDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Parameters

- `VersionDeleteParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string version`

    Path param: Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

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

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

### Returns

- `class VersionDeleteResponse:`

  - `required string ID`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `required string Type`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```csharp
VersionDeleteParams parameters = new()
{
    SkillID = "skill_id",
    Version = "version",
};

var version = await client.Beta.Skills.Versions.Delete(parameters);

Console.WriteLine(version);
```

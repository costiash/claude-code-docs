## List

`SkillListPageResponse Beta.Skills.List(SkillListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/skills`

List Skills

### Parameters

- `SkillListParams parameters`

  - `Long limit`

    Query param: Number of results to return per page.

    Maximum value is 100. Defaults to 20.

  - `string? page`

    Query param: Pagination token for fetching a specific page of results.

    Pass the value from a previous response's `next_page` field to get the next page of results.

  - `string? source`

    Query param: Filter skills by source.

    If provided, only skills from the specified source will be returned:

    * `"custom"`: only return user-created skills
    * `"anthropic"`: only return Anthropic-created skills

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

### Returns

- `class SkillListPageResponse:`

  - `required IReadOnlyList<SkillListResponse> Data`

    List of skills.

    - `required string ID`

      Unique identifier for the skill.

      The format and length of IDs may change over time.

    - `required string CreatedAt`

      ISO 8601 timestamp of when the skill was created.

    - `required string? DisplayTitle`

      Display title for the skill.

      This is a human-readable label that is not included in the prompt sent to the model.

    - `required string? LatestVersion`

      The latest version identifier for the skill.

      This represents the most recent version of the skill that has been created.

    - `required string Source`

      Source of the skill.

      This may be one of the following values:

      * `"custom"`: the skill was created by a user
      * `"anthropic"`: the skill was created by Anthropic

    - `required string Type`

      Object type.

      For Skills, this is always `"skill"`.

    - `required string UpdatedAt`

      ISO 8601 timestamp of when the skill was last updated.

  - `required Boolean HasMore`

    Whether there are more results available.

    If `true`, there are additional results that can be fetched using the `next_page` token.

  - `required string? NextPage`

    Token for fetching the next page of results.

    If `null`, there are no more results available. Pass this value to the `page_token` parameter in the next request to get the next page.

### Example

```csharp
SkillListParams parameters = new();

var page = await client.Beta.Skills.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

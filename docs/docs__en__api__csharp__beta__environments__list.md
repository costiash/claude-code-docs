## List

`EnvironmentListPageResponse Beta.Environments.List(EnvironmentListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/environments`

List environments with pagination support.

### Parameters

- `EnvironmentListParams parameters`

  - `Boolean includeArchived`

    Query param: Include archived environments in the response

  - `Long limit`

    Query param: Maximum number of environments to return

  - `string? page`

    Query param: Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.

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

- `class EnvironmentListPageResponse:`

  Response when listing environments.

  This response model uses opaque cursor-based pagination. Use the `page`
  query parameter with the value from `next_page` to fetch the next page.

  - `required IReadOnlyList<BetaEnvironment> Data`

    List of environments.

    - `required string ID`

      Environment identifier (e.g., 'env_...')

    - `required string? ArchivedAt`

      RFC 3339 timestamp when environment was archived, or null if not archived

    - `required BetaCloudConfig Config`

      `cloud` environment configuration.

      - `required Networking Networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork:`

          Unrestricted network access.

          - `JsonElement Type "unrestricted"constant`

            Network policy type

        - `class BetaLimitedNetwork:`

          Limited network access.

          - `required Boolean AllowMcpServers`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `required Boolean AllowPackageManagers`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `required IReadOnlyList<string> AllowedHosts`

            Specifies domains the container can reach.

          - `JsonElement Type "limited"constant`

            Network policy type

      - `required BetaPackages Packages`

        Package manager configuration.

        - `required IReadOnlyList<string> Apt`

          Ubuntu/Debian packages to install

        - `required IReadOnlyList<string> Cargo`

          Rust packages to install

        - `required IReadOnlyList<string> Gem`

          Ruby packages to install

        - `required IReadOnlyList<string> Go`

          Go packages to install

        - `required IReadOnlyList<string> Npm`

          Node.js packages to install

        - `required IReadOnlyList<string> Pip`

          Python packages to install

        - `Type Type`

          Package configuration type

          - `"packages"Packages`

      - `JsonElement Type "cloud"constant`

        Environment type

    - `required string CreatedAt`

      RFC 3339 timestamp when environment was created

    - `required string Description`

      User-provided description for the environment

    - `required IReadOnlyDictionary<string, string> Metadata`

      User-provided metadata key-value pairs

    - `required string Name`

      Human-readable name for the environment

    - `JsonElement Type "environment"constant`

      The type of object (always 'environment')

    - `required string UpdatedAt`

      RFC 3339 timestamp when environment was last updated

  - `required string? NextPage`

    Token for fetching the next page of results. If `null`, there are no more results available. Pass this value to the `page` parameter in the next request.

### Example

```csharp
EnvironmentListParams parameters = new();

var page = await client.Beta.Environments.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

## Archive

`BetaEnvironment Beta.Environments.Archive(EnvironmentArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Parameters

- `EnvironmentArchiveParams parameters`

  - `required string environmentID`

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and self-hosted environments.

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

### Example

```csharp
EnvironmentArchiveParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaEnvironment = await client.Beta.Environments.Archive(parameters);

Console.WriteLine(betaEnvironment);
```

# Environments

## Create

`BetaEnvironment Beta.Environments.Create(EnvironmentCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `EnvironmentCreateParams parameters`

  - `required string name`

    Body param: Human-readable name for the environment

  - `BetaCloudConfigParams? config`

    Body param: Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

  - `string? description`

    Body param: Optional description of the environment

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: User-provided metadata key-value pairs

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
EnvironmentCreateParams parameters = new() { Name = "python-data-analysis" };

var betaEnvironment = await client.Beta.Environments.Create(parameters);

Console.WriteLine(betaEnvironment);
```

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

## Retrieve

`BetaEnvironment Beta.Environments.Retrieve(EnvironmentRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/environments/{environment_id}`

Retrieve a specific environment by ID.

### Parameters

- `EnvironmentRetrieveParams parameters`

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
EnvironmentRetrieveParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaEnvironment = await client.Beta.Environments.Retrieve(parameters);

Console.WriteLine(betaEnvironment);
```

## Update

`BetaEnvironment Beta.Environments.Update(EnvironmentUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `EnvironmentUpdateParams parameters`

  - `required string environmentID`

    Path param

  - `BetaCloudConfigParams? config`

    Body param: Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

  - `string? description`

    Body param: Updated description of the environment

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

  - `string? name`

    Body param: Updated name for the environment

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
EnvironmentUpdateParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaEnvironment = await client.Beta.Environments.Update(parameters);

Console.WriteLine(betaEnvironment);
```

## Delete

`BetaEnvironmentDeleteResponse Beta.Environments.Delete(EnvironmentDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Parameters

- `EnvironmentDeleteParams parameters`

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

### Returns

- `class BetaEnvironmentDeleteResponse:`

  Response after deleting an environment.

  - `required string ID`

    Environment identifier

  - `JsonElement Type "environment_deleted"constant`

    The type of response

### Example

```csharp
EnvironmentDeleteParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaEnvironmentDeleteResponse = await client.Beta.Environments.Delete(parameters);

Console.WriteLine(betaEnvironmentDeleteResponse);
```

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

## Domain Types

### Beta Cloud Config

- `class BetaCloudConfig:`

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

### Beta Cloud Config Params

- `class BetaCloudConfigParams:`

  Request params for `cloud` environment configuration.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `JsonElement Type "cloud"constant`

    Environment type

  - `Networking? Networking`

    Network configuration policy. Omit on update to preserve the existing value.

    - `class BetaUnrestrictedNetwork:`

      Unrestricted network access.

      - `JsonElement Type "unrestricted"constant`

        Network policy type

    - `class BetaLimitedNetworkParams:`

      Limited network request params.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `JsonElement Type "limited"constant`

        Network policy type

      - `Boolean? AllowMcpServers`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `Boolean? AllowPackageManagers`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `IReadOnlyList<string>? AllowedHosts`

        Specifies domains the container can reach.

  - `BetaPackagesParams? Packages`

    Specify packages (and optionally their versions) available in this environment.

    When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

    - `IReadOnlyList<string>? Apt`

      Ubuntu/Debian packages to install

    - `IReadOnlyList<string>? Cargo`

      Rust packages to install

    - `IReadOnlyList<string>? Gem`

      Ruby packages to install

    - `IReadOnlyList<string>? Go`

      Go packages to install

    - `IReadOnlyList<string>? Npm`

      Node.js packages to install

    - `IReadOnlyList<string>? Pip`

      Python packages to install

    - `Type Type`

      Package configuration type

      - `"packages"Packages`

### Beta Environment

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

### Beta Environment Delete Response

- `class BetaEnvironmentDeleteResponse:`

  Response after deleting an environment.

  - `required string ID`

    Environment identifier

  - `JsonElement Type "environment_deleted"constant`

    The type of response

### Beta Limited Network

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

### Beta Limited Network Params

- `class BetaLimitedNetworkParams:`

  Limited network request params.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `JsonElement Type "limited"constant`

    Network policy type

  - `Boolean? AllowMcpServers`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `Boolean? AllowPackageManagers`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `IReadOnlyList<string>? AllowedHosts`

    Specifies domains the container can reach.

### Beta Packages

- `class BetaPackages:`

  Packages (and their versions) available in this environment.

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

### Beta Packages Params

- `class BetaPackagesParams:`

  Specify packages (and optionally their versions) available in this environment.

  When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

  - `IReadOnlyList<string>? Apt`

    Ubuntu/Debian packages to install

  - `IReadOnlyList<string>? Cargo`

    Rust packages to install

  - `IReadOnlyList<string>? Gem`

    Ruby packages to install

  - `IReadOnlyList<string>? Go`

    Go packages to install

  - `IReadOnlyList<string>? Npm`

    Node.js packages to install

  - `IReadOnlyList<string>? Pip`

    Python packages to install

  - `Type Type`

    Package configuration type

    - `"packages"Packages`

### Beta Unrestricted Network

- `class BetaUnrestrictedNetwork:`

  Unrestricted network access.

  - `JsonElement Type "unrestricted"constant`

    Network policy type

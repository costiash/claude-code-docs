# Environments

## Create Environment

`BetaEnvironment Beta.Environments.Create(EnvironmentCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `EnvironmentCreateParams parameters`

  - `required string name`

    Body param: Human-readable name for the environment

  - `Config? config`

    Body param: Environment configuration

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

    - `class BetaSelfHostedConfigParams:`

      Request params for `self_hosted` environment configuration.

      - `JsonElement Type "self_hosted"constant`

        Environment type

  - `string? description`

    Body param: Optional description of the environment

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: User-provided metadata key-value pairs

  - `Scope? scope`

    Body param: The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. Only applicable for self-hosted environments. If not specified, defaults based on organization type.

    - `"organization"Organization`

    - `"account"Account`

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and self-hosted environments.

  - `required string ID`

    Environment identifier (e.g., 'env_...')

  - `required string? ArchivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `required Config Config`

    Environment configuration (either Anthropic Cloud or self-hosted)

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

    - `class BetaSelfHostedConfig:`

      Configuration for self-hosted environments.

      - `JsonElement Type "self_hosted"constant`

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

  - `Scope Scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"Organization`

    - `"account"Account`

### Example

```csharp
EnvironmentCreateParams parameters = new() { Name = "python-data-analysis" };

var betaEnvironment = await client.Beta.Environments.Create(parameters);

Console.WriteLine(betaEnvironment);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## List Environments

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

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

    - `required Config Config`

      Environment configuration (either Anthropic Cloud or self-hosted)

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

      - `class BetaSelfHostedConfig:`

        Configuration for self-hosted environments.

        - `JsonElement Type "self_hosted"constant`

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

    - `Scope Scope`

      The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

      - `"organization"Organization`

      - `"account"Account`

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

#### Response

```json
{
  "data": [
    {
      "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "archived_at": null,
      "config": {
        "networking": {
          "allow_mcp_servers": false,
          "allow_package_managers": true,
          "allowed_hosts": [
            "api.example.com"
          ],
          "type": "limited"
        },
        "packages": {
          "apt": [
            "string"
          ],
          "cargo": [
            "string"
          ],
          "gem": [
            "string"
          ],
          "go": [
            "string"
          ],
          "npm": [
            "string"
          ],
          "pip": [
            "pandas",
            "numpy"
          ],
          "type": "packages"
        },
        "type": "cloud"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Python environment with data-analysis packages.",
      "metadata": {},
      "name": "python-data-analysis",
      "type": "environment",
      "updated_at": "2026-03-15T10:00:00Z",
      "scope": "organization"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Environment

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and self-hosted environments.

  - `required string ID`

    Environment identifier (e.g., 'env_...')

  - `required string? ArchivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `required Config Config`

    Environment configuration (either Anthropic Cloud or self-hosted)

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

    - `class BetaSelfHostedConfig:`

      Configuration for self-hosted environments.

      - `JsonElement Type "self_hosted"constant`

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

  - `Scope Scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"Organization`

    - `"account"Account`

### Example

```csharp
EnvironmentRetrieveParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaEnvironment = await client.Beta.Environments.Retrieve(parameters);

Console.WriteLine(betaEnvironment);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Update Environment

`BetaEnvironment Beta.Environments.Update(EnvironmentUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `EnvironmentUpdateParams parameters`

  - `required string environmentID`

    Path param

  - `Config? config`

    Body param: Updated environment configuration

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

    - `class BetaSelfHostedConfigParams:`

      Request params for `self_hosted` environment configuration.

      - `JsonElement Type "self_hosted"constant`

        Environment type

  - `string? description`

    Body param: Updated description of the environment

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

  - `string? name`

    Body param: Updated name for the environment

  - `Scope? scope`

    Body param: The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only.

    - `"organization"Organization`

    - `"account"Account`

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and self-hosted environments.

  - `required string ID`

    Environment identifier (e.g., 'env_...')

  - `required string? ArchivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `required Config Config`

    Environment configuration (either Anthropic Cloud or self-hosted)

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

    - `class BetaSelfHostedConfig:`

      Configuration for self-hosted environments.

      - `JsonElement Type "self_hosted"constant`

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

  - `Scope Scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"Organization`

    - `"account"Account`

### Example

```csharp
EnvironmentUpdateParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaEnvironment = await client.Beta.Environments.Update(parameters);

Console.WriteLine(betaEnvironment);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Delete Environment

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

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

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```

## Archive Environment

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

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and self-hosted environments.

  - `required string ID`

    Environment identifier (e.g., 'env_...')

  - `required string? ArchivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `required Config Config`

    Environment configuration (either Anthropic Cloud or self-hosted)

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

    - `class BetaSelfHostedConfig:`

      Configuration for self-hosted environments.

      - `JsonElement Type "self_hosted"constant`

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

  - `Scope Scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"Organization`

    - `"account"Account`

### Example

```csharp
EnvironmentArchiveParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaEnvironment = await client.Beta.Environments.Archive(parameters);

Console.WriteLine(betaEnvironment);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
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

  - `required Config Config`

    Environment configuration (either Anthropic Cloud or self-hosted)

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

    - `class BetaSelfHostedConfig:`

      Configuration for self-hosted environments.

      - `JsonElement Type "self_hosted"constant`

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

  - `Scope Scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `"organization"Organization`

    - `"account"Account`

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

### Beta Self Hosted Config

- `class BetaSelfHostedConfig:`

  Configuration for self-hosted environments.

  - `JsonElement Type "self_hosted"constant`

    Environment type

### Beta Self Hosted Config Params

- `class BetaSelfHostedConfigParams:`

  Request params for `self_hosted` environment configuration.

  - `JsonElement Type "self_hosted"constant`

    Environment type

### Beta Unrestricted Network

- `class BetaUnrestrictedNetwork:`

  Unrestricted network access.

  - `JsonElement Type "unrestricted"constant`

    Network policy type

# Work

## Get Work Item

`BetaSelfHostedWork Beta.Environments.Work.Retrieve(WorkRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

### Parameters

- `WorkRetrieveParams parameters`

  - `required string environmentID`

    Path param

  - `required string workID`

    Path param

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `required string ID`

    Work identifier (e.g., 'work_...')

  - `required string? AcknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `required string CreatedAt`

    RFC 3339 timestamp when work was created

  - `required BetaSessionWorkData Data`

    The actual work to be performed

    - `required string ID`

      Session identifier (e.g., 'session_...')

    - `JsonElement Type "session"constant`

      Type of work data

  - `required string EnvironmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `required string? LatestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs associated with this work item

  - `required string? StartedAt`

    RFC 3339 timestamp when work execution started

  - `required State State`

    Current state of the work item

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required string? StopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `required string? StoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonElement Type "work"constant`

    The type of object (always 'work')

### Example

```csharp
WorkRetrieveParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
    WorkID = "work_id",
};

var betaSelfHostedWork = await client.Beta.Environments.Work.Retrieve(parameters);

Console.WriteLine(betaSelfHostedWork);
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Poll for Work

`BetaSelfHostedWork? Beta.Environments.Work.Poll(WorkPollParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

### Parameters

- `WorkPollParams parameters`

  - `required string environmentID`

    Path param

  - `Long? blockMs`

    Query param: How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

  - `Long? reclaimOlderThanMs`

    Query param: Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

  - `string anthropicWorkerID`

    Header param: Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `required string ID`

    Work identifier (e.g., 'work_...')

  - `required string? AcknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `required string CreatedAt`

    RFC 3339 timestamp when work was created

  - `required BetaSessionWorkData Data`

    The actual work to be performed

    - `required string ID`

      Session identifier (e.g., 'session_...')

    - `JsonElement Type "session"constant`

      Type of work data

  - `required string EnvironmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `required string? LatestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs associated with this work item

  - `required string? StartedAt`

    RFC 3339 timestamp when work execution started

  - `required State State`

    Current state of the work item

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required string? StopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `required string? StoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonElement Type "work"constant`

    The type of object (always 'work')

### Example

```csharp
WorkPollParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaSelfHostedWork = await client.Beta.Environments.Work.Poll(parameters);

Console.WriteLine(betaSelfHostedWork);
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Acknowledge Work

`BetaSelfHostedWork Beta.Environments.Work.Ack(WorkAckParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/environments/{environment_id}/work/{work_id}/ack`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Acknowledge receipt of a work item, transitioning it from 'queued' to 'starting' and removing it from the queue.

### Parameters

- `WorkAckParams parameters`

  - `required string environmentID`

    Path param

  - `required string workID`

    Path param

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `required string ID`

    Work identifier (e.g., 'work_...')

  - `required string? AcknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `required string CreatedAt`

    RFC 3339 timestamp when work was created

  - `required BetaSessionWorkData Data`

    The actual work to be performed

    - `required string ID`

      Session identifier (e.g., 'session_...')

    - `JsonElement Type "session"constant`

      Type of work data

  - `required string EnvironmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `required string? LatestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs associated with this work item

  - `required string? StartedAt`

    RFC 3339 timestamp when work execution started

  - `required State State`

    Current state of the work item

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required string? StopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `required string? StoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonElement Type "work"constant`

    The type of object (always 'work')

### Example

```csharp
WorkAckParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
    WorkID = "work_id",
};

var betaSelfHostedWork = await client.Beta.Environments.Work.Ack(parameters);

Console.WriteLine(betaSelfHostedWork);
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Record Heartbeat

`BetaSelfHostedWorkHeartbeatResponse Beta.Environments.Work.Heartbeat(WorkHeartbeatParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/environments/{environment_id}/work/{work_id}/heartbeat`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

### Parameters

- `WorkHeartbeatParams parameters`

  - `required string environmentID`

    Path param

  - `required string workID`

    Path param

  - `Long? desiredTtlSeconds`

    Query param: Desired TTL in seconds

  - `string? expectedLastHeartbeat`

    Query param: Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

### Returns

- `class BetaSelfHostedWorkHeartbeatResponse:`

  Response after recording a heartbeat for a work item.

  - `required string LastHeartbeat`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `required Boolean LeaseExtended`

    Whether the heartbeat succeeded in extending the lease

  - `required State State`

    Current state of the work item (active/stopping/stopped)

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required Long TtlSeconds`

    Effective TTL applied to the lease

  - `JsonElement Type "work_heartbeat"constant`

    The type of response

### Example

```csharp
WorkHeartbeatParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
    WorkID = "work_id",
};

var betaSelfHostedWorkHeartbeatResponse = await client.Beta.Environments.Work.Heartbeat(parameters);

Console.WriteLine(betaSelfHostedWorkHeartbeatResponse);
```

#### Response

```json
{
  "last_heartbeat": "last_heartbeat",
  "lease_extended": true,
  "state": "queued",
  "ttl_seconds": 0,
  "type": "work_heartbeat"
}
```

## Stop Work

`BetaSelfHostedWork Beta.Environments.Work.Stop(WorkStopParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

### Parameters

- `WorkStopParams parameters`

  - `required string environmentID`

    Path param

  - `required string workID`

    Path param

  - `Boolean force`

    Body param: If true, immediately stop work without graceful shutdown

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `required string ID`

    Work identifier (e.g., 'work_...')

  - `required string? AcknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `required string CreatedAt`

    RFC 3339 timestamp when work was created

  - `required BetaSessionWorkData Data`

    The actual work to be performed

    - `required string ID`

      Session identifier (e.g., 'session_...')

    - `JsonElement Type "session"constant`

      Type of work data

  - `required string EnvironmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `required string? LatestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs associated with this work item

  - `required string? StartedAt`

    RFC 3339 timestamp when work execution started

  - `required State State`

    Current state of the work item

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required string? StopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `required string? StoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonElement Type "work"constant`

    The type of object (always 'work')

### Example

```csharp
WorkStopParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
    WorkID = "work_id",
};

var betaSelfHostedWork = await client.Beta.Environments.Work.Stop(parameters);

Console.WriteLine(betaSelfHostedWork);
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## List Work Items

`BetaSelfHostedWorkListResponse Beta.Environments.Work.List(WorkListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

### Parameters

- `WorkListParams parameters`

  - `required string environmentID`

    Path param

  - `Long limit`

    Query param: Maximum number of work items to return

  - `string? page`

    Query param: Opaque cursor from previous response for pagination

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

### Returns

- `class BetaSelfHostedWorkListResponse:`

  Response when listing work items with cursor-based pagination.

  - `required IReadOnlyList<BetaSelfHostedWork> Data`

    List of work items

    - `required string ID`

      Work identifier (e.g., 'work_...')

    - `required string? AcknowledgedAt`

      RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

    - `required string CreatedAt`

      RFC 3339 timestamp when work was created

    - `required BetaSessionWorkData Data`

      The actual work to be performed

      - `required string ID`

        Session identifier (e.g., 'session_...')

      - `JsonElement Type "session"constant`

        Type of work data

    - `required string EnvironmentID`

      Environment identifier this work belongs to (e.g., `env_...`)

    - `required string? LatestHeartbeatAt`

      RFC 3339 timestamp of the most recent heartbeat

    - `required IReadOnlyDictionary<string, string> Metadata`

      User-provided metadata key-value pairs associated with this work item

    - `required string? StartedAt`

      RFC 3339 timestamp when work execution started

    - `required State State`

      Current state of the work item

      - `"queued"Queued`

      - `"starting"Starting`

      - `"active"Active`

      - `"stopping"Stopping`

      - `"stopped"Stopped`

    - `required string? StopRequestedAt`

      RFC 3339 timestamp when stop was requested

    - `required string? StoppedAt`

      RFC 3339 timestamp when work execution stopped

    - `JsonElement Type "work"constant`

      The type of object (always 'work')

  - `required string? NextPage`

    Opaque cursor for fetching the next page of results

### Example

```csharp
WorkListParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var page = await client.Beta.Environments.Work.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "acknowledged_at": "acknowledged_at",
      "created_at": "created_at",
      "data": {
        "id": "id",
        "type": "session"
      },
      "environment_id": "environment_id",
      "latest_heartbeat_at": "latest_heartbeat_at",
      "metadata": {
        "foo": "string"
      },
      "started_at": "started_at",
      "state": "queued",
      "stop_requested_at": "stop_requested_at",
      "stopped_at": "stopped_at",
      "type": "work"
    }
  ],
  "next_page": "next_page"
}
```

## Update Work Item

`BetaSelfHostedWork Beta.Environments.Work.Update(WorkUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

### Parameters

- `WorkUpdateParams parameters`

  - `required string environmentID`

    Path param

  - `required string workID`

    Path param

  - `required IReadOnlyDictionary<string, string> metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

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

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `required string ID`

    Work identifier (e.g., 'work_...')

  - `required string? AcknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `required string CreatedAt`

    RFC 3339 timestamp when work was created

  - `required BetaSessionWorkData Data`

    The actual work to be performed

    - `required string ID`

      Session identifier (e.g., 'session_...')

    - `JsonElement Type "session"constant`

      Type of work data

  - `required string EnvironmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `required string? LatestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs associated with this work item

  - `required string? StartedAt`

    RFC 3339 timestamp when work execution started

  - `required State State`

    Current state of the work item

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required string? StopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `required string? StoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonElement Type "work"constant`

    The type of object (always 'work')

### Example

```csharp
WorkUpdateParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
    WorkID = "work_id",
    Metadata = new Dictionary<string, string?>() { { "foo", "string" } },
};

var betaSelfHostedWork = await client.Beta.Environments.Work.Update(parameters);

Console.WriteLine(betaSelfHostedWork);
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Get Queue Statistics

`BetaSelfHostedWorkQueueStats Beta.Environments.Work.Stats(WorkStatsParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

### Parameters

- `WorkStatsParams parameters`

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

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

### Returns

- `class BetaSelfHostedWorkQueueStats:`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `required Long Depth`

    Number of work items waiting to be picked up (lag from consumer group)

  - `required string? OldestQueuedAt`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `required Long Pending`

    Number of work items being processed (polled but not acknowledged)

  - `JsonElement Type "work_queue_stats"constant`

    The type of object

  - `required Long? WorkersPolling`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Example

```csharp
WorkStatsParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaSelfHostedWorkQueueStats = await client.Beta.Environments.Work.Stats(parameters);

Console.WriteLine(betaSelfHostedWorkQueueStats);
```

#### Response

```json
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```

## Domain Types

### Beta Self Hosted Work

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `required string ID`

    Work identifier (e.g., 'work_...')

  - `required string? AcknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `required string CreatedAt`

    RFC 3339 timestamp when work was created

  - `required BetaSessionWorkData Data`

    The actual work to be performed

    - `required string ID`

      Session identifier (e.g., 'session_...')

    - `JsonElement Type "session"constant`

      Type of work data

  - `required string EnvironmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `required string? LatestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs associated with this work item

  - `required string? StartedAt`

    RFC 3339 timestamp when work execution started

  - `required State State`

    Current state of the work item

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required string? StopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `required string? StoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonElement Type "work"constant`

    The type of object (always 'work')

### Beta Self Hosted Work Heartbeat Response

- `class BetaSelfHostedWorkHeartbeatResponse:`

  Response after recording a heartbeat for a work item.

  - `required string LastHeartbeat`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `required Boolean LeaseExtended`

    Whether the heartbeat succeeded in extending the lease

  - `required State State`

    Current state of the work item (active/stopping/stopped)

    - `"queued"Queued`

    - `"starting"Starting`

    - `"active"Active`

    - `"stopping"Stopping`

    - `"stopped"Stopped`

  - `required Long TtlSeconds`

    Effective TTL applied to the lease

  - `JsonElement Type "work_heartbeat"constant`

    The type of response

### Beta Self Hosted Work List Response

- `class BetaSelfHostedWorkListResponse:`

  Response when listing work items with cursor-based pagination.

  - `required IReadOnlyList<BetaSelfHostedWork> Data`

    List of work items

    - `required string ID`

      Work identifier (e.g., 'work_...')

    - `required string? AcknowledgedAt`

      RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

    - `required string CreatedAt`

      RFC 3339 timestamp when work was created

    - `required BetaSessionWorkData Data`

      The actual work to be performed

      - `required string ID`

        Session identifier (e.g., 'session_...')

      - `JsonElement Type "session"constant`

        Type of work data

    - `required string EnvironmentID`

      Environment identifier this work belongs to (e.g., `env_...`)

    - `required string? LatestHeartbeatAt`

      RFC 3339 timestamp of the most recent heartbeat

    - `required IReadOnlyDictionary<string, string> Metadata`

      User-provided metadata key-value pairs associated with this work item

    - `required string? StartedAt`

      RFC 3339 timestamp when work execution started

    - `required State State`

      Current state of the work item

      - `"queued"Queued`

      - `"starting"Starting`

      - `"active"Active`

      - `"stopping"Stopping`

      - `"stopped"Stopped`

    - `required string? StopRequestedAt`

      RFC 3339 timestamp when stop was requested

    - `required string? StoppedAt`

      RFC 3339 timestamp when work execution stopped

    - `JsonElement Type "work"constant`

      The type of object (always 'work')

  - `required string? NextPage`

    Opaque cursor for fetching the next page of results

### Beta Self Hosted Work Queue Stats

- `class BetaSelfHostedWorkQueueStats:`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `required Long Depth`

    Number of work items waiting to be picked up (lag from consumer group)

  - `required string? OldestQueuedAt`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `required Long Pending`

    Number of work items being processed (polled but not acknowledged)

  - `JsonElement Type "work_queue_stats"constant`

    The type of object

  - `required Long? WorkersPolling`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Beta Self Hosted Work Stop Request

- `class BetaSelfHostedWorkStopRequest:`

  Request to stop a work item.

  - `Boolean Force`

    If true, immediately stop work without graceful shutdown

### Beta Self Hosted Work Update Request

- `class BetaSelfHostedWorkUpdateRequest:`

  Request to update work item metadata.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

### Beta Session Work Data

- `class BetaSessionWorkData:`

  Work data for session work items.

  This resource type is used when work represents a session that needs to be executed
  in a self-hosted environment.

  - `required string ID`

    Session identifier (e.g., 'session_...')

  - `JsonElement Type "session"constant`

    Type of work data

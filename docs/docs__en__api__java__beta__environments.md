# Environments

## Create Environment

`BetaEnvironment beta().environments().create(EnvironmentCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `EnvironmentCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

  - `String name`

    Human-readable name for the environment

  - `Optional<Config> config`

    Environment configuration

    - `class BetaCloudConfigParams:`

      Request params for `cloud` environment configuration.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `JsonValue; type "cloud"constant`

        Environment type

        - `CLOUD("cloud")`

      - `Optional<Networking> networking`

        Network configuration policy. Omit on update to preserve the existing value.

        - `class BetaUnrestrictedNetwork:`

          Unrestricted network access.

          - `JsonValue; type "unrestricted"constant`

            Network policy type

            - `UNRESTRICTED("unrestricted")`

        - `class BetaLimitedNetworkParams:`

          Limited network request params.

          Fields default to null; on update, omitted fields preserve the
          existing value.

          - `JsonValue; type "limited"constant`

            Network policy type

            - `LIMITED("limited")`

          - `Optional<Boolean> allowMcpServers`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

          - `Optional<Boolean> allowPackageManagers`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

          - `Optional<List<String>> allowedHosts`

            Specifies domains the container can reach.

      - `Optional<BetaPackagesParams> packages`

        Specify packages (and optionally their versions) available in this environment.

        When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

        - `Optional<List<String>> apt`

          Ubuntu/Debian packages to install

        - `Optional<List<String>> cargo`

          Rust packages to install

        - `Optional<List<String>> gem`

          Ruby packages to install

        - `Optional<List<String>> go`

          Go packages to install

        - `Optional<List<String>> npm`

          Node.js packages to install

        - `Optional<List<String>> pip`

          Python packages to install

        - `Optional<Type> type`

          Package configuration type

          - `PACKAGES("packages")`

    - `class BetaSelfHostedConfigParams:`

      Request params for `self_hosted` environment configuration.

      - `JsonValue; type "self_hosted"constant`

        Environment type

        - `SELF_HOSTED("self_hosted")`

  - `Optional<String> description`

    Optional description of the environment

  - `Optional<Metadata> metadata`

    User-provided metadata key-value pairs

  - `Optional<Scope> scope`

    The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. Only applicable for self-hosted environments. If not specified, defaults based on organization type.

    - `ORGANIZATION("organization")`

    - `ACCOUNT("account")`

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and self-hosted environments.

  - `String id`

    Environment identifier (e.g., 'env_...')

  - `Optional<String> archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig:`

      `cloud` environment configuration.

      - `Networking networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork:`

          Unrestricted network access.

          - `JsonValue; type "unrestricted"constant`

            Network policy type

            - `UNRESTRICTED("unrestricted")`

        - `class BetaLimitedNetwork:`

          Limited network access.

          - `boolean allowMcpServers`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `boolean allowPackageManagers`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `List<String> allowedHosts`

            Specifies domains the container can reach.

          - `JsonValue; type "limited"constant`

            Network policy type

            - `LIMITED("limited")`

      - `BetaPackages packages`

        Package manager configuration.

        - `List<String> apt`

          Ubuntu/Debian packages to install

        - `List<String> cargo`

          Rust packages to install

        - `List<String> gem`

          Ruby packages to install

        - `List<String> go`

          Go packages to install

        - `List<String> npm`

          Node.js packages to install

        - `List<String> pip`

          Python packages to install

        - `Optional<Type> type`

          Package configuration type

          - `PACKAGES("packages")`

      - `JsonValue; type "cloud"constant`

        Environment type

        - `CLOUD("cloud")`

    - `class BetaSelfHostedConfig:`

      Configuration for self-hosted environments.

      - `JsonValue; type "self_hosted"constant`

        Environment type

        - `SELF_HOSTED("self_hosted")`

  - `String createdAt`

    RFC 3339 timestamp when environment was created

  - `String description`

    User-provided description for the environment

  - `Metadata metadata`

    User-provided metadata key-value pairs

  - `String name`

    Human-readable name for the environment

  - `JsonValue; type "environment"constant`

    The type of object (always 'environment')

    - `ENVIRONMENT("environment")`

  - `String updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `Optional<Scope> scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `ORGANIZATION("organization")`

    - `ACCOUNT("account")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.BetaEnvironment;
import com.anthropic.models.beta.environments.EnvironmentCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EnvironmentCreateParams params = EnvironmentCreateParams.builder()
            .name("python-data-analysis")
            .build();
        BetaEnvironment betaEnvironment = client.beta().environments().create(params);
    }
}
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

`EnvironmentListPage beta().environments().list(EnvironmentListParamsparams = EnvironmentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/environments`

List environments with pagination support.

### Parameters

- `EnvironmentListParams params`

  - `Optional<Boolean> includeArchived`

    Include archived environments in the response

  - `Optional<Long> limit`

    Maximum number of environments to return

  - `Optional<String> page`

    Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and self-hosted environments.

  - `String id`

    Environment identifier (e.g., 'env_...')

  - `Optional<String> archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig:`

      `cloud` environment configuration.

      - `Networking networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork:`

          Unrestricted network access.

          - `JsonValue; type "unrestricted"constant`

            Network policy type

            - `UNRESTRICTED("unrestricted")`

        - `class BetaLimitedNetwork:`

          Limited network access.

          - `boolean allowMcpServers`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `boolean allowPackageManagers`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `List<String> allowedHosts`

            Specifies domains the container can reach.

          - `JsonValue; type "limited"constant`

            Network policy type

            - `LIMITED("limited")`

      - `BetaPackages packages`

        Package manager configuration.

        - `List<String> apt`

          Ubuntu/Debian packages to install

        - `List<String> cargo`

          Rust packages to install

        - `List<String> gem`

          Ruby packages to install

        - `List<String> go`

          Go packages to install

        - `List<String> npm`

          Node.js packages to install

        - `List<String> pip`

          Python packages to install

        - `Optional<Type> type`

          Package configuration type

          - `PACKAGES("packages")`

      - `JsonValue; type "cloud"constant`

        Environment type

        - `CLOUD("cloud")`

    - `class BetaSelfHostedConfig:`

      Configuration for self-hosted environments.

      - `JsonValue; type "self_hosted"constant`

        Environment type

        - `SELF_HOSTED("self_hosted")`

  - `String createdAt`

    RFC 3339 timestamp when environment was created

  - `String description`

    User-provided description for the environment

  - `Metadata metadata`

    User-provided metadata key-value pairs

  - `String name`

    Human-readable name for the environment

  - `JsonValue; type "environment"constant`

    The type of object (always 'environment')

    - `ENVIRONMENT("environment")`

  - `String updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `Optional<Scope> scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `ORGANIZATION("organization")`

    - `ACCOUNT("account")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.EnvironmentListPage;
import com.anthropic.models.beta.environments.EnvironmentListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EnvironmentListPage page = client.beta().environments().list();
    }
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

`BetaEnvironment beta().environments().retrieve(EnvironmentRetrieveParamsparams = EnvironmentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/environments/{environment_id}`

Retrieve a specific environment by ID.

### Parameters

- `EnvironmentRetrieveParams params`

  - `Optional<String> environmentId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and self-hosted environments.

  - `String id`

    Environment identifier (e.g., 'env_...')

  - `Optional<String> archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig:`

      `cloud` environment configuration.

      - `Networking networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork:`

          Unrestricted network access.

          - `JsonValue; type "unrestricted"constant`

            Network policy type

            - `UNRESTRICTED("unrestricted")`

        - `class BetaLimitedNetwork:`

          Limited network access.

          - `boolean allowMcpServers`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `boolean allowPackageManagers`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `List<String> allowedHosts`

            Specifies domains the container can reach.

          - `JsonValue; type "limited"constant`

            Network policy type

            - `LIMITED("limited")`

      - `BetaPackages packages`

        Package manager configuration.

        - `List<String> apt`

          Ubuntu/Debian packages to install

        - `List<String> cargo`

          Rust packages to install

        - `List<String> gem`

          Ruby packages to install

        - `List<String> go`

          Go packages to install

        - `List<String> npm`

          Node.js packages to install

        - `List<String> pip`

          Python packages to install

        - `Optional<Type> type`

          Package configuration type

          - `PACKAGES("packages")`

      - `JsonValue; type "cloud"constant`

        Environment type

        - `CLOUD("cloud")`

    - `class BetaSelfHostedConfig:`

      Configuration for self-hosted environments.

      - `JsonValue; type "self_hosted"constant`

        Environment type

        - `SELF_HOSTED("self_hosted")`

  - `String createdAt`

    RFC 3339 timestamp when environment was created

  - `String description`

    User-provided description for the environment

  - `Metadata metadata`

    User-provided metadata key-value pairs

  - `String name`

    Human-readable name for the environment

  - `JsonValue; type "environment"constant`

    The type of object (always 'environment')

    - `ENVIRONMENT("environment")`

  - `String updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `Optional<Scope> scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `ORGANIZATION("organization")`

    - `ACCOUNT("account")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.BetaEnvironment;
import com.anthropic.models.beta.environments.EnvironmentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaEnvironment betaEnvironment = client.beta().environments().retrieve("env_011CZkZ9X2dpNyB7HsEFoRfW");
    }
}
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

`BetaEnvironment beta().environments().update(EnvironmentUpdateParamsparams = EnvironmentUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `EnvironmentUpdateParams params`

  - `Optional<String> environmentId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

  - `Optional<Config> config`

    Updated environment configuration

    - `class BetaCloudConfigParams:`

      Request params for `cloud` environment configuration.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `JsonValue; type "cloud"constant`

        Environment type

        - `CLOUD("cloud")`

      - `Optional<Networking> networking`

        Network configuration policy. Omit on update to preserve the existing value.

        - `class BetaUnrestrictedNetwork:`

          Unrestricted network access.

          - `JsonValue; type "unrestricted"constant`

            Network policy type

            - `UNRESTRICTED("unrestricted")`

        - `class BetaLimitedNetworkParams:`

          Limited network request params.

          Fields default to null; on update, omitted fields preserve the
          existing value.

          - `JsonValue; type "limited"constant`

            Network policy type

            - `LIMITED("limited")`

          - `Optional<Boolean> allowMcpServers`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

          - `Optional<Boolean> allowPackageManagers`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

          - `Optional<List<String>> allowedHosts`

            Specifies domains the container can reach.

      - `Optional<BetaPackagesParams> packages`

        Specify packages (and optionally their versions) available in this environment.

        When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

        - `Optional<List<String>> apt`

          Ubuntu/Debian packages to install

        - `Optional<List<String>> cargo`

          Rust packages to install

        - `Optional<List<String>> gem`

          Ruby packages to install

        - `Optional<List<String>> go`

          Go packages to install

        - `Optional<List<String>> npm`

          Node.js packages to install

        - `Optional<List<String>> pip`

          Python packages to install

        - `Optional<Type> type`

          Package configuration type

          - `PACKAGES("packages")`

    - `class BetaSelfHostedConfigParams:`

      Request params for `self_hosted` environment configuration.

      - `JsonValue; type "self_hosted"constant`

        Environment type

        - `SELF_HOSTED("self_hosted")`

  - `Optional<String> description`

    Updated description of the environment

  - `Optional<Metadata> metadata`

    User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

  - `Optional<String> name`

    Updated name for the environment

  - `Optional<Scope> scope`

    The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only.

    - `ORGANIZATION("organization")`

    - `ACCOUNT("account")`

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and self-hosted environments.

  - `String id`

    Environment identifier (e.g., 'env_...')

  - `Optional<String> archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig:`

      `cloud` environment configuration.

      - `Networking networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork:`

          Unrestricted network access.

          - `JsonValue; type "unrestricted"constant`

            Network policy type

            - `UNRESTRICTED("unrestricted")`

        - `class BetaLimitedNetwork:`

          Limited network access.

          - `boolean allowMcpServers`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `boolean allowPackageManagers`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `List<String> allowedHosts`

            Specifies domains the container can reach.

          - `JsonValue; type "limited"constant`

            Network policy type

            - `LIMITED("limited")`

      - `BetaPackages packages`

        Package manager configuration.

        - `List<String> apt`

          Ubuntu/Debian packages to install

        - `List<String> cargo`

          Rust packages to install

        - `List<String> gem`

          Ruby packages to install

        - `List<String> go`

          Go packages to install

        - `List<String> npm`

          Node.js packages to install

        - `List<String> pip`

          Python packages to install

        - `Optional<Type> type`

          Package configuration type

          - `PACKAGES("packages")`

      - `JsonValue; type "cloud"constant`

        Environment type

        - `CLOUD("cloud")`

    - `class BetaSelfHostedConfig:`

      Configuration for self-hosted environments.

      - `JsonValue; type "self_hosted"constant`

        Environment type

        - `SELF_HOSTED("self_hosted")`

  - `String createdAt`

    RFC 3339 timestamp when environment was created

  - `String description`

    User-provided description for the environment

  - `Metadata metadata`

    User-provided metadata key-value pairs

  - `String name`

    Human-readable name for the environment

  - `JsonValue; type "environment"constant`

    The type of object (always 'environment')

    - `ENVIRONMENT("environment")`

  - `String updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `Optional<Scope> scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `ORGANIZATION("organization")`

    - `ACCOUNT("account")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.BetaEnvironment;
import com.anthropic.models.beta.environments.EnvironmentUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaEnvironment betaEnvironment = client.beta().environments().update("env_011CZkZ9X2dpNyB7HsEFoRfW");
    }
}
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

`BetaEnvironmentDeleteResponse beta().environments().delete(EnvironmentDeleteParamsparams = EnvironmentDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Parameters

- `EnvironmentDeleteParams params`

  - `Optional<String> environmentId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

### Returns

- `class BetaEnvironmentDeleteResponse:`

  Response after deleting an environment.

  - `String id`

    Environment identifier

  - `JsonValue; type "environment_deleted"constant`

    The type of response

    - `ENVIRONMENT_DELETED("environment_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.BetaEnvironmentDeleteResponse;
import com.anthropic.models.beta.environments.EnvironmentDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaEnvironmentDeleteResponse betaEnvironmentDeleteResponse = client.beta().environments().delete("env_011CZkZ9X2dpNyB7HsEFoRfW");
    }
}
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```

## Archive Environment

`BetaEnvironment beta().environments().archive(EnvironmentArchiveParamsparams = EnvironmentArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Parameters

- `EnvironmentArchiveParams params`

  - `Optional<String> environmentId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and self-hosted environments.

  - `String id`

    Environment identifier (e.g., 'env_...')

  - `Optional<String> archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig:`

      `cloud` environment configuration.

      - `Networking networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork:`

          Unrestricted network access.

          - `JsonValue; type "unrestricted"constant`

            Network policy type

            - `UNRESTRICTED("unrestricted")`

        - `class BetaLimitedNetwork:`

          Limited network access.

          - `boolean allowMcpServers`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `boolean allowPackageManagers`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `List<String> allowedHosts`

            Specifies domains the container can reach.

          - `JsonValue; type "limited"constant`

            Network policy type

            - `LIMITED("limited")`

      - `BetaPackages packages`

        Package manager configuration.

        - `List<String> apt`

          Ubuntu/Debian packages to install

        - `List<String> cargo`

          Rust packages to install

        - `List<String> gem`

          Ruby packages to install

        - `List<String> go`

          Go packages to install

        - `List<String> npm`

          Node.js packages to install

        - `List<String> pip`

          Python packages to install

        - `Optional<Type> type`

          Package configuration type

          - `PACKAGES("packages")`

      - `JsonValue; type "cloud"constant`

        Environment type

        - `CLOUD("cloud")`

    - `class BetaSelfHostedConfig:`

      Configuration for self-hosted environments.

      - `JsonValue; type "self_hosted"constant`

        Environment type

        - `SELF_HOSTED("self_hosted")`

  - `String createdAt`

    RFC 3339 timestamp when environment was created

  - `String description`

    User-provided description for the environment

  - `Metadata metadata`

    User-provided metadata key-value pairs

  - `String name`

    Human-readable name for the environment

  - `JsonValue; type "environment"constant`

    The type of object (always 'environment')

    - `ENVIRONMENT("environment")`

  - `String updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `Optional<Scope> scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `ORGANIZATION("organization")`

    - `ACCOUNT("account")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.BetaEnvironment;
import com.anthropic.models.beta.environments.EnvironmentArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaEnvironment betaEnvironment = client.beta().environments().archive("env_011CZkZ9X2dpNyB7HsEFoRfW");
    }
}
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

  - `Networking networking`

    Network configuration policy.

    - `class BetaUnrestrictedNetwork:`

      Unrestricted network access.

      - `JsonValue; type "unrestricted"constant`

        Network policy type

        - `UNRESTRICTED("unrestricted")`

    - `class BetaLimitedNetwork:`

      Limited network access.

      - `boolean allowMcpServers`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

      - `boolean allowPackageManagers`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

      - `List<String> allowedHosts`

        Specifies domains the container can reach.

      - `JsonValue; type "limited"constant`

        Network policy type

        - `LIMITED("limited")`

  - `BetaPackages packages`

    Package manager configuration.

    - `List<String> apt`

      Ubuntu/Debian packages to install

    - `List<String> cargo`

      Rust packages to install

    - `List<String> gem`

      Ruby packages to install

    - `List<String> go`

      Go packages to install

    - `List<String> npm`

      Node.js packages to install

    - `List<String> pip`

      Python packages to install

    - `Optional<Type> type`

      Package configuration type

      - `PACKAGES("packages")`

  - `JsonValue; type "cloud"constant`

    Environment type

    - `CLOUD("cloud")`

### Beta Cloud Config Params

- `class BetaCloudConfigParams:`

  Request params for `cloud` environment configuration.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `JsonValue; type "cloud"constant`

    Environment type

    - `CLOUD("cloud")`

  - `Optional<Networking> networking`

    Network configuration policy. Omit on update to preserve the existing value.

    - `class BetaUnrestrictedNetwork:`

      Unrestricted network access.

      - `JsonValue; type "unrestricted"constant`

        Network policy type

        - `UNRESTRICTED("unrestricted")`

    - `class BetaLimitedNetworkParams:`

      Limited network request params.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `JsonValue; type "limited"constant`

        Network policy type

        - `LIMITED("limited")`

      - `Optional<Boolean> allowMcpServers`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `Optional<Boolean> allowPackageManagers`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `Optional<List<String>> allowedHosts`

        Specifies domains the container can reach.

  - `Optional<BetaPackagesParams> packages`

    Specify packages (and optionally their versions) available in this environment.

    When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

    - `Optional<List<String>> apt`

      Ubuntu/Debian packages to install

    - `Optional<List<String>> cargo`

      Rust packages to install

    - `Optional<List<String>> gem`

      Ruby packages to install

    - `Optional<List<String>> go`

      Go packages to install

    - `Optional<List<String>> npm`

      Node.js packages to install

    - `Optional<List<String>> pip`

      Python packages to install

    - `Optional<Type> type`

      Package configuration type

      - `PACKAGES("packages")`

### Beta Environment

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and self-hosted environments.

  - `String id`

    Environment identifier (e.g., 'env_...')

  - `Optional<String> archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig:`

      `cloud` environment configuration.

      - `Networking networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork:`

          Unrestricted network access.

          - `JsonValue; type "unrestricted"constant`

            Network policy type

            - `UNRESTRICTED("unrestricted")`

        - `class BetaLimitedNetwork:`

          Limited network access.

          - `boolean allowMcpServers`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `boolean allowPackageManagers`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `List<String> allowedHosts`

            Specifies domains the container can reach.

          - `JsonValue; type "limited"constant`

            Network policy type

            - `LIMITED("limited")`

      - `BetaPackages packages`

        Package manager configuration.

        - `List<String> apt`

          Ubuntu/Debian packages to install

        - `List<String> cargo`

          Rust packages to install

        - `List<String> gem`

          Ruby packages to install

        - `List<String> go`

          Go packages to install

        - `List<String> npm`

          Node.js packages to install

        - `List<String> pip`

          Python packages to install

        - `Optional<Type> type`

          Package configuration type

          - `PACKAGES("packages")`

      - `JsonValue; type "cloud"constant`

        Environment type

        - `CLOUD("cloud")`

    - `class BetaSelfHostedConfig:`

      Configuration for self-hosted environments.

      - `JsonValue; type "self_hosted"constant`

        Environment type

        - `SELF_HOSTED("self_hosted")`

  - `String createdAt`

    RFC 3339 timestamp when environment was created

  - `String description`

    User-provided description for the environment

  - `Metadata metadata`

    User-provided metadata key-value pairs

  - `String name`

    Human-readable name for the environment

  - `JsonValue; type "environment"constant`

    The type of object (always 'environment')

    - `ENVIRONMENT("environment")`

  - `String updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `Optional<Scope> scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `ORGANIZATION("organization")`

    - `ACCOUNT("account")`

### Beta Environment Delete Response

- `class BetaEnvironmentDeleteResponse:`

  Response after deleting an environment.

  - `String id`

    Environment identifier

  - `JsonValue; type "environment_deleted"constant`

    The type of response

    - `ENVIRONMENT_DELETED("environment_deleted")`

### Beta Limited Network

- `class BetaLimitedNetwork:`

  Limited network access.

  - `boolean allowMcpServers`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

  - `boolean allowPackageManagers`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

  - `List<String> allowedHosts`

    Specifies domains the container can reach.

  - `JsonValue; type "limited"constant`

    Network policy type

    - `LIMITED("limited")`

### Beta Limited Network Params

- `class BetaLimitedNetworkParams:`

  Limited network request params.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `JsonValue; type "limited"constant`

    Network policy type

    - `LIMITED("limited")`

  - `Optional<Boolean> allowMcpServers`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `Optional<Boolean> allowPackageManagers`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `Optional<List<String>> allowedHosts`

    Specifies domains the container can reach.

### Beta Packages

- `class BetaPackages:`

  Packages (and their versions) available in this environment.

  - `List<String> apt`

    Ubuntu/Debian packages to install

  - `List<String> cargo`

    Rust packages to install

  - `List<String> gem`

    Ruby packages to install

  - `List<String> go`

    Go packages to install

  - `List<String> npm`

    Node.js packages to install

  - `List<String> pip`

    Python packages to install

  - `Optional<Type> type`

    Package configuration type

    - `PACKAGES("packages")`

### Beta Packages Params

- `class BetaPackagesParams:`

  Specify packages (and optionally their versions) available in this environment.

  When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

  - `Optional<List<String>> apt`

    Ubuntu/Debian packages to install

  - `Optional<List<String>> cargo`

    Rust packages to install

  - `Optional<List<String>> gem`

    Ruby packages to install

  - `Optional<List<String>> go`

    Go packages to install

  - `Optional<List<String>> npm`

    Node.js packages to install

  - `Optional<List<String>> pip`

    Python packages to install

  - `Optional<Type> type`

    Package configuration type

    - `PACKAGES("packages")`

### Beta Self Hosted Config

- `class BetaSelfHostedConfig:`

  Configuration for self-hosted environments.

  - `JsonValue; type "self_hosted"constant`

    Environment type

    - `SELF_HOSTED("self_hosted")`

### Beta Self Hosted Config Params

- `class BetaSelfHostedConfigParams:`

  Request params for `self_hosted` environment configuration.

  - `JsonValue; type "self_hosted"constant`

    Environment type

    - `SELF_HOSTED("self_hosted")`

### Beta Unrestricted Network

- `class BetaUnrestrictedNetwork:`

  Unrestricted network access.

  - `JsonValue; type "unrestricted"constant`

    Network policy type

    - `UNRESTRICTED("unrestricted")`

# Work

## Get Work Item

`BetaSelfHostedWork beta().environments().work().retrieve(WorkRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

### Parameters

- `WorkRetrieveParams params`

  - `String environmentId`

  - `Optional<String> workId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `String id`

    Work identifier (e.g., 'work_...')

  - `Optional<String> acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `String createdAt`

    RFC 3339 timestamp when work was created

  - `BetaSessionWorkData data`

    The actual work to be performed

    - `String id`

      Session identifier (e.g., 'session_...')

    - `JsonValue; type "session"constant`

      Type of work data

      - `SESSION("session")`

  - `String environmentId`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `Optional<String> latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata metadata`

    User-provided metadata key-value pairs associated with this work item

  - `Optional<String> startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

    - `QUEUED("queued")`

    - `STARTING("starting")`

    - `ACTIVE("active")`

    - `STOPPING("stopping")`

    - `STOPPED("stopped")`

  - `Optional<String> stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `Optional<String> stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonValue; type "work"constant`

    The type of object (always 'work')

    - `WORK("work")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWork;
import com.anthropic.models.beta.environments.work.WorkRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkRetrieveParams params = WorkRetrieveParams.builder()
            .environmentId("env_011CZkZ9X2dpNyB7HsEFoRfW")
            .workId("work_id")
            .build();
        BetaSelfHostedWork betaSelfHostedWork = client.beta().environments().work().retrieve(params);
    }
}
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

`BetaSelfHostedWork beta().environments().work().poll(WorkPollParamsparams = WorkPollParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

### Parameters

- `WorkPollParams params`

  - `Optional<String> environmentId`

  - `Optional<Long> blockMs`

    How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

  - `Optional<Long> reclaimOlderThanMs`

    Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

  - `Optional<String> anthropicWorkerId`

    Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `String id`

    Work identifier (e.g., 'work_...')

  - `Optional<String> acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `String createdAt`

    RFC 3339 timestamp when work was created

  - `BetaSessionWorkData data`

    The actual work to be performed

    - `String id`

      Session identifier (e.g., 'session_...')

    - `JsonValue; type "session"constant`

      Type of work data

      - `SESSION("session")`

  - `String environmentId`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `Optional<String> latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata metadata`

    User-provided metadata key-value pairs associated with this work item

  - `Optional<String> startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

    - `QUEUED("queued")`

    - `STARTING("starting")`

    - `ACTIVE("active")`

    - `STOPPING("stopping")`

    - `STOPPED("stopped")`

  - `Optional<String> stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `Optional<String> stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonValue; type "work"constant`

    The type of object (always 'work')

    - `WORK("work")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWork;
import com.anthropic.models.beta.environments.work.WorkPollParams;
import java.util.Optional;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        Optional<BetaSelfHostedWork> betaSelfHostedWork = client.beta().environments().work().poll("env_011CZkZ9X2dpNyB7HsEFoRfW");
    }
}
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

`BetaSelfHostedWork beta().environments().work().ack(WorkAckParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/environments/{environment_id}/work/{work_id}/ack`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Acknowledge receipt of a work item, transitioning it from 'queued' to 'starting' and removing it from the queue.

### Parameters

- `WorkAckParams params`

  - `String environmentId`

  - `Optional<String> workId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `String id`

    Work identifier (e.g., 'work_...')

  - `Optional<String> acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `String createdAt`

    RFC 3339 timestamp when work was created

  - `BetaSessionWorkData data`

    The actual work to be performed

    - `String id`

      Session identifier (e.g., 'session_...')

    - `JsonValue; type "session"constant`

      Type of work data

      - `SESSION("session")`

  - `String environmentId`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `Optional<String> latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata metadata`

    User-provided metadata key-value pairs associated with this work item

  - `Optional<String> startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

    - `QUEUED("queued")`

    - `STARTING("starting")`

    - `ACTIVE("active")`

    - `STOPPING("stopping")`

    - `STOPPED("stopped")`

  - `Optional<String> stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `Optional<String> stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonValue; type "work"constant`

    The type of object (always 'work')

    - `WORK("work")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWork;
import com.anthropic.models.beta.environments.work.WorkAckParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkAckParams params = WorkAckParams.builder()
            .environmentId("env_011CZkZ9X2dpNyB7HsEFoRfW")
            .workId("work_id")
            .build();
        BetaSelfHostedWork betaSelfHostedWork = client.beta().environments().work().ack(params);
    }
}
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

`BetaSelfHostedWorkHeartbeatResponse beta().environments().work().heartbeat(WorkHeartbeatParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/environments/{environment_id}/work/{work_id}/heartbeat`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

### Parameters

- `WorkHeartbeatParams params`

  - `String environmentId`

  - `Optional<String> workId`

  - `Optional<Long> desiredTtlSeconds`

    Desired TTL in seconds

  - `Optional<String> expectedLastHeartbeat`

    Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

### Returns

- `class BetaSelfHostedWorkHeartbeatResponse:`

  Response after recording a heartbeat for a work item.

  - `String lastHeartbeat`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `boolean leaseExtended`

    Whether the heartbeat succeeded in extending the lease

  - `State state`

    Current state of the work item (active/stopping/stopped)

    - `QUEUED("queued")`

    - `STARTING("starting")`

    - `ACTIVE("active")`

    - `STOPPING("stopping")`

    - `STOPPED("stopped")`

  - `long ttlSeconds`

    Effective TTL applied to the lease

  - `JsonValue; type "work_heartbeat"constant`

    The type of response

    - `WORK_HEARTBEAT("work_heartbeat")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWorkHeartbeatResponse;
import com.anthropic.models.beta.environments.work.WorkHeartbeatParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkHeartbeatParams params = WorkHeartbeatParams.builder()
            .environmentId("env_011CZkZ9X2dpNyB7HsEFoRfW")
            .workId("work_id")
            .build();
        BetaSelfHostedWorkHeartbeatResponse betaSelfHostedWorkHeartbeatResponse = client.beta().environments().work().heartbeat(params);
    }
}
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

`BetaSelfHostedWork beta().environments().work().stop(WorkStopParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

### Parameters

- `WorkStopParams params`

  - `String environmentId`

  - `Optional<String> workId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

  - `BetaSelfHostedWorkStopRequest betaSelfHostedWorkStopRequest`

    Request to stop a work item.

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `String id`

    Work identifier (e.g., 'work_...')

  - `Optional<String> acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `String createdAt`

    RFC 3339 timestamp when work was created

  - `BetaSessionWorkData data`

    The actual work to be performed

    - `String id`

      Session identifier (e.g., 'session_...')

    - `JsonValue; type "session"constant`

      Type of work data

      - `SESSION("session")`

  - `String environmentId`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `Optional<String> latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata metadata`

    User-provided metadata key-value pairs associated with this work item

  - `Optional<String> startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

    - `QUEUED("queued")`

    - `STARTING("starting")`

    - `ACTIVE("active")`

    - `STOPPING("stopping")`

    - `STOPPED("stopped")`

  - `Optional<String> stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `Optional<String> stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonValue; type "work"constant`

    The type of object (always 'work')

    - `WORK("work")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWork;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWorkStopRequest;
import com.anthropic.models.beta.environments.work.WorkStopParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkStopParams params = WorkStopParams.builder()
            .environmentId("env_011CZkZ9X2dpNyB7HsEFoRfW")
            .workId("work_id")
            .betaSelfHostedWorkStopRequest(BetaSelfHostedWorkStopRequest.builder().build())
            .build();
        BetaSelfHostedWork betaSelfHostedWork = client.beta().environments().work().stop(params);
    }
}
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

`WorkListPage beta().environments().work().list(WorkListParamsparams = WorkListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

### Parameters

- `WorkListParams params`

  - `Optional<String> environmentId`

  - `Optional<Long> limit`

    Maximum number of work items to return

  - `Optional<String> page`

    Opaque cursor from previous response for pagination

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `String id`

    Work identifier (e.g., 'work_...')

  - `Optional<String> acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `String createdAt`

    RFC 3339 timestamp when work was created

  - `BetaSessionWorkData data`

    The actual work to be performed

    - `String id`

      Session identifier (e.g., 'session_...')

    - `JsonValue; type "session"constant`

      Type of work data

      - `SESSION("session")`

  - `String environmentId`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `Optional<String> latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata metadata`

    User-provided metadata key-value pairs associated with this work item

  - `Optional<String> startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

    - `QUEUED("queued")`

    - `STARTING("starting")`

    - `ACTIVE("active")`

    - `STOPPING("stopping")`

    - `STOPPED("stopped")`

  - `Optional<String> stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `Optional<String> stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonValue; type "work"constant`

    The type of object (always 'work')

    - `WORK("work")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.work.WorkListPage;
import com.anthropic.models.beta.environments.work.WorkListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkListPage page = client.beta().environments().work().list("env_011CZkZ9X2dpNyB7HsEFoRfW");
    }
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

`BetaSelfHostedWork beta().environments().work().update(WorkUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

### Parameters

- `WorkUpdateParams params`

  - `String environmentId`

  - `Optional<String> workId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

  - `BetaSelfHostedWorkUpdateRequest betaSelfHostedWorkUpdateRequest`

    Request to update work item metadata.

### Returns

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `String id`

    Work identifier (e.g., 'work_...')

  - `Optional<String> acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `String createdAt`

    RFC 3339 timestamp when work was created

  - `BetaSessionWorkData data`

    The actual work to be performed

    - `String id`

      Session identifier (e.g., 'session_...')

    - `JsonValue; type "session"constant`

      Type of work data

      - `SESSION("session")`

  - `String environmentId`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `Optional<String> latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata metadata`

    User-provided metadata key-value pairs associated with this work item

  - `Optional<String> startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

    - `QUEUED("queued")`

    - `STARTING("starting")`

    - `ACTIVE("active")`

    - `STOPPING("stopping")`

    - `STOPPED("stopped")`

  - `Optional<String> stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `Optional<String> stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonValue; type "work"constant`

    The type of object (always 'work')

    - `WORK("work")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.JsonValue;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWork;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWorkUpdateRequest;
import com.anthropic.models.beta.environments.work.WorkUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkUpdateParams params = WorkUpdateParams.builder()
            .environmentId("env_011CZkZ9X2dpNyB7HsEFoRfW")
            .workId("work_id")
            .betaSelfHostedWorkUpdateRequest(BetaSelfHostedWorkUpdateRequest.builder()
                .metadata(BetaSelfHostedWorkUpdateRequest.Metadata.builder()
                    .putAdditionalProperty("foo", JsonValue.from("string"))
                    .build())
                .build())
            .build();
        BetaSelfHostedWork betaSelfHostedWork = client.beta().environments().work().update(params);
    }
}
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

`BetaSelfHostedWorkQueueStats beta().environments().work().stats(WorkStatsParamsparams = WorkStatsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

### Parameters

- `WorkStatsParams params`

  - `Optional<String> environmentId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `MID_CONVERSATION_SYSTEM_2026_04_07("mid-conversation-system-2026-04-07")`

### Returns

- `class BetaSelfHostedWorkQueueStats:`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `long depth`

    Number of work items waiting to be picked up (lag from consumer group)

  - `Optional<String> oldestQueuedAt`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `long pending`

    Number of work items being processed (polled but not acknowledged)

  - `JsonValue; type "work_queue_stats"constant`

    The type of object

    - `WORK_QUEUE_STATS("work_queue_stats")`

  - `Optional<Long> workersPolling`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWorkQueueStats;
import com.anthropic.models.beta.environments.work.WorkStatsParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaSelfHostedWorkQueueStats betaSelfHostedWorkQueueStats = client.beta().environments().work().stats("env_011CZkZ9X2dpNyB7HsEFoRfW");
    }
}
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

  - `String id`

    Work identifier (e.g., 'work_...')

  - `Optional<String> acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `String createdAt`

    RFC 3339 timestamp when work was created

  - `BetaSessionWorkData data`

    The actual work to be performed

    - `String id`

      Session identifier (e.g., 'session_...')

    - `JsonValue; type "session"constant`

      Type of work data

      - `SESSION("session")`

  - `String environmentId`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `Optional<String> latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata metadata`

    User-provided metadata key-value pairs associated with this work item

  - `Optional<String> startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

    - `QUEUED("queued")`

    - `STARTING("starting")`

    - `ACTIVE("active")`

    - `STOPPING("stopping")`

    - `STOPPED("stopped")`

  - `Optional<String> stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `Optional<String> stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonValue; type "work"constant`

    The type of object (always 'work')

    - `WORK("work")`

### Beta Self Hosted Work Heartbeat Response

- `class BetaSelfHostedWorkHeartbeatResponse:`

  Response after recording a heartbeat for a work item.

  - `String lastHeartbeat`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `boolean leaseExtended`

    Whether the heartbeat succeeded in extending the lease

  - `State state`

    Current state of the work item (active/stopping/stopped)

    - `QUEUED("queued")`

    - `STARTING("starting")`

    - `ACTIVE("active")`

    - `STOPPING("stopping")`

    - `STOPPED("stopped")`

  - `long ttlSeconds`

    Effective TTL applied to the lease

  - `JsonValue; type "work_heartbeat"constant`

    The type of response

    - `WORK_HEARTBEAT("work_heartbeat")`

### Beta Self Hosted Work List Response

- `class BetaSelfHostedWorkListResponse:`

  Response when listing work items with cursor-based pagination.

  - `List<BetaSelfHostedWork> data`

    List of work items

    - `String id`

      Work identifier (e.g., 'work_...')

    - `Optional<String> acknowledgedAt`

      RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

    - `String createdAt`

      RFC 3339 timestamp when work was created

    - `BetaSessionWorkData data`

      The actual work to be performed

      - `String id`

        Session identifier (e.g., 'session_...')

      - `JsonValue; type "session"constant`

        Type of work data

        - `SESSION("session")`

    - `String environmentId`

      Environment identifier this work belongs to (e.g., `env_...`)

    - `Optional<String> latestHeartbeatAt`

      RFC 3339 timestamp of the most recent heartbeat

    - `Metadata metadata`

      User-provided metadata key-value pairs associated with this work item

    - `Optional<String> startedAt`

      RFC 3339 timestamp when work execution started

    - `State state`

      Current state of the work item

      - `QUEUED("queued")`

      - `STARTING("starting")`

      - `ACTIVE("active")`

      - `STOPPING("stopping")`

      - `STOPPED("stopped")`

    - `Optional<String> stopRequestedAt`

      RFC 3339 timestamp when stop was requested

    - `Optional<String> stoppedAt`

      RFC 3339 timestamp when work execution stopped

    - `JsonValue; type "work"constant`

      The type of object (always 'work')

      - `WORK("work")`

  - `Optional<String> nextPage`

    Opaque cursor for fetching the next page of results

### Beta Self Hosted Work Queue Stats

- `class BetaSelfHostedWorkQueueStats:`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `long depth`

    Number of work items waiting to be picked up (lag from consumer group)

  - `Optional<String> oldestQueuedAt`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `long pending`

    Number of work items being processed (polled but not acknowledged)

  - `JsonValue; type "work_queue_stats"constant`

    The type of object

    - `WORK_QUEUE_STATS("work_queue_stats")`

  - `Optional<Long> workersPolling`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Beta Self Hosted Work Stop Request

- `class BetaSelfHostedWorkStopRequest:`

  Request to stop a work item.

  - `Optional<Boolean> force`

    If true, immediately stop work without graceful shutdown

### Beta Self Hosted Work Update Request

- `class BetaSelfHostedWorkUpdateRequest:`

  Request to update work item metadata.

  - `Metadata metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

### Beta Session Work Data

- `class BetaSessionWorkData:`

  Work data for session work items.

  This resource type is used when work represents a session that needs to be executed
  in a self-hosted environment.

  - `String id`

    Session identifier (e.g., 'session_...')

  - `JsonValue; type "session"constant`

    Type of work data

    - `SESSION("session")`

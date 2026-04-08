# Environments

## Create

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

  - `String name`

    Human-readable name for the environment

  - `Optional<BetaCloudConfigParams> config`

    Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

  - `Optional<String> description`

    Optional description of the environment

  - `Optional<Metadata> metadata`

    User-provided metadata key-value pairs

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and BYOC environments.

  - `String id`

    Environment identifier (e.g., 'env_...')

  - `Optional<String> archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `BetaCloudConfig config`

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

## List

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

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and BYOC environments.

  - `String id`

    Environment identifier (e.g., 'env_...')

  - `Optional<String> archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `BetaCloudConfig config`

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

## Retrieve

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

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and BYOC environments.

  - `String id`

    Environment identifier (e.g., 'env_...')

  - `Optional<String> archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `BetaCloudConfig config`

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

## Update

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

  - `Optional<BetaCloudConfigParams> config`

    Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

  - `Optional<String> description`

    Updated description of the environment

  - `Optional<Metadata> metadata`

    User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

  - `Optional<String> name`

    Updated name for the environment

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and BYOC environments.

  - `String id`

    Environment identifier (e.g., 'env_...')

  - `Optional<String> archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `BetaCloudConfig config`

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

## Delete

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

## Archive

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

### Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and BYOC environments.

  - `String id`

    Environment identifier (e.g., 'env_...')

  - `Optional<String> archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `BetaCloudConfig config`

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

  Unified Environment resource for both cloud and BYOC environments.

  - `String id`

    Environment identifier (e.g., 'env_...')

  - `Optional<String> archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `BetaCloudConfig config`

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

### Beta Unrestricted Network

- `class BetaUnrestrictedNetwork:`

  Unrestricted network access.

  - `JsonValue; type "unrestricted"constant`

    Network policy type

    - `UNRESTRICTED("unrestricted")`

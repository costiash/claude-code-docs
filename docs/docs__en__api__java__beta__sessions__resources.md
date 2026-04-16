# Resources

## Add

`BetaManagedAgentsFileResource beta().sessions().resources().add(ResourceAddParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Parameters

- `ResourceAddParams params`

  - `Optional<String> sessionId`

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

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

  - `BetaManagedAgentsFileResourceParams betaManagedAgentsFileResourceParams`

    Mount a file uploaded via the Files API into the session.

### Returns

- `class BetaManagedAgentsFileResource:`

  - `String id`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String fileId`

  - `String mountPath`

  - `Type type`

    - `FILE("file")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.BetaManagedAgentsFileResourceParams;
import com.anthropic.models.beta.sessions.resources.BetaManagedAgentsFileResource;
import com.anthropic.models.beta.sessions.resources.ResourceAddParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceAddParams params = ResourceAddParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .betaManagedAgentsFileResourceParams(BetaManagedAgentsFileResourceParams.builder()
                .fileId("file_011CNha8iCJcU1wXNR6q4V8w")
                .type(BetaManagedAgentsFileResourceParams.Type.FILE)
                .build())
            .build();
        BetaManagedAgentsFileResource betaManagedAgentsFileResource = client.beta().sessions().resources().add(params);
    }
}
```

## List

`ResourceListPage beta().sessions().resources().list(ResourceListParamsparams = ResourceListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Parameters

- `ResourceListParams params`

  - `Optional<String> sessionId`

  - `Optional<Long> limit`

    Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

  - `Optional<String> page`

    Opaque cursor from a previous response's next_page field.

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

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

### Returns

- `class BetaManagedAgentsSessionResource: A class that can be one of several variants.union`

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

    - `String mountPath`

    - `Type type`

      - `GITHUB_REPOSITORY("github_repository")`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

    - `String url`

    - `Optional<Checkout> checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `String name`

          Branch name to check out.

        - `Type type`

          - `BRANCH("branch")`

      - `class BetaManagedAgentsCommitCheckout:`

        - `String sha`

          Full commit SHA to check out.

        - `Type type`

          - `COMMIT("commit")`

  - `class BetaManagedAgentsFileResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

    - `String fileId`

    - `String mountPath`

    - `Type type`

      - `FILE("file")`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.resources.ResourceListPage;
import com.anthropic.models.beta.sessions.resources.ResourceListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceListPage page = client.beta().sessions().resources().list("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
}
```

## Retrieve

`ResourceRetrieveResponse beta().sessions().resources().retrieve(ResourceRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `ResourceRetrieveParams params`

  - `String sessionId`

  - `Optional<String> resourceId`

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

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

### Returns

- `class ResourceRetrieveResponse: A class that can be one of several variants.union`

  The requested session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

    - `String mountPath`

    - `Type type`

      - `GITHUB_REPOSITORY("github_repository")`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

    - `String url`

    - `Optional<Checkout> checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `String name`

          Branch name to check out.

        - `Type type`

          - `BRANCH("branch")`

      - `class BetaManagedAgentsCommitCheckout:`

        - `String sha`

          Full commit SHA to check out.

        - `Type type`

          - `COMMIT("commit")`

  - `class BetaManagedAgentsFileResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

    - `String fileId`

    - `String mountPath`

    - `Type type`

      - `FILE("file")`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.resources.ResourceRetrieveParams;
import com.anthropic.models.beta.sessions.resources.ResourceRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceRetrieveParams params = ResourceRetrieveParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .resourceId("sesrsc_011CZkZBJq5dWxk9fVLNcPht")
            .build();
        ResourceRetrieveResponse resource = client.beta().sessions().resources().retrieve(params);
    }
}
```

## Update

`ResourceUpdateResponse beta().sessions().resources().update(ResourceUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Parameters

- `ResourceUpdateParams params`

  - `String sessionId`

  - `Optional<String> resourceId`

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

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

  - `String authorizationToken`

    New authorization token for the resource. Currently only `github_repository` resources support token rotation.

### Returns

- `class ResourceUpdateResponse: A class that can be one of several variants.union`

  The updated session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

    - `String mountPath`

    - `Type type`

      - `GITHUB_REPOSITORY("github_repository")`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

    - `String url`

    - `Optional<Checkout> checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `String name`

          Branch name to check out.

        - `Type type`

          - `BRANCH("branch")`

      - `class BetaManagedAgentsCommitCheckout:`

        - `String sha`

          Full commit SHA to check out.

        - `Type type`

          - `COMMIT("commit")`

  - `class BetaManagedAgentsFileResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

    - `String fileId`

    - `String mountPath`

    - `Type type`

      - `FILE("file")`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.resources.ResourceUpdateParams;
import com.anthropic.models.beta.sessions.resources.ResourceUpdateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceUpdateParams params = ResourceUpdateParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .resourceId("sesrsc_011CZkZBJq5dWxk9fVLNcPht")
            .authorizationToken("ghp_exampletoken")
            .build();
        ResourceUpdateResponse resource = client.beta().sessions().resources().update(params);
    }
}
```

## Delete

`BetaManagedAgentsDeleteSessionResource beta().sessions().resources().delete(ResourceDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Parameters

- `ResourceDeleteParams params`

  - `String sessionId`

  - `Optional<String> resourceId`

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

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

### Returns

- `class BetaManagedAgentsDeleteSessionResource:`

  Confirmation of resource deletion.

  - `String id`

  - `Type type`

    - `SESSION_RESOURCE_DELETED("session_resource_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.resources.BetaManagedAgentsDeleteSessionResource;
import com.anthropic.models.beta.sessions.resources.ResourceDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceDeleteParams params = ResourceDeleteParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .resourceId("sesrsc_011CZkZBJq5dWxk9fVLNcPht")
            .build();
        BetaManagedAgentsDeleteSessionResource betaManagedAgentsDeleteSessionResource = client.beta().sessions().resources().delete(params);
    }
}
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `class BetaManagedAgentsDeleteSessionResource:`

  Confirmation of resource deletion.

  - `String id`

  - `Type type`

    - `SESSION_RESOURCE_DELETED("session_resource_deleted")`

### Beta Managed Agents File Resource

- `class BetaManagedAgentsFileResource:`

  - `String id`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String fileId`

  - `String mountPath`

  - `Type type`

    - `FILE("file")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents GitHub Repository Resource

- `class BetaManagedAgentsGitHubRepositoryResource:`

  - `String id`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String mountPath`

  - `Type type`

    - `GITHUB_REPOSITORY("github_repository")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String url`

  - `Optional<Checkout> checkout`

    - `class BetaManagedAgentsBranchCheckout:`

      - `String name`

        Branch name to check out.

      - `Type type`

        - `BRANCH("branch")`

    - `class BetaManagedAgentsCommitCheckout:`

      - `String sha`

        Full commit SHA to check out.

      - `Type type`

        - `COMMIT("commit")`

### Beta Managed Agents Session Resource

- `class BetaManagedAgentsSessionResource: A class that can be one of several variants.union`

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

    - `String mountPath`

    - `Type type`

      - `GITHUB_REPOSITORY("github_repository")`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

    - `String url`

    - `Optional<Checkout> checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `String name`

          Branch name to check out.

        - `Type type`

          - `BRANCH("branch")`

      - `class BetaManagedAgentsCommitCheckout:`

        - `String sha`

          Full commit SHA to check out.

        - `Type type`

          - `COMMIT("commit")`

  - `class BetaManagedAgentsFileResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

    - `String fileId`

    - `String mountPath`

    - `Type type`

      - `FILE("file")`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

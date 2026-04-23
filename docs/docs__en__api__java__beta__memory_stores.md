# Memory Stores

## Create

`BetaManagedAgentsMemoryStore beta().memoryStores().create(MemoryStoreCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/memory_stores`

CreateMemoryStore

### Parameters

- `MemoryStoreCreateParams params`

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

  - `String name`

  - `Optional<String> description`

  - `Optional<Metadata> metadata`

### Returns

- `class BetaManagedAgentsMemoryStore:`

  - `String id`

  - `Type type`

    - `MEMORY_STORE("memory_store")`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

  - `Optional<Metadata> metadata`

  - `Optional<String> name`

  - `Optional<LocalDateTime> updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryStoreCreateParams params = MemoryStoreCreateParams.builder()
            .name("x")
            .build();
        BetaManagedAgentsMemoryStore betaManagedAgentsMemoryStore = client.beta().memoryStores().create(params);
    }
}
```

## List

`MemoryStoreListPage beta().memoryStores().list(MemoryStoreListParamsparams = MemoryStoreListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/memory_stores`

ListMemoryStores

### Parameters

- `MemoryStoreListParams params`

  - `Optional<LocalDateTime> createdAtGte`

    Return stores created at or after this time (inclusive).

  - `Optional<LocalDateTime> createdAtLte`

    Return stores created at or before this time (inclusive).

  - `Optional<Boolean> includeArchived`

    Query parameter for include_archived

  - `Optional<Long> limit`

    Query parameter for limit

  - `Optional<String> page`

    Query parameter for page

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

### Returns

- `class BetaManagedAgentsMemoryStore:`

  - `String id`

  - `Type type`

    - `MEMORY_STORE("memory_store")`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

  - `Optional<Metadata> metadata`

  - `Optional<String> name`

  - `Optional<LocalDateTime> updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.MemoryStoreListPage;
import com.anthropic.models.beta.memorystores.MemoryStoreListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryStoreListPage page = client.beta().memoryStores().list();
    }
}
```

## Retrieve

`BetaManagedAgentsMemoryStore beta().memoryStores().retrieve(MemoryStoreRetrieveParamsparams = MemoryStoreRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/memory_stores/{memory_store_id}`

GetMemoryStore

### Parameters

- `MemoryStoreRetrieveParams params`

  - `Optional<String> memoryStoreId`

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

### Returns

- `class BetaManagedAgentsMemoryStore:`

  - `String id`

  - `Type type`

    - `MEMORY_STORE("memory_store")`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

  - `Optional<Metadata> metadata`

  - `Optional<String> name`

  - `Optional<LocalDateTime> updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsMemoryStore betaManagedAgentsMemoryStore = client.beta().memoryStores().retrieve("memory_store_id");
    }
}
```

## Update

`BetaManagedAgentsMemoryStore beta().memoryStores().update(MemoryStoreUpdateParamsparams = MemoryStoreUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/memory_stores/{memory_store_id}`

UpdateMemoryStore

### Parameters

- `MemoryStoreUpdateParams params`

  - `Optional<String> memoryStoreId`

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

  - `Optional<String> description`

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Optional<String> name`

### Returns

- `class BetaManagedAgentsMemoryStore:`

  - `String id`

  - `Type type`

    - `MEMORY_STORE("memory_store")`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

  - `Optional<Metadata> metadata`

  - `Optional<String> name`

  - `Optional<LocalDateTime> updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsMemoryStore betaManagedAgentsMemoryStore = client.beta().memoryStores().update("memory_store_id");
    }
}
```

## Delete

`BetaManagedAgentsDeletedMemoryStore beta().memoryStores().delete(MemoryStoreDeleteParamsparams = MemoryStoreDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/memory_stores/{memory_store_id}`

DeleteMemoryStore

### Parameters

- `MemoryStoreDeleteParams params`

  - `Optional<String> memoryStoreId`

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

### Returns

- `class BetaManagedAgentsDeletedMemoryStore:`

  - `String id`

  - `Type type`

    - `MEMORY_STORE_DELETED("memory_store_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsDeletedMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeletedMemoryStore betaManagedAgentsDeletedMemoryStore = client.beta().memoryStores().delete("memory_store_id");
    }
}
```

## Archive

`BetaManagedAgentsMemoryStore beta().memoryStores().archive(MemoryStoreArchiveParamsparams = MemoryStoreArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/memory_stores/{memory_store_id}/archive`

ArchiveMemoryStore

### Parameters

- `MemoryStoreArchiveParams params`

  - `Optional<String> memoryStoreId`

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

### Returns

- `class BetaManagedAgentsMemoryStore:`

  - `String id`

  - `Type type`

    - `MEMORY_STORE("memory_store")`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

  - `Optional<Metadata> metadata`

  - `Optional<String> name`

  - `Optional<LocalDateTime> updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsMemoryStore betaManagedAgentsMemoryStore = client.beta().memoryStores().archive("memory_store_id");
    }
}
```

## Domain Types

### Beta Managed Agents Deleted Memory Store

- `class BetaManagedAgentsDeletedMemoryStore:`

  - `String id`

  - `Type type`

    - `MEMORY_STORE_DELETED("memory_store_deleted")`

### Beta Managed Agents Memory Store

- `class BetaManagedAgentsMemoryStore:`

  - `String id`

  - `Type type`

    - `MEMORY_STORE("memory_store")`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Optional<LocalDateTime> createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

  - `Optional<Metadata> metadata`

  - `Optional<String> name`

  - `Optional<LocalDateTime> updatedAt`

    A timestamp in RFC 3339 format

# Memories

## Create

`BetaManagedAgentsMemory beta().memoryStores().memories().create(MemoryCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/memory_stores/{memory_store_id}/memories`

CreateMemory

### Parameters

- `MemoryCreateParams params`

  - `Optional<String> memoryStoreId`

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

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

  - `Optional<String> content`

  - `String path`

### Returns

- `class BetaManagedAgentsMemory:`

  - `String id`

  - `String contentSha256`

  - `long contentSizeBytes`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryStoreId`

  - `String memoryVersionId`

  - `String path`

  - `Type type`

    - `MEMORY("memory")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> content`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.BetaManagedAgentsMemory;
import com.anthropic.models.beta.memorystores.memories.MemoryCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryCreateParams params = MemoryCreateParams.builder()
            .memoryStoreId("memory_store_id")
            .content("content")
            .path("xx")
            .build();
        BetaManagedAgentsMemory betaManagedAgentsMemory = client.beta().memoryStores().memories().create(params);
    }
}
```

## List

`MemoryListPage beta().memoryStores().memories().list(MemoryListParamsparams = MemoryListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/memory_stores/{memory_store_id}/memories`

ListMemories

### Parameters

- `MemoryListParams params`

  - `Optional<String> memoryStoreId`

  - `Optional<Long> depth`

    Query parameter for depth

  - `Optional<Long> limit`

    Query parameter for limit

  - `Optional<Order> order`

    Query parameter for order

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> orderBy`

    Query parameter for order_by

  - `Optional<String> page`

    Query parameter for page

  - `Optional<String> pathPrefix`

    Optional path prefix filter (raw string-prefix match; include a trailing slash for directory-scoped lists). This value appears in request URLs. Do not include secrets or personally identifiable information.

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

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

### Returns

- `class BetaManagedAgentsMemoryListItem: A class that can be one of several variants.union`

  - `class BetaManagedAgentsMemory:`

    - `String id`

    - `String contentSha256`

    - `long contentSizeBytes`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

    - `String memoryStoreId`

    - `String memoryVersionId`

    - `String path`

    - `Type type`

      - `MEMORY("memory")`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

    - `Optional<String> content`

  - `class BetaManagedAgentsMemoryPrefix:`

    - `String path`

    - `Type type`

      - `MEMORY_PREFIX("memory_prefix")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.MemoryListPage;
import com.anthropic.models.beta.memorystores.memories.MemoryListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryListPage page = client.beta().memoryStores().memories().list("memory_store_id");
    }
}
```

## Retrieve

`BetaManagedAgentsMemory beta().memoryStores().memories().retrieve(MemoryRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

GetMemory

### Parameters

- `MemoryRetrieveParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryId`

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

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

### Returns

- `class BetaManagedAgentsMemory:`

  - `String id`

  - `String contentSha256`

  - `long contentSizeBytes`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryStoreId`

  - `String memoryVersionId`

  - `String path`

  - `Type type`

    - `MEMORY("memory")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> content`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.BetaManagedAgentsMemory;
import com.anthropic.models.beta.memorystores.memories.MemoryRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryRetrieveParams params = MemoryRetrieveParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryId("memory_id")
            .build();
        BetaManagedAgentsMemory betaManagedAgentsMemory = client.beta().memoryStores().memories().retrieve(params);
    }
}
```

## Update

`BetaManagedAgentsMemory beta().memoryStores().memories().update(MemoryUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

UpdateMemory

### Parameters

- `MemoryUpdateParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryId`

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

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

  - `Optional<String> content`

  - `Optional<String> path`

  - `Optional<BetaManagedAgentsPrecondition> precondition`

### Returns

- `class BetaManagedAgentsMemory:`

  - `String id`

  - `String contentSha256`

  - `long contentSizeBytes`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryStoreId`

  - `String memoryVersionId`

  - `String path`

  - `Type type`

    - `MEMORY("memory")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> content`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.BetaManagedAgentsMemory;
import com.anthropic.models.beta.memorystores.memories.MemoryUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryUpdateParams params = MemoryUpdateParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryId("memory_id")
            .build();
        BetaManagedAgentsMemory betaManagedAgentsMemory = client.beta().memoryStores().memories().update(params);
    }
}
```

## Delete

`BetaManagedAgentsDeletedMemory beta().memoryStores().memories().delete(MemoryDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

DeleteMemory

### Parameters

- `MemoryDeleteParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryId`

  - `Optional<String> expectedContentSha256`

    Query parameter for expected_content_sha256

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

### Returns

- `class BetaManagedAgentsDeletedMemory:`

  - `String id`

  - `Type type`

    - `MEMORY_DELETED("memory_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.BetaManagedAgentsDeletedMemory;
import com.anthropic.models.beta.memorystores.memories.MemoryDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryDeleteParams params = MemoryDeleteParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryId("memory_id")
            .build();
        BetaManagedAgentsDeletedMemory betaManagedAgentsDeletedMemory = client.beta().memoryStores().memories().delete(params);
    }
}
```

## Domain Types

### Beta Managed Agents Content Sha256 Precondition

- `class BetaManagedAgentsContentSha256Precondition:`

  - `Type type`

    - `CONTENT_SHA256("content_sha256")`

  - `Optional<String> contentSha256`

### Beta Managed Agents Deleted Memory

- `class BetaManagedAgentsDeletedMemory:`

  - `String id`

  - `Type type`

    - `MEMORY_DELETED("memory_deleted")`

### Beta Managed Agents Memory

- `class BetaManagedAgentsMemory:`

  - `String id`

  - `String contentSha256`

  - `long contentSizeBytes`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryStoreId`

  - `String memoryVersionId`

  - `String path`

  - `Type type`

    - `MEMORY("memory")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `Optional<String> content`

### Beta Managed Agents Memory List Item

- `class BetaManagedAgentsMemoryListItem: A class that can be one of several variants.union`

  - `class BetaManagedAgentsMemory:`

    - `String id`

    - `String contentSha256`

    - `long contentSizeBytes`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

    - `String memoryStoreId`

    - `String memoryVersionId`

    - `String path`

    - `Type type`

      - `MEMORY("memory")`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

    - `Optional<String> content`

  - `class BetaManagedAgentsMemoryPrefix:`

    - `String path`

    - `Type type`

      - `MEMORY_PREFIX("memory_prefix")`

### Beta Managed Agents Memory Path Conflict Error

- `class BetaManagedAgentsMemoryPathConflictError:`

  - `Type type`

    - `MEMORY_PATH_CONFLICT_ERROR("memory_path_conflict_error")`

  - `Optional<String> conflictingMemoryId`

  - `Optional<String> conflictingPath`

  - `Optional<String> message`

### Beta Managed Agents Memory Precondition Failed Error

- `class BetaManagedAgentsMemoryPreconditionFailedError:`

  - `Type type`

    - `MEMORY_PRECONDITION_FAILED_ERROR("memory_precondition_failed_error")`

  - `Optional<String> message`

### Beta Managed Agents Memory Prefix

- `class BetaManagedAgentsMemoryPrefix:`

  - `String path`

  - `Type type`

    - `MEMORY_PREFIX("memory_prefix")`

### Beta Managed Agents Memory View

- `enum BetaManagedAgentsMemoryView:`

  MemoryView enum

  - `BASIC("basic")`

  - `FULL("full")`

### Beta Managed Agents Precondition

- `class BetaManagedAgentsPrecondition:`

  - `Type type`

    - `CONTENT_SHA256("content_sha256")`

  - `Optional<String> contentSha256`

# Memory Versions

## List

`MemoryVersionListPage beta().memoryStores().memoryVersions().list(MemoryVersionListParamsparams = MemoryVersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

ListMemoryVersions

### Parameters

- `MemoryVersionListParams params`

  - `Optional<String> memoryStoreId`

  - `Optional<String> apiKeyId`

    Query parameter for api_key_id

  - `Optional<LocalDateTime> createdAtGte`

    Return versions created at or after this time (inclusive).

  - `Optional<LocalDateTime> createdAtLte`

    Return versions created at or before this time (inclusive).

  - `Optional<Long> limit`

    Query parameter for limit

  - `Optional<String> memoryId`

    Query parameter for memory_id

  - `Optional<BetaManagedAgentsMemoryVersionOperation> operation`

    Query parameter for operation

  - `Optional<String> page`

    Query parameter for page

  - `Optional<String> sessionId`

    Query parameter for session_id

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

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

### Returns

- `class BetaManagedAgentsMemoryVersion:`

  - `String id`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryId`

  - `String memoryStoreId`

  - `BetaManagedAgentsMemoryVersionOperation operation`

    MemoryVersionOperation enum

    - `CREATED("created")`

    - `MODIFIED("modified")`

    - `DELETED("deleted")`

  - `Type type`

    - `MEMORY_VERSION("memory_version")`

  - `Optional<String> content`

  - `Optional<String> contentSha256`

  - `Optional<Long> contentSizeBytes`

  - `Optional<BetaManagedAgentsActor> createdBy`

    - `class BetaManagedAgentsSessionActor:`

      - `String sessionId`

      - `Type type`

        - `SESSION_ACTOR("session_actor")`

    - `class BetaManagedAgentsApiActor:`

      - `String apiKeyId`

      - `Type type`

        - `API_ACTOR("api_actor")`

    - `class BetaManagedAgentsUserActor:`

      - `Type type`

        - `USER_ACTOR("user_actor")`

      - `String userId`

  - `Optional<String> path`

  - `Optional<LocalDateTime> redactedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsActor> redactedBy`

    - `class BetaManagedAgentsSessionActor:`

      - `String sessionId`

      - `Type type`

        - `SESSION_ACTOR("session_actor")`

    - `class BetaManagedAgentsApiActor:`

      - `String apiKeyId`

      - `Type type`

        - `API_ACTOR("api_actor")`

    - `class BetaManagedAgentsUserActor:`

      - `Type type`

        - `USER_ACTOR("user_actor")`

      - `String userId`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionListPage;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryVersionListPage page = client.beta().memoryStores().memoryVersions().list("memory_store_id");
    }
}
```

## Retrieve

`BetaManagedAgentsMemoryVersion beta().memoryStores().memoryVersions().retrieve(MemoryVersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

GetMemoryVersion

### Parameters

- `MemoryVersionRetrieveParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryVersionId`

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

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

### Returns

- `class BetaManagedAgentsMemoryVersion:`

  - `String id`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryId`

  - `String memoryStoreId`

  - `BetaManagedAgentsMemoryVersionOperation operation`

    MemoryVersionOperation enum

    - `CREATED("created")`

    - `MODIFIED("modified")`

    - `DELETED("deleted")`

  - `Type type`

    - `MEMORY_VERSION("memory_version")`

  - `Optional<String> content`

  - `Optional<String> contentSha256`

  - `Optional<Long> contentSizeBytes`

  - `Optional<BetaManagedAgentsActor> createdBy`

    - `class BetaManagedAgentsSessionActor:`

      - `String sessionId`

      - `Type type`

        - `SESSION_ACTOR("session_actor")`

    - `class BetaManagedAgentsApiActor:`

      - `String apiKeyId`

      - `Type type`

        - `API_ACTOR("api_actor")`

    - `class BetaManagedAgentsUserActor:`

      - `Type type`

        - `USER_ACTOR("user_actor")`

      - `String userId`

  - `Optional<String> path`

  - `Optional<LocalDateTime> redactedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsActor> redactedBy`

    - `class BetaManagedAgentsSessionActor:`

      - `String sessionId`

      - `Type type`

        - `SESSION_ACTOR("session_actor")`

    - `class BetaManagedAgentsApiActor:`

      - `String apiKeyId`

      - `Type type`

        - `API_ACTOR("api_actor")`

    - `class BetaManagedAgentsUserActor:`

      - `Type type`

        - `USER_ACTOR("user_actor")`

      - `String userId`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memoryversions.BetaManagedAgentsMemoryVersion;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryVersionRetrieveParams params = MemoryVersionRetrieveParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryVersionId("memory_version_id")
            .build();
        BetaManagedAgentsMemoryVersion betaManagedAgentsMemoryVersion = client.beta().memoryStores().memoryVersions().retrieve(params);
    }
}
```

## Redact

`BetaManagedAgentsMemoryVersion beta().memoryStores().memoryVersions().redact(MemoryVersionRedactParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

RedactMemoryVersion

### Parameters

- `MemoryVersionRedactParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryVersionId`

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

### Returns

- `class BetaManagedAgentsMemoryVersion:`

  - `String id`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryId`

  - `String memoryStoreId`

  - `BetaManagedAgentsMemoryVersionOperation operation`

    MemoryVersionOperation enum

    - `CREATED("created")`

    - `MODIFIED("modified")`

    - `DELETED("deleted")`

  - `Type type`

    - `MEMORY_VERSION("memory_version")`

  - `Optional<String> content`

  - `Optional<String> contentSha256`

  - `Optional<Long> contentSizeBytes`

  - `Optional<BetaManagedAgentsActor> createdBy`

    - `class BetaManagedAgentsSessionActor:`

      - `String sessionId`

      - `Type type`

        - `SESSION_ACTOR("session_actor")`

    - `class BetaManagedAgentsApiActor:`

      - `String apiKeyId`

      - `Type type`

        - `API_ACTOR("api_actor")`

    - `class BetaManagedAgentsUserActor:`

      - `Type type`

        - `USER_ACTOR("user_actor")`

      - `String userId`

  - `Optional<String> path`

  - `Optional<LocalDateTime> redactedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsActor> redactedBy`

    - `class BetaManagedAgentsSessionActor:`

      - `String sessionId`

      - `Type type`

        - `SESSION_ACTOR("session_actor")`

    - `class BetaManagedAgentsApiActor:`

      - `String apiKeyId`

      - `Type type`

        - `API_ACTOR("api_actor")`

    - `class BetaManagedAgentsUserActor:`

      - `Type type`

        - `USER_ACTOR("user_actor")`

      - `String userId`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memoryversions.BetaManagedAgentsMemoryVersion;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionRedactParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryVersionRedactParams params = MemoryVersionRedactParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryVersionId("memory_version_id")
            .build();
        BetaManagedAgentsMemoryVersion betaManagedAgentsMemoryVersion = client.beta().memoryStores().memoryVersions().redact(params);
    }
}
```

## Domain Types

### Beta Managed Agents Actor

- `class BetaManagedAgentsActor: A class that can be one of several variants.union`

  - `class BetaManagedAgentsSessionActor:`

    - `String sessionId`

    - `Type type`

      - `SESSION_ACTOR("session_actor")`

  - `class BetaManagedAgentsApiActor:`

    - `String apiKeyId`

    - `Type type`

      - `API_ACTOR("api_actor")`

  - `class BetaManagedAgentsUserActor:`

    - `Type type`

      - `USER_ACTOR("user_actor")`

    - `String userId`

### Beta Managed Agents API Actor

- `class BetaManagedAgentsApiActor:`

  - `String apiKeyId`

  - `Type type`

    - `API_ACTOR("api_actor")`

### Beta Managed Agents Memory Version

- `class BetaManagedAgentsMemoryVersion:`

  - `String id`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String memoryId`

  - `String memoryStoreId`

  - `BetaManagedAgentsMemoryVersionOperation operation`

    MemoryVersionOperation enum

    - `CREATED("created")`

    - `MODIFIED("modified")`

    - `DELETED("deleted")`

  - `Type type`

    - `MEMORY_VERSION("memory_version")`

  - `Optional<String> content`

  - `Optional<String> contentSha256`

  - `Optional<Long> contentSizeBytes`

  - `Optional<BetaManagedAgentsActor> createdBy`

    - `class BetaManagedAgentsSessionActor:`

      - `String sessionId`

      - `Type type`

        - `SESSION_ACTOR("session_actor")`

    - `class BetaManagedAgentsApiActor:`

      - `String apiKeyId`

      - `Type type`

        - `API_ACTOR("api_actor")`

    - `class BetaManagedAgentsUserActor:`

      - `Type type`

        - `USER_ACTOR("user_actor")`

      - `String userId`

  - `Optional<String> path`

  - `Optional<LocalDateTime> redactedAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsActor> redactedBy`

    - `class BetaManagedAgentsSessionActor:`

      - `String sessionId`

      - `Type type`

        - `SESSION_ACTOR("session_actor")`

    - `class BetaManagedAgentsApiActor:`

      - `String apiKeyId`

      - `Type type`

        - `API_ACTOR("api_actor")`

    - `class BetaManagedAgentsUserActor:`

      - `Type type`

        - `USER_ACTOR("user_actor")`

      - `String userId`

### Beta Managed Agents Memory Version Operation

- `enum BetaManagedAgentsMemoryVersionOperation:`

  MemoryVersionOperation enum

  - `CREATED("created")`

  - `MODIFIED("modified")`

  - `DELETED("deleted")`

### Beta Managed Agents Session Actor

- `class BetaManagedAgentsSessionActor:`

  - `String sessionId`

  - `Type type`

    - `SESSION_ACTOR("session_actor")`

### Beta Managed Agents User Actor

- `class BetaManagedAgentsUserActor:`

  - `Type type`

    - `USER_ACTOR("user_actor")`

  - `String userId`

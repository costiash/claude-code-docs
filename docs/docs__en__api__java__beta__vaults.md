# Vaults

## Create

`BetaManagedAgentsVault beta().vaults().create(VaultCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults`

Create Vault

### Parameters

- `VaultCreateParams params`

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

  - `String displayName`

    Human-readable name for the vault. 1-255 characters.

  - `Optional<Metadata> metadata`

    Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

    - `VAULT("vault")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VaultCreateParams params = VaultCreateParams.builder()
            .displayName("Example vault")
            .build();
        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().create(params);
    }
}
```

## List

`VaultListPage beta().vaults().list(VaultListParamsparams = VaultListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/vaults`

List Vaults

### Parameters

- `VaultListParams params`

  - `Optional<Boolean> includeArchived`

    Whether to include archived vaults in the results.

  - `Optional<Long> limit`

    Maximum number of vaults to return per page. Defaults to 20, maximum 100.

  - `Optional<String> page`

    Opaque pagination token from a previous `list_vaults` response.

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

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

    - `VAULT("vault")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.VaultListPage;
import com.anthropic.models.beta.vaults.VaultListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VaultListPage page = client.beta().vaults().list();
    }
}
```

## Retrieve

`BetaManagedAgentsVault beta().vaults().retrieve(VaultRetrieveParamsparams = VaultRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/vaults/{vault_id}`

Get Vault

### Parameters

- `VaultRetrieveParams params`

  - `Optional<String> vaultId`

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

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

    - `VAULT("vault")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().retrieve("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
```

## Update

`BetaManagedAgentsVault beta().vaults().update(VaultUpdateParamsparams = VaultUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `VaultUpdateParams params`

  - `Optional<String> vaultId`

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

  - `Optional<String> displayName`

    Updated human-readable name for the vault. 1-255 characters.

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

    - `VAULT("vault")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().update("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
```

## Delete

`BetaManagedAgentsDeletedVault beta().vaults().delete(VaultDeleteParamsparams = VaultDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/vaults/{vault_id}`

Delete Vault

### Parameters

- `VaultDeleteParams params`

  - `Optional<String> vaultId`

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

### Returns

- `class BetaManagedAgentsDeletedVault:`

  Confirmation of a deleted vault.

  - `String id`

    Unique identifier of the deleted vault.

  - `Type type`

    - `VAULT_DELETED("vault_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsDeletedVault;
import com.anthropic.models.beta.vaults.VaultDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeletedVault betaManagedAgentsDeletedVault = client.beta().vaults().delete("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
```

## Archive

`BetaManagedAgentsVault beta().vaults().archive(VaultArchiveParamsparams = VaultArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Parameters

- `VaultArchiveParams params`

  - `Optional<String> vaultId`

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

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

    - `VAULT("vault")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().archive("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
```

## Domain Types

### Beta Managed Agents Deleted Vault

- `class BetaManagedAgentsDeletedVault:`

  Confirmation of a deleted vault.

  - `String id`

    Unique identifier of the deleted vault.

  - `Type type`

    - `VAULT_DELETED("vault_deleted")`

### Beta Managed Agents Vault

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

    - `VAULT("vault")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

# Credentials

## Create

`BetaManagedAgentsCredential beta().vaults().credentials().create(CredentialCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Parameters

- `CredentialCreateParams params`

  - `Optional<String> vaultId`

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

  - `Auth auth`

    Authentication details for creating a credential.

    - `class BetaManagedAgentsMcpOAuthCreateParams:`

      Parameters for creating an MCP OAuth credential.

      - `String accessToken`

        OAuth access token.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshParams> refresh`

        OAuth refresh token parameters for creating a credential with refresh support.

        - `String clientId`

          OAuth client ID.

        - `String refreshToken`

          OAuth refresh token.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `String clientSecret`

              OAuth client secret.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

            Token endpoint uses POST body authentication with client credentials.

            - `String clientSecret`

              OAuth client secret.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerCreateParams:`

      Parameters for creating a static bearer token credential.

      - `String token`

        Static bearer token value.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

  - `Optional<String> displayName`

    Human-readable name for the credential. Up to 255 characters.

  - `Optional<Metadata> metadata`

    Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

    - `VAULT_CREDENTIAL("vault_credential")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsStaticBearerCreateParams;
import com.anthropic.models.beta.vaults.credentials.CredentialCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialCreateParams params = CredentialCreateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .auth(BetaManagedAgentsStaticBearerCreateParams.builder()
                .token("bearer_exampletoken")
                .mcpServerUrl("https://example-server.modelcontextprotocol.io/sse")
                .type(BetaManagedAgentsStaticBearerCreateParams.Type.STATIC_BEARER)
                .build())
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().create(params);
    }
}
```

## List

`CredentialListPage beta().vaults().credentials().list(CredentialListParamsparams = CredentialListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `CredentialListParams params`

  - `Optional<String> vaultId`

  - `Optional<Boolean> includeArchived`

    Whether to include archived credentials in the results.

  - `Optional<Long> limit`

    Maximum number of credentials to return per page. Defaults to 20, maximum 100.

  - `Optional<String> page`

    Opaque pagination token from a previous `list_credentials` response.

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

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

    - `VAULT_CREDENTIAL("vault_credential")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.CredentialListPage;
import com.anthropic.models.beta.vaults.credentials.CredentialListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialListPage page = client.beta().vaults().credentials().list("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
```

## Retrieve

`BetaManagedAgentsCredential beta().vaults().credentials().retrieve(CredentialRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Parameters

- `CredentialRetrieveParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

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

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

    - `VAULT_CREDENTIAL("vault_credential")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialRetrieveParams params = CredentialRetrieveParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().retrieve(params);
    }
}
```

## Update

`BetaManagedAgentsCredential beta().vaults().credentials().update(CredentialUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `CredentialUpdateParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

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

  - `Optional<Auth> auth`

    Updated authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthUpdateParams:`

      Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<String> accessToken`

        Updated OAuth access token.

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshUpdateParams> refresh`

        Parameters for updating OAuth refresh token configuration.

        - `Optional<String> refreshToken`

          Updated OAuth refresh token.

        - `Optional<String> scope`

          Updated OAuth scope for the refresh request.

        - `Optional<TokenEndpointAuth> tokenEndpointAuth`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

            - `Optional<String> clientSecret`

              Updated OAuth client secret.

          - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

            Updated POST body authentication parameters for the token endpoint.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

            - `Optional<String> clientSecret`

              Updated OAuth client secret.

    - `class BetaManagedAgentsStaticBearerUpdateParams:`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

      - `Optional<String> token`

        Updated static bearer token value.

  - `Optional<String> displayName`

    Updated human-readable name for the credential. 1-255 characters.

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

    - `VAULT_CREDENTIAL("vault_credential")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialUpdateParams params = CredentialUpdateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().update(params);
    }
}
```

## Delete

`BetaManagedAgentsDeletedCredential beta().vaults().credentials().delete(CredentialDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `CredentialDeleteParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

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

### Returns

- `class BetaManagedAgentsDeletedCredential:`

  Confirmation of a deleted credential.

  - `String id`

    Unique identifier of the deleted credential.

  - `Type type`

    - `VAULT_CREDENTIAL_DELETED("vault_credential_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsDeletedCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialDeleteParams params = CredentialDeleteParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsDeletedCredential betaManagedAgentsDeletedCredential = client.beta().vaults().credentials().delete(params);
    }
}
```

## Archive

`BetaManagedAgentsCredential beta().vaults().credentials().archive(CredentialArchiveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `CredentialArchiveParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

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

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

    - `VAULT_CREDENTIAL("vault_credential")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialArchiveParams params = CredentialArchiveParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().archive(params);
    }
}
```

## MCP OAuth Validate

`BetaManagedAgentsCredentialValidation beta().vaults().credentials().mcpOAuthValidate(CredentialMcpOAuthValidateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Parameters

- `CredentialMcpOAuthValidateParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

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

### Returns

- `class BetaManagedAgentsCredentialValidation:`

  Result of live-probing a credential against its configured MCP server.

  - `String credentialId`

    Unique identifier of the credential that was validated.

  - `boolean hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `Optional<BetaManagedAgentsMcpProbe> mcpProbe`

    The failing step of an MCP validation probe.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      An HTTP response captured during a credential validation probe.

      - `String body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `boolean bodyTruncated`

        Whether `body` was truncated.

      - `String contentType`

        Value of the `Content-Type` response header.

      - `long statusCode`

        HTTP status code.

    - `String method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `Optional<BetaManagedAgentsRefreshObject> refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      An HTTP response captured during a credential validation probe.

      - `String body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `boolean bodyTruncated`

        Whether `body` was truncated.

      - `String contentType`

        Value of the `Content-Type` response header.

      - `long statusCode`

        HTTP status code.

    - `Status status`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `SUCCEEDED("succeeded")`

      - `FAILED("failed")`

      - `CONNECT_ERROR("connect_error")`

      - `NO_REFRESH_TOKEN("no_refresh_token")`

  - `BetaManagedAgentsCredentialValidationStatus status`

    Overall verdict of a credential validation probe.

    - `VALID("valid")`

    - `INVALID("invalid")`

    - `UNKNOWN("unknown")`

  - `Type type`

    - `VAULT_CREDENTIAL_VALIDATION("vault_credential_validation")`

  - `LocalDateTime validatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault containing the credential.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredentialValidation;
import com.anthropic.models.beta.vaults.credentials.CredentialMcpOAuthValidateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialMcpOAuthValidateParams params = CredentialMcpOAuthValidateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredentialValidation betaManagedAgentsCredentialValidation = client.beta().vaults().credentials().mcpOAuthValidate(params);
    }
}
```

## Domain Types

### Beta Managed Agents Credential

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `MCP_OAUTH("mcp_oauth")`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

              - `NONE("none")`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

              - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

        - `STATIC_BEARER("static_bearer")`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

    - `VAULT_CREDENTIAL("vault_credential")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

### Beta Managed Agents Credential Validation

- `class BetaManagedAgentsCredentialValidation:`

  Result of live-probing a credential against its configured MCP server.

  - `String credentialId`

    Unique identifier of the credential that was validated.

  - `boolean hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `Optional<BetaManagedAgentsMcpProbe> mcpProbe`

    The failing step of an MCP validation probe.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      An HTTP response captured during a credential validation probe.

      - `String body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `boolean bodyTruncated`

        Whether `body` was truncated.

      - `String contentType`

        Value of the `Content-Type` response header.

      - `long statusCode`

        HTTP status code.

    - `String method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `Optional<BetaManagedAgentsRefreshObject> refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      An HTTP response captured during a credential validation probe.

      - `String body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `boolean bodyTruncated`

        Whether `body` was truncated.

      - `String contentType`

        Value of the `Content-Type` response header.

      - `long statusCode`

        HTTP status code.

    - `Status status`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `SUCCEEDED("succeeded")`

      - `FAILED("failed")`

      - `CONNECT_ERROR("connect_error")`

      - `NO_REFRESH_TOKEN("no_refresh_token")`

  - `BetaManagedAgentsCredentialValidationStatus status`

    Overall verdict of a credential validation probe.

    - `VALID("valid")`

    - `INVALID("invalid")`

    - `UNKNOWN("unknown")`

  - `Type type`

    - `VAULT_CREDENTIAL_VALIDATION("vault_credential_validation")`

  - `LocalDateTime validatedAt`

    A timestamp in RFC 3339 format

  - `String vaultId`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `enum BetaManagedAgentsCredentialValidationStatus:`

  Overall verdict of a credential validation probe.

  - `VALID("valid")`

  - `INVALID("invalid")`

  - `UNKNOWN("unknown")`

### Beta Managed Agents Deleted Credential

- `class BetaManagedAgentsDeletedCredential:`

  Confirmation of a deleted credential.

  - `String id`

    Unique identifier of the deleted credential.

  - `Type type`

    - `VAULT_CREDENTIAL_DELETED("vault_credential_deleted")`

### Beta Managed Agents MCP OAuth Auth Response

- `class BetaManagedAgentsMcpOAuthAuthResponse:`

  OAuth credential details for an MCP server.

  - `String mcpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `Type type`

    - `MCP_OAUTH("mcp_oauth")`

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

    OAuth refresh token configuration returned in credential responses.

    - `String clientId`

      OAuth client ID.

    - `String tokenEndpoint`

      Token endpoint URL used to refresh the access token.

    - `TokenEndpointAuth tokenEndpointAuth`

      Token endpoint requires no client authentication.

      - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

        Token endpoint requires no client authentication.

        - `Type type`

          - `NONE("none")`

      - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `Type type`

          - `CLIENT_SECRET_BASIC("client_secret_basic")`

      - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

        Token endpoint uses POST body authentication with client credentials.

        - `Type type`

          - `CLIENT_SECRET_POST("client_secret_post")`

    - `Optional<String> resource`

      OAuth resource indicator.

    - `Optional<String> scope`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Create Params

- `class BetaManagedAgentsMcpOAuthCreateParams:`

  Parameters for creating an MCP OAuth credential.

  - `String accessToken`

    OAuth access token.

  - `String mcpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `Type type`

    - `MCP_OAUTH("mcp_oauth")`

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsMcpOAuthRefreshParams> refresh`

    OAuth refresh token parameters for creating a credential with refresh support.

    - `String clientId`

      OAuth client ID.

    - `String refreshToken`

      OAuth refresh token.

    - `String tokenEndpoint`

      Token endpoint URL used to refresh the access token.

    - `TokenEndpointAuth tokenEndpointAuth`

      Token endpoint requires no client authentication.

      - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

        Token endpoint requires no client authentication.

        - `Type type`

          - `NONE("none")`

      - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `String clientSecret`

          OAuth client secret.

        - `Type type`

          - `CLIENT_SECRET_BASIC("client_secret_basic")`

      - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

        Token endpoint uses POST body authentication with client credentials.

        - `String clientSecret`

          OAuth client secret.

        - `Type type`

          - `CLIENT_SECRET_POST("client_secret_post")`

    - `Optional<String> resource`

      OAuth resource indicator.

    - `Optional<String> scope`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Params

- `class BetaManagedAgentsMcpOAuthRefreshParams:`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `String clientId`

    OAuth client ID.

  - `String refreshToken`

    OAuth refresh token.

  - `String tokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth tokenEndpointAuth`

    Token endpoint requires no client authentication.

    - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

      Token endpoint requires no client authentication.

      - `Type type`

        - `NONE("none")`

    - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `String clientSecret`

        OAuth client secret.

      - `Type type`

        - `CLIENT_SECRET_BASIC("client_secret_basic")`

    - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

      Token endpoint uses POST body authentication with client credentials.

      - `String clientSecret`

        OAuth client secret.

      - `Type type`

        - `CLIENT_SECRET_POST("client_secret_post")`

  - `Optional<String> resource`

    OAuth resource indicator.

  - `Optional<String> scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `class BetaManagedAgentsMcpOAuthRefreshResponse:`

  OAuth refresh token configuration returned in credential responses.

  - `String clientId`

    OAuth client ID.

  - `String tokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth tokenEndpointAuth`

    Token endpoint requires no client authentication.

    - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

      Token endpoint requires no client authentication.

      - `Type type`

        - `NONE("none")`

    - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `Type type`

        - `CLIENT_SECRET_BASIC("client_secret_basic")`

    - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

      Token endpoint uses POST body authentication with client credentials.

      - `Type type`

        - `CLIENT_SECRET_POST("client_secret_post")`

  - `Optional<String> resource`

    OAuth resource indicator.

  - `Optional<String> scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `class BetaManagedAgentsMcpOAuthRefreshUpdateParams:`

  Parameters for updating OAuth refresh token configuration.

  - `Optional<String> refreshToken`

    Updated OAuth refresh token.

  - `Optional<String> scope`

    Updated OAuth scope for the refresh request.

  - `Optional<TokenEndpointAuth> tokenEndpointAuth`

    Updated HTTP Basic authentication parameters for the token endpoint.

    - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `Type type`

        - `CLIENT_SECRET_BASIC("client_secret_basic")`

      - `Optional<String> clientSecret`

        Updated OAuth client secret.

    - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

      Updated POST body authentication parameters for the token endpoint.

      - `Type type`

        - `CLIENT_SECRET_POST("client_secret_post")`

      - `Optional<String> clientSecret`

        Updated OAuth client secret.

### Beta Managed Agents MCP OAuth Update Params

- `class BetaManagedAgentsMcpOAuthUpdateParams:`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `Type type`

    - `MCP_OAUTH("mcp_oauth")`

  - `Optional<String> accessToken`

    Updated OAuth access token.

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

  - `Optional<BetaManagedAgentsMcpOAuthRefreshUpdateParams> refresh`

    Parameters for updating OAuth refresh token configuration.

    - `Optional<String> refreshToken`

      Updated OAuth refresh token.

    - `Optional<String> scope`

      Updated OAuth scope for the refresh request.

    - `Optional<TokenEndpointAuth> tokenEndpointAuth`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `Type type`

          - `CLIENT_SECRET_BASIC("client_secret_basic")`

        - `Optional<String> clientSecret`

          Updated OAuth client secret.

      - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

        Updated POST body authentication parameters for the token endpoint.

        - `Type type`

          - `CLIENT_SECRET_POST("client_secret_post")`

        - `Optional<String> clientSecret`

          Updated OAuth client secret.

### Beta Managed Agents MCP Probe

- `class BetaManagedAgentsMcpProbe:`

  The failing step of an MCP validation probe.

  - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

    An HTTP response captured during a credential validation probe.

    - `String body`

      Response body. May be truncated and has sensitive values scrubbed.

    - `boolean bodyTruncated`

      Whether `body` was truncated.

    - `String contentType`

      Value of the `Content-Type` response header.

    - `long statusCode`

      HTTP status code.

  - `String method`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `class BetaManagedAgentsRefreshHttpResponse:`

  An HTTP response captured during a credential validation probe.

  - `String body`

    Response body. May be truncated and has sensitive values scrubbed.

  - `boolean bodyTruncated`

    Whether `body` was truncated.

  - `String contentType`

    Value of the `Content-Type` response header.

  - `long statusCode`

    HTTP status code.

### Beta Managed Agents Refresh Object

- `class BetaManagedAgentsRefreshObject:`

  Outcome of a refresh-token exchange attempted during credential validation.

  - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

    An HTTP response captured during a credential validation probe.

    - `String body`

      Response body. May be truncated and has sensitive values scrubbed.

    - `boolean bodyTruncated`

      Whether `body` was truncated.

    - `String contentType`

      Value of the `Content-Type` response header.

    - `long statusCode`

      HTTP status code.

  - `Status status`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `SUCCEEDED("succeeded")`

    - `FAILED("failed")`

    - `CONNECT_ERROR("connect_error")`

    - `NO_REFRESH_TOKEN("no_refresh_token")`

### Beta Managed Agents Static Bearer Auth Response

- `class BetaManagedAgentsStaticBearerAuthResponse:`

  Static bearer token credential details for an MCP server.

  - `String mcpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `Type type`

    - `STATIC_BEARER("static_bearer")`

### Beta Managed Agents Static Bearer Create Params

- `class BetaManagedAgentsStaticBearerCreateParams:`

  Parameters for creating a static bearer token credential.

  - `String token`

    Static bearer token value.

  - `String mcpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `Type type`

    - `STATIC_BEARER("static_bearer")`

### Beta Managed Agents Static Bearer Update Params

- `class BetaManagedAgentsStaticBearerUpdateParams:`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `Type type`

    - `STATIC_BEARER("static_bearer")`

  - `Optional<String> token`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `String clientSecret`

    OAuth client secret.

  - `Type type`

    - `CLIENT_SECRET_BASIC("client_secret_basic")`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `Type type`

    - `CLIENT_SECRET_BASIC("client_secret_basic")`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `Type type`

    - `CLIENT_SECRET_BASIC("client_secret_basic")`

  - `Optional<String> clientSecret`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

  Token endpoint requires no client authentication.

  - `Type type`

    - `NONE("none")`

### Beta Managed Agents Token Endpoint Auth None Response

- `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

  Token endpoint requires no client authentication.

  - `Type type`

    - `NONE("none")`

### Beta Managed Agents Token Endpoint Auth Post Param

- `class BetaManagedAgentsTokenEndpointAuthPostParam:`

  Token endpoint uses POST body authentication with client credentials.

  - `String clientSecret`

    OAuth client secret.

  - `Type type`

    - `CLIENT_SECRET_POST("client_secret_post")`

### Beta Managed Agents Token Endpoint Auth Post Response

- `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

  Token endpoint uses POST body authentication with client credentials.

  - `Type type`

    - `CLIENT_SECRET_POST("client_secret_post")`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

  Updated POST body authentication parameters for the token endpoint.

  - `Type type`

    - `CLIENT_SECRET_POST("client_secret_post")`

  - `Optional<String> clientSecret`

    Updated OAuth client secret.

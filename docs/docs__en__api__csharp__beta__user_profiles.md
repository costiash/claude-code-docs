# User Profiles

## Create

`BetaUserProfile Beta.UserProfiles.Create(UserProfileCreateParams?parameters, CancellationTokencancellationToken = default)`

**post** `/v1/user_profiles`

Create User Profile

### Parameters

- `UserProfileCreateParams parameters`

  - `string? externalID`

    Body param

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

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

### Returns

- `class BetaUserProfile:`

  - `required string ID`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    - `required string Status`

  - `required string Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? ExternalID`

### Example

```csharp
UserProfileCreateParams parameters = new();

var betaUserProfile = await client.Beta.UserProfiles.Create(parameters);

Console.WriteLine(betaUserProfile);
```

## List

`UserProfileListPageResponse Beta.UserProfiles.List(UserProfileListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/user_profiles`

List User Profiles

### Parameters

- `UserProfileListParams parameters`

  - `Int limit`

    Query param: Query parameter for limit

  - `Order order`

    Query param: Query parameter for order

    - `"asc"Asc`

    - `"desc"Desc`

  - `string page`

    Query param: Query parameter for page

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

### Returns

- `class UserProfileListPageResponse:`

  - `required IReadOnlyList<BetaUserProfile> Data`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required IReadOnlyDictionary<string, string> Metadata`

    - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

      - `required string Status`

    - `required string Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

    - `string? ExternalID`

  - `string? NextPage`

### Example

```csharp
UserProfileListParams parameters = new();

var page = await client.Beta.UserProfiles.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

## Retrieve

`BetaUserProfile Beta.UserProfiles.Retrieve(UserProfileRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/user_profiles/{id}`

Get User Profile

### Parameters

- `UserProfileRetrieveParams parameters`

  - `required string id`

    Path parameter id

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

### Returns

- `class BetaUserProfile:`

  - `required string ID`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    - `required string Status`

  - `required string Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? ExternalID`

### Example

```csharp
UserProfileRetrieveParams parameters = new() { ID = "id" };

var betaUserProfile = await client.Beta.UserProfiles.Retrieve(parameters);

Console.WriteLine(betaUserProfile);
```

## Update

`BetaUserProfile Beta.UserProfiles.Update(UserProfileUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/user_profiles/{id}`

Update User Profile

### Parameters

- `UserProfileUpdateParams parameters`

  - `required string id`

    Path param: Path parameter id

  - `string? externalID`

    Body param

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

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

### Returns

- `class BetaUserProfile:`

  - `required string ID`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    - `required string Status`

  - `required string Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? ExternalID`

### Example

```csharp
UserProfileUpdateParams parameters = new() { ID = "id" };

var betaUserProfile = await client.Beta.UserProfiles.Update(parameters);

Console.WriteLine(betaUserProfile);
```

## Create Enrollment URL

`BetaUserProfileEnrollmentUrl Beta.UserProfiles.CreateEnrollmentUrl(UserProfileCreateEnrollmentUrlParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/user_profiles/{id}/enrollment_url`

Create Enrollment URL

### Parameters

- `UserProfileCreateEnrollmentUrlParams parameters`

  - `required string id`

    Path parameter id

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

### Returns

- `class BetaUserProfileEnrollmentUrl:`

  - `required DateTimeOffset ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Type`

  - `required string Url`

### Example

```csharp
UserProfileCreateEnrollmentUrlParams parameters = new() { ID = "id" };

var betaUserProfileEnrollmentUrl = await client.Beta.UserProfiles.CreateEnrollmentUrl(parameters);

Console.WriteLine(betaUserProfileEnrollmentUrl);
```

## Domain Types

### Beta User Profile

- `class BetaUserProfile:`

  - `required string ID`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    - `required string Status`

  - `required string Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? ExternalID`

### Beta User Profile Enrollment URL

- `class BetaUserProfileEnrollmentUrl:`

  - `required DateTimeOffset ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Type`

  - `required string Url`

### Beta User Profile Trust Grant

- `class BetaUserProfileTrustGrant:`

  - `required string Status`

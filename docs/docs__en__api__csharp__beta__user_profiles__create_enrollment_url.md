## Create Enrollment URL

`BetaUserProfileEnrollmentUrl Beta.UserProfiles.CreateEnrollmentUrl(UserProfileCreateEnrollmentUrlParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `UserProfileCreateEnrollmentUrlParams parameters`

  - `required string userProfileID`

    Path parameter user_profile_id

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

- `class BetaUserProfileEnrollmentUrl:`

  - `required DateTimeOffset ExpiresAt`

    A timestamp in RFC 3339 format

  - `required Type Type`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"EnrollmentUrl`

  - `required string Url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```csharp
UserProfileCreateEnrollmentUrlParams parameters = new()
{
    UserProfileID = "uprof_011CZkZCu8hGbp5mYRQgUmz9"
};

var betaUserProfileEnrollmentUrl = await client.Beta.UserProfiles.CreateEnrollmentUrl(parameters);

Console.WriteLine(betaUserProfileEnrollmentUrl);
```

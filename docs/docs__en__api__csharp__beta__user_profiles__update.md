## Update

`BetaUserProfile Beta.UserProfiles.Update(UserProfileUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `UserProfileUpdateParams parameters`

  - `required string userProfileID`

    Path param: Path parameter user_profile_id

  - `string? externalID`

    Body param: If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

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

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

### Returns

- `class BetaUserProfile:`

  - `required string ID`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `required Status Status`

      Status of the trust grant.

      - `"active"Active`

      - `"pending"Pending`

      - `"rejected"Rejected`

  - `required Type Type`

    Object type. Always `user_profile`.

    - `"user_profile"UserProfile`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `string? ExternalID`

    Platform's own identifier for this user. Not enforced unique.

### Example

```csharp
UserProfileUpdateParams parameters = new()
{
    UserProfileID = "uprof_011CZkZCu8hGbp5mYRQgUmz9"
};

var betaUserProfile = await client.Beta.UserProfiles.Update(parameters);

Console.WriteLine(betaUserProfile);
```

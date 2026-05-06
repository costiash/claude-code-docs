## Update

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Update(CredentialUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `CredentialUpdateParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

  - `Auth auth`

    Body param: Updated authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthUpdateParams:`

      Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

      - `required Type Type`

        - `"mcp_oauth"McpOAuth`

      - `string? AccessToken`

        Updated OAuth access token.

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

      - `BetaManagedAgentsMcpOAuthRefreshUpdateParams? Refresh`

        Parameters for updating OAuth refresh token configuration.

        - `string? RefreshToken`

          Updated OAuth refresh token.

        - `string? Scope`

          Updated OAuth scope for the refresh request.

        - `TokenEndpointAuth TokenEndpointAuth`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `required Type Type`

              - `"client_secret_basic"ClientSecretBasic`

            - `string? ClientSecret`

              Updated OAuth client secret.

          - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

            Updated POST body authentication parameters for the token endpoint.

            - `required Type Type`

              - `"client_secret_post"ClientSecretPost`

            - `string? ClientSecret`

              Updated OAuth client secret.

    - `class BetaManagedAgentsStaticBearerUpdateParams:`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `required Type Type`

        - `"static_bearer"StaticBearer`

      - `string? Token`

        Updated static bearer token value.

  - `string? displayName`

    Body param: Updated human-readable name for the credential. 1-255 characters.

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

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

### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `required string ID`

    Unique identifier for the credential.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required Auth Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"mcp_oauth"McpOAuth`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

      - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

        OAuth refresh token configuration returned in credential responses.

        - `required string ClientID`

          OAuth client ID.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `required Type Type`

              - `"none"None`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required Type Type`

              - `"client_secret_basic"ClientSecretBasic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `required Type Type`

              - `"client_secret_post"ClientSecretPost`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

        - `"static_bearer"StaticBearer`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required Type Type`

    - `"vault_credential"VaultCredential`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

### Example

```csharp
CredentialUpdateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Update(parameters);

Console.WriteLine(betaManagedAgentsCredential);
```

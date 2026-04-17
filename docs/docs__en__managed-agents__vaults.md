# Authenticate with vaults

Register per-user credentials when creating sessions.

---

Vaults and credentials are authentication primitives that let you register credentials for third-party services once and reference them by ID at session creation. This means you don't need to run your own secret store, transmit tokens on every call, or lose track of which end user an agent acted on behalf of.

The vault reference is a per-session parameter, so you can manage your product at the agent level and your users at the session level.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
</Note>

## Create a vault

<Warning>
Vaults and credentials are workspace-scoped, meaning anyone with API key access can use them for authorizing an agent to complete a task. To revoke access, delete the vault or credential.
</Warning>

A vault is the collection of `credentials` associated with an end-user. Give it a `display_name` and optionally tag it with `metadata` so you can map it back to your own user records.

<CodeGroup defaultLanguage="CLI">
  
````bash
vault_id=$(curl --fail-with-body -sS https://api.anthropic.com/v1/vaults \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- <<'EOF' | jq -r '.id'
{
  "display_name": "Alice",
  "metadata": {"external_user_id": "usr_abc123"}
}
EOF
)
echo "$vault_id"  # "vlt_01ABC..."
````

  
````bash
VAULT_ID=$(ant beta:vaults create \
  --display-name "Alice" \
  --metadata '{external_user_id: usr_abc123}' \
  --transform id --format yaml)
````

  
````python
vault = client.beta.vaults.create(
    display_name="Alice",
    metadata={"external_user_id": "usr_abc123"},
)
print(vault.id)  # "vlt_01ABC..."
````

  
````typescript
const vault = await client.beta.vaults.create({
  display_name: "Alice",
  metadata: { external_user_id: "usr_abc123" },
});
console.log(vault.id); // "vlt_01ABC..."
````

  
````csharp
var vault = await client.Beta.Vaults.Create(new()
{
    DisplayName = "Alice",
    Metadata = new Dictionary<string, string> { ["external_user_id"] = "usr_abc123" },
});
Console.WriteLine(vault.ID); // "vlt_01ABC..."
````

  
````go
vault, err := client.Beta.Vaults.New(ctx, anthropic.BetaVaultNewParams{
	DisplayName: "Alice",
	Metadata:    map[string]string{"external_user_id": "usr_abc123"},
})
if err != nil {
	panic(err)
}
fmt.Println(vault.ID) // "vlt_01ABC..."
````

  
````java
var vault = client.beta().vaults().create(VaultCreateParams.builder()
    .displayName("Alice")
    .metadata(VaultCreateParams.Metadata.builder()
        .putAdditionalProperty("external_user_id", JsonValue.from("usr_abc123"))
        .build())
    .build());
IO.println(vault.id()); // "vlt_01ABC..."
````

  
````php
$vault = $client->beta->vaults->create(
    displayName: 'Alice',
    metadata: ['external_user_id' => 'usr_abc123'],
);
echo $vault->id . "\n"; // "vlt_01ABC..."
````

  
````ruby
vault = client.beta.vaults.create(
  display_name: "Alice",
  metadata: {external_user_id: "usr_abc123"}
)
puts vault.id # "vlt_01ABC..."
````

</CodeGroup>

The response is the full vault record:

```json
{
  "type": "vault",
  "id": "vlt_01ABC...",
  "display_name": "Alice",
  "metadata": { "external_user_id": "usr_abc123" },
  "created_at": "2026-03-18T10:00:00Z",
  "updated_at": "2026-03-18T10:00:00Z",
  "archived_at": null
}
```

## Add a credential

Each credential binds to a single `mcp_server_url`. When the agent connects to an MCP server at session runtime, the API matches the server URL against active credentials on the referenced vault and injects the token.

<Tabs>
  <Tab title="MCP OAuth credential">

Use `mcp_oauth` when the MCP server uses OAuth 2.0. If you supply a `refresh` block, Anthropic refreshes the access token on your behalf when it expires.

The `refresh.token_endpoint_auth.type` field indicates how to authenticate the refresh call:
- `none`: public client
- `client_secret_basic`: HTTP Basic auth with the client secret
- `client_secret_post`: client secret in the POST body

<CodeGroup defaultLanguage="CLI">
  
````bash
credential_id=$(curl --fail-with-body -sS "https://api.anthropic.com/v1/vaults/$vault_id/credentials" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- <<'EOF' | jq -r '.id'
{
  "display_name": "Alice's Slack",
  "auth": {
    "type": "mcp_oauth",
    "mcp_server_url": "https://mcp.slack.com/mcp",
    "access_token": "xoxp-...",
    "expires_at": "2026-04-15T00:00:00Z",
    "refresh": {
      "token_endpoint": "https://slack.com/api/oauth.v2.access",
      "client_id": "1234567890.0987654321",
      "scope": "channels:read chat:write",
      "refresh_token": "xoxe-1-...",
      "token_endpoint_auth": {"type": "client_secret_post", "client_secret": "abc123..."}
    }
  }
}
EOF
)
````

  
````bash
CREDENTIAL_ID=$(ant beta:vaults:credentials create \
  --vault-id "$VAULT_ID" \
  --display-name "Alice's Slack" \
  --transform id --format yaml <<'EOF'
auth:
  type: mcp_oauth
  mcp_server_url: https://mcp.slack.com/mcp
  access_token: xoxp-...
  expires_at: "2026-04-15T00:00:00Z"
  refresh:
    token_endpoint: https://slack.com/api/oauth.v2.access
    client_id: "1234567890.0987654321"
    scope: channels:read chat:write
    refresh_token: xoxe-1-...
    token_endpoint_auth:
      type: client_secret_post
      client_secret: abc123...
EOF
)
````

  
````python
credential = client.beta.vaults.credentials.create(
    vault_id=vault.id,
    display_name="Alice's Slack",
    auth={
        "type": "mcp_oauth",
        "mcp_server_url": "https://mcp.slack.com/mcp",
        "access_token": "xoxp-...",
        "expires_at": "2026-04-15T00:00:00Z",
        "refresh": {
            "token_endpoint": "https://slack.com/api/oauth.v2.access",
            "client_id": "1234567890.0987654321",
            "scope": "channels:read chat:write",
            "refresh_token": "xoxe-1-...",
            "token_endpoint_auth": {"type": "client_secret_post", "client_secret": "abc123..."},
        },
    },
)
````

  
````typescript
const credential = await client.beta.vaults.credentials.create(vault.id, {
  display_name: "Alice's Slack",
  auth: {
    type: "mcp_oauth",
    mcp_server_url: "https://mcp.slack.com/mcp",
    access_token: "xoxp-...",
    expires_at: "2026-04-15T00:00:00Z",
    refresh: {
      token_endpoint: "https://slack.com/api/oauth.v2.access",
      client_id: "1234567890.0987654321",
      scope: "channels:read chat:write",
      refresh_token: "xoxe-1-...",
      token_endpoint_auth: {
        type: "client_secret_post",
        client_secret: "abc123...",
      },
    },
  },
});
````

  
````csharp
var credential = await client.Beta.Vaults.Credentials.Create(vault.ID, new()
{
    DisplayName = "Alice's Slack",
    Auth = new BetaManagedAgentsMcpOAuthCreateParams
    {
        Type = "mcp_oauth",
        McpServerUrl = "https://mcp.slack.com/mcp",
        AccessToken = "xoxp-...",
        ExpiresAt = DateTimeOffset.Parse("2026-04-15T00:00:00Z"),
        Refresh = new()
        {
            TokenEndpoint = "https://slack.com/api/oauth.v2.access",
            ClientID = "1234567890.0987654321",
            Scope = "channels:read chat:write",
            RefreshToken = "xoxe-1-...",
            TokenEndpointAuth = new BetaManagedAgentsTokenEndpointAuthPostParam
            {
                Type = "client_secret_post",
                ClientSecret = "abc123...",
            },
        },
    },
});
````

  
````go
credential, err := client.Beta.Vaults.Credentials.New(ctx, vault.ID, anthropic.BetaVaultCredentialNewParams{
	DisplayName: anthropic.String("Alice's Slack"),
	Auth: anthropic.BetaVaultCredentialNewParamsAuthUnion{
		OfMCPOAuth: &anthropic.BetaManagedAgentsMCPOAuthCreateParams{
			Type:         anthropic.BetaManagedAgentsMCPOAuthCreateParamsTypeMCPOAuth,
			MCPServerURL: "https://mcp.slack.com/mcp",
			AccessToken:  "xoxp-...",
			ExpiresAt:    anthropic.Time(time.Date(2026, time.April, 15, 0, 0, 0, 0, time.UTC)),
			Refresh: anthropic.BetaManagedAgentsMCPOAuthRefreshParams{
				TokenEndpoint: "https://slack.com/api/oauth.v2.access",
				ClientID:      "1234567890.0987654321",
				Scope:         anthropic.String("channels:read chat:write"),
				RefreshToken:  "xoxe-1-...",
				TokenEndpointAuth: anthropic.BetaManagedAgentsMCPOAuthRefreshParamsTokenEndpointAuthUnion{
					OfClientSecretPost: &anthropic.BetaManagedAgentsTokenEndpointAuthPostParam{
						Type:         anthropic.BetaManagedAgentsTokenEndpointAuthPostParamTypeClientSecretPost,
						ClientSecret: "abc123...",
					},
				},
			},
		},
	},
})
if err != nil {
	panic(err)
}
````

  
````java
var credential = client.beta().vaults().credentials().create(vault.id(),
    CredentialCreateParams.builder()
        .displayName("Alice's Slack")
        .auth(BetaManagedAgentsMcpOAuthCreateParams.builder()
            .type(BetaManagedAgentsMcpOAuthCreateParams.Type.MCP_OAUTH)
            .mcpServerUrl("https://mcp.slack.com/mcp")
            .accessToken("xoxp-...")
            .expiresAt(OffsetDateTime.parse("2026-04-15T00:00:00Z"))
            .refresh(BetaManagedAgentsMcpOAuthRefreshParams.builder()
                .tokenEndpoint("https://slack.com/api/oauth.v2.access")
                .clientId("1234567890.0987654321")
                .scope("channels:read chat:write")
                .refreshToken("xoxe-1-...")
                .clientSecretPostTokenEndpointAuth("abc123...")
                .build())
            .build())
        .build());
````

  
````php
$credential = $client->beta->vaults->credentials->create(
    vaultID: $vault->id,
    displayName: "Alice's Slack",
    auth: [
        'type' => 'mcp_oauth',
        'mcp_server_url' => 'https://mcp.slack.com/mcp',
        'access_token' => 'xoxp-...',
        'expires_at' => '2026-04-15T00:00:00Z',
        'refresh' => [
            'token_endpoint' => 'https://slack.com/api/oauth.v2.access',
            'client_id' => '1234567890.0987654321',
            'scope' => 'channels:read chat:write',
            'refresh_token' => 'xoxe-1-...',
            'token_endpoint_auth' => [
                'type' => 'client_secret_post',
                'client_secret' => 'abc123...',
            ],
        ],
    ],
);
````

  
````ruby
credential = client.beta.vaults.credentials.create(
  vault.id,
  display_name: "Alice's Slack",
  auth: {
    type: "mcp_oauth",
    mcp_server_url: "https://mcp.slack.com/mcp",
    access_token: "xoxp-...",
    expires_at: "2026-04-15T00:00:00Z",
    refresh: {
      token_endpoint: "https://slack.com/api/oauth.v2.access",
      client_id: "1234567890.0987654321",
      scope: "channels:read chat:write",
      refresh_token: "xoxe-1-...",
      token_endpoint_auth: {
        type: "client_secret_post",
        client_secret: "abc123..."
      }
    }
  }
)
````

</CodeGroup>

  </Tab>
  <Tab title="Static bearer credential">

Use `static_bearer` when the MCP server accepts a fixed bearer token (API key, personal access token, or similar). No refresh flow is needed.

<CodeGroup defaultLanguage="CLI">
```bash curl
curl -fsSL "https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d '{
    "display_name": "Linear API key",
    "auth": {
      "type": "static_bearer",
      "mcp_server_url": "https://mcp.linear.app/mcp",
      "token": "lin_api_your_linear_key"
    }
  }'
```

```bash CLI nocheck
ant beta:vaults:credentials create --vault-id "$VAULT_ID" <<'YAML'
display_name: Linear API key
auth:
  type: static_bearer
  mcp_server_url: https://mcp.linear.app/mcp
  token: lin_api_your_linear_key
YAML
```

```python Python
credential = client.beta.vaults.credentials.create(
    vault_id=vault.id,
    display_name="Linear API key",
    auth={
        "type": "static_bearer",
        "mcp_server_url": "https://mcp.linear.app/mcp",
        "token": "lin_api_your_linear_key",
    },
)
```

```typescript TypeScript
const credential = await client.beta.vaults.credentials.create(vault.id, {
  display_name: "Linear API key",
  auth: {
    type: "static_bearer",
    mcp_server_url: "https://mcp.linear.app/mcp",
    token: "lin_api_your_linear_key"
  }
});
```

```csharp C#
var credential = await client.Beta.Vaults.Credentials.Create(vault.ID, new()
{
    DisplayName = "Linear API key",
    Auth = new BetaManagedAgentsStaticBearerCreateParams
    {
        Type = "static_bearer",
        McpServerUrl = "https://mcp.linear.app/mcp",
        Token = "lin_api_your_linear_key",
    },
});
```

```go Go
credential, err := client.Beta.Vaults.Credentials.New(ctx, vault.ID, anthropic.BetaVaultCredentialNewParams{
	DisplayName: anthropic.String("Linear API key"),
	Auth: anthropic.BetaVaultCredentialNewParamsAuthUnion{
		OfStaticBearer: &anthropic.BetaManagedAgentsStaticBearerCreateParams{
			Type:         anthropic.BetaManagedAgentsStaticBearerCreateParamsTypeStaticBearer,
			MCPServerURL: "https://mcp.linear.app/mcp",
			Token:        "lin_api_your_linear_key",
		},
	},
})
if err != nil {
	panic(err)
}
```

```java Java
var credential = client.beta().vaults().credentials().create(vault.id(),
    CredentialCreateParams.builder()
        .displayName("Linear API key")
        .auth(BetaManagedAgentsStaticBearerCreateParams.builder()
            .type(BetaManagedAgentsStaticBearerCreateParams.Type.STATIC_BEARER)
            .mcpServerUrl("https://mcp.linear.app/mcp")
            .token("lin_api_your_linear_key")
            .build())
        .build());
```

```php PHP
$credential = $client->beta->vaults->credentials->create(
    vaultID: $vault->id,
    displayName: 'Notion token',
    auth: [
        'type' => 'static_bearer',
        'mcp_server_url' => 'https://mcp.linear.app/mcp',
        'token' => 'lin_api_your_linear_key',
    ],
);
```

```ruby Ruby
credential = client.beta.vaults.credentials.create(
  vault.id,
  display_name: "Linear API key",
  auth: {
    type: "static_bearer",
    mcp_server_url: "https://mcp.linear.app/mcp",
    token: "lin_api_your_linear_key"
  }
)
```
</CodeGroup>

  </Tab>
</Tabs>

<Warning>
Secret fields (`token`, `access_token`, `refresh_token`, `client_secret`) are write-only. They are never returned in API responses.
</Warning>

Credentials are stored as provided and are not validated until session runtime. A bad token surfaces as an MCP auth error during the session, which is emitted but does not block the session from continuing.

Constraints:

- **One active credential per `mcp_server_url` per vault.** Creating a second credential for the same URL returns a 409.
- **`mcp_server_url` is immutable.** To point at a different server, archive this credential and create a new one.
- **Maximum 20 credentials per vault.** This matches the maximum amount of MCP servers per agent.

## Rotate a credential

Only the secret payload and a handful of metadata fields are mutable. `mcp_server_url`, `token_endpoint`, and `client_id` are locked after creation.

<CodeGroup defaultLanguage="CLI">
  
````bash
curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/vaults/$vault_id/credentials/$credential_id" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- <<'EOF' > /dev/null
{
  "auth": {
    "type": "mcp_oauth",
    "access_token": "xoxp-new-...",
    "expires_at": "2026-05-15T00:00:00Z",
    "refresh": {"refresh_token": "xoxe-1-new-..."}
  }
}
EOF
````

  
````bash
ant beta:vaults:credentials update \
  --vault-id "$VAULT_ID" \
  --credential-id "$CREDENTIAL_ID" <<'EOF'
auth:
  type: mcp_oauth
  access_token: xoxp-new-...
  expires_at: "2026-05-15T00:00:00Z"
  refresh:
    refresh_token: xoxe-1-new-...
EOF
````

  
````python
client.beta.vaults.credentials.update(
    credential.id,
    vault_id=vault.id,
    auth={
        "type": "mcp_oauth",
        "access_token": "xoxp-new-...",
        "expires_at": "2026-05-15T00:00:00Z",
        "refresh": {"refresh_token": "xoxe-1-new-..."},
    },
)
````

  
````typescript
await client.beta.vaults.credentials.update(credential.id, {
  vault_id: vault.id,
  auth: {
    type: "mcp_oauth",
    access_token: "xoxp-new-...",
    expires_at: "2026-05-15T00:00:00Z",
    refresh: {
      refresh_token: "xoxe-1-new-...",
    },
  },
});
````

  
````csharp
await client.Beta.Vaults.Credentials.Update(credential.ID, new()
{
    VaultID = vault.ID,
    Auth = new BetaManagedAgentsMcpOAuthUpdateParams
    {
        Type = "mcp_oauth",
        AccessToken = "xoxp-new-...",
        ExpiresAt = DateTimeOffset.Parse("2026-05-15T00:00:00Z"),
        Refresh = new() { RefreshToken = "xoxe-1-new-..." },
    },
});
````

  
````go
_, err = client.Beta.Vaults.Credentials.Update(ctx, credential.ID, anthropic.BetaVaultCredentialUpdateParams{
	VaultID: vault.ID,
	Auth: anthropic.BetaVaultCredentialUpdateParamsAuthUnion{
		OfMCPOAuth: &anthropic.BetaManagedAgentsMCPOAuthUpdateParams{
			Type:        anthropic.BetaManagedAgentsMCPOAuthUpdateParamsTypeMCPOAuth,
			AccessToken: anthropic.String("xoxp-new-..."),
			ExpiresAt:   anthropic.Time(time.Date(2026, time.May, 15, 0, 0, 0, 0, time.UTC)),
			Refresh: anthropic.BetaManagedAgentsMCPOAuthRefreshUpdateParams{
				RefreshToken: anthropic.String("xoxe-1-new-..."),
			},
		},
	},
})
if err != nil {
	panic(err)
}
````

  
````java
client.beta().vaults().credentials().update(credential.id(),
    CredentialUpdateParams.builder()
        .vaultId(vault.id())
        .auth(BetaManagedAgentsMcpOAuthUpdateParams.builder()
            .type(BetaManagedAgentsMcpOAuthUpdateParams.Type.MCP_OAUTH)
            .accessToken("xoxp-new-...")
            .expiresAt(OffsetDateTime.parse("2026-05-15T00:00:00Z"))
            .refresh(BetaManagedAgentsMcpOAuthRefreshUpdateParams.builder()
                .refreshToken("xoxe-1-new-...")
                .build())
            .build())
        .build());
````

  
````php
$client->beta->vaults->credentials->update(
    $credential->id,
    vaultID: $vault->id,
    auth: [
        'type' => 'mcp_oauth',
        'access_token' => 'xoxp-new-...',
        'expires_at' => '2026-05-15T00:00:00Z',
        'refresh' => ['refresh_token' => 'xoxe-1-new-...'],
    ],
);
````

  
````ruby
client.beta.vaults.credentials.update(
  credential.id,
  vault_id: vault.id,
  auth: {
    type: "mcp_oauth",
    access_token: "xoxp-new-...",
    expires_at: "2026-05-15T00:00:00Z",
    refresh: {refresh_token: "xoxe-1-new-..."}
  }
)
````

</CodeGroup>

## Reference the vault at session creation

Pass `vault_ids` when creating a session:

<CodeGroup>
  
````bash
session_id=$(curl --fail-with-body -sS https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- <<EOF | jq -r '.id'
{
  "agent": "$agent_id",
  "environment_id": "$environment_id",
  "vault_ids": ["$vault_id"],
  "title": "Alice's Slack digest"
}
EOF
)
````

  
````bash
SESSION_ID=$(ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID" \
  --vault-id "$VAULT_ID" \
  --title "Alice's Slack digest" \
  --transform id --format yaml)
````

  
````python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    vault_ids=[vault.id],
    title="Alice's Slack digest",
)
````

  
````typescript
const session = await client.beta.sessions.create({
  agent: agent.id,
  environment_id: environment.id,
  vault_ids: [vault.id],
  title: "Alice's Slack digest",
});
````

  
````csharp
var session = await client.Beta.Sessions.Create(new()
{
    Agent = agent.ID,
    EnvironmentID = environment.ID,
    VaultIds = [vault.ID],
    Title = "Alice's Slack digest",
});
````

  
````go
session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
	Agent: anthropic.BetaSessionNewParamsAgentUnion{
		OfString: anthropic.String(agent.ID),
	},
	EnvironmentID: environment.ID,
	VaultIDs:      []string{vault.ID},
	Title:         anthropic.String("Alice's Slack digest"),
})
if err != nil {
	panic(err)
}
````

  
````java
var session = client.beta().sessions().create(SessionCreateParams.builder()
    .agent(agent.id())
    .environmentId(environment.id())
    .vaultIds(List.of(vault.id()))
    .title("Alice's Slack digest")
    .build());
````

  
````php
$session = $client->beta->sessions->create(
    agent: $agent->id,
    environmentID: $environment->id,
    vaultIDs: [$vault->id],
    title: "Alice's Slack digest",
);
````

  
````ruby
session = client.beta.sessions.create(
  agent: agent.id,
  environment_id: environment.id,
  vault_ids: [vault.id],
  title: "Alice's Slack digest"
)
````

</CodeGroup>

Runtime behavior:

- Credentials are re-resolved periodically during the session, so a rotation or archive propagates to running sessions without a restart.
- When a vault has no credential for the MCP server, the connection is attempted unauthenticated and produces an error.
- When multiple vaults cover the the MCP server, the first vault with a match wins.

## Other operations

- **List vaults or credentials:** Paginated, newest first. Archived records are excluded by default (pass `include_archived=true` to include them).
- **Archive a vault:** `POST /v1/vaults/{id}/archive`. Cascades to all credentials. Secrets are purged; records are retained for auditing. Future sessions referencing this vault fail; running sessions continue.
- **Archive a credential:** `POST /v1/vaults/{id}/credentials/{cred_id}/archive`. Purges the secret payload; `mcp_server_url` remains visible. Frees the `mcp_server_url` for a replacement credential.
- **Delete a vault or credential:** Hard delete. The record is not retained. Use archive if you need an audit trail.
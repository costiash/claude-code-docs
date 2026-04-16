# Accessing GitHub

Connect your agent to GitHub repositories for cloning, reading, and creating pull requests.

---

You can mount a GitHub repository to your session container and connect to the GitHub MCP for making pull requests.

GitHub repositories are cached, so future sessions that use the same repository start faster.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
</Note>

## GitHub MCP and Session Resources

First, create an agent that declares the GitHub MCP server. The agent definition holds the server URL but no auth token:

<CodeGroup defaultLanguage="CLI">
  
````bash
agent_id=$(curl -fsS https://api.anthropic.com/v1/agents \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- <<JSON | jq -r '.id'
{
  "name": "Code Reviewer",
  "model": "claude-opus-4-7",
  "system": "You are a code review assistant with access to GitHub.",
  "mcp_servers": [
    {
      "type": "url",
      "name": "github",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  ],
  "tools": [
    {"type": "agent_toolset_20260401"},
    {
      "type": "mcp_toolset",
      "mcp_server_name": "github"
    }
  ]
}
JSON
)
````

  
````bash
AGENT_ID=$(ant beta:agents create \
  --name "Code Reviewer" \
  --model '{id: claude-opus-4-7}' \
  --system "You are a code review assistant with access to GitHub." \
  --mcp-server '{type: url, name: github, url: https://api.githubcopilot.com/mcp/}' \
  --tool '{type: agent_toolset_20260401}' \
  --tool '{type: mcp_toolset, mcp_server_name: github}' \
  --transform id --format yaml)
````

  
````python
agent = client.beta.agents.create(
    name="Code Reviewer",
    model="claude-opus-4-7",
    system="You are a code review assistant with access to GitHub.",
    mcp_servers=[
        {
            "type": "url",
            "name": "github",
            "url": "https://api.githubcopilot.com/mcp/",
        },
    ],
    tools=[
        {"type": "agent_toolset_20260401"},
        {
            "type": "mcp_toolset",
            "mcp_server_name": "github",
        },
    ],
)
````

  
````typescript
const agent = await client.beta.agents.create({
  name: "Code Reviewer",
  model: "claude-opus-4-7",
  system: "You are a code review assistant with access to GitHub.",
  mcp_servers: [
    {
      type: "url",
      name: "github",
      url: "https://api.githubcopilot.com/mcp/",
    },
  ],
  tools: [
    { type: "agent_toolset_20260401" },
    {
      type: "mcp_toolset",
      mcp_server_name: "github",
    },
  ],
});
````

  
````csharp
var agent = await client.Beta.Agents.Create(new()
{
    Name = "Code Reviewer",
    Model = new("claude-opus-4-7"),
    System = "You are a code review assistant with access to GitHub.",
    McpServers =
    [
        new() { Type = "url", Name = "github", Url = "https://api.githubcopilot.com/mcp/" },
    ],
    Tools =
    [
        new BetaManagedAgentsAgentToolset20260401Params
        {
            Type = "agent_toolset_20260401",
        },
        new BetaManagedAgentsMcpToolsetParams
        {
            Type = "mcp_toolset",
            McpServerName = "github",
        },
    ],
});
````

  
````go
agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
	Name: "Code Reviewer",
	Model: anthropic.BetaManagedAgentsModelConfigParams{
		ID:   "claude-opus-4-7",
		Type: anthropic.BetaManagedAgentsModelConfigParamsTypeModelConfig,
	},
	System: anthropic.String("You are a code review assistant with access to GitHub."),
	MCPServers: []anthropic.BetaManagedAgentsUrlmcpServerParams{
		{
			Type: anthropic.BetaManagedAgentsUrlmcpServerParamsTypeURL,
			Name: "github",
			URL:  "https://api.githubcopilot.com/mcp/",
		},
	},
	Tools: []anthropic.BetaAgentNewParamsToolUnion{
		{
			OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
				Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
			},
		},
		{
			OfMCPToolset: &anthropic.BetaManagedAgentsMCPToolsetParams{
				Type:          anthropic.BetaManagedAgentsMCPToolsetParamsTypeMCPToolset,
				MCPServerName: "github",
			},
		},
	},
})
if err != nil {
	panic(err)
}
````

  
````java
var agent = client.beta().agents().create(AgentCreateParams.builder()
    .name("Code Reviewer")
    .model(BetaManagedAgentsModel.CLAUDE_OPUS_4_7)
    .system("You are a code review assistant with access to GitHub.")
    .addMcpServer(BetaManagedAgentsUrlmcpServerParams.builder()
        .type(BetaManagedAgentsUrlmcpServerParams.Type.URL)
        .name("github")
        .url("https://api.githubcopilot.com/mcp/")
        .build())
    .addTool(BetaManagedAgentsAgentToolset20260401Params.builder()
        .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
        .build())
    .addTool(BetaManagedAgentsMcpToolsetParams.builder()
        .type(BetaManagedAgentsMcpToolsetParams.Type.MCP_TOOLSET)
        .mcpServerName("github")
        .build())
    .build());
````

  
````php
$agent = $client->beta->agents->create(
    name: 'Code Reviewer',
    model: 'claude-opus-4-7',
    system: 'You are a code review assistant with access to GitHub.',
    mcpServers: [
        [
            'type' => 'url',
            'name' => 'github',
            'url' => 'https://api.githubcopilot.com/mcp/',
        ],
    ],
    tools: [
        ['type' => 'agent_toolset_20260401'],
        [
            'type' => 'mcp_toolset',
            'mcpServerName' => 'github',
        ],
    ],
);
````

  
````ruby
agent = client.beta.agents.create(
  name: "Code Reviewer",
  model: "claude-opus-4-7",
  system_: "You are a code review assistant with access to GitHub.",
  mcp_servers: [
    {
      type: "url",
      name: "github",
      url: "https://api.githubcopilot.com/mcp/"
    }
  ],
  tools: [
    {type: "agent_toolset_20260401"},
    {
      type: "mcp_toolset",
      mcp_server_name: "github"
    }
  ]
)
````

</CodeGroup>

Then create a session that mounts the GitHub repository:

<CodeGroup>
  
````bash
session_id=$(curl -fsS https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- <<JSON | jq -r '.id'
{
  "agent": "$agent_id",
  "environment_id": "$environment_id",
  "resources": [
    {
      "type": "github_repository",
      "url": "https://github.com/org/repo",
      "mount_path": "/workspace/repo",
      "authorization_token": "ghp_your_github_token"
    }
  ]
}
JSON
)
````

  
````bash
SESSION_ID=$(ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID" \
  --transform id --format yaml <<'EOF'
resources:
  - type: github_repository
    url: https://github.com/org/repo
    mount_path: /workspace/repo
    authorization_token: ghp_your_github_token
EOF
)
````

  
````python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    resources=[
        {
            "type": "github_repository",
            "url": "https://github.com/org/repo",
            "mount_path": "/workspace/repo",
            "authorization_token": "ghp_your_github_token",
        },
    ],
)
````

  
````typescript
const session = await client.beta.sessions.create({
  agent: agent.id,
  environment_id: environment.id,
  resources: [
    {
      type: "github_repository",
      url: "https://github.com/org/repo",
      mount_path: "/workspace/repo",
      authorization_token: "ghp_your_github_token",
    },
  ],
});
````

  
````csharp
var session = await client.Beta.Sessions.Create(new()
{
    Agent = agent.ID,
    EnvironmentID = environment.ID,
    Resources =
    [
        new BetaManagedAgentsGitHubRepositoryResourceParams
        {
            Type = "github_repository",
            Url = "https://github.com/org/repo",
            MountPath = "/workspace/repo",
            AuthorizationToken = "ghp_your_github_token",
        },
    ],
});
````

  
````go
session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
	Agent:         anthropic.BetaSessionNewParamsAgentUnion{OfString: anthropic.String(agent.ID)},
	EnvironmentID: environment.ID,
	Resources: []anthropic.BetaSessionNewParamsResourceUnion{
		{
			OfGitHubRepository: &anthropic.BetaManagedAgentsGitHubRepositoryResourceParams{
				Type:               anthropic.BetaManagedAgentsGitHubRepositoryResourceParamsTypeGitHubRepository,
				URL:                "https://github.com/org/repo",
				MountPath:          anthropic.String("/workspace/repo"),
				AuthorizationToken: "ghp_your_github_token",
			},
		},
	},
})
if err != nil {
	panic(err)
}
````

  
````java
var session = client.beta().sessions().create(SessionCreateParams.builder()
    .agent(agent.id())
    .environmentId(environment.id())
    .addResource(BetaManagedAgentsGitHubRepositoryResourceParams.builder()
        .type(BetaManagedAgentsGitHubRepositoryResourceParams.Type.GITHUB_REPOSITORY)
        .url("https://github.com/org/repo")
        .mountPath("/workspace/repo")
        .authorizationToken("ghp_your_github_token")
        .build())
    .build());
````

  
````php
$session = $client->beta->sessions->create(
    agent: $agent->id,
    environmentID: $environment->id,
    resources: [
        [
            'type' => 'github_repository',
            'url' => 'https://github.com/org/repo',
            'mountPath' => '/workspace/repo',
            'authorizationToken' => 'ghp_your_github_token',
        ],
    ],
);
````

  
````ruby
session = client.beta.sessions.create(
  agent: agent.id,
  environment_id: environment.id,
  resources: [
    {
      type: "github_repository",
      url: "https://github.com/org/repo",
      mount_path: "/workspace/repo",
      authorization_token: "ghp_your_github_token"
    }
  ]
)
````

</CodeGroup>

The `resources[].authorization_token` authenticates the repository clone operation and is not echoed in API responses.

## Token permissions

When providing a GitHub token, use the minimum required permissions:

| Action | Required scopes |
|--------|----------------|
| Clone private repos | `repo` |
| Create PRs | `repo` |
| Read issues | `repo` (private) or `public_repo` |
| Create issues | `repo` (private) or `public_repo` |

<Warning>
Use fine-grained personal access tokens with minimum required permissions. Avoid using tokens with broad access to your GitHub account.
</Warning>

## Multiple repositories

Mount multiple repositories by adding entries to the `resources` array:

<CodeGroup>
  
````bash
resources='[
  {
    "type": "github_repository",
    "url": "https://github.com/org/frontend",
    "mount_path": "/workspace/frontend",
    "authorization_token": "ghp_your_github_token"
  },
  {
    "type": "github_repository",
    "url": "https://github.com/org/backend",
    "mount_path": "/workspace/backend",
    "authorization_token": "ghp_your_github_token"
  }
]'
````

  
````bash
RESOURCES_BODY=$(cat <<'EOF'
resources:
  - type: github_repository
    url: https://github.com/org/frontend
    mount_path: /workspace/frontend
    authorization_token: ghp_your_github_token
  - type: github_repository
    url: https://github.com/org/backend
    mount_path: /workspace/backend
    authorization_token: ghp_your_github_token
EOF
)
````

  
````python
resources = [
    {
        "type": "github_repository",
        "url": "https://github.com/org/frontend",
        "mount_path": "/workspace/frontend",
        "authorization_token": "ghp_your_github_token",
    },
    {
        "type": "github_repository",
        "url": "https://github.com/org/backend",
        "mount_path": "/workspace/backend",
        "authorization_token": "ghp_your_github_token",
    },
]
````

  
````typescript
const resources = [
  {
    type: "github_repository",
    url: "https://github.com/org/frontend",
    mount_path: "/workspace/frontend",
    authorization_token: "ghp_your_github_token",
  },
  {
    type: "github_repository",
    url: "https://github.com/org/backend",
    mount_path: "/workspace/backend",
    authorization_token: "ghp_your_github_token",
  },
];
````

  
````csharp
BetaManagedAgentsGitHubRepositoryResourceParams[] resources =
[
    new()
    {
        Type = "github_repository",
        Url = "https://github.com/org/frontend",
        MountPath = "/workspace/frontend",
        AuthorizationToken = "ghp_your_github_token",
    },
    new()
    {
        Type = "github_repository",
        Url = "https://github.com/org/backend",
        MountPath = "/workspace/backend",
        AuthorizationToken = "ghp_your_github_token",
    },
];
````

  
````go
resources := []anthropic.BetaSessionNewParamsResourceUnion{
	{
		OfGitHubRepository: &anthropic.BetaManagedAgentsGitHubRepositoryResourceParams{
			Type:               anthropic.BetaManagedAgentsGitHubRepositoryResourceParamsTypeGitHubRepository,
			URL:                "https://github.com/org/frontend",
			MountPath:          anthropic.String("/workspace/frontend"),
			AuthorizationToken: "ghp_your_github_token",
		},
	},
	{
		OfGitHubRepository: &anthropic.BetaManagedAgentsGitHubRepositoryResourceParams{
			Type:               anthropic.BetaManagedAgentsGitHubRepositoryResourceParamsTypeGitHubRepository,
			URL:                "https://github.com/org/backend",
			MountPath:          anthropic.String("/workspace/backend"),
			AuthorizationToken: "ghp_your_github_token",
		},
	},
}
````

  
````java
var resources = List.of(
    BetaManagedAgentsGitHubRepositoryResourceParams.builder()
        .type(BetaManagedAgentsGitHubRepositoryResourceParams.Type.GITHUB_REPOSITORY)
        .url("https://github.com/org/frontend")
        .mountPath("/workspace/frontend")
        .authorizationToken("ghp_your_github_token")
        .build(),
    BetaManagedAgentsGitHubRepositoryResourceParams.builder()
        .type(BetaManagedAgentsGitHubRepositoryResourceParams.Type.GITHUB_REPOSITORY)
        .url("https://github.com/org/backend")
        .mountPath("/workspace/backend")
        .authorizationToken("ghp_your_github_token")
        .build());
````

  
````php
$resources = [
    [
        'type' => 'github_repository',
        'url' => 'https://github.com/org/frontend',
        'mountPath' => '/workspace/frontend',
        'authorizationToken' => 'ghp_your_github_token',
    ],
    [
        'type' => 'github_repository',
        'url' => 'https://github.com/org/backend',
        'mountPath' => '/workspace/backend',
        'authorizationToken' => 'ghp_your_github_token',
    ],
];
````

  
````ruby
resources = [
  {
    type: "github_repository",
    url: "https://github.com/org/frontend",
    mount_path: "/workspace/frontend",
    authorization_token: "ghp_your_github_token"
  },
  {
    type: "github_repository",
    url: "https://github.com/org/backend",
    mount_path: "/workspace/backend",
    authorization_token: "ghp_your_github_token"
  }
]
````

</CodeGroup>

## Managing repositories on a running session

After a session is created, you can list its repository resources and rotate their authorization tokens. Each resource has an `id` returned at session creation time (or via `resources.list`) that you use for updates. Repositories are attached for the lifetime of the session; to change which repositories are mounted, create a new session.

<CodeGroup>
  
````bash
# List resources on the session
repo_resource_id=$(curl -fsS "https://api.anthropic.com/v1/sessions/$session_id/resources" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" | jq -r '.data[0].id')
echo "$repo_resource_id"  # "sesrsc_01ABC..."

# Rotate the authorization token
curl -fsS "https://api.anthropic.com/v1/sessions/$session_id/resources/$repo_resource_id" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -o /dev/null \
  --data @- <<JSON
{
  "authorization_token": "ghp_your_new_github_token"
}
JSON
````

  
````bash
# List resources on the session
ant beta:sessions:resources list --session-id "$SESSION_ID"

# Rotate the authorization token on a specific resource
ant beta:sessions:resources update \
  --session-id "$SESSION_ID" \
  --resource-id "$RESOURCE_ID" \
  --authorization-token "ghp_your_new_github_token"
````

  
````python
# List resources on the session
listed = client.beta.sessions.resources.list(session.id)
repo_resource_id = listed.data[0].id
print(repo_resource_id)  # "sesrsc_01ABC..."

# Rotate the authorization token
client.beta.sessions.resources.update(
    repo_resource_id,
    session_id=session.id,
    authorization_token="ghp_your_new_github_token",
)
````

  
````typescript
// List resources on the session
const listed = await client.beta.sessions.resources.list(session.id);
const repoResourceId = listed.data[0].id;
console.log(repoResourceId); // "sesrsc_01ABC..."

// Rotate the authorization token
await client.beta.sessions.resources.update(repoResourceId, {
  session_id: session.id,
  authorization_token: "ghp_your_new_github_token",
});
````

  
````csharp
// List resources on the session
var listed = await client.Beta.Sessions.Resources.List(session.ID);
var repoResourceId = listed.Data[0].ID;
Console.WriteLine(repoResourceId); // "sesrsc_01ABC..."

// Rotate the authorization token
await client.Beta.Sessions.Resources.Update(repoResourceId, new()
{
    SessionID = session.ID,
    AuthorizationToken = "ghp_your_new_github_token",
});
````

  
````go
// List resources on the session
listed, err := client.Beta.Sessions.Resources.List(ctx, session.ID, anthropic.BetaSessionResourceListParams{})
if err != nil {
	panic(err)
}
repoResourceID := listed.Data[0].ID
fmt.Println(repoResourceID) // "sesrsc_01ABC..."

// Rotate the authorization token
_, err = client.Beta.Sessions.Resources.Update(ctx, repoResourceID, anthropic.BetaSessionResourceUpdateParams{
	SessionID:          session.ID,
	AuthorizationToken: "ghp_your_new_github_token",
})
if err != nil {
	panic(err)
}
````

  
````java
// List resources on the session
var listed = client.beta().sessions().resources().list(session.id());
var repoResourceId = listed.data().getFirst().asGitHubRepository().id();
IO.println(repoResourceId);  // "sesrsc_01ABC..."

// Rotate the authorization token
client.beta().sessions().resources().update(repoResourceId, ResourceUpdateParams.builder()
    .sessionId(session.id())
    .authorizationToken("ghp_your_new_github_token")
    .build());
````

  
````php
// List resources on the session
$listed = $client->beta->sessions->resources->list($session->id);
$repoResourceId = $listed->data[0]->id;
echo $repoResourceId, PHP_EOL; // "sesrsc_01ABC..."

// Rotate the authorization token
$client->beta->sessions->resources->update(
    $repoResourceId,
    sessionID: $session->id,
    authorizationToken: 'ghp_your_new_github_token',
);
````

  
````ruby
# List resources on the session
listed = client.beta.sessions.resources.list(session.id)
repo_resource_id = listed.data.first.id
puts repo_resource_id # "sesrsc_01ABC..."

# Rotate the authorization token
client.beta.sessions.resources.update(
  repo_resource_id,
  session_id: session.id,
  authorization_token: "ghp_your_new_github_token"
)
````

</CodeGroup>

## Creating pull requests

With the GitHub MCP server, the agent can create branches, commit changes, and push them:

<CodeGroup>
  
````bash
curl -fsS "https://api.anthropic.com/v1/sessions/$session_id/events" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -o /dev/null \
  --data @- <<JSON
{
  "events": [
    {
      "type": "user.message",
      "content": [
        {
          "type": "text",
          "text": "Fix the type error in src/utils.ts, commit it to a new branch, and push it."
        }
      ]
    }
  ]
}
JSON
````

  
````bash
ant beta:sessions:events send \
  --session-id "$SESSION_ID" \
  > /dev/null <<'EOF'
events:
  - type: user.message
    content:
      - type: text
        text: Fix the type error in src/utils.ts, commit it to a new branch, and push it.
EOF
````

  
````python
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.message",
            "content": [
                {
                    "type": "text",
                    "text": "Fix the type error in src/utils.ts, commit it to a new branch, and push it.",
                },
            ],
        },
    ],
)
````

  
````typescript
await client.beta.sessions.events.send(session.id, {
  events: [
    {
      type: "user.message",
      content: [
        {
          type: "text",
          text: "Fix the type error in src/utils.ts, commit it to a new branch, and push it.",
        },
      ],
    },
  ],
});
````

  
````csharp
await client.Beta.Sessions.Events.Send(session.ID, new()
{
    Events =
    [
        new BetaManagedAgentsUserMessageEventParams
        {
            Type = "user.message",
            Content =
            [
                new BetaManagedAgentsTextBlock
                {
                    Type = "text",
                    Text = "Fix the type error in src/utils.ts, commit it to a new branch, and push it.",
                },
            ],
        },
    ],
});
````

  
````go
_, err = client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
	Events: []anthropic.SendEventsParamsUnion{
		{
			OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
				Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
				Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{
					{
						OfText: &anthropic.BetaManagedAgentsTextBlockParam{
							Type: anthropic.BetaManagedAgentsTextBlockTypeText,
							Text: "Fix the type error in src/utils.ts, commit it to a new branch, and push it.",
						},
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
client.beta().sessions().events().send(session.id(), EventSendParams.builder()
    .addEvent(BetaManagedAgentsUserMessageEventParams.builder()
        .type(BetaManagedAgentsUserMessageEventParams.Type.USER_MESSAGE)
        .addContent(BetaManagedAgentsTextBlock.builder()
            .type(BetaManagedAgentsTextBlock.Type.TEXT)
            .text("Fix the type error in src/utils.ts, commit it to a new branch, and push it.")
            .build())
        .build())
    .build());
````

  
````php
$client->beta->sessions->events->send(
    $session->id,
    events: [
        [
            'type' => 'user.message',
            'content' => [
                [
                    'type' => 'text',
                    'text' => 'Fix the type error in src/utils.ts, commit it to a new branch, and push it.',
                ],
            ],
        ],
    ],
);
````

  
````ruby
client.beta.sessions.events.send_(
  session.id,
  events: [
    {
      type: "user.message",
      content: [
        {
          type: "text",
          text: "Fix the type error in src/utils.ts, commit it to a new branch, and push it."
        }
      ]
    }
  ]
)
````

</CodeGroup>
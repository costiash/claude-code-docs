# Cloud environment setup

Customize cloud containers for your sessions.

---

Environments define the container configuration where your agent runs. You create an environment once, then reference its ID each time you start a session. Multiple sessions can share the same environment, but each session gets its own isolated container instance.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
</Note>

## Create an environment

<CodeGroup defaultLanguage="CLI">
  
````bash
environment=$(curl -fsS https://api.anthropic.com/v1/environments \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- <<'EOF'
{
  "name": "python-dev",
  "config": {
    "type": "cloud",
    "networking": {"type": "unrestricted"}
  }
}
EOF
)
environment_id=$(jq -r '.id' <<< "$environment")

echo "Environment ID: $environment_id"
````

  
````bash
ant beta:environments create \
  --name "python-dev" \
  --config '{type: cloud, networking: {type: unrestricted}}'
````

  
````python
environment = client.beta.environments.create(
    name="python-dev",
    config={
        "type": "cloud",
        "networking": {"type": "unrestricted"},
    },
)

print(f"Environment ID: {environment.id}")
````

  
````typescript
const environment = await client.beta.environments.create({
  name: "python-dev",
  config: {
    type: "cloud",
    networking: { type: "unrestricted" },
  },
});

console.log(`Environment ID: ${environment.id}`);
````

  
````csharp
var environment = await client.Beta.Environments.Create(new()
{
    Name = "python-dev",
    Config = new()
    {
        Networking = new UnrestrictedNetwork(),
    },
});

Console.WriteLine($"Environment ID: {environment.ID}");
````

  
````go
environment, err := client.Beta.Environments.New(ctx, anthropic.BetaEnvironmentNewParams{
	Name: "python-dev",
	Config: anthropic.BetaCloudConfigParams{
		Networking: anthropic.BetaCloudConfigParamsNetworkingUnion{
			OfUnrestricted: &anthropic.UnrestrictedNetworkParam{},
		},
	},
})
if err != nil {
	panic(err)
}

fmt.Printf("Environment ID: %s\n", environment.ID)
````

  
````java
var environment = client.beta().environments().create(EnvironmentCreateParams.builder()
    .name("python-dev")
    .config(BetaCloudConfigParams.builder()
        .networking(UnrestrictedNetwork.builder().build())
        .build())
    .build());
IO.println("Environment ID: " + environment.id());
````

  
````php
$environment = $client->beta->environments->create(
    name: 'python-dev',
    config: ['type' => 'cloud', 'networking' => ['type' => 'unrestricted']],
);
echo "Environment ID: {$environment->id}\n";
````

  
````ruby
environment = client.beta.environments.create(
  name: "python-dev",
  config: {
    type: "cloud",
    networking: {type: "unrestricted"}
  }
)

puts "Environment ID: #{environment.id}"
````

</CodeGroup>

The `name` must be unique within your organization and workspace.

## Use the environment in a session

Pass the environment ID as a string when creating a session.

<CodeGroup>
  
````bash
session=$(curl -fsS https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- <<EOF
{
  "agent": "$agent_id",
  "environment_id": "$environment_id"
}
EOF
)
````

  
````python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
)
````

  
````typescript
const session = await client.beta.sessions.create({
  agent: agent.id,
  environment_id: environment.id,
});
````

  
````csharp
var session = await client.Beta.Sessions.Create(new()
{
    Agent = agent.ID,
    EnvironmentID = environment.ID,
});
````

  
````go
session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
	Agent: anthropic.BetaSessionNewParamsAgentUnion{
		OfString: anthropic.String(agent.ID),
	},
	EnvironmentID: environment.ID,
})
if err != nil {
	panic(err)
}
````

  
````java
var session = client.beta().sessions().create(SessionCreateParams.builder()
    .agent(agent.id())
    .environmentId(environment.id())
    .build());
````

  
````php
$session = $client->beta->sessions->create(
    agent: $agent->id,
    environmentID: $environment->id,
);
````

  
````ruby
session = client.beta.sessions.create(
  agent: agent.id,
  environment_id: environment.id
)
````

</CodeGroup>

## Configuration options

### Packages

The `packages` field pre-installs packages into the container before the agent starts. Packages are installed by their respective package managers and cached across sessions that share the same environment. When multiple package managers are specified, they run in alphabetical order (apt, cargo, gem, go, npm, pip). You can optionally pin specific versions; the default is latest.

<CodeGroup defaultLanguage="CLI">
```bash curl
environment=$(curl -fsS https://api.anthropic.com/v1/environments \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- <<'EOF'
{
  "name": "data-analysis",
  "config": {
    "type": "cloud",
    "packages": {
      "pip": ["pandas", "numpy", "scikit-learn"],
      "npm": ["express"]
    },
    "networking": {"type": "unrestricted"}
  }
}
EOF
)
```

```bash CLI
ant beta:environments create <<'YAML'
name: data-analysis
config:
  type: cloud
  packages:
    pip:
      - pandas
      - numpy
      - scikit-learn
    npm:
      - express
  networking:
    type: unrestricted
YAML
```

```python Python
environment = client.beta.environments.create(
    name="data-analysis",
    config={
        "type": "cloud",
        "packages": {
            "pip": ["pandas", "numpy", "scikit-learn"],
            "npm": ["express"],
        },
        "networking": {"type": "unrestricted"},
    },
)
```

```typescript TypeScript
const environment = await client.beta.environments.create({
  name: "data-analysis",
  config: {
    type: "cloud",
    packages: {
      pip: ["pandas", "numpy", "scikit-learn"],
      npm: ["express"]
    },
    networking: { type: "unrestricted" }
  }
});
```

```csharp C#
var environment = await client.Beta.Environments.Create(new()
{
    Name = "data-analysis",
    Config = new()
    {
        Packages = new()
        {
            Pip = ["pandas", "numpy", "scikit-learn"],
            Npm = ["express"],
        },
        Networking = new UnrestrictedNetwork(),
    },
});
```

```go Go
environment, err := client.Beta.Environments.New(ctx, anthropic.BetaEnvironmentNewParams{
	Name: "data-analysis",
	Config: anthropic.BetaCloudConfigParams{
		Packages: anthropic.BetaPackagesParams{
			Pip: []string{"pandas", "numpy", "scikit-learn"},
			Npm: []string{"express"},
		},
		Networking: anthropic.BetaCloudConfigParamsNetworkingUnion{
			OfUnrestricted: &anthropic.UnrestrictedNetworkParam{},
		},
	},
})
if err != nil {
	panic(err)
}
```

```java Java
var environment = client.beta().environments().create(EnvironmentCreateParams.builder()
    .name("data-analysis")
    .config(BetaCloudConfigParams.builder()
        .packages(BetaPackagesParams.builder()
            .pip(List.of("pandas", "numpy", "scikit-learn"))
            .npm(List.of("express"))
            .build())
        .networking(UnrestrictedNetwork.builder().build())
        .build())
    .build());
```

```php PHP
$environment = $client->beta->environments->create(
    name: 'data-analysis',
    config: [
        'type' => 'cloud',
        'packages' => [
            'pip' => ['pandas', 'numpy', 'scikit-learn'],
            'npm' => ['express'],
        ],
        'networking' => ['type' => 'unrestricted'],
    ],
);
```

```ruby Ruby
environment = client.beta.environments.create(
  name: "data-analysis",
  config: {
    type: "cloud",
    packages: {
      pip: %w[pandas numpy scikit-learn],
      npm: %w[express]
    },
    networking: {type: "unrestricted"}
  }
)
```
</CodeGroup>

Supported package managers:

| Field | Package manager | Example |
| --- | --- | --- |
| `apt` | System packages (apt-get) | `"ffmpeg"` |
| `cargo` | Rust (cargo) | `"ripgrep@14.0.0"` |
| `gem` | Ruby (gem) | `"rails:7.1.0"` |
| `go` | Go modules | `"golang.org/x/tools/cmd/goimports@latest"` |
| `npm` | Node.js (npm) | `"express@4.18.0"` |
| `pip` | Python (pip) | `"pandas==2.2.0"` |

### Networking

The `networking` field controls the container's outbound network access. It does not impact the `web_search` or `web_fetch` tools' allowed domains.

| Mode | Description |
| --- | --- |
| `unrestricted` | Full outbound network access, except for a general safety blocklist. This is the default. |
| `limited` | Restricts container network access to the `allowed_hosts` list. Further access is enabled via the `allow_package_managers` and `allow_mcp_servers` bool.|

<CodeGroup>
```bash curl
config=$(cat <<'EOF'
{
  "type": "cloud",
  "networking": {
    "type": "limited",
    "allowed_hosts": ["api.example.com"],
    "allow_mcp_servers": true,
    "allow_package_managers": true
  }
}
EOF
)
```

```python Python
config = {
    "type": "cloud",
    "networking": {
        "type": "limited",
        "allowed_hosts": ["api.example.com"],
        "allow_mcp_servers": True,
        "allow_package_managers": True,
    },
}
```

```typescript TypeScript
const config = {
  type: "cloud",
  networking: {
    type: "limited",
    allowed_hosts: ["api.example.com"],
    allow_mcp_servers: true,
    allow_package_managers: true
  }
};
```

```csharp C#
var config = new BetaCloudConfigParams
{
    Networking = new BetaLimitedNetworkParams
    {
        AllowedHosts = ["api.example.com"],
        AllowMcpServers = true,
        AllowPackageManagers = true,
    },
};
```

```go Go
config := anthropic.BetaCloudConfigParams{
	Networking: anthropic.BetaCloudConfigParamsNetworkingUnion{
		OfLimited: &anthropic.BetaLimitedNetworkParams{
			AllowedHosts:         []string{"api.example.com"},
			AllowMCPServers:      anthropic.Bool(true),
			AllowPackageManagers: anthropic.Bool(true),
		},
	},
}
```

```java Java
var config = BetaCloudConfigParams.builder()
    .networking(BetaLimitedNetworkParams.builder()
        .allowedHosts(List.of("api.example.com"))
        .allowMcpServers(true)
        .allowPackageManagers(true)
        .build())
    .build();
```

```php PHP
$config = [
    'type' => 'cloud',
    'networking' => [
        'type' => 'limited',
        'allowed_hosts' => ['api.example.com'],
        'allow_mcp_servers' => true,
        'allow_package_managers' => true,
    ],
];
```

```ruby Ruby
config = {
  type: "cloud",
  networking: {
    type: "limited",
    allowed_hosts: %w[api.example.com],
    allow_mcp_servers: true,
    allow_package_managers: true
  }
}
```
</CodeGroup>

<Info>
For production deployments, use `limited` networking with an explicit `allowed_hosts` list. Follow the principle of least privilege by granting only the minimum network access your agent requires, and regularly audit your allowed domains.
</Info>

When using `limited` networking:
- `allowed_hosts` specifies domains the container can reach. These must be HTTPS-prefixed.
- `allow_mcp_servers` permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.
- `allow_package_managers` permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

## Environment lifecycle

- Environments persist until explicitly archived or deleted.
- Multiple sessions can reference the same environment.
- Each session gets its own container instance. Sessions do not share file system state.
- Environments are not versioned. If you frequently update your environments, you may want to log these updates on your side, to map environment state with sessions.

## Manage environments

<CodeGroup defaultLanguage="CLI">
  
````bash
# List environments
environments=$(curl -fsS https://api.anthropic.com/v1/environments \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01")

# Retrieve a specific environment
env=$(curl -fsS "https://api.anthropic.com/v1/environments/$environment_id" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01")

# Archive an environment (read-only, existing sessions continue)
curl -fsS -X POST "https://api.anthropic.com/v1/environments/$environment_id/archive" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01"

# Delete an environment (only if no sessions reference it)
curl -fsS -X DELETE "https://api.anthropic.com/v1/environments/$environment_id" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01"
````

  
````bash
# List environments
ant beta:environments list

# Retrieve a specific environment
ant beta:environments retrieve --environment-id "$ENVIRONMENT_ID"

# Archive an environment (read-only, existing sessions continue)
ant beta:environments archive --environment-id "$ENVIRONMENT_ID"

# Delete an environment (only if no sessions reference it)
ant beta:environments delete --environment-id "$ENVIRONMENT_ID"
````

  
````python
# List environments
environments = client.beta.environments.list()

# Retrieve a specific environment
env = client.beta.environments.retrieve(environment.id)

# Archive an environment (read-only, existing sessions continue)
client.beta.environments.archive(environment.id)

# Delete an environment (only if no sessions reference it)
client.beta.environments.delete(environment.id)
````

  
````typescript
// List environments
const environments = await client.beta.environments.list();

// Retrieve a specific environment
const env = await client.beta.environments.retrieve(environment.id);

// Archive an environment (read-only, existing sessions continue)
await client.beta.environments.archive(environment.id);

// Delete an environment (only if no sessions reference it)
await client.beta.environments.delete(environment.id);
````

  
````csharp
// List environments
var environments = await client.Beta.Environments.List();

// Retrieve a specific environment
var env = await client.Beta.Environments.Retrieve(environment.ID);

// Archive an environment (read-only, existing sessions continue)
await client.Beta.Environments.Archive(environment.ID);

// Delete an environment (only if no sessions reference it)
await client.Beta.Environments.Delete(environment.ID);
````

  
````go
// List environments
environments, err := client.Beta.Environments.List(ctx, anthropic.BetaEnvironmentListParams{})
if err != nil {
	panic(err)
}

// Retrieve a specific environment
env, err := client.Beta.Environments.Get(ctx, environment.ID, anthropic.BetaEnvironmentGetParams{})
if err != nil {
	panic(err)
}

// Archive an environment (read-only, existing sessions continue)
_, err = client.Beta.Environments.Archive(ctx, environment.ID, anthropic.BetaEnvironmentArchiveParams{})
if err != nil {
	panic(err)
}

// Delete an environment (only if no sessions reference it)
_, err = client.Beta.Environments.Delete(ctx, environment.ID, anthropic.BetaEnvironmentDeleteParams{})
if err != nil {
	panic(err)
}
````

  
````java
// List environments
var environments = client.beta().environments().list();
// Retrieve a specific environment
var env = client.beta().environments().retrieve(environment.id());
// Archive an environment (read-only, existing sessions continue)
client.beta().environments().archive(environment.id());
// Delete an environment (only if no sessions reference it)
client.beta().environments().delete(environment.id());
````

  
````php
// List environments
$environments = $client->beta->environments->list();
// Retrieve a specific environment
$env = $client->beta->environments->retrieve($environment->id);
// Archive an environment (read-only, existing sessions continue)
$client->beta->environments->archive($environment->id);
// Delete an environment (only if no sessions reference it)
$client->beta->environments->delete($environment->id);
````

  
````ruby
# List environments
environments = client.beta.environments.list

# Retrieve a specific environment
env = client.beta.environments.retrieve(environment.id)

# Archive an environment (read-only, existing sessions continue)
client.beta.environments.archive(environment.id)

# Delete an environment (only if no sessions reference it)
client.beta.environments.delete(environment.id)
````

</CodeGroup>

## Pre-installed runtimes

Cloud containers include common runtimes out of the box. See [Container reference](/docs/en/managed-agents/cloud-containers) for the full list of pre-installed languages, databases, and utilities.
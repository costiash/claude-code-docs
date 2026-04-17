# Start a session

Create a session to run your agent and begin executing tasks.

---

A session is a running agent instance within an environment. Each session references an [agent](/docs/en/managed-agents/agent-setup) and an [environment](/docs/en/managed-agents/environments) (both created separately), and maintains conversation history across multiple interactions.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
</Note>

## Creating a session

A session requires an `agent` ID and an `environment` ID. Agents are versioned resources; passing in the `agent` ID as a string starts the session with the latest agent version.

<CodeGroup>
  
  ```bash curl
  session=$(curl -fsSL https://api.anthropic.com/v1/sessions \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d @- <<EOF
  {
    "agent": "$AGENT_ID",
    "environment_id": "$ENVIRONMENT_ID"
  }
  EOF
  )
  SESSION_ID=$(jq -r '.id' <<< "$session")
  ```
  
  ```bash CLI nocheck
  ant beta:sessions create \
    --agent "$AGENT_ID" \
    --environment-id "$ENVIRONMENT_ID"
  ```
  ```python Python
  session = client.beta.sessions.create(
      agent=agent.id,
      environment_id=environment.id,
  )
  ```
  ```typescript TypeScript
  const session = await client.beta.sessions.create({
    agent: agent.id,
    environment_id: environment.id
  });
  ```
  ```csharp C#
  var session = await client.Beta.Sessions.Create(new()
  {
      Agent = agent.ID,
      EnvironmentID = environment.ID,
  });
  ```
  ```go Go
  	session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
  		Agent: anthropic.BetaSessionNewParamsAgentUnion{
  			OfString: anthropic.String(agent.ID),
  		},
  		EnvironmentID: environment.ID,
  	})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      var session = client.beta().sessions().create(SessionCreateParams.builder()
          .agent(agent.id())
          .environmentId(environment.id())
          .build());
  ```
  ```php PHP
  $session = $client->beta->sessions->create(
      agent: $agent->id,
      environmentID: $environment->id,
  );
  ```
  ```ruby Ruby
  session = client.beta.sessions.create(
    agent: agent.id,
    environment_id: environment.id
  )
  ```
</CodeGroup>

To pin a session to a specific agent version, pass an object. This lets you control exactly which version runs and stage rollouts of new versions independently.

<CodeGroup>
  
  ```bash curl
  pinned_session=$(curl -fsSL https://api.anthropic.com/v1/sessions \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d @- <<EOF
  {
    "agent": {"type": "agent", "id": "$AGENT_ID", "version": 1},
    "environment_id": "$ENVIRONMENT_ID"
  }
  EOF
  )
  PINNED_SESSION_ID=$(jq -r '.id' <<< "$pinned_session")
  ```
  
  ```bash CLI nocheck
  ant beta:sessions create <<YAML
  agent:
    type: agent
    id: $AGENT_ID
    version: 1
  environment_id: $ENVIRONMENT_ID
  YAML
  ```
  ```python Python
  pinned_session = client.beta.sessions.create(
      agent={"type": "agent", "id": agent.id, "version": 1},
      environment_id=environment.id,
  )
  ```
  ```typescript TypeScript
  const pinnedSession = await client.beta.sessions.create({
    agent: { type: "agent", id: agent.id, version: 1 },
    environment_id: environment.id
  });
  ```
  ```csharp C#
  var pinnedSession = await client.Beta.Sessions.Create(new()
  {
      Agent = new BetaManagedAgentsAgentParams
      {
          Type = "agent",
          ID = agent.ID,
          Version = 1,
      },
      EnvironmentID = environment.ID,
  });
  ```
  ```go Go
  	pinnedSession, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
  		Agent: anthropic.BetaSessionNewParamsAgentUnion{
  			OfBetaManagedAgentsAgents: &anthropic.BetaManagedAgentsAgentParams{
  				Type:    anthropic.BetaManagedAgentsAgentParamsTypeAgent,
  				ID:      agent.ID,
  				Version: anthropic.Int(1),
  			},
  		},
  		EnvironmentID: environment.ID,
  	})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      var pinnedSession = client.beta().sessions().create(SessionCreateParams.builder()
          .agent(BetaManagedAgentsAgentParams.builder()
              .type(BetaManagedAgentsAgentParams.Type.AGENT)
              .id(agent.id())
              .version(1)
              .build())
          .environmentId(environment.id())
          .build());
  ```
  ```php PHP
  $pinnedSession = $client->beta->sessions->create(
      agent: ['type' => 'agent', 'id' => $agent->id, 'version' => 1],
      environmentID: $environment->id,
  );
  ```
  ```ruby Ruby
  pinned_session = client.beta.sessions.create(
    agent: {type: "agent", id: agent.id, version: 1},
    environment_id: environment.id
  )
  ```
</CodeGroup>

<Tip>
The agent defines how Claude behaves within the session, including the model, system prompt, tools, and MCP servers. See [Agent setup](/docs/en/managed-agents/agent-setup) for details.
</Tip>

## MCP authentication through vaults

If your agent uses MCP tools that require authentication, pass `vault_ids` at session creation to reference a vault containing stored OAuth credentials. Anthropic manages token refresh on your behalf. See [Authenticate with vaults](/docs/en/managed-agents/vaults) for how to create vaults and register credentials.

<CodeGroup>
  
  ```bash curl
  vault_session=$(curl -fsSL https://api.anthropic.com/v1/sessions \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d @- <<EOF
  {
    "agent": "$AGENT_ID",
    "environment_id": "$ENVIRONMENT_ID",
    "vault_ids": ["$VAULT_ID"]
  }
  EOF
  )
  VAULT_SESSION_ID=$(jq -r '.id' <<< "$vault_session")
  ```
  
  ```bash CLI nocheck
  ant beta:sessions create <<YAML
  agent: $AGENT_ID
  environment_id: $ENVIRONMENT_ID
  vault_ids:
    - $VAULT_ID
  YAML
  ```
  ```python Python
  vault_session = client.beta.sessions.create(
      agent=agent.id,
      environment_id=environment.id,
      vault_ids=[vault.id],
  )
  ```
  ```typescript TypeScript
  const vaultSession = await client.beta.sessions.create({
    agent: agent.id,
    environment_id: environment.id,
    vault_ids: [vault.id]
  });
  ```
  ```csharp C#
  var vaultSession = await client.Beta.Sessions.Create(new()
  {
      Agent = agent.ID,
      EnvironmentID = environment.ID,
      VaultIds = [vault.ID],
  });
  ```
  ```go Go
  	vaultSession, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
  		Agent: anthropic.BetaSessionNewParamsAgentUnion{
  			OfString: anthropic.String(agent.ID),
  		},
  		EnvironmentID: environment.ID,
  		VaultIDs:      []string{vault.ID},
  	})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      var vaultSession = client.beta().sessions().create(SessionCreateParams.builder()
          .agent(agent.id())
          .environmentId(environment.id())
          .addVaultId(vault.id())
          .build());
  ```
  ```php PHP
  $vaultSession = $client->beta->sessions->create(
      agent: $agent->id,
      environmentID: $environment->id,
      vaultIDs: [$vault->id],
  );
  ```
  ```ruby Ruby
  vault_session = client.beta.sessions.create(
    agent: agent.id,
    environment_id: environment.id,
    vault_ids: [vault.id]
  )
  ```
</CodeGroup>

## Starting the session

Creating a session provisions the environment and agent but does not start any work. To delegate a task, send events to the session using a [user event](/docs/en/managed-agents/events-and-streaming#user-events). The session acts as a state machine that tracks progress while events drive the actual execution.

<CodeGroup>
  
  ```bash curl
  curl -fsSL "https://api.anthropic.com/v1/sessions/$SESSION_ID/events" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d @- <<'EOF'
  {
    "events": [
      {
        "type": "user.message",
        "content": [{"type": "text", "text": "List the files in the working directory."}]
      }
    ]
  }
  EOF
  ```
  
  ```bash CLI nocheck
  ant beta:sessions:events send \
    --session-id "$SESSION_ID" \
 <<'YAML'
  events:
    - type: user.message
      content:
        - type: text
          text: List the files in the working directory.
  YAML
  ```
  ```python Python
  client.beta.sessions.events.send(
      session.id,
      events=[
          {
              "type": "user.message",
              "content": [
                  {"type": "text", "text": "List the files in the working directory."}
              ],
          },
      ],
  )
  ```
  ```typescript TypeScript
  await client.beta.sessions.events.send(session.id, {
    events: [
      {
        type: "user.message",
        content: [{ type: "text", text: "List the files in the working directory." }]
      }
    ]
  });
  ```
  ```csharp C#
  await client.Beta.Sessions.Events.Send(session.ID, new()
  {
      Events =
      [
          new BetaManagedAgentsUserMessageEventParams
          {
              Type = BetaManagedAgentsUserMessageEventParamsType.UserMessage,
              Content =
              [
                  new BetaManagedAgentsTextBlock
                  {
                      Type = BetaManagedAgentsTextBlockType.Text,
                      Text = "List the files in the working directory.",
                  },
              ],
          },
      ],
  });
  ```
  ```go Go
  	if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
  		Events: []anthropic.SendEventsParamsUnion{{
  			OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
  				Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
  				Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{{
  					OfText: &anthropic.BetaManagedAgentsTextBlockParam{
  						Type: anthropic.BetaManagedAgentsTextBlockTypeText,
  						Text: "List the files in the working directory.",
  					},
  				}},
  			},
  		}},
  	}); err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      client.beta().sessions().events().send(
          session.id(),
          EventSendParams.builder()
              .addEvent(BetaManagedAgentsUserMessageEventParams.builder()
                  .type(BetaManagedAgentsUserMessageEventParams.Type.USER_MESSAGE)
                  .addTextContent("List the files in the working directory.")
                  .build())
              .build());
  ```
  ```php PHP
  $client->beta->sessions->events->send(
      $session->id,
      events: [
          [
              'type' => 'user.message',
              'content' => [['type' => 'text', 'text' => 'List the files in the working directory.']],
          ],
      ],
  );
  ```
  ```ruby Ruby
  client.beta.sessions.events.send_(
    session.id,
    events: [
      {
        type: "user.message",
        content: [{type: "text", text: "List the files in the working directory."}]
      }
    ]
  )
  ```
</CodeGroup>

See [Events and streaming](/docs/en/managed-agents/events-and-streaming) for how to stream the agent's responses and handle tool confirmations.

## Session statuses

Sessions progress through these statuses:

| Status | Description |
|--------|-------------|
| `idle` | Agent is waiting for input, including user messages or tool confirmations. Sessions start in `idle`. |
| `running` | Agent is actively executing |
| `rescheduling` | Transient error occurred, retrying automatically |
| `terminated` | Session has ended due to an unrecoverable error |

## Other session operations

### Retrieving a session

<CodeGroup>
  
  ```bash curl
  retrieved=$(curl -fsSL "https://api.anthropic.com/v1/sessions/$SESSION_ID" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01")
  echo "Status: $(jq -r '.status' <<< "$retrieved")"
  ```
  
  ```bash CLI nocheck
  ant beta:sessions retrieve --session-id "$SESSION_ID"
  ```
  ```python Python
  retrieved = client.beta.sessions.retrieve(session.id)
  print(f"Status: {retrieved.status}")
  ```
  ```typescript TypeScript
  const retrieved = await client.beta.sessions.retrieve(session.id);
  console.log(`Status: ${retrieved.status}`);
  ```
  ```csharp C#
  var retrieved = await client.Beta.Sessions.Retrieve(session.ID);
  Console.WriteLine($"Status: {retrieved.Status.Raw()}");
  ```
  ```go Go
  	retrieved, err := client.Beta.Sessions.Get(ctx, session.ID, anthropic.BetaSessionGetParams{})
  	if err != nil {
  		panic(err)
  	}
  	fmt.Printf("Status: %s\n", retrieved.Status)
  ```
  ```java Java
      var retrieved = client.beta().sessions().retrieve(session.id());
      IO.println("Status: " + retrieved.status());
  ```
  ```php PHP
  $retrieved = $client->beta->sessions->retrieve($session->id);
  echo "Status: {$retrieved->status}\n";
  ```
  ```ruby Ruby
  retrieved = client.beta.sessions.retrieve(session.id)
  puts "Status: #{retrieved.status}"
  ```
</CodeGroup>

### Listing sessions

<CodeGroup>
  ```bash curl
  curl -fsSL https://api.anthropic.com/v1/sessions \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    | jq -r '.data[] | "\(.id): \(.status)"'
  ```
  ```bash CLI
  ant beta:sessions list
  ```
  ```python Python
  for session in client.beta.sessions.list():
      print(f"{session.id}: {session.status}")
  ```
  ```typescript TypeScript
  for await (const session of client.beta.sessions.list()) {
    console.log(`${session.id}: ${session.status}`);
  }
  ```
  ```csharp C#
  var sessions = await client.Beta.Sessions.List();
  await foreach (var listedSession in sessions.Paginate())
  {
      Console.WriteLine($"{listedSession.ID}: {listedSession.Status.Raw()}");
  }
  ```
  ```go Go
  	page := client.Beta.Sessions.ListAutoPaging(ctx, anthropic.BetaSessionListParams{})
  	for page.Next() {
  		session := page.Current()
  		fmt.Printf("%s: %s\n", session.ID, session.Status)
  	}
  	if err := page.Err(); err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      for (var listed : client.beta().sessions().list().autoPager()) {
          IO.println(listed.id() + ": " + listed.status());
      }
  ```
  ```php PHP
  foreach ($client->beta->sessions->list()->pagingEachItem() as $session) {
      echo "{$session->id}: {$session->status}\n";
  }
  ```
  ```ruby Ruby
  client.beta.sessions.list.auto_paging_each do |session|
    puts "#{session.id}: #{session.status}"
  end
  ```
</CodeGroup>

### Archiving a session

Archive a session to prevent new events from being sent while preserving its history:

<CodeGroup>
  
  ```bash curl
  curl -fsSL -X POST "https://api.anthropic.com/v1/sessions/$SESSION_ID/archive" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01"
  ```
  
  ```bash CLI nocheck
  ant beta:sessions archive \
    --session-id "$SESSION_ID"
  ```
  ```python Python
  client.beta.sessions.archive(session.id)
  ```
  ```typescript TypeScript
  await client.beta.sessions.archive(session.id);
  ```
  ```csharp C#
  await client.Beta.Sessions.Archive(session.ID);
  ```
  ```go Go
  	_, err = client.Beta.Sessions.Archive(ctx, session.ID, anthropic.BetaSessionArchiveParams{})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      client.beta().sessions().archive(session.id());
  ```
  ```php PHP
  $client->beta->sessions->archive($session->id);
  ```
  ```ruby Ruby
  client.beta.sessions.archive(session.id)
  ```
</CodeGroup>

### Deleting a session

Delete a session to permanently remove its record, events, and associated container. A `running` session cannot be deleted; send an [interrupt event](/docs/en/managed-agents/events-and-streaming#user-events) if you need to delete it immediately.

Files, memory stores, environments, and agents are independent resources and are not affected by session deletion.

<CodeGroup>
  
  ```bash curl
  curl -fsSL -X DELETE "https://api.anthropic.com/v1/sessions/$SESSION_ID" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01"
  ```
  
  ```bash CLI nocheck
  ant beta:sessions delete \
    --session-id "$SESSION_ID"
  ```
  ```python Python
  client.beta.sessions.delete(session.id)
  ```
  ```typescript TypeScript
  await client.beta.sessions.delete(session.id);
  ```
  ```csharp C#
  await client.Beta.Sessions.Delete(session.ID);
  ```
  ```go Go
  	_, err = client.Beta.Sessions.Delete(ctx, session.ID, anthropic.BetaSessionDeleteParams{})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      client.beta().sessions().delete(session.id());
  ```
  ```php PHP
  $client->beta->sessions->delete($session->id);
  ```
  ```ruby Ruby
  client.beta.sessions.delete(session.id)
  ```
</CodeGroup>
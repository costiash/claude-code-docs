# Migration

Move an existing agent built on the Messages API or the Claude Agent SDK to Claude Managed Agents.

---

Claude Managed Agents replaces your hand-written agent loop with managed infrastructure. This page covers what changes when you migrate from a custom loop built on the [Messages API](/docs/en/build-with-claude/working-with-messages) or from the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview).

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
</Note>

## From a Messages API agent loop

If you built an agent by calling `messages.create` in a `while` loop, executing tool calls yourself, and appending results to the conversation history, most of that code goes away.

### What you stop managing

| Before | After |
| --- | --- |
| You maintain the conversation history array and pass it back on every turn. | The session stores history server-side. Send events, receive events. |
| You parse `stop_reason: "tool_use"`, execute the tool, and loop back with a `tool_result` message. | Pre-built tools execute inside the container automatically. You only handle custom tools via `agent.custom_tool_use` events. |
| You provision your own sandbox for running agent-generated code. | The session container handles code execution, file operations, and bash. |
| You decide when the loop is done. | The session emits `session.status_idle` when the agent has nothing more to do. |

### Code comparison

**Before** (Messages API loop, simplified):

<CodeGroup>

```python Python
messages = [{"role": "user", "content": task}]
while True:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=messages,
        tools=tools,
    )
    messages.append({"role": "assistant", "content": response.content})
    if response.stop_reason == "end_turn":
        break
    for block in response.content:
        if block.type == "tool_use":
            result = execute_tool(block.name, block.input)
            messages.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result,
                        }
                    ],
                }
            )
```

```typescript TypeScript
const messages: Anthropic.MessageParam[] = [{ role: "user", content: task }];
while (true) {
  const response = await client.messages.create({
    model: "claude-sonnet-4-6",
    max_tokens: 1024,
    messages,
    tools
  });
  messages.push({ role: "assistant", content: response.content });
  if (response.stop_reason === "end_turn") {
    break;
  }
  for (const block of response.content) {
    if (block.type === "tool_use") {
      const result = executeTool(block.name, block.input);
      messages.push({
        role: "user",
        content: [
          {
            type: "tool_result",
            tool_use_id: block.id,
            content: result
          }
        ]
      });
    }
  }
}
```

```csharp C#
List<MessageParam> messages = [new() { Role = Role.User, Content = task }];
while (true)
{
    var response = await client.Messages.Create(new()
    {
        Model = Model.ClaudeSonnet4_6,
        MaxTokens = 1024,
        Messages = messages,
        Tools = tools,
    });
    messages.Add(new()
    {
        Role = Role.Assistant,
        Content = new([.. response.Content.Select(block => new ContentBlockParam(block.Json))]),
    });
    if (response.StopReason == StopReason.EndTurn)
    {
        break;
    }
    foreach (var block in response.Content)
    {
        if (block.Value is ToolUseBlock toolUse)
        {
            var result = ExecuteTool(toolUse.Name, toolUse.Input);
            messages.Add(new()
            {
                Role = Role.User,
                Content = new([new ToolResultBlockParam { ToolUseID = toolUse.ID, Content = result }]),
            });
        }
    }
}
```

```go Go
messages := []anthropic.MessageParam{
	anthropic.NewUserMessage(anthropic.NewTextBlock(task)),
}
for {
	response, err := client.Messages.New(ctx, anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeSonnet4_6,
		MaxTokens: 1024,
		Messages:  messages,
		Tools:     tools,
	})
	if err != nil {
		log.Fatal(err)
	}
	messages = append(messages, response.ToParam())
	if response.StopReason == anthropic.StopReasonEndTurn {
		break
	}
	for _, block := range response.Content {
		if toolUse, ok := block.AsAny().(anthropic.ToolUseBlock); ok {
			result := executeTool(toolUse.Name, toolUse.Input)
			messages = append(messages, anthropic.NewUserMessage(
				anthropic.NewToolResultBlock(toolUse.ID, result, false),
			))
		}
	}
}
```

```java Java
var messages = new ArrayList<MessageParam>();
messages.add(MessageParam.builder()
    .role(MessageParam.Role.USER)
    .content(task)
    .build());
while (true) {
    var response = client.messages().create(MessageCreateParams.builder()
        .model(Model.CLAUDE_SONNET_4_6)
        .maxTokens(1024)
        .messages(messages)
        .tools(tools)
        .build());
    messages.add(response.toParam());
    if (StopReason.END_TURN.equals(response.stopReason().orElse(null))) {
        break;
    }
    for (var block : response.content()) {
        block.toolUse().ifPresent(toolUse -> {
            var result = executeTool(toolUse.name(), toolUse._input());
            messages.add(MessageParam.builder()
                .role(MessageParam.Role.USER)
                .contentOfBlockParams(List.of(
                    ContentBlockParam.ofToolResult(ToolResultBlockParam.builder()
                        .toolUseId(toolUse.id())
                        .content(result)
                        .build())))
                .build());
        });
    }
}
```

```php PHP
$messages = [['role' => 'user', 'content' => $task]];
while (true) {
    $response = $client->messages->create(
        model: 'claude-sonnet-4-6',
        maxTokens: 1024,
        messages: $messages,
        tools: $tools,
    );
    $messages[] = ['role' => 'assistant', 'content' => $response->content];
    if ($response->stopReason === 'end_turn') {
        break;
    }
    foreach ($response->content as $block) {
        if ($block->type === 'tool_use') {
            $result = executeTool($block->name, $block->input);
            $messages[] = [
                'role' => 'user',
                'content' => [
                    [
                        'type' => 'tool_result',
                        'tool_use_id' => $block->id,
                        'content' => $result,
                    ],
                ],
            ];
        }
    }
}
```

```ruby Ruby
messages = [{ role: "user", content: task }]
loop do
  response = client.messages.create(
    model: "claude-sonnet-4-6",
    max_tokens: 1024,
    messages: messages,
    tools: tools
  )
  messages << { role: "assistant", content: response.content }
  break if response.stop_reason == :end_turn
  response.content.each do |block|
    next unless block.type == :tool_use
    result = execute_tool(block.name, block.input)
    messages << {
      role: "user",
      content: [
        {
          type: "tool_result",
          tool_use_id: block.id,
          content: result
        }
      ]
    }
  end
end
```
</CodeGroup>

**After** (Claude Managed Agents):

<CodeGroup>
  ```bash curl
  agent=$(
    curl --fail-with-body -sS "https://api.anthropic.com/v1/agents?beta=true" \
      -H "x-api-key: ${ANTHROPIC_API_KEY}" \
      -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: managed-agents-2026-04-01" \
      --json '{
        "name": "Task Runner",
        "model": "claude-sonnet-4-6",
        "tools": [{"type": "agent_toolset_20260401"}]
      }'
  )
  agent_id=$(jq -r '.id' <<< "${agent}")

  session_id=$(
    curl --fail-with-body -sS "https://api.anthropic.com/v1/sessions?beta=true" \
      -H "x-api-key: ${ANTHROPIC_API_KEY}" \
      -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: managed-agents-2026-04-01" \
      --json "$(jq -n --argjson a "${agent}" --arg env "${environment_id}" \
        '{agent: {type: "agent", id: $a.id, version: $a.version}, environment_id: $env}')" \
    | jq -r '.id'
  )

  # Open the SSE stream in the background, then send the user message.
  stream_log=$(mktemp)
  curl --fail-with-body -sS -N \
    "https://api.anthropic.com/v1/sessions/${session_id}/stream?beta=true" \
    -H "x-api-key: ${ANTHROPIC_API_KEY}" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    > "${stream_log}" &
  stream_pid=$!

  curl --fail-with-body -sS \
    "https://api.anthropic.com/v1/sessions/${session_id}/events?beta=true" \
    -H "x-api-key: ${ANTHROPIC_API_KEY}" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    --json "$(jq -n --arg text "${task}" \
      '{events: [{type: "user.message", content: [{type: "text", text: $text}]}]}')" \
    > /dev/null

  # Read events until the session goes idle.
  while IFS= read -r line; do
    [[ ${line} == data:* ]] || continue
    event_type=$(jq -r '.type // empty' 2>/dev/null <<< "${line#data: }" || true)
    [[ ${event_type} == "session.status_idle" ]] && break
  done < <(tail -f -n +1 "${stream_log}")

  kill "${stream_pid}" 2>/dev/null || true
  ```
  ```bash CLI
  { read -r _ agent_id; read -r _ agent_version; } < <(ant beta:agents create \
    --name "Task Runner" \
    --model claude-sonnet-4-6 \
    --tool '{type: agent_toolset_20260401}' \
    --transform '{id,version}' --format yaml)

  session_id=$(ant beta:sessions create \
    --agent "{type: agent, id: $agent_id, version: $agent_version}" \
    --environment "$environment_id" \
    --transform id --format yaml)

  # Open the stream first, then send the user message
  exec {stream}< <(ant beta:sessions stream \
    --session-id "$session_id" \
    --transform type --format yaml)

  ant beta:sessions:events send \
    --session-id "$session_id" \
    --event "{type: user.message, content: [{type: text, text: \"$task\"}]}" \
 > /dev/null

  while IFS= read -r -u "$stream" type; do
    [[ $type == session.status_idle ]] && break
  done
  exec {stream}<&-
  ```
  ```python Python
  agent = client.beta.agents.create(
      name="Task Runner",
      model="claude-sonnet-4-6",
      tools=[{"type": "agent_toolset_20260401"}],
  )

  session = client.beta.sessions.create(
      agent={"type": "agent", "id": agent.id, "version": agent.version},
      environment_id=environment.id,
  )

  with client.beta.sessions.events.stream(session.id) as stream:
      client.beta.sessions.events.send(
          session.id,
          events=[{"type": "user.message", "content": [{"type": "text", "text": task}]}],
      )
      for event in stream:
          if event.type == "session.status_idle":
              break
  ```
  ```typescript TypeScript
  const agent = await client.beta.agents.create({
    name: "Task Runner",
    model: "claude-sonnet-4-6",
    tools: [{ type: "agent_toolset_20260401" }]
  });

  const session = await client.beta.sessions.create({
    agent: { type: "agent", id: agent.id, version: agent.version },
    environment_id: environment.id
  });

  const stream = await client.beta.sessions.events.stream(session.id);

  await client.beta.sessions.events.send(session.id, {
    events: [
      {
        type: "user.message",
        content: [{ type: "text", text: task }]
      }
    ]
  });

  for await (const event of stream) {
    if (event.type === "session.status_idle") {
      break;
    }
  }
  ```
  ```csharp C#
  var agent = await client.Beta.Agents.Create(new()
  {
      Name = "Task Runner",
      Model = BetaManagedAgentsModel.ClaudeSonnet4_6,
      Tools =
      [
          new BetaManagedAgentsAgentToolset20260401Params
          {
              Type = "agent_toolset_20260401",
          },
      ],
  });

  var session = await client.Beta.Sessions.Create(new()
  {
      Agent = new BetaManagedAgentsAgentParams
      {
          Type = "agent",
          ID = agent.ID,
          Version = agent.Version,
      },
      EnvironmentID = environment.ID,
  });

  var stream = client.Beta.Sessions.Events.StreamStreaming(session.ID);

  await client.Beta.Sessions.Events.Send(session.ID, new()
  {
      Events =
      [
          new BetaManagedAgentsUserMessageEventParams
          {
              Type = "user.message",
              Content = [new BetaManagedAgentsTextBlock { Type = "text", Text = task }],
          },
      ],
  });

  await foreach (var streamEvent in stream)
  {
      if (streamEvent.Value is BetaManagedAgentsSessionStatusIdleEvent)
      {
          break;
      }
  }
  ```
  ```go Go
  	agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
  		Name: "Task Runner",
  		Model: anthropic.BetaManagedAgentsModelConfigParams{
  			ID:   "claude-sonnet-4-6",
  			Type: anthropic.BetaManagedAgentsModelConfigParamsTypeModelConfig,
  		},
  		Tools: []anthropic.BetaAgentNewParamsToolUnion{{
  			OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
  				Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
  			},
  		}},
  	})
  	if err != nil {
  		log.Fatal(err)
  	}

  	session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
  		Agent: anthropic.BetaSessionNewParamsAgentUnion{
  			OfBetaManagedAgentsAgents: &anthropic.BetaManagedAgentsAgentParams{
  				Type:    anthropic.BetaManagedAgentsAgentParamsTypeAgent,
  				ID:      agent.ID,
  				Version: anthropic.Int(agent.Version),
  			},
  		},
  		EnvironmentID: environment.ID,
  	})
  	if err != nil {
  		log.Fatal(err)
  	}

  	stream := client.Beta.Sessions.Events.StreamEvents(ctx, session.ID, anthropic.BetaSessionEventStreamParams{})
  	defer stream.Close()

  	_, err = client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
  		Events: []anthropic.SendEventsParamsUnion{{
  			OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
  				Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
  				Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{{
  					OfText: &anthropic.BetaManagedAgentsTextBlockParam{
  						Type: anthropic.BetaManagedAgentsTextBlockTypeText,
  						Text: task,
  					},
  				}},
  			},
  		}},
  	})
  	if err != nil {
  		log.Fatal(err)
  	}

  	for stream.Next() {
  		event := stream.Current()
  		if event.Type == "session.status_idle" {
  			break
  		}
  	}
  	if err := stream.Err(); err != nil {
  		log.Fatal(err)
  	}
  ```
  ```java Java
      var agent = client.beta().agents().create(
          AgentCreateParams.builder()
              .name("Task Runner")
              .model(BetaManagedAgentsModel.CLAUDE_SONNET_4_6)
              .addTool(
                  BetaManagedAgentsAgentToolset20260401Params.builder()
                      .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
                      .build()
              )
              .build()
      );

      var session = client.beta().sessions().create(
          SessionCreateParams.builder()
              .agent(
                  BetaManagedAgentsAgentParams.builder()
                      .type(BetaManagedAgentsAgentParams.Type.AGENT)
                      .id(agent.id())
                      .version(agent.version())
                      .build()
              )
              .environmentId(environment.id())
              .build()
      );

      try (var stream = client.beta().sessions().events().streamStreaming(session.id())) {
          client.beta().sessions().events().send(
              session.id(),
              EventSendParams.builder()
                  .addEvent(
                      BetaManagedAgentsUserMessageEventParams.builder()
                          .type(BetaManagedAgentsUserMessageEventParams.Type.USER_MESSAGE)
                          .addTextContent(task)
                          .build()
                  )
                  .build()
          );
          stream.stream()
              .takeWhile(event -> !event.isSessionStatusIdle())
              .forEach(_ -> {});
      }
  ```
  ```php PHP
  $agent = $client->beta->agents->create(
      name: 'Task Runner',
      model: 'claude-sonnet-4-6',
      tools: [
          BetaManagedAgentsAgentToolset20260401Params::with(
              type: 'agent_toolset_20260401',
          ),
      ],
  );

  $session = $client->beta->sessions->create(
      agent: BetaManagedAgentsAgentParams::with(
          type: 'agent',
          id: $agent->id,
          version: $agent->version,
      ),
      environmentID: $environment->id,
  );

  $stream = $client->beta->sessions->events->streamStream($session->id);

  $client->beta->sessions->events->send(
      $session->id,
      events: [
          ManagedAgentsUserMessageEventParams::with(
              type: 'user.message',
              content: [ManagedAgentsTextBlock::with(type: 'text', text: $task)],
          ),
      ],
  );

  foreach ($stream as $event) {
      if ($event->type === 'session.status_idle') {
          break;
      }
  }
  ```
  ```ruby Ruby
  agent = client.beta.agents.create(
    name: "Task Runner",
    model: "claude-sonnet-4-6",
    tools: [{type: "agent_toolset_20260401"}]
  )

  session = client.beta.sessions.create(
    agent: {type: "agent", id: agent.id, version: agent.version},
    environment_id: environment.id
  )

  stream = client.beta.sessions.events.stream_events(session.id)
  client.beta.sessions.events.send_(
    session.id,
    events: [{type: "user.message", content: [{type: "text", text: task}]}]
  )
  stream.each do
    break if it.type == :"session.status_idle"
  end
  ```
</CodeGroup>

### What you still control

- **System prompt and model:** Same fields, now on the agent definition.
- **Custom tools:** Still declared with JSON Schema. Execution moves from inline handling to responding to `agent.custom_tool_use` events. See [Session event stream](/docs/en/managed-agents/events-and-streaming).
- **Context:** You can still inject context via the system prompt, [file resources](/docs/en/managed-agents/files), or [skills](/docs/en/managed-agents/skills).

## From the Claude Agent SDK

If you built with the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview), you're already working with agents, tools, and sessions as concepts. The difference is where they run: the SDK executes in a process you operate, while Managed Agents runs in Anthropic's infrastructure. Most of the migration is mapping SDK configuration objects to their API-side equivalents.

### What changes

| Agent SDK | Managed Agents |
| --- | --- |
| `ClaudeAgentOptions(...)` constructed per run | `client.beta.agents.create(...)` once; the Agent is persisted and versioned server-side. See [Agent setup](/docs/en/managed-agents/agent-setup). |
| `async with ClaudeSDKClient(...)` or `query(...)` | `client.beta.sessions.create(...)` then send and receive [events](/docs/en/managed-agents/events-and-streaming). |
| `@tool`-decorated functions dispatched automatically by the SDK | Declare as `{"type": "custom", ...}` on the Agent; your client handles `agent.custom_tool_use` events and replies with `user.custom_tool_result`. See [Tools](/docs/en/managed-agents/tools). |
| Built-in tools run in your process against your filesystem | `{"type": "agent_toolset_20260401"}` runs the same tools inside the session container against `/workspace`. |
| `cwd`, `add_dirs` point at local paths | Upload or mount [files](/docs/en/managed-agents/files) as session resources. |
| `system_prompt` and the `CLAUDE.md` hierarchy | A single `system` string on the Agent. Each update produces a new server-side version; pin sessions to a specific version to promote or roll back without a deploy. See [Agent setup](/docs/en/managed-agents/agent-setup). |
| `mcp_servers` configured and authenticated in one place | Declare servers on the Agent; provide credentials through a [Vault](/docs/en/managed-agents/vaults) on the Session. |
| `permission_mode`, `can_use_tool` | Per-tool [`permission_policy`](/docs/en/managed-agents/permission-policies); respond to `user.tool_confirmation` events for `always_ask` tools. |

### Code comparison

**Before** (Agent SDK):

```python
from claude_agent_sdk import (
    ClaudeAgentOptions,
    ClaudeSDKClient,
    create_sdk_mcp_server,
    tool,
)


@tool("get_weather", "Get the current weather for a city.", {"city": str})
async def get_weather(args: dict) -> dict:
    return {"content": [{"type": "text", "text": f"{args['city']}: 18°C, clear"}]}


options = ClaudeAgentOptions(
    model="claude-sonnet-4-6",
    system_prompt="You are a concise weather assistant.",
    mcp_servers={
        "weather": create_sdk_mcp_server("weather", "1.0", tools=[get_weather])
    },
)

async with ClaudeSDKClient(options=options) as agent:
    await agent.query("What's the weather in Tokyo?")
    async for msg in agent.receive_response():
        print(msg)
```

**After** (Managed Agents):

```python
from anthropic import Anthropic

client = Anthropic()

agent = client.beta.agents.create(
    name="weather-agent",
    model="claude-sonnet-4-6",
    system="You are a concise weather assistant.",
    tools=[
        {
            "type": "custom",
            "name": "get_weather",
            "description": "Get the current weather for a city.",
            "input_schema": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        }
    ],
)
environment = client.beta.environments.create(
    name="weather-env",
    config={"type": "cloud", "networking": {"type": "unrestricted"}},
)

session = client.beta.sessions.create(
    agent={"type": "agent", "id": agent.id, "version": agent.version},
    environment_id=environment.id,
)


def get_weather(city: str) -> str:
    return f"{city}: 18°C, clear"


with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.message",
                "content": [{"type": "text", "text": "What's the weather in Tokyo?"}],
            }
        ],
    )
    for ev in stream:
        if ev.type == "agent.message":
            print("".join(b.text for b in ev.content))
        elif ev.type == "agent.custom_tool_use":
            result = get_weather(**ev.input)
            client.beta.sessions.events.send(
                session.id,
                events=[
                    {
                        "type": "user.custom_tool_result",
                        "custom_tool_use_id": ev.id,
                        "content": [{"type": "text", "text": result}],
                    }
                ],
            )
        elif ev.type == "session.status_idle" and ev.stop_reason.type == "end_turn":
            break
```

The Agent and Environment are created once and reused across sessions. The tool function still runs in your process; the difference is that you read the `agent.custom_tool_use` event and send the result explicitly instead of the SDK dispatching it for you.

### Features that move to your client

The tradeoff for Anthropic running the agent loop is that a few things the SDK handled automatically become your client's responsibility.

| SDK feature | Managed Agents approach |
| --- | --- |
| Plan mode | Run a planning-only session first, then a second session to execute. |
| Output styles, slash commands | Apply in your client before sending `user.message` or after receiving `agent.message`. |
| `PreToolUse` / `PostToolUse` hooks | Your client already sees every `agent.custom_tool_use` event before responding; put the logic there. For built-in tools, use `permission_policy: always_ask`. |
| `max_turns` | Count turns client-side. |

## Migration checklist

1. [Create an environment](/docs/en/managed-agents/environments) with the networking and runtimes your agent needs.
2. Port your system prompt and tool selection to an [agent definition](/docs/en/managed-agents/agent-setup).
3. Replace your loop with [`sessions.create`](/docs/en/managed-agents/sessions) and [`sessions.stream`](/docs/en/managed-agents/events-and-streaming).
4. For any local files the agent reads, upload them via the [Files API](/docs/en/managed-agents/files) and mount them as `resources`.
5. For any custom tool handlers, move execution into your event loop as responses to `agent.custom_tool_use` events.
6. Verify with a test session before pointing production traffic at the new flow.

## Migrating between model versions

When a new Claude model is released, migrating a Claude Managed Agents integration is typically a one-field change: update `model` on your [agent definition](/docs/en/managed-agents/agent-setup) and the change takes effect on the next session you create.

<CodeGroup defaultLanguage="CLI">
```bash curl
curl -sS --fail-with-body "https://api.anthropic.com/v1/agents/$AGENT_ID?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  --json "$(jq -n --argjson version "$AGENT_VERSION" '{version: $version, model: "claude-sonnet-4-6"}')"
```

```bash CLI
ant beta:agents update \
  --agent-id "$AGENT_ID" \
  --version "$AGENT_VERSION" \
  --model claude-sonnet-4-6
```

```python Python
client.beta.agents.update(
    agent.id,
    version=agent.version,
    model="claude-sonnet-4-6",
)
```

```typescript TypeScript
await client.beta.agents.update(agent.id, {
  version: agent.version,
  model: "claude-sonnet-4-6"
});
```

```csharp C#
await client.Beta.Agents.Update(agent.ID, new()
{
    Version = agent.Version,
    Model = BetaManagedAgentsModel.ClaudeSonnet4_6,
});
```

```go Go
_, err = client.Beta.Agents.Update(ctx, agent.ID, anthropic.BetaAgentUpdateParams{
	Version: agent.Version,
	Model: anthropic.BetaManagedAgentsModelConfigParams{
		ID:   anthropic.BetaManagedAgentsModelClaudeSonnet4_6,
		Type: anthropic.BetaManagedAgentsModelConfigParamsTypeModelConfig,
	},
})
if err != nil {
	panic(err)
}
```

```java Java
client.beta().agents().update(
    agent.id(),
    AgentUpdateParams.builder()
        .version(agent.version())
        .model(BetaManagedAgentsModel.CLAUDE_SONNET_4_6)
        .build()
);
```

```php PHP
$client->beta->agents->update(
    $agent->id,
    version: $agent->version,
    model: 'claude-sonnet-4-6',
);
```

```ruby Ruby
client.beta.agents.update(
  agent.id,
  version: agent.version,
  model: "claude-sonnet-4-6"
)
```
</CodeGroup>

Most model-level behavior changes documented in the [Messages API migration guide](/docs/en/about-claude/models/migration-guide) do not require action on your side:

- **Request parameter changes** (`max_tokens` defaults, `thinking` configuration) are handled by the Claude Managed Agents runtime. These fields are not exposed on the agent definition.
- **Assistant message prefilling** does not exist in the event-based session model, so its removal on newer models is a no-op.
- **Tool argument JSON escaping** is parsed by the runtime before you receive `agent.custom_tool_use` events. You see structured data, not raw strings.

The behavior descriptions in the Messages API guide (what the model does differently) still apply. The migration steps (how to change your request code) do not.
# Session event stream

Send events, stream responses, and interrupt or redirect your session mid-execution.

---

Communication with Claude Managed Agents is event-based. You send user events to the agent, and receive agent and session events back to track status.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
</Note>

## Event types

Events flow in two directions.
- **User events** are what you send to the agent to kick off a session and steer it as it progresses.
- **Session events**, **span events**, and **agent events** are sent to you for observability into your session state and agent progress.

Event type strings follow a `{domain}.{action}` naming convention.

<Tabs>
  <Tab title="User events">

| Type | Description |
| --- | --- |
| `user.message` | A user message with text content. |
| `user.interrupt` | Stop the agent mid-execution. |
| `user.custom_tool_result` | Response to a custom tool call from the agent. |
| `user.tool_confirmation` | Approve or deny an agent or MCP tool call when a permission policy requires confirmation. |
| `user.define_outcome` | Define an [outcome](/docs/en/managed-agents/define-outcomes) for the agent to work toward.  |

  </Tab>
  <Tab title="Agent events">

| Type | Description |
| --- | --- |
| `agent.message` | Agent response containing text content blocks. |
| `agent.thinking` | Agent thinking content, emitted separately from messages. |
| `agent.tool_use` | Agent invoked a pre-built agent tool (bash, file operations, and so on). |
| `agent.tool_result` | Result of a pre-built agent tool execution. |
| `agent.mcp_tool_use` | Agent invoked an MCP server tool. |
| `agent.mcp_tool_result` | Result of an MCP tool execution. |
| `agent.custom_tool_use` | Agent invoked one of your custom tools. Respond with a `user.custom_tool_result` event. |
| `agent.thread_context_compacted` | Conversation history was compacted to fit the context window. |
| `agent.thread_message_sent` | Agent sent a message to another [multiagent](/docs/en/managed-agents/multi-agent) thread. |
| `agent.thread_message_received` | Agent received a message from another [multiagent](/docs/en/managed-agents/multi-agent) thread. |

  </Tab>
  <Tab title="Session events">

| Type | Description |
| --- | --- |
| `session.status_running` | Agent is actively processing. |
| `session.status_idle` | Agent finished its current task and is waiting for input. Includes a `stop_reason` indicating why the agent stopped. |
| `session.status_rescheduled` | A transient error occurred and the session is retrying automatically. |
| `session.status_terminated` | Session ended due to an unrecoverable error. |
| `session.error` | An error occurred during processing. Includes a typed `error` object with a `retry_status`. |
| `session.outcome_evaluated` | An [outcome](/docs/en/managed-agents/define-outcomes) evaluation has reached a terminal status.  |
| `session.thread_created` | The coordinator spawned a new [multiagent](/docs/en/managed-agents/multi-agent) thread. |
| `session.thread_idle` | A [multiagent](/docs/en/managed-agents/multi-agent) thread finished its current work. |

  </Tab>
  <Tab title="Span events">

Span events are observability markers that wrap activity for timing and usage tracking.

| Type | Description |
| --- | --- |
| `span.model_request_start` | A model inference call has started. |
| `span.model_request_end` | A model inference call has completed. Includes `model_usage` with token counts. |
| `span.outcome_evaluation_start` | [Outcome](/docs/en/managed-agents/define-outcomes) evaluation has started.  |
| `span.outcome_evaluation_ongoing` | Heartbeat during an ongoing [outcome](/docs/en/managed-agents/define-outcomes) evaluation.  |
| `span.outcome_evaluation_end` | [Outcome](/docs/en/managed-agents/define-outcomes) evaluation has completed.  |

  </Tab>
</Tabs>

Every event includes a `processed_at` timestamp indicating when the event was recorded server-side. If `processed_at` is null, it means the event has been queued by the harness and will be handled after preceding events finish processing.

See the [session events API reference](/docs/en/api/beta/sessions/events/stream) for the full schema of each event type.

## Integrating events

<Tabs>
  <Tab title="Sending events">

Send a `user.message` event to start or continue the agent's work:

<CodeGroup>
```bash curl
curl -sS --fail-with-body "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<'EOF'
{
  "events": [
    {
      "type": "user.message",
      "content": [
        {"type": "text", "text": "Analyze the performance of the sort function in utils.py"}
      ]
    }
  ]
}
EOF
```

```python Python
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.message",
            "content": [
                {
                    "type": "text",
                    "text": "Analyze the performance of the sort function in utils.py",
                },
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
      content: [
        {
          type: "text",
          text: "Analyze the performance of the sort function in utils.py"
        }
      ]
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
                    Text = "Analyze the performance of the sort function in utils.py",
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
					Text: "Analyze the performance of the sort function in utils.py",
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
            .addTextContent("Analyze the performance of the sort function in utils.py")
            .build())
        .build());
```

```php PHP
$client->beta->sessions->events->send(
    $session->id,
    events: [
        [
            'type' => 'user.message',
            'content' => [
                [
                    'type' => 'text',
                    'text' => 'Analyze the performance of the sort function in utils.py',
                ],
            ],
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
      content: [
        {type: "text", text: "Analyze the performance of the sort function in utils.py"}
      ]
    }
  ]
)
```
</CodeGroup>

Send a `user.interrupt` event to stop the agent mid-execution, then follow up with a `user.message` event to redirect it:

<CodeGroup>
```bash curl
# Agent is currently analyzing a file...
# Interrupt with a new direction:
curl -sS --fail-with-body "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<'EOF'
{
  "events": [
    {"type": "user.interrupt"},
    {
      "type": "user.message",
      "content": [
        {"type": "text", "text": "Instead, focus on fixing the bug in line 42."}
      ]
    }
  ]
}
EOF
```

```python Python
# Agent is currently analyzing a file...
# Interrupt with a new direction:
client.beta.sessions.events.send(
    session.id,
    events=[
        {"type": "user.interrupt"},
        {
            "type": "user.message",
            "content": [
                {
                    "type": "text",
                    "text": "Instead, focus on fixing the bug in line 42.",
                },
            ],
        },
    ],
)
```

```typescript TypeScript
// Agent is currently analyzing a file...
// Interrupt with a new direction:
await client.beta.sessions.events.send(session.id, {
  events: [
    { type: "user.interrupt" },
    {
      type: "user.message",
      content: [
        {
          type: "text",
          text: "Instead, focus on fixing the bug in line 42."
        }
      ]
    }
  ]
});
```

```csharp C#
// Agent is currently analyzing a file...
// Interrupt with a new direction:
await client.Beta.Sessions.Events.Send(session.ID, new()
{
    Events =
    [
        new BetaManagedAgentsUserInterruptEventParams
        {
            Type = BetaManagedAgentsUserInterruptEventParamsType.UserInterrupt,
        },
        new BetaManagedAgentsUserMessageEventParams
        {
            Type = BetaManagedAgentsUserMessageEventParamsType.UserMessage,
            Content =
            [
                new BetaManagedAgentsTextBlock
                {
                    Type = BetaManagedAgentsTextBlockType.Text,
                    Text = "Instead, focus on fixing the bug in line 42.",
                },
            ],
        },
    ],
});
```

```go Go
// Agent is currently analyzing a file...
// Interrupt with a new direction:
if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
	Events: []anthropic.SendEventsParamsUnion{
		{
			OfUserInterrupt: &anthropic.BetaManagedAgentsUserInterruptEventParams{
				Type: anthropic.BetaManagedAgentsUserInterruptEventParamsTypeUserInterrupt,
			},
		},
		{
			OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
				Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
				Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{{
					OfText: &anthropic.BetaManagedAgentsTextBlockParam{
						Type: anthropic.BetaManagedAgentsTextBlockTypeText,
						Text: "Instead, focus on fixing the bug in line 42.",
					},
				}},
			},
		},
	},
}); err != nil {
	panic(err)
}
```

```java Java
// Agent is currently analyzing a file...
// Interrupt with a new direction:
client.beta().sessions().events().send(
    session.id(),
    EventSendParams.builder()
        .addEvent(BetaManagedAgentsUserInterruptEventParams.builder()
            .type(BetaManagedAgentsUserInterruptEventParams.Type.USER_INTERRUPT)
            .build())
        .addEvent(BetaManagedAgentsUserMessageEventParams.builder()
            .type(BetaManagedAgentsUserMessageEventParams.Type.USER_MESSAGE)
            .addTextContent("Instead, focus on fixing the bug in line 42.")
            .build())
        .build());
```

```php PHP
// Agent is currently analyzing a file...
// Interrupt with a new direction:
$client->beta->sessions->events->send(
    $session->id,
    events: [
        ['type' => 'user.interrupt'],
        [
            'type' => 'user.message',
            'content' => [
                [
                    'type' => 'text',
                    'text' => 'Instead, focus on fixing the bug in line 42.',
                ],
            ],
        ],
    ],
);
```

```ruby Ruby
# Agent is currently analyzing a file...
# Interrupt with a new direction:
client.beta.sessions.events.send_(
  session.id,
  events: [
    {type: "user.interrupt"},
    {
      type: "user.message",
      content: [
        {type: "text", text: "Instead, focus on fixing the bug in line 42."}
      ]
    }
  ]
)
```
</CodeGroup>

The agent will acknowledge the interruption and switch to the new task.

  </Tab>
  <Tab title="Streaming responses">

Stream events from the session to receive real-time updates as the agent works. Only events emitted after the stream is opened are delivered, so open the stream before sending events to avoid a race condition.

<CodeGroup>
  
````bash
# Open the stream first, then send the user message
exec {stream}< <(
  curl -sS -N --fail-with-body \
    "https://api.anthropic.com/v1/sessions/$SESSION_ID/stream?beta=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -H "Accept: text/event-stream"
)

curl -sS --fail-with-body \
  "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- >/dev/null <<'EOF'
{
  "events": [
    {
      "type": "user.message",
      "content": [{"type": "text", "text": "Summarize the repo README"}]
    }
  ]
}
EOF

while IFS= read -r -u "$stream" line; do
  [[ $line == data:* ]] || continue
  json=${line#data: }
  case $(jq -r '.type' <<<"$json") in
    agent.message)
      jq -j '.content[] | select(.type == "text") | .text' <<<"$json"
      ;;
    session.status_idle)
      break
      ;;
    session.error)
      printf '\n[Error: %s]\n' "$(jq -r '.error.message // "unknown"' <<<"$json")"
      break
      ;;
  esac
done
exec {stream}<&-
````

  
````bash
# Open the stream first, then send the user message
exec {stream}< <(ant beta:sessions stream \
  --session-id "$SESSION_ID" \
  --transform '{type,text:content.#(type=="text").text,err:error.message}' \
  --format yaml)

ant beta:sessions:events send \
  --session-id "$SESSION_ID" \
 > /dev/null <<'YAML'
events:
  - type: user.message
    content:
      - type: text
        text: Summarize the repo README
YAML

type=
while IFS= read -r -u "$stream" line; do
  case "$line" in
    type:\ session.status_idle) break ;;
    type:\ session.error)
      IFS= read -r -u "$stream" next || next=
      case "$next" in err:\ *) msg=${next#err: } ;; *) msg=unknown ;; esac
      printf '\n[Error: %s]\n' "$msg"; break ;;
    type:\ *) type=${line#type: } ;;
    text:*)
      [[ $type == agent.message ]] || continue
      val=${line#text: }
      case "$val" in '|-'|'|') ;; *) printf '%s' "$val" ;; esac ;;
    \ \ *)
      if [[ $type == agent.message ]]; then printf '%s\n' "${line#  }"; fi ;;
  esac
done
exec {stream}<&-
````

  
````python
# Open the stream first, then send the user message
with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.message",
                "content": [{"type": "text", "text": "Summarize the repo README"}],
            },
        ],
    )

    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    if block.type == "text":
                        print(block.text, end="")
            case "session.status_idle":
                break
            case "session.error":
                msg = event.error.message if event.error else "unknown"
                print(f"\n[Error: {msg}]")
                break
````

  
````typescript
// Open the stream first, then send the user message
const stream = await client.beta.sessions.events.stream(session.id);
await client.beta.sessions.events.send(session.id, {
  events: [
    {
      type: "user.message",
      content: [{ type: "text", text: "Summarize the repo README" }]
    }
  ]
});

for await (const event of stream) {
  if (event.type === "agent.message") {
    for (const block of event.content) {
      if (block.type === "text") {
        process.stdout.write(block.text);
      }
    }
  } else if (event.type === "session.status_idle") {
    break;
  } else if (event.type === "session.error") {
    console.log(`\n[Error: ${event.error?.message ?? "unknown"}]`);
    break;
  }
}
````

  
````csharp
// Open the stream first, then send the user message
using var stream = await client.Beta.Sessions.Events.WithRawResponse.StreamStreaming(session.ID);
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
                    Text = "Summarize the repo README",
                },
            ],
        },
    ],
});

await foreach (var streamEvent in stream.Enumerate())
{
    if (streamEvent.Value is BetaManagedAgentsAgentMessageEvent message)
    {
        foreach (var block in message.Content)
        {
            Console.Write(block.Text);
        }
    }
    else if (streamEvent.Value is BetaManagedAgentsSessionStatusIdleEvent)
    {
        break;
    }
    else if (streamEvent.Value is BetaManagedAgentsSessionErrorEvent error)
    {
        Console.WriteLine($"\n[Error: {error.Error?.Message ?? "unknown"}]");
        break;
    }
}
````

  
````go
	// Open the stream first, then send the user message
	stream := client.Beta.Sessions.Events.StreamEvents(ctx, session.ID, anthropic.BetaSessionEventStreamParams{})
	defer stream.Close()

	if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
		Events: []anthropic.SendEventsParamsUnion{{
			OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
				Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
				Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{{
					OfText: &anthropic.BetaManagedAgentsTextBlockParam{
						Type: anthropic.BetaManagedAgentsTextBlockTypeText,
						Text: "Summarize the repo README",
					},
				}},
			},
		}},
	}); err != nil {
		panic(err)
	}

events:
	for stream.Next() {
		switch event := stream.Current().AsAny().(type) {
		case anthropic.BetaManagedAgentsAgentMessageEvent:
			for _, block := range event.Content {
				fmt.Print(block.Text)
			}
		case anthropic.BetaManagedAgentsSessionStatusIdleEvent:
			break events
		case anthropic.BetaManagedAgentsSessionErrorEvent:
			fmt.Printf("\n[Error: %s]\n", cmp.Or(event.Error.Message, "unknown"))
			break events
		}
	}
	if err := stream.Err(); err != nil {
		panic(err)
	}
````

  
````java
// Open the stream first, then send the user message
try (var stream = client.beta().sessions().events().streamStreaming(session.id())) {
    client.beta().sessions().events().send(
        session.id(),
        EventSendParams.builder()
            .addEvent(BetaManagedAgentsUserMessageEventParams.builder()
                .type(BetaManagedAgentsUserMessageEventParams.Type.USER_MESSAGE)
                .addTextContent("Summarize the repo README")
                .build())
            .build()
    );

    for (var event : (Iterable<StreamEvents>) stream.stream()::iterator) {
        if (event.isAgentMessage()) {
            event.asAgentMessage().content().forEach(block -> IO.print(block.text()));
        } else if (event.isSessionStatusIdle()) {
            break;
        } else if (event.isSessionError()) {
            var msg = event.asSessionError().error()
                .flatMap(err -> err._json())
                .map(json -> {
                    Optional<Map<String, JsonValue>> obj = json.asObject();
                    return obj.orElseThrow().get("message").asStringOrThrow();
                })
                .orElse("unknown");
            IO.println("\n[Error: " + msg + "]");
            break;
        }
    }
}
````

  
````php
// Open the stream first, then send the user message
$stream = $client->beta->sessions->events->streamStream(
    $session->id,
    requestOptions: ['transporter' => $streamingClient],
);
$client->beta->sessions->events->send(
    $session->id,
    events: [
        [
            'type' => 'user.message',
            'content' => [['type' => 'text', 'text' => 'Summarize the repo README']],
        ],
    ],
);

foreach ($stream as $event) {
    match ($event->type) {
        'agent.message' => array_walk(
            $event->content,
            static fn($block) => $block->type === 'text' ? print($block->text) : null,
        ),
        'session.error' => printf("\n[Error: %s]", $event->error?->message ?? 'unknown'),
        default => null,
    };
    if ($event->type === 'session.status_idle' || $event->type === 'session.error') {
        break;
    }
}
$stream->close();
````

  
````ruby
# Open the stream first, then send the user message
stream = client.beta.sessions.events.stream_events(session.id)

client.beta.sessions.events.send_(
  session.id,
  events: [{
    type: "user.message",
    content: [{type: "text", text: "Summarize the repo README"}]
  }]
)

stream.each do |event|
  case event.type
  in :"agent.message"
    event.content.each { print it.text }
  in :"session.status_idle"
    break
  in :"session.error"
    puts "\n[Error: #{event.error&.message || "unknown"}]"
    break
  else
    # ignore other event types
  end
end
````

</CodeGroup>

To reconnect to an existing session without missing events, open a new stream and then list the full history to seed a set of seen event IDs. Tail the live stream while skipping any events already returned by the history list.

<CodeGroup>
  
````bash
exec {stream}< <(
  curl -sS -N --fail-with-body \
    "https://api.anthropic.com/v1/sessions/$SESSION_ID/stream?beta=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -H "Accept: text/event-stream"
)

# Stream is open and buffering. List history before tailing live.
declare -A seen_event_ids
while IFS= read -r id; do
  seen_event_ids[$id]=1
done < <(
  curl -sS --fail-with-body \
    "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" | jq -r '.data[].id'
)

# Tail live events, skipping anything already seen
while IFS= read -r -u "$stream" line; do
  [[ $line == data:* ]] || continue
  json=${line#data: }
  id=$(jq -r '.id' <<<"$json")
  [[ -n ${seen_event_ids[$id]+seen} ]] && continue
  seen_event_ids[$id]=1
  case $(jq -r '.type' <<<"$json") in
    agent.message)
      jq -j '.content[] | select(.type == "text") | .text' <<<"$json"
      ;;
    session.status_idle)
      break
      ;;
  esac
done
exec {stream}<&-
````

  
````bash
exec {stream}< <(ant beta:sessions stream \
  --session-id "$SESSION_ID" \
  --transform '{id,type,text:content.#(type=="text").text}' \
  --format yaml)
stream_pid=$!

# Stream is open and buffering. List history before tailing live.
declare -A seen_event_ids
while IFS= read -r id; do
  seen_event_ids[$id]=1
done < <(ant beta:sessions:events list \
  --session-id "$SESSION_ID" \
  --transform id --format yaml)

# Tail live events, skipping anything already seen
id= type= skip=
while IFS= read -r -u "$stream" line; do
  case "$line" in
    id:\ *)
      id=${line#id: }
      if [[ -n ${seen_event_ids[$id]+seen} ]]; then skip=1; continue; fi
      skip=; seen_event_ids[$id]=1 ;;
    type:\ *)
      [[ -n $skip ]] && continue
      type=${line#type: }
      [[ $type == session.status_idle ]] && break ;;
    text:*)
      [[ -z $skip && $type == agent.message ]] || continue
      val=${line#text: }
      case "$val" in '|-'|'|') ;; *) printf '%s' "$val" ;; esac ;;
    \ \ *)
      [[ -z $skip && $type == agent.message ]] && printf '%s\n' "${line#  }" ;;
  esac
done
exec {stream}<&-
````

  
````python
with client.beta.sessions.events.stream(session.id) as stream:
    # Stream is open and buffering. List history before tailing live.
    seen_event_ids = {event.id for event in client.beta.sessions.events.list(session.id)}

    # Tail live events, skipping anything already seen
    for event in stream:
        if event.id in seen_event_ids:
            continue
        seen_event_ids.add(event.id)
        match event.type:
            case "agent.message":
                for block in event.content:
                    if block.type == "text":
                        print(block.text, end="")
            case "session.status_idle":
                break
````

  
````typescript
const seenEventIds = new Set<string>();
const stream = await client.beta.sessions.events.stream(session.id);

// Stream is open and buffering. List history before tailing live.
for await (const event of client.beta.sessions.events.list(session.id)) {
  seenEventIds.add(event.id);
}

// Tail live events, skipping anything already seen
for await (const event of stream) {
  if (seenEventIds.has(event.id)) continue;
  seenEventIds.add(event.id);
  if (event.type === "agent.message") {
    for (const block of event.content) {
      if (block.type === "text") {
        process.stdout.write(block.text);
      }
    }
  } else if (event.type === "session.status_idle") {
    break;
  }
}
````

  
````csharp
using var stream = await client.Beta.Sessions.Events.WithRawResponse.StreamStreaming(session.ID);

// Stream is open and buffering. List history before tailing live.
HashSet<string> seenEventIds = [];
var history = await client.Beta.Sessions.Events.List(session.ID);
await foreach (var pastEvent in history.Paginate())
{
    seenEventIds.Add(pastEvent.ID);
}

// Tail live events, skipping anything already seen
await foreach (var streamEvent in stream.Enumerate())
{
    if (!seenEventIds.Add(streamEvent.ID))
    {
        continue;
    }
    if (streamEvent.Value is BetaManagedAgentsAgentMessageEvent message)
    {
        foreach (var block in message.Content)
        {
            Console.Write(block.Text);
        }
    }
    else if (streamEvent.Value is BetaManagedAgentsSessionStatusIdleEvent)
    {
        break;
    }
}
````

  
````go
	stream := client.Beta.Sessions.Events.StreamEvents(ctx, session.ID, anthropic.BetaSessionEventStreamParams{})
	defer stream.Close()

	// Stream is open and buffering. List history before tailing live.
	seenEventIDs := map[string]struct{}{}
	history := client.Beta.Sessions.Events.ListAutoPaging(ctx, session.ID, anthropic.BetaSessionEventListParams{})
	for history.Next() {
		seenEventIDs[history.Current().ID] = struct{}{}
	}
	if err := history.Err(); err != nil {
		panic(err)
	}

	// Tail live events, skipping anything already seen
tail:
	for stream.Next() {
		event := stream.Current()
		if _, seen := seenEventIDs[event.ID]; seen {
			continue
		}
		seenEventIDs[event.ID] = struct{}{}
		switch event := event.AsAny().(type) {
		case anthropic.BetaManagedAgentsAgentMessageEvent:
			for _, block := range event.Content {
				fmt.Print(block.Text)
			}
		case anthropic.BetaManagedAgentsSessionStatusIdleEvent:
			break tail
		}
	}
	if err := stream.Err(); err != nil {
		panic(err)
	}
````

  
````java
try (var stream = client.beta().sessions().events().streamStreaming(session.id())) {
    // Stream is open and buffering. List history before tailing live.
    // _json() exposes the raw event so we can read the cross-variant `id` field.
    var seenEventIds = new HashSet<String>();
    for (var past : client.beta().sessions().events().list(session.id()).autoPager()) {
        Optional<Map<String, JsonValue>> obj = past._json().orElseThrow().asObject();
        seenEventIds.add(obj.orElseThrow().get("id").asStringOrThrow());
    }

    // Tail live events, skipping anything already seen
    for (var event : (Iterable<StreamEvents>) stream.stream()::iterator) {
        Optional<Map<String, JsonValue>> obj = event._json().orElseThrow().asObject();
        if (!seenEventIds.add(obj.orElseThrow().get("id").asStringOrThrow())) continue;
        if (event.isAgentMessage()) {
            event.asAgentMessage().content().forEach(block -> IO.print(block.text()));
        } else if (event.isSessionStatusIdle()) {
            break;
        }
    }
}
````

  
````php
$stream = $client->beta->sessions->events->streamStream(
    $session->id,
    requestOptions: ['transporter' => $streamingClient],
);

// Stream is open and buffering. List history before tailing live.
$seenEventIds = [];
foreach ($client->beta->sessions->events->list($session->id)->pagingEachItem() as $event) {
    $seenEventIds[$event->id] = true;
}

// Tail live events, skipping anything already seen
foreach ($stream as $event) {
    if (isset($seenEventIds[$event->id])) {
        continue;
    }
    $seenEventIds[$event->id] = true;
    match ($event->type) {
        'agent.message' => array_walk(
            $event->content,
            static fn($block) => $block->type === 'text' ? print($block->text) : null,
        ),
        default => null,
    };
    if ($event->type === 'session.status_idle') {
        break;
    }
}
$stream->close();
````

  
````ruby
stream = client.beta.sessions.events.stream_events(session.id)

# Stream is open and buffering. List history before tailing live.
seen_event_ids = Set.new
client.beta.sessions.events.list(session.id).auto_paging_each { seen_event_ids << it.id }

# Tail live events, skipping anything already seen
stream.each do |event|
  next if seen_event_ids.include?(event.id)
  seen_event_ids << event.id
  case event.type
  in :"agent.message"
    event.content.each { print it.text }
  in :"session.status_idle"
    break
  else
    # ignore other event types
  end
end
````

</CodeGroup>

  </Tab>
  <Tab title="Listing past events">

Retrieve the full event history for a session:

<CodeGroup>
```bash curl
curl -sS --fail-with-body "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  | jq -r '.data[] | "[\(.type)] \(.processed_at)"'
```

```python Python
events = client.beta.sessions.events.list(session.id)
for event in events.data:
    print(f"[{event.type}] {event.processed_at}")
```

```typescript TypeScript
const events = await client.beta.sessions.events.list(session.id);
for (const event of events.data) {
  console.log(`[${event.type}] ${event.processed_at}`);
}
```

```csharp C#
var events = await client.Beta.Sessions.Events.List(session.ID);
foreach (var evt in events.Items)
{
    Console.WriteLine($"[{evt.Json.GetProperty("type").GetString()}] {evt.ProcessedAt}");
}
```

```go Go
events, err := client.Beta.Sessions.Events.List(ctx, session.ID, anthropic.BetaSessionEventListParams{})
if err != nil {
	panic(err)
}
for _, event := range events.Data {
	fmt.Printf("[%s] %s\n", event.Type, event.ProcessedAt)
}
```

```java Java
var events = client.beta().sessions().events().list(session.id());
for (var event : events.data()) {
    var json = (Map<String, JsonValue>) event._json().orElseThrow().asObject().orElseThrow();
    var type = json.get("type").asStringOrThrow();
    var processedAt = json.containsKey("processed_at")
        ? json.get("processed_at").asStringOrThrow()
        : "pending";
    IO.println("[" + type + "] " + processedAt);
}
```

```php PHP
$events = $client->beta->sessions->events->list($session->id);
foreach ($events->data as $event) {
    $processedAt = ($event->processedAt ?? null)?->format(DATE_RFC3339) ?? 'pending';
    echo "[{$event->type}] {$processedAt}\n";
}
```

```ruby Ruby
events = client.beta.sessions.events.list(session.id)
events.data.each { puts "[#{it.type}] #{it.processed_at}" }
```
</CodeGroup>

  </Tab>
</Tabs>

## Additional scenarios

### Handling custom tool calls

When the agent invokes a [custom tool](/docs/en/managed-agents/tools#custom-tools):

1. The session emits an `agent.custom_tool_use` event containing the tool name and input.
2. The session pauses with a `session.status_idle` event containing `stop_reason: requires_action`. The blocking event IDs are in the `stop_reason.requires_action.event_ids` array.
3. Execute the tool in your system and send a `user.custom_tool_result` event for each, passing the event ID in the `custom_tool_use_id` param along with the result content.
4. Once all blocking events are resolved, the session transitions back to `running`.

<CodeGroup>
```bash curl
exec {fd}< <(curl -sS -N --fail-with-body \
  "https://api.anthropic.com/v1/sessions/$SESSION_ID/stream?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -H "Accept: text/event-stream")

while IFS= read -r -u "$fd" line; do
  [[ $line == data:* ]] || continue
  data="${line#data: }"
  [[ $(jq -r '.type' <<<"$data") == "session.status_idle" ]] || continue
  case $(jq -r '.stop_reason.type // empty' <<<"$data") in
    requires_action)
      while IFS= read -r event_id; do
        # Look up the custom tool use event and execute it
        result=$(call_tool "$event_id")
        # Send the result back
        jq -n --arg id "$event_id" --arg result "$result" \
          '{events: [{type: "user.custom_tool_result", custom_tool_use_id: $id, content: [{type: "text", text: $result}]}]}' |
          curl -sS --fail-with-body \
            "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
            -H "x-api-key: $ANTHROPIC_API_KEY" \
            -H "anthropic-version: 2023-06-01" \
            -H "anthropic-beta: managed-agents-2026-04-01" \
            -H "content-type: application/json" \
            -d @-
      done < <(jq -r '.stop_reason.event_ids[]' <<<"$data")
      ;;
    end_turn)
      break
      ;;
  esac
done
exec {fd}<&-
```

```python Python
with client.beta.sessions.events.stream(session.id) as stream:
    for event in stream:
        if event.type == "session.status_idle" and (stop := event.stop_reason):
            match stop.type:
                case "requires_action":
                    for event_id in stop.event_ids:
                        # Look up the custom tool use event and execute it
                        tool_event = events_by_id[event_id]
                        result = call_tool(tool_event.name, tool_event.input)

                        # Send the result back
                        client.beta.sessions.events.send(
                            session.id,
                            events=[
                                {
                                    "type": "user.custom_tool_result",
                                    "custom_tool_use_id": event_id,
                                    "content": [{"type": "text", "text": result}],
                                },
                            ],
                        )
                case "end_turn":
                    break
```

```typescript TypeScript
const stream = await client.beta.sessions.events.stream(session.id);

for await (const event of stream) {
  if (event.type === "session.status_idle") {
    if (event.stop_reason?.type === "requires_action") {
      for (const eventId of event.stop_reason.event_ids) {
        // Look up the custom tool use event and execute it
        const toolEvent = eventsById[eventId];
        const result = await callTool(toolEvent.name, toolEvent.input);

        // Send the result back
        await client.beta.sessions.events.send(session.id, {
          events: [
            {
              type: "user.custom_tool_result",
              custom_tool_use_id: eventId,
              content: [{ type: "text", text: result }]
            }
          ]
        });
      }
    } else if (event.stop_reason?.type === "end_turn") {
      break;
    }
  }
}
```

```csharp C#
await foreach (var streamEvent in client.Beta.Sessions.Events.StreamStreaming(session.ID))
{
    if (streamEvent.Value is BetaManagedAgentsSessionStatusIdleEvent idle)
    {
        if (idle.StopReason?.Value is BetaManagedAgentsSessionRequiresAction requiresAction)
        {
            foreach (var eventId in requiresAction.EventIds)
            {
                // Look up the custom tool use event and execute it
                var toolEvent = eventsById[eventId];
                var result = await CallTool(toolEvent.Name, toolEvent.Input);
                // Send the result back
                await client.Beta.Sessions.Events.Send(session.ID, new()
                {
                    Events =
                    [
                        new BetaManagedAgentsUserCustomToolResultEventParams
                        {
                            Type = BetaManagedAgentsUserCustomToolResultEventParamsType.UserCustomToolResult,
                            CustomToolUseID = eventId,
                            Content =
                            [
                                new BetaManagedAgentsTextBlock
                                {
                                    Type = BetaManagedAgentsTextBlockType.Text,
                                    Text = result,
                                },
                            ],
                        },
                    ],
                });
            }
        }
        else if (idle.StopReason?.Value is BetaManagedAgentsSessionEndTurn)
        {
            break;
        }
    }
}
```

```go Go
stream := client.Beta.Sessions.Events.StreamEvents(ctx, session.ID, anthropic.BetaSessionEventStreamParams{})
defer stream.Close()

loop:
for stream.Next() {
	event, ok := stream.Current().AsAny().(anthropic.BetaManagedAgentsSessionStatusIdleEvent)
	if !ok {
		continue
	}
	switch stopReason := event.StopReason.AsAny().(type) {
	case anthropic.BetaManagedAgentsSessionRequiresAction:
		for _, eventID := range stopReason.EventIDs {
			// Look up the custom tool use event and execute it
			toolEvent := eventsByID[eventID]
			result := callTool(toolEvent.Name, toolEvent.Input)
			// Send the result back
			if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
				Events: []anthropic.SendEventsParamsUnion{{
					OfUserCustomToolResult: &anthropic.BetaManagedAgentsUserCustomToolResultEventParams{
						Type:            anthropic.BetaManagedAgentsUserCustomToolResultEventParamsTypeUserCustomToolResult,
						CustomToolUseID: eventID,
						Content: []anthropic.BetaManagedAgentsUserCustomToolResultEventParamsContentUnion{{
							OfText: &anthropic.BetaManagedAgentsTextBlockParam{
								Type: anthropic.BetaManagedAgentsTextBlockTypeText,
								Text: result,
							},
						}},
					},
				}},
			}); err != nil {
				panic(err)
			}
		}
	case anthropic.BetaManagedAgentsSessionEndTurn:
		break loop
	}
}
if err := stream.Err(); err != nil {
	panic(err)
}
```

```java Java
try (var stream = client.beta().sessions().events().streamStreaming(session.id())) {
    for (var event : (Iterable<StreamEvents>) stream.stream()::iterator) {
        if (!event.isSessionStatusIdle()) continue;
        var stopReason = event.asSessionStatusIdle().stopReason().orElseThrow();
        if (stopReason.isRequiresAction()) {
            for (var eventId : stopReason.asRequiresAction().eventIds()) {
                // Look up the custom tool use event and execute it
                var toolEvent = eventsById.get(eventId);
                var result = callTool(toolEvent.name(), toolEvent.input());
                // Send the result back
                client.beta().sessions().events().send(
                    session.id(),
                    EventSendParams.builder()
                        .addEvent(BetaManagedAgentsUserCustomToolResultEventParams.builder()
                            .type(BetaManagedAgentsUserCustomToolResultEventParams.Type.USER_CUSTOM_TOOL_RESULT)
                            .customToolUseId(eventId)
                            .addTextContent(result)
                            .build())
                        .build());
            }
        } else if (stopReason.isEndTurn()) {
            break;
        }
    }
}
```

```php PHP
$stream = $client->beta->sessions->events->streamStream(
    $session->id,
    requestOptions: ['transporter' => $streamingClient],
);

foreach ($stream as $event) {
    if ($event->type === 'session.status_idle' && $event->stopReason) {
        if ($event->stopReason->type === 'requires_action') {
            foreach ($event->stopReason->eventIDs as $eventId) {
                // Look up the custom tool use event and execute it
                $toolEvent = $eventsById[$eventId];
                $result = callTool($toolEvent->name, $toolEvent->input);

                // Send the result back
                $client->beta->sessions->events->send(
                    $session->id,
                    events: [
                        [
                            'type' => 'user.custom_tool_result',
                            'custom_tool_use_id' => $eventId,
                            'content' => [['type' => 'text', 'text' => $result]],
                        ],
                    ],
                );
            }
        } elseif ($event->stopReason->type === 'end_turn') {
            break;
        }
    }
}
```

```ruby Ruby
client.beta.sessions.events.stream_events(session.id).each do |event|
  case event
  in {type: :"session.status_idle", stop_reason: {type: :requires_action, event_ids:}}
    event_ids.each do |event_id|
      # Look up the custom tool use event and execute it
      tool_event = events_by_id[event_id]
      result = call_tool(tool_event.name, tool_event.input)
      # Send the result back
      client.beta.sessions.events.send_(
        session.id,
        events: [
          {
            type: "user.custom_tool_result",
            custom_tool_use_id: event_id,
            content: [{type: "text", text: result}]
          }
        ]
      )
    end
  in {type: :"session.status_idle", stop_reason: {type: :end_turn}}
    break
  else
  end
end
```
</CodeGroup>

### Tool confirmation

When a [permission policy](/docs/en/managed-agents/permission-policies) requires confirmation before a tool executes:

1. The session emits an `agent.tool_use` or `agent.mcp_tool_use` event.
2. The session pauses with a `session.status_idle` event containing `stop_reason: requires_action`. The blocking event IDs are in the `stop_reason.requires_action.event_ids` array.
3. Send a `user.tool_confirmation` event for each, passing the event ID in the `tool_use_id` param. Set `result` to `"allow"` or `"deny"`. Use `deny_message` to explain a denial.
4. Once all blocking events are resolved, the session transitions back to `running`.

<CodeGroup>
```bash curl
exec {fd}< <(curl -sS -N --fail-with-body \
  "https://api.anthropic.com/v1/sessions/$SESSION_ID/stream?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -H "Accept: text/event-stream")

while IFS= read -r -u "$fd" line; do
  [[ $line == data:* ]] || continue
  data="${line#data: }"
  [[ $(jq -r '.type' <<<"$data") == "session.status_idle" ]] || continue
  case $(jq -r '.stop_reason.type // empty' <<<"$data") in
    requires_action)
      while IFS= read -r event_id; do
        # Approve the pending tool call
        jq -n --arg id "$event_id" \
          '{events: [{type: "user.tool_confirmation", tool_use_id: $id, result: "allow"}]}' |
          curl -sS --fail-with-body \
            "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
            -H "x-api-key: $ANTHROPIC_API_KEY" \
            -H "anthropic-version: 2023-06-01" \
            -H "anthropic-beta: managed-agents-2026-04-01" \
            -H "content-type: application/json" \
            -d @-
      done < <(jq -r '.stop_reason.event_ids[]' <<<"$data")
      ;;
    end_turn)
      break
      ;;
  esac
done
exec {fd}<&-
```

```python Python
with client.beta.sessions.events.stream(session.id) as stream:
    for event in stream:
        if event.type == "session.status_idle" and (stop := event.stop_reason):
            match stop.type:
                case "requires_action":
                    for event_id in stop.event_ids:
                        # Approve the pending tool call
                        client.beta.sessions.events.send(
                            session.id,
                            events=[
                                {
                                    "type": "user.tool_confirmation",
                                    "tool_use_id": event_id,
                                    "result": "allow",
                                },
                            ],
                        )
                case "end_turn":
                    break
```

```typescript TypeScript
const stream = await client.beta.sessions.events.stream(session.id);

for await (const event of stream) {
  if (event.type === "session.status_idle") {
    if (event.stop_reason?.type === "requires_action") {
      for (const eventId of event.stop_reason.event_ids) {
        // Approve the pending tool call
        await client.beta.sessions.events.send(session.id, {
          events: [
            {
              type: "user.tool_confirmation",
              tool_use_id: eventId,
              result: "allow"
            }
          ]
        });
      }
    } else if (event.stop_reason?.type === "end_turn") {
      break;
    }
  }
}
```

```csharp C#
await foreach (var streamEvent in client.Beta.Sessions.Events.StreamStreaming(session.ID))
{
    if (streamEvent.Value is BetaManagedAgentsSessionStatusIdleEvent idle)
    {
        if (idle.StopReason?.Value is BetaManagedAgentsSessionRequiresAction requiresAction)
        {
            foreach (var eventId in requiresAction.EventIds)
            {
                // Approve the pending tool call
                await client.Beta.Sessions.Events.Send(session.ID, new()
                {
                    Events =
                    [
                        new BetaManagedAgentsUserToolConfirmationEventParams
                        {
                            Type = BetaManagedAgentsUserToolConfirmationEventParamsType.UserToolConfirmation,
                            ToolUseID = eventId,
                            Result = BetaManagedAgentsUserToolConfirmationEventParamsResult.Allow,
                        },
                    ],
                });
            }
        }
        else if (idle.StopReason?.Value is BetaManagedAgentsSessionEndTurn)
        {
            break;
        }
    }
}
```

```go Go
stream := client.Beta.Sessions.Events.StreamEvents(ctx, session.ID, anthropic.BetaSessionEventStreamParams{})
defer stream.Close()

loop:
for stream.Next() {
	event, ok := stream.Current().AsAny().(anthropic.BetaManagedAgentsSessionStatusIdleEvent)
	if !ok {
		continue
	}
	switch stopReason := event.StopReason.AsAny().(type) {
	case anthropic.BetaManagedAgentsSessionRequiresAction:
		for _, eventID := range stopReason.EventIDs {
			// Approve the pending tool call
			if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
				Events: []anthropic.SendEventsParamsUnion{{
					OfUserToolConfirmation: &anthropic.BetaManagedAgentsUserToolConfirmationEventParams{
						Type:      anthropic.BetaManagedAgentsUserToolConfirmationEventParamsTypeUserToolConfirmation,
						ToolUseID: eventID,
						Result:    anthropic.BetaManagedAgentsUserToolConfirmationEventParamsResultAllow,
					},
				}},
			}); err != nil {
				panic(err)
			}
		}
	case anthropic.BetaManagedAgentsSessionEndTurn:
		break loop
	}
}
if err := stream.Err(); err != nil {
	panic(err)
}
```

```java Java
try (var stream = client.beta().sessions().events().streamStreaming(session.id())) {
    for (var event : (Iterable<StreamEvents>) stream.stream()::iterator) {
        if (!event.isSessionStatusIdle()) continue;
        var stopReason = event.asSessionStatusIdle().stopReason().orElseThrow();
        if (stopReason.isRequiresAction()) {
            for (var eventId : stopReason.asRequiresAction().eventIds()) {
                // Approve the pending tool call
                client.beta().sessions().events().send(
                    session.id(),
                    EventSendParams.builder()
                        .addEvent(BetaManagedAgentsUserToolConfirmationEventParams.builder()
                            .type(BetaManagedAgentsUserToolConfirmationEventParams.Type.USER_TOOL_CONFIRMATION)
                            .toolUseId(eventId)
                            .result(BetaManagedAgentsUserToolConfirmationEventParams.Result.ALLOW)
                            .build())
                        .build());
            }
        } else if (stopReason.isEndTurn()) {
            break;
        }
    }
}
```

```php PHP
$stream = $client->beta->sessions->events->streamStream(
    $session->id,
    requestOptions: ['transporter' => $streamingClient],
);

foreach ($stream as $event) {
    if ($event->type === 'session.status_idle' && $event->stopReason) {
        if ($event->stopReason->type === 'requires_action') {
            foreach ($event->stopReason->eventIDs as $eventId) {
                // Approve the pending tool call
                $client->beta->sessions->events->send(
                    $session->id,
                    events: [
                        [
                            'type' => 'user.tool_confirmation',
                            'tool_use_id' => $eventId,
                            'result' => 'allow',
                        ],
                    ],
                );
            }
        } elseif ($event->stopReason->type === 'end_turn') {
            break;
        }
    }
}
```

```ruby Ruby
client.beta.sessions.events.stream_events(session.id).each do |event|
  case event
  in {type: :"session.status_idle", stop_reason: {type: :requires_action, event_ids:}}
    event_ids.each do |event_id|
      # Approve the pending tool call
      client.beta.sessions.events.send_(
        session.id,
        events: [
          {type: "user.tool_confirmation", tool_use_id: event_id, result: "allow"}
        ]
      )
    end
  in {type: :"session.status_idle", stop_reason: {type: :end_turn}}
    break
  else
  end
end
```
</CodeGroup>

### Tracking usage

The session object includes a `usage` field with cumulative token statistics. Fetch the session after it goes idle to read the latest totals, and use them to track costs, enforce budgets, or monitor consumption.

```json
{
  "id": "sesn_01...",
  "status": "idle",
  "usage": {
    "input_tokens": 5000,
    "output_tokens": 3200,
    "cache_creation_input_tokens": 2000,
    "cache_read_input_tokens": 20000
  }
}
```

`input_tokens` reports uncached input tokens and `output_tokens` reports total output tokens across all model calls in the session. The `cache_creation_input_tokens` and `cache_read_input_tokens` fields reflect prompt caching activity. Cache entries use a 5-minute TTL, so back-to-back turns within that window benefit from cache reads, which reduce per-token cost.
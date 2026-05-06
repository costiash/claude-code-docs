# Multiagent sessions

Coordinate multiple agents within a single session.

---

Multi-agent orchestration lets one agent coordinate with others to complete complex work. Agents can act in parallel with their own isolated context, which helps improve output quality and can also improve time to completion.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets this beta header automatically.
</Note>

## How it works

All agents share the same container and filesystem, but each agent runs in its own **session thread**, a context-isolated event stream with its own conversation history. The coordinator reports activity in the **primary thread** (which is the same as the session-level [event stream](/docs/en/managed-agents/events-and-streaming)); additional threads are spawned at runtime when the coordinator decides to delegate.

Threads are persistent: the coordinator can send a follow-up to an agent it called earlier, and that agent retains everything from its previous turns.

Each agent uses its own configuration (model, system prompt, tools, MCP servers, and skills) as defined when that agent was created. Tools and context are not shared.

### What to delegate

Multiagent coordination is best-suited for complex tasks that either require work across a variety of surfaces, or where multiple well-scoped tasks contribute to an overall goal.

Patterns that work well:

- **Parallelization:** Fan out independent subtasks simultaneously (searching multiple sources, analyzing separate files) and have the coordinator synthesize the results.
- **Specialization:** Route to agents with domain-focused system prompts and tools, such as a security agent or a documentation agent, rather than loading a single agent with every capability.
- **Escalation:** Consult a more capable agent / model for a subset of complex subtasks.

## Configure the coordinator

When [defining your agent](/docs/en/managed-agents/agent-setup), set `multiagent` to declare the list of agents the coordinator can delegate to:

<CodeGroup defaultLanguage="CLI">
  
````bash
coordinator=$(curl -fsS https://api.anthropic.com/v1/agents \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "name": "Engineering Lead",
  "model": "claude-opus-4-7",
  "system": "You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.",
  "tools": [
    {
      "type": "agent_toolset_20260401"
    }
  ],
  "multiagent": {
    "type": "coordinator",
    "agents": [
      {"type": "agent", "id": "$REVIEWER_AGENT_ID"},
      {"type": "agent", "id": "$TEST_WRITER_AGENT_ID"}
    ]
  }
}
EOF
)
````

  
````bash
ant beta:agents create <<YAML
name: Engineering Lead
model: claude-opus-4-7
system: You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.
tools:
  - type: agent_toolset_20260401
multiagent:
  type: coordinator
  agents:
    - type: agent
      id: $REVIEWER_AGENT_ID
    - type: agent
      id: $TEST_WRITER_AGENT_ID
YAML
````

  
````python
coordinator = client.beta.agents.create(
    name="Engineering Lead",
    model="claude-opus-4-7",
    system="You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.",
    tools=[
        {"type": "agent_toolset_20260401"},
    ],
    multiagent={
        "type": "coordinator",
        "agents": [
            {"type": "agent", "id": reviewer_agent.id},
            {"type": "agent", "id": test_writer_agent.id},
        ],
    },
)
````

  
````typescript
const coordinator = await client.beta.agents.create({
  name: "Engineering Lead",
  model: "claude-opus-4-7",
  system:
    "You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.",
  tools: [{ type: "agent_toolset_20260401" }],
  multiagent: {
    type: "coordinator",
    agents: [
      { type: "agent", id: reviewerAgent.id },
      { type: "agent", id: testWriterAgent.id },
    ],
  },
});
````

  
````csharp
var coordinator = await client.Beta.Agents.Create(new()
{
    Name = "Engineering Lead",
    Model = BetaManagedAgentsModel.ClaudeOpus4_7,
    System = "You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.",
    Tools =
    [
        new BetaManagedAgentsAgentToolset20260401Params
        {
            Type = BetaManagedAgentsAgentToolset20260401ParamsType.AgentToolset20260401,
        },
    ],
    Multiagent = new BetaManagedAgentsMultiagentCoordinatorParams
    {
        Type = BetaManagedAgentsMultiagentCoordinatorParamsType.Coordinator,
        Agents =
        [
            new BetaManagedAgentsRosterAgentParams { Type = "agent", ID = reviewerAgent.ID },
            new BetaManagedAgentsRosterAgentParams { Type = "agent", ID = testWriterAgent.ID },
        ],
    },
});
````

  
````go
coordinator, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
	Name:   "Engineering Lead",
	Model:  anthropic.BetaManagedAgentsModelConfigParams{ID: anthropic.BetaManagedAgentsModelClaudeOpus4_7},
	System: anthropic.String("You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent."),
	Tools: []anthropic.BetaAgentNewParamsToolUnion{{
		OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
			Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
		},
	}},
	Multiagent: anthropic.BetaAgentNewParamsMultiagentUnion{
		OfCoordinator: &anthropic.BetaManagedAgentsMultiagentCoordinatorParams{
			Type: "coordinator",
			Agents: []anthropic.BetaManagedAgentsRosterEntryUnion{
				{OfAgent: &anthropic.BetaManagedAgentsRosterAgentParams{Type: "agent", ID: reviewerAgent.ID}},
				{OfAgent: &anthropic.BetaManagedAgentsRosterAgentParams{Type: "agent", ID: testWriterAgent.ID}},
			},
		},
	},
})
if err != nil {
	panic(err)
}
````

  
````java
var coordinator = client.beta().agents().create(
    AgentCreateParams.builder()
        .name("Engineering Lead")
        .model(BetaManagedAgentsModel.CLAUDE_OPUS_4_7)
        .system("You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.")
        .addTool(
            BetaManagedAgentsAgentToolset20260401Params.builder()
                .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
                .build()
        )
        .multiagent(BetaManagedAgentsMultiagentCoordinatorParams.builder()
            .type(BetaManagedAgentsMultiagentCoordinatorParams.Type.COORDINATOR)
            .addAgent(BetaManagedAgentsRosterAgentParams.builder()
                .type("agent")
                .id(reviewerAgent.id())
                .build())
            .addAgent(BetaManagedAgentsRosterAgentParams.builder()
                .type("agent")
                .id(testWriterAgent.id())
                .build())
            .build())
        .build()
);
````

  
````php
$coordinator = $client->beta->agents->create(
    name: 'Engineering Lead',
    model: 'claude-opus-4-7',
    system: 'You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.',
    tools: [
        ['type' => 'agent_toolset_20260401'],
    ],
    multiagent: [
        'type' => 'coordinator',
        'agents' => [
            ['type' => 'agent', 'id' => $reviewerAgent->id],
            ['type' => 'agent', 'id' => $testWriterAgent->id],
        ],
    ],
);
````

  
````ruby
coordinator = client.beta.agents.create(
  name: "Engineering Lead",
  model: "claude-opus-4-7",
  system: "You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.",
  tools: [
    {type: "agent_toolset_20260401"}
  ],
  multiagent: {
    type: "coordinator",
    agents: [
      {type: "agent", id: reviewer_agent.id},
      {type: "agent", id: test_writer_agent.id}
    ]
  }
)
````

</CodeGroup>

`multiagent.agents` can accept any of the following:
* `{"type": "agent", "id": agent.id}` references a previously created `agent` by ID. Defaults to pinning the latest agent version if no `version` is specified.
* `{"type": "agent", "id": agent.id, "version": agent.version}` pins a specific agent version.
* `{"type": "self"}`: allows the coordinator to spawn copies of itself.

The coordinator can only delegate to one level of agents; depth > 1 is ignored. A maximum of 20 unique agents can be listed in `multiagent.agents`, but the coordinator can call multiple copies of each agent.

## Create the session

Create a session referencing the coordinator. The coordinator will delegate to the agents in its roster as needed.

<CodeGroup>
  
````bash
session=$(curl -fsSL https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d @- <<EOF
{
  "agent": "$COORDINATOR_ID",
  "environment_id": "$ENVIRONMENT_ID"
}
EOF
)
SESSION_ID=$(jq -r '.id' <<< "$session")
````

  
````bash
ant beta:sessions create \
  --agent "$COORDINATOR_ID" \
  --environment-id "$ENVIRONMENT_ID"
````

  
````python
session = client.beta.sessions.create(
    agent=coordinator.id,
    environment_id=environment.id,
)
````

  
````typescript
const session = await client.beta.sessions.create({
  agent: coordinator.id,
  environment_id: environment.id,
});
````

  
````csharp
var session = await client.Beta.Sessions.Create(new()
{
    Agent = coordinator.ID,
    EnvironmentID = environment.ID,
});
````

  
````go
session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
	Agent: anthropic.BetaSessionNewParamsAgentUnion{
		OfString: anthropic.String(coordinator.ID),
	},
	EnvironmentID: environment.ID,
})
if err != nil {
	panic(err)
}
````

  
````java
var session = client.beta().sessions().create(SessionCreateParams.builder()
    .agent(coordinator.id())
    .environmentId(environment.id())
    .build());
````

  
````php
$session = $client->beta->sessions->create(
    agent: $coordinator->id,
    environmentID: $environment->id,
);
````

  
````ruby
session = client.beta.sessions.create(
  agent: coordinator.id,
  environment_id: environment.id
)
````

</CodeGroup>

## Threads

The **session-level event stream** (`/v1/sessions/:id/events/stream`) is considered the **primary thread**, containing a condensed view of all activity across all threads. You won't see the full activity from non-coordinator agents, but you will see the start and end of their work, as well as blocking events like tool permission requests.

**Session threads** are where you drill into a specific agent's activity.

The session `status` is an aggregation of all agent activity; if at least one thread is `running`, then the overall session status will be `running` as well.

<Note>
A maximum of 25 concurrent threads are supported. The coordinator can call multiple copies of a single agent in the roster, creating multiple threads associated with one `agent`.
</Note>

<Tabs>
  <Tab title="List threads">
List all threads associated with a session as follows:
<CodeGroup>
  
````bash
curl -fsS "https://api.anthropic.com/v1/sessions/$SESSION_ID/threads" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  | jq -r '.data[] | "[\(.agent.name)] \(.status)"'
````

  
````bash
ant beta:sessions:threads list --session-id "$SESSION_ID"
````

  
````python
for thread in client.beta.sessions.threads.list(session.id):
    print(f"[{thread.agent.name}] {thread.status}")
````

  
````typescript
for await (const thread of client.beta.sessions.threads.list(session.id)) {
  console.log(`[${thread.agent.name}] ${thread.status}`);
}
````

  
````csharp
await foreach (var thread in (await client.Beta.Sessions.Threads.List(session.ID)).Paginate())
{
    Console.WriteLine($"[{thread.Agent.Name}] {thread.Status}");
}
````

  
````go
threads := client.Beta.Sessions.Threads.ListAutoPaging(ctx, session.ID, anthropic.BetaSessionThreadListParams{})
for threads.Next() {
	thread := threads.Current()
	fmt.Printf("[%s] %s\n", thread.Agent.Name, thread.Status)
}
if err := threads.Err(); err != nil {
	panic(err)
}
````

  
````java
for (var thread : client.beta().sessions().threads().list(session.id()).autoPager()) {
    IO.println("[" + thread.agent().name() + "] " + thread.status());
}
````

  
````php
foreach ($client->beta->sessions->threads->list($session->id)->pagingEachItem() as $thread) {
    echo "[{$thread->agent->name}] {$thread->status}\n";
}
````

  
````ruby
client.beta.sessions.threads.list(session.id).auto_paging_each do |thread|
  puts "[#{thread.agent.name}] #{thread.status}"
end
````

</CodeGroup>

The full list includes the primary thread. `parent_thread_id` will be null for the primary thread.
  </Tab>

  <Tab title="Interrupt a session thread">
Send `user.interrupt` with `session_thread_id` to stop a specific thread. Omitting `session_thread_id` targets the primary thread.

<CodeGroup>
  
````bash
curl -fsS "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d "{\"events\": [{\"type\": \"user.interrupt\", \"session_thread_id\": \"$THREAD_ID\"}]}"
````

  
````bash
ant beta:sessions:events send \
  --session-id "$SESSION_ID" \
  --event "{type: user.interrupt, session_thread_id: $THREAD_ID}"
````

  
````python
client.beta.sessions.events.send(
    session.id,
    events=[{"type": "user.interrupt", "session_thread_id": thread.id}],
)
````

  
````typescript
await client.beta.sessions.events.send(session.id, {
  events: [{ type: "user.interrupt", session_thread_id: thread.id }],
});
````

  
````csharp
await client.Beta.Sessions.Events.Send(session.ID, new()
{
    Events =
    [
        new BetaManagedAgentsUserInterruptEventParams
        {
            Type = BetaManagedAgentsUserInterruptEventParamsType.UserInterrupt,
            SessionThreadID = thread.ID,
        },
    ],
});
````

  
````go
if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
	Events: []anthropic.BetaManagedAgentsEventParamsUnion{{
		OfUserInterrupt: &anthropic.BetaManagedAgentsUserInterruptEventParams{
			Type:            anthropic.BetaManagedAgentsUserInterruptEventParamsTypeUserInterrupt,
			SessionThreadID: anthropic.String(thread.ID),
		},
	}},
}); err != nil {
	panic(err)
}
````

  
````java
client.beta().sessions().events().send(
    session.id(),
    EventSendParams.builder()
        .addEvent(BetaManagedAgentsUserInterruptEventParams.builder()
            .type(BetaManagedAgentsUserInterruptEventParams.Type.USER_INTERRUPT)
            .sessionThreadId(thread.id())
            .build())
        .build());
````

  
````php
$client->beta->sessions->events->send(
    $session->id,
    events: [
        ['type' => 'user.interrupt', 'session_thread_id' => $thread->id],
    ],
);
````

  
````ruby
client.beta.sessions.events.send_(
  session.id,
  events: [{type: "user.interrupt", session_thread_id: thread.id}]
)
````

</CodeGroup>

Against a child thread blocked on `requires_action`, the interrupt marks each pending tool call denied and re-emits `session.thread_status_idle` with `stop_reason: end_turn` directly; the model is not sampled. Against a thread already at `idle`, the interrupt is a no-op.
  </Tab>

  <Tab title="Archive a session thread">
Optionally archive a session thread when it has finished its work. This frees up a thread against the 25 thread limit.

<CodeGroup>
  
````bash
curl -fsS -X POST "https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/archive" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01"
````

  
````bash
ant beta:sessions:threads archive \
  --session-id "$SESSION_ID" \
  --thread-id "$THREAD_ID"
````

  
````python
archived = client.beta.sessions.threads.archive(thread.id, session_id=session.id)
print(archived.status, archived.archived_at)
````

  
````typescript
const archived = await client.beta.sessions.threads.archive(thread.id, {
  session_id: session.id,
});
console.log(archived.status, archived.archived_at);
````

  
````csharp
var archived = await client.Beta.Sessions.Threads.Archive(thread.ID, new() { SessionID = session.ID });
Console.WriteLine($"{archived.Status} {archived.ArchivedAt}");
````

  
````go
archived, err := client.Beta.Sessions.Threads.Archive(ctx, thread.ID, anthropic.BetaSessionThreadArchiveParams{
	SessionID: session.ID,
})
if err != nil {
	panic(err)
}
fmt.Println(archived.Status, archived.ArchivedAt)
````

  
````java
var archived = client.beta().sessions().threads().archive(
    thread.id(),
    ThreadArchiveParams.builder()
        .sessionId(session.id())
        .build());
IO.println(archived.status() + " " + archived.archivedAt());
````

  
````php
$archived = $client->beta->sessions->threads->archive($thread->id, sessionID: $session->id);
echo "{$archived->status} {$archived->archivedAt->format(DATE_ATOM)}\n";
````

  
````ruby
archived = client.beta.sessions.threads.archive(thread.id, session_id: session.id)
puts "#{archived.status} #{archived.archived_at}"
````

</CodeGroup>

Archive only succeeds if the thread is `idle`. If the thread is running or blocked on `requires_action`, interrupt it first:

<CodeGroup>
  
````bash
# Interrupt the thread, then archive it
curl -fsS "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d "{\"events\": [{\"type\": \"user.interrupt\", \"session_thread_id\": \"$THREAD_ID\"}]}"

curl -fsS -X POST "https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/archive" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01"
````

  
````bash
ant beta:sessions:events send \
  --session-id "$SESSION_ID" \
  --event "{type: user.interrupt, session_thread_id: $THREAD_ID}"

ant beta:sessions:threads archive \
  --session-id "$SESSION_ID" \
  --thread-id "$THREAD_ID"
````

  
````python
client.beta.sessions.events.send(
    session.id,
    events=[{"type": "user.interrupt", "session_thread_id": thread.id}],
)
archived = client.beta.sessions.threads.archive(thread.id, session_id=session.id)
print(archived.status, archived.archived_at)
````

  
````typescript
await client.beta.sessions.events.send(session.id, {
  events: [{ type: "user.interrupt", session_thread_id: thread.id }],
});
const archived = await client.beta.sessions.threads.archive(thread.id, {
  session_id: session.id,
});
console.log(archived.status, archived.archived_at);
````

  
````csharp
await client.Beta.Sessions.Events.Send(session.ID, new()
{
    Events =
    [
        new BetaManagedAgentsUserInterruptEventParams
        {
            Type = BetaManagedAgentsUserInterruptEventParamsType.UserInterrupt,
            SessionThreadID = thread.ID,
        },
    ],
});
archived = await client.Beta.Sessions.Threads.Archive(thread.ID, new() { SessionID = session.ID });
Console.WriteLine($"{archived.Status} {archived.ArchivedAt}");
````

  
````go
if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
	Events: []anthropic.BetaManagedAgentsEventParamsUnion{{
		OfUserInterrupt: &anthropic.BetaManagedAgentsUserInterruptEventParams{
			Type:            anthropic.BetaManagedAgentsUserInterruptEventParamsTypeUserInterrupt,
			SessionThreadID: anthropic.String(thread.ID),
		},
	}},
}); err != nil {
	panic(err)
}

archived, err := client.Beta.Sessions.Threads.Archive(ctx, thread.ID, anthropic.BetaSessionThreadArchiveParams{
	SessionID: session.ID,
})
if err != nil {
	panic(err)
}
fmt.Println(archived.Status, archived.ArchivedAt)
````

  
````java
client.beta().sessions().events().send(
    session.id(),
    EventSendParams.builder()
        .addEvent(BetaManagedAgentsUserInterruptEventParams.builder()
            .type(BetaManagedAgentsUserInterruptEventParams.Type.USER_INTERRUPT)
            .sessionThreadId(thread.id())
            .build())
        .build());

archived = client.beta().sessions().threads().archive(
    thread.id(),
    ThreadArchiveParams.builder()
        .sessionId(session.id())
        .build());
IO.println(archived.status() + " " + archived.archivedAt());
````

  
````php
$client->beta->sessions->events->send(
    $session->id,
    events: [['type' => 'user.interrupt', 'session_thread_id' => $thread->id]],
);
$archived = $client->beta->sessions->threads->archive($thread->id, sessionID: $session->id);
echo "{$archived->status} {$archived->archivedAt->format(DATE_ATOM)}\n";
````

  
````ruby
client.beta.sessions.events.send_(
  session.id,
  events: [{type: "user.interrupt", session_thread_id: thread.id}]
)
archived = client.beta.sessions.threads.archive(thread.id, session_id: session.id)
puts "#{archived.status} #{archived.archived_at}"
````

</CodeGroup>
  </Tab>
</Tabs>

### Primary thread events

These events surface multiagent activity on the primary thread at `/v1/sessions/:id/events/stream`.

| Type | Description |
| --- | --- |
| `session.thread_created` | A thread was created. Includes `session_thread_id` and `agent_name`. |
| `session.thread_status_running` | A thread started activity. |
| `session.thread_status_idle` | The agent associated with the thread is awaiting input. Includes a `stop_reason` indicating why the agent stopped.  |
| `session.thread_status_terminated` | A thread was archived or encountered a terminal error. |
| `agent.thread_message_received` | An agent delivered its result to the coordinator. Includes `from_session_thread_id`, `from_agent_name`, and `content`. |
| `agent.thread_message_sent` | The coordinator sent a follow-up to another agent. Includes `to_session_thread_id`, `to_agent_name`, and `content`. |

### Session thread events
Critical events are proxied to the primary thread. However, you may still want to investigate a specific agent's reasoning and tool calls. To do so, stream or list the events from the associated session thread.

<Tabs>
  <Tab title="Stream session thread events">
<CodeGroup>
  
````bash
curl -fsSN "https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/stream?beta=true" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" |
  while IFS= read -r line; do
    [[ $line == data:* ]] || continue
    json=${line#data: }
    case $(jq -r '.type' <<<"$json") in
      agent.message)
        printf '%s' "$(jq -j '.content[] | select(.type == "text") | .text' <<<"$json")"
        ;;
      session.thread_status_idle)
        break
        ;;
    esac
  done
````

  
````bash
ant beta:sessions:threads:events stream \
  --session-id "$SESSION_ID" \
  --thread-id "$THREAD_ID"
````

  
````python
with client.beta.sessions.threads.events.stream(
    thread.id,
    session_id=session.id,
) as stream:
    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    if block.type == "text":
                        print(block.text, end="")
            case "session.thread_status_idle":
                break
````

  
````typescript
const stream = await client.beta.sessions.threads.events.stream(thread.id, {
  session_id: session.id,
});

for await (const event of stream) {
  if (event.type === "agent.message") {
    for (const block of event.content) {
      if (block.type === "text") {
        process.stdout.write(block.text);
      }
    }
  } else if (event.type === "session.thread_status_idle") {
    break;
  }
}
````

  
````csharp
await foreach (var evt in client.Beta.Sessions.Threads.Events.StreamStreaming(thread.ID, new() { SessionID = session.ID }))
{
    if (evt.Value is BetaManagedAgentsAgentMessageEvent message)
    {
        foreach (var block in message.Content)
        {
            if (block.Type == "text")
            {
                Console.Write(block.Text);
            }
        }
    }
    else if (evt.Value is BetaManagedAgentsSessionThreadStatusIdleEvent)
    {
        break;
    }
}
````

  
````go
	stream := client.Beta.Sessions.Threads.Events.StreamEvents(ctx, thread.ID, anthropic.BetaSessionThreadEventStreamParams{
		SessionID: session.ID,
	})
	defer stream.Close()

loop:
	for stream.Next() {
		event := stream.Current()
		switch event.Type {
		case "agent.message":
			for _, block := range event.AsAgentMessage().Content {
				if block.Type == "text" {
					fmt.Print(block.Text)
				}
			}
		case "session.thread_status_idle":
			break loop
		}
	}
	if err := stream.Err(); err != nil {
		panic(err)
	}
````

  
````java
try (var streamResponse = client.beta().sessions().threads().events().streamStreaming(
    thread.id(),
    ThreadStreamParams.builder().sessionId(session.id()).build()
)) {
    for (var event : (Iterable<StreamEvents>) streamResponse.stream()::iterator) {
        if (event.isAgentMessage()) {
            for (var block : event.asAgentMessage().content()) {
                IO.print(block.text());
            }
        } else if (event.isSessionThreadStatusIdle()) {
            break;
        }
    }
}
````

  
````php
$stream = $client->beta->sessions->threads->events->streamStream(
    $thread->id,
    sessionID: $session->id,
);

foreach ($stream as $event) {
    if ($event->type === 'agent.message') {
        foreach ($event->content as $block) {
            if ($block->type === 'text') {
                echo $block->text;
            }
        }
    } elseif ($event->type === 'session.thread_status_idle') {
        break;
    }
}
````

  
````ruby
client.beta.sessions.threads.events.stream_events(thread.id, session_id: session.id).each do |event|
  case event.type
  when :"agent.message"
    event.content.each do |block|
      print block.text if block.type == :text
    end
  when :"session.thread_status_idle"
    break
  end
end
````

</CodeGroup>
  </Tab>

  <Tab title="List session thread events">
List all past session thread events to pull a complete history.

<CodeGroup>
  
````bash
curl -fsS "https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID/events" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  | jq -r '.data[] | "[\(.type)] \(.processed_at)"'
````

  
````bash
ant beta:sessions:threads:events list \
  --session-id "$SESSION_ID" \
  --thread-id "$THREAD_ID"
````

  
````python
for event in client.beta.sessions.threads.events.list(
    thread.id,
    session_id=session.id,
):
    print(f"[{event.type}] {event.processed_at}")
````

  
````typescript
for await (const event of client.beta.sessions.threads.events.list(thread.id, {
  session_id: session.id,
})) {
  console.log(`[${event.type}] ${event.processed_at}`);
}
````

  
````csharp
var page = await client.Beta.Sessions.Threads.Events.List(thread.ID, new() { SessionID = session.ID });
await foreach (var evt in page.Paginate())
{
    Console.WriteLine($"[{evt.Type}] {evt.ProcessedAt}");
}
````

  
````go
pager := client.Beta.Sessions.Threads.Events.ListAutoPaging(ctx, thread.ID, anthropic.BetaSessionThreadEventListParams{
	SessionID: session.ID,
})
for pager.Next() {
	event := pager.Current()
	fmt.Printf("[%s] %s\n", event.Type, event.ProcessedAt)
}
if err := pager.Err(); err != nil {
	panic(err)
}
````

  
````java
for (var event : client.beta().sessions().threads().events().list(
        thread.id(),
        EventListParams.builder().sessionId(session.id()).build()
    ).autoPager()) {
    IO.println("[" + event.type() + "] " + event.processedAt());
}
````

  
````php
foreach (
    $client->beta->sessions->threads->events->list(
        $thread->id,
        sessionID: $session->id,
    )->pagingEachItem() as $event
) {
    echo "[{$event->type}] {$event->processedAt->format(DATE_RFC3339)}\n";
}
````

  
````ruby
client.beta.sessions.threads.events.list(
  thread.id,
  session_id: session.id
).auto_paging_each do |event|
  puts "[#{event.type}] #{event.processed_at}"
end
````

</CodeGroup>
  </Tab>
</Tabs>

### Tool permissions and custom tools

If a non-coordinator agent needs something from your client, such as [permission](/docs/en/managed-agents/events-and-streaming#tool-confirmation) to run an `always_ask` tool, or the [result of a custom tool](/docs/en/managed-agents/events-and-streaming#handling-custom-tool-calls), the event is cross-posted to the **primary thread** with `session_thread_id` identifying the originating session thread.

```json
{
  "type": "session.thread_status_idle",
  "id": "sevt_01ABC...",
  "session_thread_id": "sth_01DEF...",
  "agent_name": "code-reviewer",
  "stop_reason": {
    "type": "requires_action",
    "event_ids": ["toolu_01XYZ..."]
  }
}
```

Post `user.tool_confirmation` (with `tool_use_id`) or `user.custom_tool_result` (with `custom_tool_use_id`); the server routes the response to the correct thread automatically.

The example below extends the [tool confirmation handler](/docs/en/managed-agents/events-and-streaming#tool-confirmation) to route replies. The same pattern applies to `user.custom_tool_result`.

<CodeGroup>
  
````bash
while IFS= read -r event_id; do
  jq -n --arg id "$event_id" \
    '{events: [{type: "user.tool_confirmation", tool_use_id: $id, result: "allow"}]}' |
    curl -fsS "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: managed-agents-2026-04-01" \
      -H "content-type: application/json" \
      -d @-
done < <(jq -r '.stop_reason.event_ids[]' <<<"$data")
````

  
````bash
# This workflow does not translate well to a one-off shell command.
# Use one of the SDK examples in this code group instead.
````

  
````python
for event_id in stop.event_ids:
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.tool_confirmation",
                "tool_use_id": event_id,
                "result": "allow",
            }
        ],
    )
````

  
````typescript
for (const eventId of stop.event_ids) {
  await client.beta.sessions.events.send(session.id, {
    events: [
      {
        type: "user.tool_confirmation",
        tool_use_id: eventId,
        result: "allow",
      },
    ],
  });
}
````

  
````csharp
foreach (var eventId in requiresAction.EventIds)
{
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
````

  
````go
for _, eventID := range stopReason.EventIDs {
	params := anthropic.BetaManagedAgentsUserToolConfirmationEventParams{
		Type:      anthropic.BetaManagedAgentsUserToolConfirmationEventParamsTypeUserToolConfirmation,
		ToolUseID: eventID,
		Result:    anthropic.BetaManagedAgentsUserToolConfirmationEventParamsResultAllow,
	}
	if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
		Events: []anthropic.BetaManagedAgentsEventParamsUnion{{OfUserToolConfirmation: &params}},
	}); err != nil {
		panic(err)
	}
}
````

  
````java
for (var eventId : pendingToolUseIds) {
    client.beta().sessions().events().send(
        session.id(),
        EventSendParams.builder()
            .addEvent(BetaManagedAgentsUserToolConfirmationEventParams.builder()
                .toolUseId(eventId)
                .result(BetaManagedAgentsUserToolConfirmationEventParams.Result.ALLOW)
                .build())
            .build()
    );
}
````

  
````php
foreach ($event->stopReason->eventIDs as $eventId) {
    $client->beta->sessions->events->send($session->id, events: [[
        'type' => 'user.tool_confirmation',
        'tool_use_id' => $eventId,
        'result' => 'allow',
    ]]);
}
````

  
````ruby
event_ids.each do |event_id|
  client.beta.sessions.events.send_(session.id, events: [{
    type: "user.tool_confirmation",
    tool_use_id: event_id,
    result: "allow"
  }])
end
````

</CodeGroup>
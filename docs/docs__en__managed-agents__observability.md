# Session tracing

Monitor and debug your sessions using the Console timeline and raw event views.

---

Claude Managed Agents provides observability tools in the [Claude Console](/) to help you monitor, debug, and understand your agent sessions.

## Console observability

The Console provides a visual timeline view of your agent sessions. Navigate to the Claude Managed Agents section in the Console to see:

- **Session list** - All sessions with their status, creation time, and model
- **Tracing view** - A chronological view of events (content, timestamps, token usage) within a session. These are only accessible to Developers and Admins.
- **Tool execution** - Details of each tool call and its result

## Raw events

For programmatic debugging, retrieve raw events via the API:

<CodeGroup>

```bash curl
curl -fsSL "https://api.anthropic.com/v1/sessions/$SESSION_ID/events" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
| jq -r '
  .data[]
  | "Type: \(.type)",
    "Processed: \(.processed_at)",
    ( if .type | IN("user.message", "agent.message") then
        .content[]
        | "  Block: \(.type)",
          (select(.type == "text") | "  Text: \(.text[:100])...")
      elif .type | IN("agent.tool_use", "agent.custom_tool_use", "agent.mcp_tool_use") then
        "  Tool: \(.name)"
      else empty end ),
    "---"
'
```

```bash CLI nocheck
ant beta:sessions:events list --session-id "$SESSION_ID"
```

```python Python
events = client.beta.sessions.events.list(session.id)

for event in events:
    print(f"Type: {event.type}")
    print(f"Processed: {event.processed_at}")
    match event.type:
        case "user.message" | "agent.message":
            for block in event.content:
                print(f"  Block: {block.type}")
                if block.type == "text":
                    print(f"  Text: {block.text[:100]}...")
        case "agent.tool_use" | "agent.custom_tool_use" | "agent.mcp_tool_use":
            print(f"  Tool: {event.name}")
    print("---")
```

```typescript TypeScript
for await (const event of client.beta.sessions.events.list(session.id)) {
  console.log(`Type: ${event.type}`);
  console.log(`Processed: ${event.processed_at}`);
  switch (event.type) {
    case "user.message":
    case "agent.message":
      for (const block of event.content) {
        console.log(`  Block: ${block.type}`);
        if (block.type === "text") {
          console.log(`  Text: ${block.text.slice(0, 100)}...`);
        }
      }
      break;
    case "agent.tool_use":
    case "agent.custom_tool_use":
    case "agent.mcp_tool_use":
      console.log(`  Tool: ${event.name}`);
      break;
  }
  console.log("---");
}
```

```csharp C#
var events = await client.Beta.Sessions.Events.List(session.ID);

await foreach (var evt in events.Paginate())
{
    Console.WriteLine($"Type: {evt.Json.GetProperty("type").GetString()}");
    Console.WriteLine($"Processed: {evt.ProcessedAt}");
    switch (evt.Value)
    {
        case BetaManagedAgentsUserMessageEvent userMessage:
            foreach (var block in userMessage.Content)
            {
                Console.WriteLine($"  Block: {block.Json.GetProperty("type").GetString()}");
                if (block.Value is BetaManagedAgentsTextBlock textBlock)
                {
                    Console.WriteLine($"  Text: {textBlock.Text[..Math.Min(100, textBlock.Text.Length)]}...");
                }
            }
            break;
        case BetaManagedAgentsAgentMessageEvent agentMessage:
            foreach (var block in agentMessage.Content)
            {
                Console.WriteLine($"  Block: {block.Type.Raw()}");
                Console.WriteLine($"  Text: {block.Text[..Math.Min(100, block.Text.Length)]}...");
            }
            break;
        case BetaManagedAgentsAgentToolUseEvent or BetaManagedAgentsAgentCustomToolUseEvent or BetaManagedAgentsAgentMcpToolUseEvent:
            Console.WriteLine($"  Tool: {evt.Name}");
            break;
    }
    Console.WriteLine("---");
}
```

```go Go
events := client.Beta.Sessions.Events.ListAutoPaging(ctx, session.ID, anthropic.BetaSessionEventListParams{})

for events.Next() {
	event := events.Current()
	fmt.Printf("Type: %s\n", event.Type)
	fmt.Printf("Processed: %s\n", event.ProcessedAt)
	switch event.Type {
	case "user.message":
		for _, block := range event.AsUserMessage().Content {
			fmt.Printf("  Block: %s\n", block.Type)
			if block.Type == "text" {
				fmt.Printf("  Text: %s...\n", block.Text[:min(100, len(block.Text))])
			}
		}
	case "agent.message":
		for _, block := range event.AsAgentMessage().Content {
			fmt.Printf("  Block: %s\n", block.Type)
			if block.Type == "text" {
				fmt.Printf("  Text: %s...\n", block.Text[:min(100, len(block.Text))])
			}
		}
	case "agent.tool_use", "agent.custom_tool_use", "agent.mcp_tool_use":
		fmt.Printf("  Tool: %s\n", event.Name)
	}
	fmt.Println("---")
}
if err := events.Err(); err != nil {
	panic(err)
}
```

```java Java
var events = client.beta().sessions().events()
    .list(EventListParams.builder().sessionId(session.id()).build());

for (var event : events.autoPager()) {
    var json = (Map<String, JsonValue>) event._json().orElseThrow().asObject().orElseThrow();
    var type = json.get("type").asStringOrThrow();
    IO.println("Type: " + type);
    IO.println("Processed: " + json.get("processed_at"));
    if (event.isUserMessage() || event.isAgentMessage()) {
        for (var block : (List<JsonValue>) json.get("content").asArray().orElseThrow()) {
            var blockJson = (Map<String, JsonValue>) block.asObject().orElseThrow();
            var blockType = blockJson.get("type").asStringOrThrow();
            IO.println("  Block: " + blockType);
            if (blockType.equals("text")) {
                var text = blockJson.get("text").asStringOrThrow();
                IO.println("  Text: " + text.substring(0, Math.min(100, text.length())) + "...");
            }
        }
    } else if (event.isAgentToolUse() || event.isAgentCustomToolUse() || event.isAgentMcpToolUse()) {
        IO.println("  Tool: " + json.get("name").asStringOrThrow());
    }
    IO.println("---");
}
```

```php PHP
foreach ($client->beta->sessions->events->list($session->id)->pagingEachItem() as $event) {
    echo "Type: {$event->type}\n";
    $processedAt = ($event->processedAt ?? null)?->format(DATE_RFC3339) ?? 'pending';
    echo "Processed: {$processedAt}\n";
    if (in_array($event->type, ['user.message', 'agent.message'], true)) {
        foreach ($event->content as $block) {
            echo "  Block: {$block->type}\n";
            if ($block->type === 'text') {
                echo '  Text: ' . mb_substr($block->text, 0, 100) . "...\n";
            }
        }
    } elseif (in_array($event->type, ['agent.tool_use', 'agent.custom_tool_use', 'agent.mcp_tool_use'], true)) {
        echo "  Tool: {$event->name}\n";
    }
    echo "---\n";
}
```

```ruby Ruby
client.beta.sessions.events.list(session.id).auto_paging_each do |event|
  puts "Type: #{event.type}"
  puts "Processed: #{event.processed_at}"
  case event.type
  when :"user.message", :"agent.message"
    event.content.each do |block|
      puts "  Block: #{block.type}"
      puts "  Text: #{block.text[0, 100]}..." if block.type == :text
    end
  when :"agent.tool_use", :"agent.custom_tool_use", :"agent.mcp_tool_use"
    puts "  Tool: #{event.name}"
  end
  puts "---"
end
```
</CodeGroup>

Use the same event stream to surface errors and track token consumption:

<CodeGroup>

```bash curl
curl -fsSL "https://api.anthropic.com/v1/sessions/$SESSION_ID/events" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
| jq -r '
  (.data[] | select(.type == "session.error") | "[\(.error.type)] \(.error.message)"),
  (reduce (.data[] | select(.type == "span.model_request_end") | .model_usage) as $u
     ({input: 0, output: 0}; .input += $u.input_tokens | .output += $u.output_tokens)
   | "Total input tokens: \(.input), output tokens: \(.output)")
'
```

```bash CLI nocheck
ant beta:sessions:events list \
  --session-id "$SESSION_ID" \
  --format jsonl \
| jq -sr '
  (.[] | select(.type == "session.error") | "[\(.error.type)] \(.error.message)"),
  (reduce (.[] | select(.type == "span.model_request_end") | .model_usage) as $u
     ({input: 0, output: 0}; .input += $u.input_tokens | .output += $u.output_tokens)
   | "Total input tokens: \(.input), output tokens: \(.output)")
'
```

```python Python
events = client.beta.sessions.events.list(session.id)

input_tokens, output_tokens = 0, 0
for event in events:
    match event.type:
        case "session.error":
            print(f"[{event.error.type}] {event.error.message}")
        case "span.model_request_end":
            input_tokens += event.model_usage.input_tokens
            output_tokens += event.model_usage.output_tokens

print(f"Total input tokens: {input_tokens}, output tokens: {output_tokens}")
```

```typescript TypeScript
let inputTokens = 0;
let outputTokens = 0;
for await (const event of client.beta.sessions.events.list(session.id)) {
  switch (event.type) {
    case "session.error":
      console.log(`[${event.error?.type}] ${event.error?.message}`);
      break;
    case "span.model_request_end":
      inputTokens += event.model_usage.input_tokens;
      outputTokens += event.model_usage.output_tokens;
      break;
  }
}

console.log(`Total input tokens: ${inputTokens}, output tokens: ${outputTokens}`);
```

```csharp C#
var events = await client.Beta.Sessions.Events.List(session.ID);

var inputTokens = 0;
var outputTokens = 0;
await foreach (var evt in events.Paginate())
{
    switch (evt.Value)
    {
        case BetaManagedAgentsSessionErrorEvent { Error: { } error }:
            Console.WriteLine($"[{error.Json.GetProperty("type").GetString()}] {error.Message}");
            break;
        case BetaManagedAgentsSpanModelRequestEndEvent spanEnd:
            inputTokens += spanEnd.ModelUsage.InputTokens;
            outputTokens += spanEnd.ModelUsage.OutputTokens;
            break;
    }
}

Console.WriteLine($"Total input tokens: {inputTokens}, output tokens: {outputTokens}");
```

```go Go
events := client.Beta.Sessions.Events.ListAutoPaging(ctx, session.ID, anthropic.BetaSessionEventListParams{})

var inputTokens, outputTokens int64
for events.Next() {
	event := events.Current()
	switch event.Type {
	case "session.error":
		e := event.AsSessionError().Error
		fmt.Printf("[%s] %s\n", e.Type, e.Message)
	case "span.model_request_end":
		usage := event.AsSpanModelRequestEnd().ModelUsage
		inputTokens += usage.InputTokens
		outputTokens += usage.OutputTokens
	}
}
if err := events.Err(); err != nil {
	panic(err)
}

fmt.Printf("Total input tokens: %d, output tokens: %d\n", inputTokens, outputTokens)
```

```java Java
var events = client.beta().sessions().events()
    .list(EventListParams.builder().sessionId(session.id()).build());

var inputTokens = 0;
var outputTokens = 0;
for (var event : events.autoPager()) {
    if (event.isError()) {
        var json = (Map<String, JsonValue>) event._json().orElseThrow().asObject().orElseThrow();
        var error = (Map<String, JsonValue>) json.get("error").asObject().orElseThrow();
        IO.println("[" + error.get("type").asStringOrThrow() + "] "
            + error.get("message").asStringOrThrow());
    } else if (event.isSpanModelRequestEnd()) {
        var usage = event.asSpanModelRequestEnd().modelUsage();
        inputTokens += usage.inputTokens();
        outputTokens += usage.outputTokens();
    }
}

IO.println("Total input tokens: " + inputTokens + ", output tokens: " + outputTokens);
```

```php PHP
$inputTokens = 0;
$outputTokens = 0;
foreach ($client->beta->sessions->events->list($session->id)->pagingEachItem() as $event) {
    match ($event->type) {
        'session.error' => printf("[%s] %s\n", $event->error->type, $event->error->message),
        'span.model_request_end' => [
            $inputTokens += $event->modelUsage->inputTokens,
            $outputTokens += $event->modelUsage->outputTokens,
        ],
        default => null,
    };
}

echo "Total input tokens: {$inputTokens}, output tokens: {$outputTokens}\n";
```

```ruby Ruby
input_tokens, output_tokens = 0, 0
client.beta.sessions.events.list(session.id).auto_paging_each do |event|
  case event.type
  when :"session.error"
    puts "[#{event.error.type}] #{event.error.message}"
  when :"span.model_request_end"
    input_tokens += event.model_usage.input_tokens
    output_tokens += event.model_usage.output_tokens
  end
end

puts "Total input tokens: #{input_tokens}, output tokens: #{output_tokens}"
```
</CodeGroup>

## Debugging tips

- **Check session events** - Session errors are conveyed through the `session.error` event
- **Review tool results** - Tool execution failures often explain unexpected agent behavior
- **Track token usage** - Monitor token consumption to optimize prompts and reduce costs
- **Use system prompts** - Add logging instructions to the system prompt to make the agent explain its reasoning
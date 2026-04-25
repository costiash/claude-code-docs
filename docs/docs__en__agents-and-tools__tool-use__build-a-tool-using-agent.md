# Tutorial: Build a tool-using agent

A guided walkthrough from a single tool call to a production-ready agentic loop.

---

This tutorial builds a calendar-management agent in five concentric rings. Each ring is a complete, runnable program that adds exactly one concept to the ring before it. By the end you will have written the agentic loop by hand and then replaced it with the Tool Runner SDK abstraction.

The example tool is `create_calendar_event`. Its schema uses nested objects, arrays, and optional fields, so you will see how Claude handles realistic input shapes rather than a single flat string.

<Note>
Every ring runs standalone. Copy any ring into a fresh file and it will execute without the code from earlier rings.
</Note>

## Ring 1: Single tool, single turn

The smallest possible tool-using program: one tool, one user message, one tool call, one result. The code is heavily commented so you can map each line to the [tool use lifecycle](/docs/en/agents-and-tools/tool-use/how-tool-use-works).

The request sends a `tools` array alongside the user message. When Claude decides to call a tool, the response comes back with `stop_reason: "tool_use"` and a `tool_use` content block containing the tool name, a unique `id`, and the structured `input`. Your code executes the tool, then sends the result back in a `tool_result` block whose `tool_use_id` matches the `id` from the call.

<CodeGroup>
  
````bash
#!/bin/bash
# Ring 1: Single tool, single turn.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.

# Define one tool as a JSON fragment. The input_schema is a JSON Schema
# object describing the arguments Claude should pass when it calls this
# tool. This schema includes nested objects (recurrence), arrays
# (attendees), and optional fields, which is closer to real-world tools
# than a flat string argument.
TOOLS='[
  {
    "name": "create_calendar_event",
    "description": "Create a calendar event with attendees and optional recurrence.",
    "input_schema": {
      "type": "object",
      "properties": {
        "title": {"type": "string"},
        "start": {"type": "string", "format": "date-time"},
        "end": {"type": "string", "format": "date-time"},
        "attendees": {
          "type": "array",
          "items": {"type": "string", "format": "email"}
        },
        "recurrence": {
          "type": "object",
          "properties": {
            "frequency": {"enum": ["daily", "weekly", "monthly"]},
            "count": {"type": "integer", "minimum": 1}
          }
        }
      },
      "required": ["title", "start", "end"]
    }
  }
]'

USER_MSG="Schedule a 30-minute sync with alice@example.com and bob@example.com next Monday at 10am."

# Send the user's request along with the tool definition. Claude decides
# whether to call the tool based on the request and the tool description.
RESPONSE=$(curl -s https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d "$(jq -n \
    --argjson tools "$TOOLS" \
    --arg msg "$USER_MSG" \
    '{
      model: "claude-opus-4-6",
      max_tokens: 1024,
      tools: $tools,
      tool_choice: {type: "auto", disable_parallel_tool_use: true},
      messages: [{role: "user", content: $msg}]
    }')")

# When Claude calls a tool, the response has stop_reason "tool_use"
# and the content array contains a tool_use block alongside any text.
echo "stop_reason: $(echo "$RESPONSE" | jq -r '.stop_reason')"

# Find the tool_use block. A response may contain text blocks before the
# tool_use block, so filter by type rather than assuming position.
TOOL_USE=$(echo "$RESPONSE" | jq '.content[] | select(.type == "tool_use")')
TOOL_USE_ID=$(echo "$TOOL_USE" | jq -r '.id')
echo "Tool: $(echo "$TOOL_USE" | jq -r '.name')"
echo "Input: $(echo "$TOOL_USE" | jq -c '.input')"

# Execute the tool. In a real system this would call your calendar API.
# Here the result is hardcoded to keep the example self-contained.
RESULT='{"event_id": "evt_123", "status": "created"}'

# Send the result back. The tool_result block goes in a user message and
# its tool_use_id must match the id from the tool_use block above. The
# assistant's previous response is included so Claude has the full history.
ASSISTANT_CONTENT=$(echo "$RESPONSE" | jq '.content')
FOLLOWUP=$(curl -s https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d "$(jq -n \
    --argjson tools "$TOOLS" \
    --arg msg "$USER_MSG" \
    --argjson assistant "$ASSISTANT_CONTENT" \
    --arg tool_use_id "$TOOL_USE_ID" \
    --arg result "$RESULT" \
    '{
      model: "claude-opus-4-6",
      max_tokens: 1024,
      tools: $tools,
      tool_choice: {type: "auto", disable_parallel_tool_use: true},
      messages: [
        {role: "user", content: $msg},
        {role: "assistant", content: $assistant},
        {role: "user", content: [
          {type: "tool_result", tool_use_id: $tool_use_id, content: $result}
        ]}
      ]
    }')")

# With the tool result in hand, Claude produces a final natural-language
# answer and stop_reason becomes "end_turn".
echo "stop_reason: $(echo "$FOLLOWUP" | jq -r '.stop_reason')"
echo "$FOLLOWUP" | jq -r '.content[] | select(.type == "text") | .text'
````

  
````bash
#!/usr/bin/env bash
# Ring 1: Single tool, single turn.
# Uses jq for cross-turn message-array state — building an agentic loop in shell
# requires JSON manipulation beyond ant's single-call --transform scope.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.
set -euo pipefail

USER_MSG="Schedule a 30-minute sync with alice@example.com and bob@example.com next Monday at 10am."
MESSAGES=$(jq -n --arg msg "$USER_MSG" '[{role: "user", content: $msg}]')

# Define one tool. The input_schema is a JSON Schema object describing
# the arguments Claude should pass when it calls this tool. This schema
# includes nested objects (recurrence), arrays (attendees), and optional
# fields, which is closer to real-world tools than a flat string argument.
call_api() {
  # ant reads the request body as YAML on stdin: no auth headers, no
  # hand-built JSON envelope. The static keys (model, tools, tool_choice)
  # live in a quoted heredoc; the growing messages array is appended as
  # JSON, which YAML accepts as flow syntax.
  {
    cat <<'YAML'
model: claude-opus-4-6
max_tokens: 1024
tool_choice: {type: auto, disable_parallel_tool_use: true}
tools:
  - name: create_calendar_event
    description: Create a calendar event with attendees and optional recurrence.
    input_schema:
      type: object
      properties:
        title: {type: string}
        start: {type: string, format: date-time}
        end: {type: string, format: date-time}
        attendees:
          type: array
          items: {type: string, format: email}
        recurrence:
          type: object
          properties:
            frequency: {enum: [daily, weekly, monthly]}
            count: {type: integer, minimum: 1}
      required: [title, start, end]
YAML
    printf 'messages: %s\n' "$MESSAGES"
  } | ant messages create --format json
}

# Send the user's request along with the tool definition. Claude decides
# whether to call the tool based on the request and the tool description.
RESPONSE=$(call_api)

# When Claude calls a tool, the response has stop_reason "tool_use"
# and the content array contains a tool_use block alongside any text.
echo "stop_reason: $(jq -r '.stop_reason' <<<"$RESPONSE")"

# Find the tool_use block. A response may contain text blocks before the
# tool_use block, so filter by type rather than assuming position.
TOOL_USE=$(jq '.content[] | select(.type == "tool_use")' <<<"$RESPONSE")
TOOL_USE_ID=$(jq -r '.id' <<<"$TOOL_USE")
echo "Tool: $(jq -r '.name' <<<"$TOOL_USE")"
echo "Input: $(jq -c '.input' <<<"$TOOL_USE")"

# Execute the tool. In a real system this would call your calendar API.
# Here the result is hardcoded to keep the example self-contained.
RESULT='{"event_id": "evt_123", "status": "created"}'

# Send the result back. The tool_result block goes in a user message and
# its tool_use_id must match the id from the tool_use block above. The
# assistant's previous response is included so Claude has the full history.
MESSAGES=$(jq \
  --argjson assistant "$(jq '.content' <<<"$RESPONSE")" \
  --arg tool_use_id "$TOOL_USE_ID" \
  --arg result "$RESULT" \
  '. + [
    {role: "assistant", content: $assistant},
    {role: "user", content: [
      {type: "tool_result", tool_use_id: $tool_use_id, content: $result}
    ]}
  ]' <<<"$MESSAGES")

FOLLOWUP=$(call_api)

# With the tool result in hand, Claude produces a final natural-language
# answer and stop_reason becomes "end_turn".
echo "stop_reason: $(jq -r '.stop_reason' <<<"$FOLLOWUP")"
jq -r '.content[] | select(.type == "text") | .text' <<<"$FOLLOWUP"
````

  
````python
# Ring 1: Single tool, single turn.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.

import json

import anthropic

# Create a client. It reads ANTHROPIC_API_KEY from the environment.
client = anthropic.Anthropic()

# Define one tool. The input_schema is a JSON Schema object describing
# the arguments Claude should pass when it calls this tool. This schema
# includes nested objects (recurrence), arrays (attendees), and optional
# fields, which is closer to real-world tools than a flat string argument.
tools = [
    {
        "name": "create_calendar_event",
        "description": "Create a calendar event with attendees and optional recurrence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string", "format": "date-time"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                },
                "recurrence": {
                    "type": "object",
                    "properties": {
                        "frequency": {"enum": ["daily", "weekly", "monthly"]},
                        "count": {"type": "integer", "minimum": 1},
                    },
                },
            },
            "required": ["title", "start", "end"],
        },
    }
]

# Send the user's request along with the tool definition. Claude decides
# whether to call the tool based on the request and the tool description.
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=[
        {
            "role": "user",
            "content": "Schedule a 30-minute sync with alice@example.com and bob@example.com next Monday at 10am.",
        }
    ],
)

# When Claude calls a tool, the response has stop_reason "tool_use"
# and the content array contains a tool_use block alongside any text.
print(f"stop_reason: {response.stop_reason}")

# Find the tool_use block. A response may contain text blocks before the
# tool_use block, so scan the content array rather than assuming position.
tool_use = next(block for block in response.content if block.type == "tool_use")
print(f"Tool: {tool_use.name}")
print(f"Input: {tool_use.input}")

# Execute the tool. In a real system this would call your calendar API.
# Here the result is hardcoded to keep the example self-contained.
result = {"event_id": "evt_123", "status": "created"}

# Send the result back. The tool_result block goes in a user message and
# its tool_use_id must match the id from the tool_use block above. The
# assistant's previous response is included so Claude has the full history.
followup = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=[
        {
            "role": "user",
            "content": "Schedule a 30-minute sync with alice@example.com and bob@example.com next Monday at 10am.",
        },
        {"role": "assistant", "content": response.content},
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": json.dumps(result),
                }
            ],
        },
    ],
)

# With the tool result in hand, Claude produces a final natural-language
# answer and stop_reason becomes "end_turn".
print(f"stop_reason: {followup.stop_reason}")
final_text = next(block for block in followup.content if block.type == "text")
print(final_text.text)
````

  
````typescript
// Ring 1: Single tool, single turn.
// Source for <CodeSource> in build-a-tool-using-agent.mdx.

import Anthropic from "@anthropic-ai/sdk";

// Create a client. It reads ANTHROPIC_API_KEY from the environment.
const client = new Anthropic();

// Define one tool. The input_schema is a JSON Schema object describing
// the arguments Claude should pass when it calls this tool. This schema
// includes nested objects (recurrence), arrays (attendees), and optional
// fields, which is closer to real-world tools than a flat string argument.
const tools: Anthropic.Tool[] = [
  {
    name: "create_calendar_event",
    description:
      "Create a calendar event with attendees and optional recurrence.",
    input_schema: {
      type: "object",
      properties: {
        title: { type: "string" },
        start: { type: "string", format: "date-time" },
        end: { type: "string", format: "date-time" },
        attendees: {
          type: "array",
          items: { type: "string", format: "email" },
        },
        recurrence: {
          type: "object",
          properties: {
            frequency: { enum: ["daily", "weekly", "monthly"] },
            count: { type: "integer", minimum: 1 },
          },
        },
      },
      required: ["title", "start", "end"],
    },
  },
];

// Send the user's request along with the tool definition. Claude decides
// whether to call the tool based on the request and the tool description.
const response = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  tools,
  tool_choice: { type: "auto", disable_parallel_tool_use: true },
  messages: [
    {
      role: "user",
      content:
        "Schedule a 30-minute sync with alice@example.com and bob@example.com next Monday at 10am.",
    },
  ],
});

// When Claude calls a tool, the response has stop_reason "tool_use"
// and the content array contains a tool_use block alongside any text.
console.log(`stop_reason: ${response.stop_reason}`);

// Find the tool_use block. A response may contain text blocks before the
// tool_use block, so scan the content array rather than assuming position.
const toolUse = response.content.find(
  (block): block is Anthropic.ToolUseBlock => block.type === "tool_use",
)!;
console.log(`Tool: ${toolUse.name}`);
console.log(`Input: ${JSON.stringify(toolUse.input)}`);

// Execute the tool. In a real system this would call your calendar API.
// Here the result is hardcoded to keep the example self-contained.
const result = { event_id: "evt_123", status: "created" };

// Send the result back. The tool_result block goes in a user message and
// its tool_use_id must match the id from the tool_use block above. The
// assistant's previous response is included so Claude has the full history.
const followup = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  tools,
  tool_choice: { type: "auto", disable_parallel_tool_use: true },
  messages: [
    {
      role: "user",
      content:
        "Schedule a 30-minute sync with alice@example.com and bob@example.com next Monday at 10am.",
    },
    { role: "assistant", content: response.content },
    {
      role: "user",
      content: [
        {
          type: "tool_result",
          tool_use_id: toolUse.id,
          content: JSON.stringify(result),
        },
      ],
    },
  ],
});

// With the tool result in hand, Claude produces a final natural-language
// answer and stop_reason becomes "end_turn".
console.log(`stop_reason: ${followup.stop_reason}`);
for (const block of followup.content) {
  if (block.type === "text") {
    console.log(block.text);
  }
}
````

</CodeGroup>

**What to expect**

```text Output
stop_reason: tool_use
Tool: create_calendar_event
Input: {'title': 'Sync', 'start': '2026-03-30T10:00:00', 'end': '2026-03-30T10:30:00', 'attendees': ['alice@example.com', 'bob@example.com']}
stop_reason: end_turn
I've scheduled your 30-minute sync with Alice and Bob for next Monday at 10am.
```

The first `stop_reason` is `tool_use` because Claude is waiting for the calendar result. After you send the result, the second `stop_reason` is `end_turn` and the content is natural language for the user.

## Ring 2: The agentic loop

Ring 1 assumed Claude would call the tool exactly once. Real tasks often need several calls: Claude might create an event, read the confirmation, then create another. The fix is a `while` loop that keeps running tools and feeding results back until `stop_reason` is no longer `"tool_use"`.

The other change is conversation history. Instead of rebuilding the `messages` array from scratch on each request, keep a running list and append to it. Every turn sees the complete prior context.

<CodeGroup>
  
````bash
#!/bin/bash
# Ring 2: The agentic loop.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.

TOOLS='[
  {
    "name": "create_calendar_event",
    "description": "Create a calendar event with attendees and optional recurrence.",
    "input_schema": {
      "type": "object",
      "properties": {
        "title": {"type": "string"},
        "start": {"type": "string", "format": "date-time"},
        "end": {"type": "string", "format": "date-time"},
        "attendees": {"type": "array", "items": {"type": "string", "format": "email"}},
        "recurrence": {
          "type": "object",
          "properties": {
            "frequency": {"enum": ["daily", "weekly", "monthly"]},
            "count": {"type": "integer", "minimum": 1}
          }
        }
      },
      "required": ["title", "start", "end"]
    }
  }
]'

run_tool() {
  local name="$1"
  local input="$2"
  if [ "$name" = "create_calendar_event" ]; then
    local title=$(echo "$input" | jq -r '.title')
    jq -n --arg title "$title" '{event_id: "evt_123", status: "created", title: $title}'
  else
    echo "{\"error\": \"Unknown tool: $name\"}"
  fi
}

# Keep the full conversation history in a JSON array so each turn sees prior context.
MESSAGES='[{"role": "user", "content": "Schedule a weekly team standup every Monday at 9am for the next 4 weeks. Invite the whole team: alice@example.com, bob@example.com, carol@example.com."}]'

call_api() {
  curl -s https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d "$(jq -n --argjson tools "$TOOLS" --argjson messages "$MESSAGES" \
      '{model: "claude-opus-4-6", max_tokens: 1024, tools: $tools, tool_choice: {type: "auto", disable_parallel_tool_use: true}, messages: $messages}')"
}

RESPONSE=$(call_api)

# Loop until Claude stops asking for tools. Each iteration runs the requested
# tool, appends the result to history, and asks Claude to continue.
while [ "$(echo "$RESPONSE" | jq -r '.stop_reason')" = "tool_use" ]; do
  TOOL_USE=$(echo "$RESPONSE" | jq '.content[] | select(.type == "tool_use")')
  TOOL_NAME=$(echo "$TOOL_USE" | jq -r '.name')
  TOOL_INPUT=$(echo "$TOOL_USE" | jq -c '.input')
  TOOL_USE_ID=$(echo "$TOOL_USE" | jq -r '.id')
  RESULT=$(run_tool "$TOOL_NAME" "$TOOL_INPUT")

  ASSISTANT_CONTENT=$(echo "$RESPONSE" | jq '.content')
  MESSAGES=$(echo "$MESSAGES" | jq \
    --argjson assistant "$ASSISTANT_CONTENT" \
    --arg tool_use_id "$TOOL_USE_ID" \
    --arg result "$RESULT" \
    '. + [
      {role: "assistant", content: $assistant},
      {role: "user", content: [{type: "tool_result", tool_use_id: $tool_use_id, content: $result}]}
    ]')

  RESPONSE=$(call_api)
done

echo "$RESPONSE" | jq -r '.content[] | select(.type == "text") | .text'
````

  
````bash
#!/usr/bin/env bash
# Ring 2: The agentic loop.
# Uses jq for cross-turn message-array state — building an agentic loop in shell
# requires JSON manipulation beyond ant's single-call --transform scope.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.
set -euo pipefail

run_tool() {
  local name="$1" input="$2"
  if [ "$name" = "create_calendar_event" ]; then
    jq -n --arg title "$(jq -r '.title' <<<"$input")" \
      '{event_id: "evt_123", status: "created", title: $title}'
  else
    printf '{"error": "Unknown tool: %s"}' "$name"
  fi
}

# Keep the full conversation history in a JSON array so each turn sees
# prior context.
MESSAGES='[{"role": "user", "content": "Schedule a weekly team standup every Monday at 9am for the next 4 weeks. Invite the whole team: alice@example.com, bob@example.com, carol@example.com."}]'

call_api() {
  # ant reads the request body as YAML on stdin: no auth headers, no
  # hand-built JSON envelope. The static keys (model, tools, tool_choice)
  # live in a quoted heredoc; the growing messages array is appended as
  # JSON, which YAML accepts as flow syntax.
  {
    cat <<'YAML'
model: claude-opus-4-6
max_tokens: 1024
tool_choice: {type: auto, disable_parallel_tool_use: true}
tools:
  - name: create_calendar_event
    description: Create a calendar event with attendees and optional recurrence.
    input_schema:
      type: object
      properties:
        title: {type: string}
        start: {type: string, format: date-time}
        end: {type: string, format: date-time}
        attendees:
          type: array
          items: {type: string, format: email}
        recurrence:
          type: object
          properties:
            frequency: {enum: [daily, weekly, monthly]}
            count: {type: integer, minimum: 1}
      required: [title, start, end]
YAML
    printf 'messages: %s\n' "$MESSAGES"
  } | ant messages create --format json
}

RESPONSE=$(call_api)

# Loop until Claude stops asking for tools. Each iteration runs the
# requested tool, appends the result to history, and asks Claude to
# continue.
while [ "$(jq -r '.stop_reason' <<<"$RESPONSE")" = "tool_use" ]; do
  TOOL_USE=$(jq '.content[] | select(.type == "tool_use")' <<<"$RESPONSE")
  TOOL_NAME=$(jq -r '.name' <<<"$TOOL_USE")
  TOOL_INPUT=$(jq -c '.input' <<<"$TOOL_USE")
  TOOL_USE_ID=$(jq -r '.id' <<<"$TOOL_USE")
  RESULT=$(run_tool "$TOOL_NAME" "$TOOL_INPUT")

  MESSAGES=$(jq \
    --argjson assistant "$(jq '.content' <<<"$RESPONSE")" \
    --arg tool_use_id "$TOOL_USE_ID" \
    --arg result "$RESULT" \
    '. + [
      {role: "assistant", content: $assistant},
      {role: "user", content: [
        {type: "tool_result", tool_use_id: $tool_use_id, content: $result}
      ]}
    ]' <<<"$MESSAGES")

  RESPONSE=$(call_api)
done

jq -r '.content[] | select(.type == "text") | .text' <<<"$RESPONSE"
````

  
````python
# Ring 2: The agentic loop.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.

import json

import anthropic

client = anthropic.Anthropic()

tools = [
    {
        "name": "create_calendar_event",
        "description": "Create a calendar event with attendees and optional recurrence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string", "format": "date-time"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                },
                "recurrence": {
                    "type": "object",
                    "properties": {
                        "frequency": {"enum": ["daily", "weekly", "monthly"]},
                        "count": {"type": "integer", "minimum": 1},
                    },
                },
            },
            "required": ["title", "start", "end"],
        },
    }
]


def run_tool(name, tool_input):
    if name == "create_calendar_event":
        return {"event_id": "evt_123", "status": "created", "title": tool_input["title"]}
    return {"error": f"Unknown tool: {name}"}


# Keep the full conversation history in a list so each turn sees prior context.
messages = [
    {
        "role": "user",
        "content": "Schedule a weekly team standup every Monday at 9am for the next 4 weeks. Invite the whole team: alice@example.com, bob@example.com, carol@example.com.",
    }
]

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=messages,
)

# Loop until Claude stops asking for tools. Each iteration runs the requested
# tool, appends the result to history, and asks Claude to continue.
while response.stop_reason == "tool_use":
    tool_use = next(block for block in response.content if block.type == "tool_use")
    result = run_tool(tool_use.name, tool_use.input)

    messages.append({"role": "assistant", "content": response.content})
    messages.append(
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": json.dumps(result),
                }
            ],
        }
    )

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        tools=tools,
        tool_choice={"type": "auto", "disable_parallel_tool_use": True},
        messages=messages,
    )

final_text = next(block for block in response.content if block.type == "text")
print(final_text.text)
````

  
````typescript
// Ring 2: The agentic loop.
// Source for <CodeSource> in build-a-tool-using-agent.mdx.

import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const tools: Anthropic.Tool[] = [
  {
    name: "create_calendar_event",
    description:
      "Create a calendar event with attendees and optional recurrence.",
    input_schema: {
      type: "object",
      properties: {
        title: { type: "string" },
        start: { type: "string", format: "date-time" },
        end: { type: "string", format: "date-time" },
        attendees: {
          type: "array",
          items: { type: "string", format: "email" },
        },
        recurrence: {
          type: "object",
          properties: {
            frequency: { enum: ["daily", "weekly", "monthly"] },
            count: { type: "integer", minimum: 1 },
          },
        },
      },
      required: ["title", "start", "end"],
    },
  },
];

function runTool(name: string, input: Record<string, unknown>) {
  if (name === "create_calendar_event") {
    return { event_id: "evt_123", status: "created", title: input.title };
  }
  return { error: `Unknown tool: ${name}` };
}

// Keep the full conversation history so each turn sees prior context.
const messages: Anthropic.MessageParam[] = [
  {
    role: "user",
    content:
      "Schedule a weekly team standup every Monday at 9am for the next 4 weeks. Invite the whole team: alice@example.com, bob@example.com, carol@example.com.",
  },
];

let response = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  tools,
  tool_choice: { type: "auto", disable_parallel_tool_use: true },
  messages,
});

// Loop until Claude stops asking for tools. Each iteration runs the requested
// tool, appends the result to history, and asks Claude to continue.
while (response.stop_reason === "tool_use") {
  const toolUse = response.content.find(
    (block): block is Anthropic.ToolUseBlock => block.type === "tool_use",
  )!;
  const result = runTool(toolUse.name, toolUse.input as Record<string, unknown>);

  messages.push({ role: "assistant", content: response.content });
  messages.push({
    role: "user",
    content: [
      {
        type: "tool_result",
        tool_use_id: toolUse.id,
        content: JSON.stringify(result),
      },
    ],
  });

  response = await client.messages.create({
    model: "claude-opus-4-6",
    max_tokens: 1024,
    tools,
    tool_choice: { type: "auto", disable_parallel_tool_use: true },
    messages,
  });
}

for (const block of response.content) {
  if (block.type === "text") {
    console.log(block.text);
  }
}
````

</CodeGroup>

**What to expect**

```text Output
I've set up your weekly team standup for the next 4 Mondays at 9am with Alice, Bob, and Carol invited.
```

The loop may run once or several times depending on how Claude breaks down the task. Your code no longer needs to know in advance.

## Ring 3: Multiple tools, parallel calls

Agents rarely have just one capability. Add a second tool, `list_calendar_events`, so Claude can check the existing schedule before creating something new.

When Claude has multiple independent tool calls to make, it may return several `tool_use` blocks in a single response. Your loop needs to process all of them and send back all results together in one user message. Iterate over every `tool_use` block in `response.content`, not just the first.

<CodeGroup>
  
````bash
#!/bin/bash
# Ring 3: Multiple tools, parallel calls.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.

TOOLS='[
  {
    "name": "create_calendar_event",
    "description": "Create a calendar event with attendees and optional recurrence.",
    "input_schema": {
      "type": "object",
      "properties": {
        "title": {"type": "string"},
        "start": {"type": "string", "format": "date-time"},
        "end": {"type": "string", "format": "date-time"},
        "attendees": {"type": "array", "items": {"type": "string", "format": "email"}},
        "recurrence": {
          "type": "object",
          "properties": {
            "frequency": {"enum": ["daily", "weekly", "monthly"]},
            "count": {"type": "integer", "minimum": 1}
          }
        }
      },
      "required": ["title", "start", "end"]
    }
  },
  {
    "name": "list_calendar_events",
    "description": "List all calendar events on a given date.",
    "input_schema": {
      "type": "object",
      "properties": {"date": {"type": "string", "format": "date"}},
      "required": ["date"]
    }
  }
]'

run_tool() {
  case "$1" in
    create_calendar_event)
      jq -n --arg title "$(echo "$2" | jq -r '.title')" '{event_id: "evt_123", status: "created", title: $title}' ;;
    list_calendar_events)
      echo '{"events": [{"title": "Existing meeting", "start": "14:00", "end": "15:00"}]}' ;;
    *)
      echo "{\"error\": \"Unknown tool: $1\"}" ;;
  esac
}

MESSAGES='[{"role": "user", "content": "Check what I have next Monday, then schedule a planning session that avoids any conflicts."}]'

call_api() {
  curl -s https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d "$(jq -n --argjson tools "$TOOLS" --argjson messages "$MESSAGES" \
      '{model: "claude-opus-4-6", max_tokens: 1024, tools: $tools, messages: $messages}')"
}

RESPONSE=$(call_api)

while [ "$(echo "$RESPONSE" | jq -r '.stop_reason')" = "tool_use" ]; do
  # A single response can contain multiple tool_use blocks. Process all of
  # them and return all results together in one user message.
  TOOL_RESULTS='[]'
  while read -r block; do
    NAME=$(echo "$block" | jq -r '.name')
    INPUT=$(echo "$block" | jq -c '.input')
    ID=$(echo "$block" | jq -r '.id')
    RESULT=$(run_tool "$NAME" "$INPUT")
    TOOL_RESULTS=$(echo "$TOOL_RESULTS" | jq --arg id "$ID" --arg result "$RESULT" \
      '. + [{type: "tool_result", tool_use_id: $id, content: $result}]')
  done < <(echo "$RESPONSE" | jq -c '.content[] | select(.type == "tool_use")')

  MESSAGES=$(echo "$MESSAGES" | jq \
    --argjson assistant "$(echo "$RESPONSE" | jq '.content')" \
    --argjson results "$TOOL_RESULTS" \
    '. + [{role: "assistant", content: $assistant}, {role: "user", content: $results}]')

  RESPONSE=$(call_api)
done

echo "$RESPONSE" | jq -r '.content[] | select(.type == "text") | .text'
````

  
````bash
#!/usr/bin/env bash
# Ring 3: Multiple tools, parallel calls.
# Uses jq for cross-turn message-array state — building an agentic loop in shell
# requires JSON manipulation beyond ant's single-call --transform scope.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.
set -euo pipefail

run_tool() {
  case "$1" in
    create_calendar_event)
      jq -n --arg title "$(jq -r '.title' <<<"$2")" \
        '{event_id: "evt_123", status: "created", title: $title}' ;;
    list_calendar_events)
      echo '{"events": [{"title": "Existing meeting", "start": "14:00", "end": "15:00"}]}' ;;
    *)
      printf '{"error": "Unknown tool: %s"}' "$1" ;;
  esac
}

MESSAGES='[{"role": "user", "content": "Check what I have next Monday, then schedule a planning session that avoids any conflicts."}]'

call_api() {
  # ant reads the request body as YAML on stdin: no auth headers, no
  # hand-built JSON envelope. The static keys (model, tools) live in a
  # quoted heredoc; the growing messages array is appended as JSON,
  # which YAML accepts as flow syntax.
  {
    cat <<'YAML'
model: claude-opus-4-6
max_tokens: 1024
tools:
  - name: create_calendar_event
    description: Create a calendar event with attendees and optional recurrence.
    input_schema:
      type: object
      properties:
        title: {type: string}
        start: {type: string, format: date-time}
        end: {type: string, format: date-time}
        attendees:
          type: array
          items: {type: string, format: email}
        recurrence:
          type: object
          properties:
            frequency: {enum: [daily, weekly, monthly]}
            count: {type: integer, minimum: 1}
      required: [title, start, end]
  - name: list_calendar_events
    description: List all calendar events on a given date.
    input_schema:
      type: object
      properties:
        date: {type: string, format: date}
      required: [date]
YAML
    printf 'messages: %s\n' "$MESSAGES"
  } | ant messages create --format json
}

RESPONSE=$(call_api)

while [ "$(jq -r '.stop_reason' <<<"$RESPONSE")" = "tool_use" ]; do
  # A single response can contain multiple tool_use blocks. Process all
  # of them and return all results together in one user message.
  TOOL_RESULTS='[]'
  while read -r block; do
    NAME=$(jq -r '.name' <<<"$block")
    INPUT=$(jq -c '.input' <<<"$block")
    ID=$(jq -r '.id' <<<"$block")
    RESULT=$(run_tool "$NAME" "$INPUT")
    TOOL_RESULTS=$(jq --arg id "$ID" --arg result "$RESULT" \
      '. + [{type: "tool_result", tool_use_id: $id, content: $result}]' \
      <<<"$TOOL_RESULTS")
  done < <(jq -c '.content[] | select(.type == "tool_use")' <<<"$RESPONSE")

  MESSAGES=$(jq \
    --argjson assistant "$(jq '.content' <<<"$RESPONSE")" \
    --argjson results "$TOOL_RESULTS" \
    '. + [
      {role: "assistant", content: $assistant},
      {role: "user", content: $results}
    ]' <<<"$MESSAGES")

  RESPONSE=$(call_api)
done

jq -r '.content[] | select(.type == "text") | .text' <<<"$RESPONSE"
````

  
````python
# Ring 3: Multiple tools, parallel calls.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.

import json

import anthropic

client = anthropic.Anthropic()

tools = [
    {
        "name": "create_calendar_event",
        "description": "Create a calendar event with attendees and optional recurrence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string", "format": "date-time"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                },
                "recurrence": {
                    "type": "object",
                    "properties": {
                        "frequency": {"enum": ["daily", "weekly", "monthly"]},
                        "count": {"type": "integer", "minimum": 1},
                    },
                },
            },
            "required": ["title", "start", "end"],
        },
    },
    {
        "name": "list_calendar_events",
        "description": "List all calendar events on a given date.",
        "input_schema": {
            "type": "object",
            "properties": {
                "date": {"type": "string", "format": "date"},
            },
            "required": ["date"],
        },
    },
]


def run_tool(name, tool_input):
    if name == "create_calendar_event":
        return {"event_id": "evt_123", "status": "created", "title": tool_input["title"]}
    if name == "list_calendar_events":
        return {"events": [{"title": "Existing meeting", "start": "14:00", "end": "15:00"}]}
    return {"error": f"Unknown tool: {name}"}


messages = [
    {
        "role": "user",
        "content": "Check what I have next Monday, then schedule a planning session that avoids any conflicts.",
    }
]

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=tools,
    messages=messages,
)

while response.stop_reason == "tool_use":
    # A single response can contain multiple tool_use blocks. Process all of
    # them and return all results together in one user message.
    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            result = run_tool(block.name, block.input)
            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": json.dumps(result),
                }
            )

    messages.append({"role": "assistant", "content": response.content})
    messages.append({"role": "user", "content": tool_results})

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )

final_text = next(block for block in response.content if block.type == "text")
print(final_text.text)
````

  
````typescript
// Ring 3: Multiple tools, parallel calls.
// Source for <CodeSource> in build-a-tool-using-agent.mdx.

import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const tools: Anthropic.Tool[] = [
  {
    name: "create_calendar_event",
    description:
      "Create a calendar event with attendees and optional recurrence.",
    input_schema: {
      type: "object",
      properties: {
        title: { type: "string" },
        start: { type: "string", format: "date-time" },
        end: { type: "string", format: "date-time" },
        attendees: {
          type: "array",
          items: { type: "string", format: "email" },
        },
        recurrence: {
          type: "object",
          properties: {
            frequency: { enum: ["daily", "weekly", "monthly"] },
            count: { type: "integer", minimum: 1 },
          },
        },
      },
      required: ["title", "start", "end"],
    },
  },
  {
    name: "list_calendar_events",
    description: "List all calendar events on a given date.",
    input_schema: {
      type: "object",
      properties: {
        date: { type: "string", format: "date" },
      },
      required: ["date"],
    },
  },
];

function runTool(name: string, input: Record<string, unknown>) {
  if (name === "create_calendar_event") {
    return { event_id: "evt_123", status: "created", title: input.title };
  }
  if (name === "list_calendar_events") {
    return {
      events: [{ title: "Existing meeting", start: "14:00", end: "15:00" }],
    };
  }
  return { error: `Unknown tool: ${name}` };
}

const messages: Anthropic.MessageParam[] = [
  {
    role: "user",
    content:
      "Check what I have next Monday, then schedule a planning session that avoids any conflicts.",
  },
];

let response = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  tools,
  messages,
});

while (response.stop_reason === "tool_use") {
  // A single response can contain multiple tool_use blocks. Process all of
  // them and return all results together in one user message.
  const toolResults: Anthropic.ToolResultBlockParam[] = [];
  for (const block of response.content) {
    if (block.type === "tool_use") {
      const result = runTool(block.name, block.input as Record<string, unknown>);
      toolResults.push({
        type: "tool_result",
        tool_use_id: block.id,
        content: JSON.stringify(result),
      });
    }
  }

  messages.push({ role: "assistant", content: response.content });
  messages.push({ role: "user", content: toolResults });

  response = await client.messages.create({
    model: "claude-opus-4-6",
    max_tokens: 1024,
    tools,
    messages,
  });
}

for (const block of response.content) {
  if (block.type === "text") {
    console.log(block.text);
  }
}
````

</CodeGroup>

**What to expect**

```text Output
I checked your calendar for next Monday and found an existing meeting from 2pm to 3pm. I've scheduled the planning session for 10am to 11am to avoid the conflict.
```

For more on concurrent execution and ordering guarantees, see [Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use).

## Ring 4: Error handling

Tools fail. A calendar API might reject an event with too many attendees, or a date might be malformed. When a tool raises an error, send the error message back with `is_error: true` instead of crashing. Claude reads the error and can retry with corrected input, ask the user for clarification, or explain the limitation.

<CodeGroup>
  
````bash
#!/bin/bash
# Ring 4: Error handling.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.

TOOLS='[
  {
    "name": "create_calendar_event",
    "description": "Create a calendar event with attendees and optional recurrence.",
    "input_schema": {
      "type": "object",
      "properties": {
        "title": {"type": "string"},
        "start": {"type": "string", "format": "date-time"},
        "end": {"type": "string", "format": "date-time"},
        "attendees": {"type": "array", "items": {"type": "string", "format": "email"}},
        "recurrence": {
          "type": "object",
          "properties": {
            "frequency": {"enum": ["daily", "weekly", "monthly"]},
            "count": {"type": "integer", "minimum": 1}
          }
        }
      },
      "required": ["title", "start", "end"]
    }
  },
  {
    "name": "list_calendar_events",
    "description": "List all calendar events on a given date.",
    "input_schema": {
      "type": "object",
      "properties": {"date": {"type": "string", "format": "date"}},
      "required": ["date"]
    }
  }
]'

run_tool() {
  case "$1" in
    create_calendar_event)
      local count=$(echo "$2" | jq '.attendees | length // 0')
      if [ "$count" -gt 10 ]; then
        echo "ERROR: Too many attendees (max 10)"
        return 1
      fi
      jq -n --arg title "$(echo "$2" | jq -r '.title')" '{event_id: "evt_123", status: "created", title: $title}' ;;
    list_calendar_events)
      echo '{"events": [{"title": "Existing meeting", "start": "14:00", "end": "15:00"}]}' ;;
    *)
      echo "ERROR: Unknown tool: $1"
      return 1 ;;
  esac
}

EMAILS=$(seq 0 14 | sed 's/.*/user&@example.com/' | paste -sd, -)
MESSAGES="[{\"role\": \"user\", \"content\": \"Schedule an all-hands with everyone: $EMAILS\"}]"

call_api() {
  curl -s https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d "$(jq -n --argjson tools "$TOOLS" --argjson messages "$MESSAGES" \
      '{model: "claude-opus-4-6", max_tokens: 1024, tools: $tools, messages: $messages}')"
}

RESPONSE=$(call_api)

while [ "$(echo "$RESPONSE" | jq -r '.stop_reason')" = "tool_use" ]; do
  TOOL_RESULTS='[]'
  while read -r block; do
    NAME=$(echo "$block" | jq -r '.name')
    INPUT=$(echo "$block" | jq -c '.input')
    ID=$(echo "$block" | jq -r '.id')
    if OUTPUT=$(run_tool "$NAME" "$INPUT"); then
      TOOL_RESULTS=$(echo "$TOOL_RESULTS" | jq --arg id "$ID" --arg result "$OUTPUT" \
        '. + [{type: "tool_result", tool_use_id: $id, content: $result}]')
    else
      # Signal failure so Claude can retry or ask for clarification.
      TOOL_RESULTS=$(echo "$TOOL_RESULTS" | jq --arg id "$ID" --arg result "$OUTPUT" \
        '. + [{type: "tool_result", tool_use_id: $id, content: $result, is_error: true}]')
    fi
  done < <(echo "$RESPONSE" | jq -c '.content[] | select(.type == "tool_use")')

  MESSAGES=$(echo "$MESSAGES" | jq \
    --argjson assistant "$(echo "$RESPONSE" | jq '.content')" \
    --argjson results "$TOOL_RESULTS" \
    '. + [{role: "assistant", content: $assistant}, {role: "user", content: $results}]')

  RESPONSE=$(call_api)
done

echo "$RESPONSE" | jq -r '.content[] | select(.type == "text") | .text'
````

  
````bash
#!/usr/bin/env bash
# Ring 4: Error handling.
# Uses jq for cross-turn message-array state — building an agentic loop in shell
# requires JSON manipulation beyond ant's single-call --transform scope.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.
set -euo pipefail

run_tool() {
  case "$1" in
    create_calendar_event)
      local count
      count=$(jq '.attendees | length // 0' <<<"$2")
      if [ "$count" -gt 10 ]; then
        echo "ERROR: Too many attendees (max 10)"
        return 1
      fi
      jq -n --arg title "$(jq -r '.title' <<<"$2")" \
        '{event_id: "evt_123", status: "created", title: $title}' ;;
    list_calendar_events)
      echo '{"events": [{"title": "Existing meeting", "start": "14:00", "end": "15:00"}]}' ;;
    *)
      echo "ERROR: Unknown tool: $1"
      return 1 ;;
  esac
}

EMAILS=$(seq 0 14 | sed 's/.*/user&@example.com/' | paste -sd, -)
MESSAGES=$(jq -n --arg msg "Schedule an all-hands with everyone: $EMAILS" \
  '[{role: "user", content: $msg}]')

call_api() {
  # ant reads the request body as YAML on stdin: no auth headers, no
  # hand-built JSON envelope. The static keys (model, tools) live in a
  # quoted heredoc; the growing messages array is appended as JSON,
  # which YAML accepts as flow syntax.
  {
    cat <<'YAML'
model: claude-opus-4-6
max_tokens: 1024
tools:
  - name: create_calendar_event
    description: Create a calendar event with attendees and optional recurrence.
    input_schema:
      type: object
      properties:
        title: {type: string}
        start: {type: string, format: date-time}
        end: {type: string, format: date-time}
        attendees:
          type: array
          items: {type: string, format: email}
        recurrence:
          type: object
          properties:
            frequency: {enum: [daily, weekly, monthly]}
            count: {type: integer, minimum: 1}
      required: [title, start, end]
  - name: list_calendar_events
    description: List all calendar events on a given date.
    input_schema:
      type: object
      properties:
        date: {type: string, format: date}
      required: [date]
YAML
    printf 'messages: %s\n' "$MESSAGES"
  } | ant messages create --format json
}

RESPONSE=$(call_api)

while [ "$(jq -r '.stop_reason' <<<"$RESPONSE")" = "tool_use" ]; do
  TOOL_RESULTS='[]'
  while read -r block; do
    NAME=$(jq -r '.name' <<<"$block")
    INPUT=$(jq -c '.input' <<<"$block")
    ID=$(jq -r '.id' <<<"$block")
    if OUTPUT=$(run_tool "$NAME" "$INPUT"); then
      TOOL_RESULTS=$(jq --arg id "$ID" --arg result "$OUTPUT" \
        '. + [{type: "tool_result", tool_use_id: $id, content: $result}]' \
        <<<"$TOOL_RESULTS")
    else
      # Signal failure so Claude can retry or ask for clarification.
      TOOL_RESULTS=$(jq --arg id "$ID" --arg result "$OUTPUT" \
        '. + [{type: "tool_result", tool_use_id: $id, content: $result, is_error: true}]' \
        <<<"$TOOL_RESULTS")
    fi
  done < <(jq -c '.content[] | select(.type == "tool_use")' <<<"$RESPONSE")

  MESSAGES=$(jq \
    --argjson assistant "$(jq '.content' <<<"$RESPONSE")" \
    --argjson results "$TOOL_RESULTS" \
    '. + [
      {role: "assistant", content: $assistant},
      {role: "user", content: $results}
    ]' <<<"$MESSAGES")

  RESPONSE=$(call_api)
done

jq -r '.content[] | select(.type == "text") | .text' <<<"$RESPONSE"
````

  
````python
# Ring 4: Error handling.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.

import json

import anthropic

client = anthropic.Anthropic()

tools = [
    {
        "name": "create_calendar_event",
        "description": "Create a calendar event with attendees and optional recurrence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string", "format": "date-time"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                },
                "recurrence": {
                    "type": "object",
                    "properties": {
                        "frequency": {"enum": ["daily", "weekly", "monthly"]},
                        "count": {"type": "integer", "minimum": 1},
                    },
                },
            },
            "required": ["title", "start", "end"],
        },
    },
    {
        "name": "list_calendar_events",
        "description": "List all calendar events on a given date.",
        "input_schema": {
            "type": "object",
            "properties": {
                "date": {"type": "string", "format": "date"},
            },
            "required": ["date"],
        },
    },
]


def run_tool(name, tool_input):
    if name == "create_calendar_event":
        if "attendees" in tool_input and len(tool_input["attendees"]) > 10:
            raise ValueError("Too many attendees (max 10)")
        return {"event_id": "evt_123", "status": "created", "title": tool_input["title"]}
    if name == "list_calendar_events":
        return {"events": [{"title": "Existing meeting", "start": "14:00", "end": "15:00"}]}
    raise ValueError(f"Unknown tool: {name}")


messages = [
    {
        "role": "user",
        "content": "Schedule an all-hands with everyone: " + ", ".join(f"user{i}@example.com" for i in range(15)),
    }
]

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=tools,
    messages=messages,
)

while response.stop_reason == "tool_use":
    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            try:
                result = run_tool(block.name, block.input)
                tool_results.append(
                    {"type": "tool_result", "tool_use_id": block.id, "content": json.dumps(result)}
                )
            except Exception as exc:
                # Signal failure so Claude can retry or ask for clarification.
                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(exc),
                        "is_error": True,
                    }
                )

    messages.append({"role": "assistant", "content": response.content})
    messages.append({"role": "user", "content": tool_results})

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )

final_text = next(block for block in response.content if block.type == "text")
print(final_text.text)
````

  
````typescript
// Ring 4: Error handling.
// Source for <CodeSource> in build-a-tool-using-agent.mdx.

import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const tools: Anthropic.Tool[] = [
  {
    name: "create_calendar_event",
    description:
      "Create a calendar event with attendees and optional recurrence.",
    input_schema: {
      type: "object",
      properties: {
        title: { type: "string" },
        start: { type: "string", format: "date-time" },
        end: { type: "string", format: "date-time" },
        attendees: {
          type: "array",
          items: { type: "string", format: "email" },
        },
        recurrence: {
          type: "object",
          properties: {
            frequency: { enum: ["daily", "weekly", "monthly"] },
            count: { type: "integer", minimum: 1 },
          },
        },
      },
      required: ["title", "start", "end"],
    },
  },
  {
    name: "list_calendar_events",
    description: "List all calendar events on a given date.",
    input_schema: {
      type: "object",
      properties: {
        date: { type: "string", format: "date" },
      },
      required: ["date"],
    },
  },
];

function runTool(name: string, input: Record<string, unknown>) {
  if (name === "create_calendar_event") {
    const attendees = input.attendees as string[] | undefined;
    if (attendees && attendees.length > 10) {
      throw new Error("Too many attendees (max 10)");
    }
    return { event_id: "evt_123", status: "created", title: input.title };
  }
  if (name === "list_calendar_events") {
    return {
      events: [{ title: "Existing meeting", start: "14:00", end: "15:00" }],
    };
  }
  throw new Error(`Unknown tool: ${name}`);
}

const emails = Array.from({ length: 15 }, (_, i) => `user${i}@example.com`);
const messages: Anthropic.MessageParam[] = [
  {
    role: "user",
    content: `Schedule an all-hands with everyone: ${emails.join(", ")}`,
  },
];

let response = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  tools,
  messages,
});

while (response.stop_reason === "tool_use") {
  const toolResults: Anthropic.ToolResultBlockParam[] = [];
  for (const block of response.content) {
    if (block.type === "tool_use") {
      try {
        const result = runTool(block.name, block.input as Record<string, unknown>);
        toolResults.push({
          type: "tool_result",
          tool_use_id: block.id,
          content: JSON.stringify(result),
        });
      } catch (err) {
        // Signal failure so Claude can retry or ask for clarification.
        toolResults.push({
          type: "tool_result",
          tool_use_id: block.id,
          content: String(err),
          is_error: true,
        });
      }
    }
  }

  messages.push({ role: "assistant", content: response.content });
  messages.push({ role: "user", content: toolResults });

  response = await client.messages.create({
    model: "claude-opus-4-6",
    max_tokens: 1024,
    tools,
    messages,
  });
}

for (const block of response.content) {
  if (block.type === "text") {
    console.log(block.text);
  }
}
````

</CodeGroup>

**What to expect**

```text Output
I tried to schedule the all-hands but the calendar only allows 10 attendees per event. I can split this into two sessions, or you can let me know which 10 people to prioritize.
```

The `is_error` flag is the only difference from a successful result. Claude sees the flag and the error text, and responds accordingly. See [Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls) for the full error-handling reference.

## Ring 5: The Tool Runner SDK abstraction

Rings 2 through 4 wrote the same loop by hand: call the API, check `stop_reason`, run tools, append results, repeat. The Tool Runner does this for you. Define each tool as a function, pass the list to `tool_runner`, and retrieve the final message once the loop completes. Error wrapping, result formatting, and conversation management are handled internally.

The Python SDK uses the `@beta_tool` decorator to infer the schema from type hints and the docstring. The TypeScript SDK uses `betaZodTool` with a Zod schema.

<Note>
Tool Runner is available in the Python, TypeScript, and Ruby SDKs. The cURL and CLI tabs show a note instead of code; keep the Ring 4 loop for curl- or CLI-based scripts.
</Note>

<CodeGroup>
  
````bash
#!/bin/bash
# Ring 5: The Tool Runner SDK abstraction.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.

# The Tool Runner SDK abstraction is available in the Python, TypeScript,
# and Ruby SDKs. There is no equivalent for raw curl requests. Switch to
# the Python or TypeScript tab to see Ring 5, or keep the Ring 4 loop as
# your shell implementation.
````

  
````bash
#!/usr/bin/env bash
# Ring 5: The Tool Runner SDK abstraction.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.
set -euo pipefail

# The Tool Runner SDK abstraction is available in the Python, TypeScript,
# and Ruby SDKs. The ant CLI exposes the Messages API directly and has
# no equivalent helper. Switch to the Python or TypeScript tab to see
# Ring 5, or keep the Ring 4 loop as your CLI implementation.
````

  
````python
# Ring 5: The Tool Runner SDK abstraction.
# Source for <CodeSource> in build-a-tool-using-agent.mdx.

import json

import anthropic
from anthropic import beta_tool

client = anthropic.Anthropic()


@beta_tool
def create_calendar_event(
    title: str,
    start: str,
    end: str,
    attendees: list[str] | None = None,
    recurrence: dict | None = None,
) -> str:
    """Create a calendar event with attendees and optional recurrence.

    Args:
        title: Event title.
        start: Start time in ISO 8601 format.
        end: End time in ISO 8601 format.
        attendees: Email addresses to invite.
        recurrence: Dict with 'frequency' (daily, weekly, monthly) and 'count'.
    """
    if attendees and len(attendees) > 10:
        raise ValueError("Too many attendees (max 10)")
    return json.dumps({"event_id": "evt_123", "status": "created", "title": title})


@beta_tool
def list_calendar_events(date: str) -> str:
    """List all calendar events on a given date.

    Args:
        date: Date in YYYY-MM-DD format.
    """
    return json.dumps({"events": [{"title": "Existing meeting", "start": "14:00", "end": "15:00"}]})


final_message = client.beta.messages.tool_runner(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=[create_calendar_event, list_calendar_events],
    messages=[
        {
            "role": "user",
            "content": "Check what I have next Monday, then schedule a planning session that avoids any conflicts.",
        }
    ],
).until_done()

for block in final_message.content:
    if block.type == "text":
        print(block.text)
````

  
````typescript
// Ring 5: The Tool Runner SDK abstraction.
// Source for <CodeSource> in build-a-tool-using-agent.mdx.

import Anthropic from "@anthropic-ai/sdk";
import { betaZodTool } from "@anthropic-ai/sdk/helpers/beta/zod";
import { z } from "zod";

const client = new Anthropic();

const createCalendarEvent = betaZodTool({
  name: "create_calendar_event",
  description:
    "Create a calendar event with attendees and optional recurrence.",
  inputSchema: z.object({
    title: z.string(),
    start: z.string().datetime(),
    end: z.string().datetime(),
    attendees: z.array(z.string().email()).optional(),
    recurrence: z
      .object({
        frequency: z.enum(["daily", "weekly", "monthly"]),
        count: z.number().int().min(1),
      })
      .optional(),
  }),
  run: async (input) => {
    if (input.attendees && input.attendees.length > 10) {
      throw new Error("Too many attendees (max 10)");
    }
    return JSON.stringify({
      event_id: "evt_123",
      status: "created",
      title: input.title,
    });
  },
});

const listCalendarEvents = betaZodTool({
  name: "list_calendar_events",
  description: "List all calendar events on a given date.",
  inputSchema: z.object({
    date: z.string().date(),
  }),
  run: async () => {
    return JSON.stringify({
      events: [{ title: "Existing meeting", start: "14:00", end: "15:00" }],
    });
  },
});

const finalMessage = await client.beta.messages.toolRunner({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  tools: [createCalendarEvent, listCalendarEvents],
  messages: [
    {
      role: "user",
      content:
        "Check what I have next Monday, then schedule a planning session that avoids any conflicts.",
    },
  ],
});

for (const block of finalMessage.content) {
  if (block.type === "text") {
    console.log(block.text);
  }
}
````

</CodeGroup>

**What to expect**

```text Output
I checked your calendar for next Monday and found an existing meeting from 2pm to 3pm. I've scheduled the planning session for 10am to 11am to avoid the conflict.
```

The output is identical to Ring 3. The difference is in the code: roughly half the lines, no manual loop, and the schema lives next to the implementation.

## What you built

You started with a single hardcoded tool call and ended with a production-shaped agent that handles multiple tools, parallel calls, and errors, then collapsed all of that into the Tool Runner. Along the way you saw every piece of the tool-use protocol: `tool_use` blocks, `tool_result` blocks, `tool_use_id` matching, `stop_reason` checking, and `is_error` signaling.

## Next steps

<CardGroup>
  <Card href="/docs/en/agents-and-tools/tool-use/define-tools" title="Sharpen your schemas">
    Schema specification and best practices.
  </Card>
  <Card href="/docs/en/agents-and-tools/tool-use/tool-runner" title="Tool Runner deep dive">
    The full SDK abstraction reference.
  </Card>
  <Card href="/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use" title="Troubleshooting">
    Fix common tool-use errors.
  </Card>
</CardGroup>
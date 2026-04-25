# Strict tool use

Enforce JSON Schema compliance on Claude's tool inputs with grammar-constrained sampling.

---

Setting `strict: true` on a tool definition uses grammar-constrained sampling to guarantee Claude's tool inputs match your JSON Schema. This page covers why strict mode matters for agents, how to enable it, and common use cases. For the supported JSON Schema subset, see [JSON Schema limitations](/docs/en/build-with-claude/structured-outputs#json-schema-limitations). For non-strict schema guidance, see [Define tools](/docs/en/agents-and-tools/tool-use/define-tools).

Strict tool use validates tool parameters, ensuring Claude calls your functions with correctly-typed arguments. Use strict tool use when you need to:

- Validate tool parameters
- Build agentic workflows
- Ensure type-safe function calls
- Handle complex tools with nested properties

## Why strict tool use matters for agents

Building reliable agentic systems requires guaranteed schema conformance. Without strict mode, Claude might return incompatible types (`"2"` instead of `2`) or missing required fields, breaking your functions and causing runtime errors.

Strict tool use guarantees type-safe parameters:
- Functions receive correctly-typed arguments every time
- No need to validate and retry tool calls
- Production-ready agents that work consistently at scale

For example, suppose a booking system needs `passengers: int`. Without strict mode, Claude might provide `passengers: "two"` or `passengers: "2"`. With `strict: true`, the response will always contain `passengers: 2`.

## Quick start

<CodeGroup>

```bash cURL
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "What is the weather in San Francisco?"}
    ],
    "tools": [{
      "name": "get_weather",
      "description": "Get the current weather in a given location",
      "strict": true,
      "input_schema": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": ["celsius", "fahrenheit"]
          }
        },
        "required": ["location"],
        "additionalProperties": false
      }
    }]
  }'
```

```bash CLI
ant messages create --transform content <<'YAML'
model: claude-opus-4-7
max_tokens: 1024
messages:
  - role: user
    content: What is the weather in San Francisco?
tools:
  - name: get_weather
    description: Get the current weather in a given location
    strict: true
    input_schema:
      type: object
      properties:
        location:
          type: string
          description: The city and state, e.g. San Francisco, CA
        unit:
          type: string
          enum: [celsius, fahrenheit]
      required: [location]
      additionalProperties: false
YAML
```

```python Python hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
    tools=[
        {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "strict": True,  # Enable strict mode
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The unit of temperature, either 'celsius' or 'fahrenheit'",
                    },
                },
                "required": ["location"],
                "additionalProperties": False,
            },
        }
    ],
)
print(response.content)
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY
});

const response = await client.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content: "What's the weather like in San Francisco?"
    }
  ],
  tools: [
    {
      name: "get_weather",
      description: "Get the current weather in a given location",
      strict: true, // Enable strict mode
      input_schema: {
        type: "object",
        properties: {
          location: {
            type: "string",
            description: "The city and state, e.g. San Francisco, CA"
          },
          unit: {
            type: "string",
            enum: ["celsius", "fahrenheit"]
          }
        },
        required: ["location"],
        additionalProperties: false
      }
    }
  ]
});
console.log(response.content);
```

```csharp C#
using System.Text.Json;
using Anthropic;
using Anthropic.Models.Messages;

public class Program
{
    public static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var parameters = new MessageCreateParams
        {
            Model = Model.ClaudeOpus4_7,
            MaxTokens = 1024,
            Messages = [new() { Role = Role.User, Content = "What's the weather like in San Francisco?" }],
            Tools = [
                new ToolUnion(new Tool()
                {
                    Name = "get_weather",
                    Description = "Get the current weather in a given location",
                    Strict = true,
                    InputSchema = new InputSchema(new Dictionary<string, JsonElement>
                    {
                        ["properties"] = JsonSerializer.SerializeToElement(new Dictionary<string, object>
                        {
                            ["location"] = new { type = "string", description = "The city and state, e.g. San Francisco, CA" },
                            ["unit"] = new { type = "string", @enum = new[] { "celsius", "fahrenheit" } },
                        }),
                        ["required"] = JsonSerializer.SerializeToElement(new[] { "location" }),
                        ["additionalProperties"] = JsonSerializer.SerializeToElement(false),
                    }),
                }),
            ]
        };

        var message = await client.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
```

```go Go hidelines={1..11,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_7,
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("What's the weather like in San Francisco?")),
		},
		Tools: []anthropic.ToolUnionParam{
			{OfTool: &anthropic.ToolParam{
				Name:        "get_weather",
				Description: anthropic.String("Get the current weather in a given location"),
				Strict:      anthropic.Bool(true),
				InputSchema: anthropic.ToolInputSchemaParam{
					Properties: map[string]any{
						"location": map[string]any{
							"type":        "string",
							"description": "The city and state, e.g. San Francisco, CA",
						},
						"unit": map[string]any{
							"type": "string",
							"enum": []string{"celsius", "fahrenheit"},
						},
					},
					Required: []string{"location"},
					ExtraFields: map[string]any{
						"additionalProperties": false,
					},
				}}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response.Content)
}
```

```java Java hidelines={1..12,-1..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.JsonValue;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.Tool;
import com.anthropic.models.messages.Tool.InputSchema;
import java.util.List;
import java.util.Map;

void main() {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    InputSchema schema = InputSchema.builder()
        .properties(
            JsonValue.from(
                Map.of(
                    "location", Map.of(
                        "type", "string",
                        "description", "The city and state, e.g. San Francisco, CA"
                    ),
                    "unit", Map.of(
                        "type", "string",
                        "enum", List.of("celsius", "fahrenheit")
                    )
                )
            )
        )
        .putAdditionalProperty("required", JsonValue.from(List.of("location")))
        .putAdditionalProperty("additionalProperties", JsonValue.from(false))
        .build();

    MessageCreateParams params = MessageCreateParams.builder()
        .model(Model.CLAUDE_OPUS_4_7)
        .maxTokens(1024L)
        .addUserMessage("What's the weather like in San Francisco?")
        .addTool(
            Tool.builder()
                .name("get_weather")
                .description("Get the current weather in a given location")
                .strict(true)
                .inputSchema(schema)
                .build()
        )
        .build();

    Message response = client.messages().create(params);
    IO.println(response.content());
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$message = $client->messages->create(
    maxTokens: 1024,
    messages: [
        ['role' => 'user', 'content' => "What's the weather like in San Francisco?"]
    ],
    model: 'claude-opus-4-7',
    tools: [
        [
            'name' => 'get_weather',
            'description' => 'Get the current weather in a given location',
            'strict' => true,
            'input_schema' => [
                'type' => 'object',
                'properties' => [
                    'location' => [
                        'type' => 'string',
                        'description' => 'The city and state, e.g. San Francisco, CA'
                    ],
                    'unit' => [
                        'type' => 'string',
                        'enum' => ['celsius', 'fahrenheit']
                    ]
                ],
                'required' => ['location'],
                'additionalProperties' => false
            ]
        ]
    ],
);

echo $message;
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

message = client.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 1024,
  messages: [
    { role: "user", content: "What's the weather like in San Francisco?" }
  ],
  tools: [
    {
      name: "get_weather",
      description: "Get the current weather in a given location",
      strict: true,
      input_schema: {
        type: "object",
        properties: {
          location: {
            type: "string",
            description: "The city and state, e.g. San Francisco, CA"
          },
          unit: {
            type: "string",
            enum: ["celsius", "fahrenheit"]
          }
        },
        required: ["location"],
        additionalProperties: false
      }
    }
  ]
)
puts message.content
```

</CodeGroup>

**Response format:** Tool use blocks with validated inputs in `response.content[x].input`

```json Output
{
  "type": "tool_use",
  "name": "get_weather",
  "input": {
    "location": "San Francisco, CA"
  }
}
```

**Guarantees:**
- Tool `input` strictly follows the `input_schema`
- Tool `name` is always valid (from provided tools or server tools)

## How it works

<Steps>
  <Step title="Define your tool schema">
    Create a JSON schema for your tool's `input_schema`. The schema uses standard JSON Schema format with some limitations (see [JSON Schema limitations](/docs/en/build-with-claude/structured-outputs#json-schema-limitations)).
  </Step>
  <Step title="Add strict: true">
    Set `"strict": true` as a top-level property in your tool definition, alongside `name`, `description`, and `input_schema`.
  </Step>
  <Step title="Handle tool calls">
    When Claude uses the tool, the `input` field in the tool_use block will strictly follow your `input_schema`, and the `name` will always be valid.
  </Step>
</Steps>

## Common use cases

<section title="Validated tool inputs">

Ensure tool parameters exactly match your schema:

<CodeGroup>

```bash CLI
ant messages create <<'YAML'
model: claude-opus-4-7
max_tokens: 1024
messages:
  - role: user
    content: Search for flights to Tokyo departing June 1, 2026
tools:
  - name: search_flights
    strict: true
    input_schema:
      type: object
      properties:
        destination:
          type: string
        departure_date:
          type: string
          format: date
        passengers:
          type: integer
          enum: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      required: [destination, departure_date]
      additionalProperties: false
YAML
```

```python Python hidelines={1..2}
from anthropic import Anthropic

client = Anthropic()
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Search for flights to Tokyo departing June 1, 2026",
        }
    ],
    tools=[
        {
            "name": "search_flights",
            "strict": True,
            "input_schema": {
                "type": "object",
                "properties": {
                    "destination": {"type": "string"},
                    "departure_date": {"type": "string", "format": "date"},
                    "passengers": {
                        "type": "integer",
                        "enum": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    },
                },
                "required": ["destination", "departure_date"],
                "additionalProperties": False,
            },
        }
    ],
)

print(response)
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const searchFlightsTool: Anthropic.Tool = {
  name: "search_flights",
  strict: true,
  input_schema: {
    type: "object",
    properties: {
      destination: { type: "string" },
      departure_date: { type: "string", format: "date" },
      passengers: { type: "integer", enum: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] }
    },
    required: ["destination", "departure_date"],
    additionalProperties: false
  }
};

const response = await client.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Search for flights to Tokyo departing June 1, 2026" }],
  tools: [searchFlightsTool]
});

console.log(response);
```

```csharp C#
using System;
using System.Text.Json;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new()
        {
            ApiKey = Environment.GetEnvironmentVariable("ANTHROPIC_API_KEY")
        };

        var parameters = new MessageCreateParams
        {
            Model = Model.ClaudeOpus4_7,
            MaxTokens = 1024,
            Messages = [new() { Role = Role.User, Content = "Search for flights to Tokyo departing June 1, 2026" }],
            Tools = [
                new ToolUnion(new Tool()
                {
                    Name = "search_flights",
                    Strict = true,
                    InputSchema = new InputSchema(new Dictionary<string, JsonElement>
                    {
                        ["properties"] = JsonSerializer.SerializeToElement(new Dictionary<string, object>
                        {
                            ["destination"] = new { type = "string" },
                            ["departure_date"] = new { type = "string", format = "date" },
                            ["passengers"] = new { type = "integer", @enum = new[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 } },
                        }),
                        ["required"] = JsonSerializer.SerializeToElement(new[] { "destination", "departure_date" }),
                        ["additionalProperties"] = JsonSerializer.SerializeToElement(false),
                    }),
                }),
            ]
        };

        var message = await client.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
```

```go Go hidelines={1..11,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_7,
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("Search for flights to Tokyo departing June 1, 2026")),
		},
		Tools: []anthropic.ToolUnionParam{
			{OfTool: &anthropic.ToolParam{
				Name:   "search_flights",
				Strict: anthropic.Bool(true),
				InputSchema: anthropic.ToolInputSchemaParam{
					Properties: map[string]any{
						"destination": map[string]any{
							"type": "string",
						},
						"departure_date": map[string]any{
							"type":   "string",
							"format": "date",
						},
						"passengers": map[string]any{
							"type": "integer",
							"enum": []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
						},
					},
					Required: []string{"destination", "departure_date"},
					ExtraFields: map[string]any{
						"additionalProperties": false,
					},
				}}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java hidelines={1..12,-1..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.JsonValue;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.Tool;
import com.anthropic.models.messages.Tool.InputSchema;
import java.util.List;
import java.util.Map;

void main() {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    InputSchema schema = InputSchema.builder()
        .properties(
            JsonValue.from(
                Map.of(
                    "destination", Map.of("type", "string"),
                    "departure_date", Map.of("type", "string", "format", "date"),
                    "passengers", Map.of(
                        "type", "integer",
                        "enum", List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
                    )
                )
            )
        )
        .putAdditionalProperty("required", JsonValue.from(List.of("destination", "departure_date")))
        .putAdditionalProperty("additionalProperties", JsonValue.from(false))
        .build();

    MessageCreateParams params = MessageCreateParams.builder()
        .model(Model.CLAUDE_OPUS_4_7)
        .maxTokens(1024L)
        .addUserMessage("Search for flights to Tokyo departing June 1, 2026")
        .addTool(
            Tool.builder()
                .name("search_flights")
                .strict(true)
                .inputSchema(schema)
                .build()
        )
        .build();

    Message response = client.messages().create(params);
    IO.println(response);
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$message = $client->messages->create(
    maxTokens: 1024,
    messages: [
        ['role' => 'user', 'content' => 'Search for flights to Tokyo departing June 1, 2026']
    ],
    model: 'claude-opus-4-7',
    tools: [
        [
            'name' => 'search_flights',
            'strict' => true,
            'input_schema' => [
                'type' => 'object',
                'properties' => [
                    'destination' => ['type' => 'string'],
                    'departure_date' => ['type' => 'string', 'format' => 'date'],
                    'passengers' => [
                        'type' => 'integer',
                        'enum' => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    ]
                ],
                'required' => ['destination', 'departure_date'],
                'additionalProperties' => false
            ]
        ]
    ],
);
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

message = client.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 1024,
  messages: [
    { role: "user", content: "Search for flights to Tokyo departing June 1, 2026" }
  ],
  tools: [
    {
      name: "search_flights",
      strict: true,
      input_schema: {
        type: "object",
        properties: {
          destination: { type: "string" },
          departure_date: { type: "string", format: "date" },
          passengers: {
            type: "integer",
            enum: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
          }
        },
        required: ["destination", "departure_date"],
        additionalProperties: false
      }
    }
  ]
)
puts message
```

</CodeGroup>

</section>

<section title="Agentic workflow with multiple validated tools">

Build reliable multi-step agents with guaranteed tool parameters:

<CodeGroup>

```bash CLI
ant messages create <<'YAML'
model: claude-opus-4-7
max_tokens: 1024
messages:
  - role: user
    content: >-
      Help me plan a trip from New York to Paris for 2 people,
      departing June 1, 2026
tools:
  - name: search_flights
    strict: true
    input_schema:
      type: object
      properties:
        origin: {type: string}
        destination: {type: string}
        departure_date: {type: string, format: date}
        travelers: {type: integer, enum: [1, 2, 3, 4, 5, 6]}
      required: [origin, destination, departure_date]
      additionalProperties: false
  - name: search_hotels
    strict: true
    input_schema:
      type: object
      properties:
        city: {type: string}
        check_in: {type: string, format: date}
        guests: {type: integer, enum: [1, 2, 3, 4]}
      required: [city, check_in]
      additionalProperties: false
YAML
```

```python Python hidelines={1..2}
from anthropic import Anthropic

client = Anthropic()
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Help me plan a trip from New York to Paris for 2 people, departing June 1, 2026",
        }
    ],
    tools=[
        {
            "name": "search_flights",
            "strict": True,
            "input_schema": {
                "type": "object",
                "properties": {
                    "origin": {"type": "string"},
                    "destination": {"type": "string"},
                    "departure_date": {"type": "string", "format": "date"},
                    "travelers": {"type": "integer", "enum": [1, 2, 3, 4, 5, 6]},
                },
                "required": ["origin", "destination", "departure_date"],
                "additionalProperties": False,
            },
        },
        {
            "name": "search_hotels",
            "strict": True,
            "input_schema": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"},
                    "check_in": {"type": "string", "format": "date"},
                    "guests": {"type": "integer", "enum": [1, 2, 3, 4]},
                },
                "required": ["city", "check_in"],
                "additionalProperties": False,
            },
        },
    ],
)

print(response)
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const tools: Anthropic.Tool[] = [
  {
    name: "search_flights",
    strict: true,
    input_schema: {
      type: "object",
      properties: {
        origin: { type: "string" },
        destination: { type: "string" },
        departure_date: { type: "string", format: "date" },
        travelers: { type: "integer", enum: [1, 2, 3, 4, 5, 6] }
      },
      required: ["origin", "destination", "departure_date"],
      additionalProperties: false
    }
  },
  {
    name: "search_hotels",
    strict: true,
    input_schema: {
      type: "object",
      properties: {
        city: { type: "string" },
        check_in: { type: "string", format: "date" },
        guests: { type: "integer", enum: [1, 2, 3, 4] }
      },
      required: ["city", "check_in"],
      additionalProperties: false
    }
  }
];

const response = await client.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content:
        "Help me plan a trip from New York to Paris for 2 people, departing June 1, 2026"
    }
  ],
  tools: tools
});

console.log(response);
```

```csharp C#
using System.Text.Json;
using Anthropic;
using Anthropic.Models.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var parameters = new MessageCreateParams
        {
            Model = Model.ClaudeOpus4_7,
            MaxTokens = 1024,
            Messages = [new() { Role = Role.User, Content = "Help me plan a trip from New York to Paris for 2 people, departing June 1, 2026" }],
            Tools = [
                new ToolUnion(new Tool()
                {
                    Name = "search_flights",
                    Strict = true,
                    InputSchema = new InputSchema(new Dictionary<string, JsonElement>
                    {
                        ["properties"] = JsonSerializer.SerializeToElement(new Dictionary<string, object>
                        {
                            ["origin"] = new { type = "string" },
                            ["destination"] = new { type = "string" },
                            ["departure_date"] = new { type = "string", format = "date" },
                            ["travelers"] = new { type = "integer", @enum = new[] { 1, 2, 3, 4, 5, 6 } },
                        }),
                        ["required"] = JsonSerializer.SerializeToElement(new[] { "origin", "destination", "departure_date" }),
                        ["additionalProperties"] = JsonSerializer.SerializeToElement(false),
                    }),
                }),
                new ToolUnion(new Tool()
                {
                    Name = "search_hotels",
                    Strict = true,
                    InputSchema = new InputSchema(new Dictionary<string, JsonElement>
                    {
                        ["properties"] = JsonSerializer.SerializeToElement(new Dictionary<string, object>
                        {
                            ["city"] = new { type = "string" },
                            ["check_in"] = new { type = "string", format = "date" },
                            ["guests"] = new { type = "integer", @enum = new[] { 1, 2, 3, 4 } },
                        }),
                        ["required"] = JsonSerializer.SerializeToElement(new[] { "city", "check_in" }),
                        ["additionalProperties"] = JsonSerializer.SerializeToElement(false),
                    }),
                }),
            ]
        };

        var message = await client.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
```

```go Go hidelines={1..11,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_7,
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("Help me plan a trip from New York to Paris for 2 people, departing June 1, 2026")),
		},
		Tools: []anthropic.ToolUnionParam{
			{OfTool: &anthropic.ToolParam{
				Name:   "search_flights",
				Strict: anthropic.Bool(true),
				InputSchema: anthropic.ToolInputSchemaParam{
					Properties: map[string]any{
						"origin":         map[string]any{"type": "string"},
						"destination":    map[string]any{"type": "string"},
						"departure_date": map[string]any{"type": "string", "format": "date"},
						"travelers":      map[string]any{"type": "integer", "enum": []int{1, 2, 3, 4, 5, 6}},
					},
					Required: []string{"origin", "destination", "departure_date"},
					ExtraFields: map[string]any{
						"additionalProperties": false,
					},
				}}},
			{OfTool: &anthropic.ToolParam{
				Name:   "search_hotels",
				Strict: anthropic.Bool(true),
				InputSchema: anthropic.ToolInputSchemaParam{
					Properties: map[string]any{
						"city":     map[string]any{"type": "string"},
						"check_in": map[string]any{"type": "string", "format": "date"},
						"guests":   map[string]any{"type": "integer", "enum": []int{1, 2, 3, 4}},
					},
					Required: []string{"city", "check_in"},
					ExtraFields: map[string]any{
						"additionalProperties": false,
					},
				}}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java hidelines={1..12,-1..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.JsonValue;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.Tool;
import com.anthropic.models.messages.Tool.InputSchema;
import java.util.List;
import java.util.Map;

void main() {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    InputSchema flightsSchema = InputSchema.builder()
        .properties(
            JsonValue.from(
                Map.of(
                    "origin", Map.of("type", "string"),
                    "destination", Map.of("type", "string"),
                    "departure_date", Map.of("type", "string", "format", "date"),
                    "travelers", Map.of("type", "integer", "enum", List.of(1, 2, 3, 4, 5, 6))
                )
            )
        )
        .putAdditionalProperty("required", JsonValue.from(List.of("origin", "destination", "departure_date")))
        .putAdditionalProperty("additionalProperties", JsonValue.from(false))
        .build();

    InputSchema hotelsSchema = InputSchema.builder()
        .properties(
            JsonValue.from(
                Map.of(
                    "city", Map.of("type", "string"),
                    "check_in", Map.of("type", "string", "format", "date"),
                    "guests", Map.of("type", "integer", "enum", List.of(1, 2, 3, 4))
                )
            )
        )
        .putAdditionalProperty("required", JsonValue.from(List.of("city", "check_in")))
        .putAdditionalProperty("additionalProperties", JsonValue.from(false))
        .build();

    MessageCreateParams params = MessageCreateParams.builder()
        .model(Model.CLAUDE_OPUS_4_7)
        .maxTokens(1024L)
        .addUserMessage("Help me plan a trip from New York to Paris for 2 people, departing June 1, 2026")
        .addTool(
            Tool.builder()
                .name("search_flights")
                .strict(true)
                .inputSchema(flightsSchema)
                .build()
        )
        .addTool(
            Tool.builder()
                .name("search_hotels")
                .strict(true)
                .inputSchema(hotelsSchema)
                .build()
        )
        .build();

    Message response = client.messages().create(params);
    IO.println(response);
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$message = $client->messages->create(
    maxTokens: 1024,
    messages: [
        ['role' => 'user', 'content' => 'Help me plan a trip from New York to Paris for 2 people, departing June 1, 2026']
    ],
    model: 'claude-opus-4-7',
    tools: [
        [
            'name' => 'search_flights',
            'strict' => true,
            'input_schema' => [
                'type' => 'object',
                'properties' => [
                    'origin' => ['type' => 'string'],
                    'destination' => ['type' => 'string'],
                    'departure_date' => ['type' => 'string', 'format' => 'date'],
                    'travelers' => ['type' => 'integer', 'enum' => [1, 2, 3, 4, 5, 6]]
                ],
                'required' => ['origin', 'destination', 'departure_date'],
                'additionalProperties' => false
            ]
        ],
        [
            'name' => 'search_hotels',
            'strict' => true,
            'input_schema' => [
                'type' => 'object',
                'properties' => [
                    'city' => ['type' => 'string'],
                    'check_in' => ['type' => 'string', 'format' => 'date'],
                    'guests' => ['type' => 'integer', 'enum' => [1, 2, 3, 4]]
                ],
                'required' => ['city', 'check_in'],
                'additionalProperties' => false
            ]
        ]
    ],
);

echo $message->content[0]->text;
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

message = client.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 1024,
  messages: [
    { role: "user", content: "Help me plan a trip from New York to Paris for 2 people, departing June 1, 2026" }
  ],
  tools: [
    {
      name: "search_flights",
      strict: true,
      input_schema: {
        type: "object",
        properties: {
          origin: { type: "string" },
          destination: { type: "string" },
          departure_date: { type: "string", format: "date" },
          travelers: { type: "integer", enum: [1, 2, 3, 4, 5, 6] }
        },
        required: ["origin", "destination", "departure_date"],
        additionalProperties: false
      }
    },
    {
      name: "search_hotels",
      strict: true,
      input_schema: {
        type: "object",
        properties: {
          city: { type: "string" },
          check_in: { type: "string", format: "date" },
          guests: { type: "integer", enum: [1, 2, 3, 4] }
        },
        required: ["city", "check_in"],
        additionalProperties: false
      }
    }
  ]
)
puts message
```

</CodeGroup>

</section>

## Data retention

Strict tool use compiles tool `input_schema` definitions into grammars using the same pipeline as [structured outputs](/docs/en/build-with-claude/structured-outputs). Tool schemas are temporarily cached for up to 24 hours since last use. Prompts and responses are not retained beyond the API response.

Strict tool use is HIPAA eligible, but **PHI must not be included in tool schema definitions**. The API caches compiled schemas separately from message content, and these cached schemas do not receive the same PHI protections as prompts and responses. Do not include PHI in `input_schema` property names, `enum` values, `const` values, or `pattern` regular expressions. PHI should only appear in message content (prompts and responses), where it is protected under HIPAA safeguards.

For ZDR and HIPAA eligibility across all features, see [API and data retention](/docs/en/build-with-claude/api-and-data-retention).
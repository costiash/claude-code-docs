# Structured outputs

Get validated JSON results from agent workflows

---

Structured outputs constrain Claude's responses to follow a specific schema, ensuring valid, parseable output for downstream processing. Two complementary features are available:

- **JSON outputs** (`output_config.format`): Get Claude's response in a specific JSON format
- **Strict tool use** (`strict: true`): Guarantee schema validation on tool names and inputs

These features can be used independently or together in the same request.

<Note>
Structured outputs are generally available on the Claude API and Amazon Bedrock for Claude Opus 4.6, Claude Sonnet 4.6, Claude Sonnet 4.5, Claude Opus 4.5, and Claude Haiku 4.5. Structured outputs remain in public beta on Microsoft Foundry.
</Note>

<Note>
Prompts and responses using structured outputs are processed with [Zero Data Retention (ZDR)](/docs/en/build-with-claude/zero-data-retention). However, the JSON schema itself is temporarily cached for up to 24 hours for optimization purposes. No prompt or response data is retained.
</Note>

<Tip>
**Migrating from beta?** The `output_format` parameter has moved to `output_config.format`, and beta headers are no longer required. The old beta header (`structured-outputs-2025-11-13`) and `output_format` parameter will continue working for a transition period. See code examples below for the updated API shape.
</Tip>

## Why use structured outputs

Without structured outputs, Claude can generate malformed JSON responses or invalid tool inputs that break your applications. Even with careful prompting, you may encounter:
- Parsing errors from invalid JSON syntax
- Missing required fields
- Inconsistent data types
- Schema violations requiring error handling and retries

Structured outputs guarantee schema-compliant responses through constrained decoding:
- **Always valid**: No more `JSON.parse()` errors
- **Type safe**: Guaranteed field types and required fields
- **Reliable**: No retries needed for schema violations

## JSON outputs

JSON outputs control Claude's response format, ensuring Claude returns valid JSON matching your schema. Use JSON outputs when you need to:

- Control Claude's response format
- Extract data from images or text
- Generate structured reports
- Format API responses

### Quick start

<CodeGroup>

```bash Shell
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan and wants to schedule a demo for next Tuesday at 2pm."
      }
    ],
    "output_config": {
      "format": {
        "type": "json_schema",
        "schema": {
          "type": "object",
          "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "plan_interest": {"type": "string"},
            "demo_requested": {"type": "boolean"}
          },
          "required": ["name", "email", "plan_interest", "demo_requested"],
          "additionalProperties": false
        }
      }
    }
  }'
```

```python Python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan and wants to schedule a demo for next Tuesday at 2pm.",
        }
    ],
    output_config={
        "format": {
            "type": "json_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "plan_interest": {"type": "string"},
                    "demo_requested": {"type": "boolean"},
                },
                "required": ["name", "email", "plan_interest", "demo_requested"],
                "additionalProperties": False,
            },
        }
    },
)
print(response.content[0].text)
```

```typescript TypeScript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY
});

const response = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content:
        "Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan and wants to schedule a demo for next Tuesday at 2pm."
    }
  ],
  output_config: {
    format: {
      type: "json_schema",
      schema: {
        type: "object",
        properties: {
          name: { type: "string" },
          email: { type: "string" },
          plan_interest: { type: "string" },
          demo_requested: { type: "boolean" }
        },
        required: ["name", "email", "plan_interest", "demo_requested"],
        additionalProperties: false
      }
    }
  }
});
console.log(response.content[0].text);
```

```java Java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.*;

AnthropicClient client = AnthropicOkHttpClient.fromEnv();

// Java SDK uses class-based structured outputs
// See the Java SDK page for annotation-based approach
MessageCreateParams params = MessageCreateParams.builder()
    .model(Model.CLAUDE_OPUS_4_6)
    .maxTokens(1024)
    .addUserMessage("Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan.")
    .build();

Message message = client.beta().messages().create(params);
System.out.println(message.content());
```

```go Go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	response, _ := client.Messages.New(context.Background(),
		anthropic.MessageNewParams{
			Model:     anthropic.ModelClaudeOpus4_6,
			MaxTokens: 1024,
			Messages: []anthropic.MessageParam{
				anthropic.NewUserMessage(
					anthropic.NewTextBlock("Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan."),
				),
			},
			OutputConfig: anthropic.OutputConfigParam{
				Format: anthropic.JSONOutputFormatParam{
					Schema: map[string]interface{}{
						"type": "object",
						"properties": map[string]interface{}{
							"name":           map[string]string{"type": "string"},
							"email":          map[string]string{"type": "string"},
							"plan_interest":  map[string]string{"type": "string"},
							"demo_requested": map[string]string{"type": "boolean"},
						},
						"required":             []string{"name", "email", "plan_interest", "demo_requested"},
						"additionalProperties": false,
					},
				},
			},
		})

	fmt.Println(response.Content[0].Text)
}
```

```ruby Ruby
require "anthropic"

client = Anthropic::Client.new

response = client.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content: "Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan."
    }
  ],
  output_config: {
    format: {
      type: "json_schema",
      schema: {
        type: "object",
        properties: {
          name: { type: "string" },
          email: { type: "string" },
          plan_interest: { type: "string" },
          demo_requested: { type: "boolean" }
        },
        required: ["name", "email", "plan_interest", "demo_requested"],
        additionalProperties: false
      }
    }
  }
)

puts response.content[0].text
```

```csharp C#
using Anthropic;

var client = new AnthropicClient();

var response = await client.Messages.CreateAsync(
    new MessageCreateParams
    {
        Model = "claude-opus-4-6",
        MaxTokens = 1024,
        Messages = new[]
        {
            new MessageParam
            {
                Role = "user",
                Content = "Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan."
            }
        },
        OutputConfig = new OutputConfig
        {
            Format = new JsonOutputFormat
            {
                Type = "json_schema",
                Schema = new
                {
                    type = "object",
                    properties = new
                    {
                        name = new { type = "string" },
                        email = new { type = "string" },
                        plan_interest = new { type = "string" },
                        demo_requested = new { type = "boolean" }
                    },
                    required = new[] { "name", "email", "plan_interest", "demo_requested" },
                    additionalProperties = false
                }
            }
        }
    });

Console.WriteLine(response.Content[0].Text);
```

```php PHP
<?php

use Anthropic\Client;

$client = new Client(
    apiKey: getenv("ANTHROPIC_API_KEY")
);

$response = $client->beta->messages->create([
    'model' => 'claude-opus-4-6',
    'max_tokens' => 1024,
    'betas' => ['structured-outputs-2025-11-13'],
    'messages' => [
        [
            'role' => 'user',
            'content' => 'Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan.'
        ]
    ],
    'output_format' => [
        'type' => 'json_schema',
        'schema' => [
            'type' => 'object',
            'properties' => [
                'name' => ['type' => 'string'],
                'email' => ['type' => 'string'],
                'plan_interest' => ['type' => 'string'],
                'demo_requested' => ['type' => 'boolean']
            ],
            'required' => ['name', 'email', 'plan_interest', 'demo_requested'],
            'additionalProperties' => false
        ]
    ]
]);

echo $response->content[0]->text;
```

</CodeGroup>

**Response format:** Valid JSON matching your schema in `response.content[0].text`

```json
{
  "name": "John Smith",
  "email": "john@example.com",
  "plan_interest": "Enterprise",
  "demo_requested": true
}
```

### How it works

<Steps>
  <Step title="Define your JSON schema">
    Create a JSON schema that describes the structure you want Claude to follow. The schema uses standard JSON Schema format with some limitations (see [JSON Schema limitations](#json-schema-limitations)).
  </Step>
  <Step title="Add the output_config.format parameter">
    Include the `output_config.format` parameter in your API request with `type: "json_schema"` and your schema definition.
  </Step>
  <Step title="Parse the response">
    Claude's response will be valid JSON matching your schema, returned in `response.content[0].text`.
  </Step>
</Steps>

### Working with JSON outputs in SDKs

The SDKs provide helpers that make it easier to work with JSON outputs, including schema transformation, automatic validation, and integration with popular schema libraries.

<Note>
SDK helper methods (like `.parse()` and Pydantic/Zod integration) still accept `output_format` as a convenience parameter. The SDK handles the translation to `output_config.format` internally. The examples below show the SDK helper syntax.
</Note>

#### Using native schema definitions

Instead of writing raw JSON schemas, you can use familiar schema definition tools in your language:

- **Python**: [Pydantic](https://docs.pydantic.dev/) models with `client.messages.parse()`
- **TypeScript**: [Zod](https://zod.dev/) schemas with `zodOutputFormat()`
- **Java**: Plain Java classes with automatic schema derivation via `outputFormat(Class<T>)`
- **Ruby**: `Anthropic::BaseModel` classes with `output_config: {format: Model}`
- **C#**, **Go**, **PHP**: Raw JSON schemas passed via `output_config`

<CodeGroup>

```python Python
from pydantic import BaseModel
from anthropic import Anthropic


class ContactInfo(BaseModel):
    name: str
    email: str
    plan_interest: str
    demo_requested: bool


client = Anthropic()

response = client.messages.parse(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan and wants to schedule a demo for next Tuesday at 2pm.",
        }
    ],
    output_format=ContactInfo,
)

print(response.parsed_output)
```

```typescript TypeScript
import Anthropic from "@anthropic-ai/sdk";
import { z } from "zod";
import { zodOutputFormat } from "@anthropic-ai/sdk/helpers/zod";

const ContactInfoSchema = z.object({
  name: z.string(),
  email: z.string(),
  plan_interest: z.string(),
  demo_requested: z.boolean()
});

const client = new Anthropic();

const response = await client.messages.parse({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content:
        "Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan and wants to schedule a demo for next Tuesday at 2pm."
    }
  ],
  output_config: { format: zodOutputFormat(ContactInfoSchema) }
});

// Guaranteed type-safe
console.log(response.parsed_output.email);
```

```java Java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.StructuredMessageCreateParams;
import com.anthropic.models.messages.Model;

class ContactInfo {
    public String name;
    public String email;
    public String planInterest;
    public boolean demoRequested;
}

AnthropicClient client = AnthropicOkHttpClient.fromEnv();

StructuredMessageCreateParams<ContactInfo> createParams = MessageCreateParams.builder()
  .model(Model.CLAUDE_OPUS_4_6)
  .maxTokens(1024)
  .outputFormat(ContactInfo.class)
  .addUserMessage("Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan and wants to schedule a demo for next Tuesday at 2pm.")
  .build();

var response = client.messages().create(createParams);
ContactInfo contact = response.output(ContactInfo.class);
System.out.println(contact.name + " (" + contact.email + ")");
```

```go Go
package main

import (
	"context"
	"encoding/json"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/invopop/jsonschema"
)

type ContactInfo struct {
	Name          string `json:"name" jsonschema:"description=Full name"`
	Email         string `json:"email" jsonschema:"description=Email address"`
	PlanInterest  string `json:"plan_interest" jsonschema:"description=Plan type"`
	DemoRequested bool   `json:"demo_requested" jsonschema:"description=Whether a demo was requested"`
}

func generateSchema(v any) map[string]any {
	r := jsonschema.Reflector{AllowAdditionalProperties: false, DoNotReference: true}
	s := r.Reflect(v)
	b, _ := json.Marshal(s)
	var m map[string]any
	json.Unmarshal(b, &m)
	return m
}

func main() {
	client := anthropic.NewClient()
	schema := generateSchema(&ContactInfo{})

	message, _ := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock(
				"Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan and wants to schedule a demo for next Tuesday at 2pm.",
			)),
		},
		OutputConfig: anthropic.OutputConfigParam{
			Format: anthropic.JSONOutputFormatParam{
				Schema: schema,
			},
		},
	})

	var contact ContactInfo
	json.Unmarshal([]byte(message.Content[0].AsResponseTextBlock().Text), &contact)
	fmt.Printf("%s (%s)\n", contact.Name, contact.Email)
}
```

```ruby Ruby
require "anthropic"

client = Anthropic::Client.new

class ContactInfo < Anthropic::BaseModel
  required :name, String
  required :email, String
  required :plan_interest, String
  required :demo_requested, Anthropic::Boolean
end

message = client.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [{
    role: "user",
    content: "Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan and wants to schedule a demo for next Tuesday at 2pm."
  }],
  output_config: {format: ContactInfo}
)

contact = message.parsed_output
puts "#{contact.name} (#{contact.email})"
```

```csharp C#
using System.Text.Json;
using Anthropic;
using Anthropic.Models.Messages;

var client = new AnthropicClient();

var response = await client.Messages.Create(new MessageCreateParams
{
    Model = "claude-opus-4-6",
    MaxTokens = 1024,
    Messages = [new() {
        Role = Role.User,
        Content = "Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan and wants to schedule a demo for next Tuesday at 2pm."
    }],
    OutputConfig = new OutputConfig
    {
        Format = new JsonOutputFormat
        {
            Schema = new Dictionary<string, JsonElement>
            {
                ["type"] = JsonSerializer.SerializeToElement("object"),
                ["properties"] = JsonSerializer.SerializeToElement(new
                {
                    name = new { type = "string" },
                    email = new { type = "string" },
                    plan_interest = new { type = "string" },
                    demo_requested = new { type = "boolean" },
                }),
                ["required"] = JsonSerializer.SerializeToElement(
                    new[] { "name", "email", "plan_interest", "demo_requested" }),
                ["additionalProperties"] = JsonSerializer.SerializeToElement(false),
            },
        },
    },
});

var json = (response.Content.First().Value as TextBlock)!.Text;
// JSON is guaranteed to match the schema
var contact = JsonSerializer.Deserialize<Dictionary<string, object>>(json);
Console.WriteLine($"{contact["name"]} ({contact["email"]})");
```

```php PHP
<?php

use Anthropic\Client;
use Anthropic\Messages\OutputConfig;
use Anthropic\Messages\JSONOutputFormat;

$client = new Client();

$response = $client->messages->create(
    maxTokens: 1024,
    messages: [
        ['role' => 'user', 'content' => 'Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan and wants to schedule a demo for next Tuesday at 2pm.'],
    ],
    model: 'claude-opus-4-6',
    outputConfig: OutputConfig::with(format: JSONOutputFormat::with(schema: [
        'type' => 'object',
        'properties' => [
            'name' => ['type' => 'string'],
            'email' => ['type' => 'string'],
            'plan_interest' => ['type' => 'string'],
            'demo_requested' => ['type' => 'boolean'],
        ],
        'required' => ['name', 'email', 'plan_interest', 'demo_requested'],
        'additionalProperties' => false,
    ])),
);

$data = json_decode($response->content[0]->text, true);
echo $data['name'] . ' (' . $data['email'] . ')';
```

</CodeGroup>

#### SDK-specific methods

Each SDK provides helpers that make working with structured outputs easier. See individual SDK pages for full details.

<Tabs>
<Tab title="Python">

**`client.messages.parse()` (Recommended)**

The `parse()` method automatically transforms your Pydantic model, validates the response, and returns a `parsed_output` attribute.

<section title="Example usage">

```python
from pydantic import BaseModel
import anthropic


class ContactInfo(BaseModel):
    name: str
    email: str
    plan_interest: str


client = anthropic.Anthropic()

response = client.messages.parse(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "..."}],
    output_format=ContactInfo,
)

# Access the parsed output directly
contact = response.parsed_output
print(contact.name, contact.email)
```

</section>

**`transform_schema()` helper**

For when you need to manually transform schemas before sending, or when you want to modify a Pydantic-generated schema. Unlike `client.messages.parse()`, which transforms provided schemas automatically, this gives you the transformed schema so you can further customize it.

<section title="Example usage">

```python
from anthropic import transform_schema
from pydantic import TypeAdapter

# First convert Pydantic model to JSON schema, then transform
schema = TypeAdapter(ContactInfo).json_schema()
schema = transform_schema(schema)
# Modify schema if needed
schema["properties"]["custom_field"] = {"type": "string"}

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "..."}],
    output_config={
        "format": {"type": "json_schema", "schema": schema},
    },
)
```

</section>

</Tab>
<Tab title="TypeScript">

**`client.messages.parse()` with `zodOutputFormat()`**

The `parse()` method accepts a Zod schema, validates the response, and returns a `parsed_output` attribute with the inferred TypeScript type matching the schema.

<section title="Example usage">

```typescript
import Anthropic from "@anthropic-ai/sdk";
import { z } from "zod";
import { zodOutputFormat } from "@anthropic-ai/sdk/helpers/zod";

const ContactInfo = z.object({
  name: z.string(),
  email: z.string(),
  planInterest: z.string()
});

const client = new Anthropic();

const response = await client.messages.parse({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "..." }],
  output_config: { format: zodOutputFormat(ContactInfo) }
});

// Guaranteed type-safe
console.log(response.parsed_output.email);
```

</section>

</Tab>
<Tab title="Java">

**`outputFormat(Class<T>)` method**

Pass a Java class to `outputFormat()` and the SDK automatically derives a JSON schema, validates it, and returns a `StructuredMessageCreateParams<T>`. Access the parsed result via `response.output(Class<T>)`.

<section title="Example usage">

```java
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.StructuredMessageCreateParams;
import com.anthropic.models.messages.Model;

class ContactInfo {
    public String name;
    public String email;
    public String planInterest;
}

StructuredMessageCreateParams<ContactInfo> createParams = MessageCreateParams.builder()
  .model(Model.CLAUDE_OPUS_4_6)
  .maxTokens(1024)
  .outputFormat(ContactInfo.class)
  .addUserMessage("...")
  .build();

var response = client.messages().create(createParams);
ContactInfo contact = response.output(ContactInfo.class);
System.out.println(contact.name + " (" + contact.email + ")");
```

</section>

<section title="Generic type erasure">

Generic type information for fields is retained in the class's metadata, but generic type erasure applies in other scopes. While a JSON schema can be derived from a `BookList.books` field with type `List<Book>`, a valid JSON schema cannot be derived from a local variable of that same type.

If an error occurs while converting a JSON response to a Java class instance, the error message will include the JSON response to assist in diagnosis. If your JSON response may contain sensitive information, avoid logging it directly, or ensure that you redact any sensitive details from the error message.

</section>

<section title="Local schema validation">

Structured outputs support a [subset of the JSON Schema language](/docs/en/build-with-claude/structured-outputs#json-schema-limitations). Schemas are generated automatically from classes to align with this subset. The `outputFormat(Class<T>)` method performs a validation check on the schema derived from the specified class.

Key points:

- **Local validation** occurs without sending requests to the remote AI model.
- **Remote validation** is also performed by the AI model upon receiving the JSON schema.
- **Version compatibility**: Local validation may fail while remote validation succeeds if the SDK version is outdated.
- **Disabling local validation**: Pass `JsonSchemaLocalValidation.NO` if you encounter compatibility issues:

```java
import com.anthropic.core.JsonSchemaLocalValidation;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.StructuredMessageCreateParams;
import com.anthropic.models.messages.Model;

StructuredMessageCreateParams<BookList> createParams = MessageCreateParams.builder()
  .model(Model.CLAUDE_OPUS_4_6)
  .maxTokens(2048)
  .outputFormat(BookList.class, JsonSchemaLocalValidation.NO)
  .addUserMessage("List some famous late twentieth century novels.")
  .build();
```

</section>

<section title="Streaming">

Structured outputs can also be used with streaming. As responses arrive in stream events, you need to accumulate the full response before deserializing the JSON.

Use `BetaMessageAccumulator` to collect the JSON strings from the stream. Once accumulated, call `BetaMessageAccumulator.message(Class<T>)` to convert the accumulated `BetaMessage` into a `StructuredMessage`, which automatically deserializes the JSON into your Java class.

</section>

<section title="JSON schema properties">

When a JSON schema is derived from your Java classes, all properties represented by `public` fields or `public` getter methods are included by default. Non-`public` fields and getter methods are excluded.

You can control visibility with annotations:

- `@JsonIgnore` excludes a `public` field or getter method
- `@JsonProperty` includes a non-`public` field or getter method

If you define `private` fields with `public` getter methods, the property name is derived from the getter (e.g., `private` field `myValue` with `public` method `getMyValue()` produces a `"myValue"` property). To use a non-conventional getter name, annotate the method with `@JsonProperty`.

Each class must define at least one property for the JSON schema. A validation error occurs if no fields or getter methods can produce schema properties, such as when:

- There are no fields or getter methods in the class
- All `public` members are annotated with `@JsonIgnore`
- All non-`public` members lack `@JsonProperty` annotations
- A field uses a `Map` type, which produces an empty `"properties"` field

</section>

<section title="Annotations (Jackson and Swagger)">

You can use Jackson Databind annotations to enrich the JSON schema derived from your Java classes:

```java
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;

class Person {

  @JsonPropertyDescription("The first name and surname of the person")
  public String name;

  public int birthYear;

  @JsonPropertyDescription("The year the person died, or 'present' if the person is living.")
  public String deathYear;
}

@JsonClassDescription("The details of one published book")
class Book {

  public String title;
  public Person author;

  @JsonPropertyDescription("The year in which the book was first published.")
  public int publicationYear;

  @JsonIgnore
  public String genre;
}

class BookList {

  public List<Book> books;
}
```

Annotation summary:

- `@JsonClassDescription`: Add a description to a class
- `@JsonPropertyDescription`: Add a description to a field or getter method
- `@JsonIgnore`: Exclude a `public` field or getter from the schema
- `@JsonProperty`: Include a non-`public` field or getter in the schema

If you use `@JsonProperty(required = false)`, the `false` value is ignored. Anthropic JSON schemas must mark all properties as required.

You can also use OpenAPI Swagger 2 `@Schema` and `@ArraySchema` annotations for type-specific constraints:

```java
import io.swagger.v3.oas.annotations.media.ArraySchema;
import io.swagger.v3.oas.annotations.media.Schema;

class Article {

  @ArraySchema(minItems = 1)
  public List<String> authors;

  public String title;

  @Schema(format = "date")
  public String publicationDate;

  @Schema(minimum = "1")
  public int pageCount;
}
```

Local validation checks that you haven't used any unsupported constraint keywords, but constraint values aren't validated locally. For example, an unsupported `"format"` value may pass local validation but cause a remote error.

If you use both Jackson and Swagger annotations to set the same schema field, the Jackson annotation takes precedence.

</section>

</Tab>
<Tab title="Go">

**Raw JSON schemas via `OutputConfigParam`**

The Go SDK works with raw JSON schemas. Define a Go struct with json tags, generate the JSON schema (for example, using `invopop/jsonschema`), and unmarshal the response text into your struct.

<section title="Example usage">

```go
package main

import (
	"context"
	"encoding/json"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/invopop/jsonschema"
)

type ContactInfo struct {
	Name         string `json:"name" jsonschema:"description=Full name"`
	Email        string `json:"email" jsonschema:"description=Email address"`
	PlanInterest string `json:"plan_interest" jsonschema:"description=Plan type"`
}

func generateSchema(v any) map[string]any {
	r := jsonschema.Reflector{AllowAdditionalProperties: false, DoNotReference: true}
	s := r.Reflect(v)
	b, _ := json.Marshal(s)
	var m map[string]any
	json.Unmarshal(b, &m)
	return m
}

func main() {
	client := anthropic.NewClient()
	schema := generateSchema(&ContactInfo{})

	message, _ := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock(
				"Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan.",
			)),
		},
		OutputConfig: anthropic.OutputConfigParam{
			Format: anthropic.JSONOutputFormatParam{
				Schema: schema,
			},
		},
	})

	var contact ContactInfo
	json.Unmarshal([]byte(message.Content[0].AsResponseTextBlock().Text), &contact)
	fmt.Printf("%s (%s)\n", contact.Name, contact.Email)
}
```

</section>

</Tab>
<Tab title="Ruby">

**`output_config: {format: Model}` with `parsed_output`**

Define a model class extending `Anthropic::BaseModel` and pass it as the format to `messages.create()`. The response includes a `parsed_output` attribute with a typed Ruby object.

<section title="Example usage">

```ruby
require "anthropic"

class ContactInfo < Anthropic::BaseModel
  required :name, String
  required :email, String
  required :plan_interest, String
end

client = Anthropic::Client.new

message = client.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [{role: "user", content: "..."}],
  output_config: {format: ContactInfo}
)

contact = message.parsed_output
puts "#{contact.name} (#{contact.email})"
```

</section>

<section title="Advanced model features">

The Ruby SDK supports additional model definition features for richer schemas:

- **`doc:` keyword:** Add descriptions to fields for more informative schema output
- **`Anthropic::ArrayOf[T]`:** Typed arrays with `min_length` and `max_length` constraints
- **`Anthropic::EnumOf[:a, :b]`:** Enum fields with constrained values
- **`Anthropic::UnionOf[T1, T2]`:** Union types mapped to `anyOf`

```ruby
class FamousNumber < Anthropic::BaseModel
  required :value, Float
  optional :reason, String, doc: "why is this number mathematically significant?"
end

class Output < Anthropic::BaseModel
  required :numbers, Anthropic::ArrayOf[FamousNumber], min_length: 3, max_length: 5
end

message = anthropic.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [{role: "user", content: "give me some famous numbers"}],
  output_config: {format: Output}
)

message.parsed_output
# => #<Output numbers=[#<FamousNumber value=3.14159... reason="Pi is...">...]>
```

</section>

</Tab>
<Tab title="C#">

**Raw JSON schemas via `OutputConfig`**

The C# SDK uses raw JSON schemas built programmatically with `JsonSerializer.SerializeToElement`. Deserialize the response JSON with `JsonSerializer.Deserialize`.

<section title="Example usage">

```csharp
using System.Text.Json;
using Anthropic;
using Anthropic.Models.Messages;

var client = new AnthropicClient();

var response = await client.Messages.Create(new MessageCreateParams
{
    Model = "claude-opus-4-6",
    MaxTokens = 1024,
    Messages = [new() {
        Role = Role.User,
        Content = "Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan."
    }],
    OutputConfig = new OutputConfig
    {
        Format = new JsonOutputFormat
        {
            Schema = new Dictionary<string, JsonElement>
            {
                ["type"] = JsonSerializer.SerializeToElement("object"),
                ["properties"] = JsonSerializer.SerializeToElement(new
                {
                    name = new { type = "string" },
                    email = new { type = "string" },
                    plan_interest = new { type = "string" },
                }),
                ["required"] = JsonSerializer.SerializeToElement(
                    new[] { "name", "email", "plan_interest" }),
                ["additionalProperties"] = JsonSerializer.SerializeToElement(false),
            },
        },
    },
});

var json = (response.Content.First().Value as TextBlock)!.Text;
// JSON is guaranteed to match the schema
var contact = JsonSerializer.Deserialize<Dictionary<string, object>>(json);
Console.WriteLine($"{contact["name"]} ({contact["email"]})");
```

</section>

</Tab>
<Tab title="PHP">

**Raw JSON schemas via `OutputConfig::with()`**

The PHP SDK passes raw JSON schemas as associative arrays via `OutputConfig::with()`. Decode the response with `json_decode()`.

<section title="Example usage">

```php
<?php

use Anthropic\Client;
use Anthropic\Messages\OutputConfig;
use Anthropic\Messages\JSONOutputFormat;

$client = new Client();

$response = $client->messages->create(
    maxTokens: 1024,
    messages: [
        ['role' => 'user', 'content' => 'Extract the key information from this email: John Smith (john@example.com) is interested in our Enterprise plan.'],
    ],
    model: 'claude-opus-4-6',
    outputConfig: OutputConfig::with(format: JSONOutputFormat::with(schema: [
        'type' => 'object',
        'properties' => [
            'name' => ['type' => 'string'],
            'email' => ['type' => 'string'],
            'plan_interest' => ['type' => 'string'],
        ],
        'required' => ['name', 'email', 'plan_interest'],
        'additionalProperties' => false,
    ])),
);

$data = json_decode($response->content[0]->text, true);
echo $data['name'] . ' (' . $data['email'] . ')';
```

</section>

</Tab>
</Tabs>

#### How SDK transformation works

The Python and TypeScript SDKs automatically transform schemas with unsupported features:

1. **Remove unsupported constraints** (e.g., `minimum`, `maximum`, `minLength`, `maxLength`)
2. **Update descriptions** with constraint info (e.g., "Must be at least 100"), when the constraint is not directly supported with structured outputs
3. **Add `additionalProperties: false`** to all objects
4. **Filter string formats** to supported list only
5. **Validate responses** against your original schema (with all constraints)

This means Claude receives a simplified schema, but your code still enforces all constraints through validation.

**Example:** A Pydantic field with `minimum: 100` becomes a plain integer in the sent schema, but the description is updated to "Must be at least 100", and the SDK validates the response against the original constraint.

### Common use cases

<section title="Data extraction">

Extract structured data from unstructured text:

<CodeGroup>

```python Python
from pydantic import BaseModel
from typing import List


class Invoice(BaseModel):
    invoice_number: str
    date: str
    total_amount: float
    line_items: List[dict]
    customer_name: str


response = client.messages.parse(
    model="claude-opus-4-6",
    output_format=Invoice,
    messages=[
        {"role": "user", "content": f"Extract invoice data from: {invoice_text}"}
    ],
)
```

```typescript TypeScript
import { z } from "zod";
import { zodOutputFormat } from "@anthropic-ai/sdk/helpers/zod";

const InvoiceSchema = z.object({
  invoice_number: z.string(),
  date: z.string(),
  total_amount: z.number(),
  line_items: z.array(z.record(z.string(), z.any())),
  customer_name: z.string()
});

const response = await client.messages.create({
  model: "claude-opus-4-6",
  output_config: { format: zodOutputFormat(InvoiceSchema) },
  messages: [{ role: "user", content: `Extract invoice data from: ${invoiceText}` }]
});
```

</CodeGroup>

</section>

<section title="Classification">

Classify content with structured categories:

<CodeGroup>

```python Python
from pydantic import BaseModel
from typing import List


class Classification(BaseModel):
    category: str
    confidence: float
    tags: List[str]
    sentiment: str


response = client.messages.parse(
    model="claude-opus-4-6",
    output_format=Classification,
    messages=[{"role": "user", "content": f"Classify this feedback: {feedback_text}"}],
)
```

```typescript TypeScript
import { z } from "zod";
import { zodOutputFormat } from "@anthropic-ai/sdk/helpers/zod";

const ClassificationSchema = z.object({
  category: z.string(),
  confidence: z.number(),
  tags: z.array(z.string()),
  sentiment: z.string()
});

const response = await client.messages.create({
  model: "claude-opus-4-6",
  output_config: { format: zodOutputFormat(ClassificationSchema) },
  messages: [{ role: "user", content: `Classify this feedback: ${feedbackText}` }]
});
```

</CodeGroup>

</section>

<section title="API response formatting">

Generate API-ready responses:

<CodeGroup>

```python Python
from pydantic import BaseModel
from typing import List, Optional


class APIResponse(BaseModel):
    status: str
    data: dict
    errors: Optional[List[dict]]
    metadata: dict


response = client.messages.parse(
    model="claude-opus-4-6",
    output_format=APIResponse,
    messages=[{"role": "user", "content": "Process this request: ..."}],
)
```

```typescript TypeScript
import { z } from "zod";
import { zodOutputFormat } from "@anthropic-ai/sdk/helpers/zod";

const APIResponseSchema = z.object({
  status: z.string(),
  data: z.record(z.string(), z.any()),
  errors: z.array(z.record(z.string(), z.any())).optional(),
  metadata: z.record(z.string(), z.any())
});

const response = await client.messages.create({
  model: "claude-opus-4-6",
  output_config: { format: zodOutputFormat(APIResponseSchema) },
  messages: [{ role: "user", content: "Process this request: ..." }]
});
```

</CodeGroup>

</section>

## Strict tool use

Strict tool use validates tool parameters, ensuring Claude calls your functions with correctly-typed arguments. Use strict tool use when you need to:

- Validate tool parameters
- Build agentic workflows
- Ensure type-safe function calls
- Handle complex tools with nested properties

### Why strict tool use matters for agents

Building reliable agentic systems requires guaranteed schema conformance. Without strict mode, Claude might return incompatible types (`"2"` instead of `2`) or missing required fields, breaking your functions and causing runtime errors.

Strict tool use guarantees type-safe parameters:
- Functions receive correctly-typed arguments every time
- No need to validate and retry tool calls
- Production-ready agents that work consistently at scale

For example, suppose a booking system needs `passengers: int`. Without strict mode, Claude might provide `passengers: "two"` or `passengers: "2"`. With `strict: true`, the response will always contain `passengers: 2`.

### Quick start

<CodeGroup>

```bash Shell
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-6",
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

```python Python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-6",
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

```typescript TypeScript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY
});

const response = await client.messages.create({
  model: "claude-opus-4-6",
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

</CodeGroup>

**Response format:** Tool use blocks with validated inputs in `response.content[x].input`

```json
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

### How it works

<Steps>
  <Step title="Define your tool schema">
    Create a JSON schema for your tool's `input_schema`. The schema uses standard JSON Schema format with some limitations (see [JSON Schema limitations](#json-schema-limitations)).
  </Step>
  <Step title="Add strict: true">
    Set `"strict": true` as a top-level property in your tool definition, alongside `name`, `description`, and `input_schema`.
  </Step>
  <Step title="Handle tool calls">
    When Claude uses the tool, the `input` field in the tool_use block will strictly follow your `input_schema`, and the `name` will always be valid.
  </Step>
</Steps>

### Common use cases

<section title="Validated tool inputs">

Ensure tool parameters exactly match your schema:

<CodeGroup>

```python Python
response = client.messages.create(
    model="claude-opus-4-6",
    messages=[{"role": "user", "content": "Search for flights to Tokyo"}],
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
```

```typescript TypeScript
const response = await client.messages.create({
  model: "claude-opus-4-6",
  messages: [{ role: "user", content: "Search for flights to Tokyo" }],
  tools: [
    {
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
    }
  ]
});
```

</CodeGroup>

</section>

<section title="Agentic workflow with multiple validated tools">

Build reliable multi-step agents with guaranteed tool parameters:

<CodeGroup>

```python Python
response = client.messages.create(
    model="claude-opus-4-6",
    messages=[{"role": "user", "content": "Help me plan a trip to Paris for 2 people"}],
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
```

```typescript TypeScript
const response = await client.messages.create({
  model: "claude-opus-4-6",
  messages: [{ role: "user", content: "Help me plan a trip to Paris for 2 people" }],
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
});
```

</CodeGroup>

</section>

## Using both features together

JSON outputs and strict tool use solve different problems and can be used together:

- **JSON outputs** control Claude's response format (what Claude says)
- **Strict tool use** validates tool parameters (how Claude calls your functions)

When combined, Claude can call tools with guaranteed-valid parameters AND return structured JSON responses. This is useful for agentic workflows where you need both reliable tool calls and structured final outputs.

<CodeGroup>

```python Python
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Help me plan a trip to Paris for next month"}
    ],
    # JSON outputs: structured response format
    output_config={
        "format": {
            "type": "json_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string"},
                    "next_steps": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["summary", "next_steps"],
                "additionalProperties": False,
            },
        }
    },
    # Strict tool use: guaranteed tool parameters
    tools=[
        {
            "name": "search_flights",
            "strict": True,
            "input_schema": {
                "type": "object",
                "properties": {
                    "destination": {"type": "string"},
                    "date": {"type": "string", "format": "date"},
                },
                "required": ["destination", "date"],
                "additionalProperties": False,
            },
        }
    ],
)
```

```typescript TypeScript
const response = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Help me plan a trip to Paris for next month" }],
  // JSON outputs: structured response format
  output_config: {
    format: {
      type: "json_schema",
      schema: {
        type: "object",
        properties: {
          summary: { type: "string" },
          next_steps: { type: "array", items: { type: "string" } }
        },
        required: ["summary", "next_steps"],
        additionalProperties: false
      }
    }
  },
  // Strict tool use: guaranteed tool parameters
  tools: [
    {
      name: "search_flights",
      strict: true,
      input_schema: {
        type: "object",
        properties: {
          destination: { type: "string" },
          date: { type: "string", format: "date" }
        },
        required: ["destination", "date"],
        additionalProperties: false
      }
    }
  ]
});
```

</CodeGroup>

## Important considerations

### Grammar compilation and caching

Structured outputs use constrained sampling with compiled grammar artifacts. This introduces some performance characteristics to be aware of:

- **First request latency**: The first time you use a specific schema, there will be additional latency while the grammar is compiled
- **Automatic caching**: Compiled grammars are cached for 24 hours from last use, making subsequent requests much faster
- **Cache invalidation**: The cache is invalidated if you change:
  - The JSON schema structure
  - The set of tools in your request (when using both structured outputs and tool use)
  - Changing only `name` or `description` fields does not invalidate the cache

### Prompt modification and token costs

When using structured outputs, Claude automatically receives an additional system prompt explaining the expected output format. This means:

- Your input token count will be slightly higher
- The injected prompt costs you tokens like any other system prompt
- Changing the `output_config.format` parameter will invalidate any [prompt cache](/docs/en/build-with-claude/prompt-caching) for that conversation thread

### JSON Schema limitations

Structured outputs support standard JSON Schema with some limitations. Both JSON outputs and strict tool use share these limitations.

<section title="Supported features">

- All basic types: object, array, string, integer, number, boolean, null
- `enum` (strings, numbers, bools, or nulls only - no complex types)
- `const`
- `anyOf` and `allOf` (with limitations - `allOf` with `$ref` not supported)
- `$ref`, `$def`, and `definitions` (external `$ref` not supported)
- `default` property for all supported types
- `required` and `additionalProperties` (must be set to `false` for objects)
- String formats: `date-time`, `time`, `date`, `duration`, `email`, `hostname`, `uri`, `ipv4`, `ipv6`, `uuid`
- Array `minItems` (only values 0 and 1 supported)

</section>

<section title="Not supported">

- Recursive schemas
- Complex types within enums
- External `$ref` (e.g., `'$ref': 'http://...'`)
- Numerical constraints (`minimum`, `maximum`, `multipleOf`, etc.)
- String constraints (`minLength`, `maxLength`)
- Array constraints beyond `minItems` of 0 or 1
- `additionalProperties` set to anything other than `false`

If you use an unsupported feature, you'll receive a 400 error with details.

</section>

<section title="Pattern support (regex)">

**Supported regex features:**
- Full matching (`^...$`) and partial matching
- Quantifiers: `*`, `+`, `?`, simple `{n,m}` cases
- Character classes: `[]`, `.`, `\d`, `\w`, `\s`
- Groups: `(...)`

**NOT supported:**
- Backreferences to groups (e.g., `\1`, `\2`)
- Lookahead/lookbehind assertions (e.g., `(?=...)`, `(?!...)`)
- Word boundaries: `\b`, `\B`
- Complex `{n,m}` quantifiers with large ranges

Simple regex patterns work well. Complex patterns may result in 400 errors.

</section>

<Tip>
The Python and TypeScript SDKs can automatically transform schemas with unsupported features by removing them and adding constraints to field descriptions. See [SDK-specific methods](#sdk-specific-methods) for details.
</Tip>

### Property ordering

When using structured outputs, properties in objects maintain their defined ordering from your schema, with one important caveat: **required properties appear first, followed by optional properties**.

For example, given this schema:

```json
{
  "type": "object",
  "properties": {
    "notes": { "type": "string" },
    "name": { "type": "string" },
    "email": { "type": "string" },
    "age": { "type": "integer" }
  },
  "required": ["name", "email"],
  "additionalProperties": false
}
```

The output will order properties as:

1. `name` (required, in schema order)
2. `email` (required, in schema order)
3. `notes` (optional, in schema order)
4. `age` (optional, in schema order)

This means the output might look like:

```json
{
  "name": "John Smith",
  "email": "john@example.com",
  "notes": "Interested in enterprise plan",
  "age": 35
}
```

If property order in the output is important to your application, ensure all properties are marked as required, or account for this reordering in your parsing logic.

### Invalid outputs

While structured outputs guarantee schema compliance in most cases, there are scenarios where the output may not match your schema:

**Refusals** (`stop_reason: "refusal"`)

Claude maintains its safety and helpfulness properties even when using structured outputs. If Claude refuses a request for safety reasons:

- The response will have `stop_reason: "refusal"`
- You'll receive a 200 status code
- You'll be billed for the tokens generated
- The output may not match your schema because the refusal message takes precedence over schema constraints

**Token limit reached** (`stop_reason: "max_tokens"`)

If the response is cut off due to reaching the `max_tokens` limit:

- The response will have `stop_reason: "max_tokens"`
- The output may be incomplete and not match your schema
- Retry with a higher `max_tokens` value to get the complete structured output

### Schema complexity limits

Structured outputs work by compiling your JSON schemas into a grammar that constrains Claude's output. More complex schemas produce larger grammars that take longer to compile. To protect against excessive compilation times, the API enforces several complexity limits.

#### Explicit limits

The following limits apply to all requests with `output_config.format` or `strict: true`:

| Limit | Value | Description |
|-------|-------|-------------|
| Strict tools per request | 20 | Maximum number of tools with `strict: true`. Non-strict tools don't count toward this limit. |
| Optional parameters | 24 | Total optional parameters across all strict tool schemas and JSON output schemas. Each parameter not listed in `required` counts toward this limit. |
| Parameters with union types | 16 | Total parameters that use `anyOf` or type arrays (e.g., `"type": ["string", "null"]`) across all strict schemas. These are especially expensive because they create exponential compilation cost. |

<Note>
These limits apply to the combined total across all strict schemas in a single request. For example, if you have 4 strict tools with 6 optional parameters each, you'll reach the 24-parameter limit even though no single tool seems complex.
</Note>

#### Additional internal limits

Beyond the explicit limits above, there are additional internal limits on the compiled grammar size. These limits exist because schema complexity doesn't reduce to a single dimension: features like optional parameters, union types, nested objects, and number of tools interact with each other in ways that can make the compiled grammar disproportionately large.

When these limits are exceeded, you'll receive a 400 error with the message "Schema is too complex for compilation." These errors mean the combined complexity of your schemas exceeds what can be efficiently compiled, even if each individual limit above is satisfied. As a final stop-gap, the API also enforces a **compilation timeout of 180 seconds**. Schemas that pass all explicit checks but produce very large compiled grammars may hit this timeout.

#### Tips for reducing schema complexity

If you're hitting complexity limits, try these strategies in order:

1. **Mark only critical tools as strict.** If you have many tools, reserve it for tools where schema violations cause real problems, and rely on Claude's natural adherence for simpler tools.

2. **Reduce optional parameters.** Make parameters `required` where possible. Each optional parameter roughly doubles a portion of the grammar's state space. If a parameter always has a reasonable default, consider making it required and having Claude provide that default explicitly.

3. **Simplify nested structures.** Deeply nested objects with optional fields compound the complexity. Flatten structures where possible.

4. **Split into multiple requests.** If you have many strict tools, consider splitting them across separate requests or sub-agents.

For persistent issues with valid schemas, [contact support](https://support.claude.com/en/articles/9015913-how-to-get-support) with your schema definition.

## Feature compatibility

**Works with:**
- **[Batch processing](/docs/en/build-with-claude/batch-processing)**: Process structured outputs at scale with 50% discount
- **[Token counting](/docs/en/build-with-claude/token-counting)**: Count tokens without compilation
- **[Streaming](/docs/en/build-with-claude/streaming)**: Stream structured outputs like normal responses
- **Combined usage**: Use JSON outputs (`output_config.format`) and strict tool use (`strict: true`) together in the same request

**Incompatible with:**
- **[Citations](/docs/en/build-with-claude/citations)**: Citations require interleaving citation blocks with text, which conflicts with strict JSON schema constraints. Returns 400 error if citations enabled with `output_config.format`.
- **Message Prefilling**: Incompatible with JSON outputs

<Tip>
**Grammar scope**: Grammars apply only to Claude's direct output, not to tool use calls, tool results, or thinking tags (when using [Extended Thinking](/docs/en/build-with-claude/extended-thinking)). Grammar state resets between sections, allowing Claude to think freely while still producing structured output in the final response.
</Tip>
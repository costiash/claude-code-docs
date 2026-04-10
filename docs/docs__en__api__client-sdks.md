# Client SDKs

Official SDKs for building with the Claude API in Python, TypeScript, Java, Go, Ruby, C#, PHP, and the command line.

---

Anthropic provides official client SDKs in multiple languages to make it easier to work with the Claude API. Each SDK provides idiomatic interfaces, type safety, and built-in support for features like streaming, retries, and error handling.

<CardGroup cols={3}>
  <Card title="CLI" href="/docs/en/api/sdks/cli">
    Shell scripting, typed flags, response transforms
  </Card>
  <Card title="Python" href="/docs/en/api/sdks/python">
    Sync and async clients, Pydantic models
  </Card>
  <Card title="TypeScript" href="/docs/en/api/sdks/typescript">
    Node.js, Deno, Bun, and browser support
  </Card>
  <Card title="Java" href="/docs/en/api/sdks/java">
    Builder pattern, CompletableFuture async
  </Card>
  <Card title="Go" href="/docs/en/api/sdks/go">
    Context-based cancellation, functional options
  </Card>
  <Card title="Ruby" href="/docs/en/api/sdks/ruby">
    Sorbet types, streaming helpers
  </Card>
  <Card title="C#" href="/docs/en/api/sdks/csharp">
    .NET Standard 2.0+, IChatClient integration
  </Card>
  <Card title="PHP" href="/docs/en/api/sdks/php">
    Value objects, builder pattern
  </Card>
</CardGroup>

## Quick installation

<Tabs>
<Tab title="CLI">
```bash
brew install anthropics/tap/ant
```
</Tab>
<Tab title="Python">
```bash
pip install anthropic
```
</Tab>
<Tab title="TypeScript">
```bash
npm install @anthropic-ai/sdk
```
</Tab>
<Tab title="C#">
```bash
dotnet add package Anthropic
```
</Tab>
<Tab title="Go">
```bash
go get github.com/anthropics/anthropic-sdk-go
```
</Tab>
<Tab title="Java">
<CodeGroup>
```groovy Gradle
implementation("com.anthropic:anthropic-java:2.20.0")
```

```xml Maven
<dependency>
    <groupId>com.anthropic</groupId>
    <artifactId>anthropic-java</artifactId>
    <version>2.20.0</version>
</dependency>
```
</CodeGroup>
</Tab>
<Tab title="PHP">
```bash
composer require anthropic-ai/sdk
```
</Tab>
<Tab title="Ruby">
```bash
bundler add anthropic
```
</Tab>
</Tabs>

## Quick start

<CodeGroup>
```bash CLI
ant messages create \
  --model claude-opus-4-6 \
  --max-tokens 1024 \
  --message '{role: user, content: "Hello, Claude"}' \
  --transform content
```

```python Python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message.content)
```

```typescript TypeScript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const message = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello, Claude" }]
});
console.log(message.content);
```

```csharp C# hidelines={2}
using Anthropic;
using Anthropic.Models.Messages;

var client = new AnthropicClient();

var message = await client.Messages.Create(new MessageCreateParams
{
    Model = "claude-opus-4-6",
    MaxTokens = 1024,
    Messages = [new() { Role = Role.User, Content = "Hello, Claude" }]
});
Console.WriteLine(message.Content);
```

```go Go hidelines={1..2,10..11,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	message, err := client.Messages.New(context.Background(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(message.Content)
}
```

```java Java hidelines={6..8,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

public class Main {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model(Model.CLAUDE_OPUS_4_6)
            .maxTokens(1024L)
            .addUserMessage("Hello, Claude")
            .build();

        Message message = client.messages().create(params);
        System.out.println(message.content());
    }
}
```

```php PHP hidelines={1}
<?php
use Anthropic\Client;

$client = new Client(apiKey: getenv('ANTHROPIC_API_KEY'));

$message = $client->messages->create(
    model: 'claude-opus-4-6',
    maxTokens: 1024,
    messages: [
        ['role' => 'user', 'content' => 'Hello, Claude']
    ],
);
echo $message->content[0]->text;
```

```ruby Ruby
client = Anthropic::Client.new

message = client.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [
    { role: "user", content: "Hello, Claude" }
  ]
)
puts message.content
```
</CodeGroup>

## Platform support

All SDKs support multiple deployment options:

| Platform | Description |
|----------|-------------|
| Claude API | Connect directly to Claude API endpoints |
| [Amazon Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock) | Use Claude through AWS |
| [Google Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai) | Use Claude through Google Cloud |
| [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry) | Use Claude through Microsoft Azure |

See individual SDK pages for platform-specific setup instructions.

## Beta features

Access beta features using the `beta` namespace in any SDK:

<CodeGroup>

```bash CLI nocheck
ant beta:messages create \
  --model claude-opus-4-6 \
  --max-tokens 1024 \
  --message '{role: user, content: "Hello"}' \
  --beta feature-name
```

```python Python nocheck
message = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    betas=["feature-name"],
)
```

```typescript TypeScript nocheck
const message = await client.beta.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello" }],
  betas: ["feature-name"]
});
```

```csharp C# nocheck
var message = await client.Beta.Messages.Create(new MessageCreateParams
{
    Model = "claude-opus-4-6",
    MaxTokens = 1024,
    Messages = [new() { Role = Role.User, Content = "Hello" }],
    Betas = ["feature-name"],
});
```

```go Go nocheck hidelines={9}
message, _ := client.Beta.Messages.New(context.Background(), anthropic.BetaMessageNewParams{
	Model:     anthropic.ModelClaudeOpus4_6,
	MaxTokens: 1024,
	Messages: []anthropic.BetaMessageParam{
		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hello")),
	},
	Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBeta("feature-name")},
})
fmt.Println(message)
```

```java Java nocheck
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

MessageCreateParams params = MessageCreateParams.builder()
    .model(Model.CLAUDE_OPUS_4_6)
    .maxTokens(1024L)
    .addUserMessage("Hello")
    .addBeta("feature-name")
    .build();

client.beta().messages().create(params);
```

```php PHP nocheck
$message = $client->beta->messages->create(
    model: 'claude-opus-4-6',
    maxTokens: 1024,
    messages: [['role' => 'user', 'content' => 'Hello']],
    betas: ['feature-name'],
);
```

```ruby Ruby nocheck
message = client.beta.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello" }],
  betas: ["feature-name"]
)
```
</CodeGroup>

See [Beta headers](/docs/en/api/beta-headers) for available beta features.

## Requirements

| SDK | Minimum Version |
|-----|-----------------|
| Python | 3.9+ |
| TypeScript | 4.9+ (Node.js 20+) |
| Java | 8+ |
| Go | 1.23+ |
| Ruby | 3.2.0+ |
| C# | .NET Standard 2.0 |
| PHP | 8.1.0+ |

## GitHub repositories

- [anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python)
- [anthropic-sdk-typescript](https://github.com/anthropics/anthropic-sdk-typescript)
- [anthropic-sdk-java](https://github.com/anthropics/anthropic-sdk-java)
- [anthropic-sdk-go](https://github.com/anthropics/anthropic-sdk-go)
- [anthropic-sdk-ruby](https://github.com/anthropics/anthropic-sdk-ruby)
- [anthropic-sdk-csharp](https://github.com/anthropics/anthropic-sdk-csharp)
- [anthropic-sdk-php](https://github.com/anthropics/anthropic-sdk-php)
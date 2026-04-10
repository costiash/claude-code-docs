# Claude in Amazon Bedrock (research preview)

Access Claude models through Amazon Bedrock with AWS-native authentication, billing, and security boundaries.

---

This guide walks you through setting up and making API calls to Claude in Amazon Bedrock. Claude in Amazon Bedrock runs on AWS-managed infrastructure with zero operator access (Anthropic personnel have no access to the inference infrastructure), letting you build sensitive applications entirely inside the AWS security boundary while using the same Messages API shape you use with Anthropic's first-party API.

<Note>
This page covers the research preview of the new Claude in Amazon Bedrock offering, which exposes the Messages API at `/anthropic/v1/messages`. For the existing Bedrock integration (the `InvokeModel` and `Converse` APIs with ARN-versioned model identifiers and AWS event-stream encoding), see [Claude on Amazon Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock).
</Note>

## Research preview

The Claude in Amazon Bedrock endpoint is in research preview, available in the US East (N. Virginia) `us-east-1` region. Contact your Anthropic account executive to request access.

## Prerequisites

Before you begin, ensure you have:

- A **new AWS account** in `us-east-1`. The research preview requires a dedicated account for isolation. Your Anthropic account executive will submit your account ID to the Bedrock Marketplace team for allowlisting (typically processed within 24 hours).
- The [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed and configured (optional, for credential management)
- After allowlisting, AWS sends a welcome email with additional setup details.

## Authentication

Claude in Amazon Bedrock supports three authentication paths. Choose the one that best fits your security requirements.

### Bedrock service role (recommended)

Use a Bedrock service role with AWS-managed keys for the most secure, long-lived access:

<Steps>
<Step title="Admin: provision the service role">
An AWS administrator provisions a Bedrock service role and grants developers `iam:PassRole` permission on the service role ARN.
</Step>
<Step title="Developer: pass the role">
When calling the API, Bedrock assumes the service role on your behalf. See the [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-mantle.html) for how to associate the role with your requests.
</Step>
</Steps>

### IAM assumed roles

For identity-federated access with a 12-hour maximum session:

<Steps>
<Step title="Admin: configure the IAM role">
Create an IAM role scoped to your Claude models. The trust policy names your identity provider (SAML, OIDC, or AWS Identity Center). The permissions policy grants `bedrock-mantle:CreateInference` only on the allowed model ARNs.
</Step>
<Step title="Developer: authenticate and assume">
Authenticate through your corporate identity provider, then assume the IAM role. AWS STS issues temporary credentials that the SDK or CLI uses to sign requests.
</Step>
</Steps>

### Bearer tokens

For short-term access without IAM roles (12-hour maximum, least preferred):

<Steps>
<Step title="Admin: restrict token types">
Block long-term keys by attaching a policy that denies `bedrock:CallWithBearerToken` unless the `bedrock:BearerTokenType` condition matches a short-term token.
</Step>
<Step title="Developer: mint a token">
Use the `aws-bedrock-token-generator` CLI to mint a bearer token. Pass it in the `x-api-key` header on each request.
</Step>
</Steps>

## Install an SDK

Anthropic's [client SDKs](/docs/en/api/client-sdks) support Claude in Amazon Bedrock through a Bedrock-specific package or module.

<Tabs>
<Tab title="Python">
```bash
pip install -U "anthropic[bedrock]"
```
</Tab>

<Tab title="TypeScript">
```bash
npm install @anthropic-ai/bedrock-sdk
```
</Tab>

<Tab title="C#">
```bash
dotnet add package Anthropic.Bedrock
```
</Tab>

<Tab title="Go">
```bash
go get github.com/anthropics/anthropic-sdk-go/bedrock
```
</Tab>

<Tab title="Java">
<Tabs>
<Tab title="Gradle">
```kotlin
implementation("com.anthropic:anthropic-java-bedrock:2.20.0")
```
</Tab>
<Tab title="Maven">
```xml
<dependency>
    <groupId>com.anthropic</groupId>
    <artifactId>anthropic-java-bedrock</artifactId>
    <version>2.20.0</version>
</dependency>
```
</Tab>
</Tabs>
</Tab>

<Tab title="PHP">
```bash
composer require anthropic-ai/sdk aws/aws-sdk-php
```
</Tab>

<Tab title="Ruby">
```bash
# Gemfile
gem "anthropic"
gem "aws-sdk-core"
```
</Tab>
</Tabs>

## Making your first request

The endpoint follows the pattern `https://bedrock-mantle.{region}.api.aws/anthropic/v1/messages`. Unlike the `InvokeModel`-based integration, this endpoint uses standard SSE streaming and the same request body shape as Anthropic's first-party API.

The SDK resolves credentials and region using the standard AWS precedence: constructor arguments, then environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`, `AWS_REGION`), then the AWS config file and credential chain (SSO, assumed roles, ECS task role, IMDS).

<Tabs>
<Tab title="cURL">

```bash nocheck
curl https://bedrock-mantle.us-east-1.api.aws/anthropic/v1/messages \
  --aws-sigv4 "aws:amz:us-east-1:bedrock-mantle" \
  --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
  -H "x-amz-security-token: $AWS_SESSION_TOKEN" \
  -H "content-type: application/json" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "anthropic.claude-mythos-preview",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Hello, Claude"}
    ]
  }'
```
</Tab>

<Tab title="CLI">
The `ant` CLI does not support Amazon Bedrock. Use either cURL or an SDK.
</Tab>

<Tab title="Python">

```python nocheck
from anthropic import AnthropicBedrockMantle

client = AnthropicBedrockMantle(aws_region="us-east-1")

message = client.messages.create(
    model="anthropic.claude-mythos-preview",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)

print(message.content[0].text)
```
</Tab>

<Tab title="TypeScript">

```typescript nocheck
import { AnthropicBedrockMantle } from "@anthropic-ai/bedrock-sdk";

const client = new AnthropicBedrockMantle({
  awsRegion: "us-east-1"
});

const message = await client.messages.create({
  model: "anthropic.claude-mythos-preview",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello, Claude" }]
});

const block = message.content[0];
if (block.type === "text") {
  console.log(block.text);
}
```
</Tab>

<Tab title="C#">

```csharp nocheck
using Anthropic.Bedrock;
using Anthropic.Models.Messages;

var client = new AnthropicBedrockMantleClient(new() { AwsRegion = "us-east-1" });

var message = await client.Messages.Create(new()
{
    Model = "anthropic.claude-mythos-preview",
    MaxTokens = 1024,
    Messages = [new() { Role = Role.User, Content = "Hello, Claude" }],
});

if (message.Content[0].Value is TextBlock block)
    Console.WriteLine(block.Text);
```
</Tab>

<Tab title="Go">

```go nocheck hidelines={1..2}
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/bedrock"
)

func main() {
	client, err := bedrock.NewMantleClient(context.Background(), bedrock.MantleClientConfig{
		AWSRegion: "us-east-1",
	})
	if err != nil {
		panic(err)
	}

	message, err := client.Messages.New(context.Background(), anthropic.MessageNewParams{
		Model:     "anthropic.claude-mythos-preview",
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
		},
	})
	if err != nil {
		panic(err)
	}

	fmt.Println(message.Content[0].Text)
}
```
</Tab>

<Tab title="Java">

```java nocheck
import com.anthropic.bedrock.backends.BedrockMantleBackend;
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;

void main() {
    AnthropicClient client = AnthropicOkHttpClient.builder()
        .backend(BedrockMantleBackend.fromEnv())
        .build();

    Message message = client.messages().create(
        MessageCreateParams.builder()
            .model("anthropic.claude-mythos-preview")
            .maxTokens(1024)
            .addUserMessage("Hello, Claude")
            .build()
    );

    IO.println(message.content().getFirst().asText().text());
}
```
</Tab>

<Tab title="PHP">

```php nocheck hidelines={1..2}
<?php

use Anthropic\Bedrock\MantleClient;

$client = new MantleClient(awsRegion: 'us-east-1');

$message = $client->messages->create(
    model: 'anthropic.claude-mythos-preview',
    maxTokens: 1024,
    messages: [
        ['role' => 'user', 'content' => 'Hello, Claude'],
    ],
);

echo $message->content[0]->text;
```
</Tab>

<Tab title="Ruby">

```ruby nocheck
require "anthropic"

client = Anthropic::BedrockMantleClient.new(aws_region: "us-east-1")

message = client.messages.create(
  model: "anthropic.claude-mythos-preview",
  max_tokens: 1024,
  messages: [{role: "user", content: "Hello, Claude"}]
)

puts message.content[0].text
```
</Tab>
</Tabs>

<Tip>
You can also use the standard `Anthropic` client: set `base_url` to `https://bedrock-mantle.{region}.api.aws/anthropic` and pass your bearer token as `api_key`. This path supports bearer-token authentication only. SigV4 signing requires the dedicated client.
</Tip>

## Supported models

Model IDs in Claude in Amazon Bedrock carry an `anthropic.` provider prefix. Model capabilities and behaviors are documented on the [Models overview](/docs/en/about-claude/models/overview) page.

| Model                 | Model ID                          |
| --------------------- | --------------------------------- |
| Claude Mythos Preview | `anthropic.claude-mythos-preview` |
| Claude Haiku 4.5      | `anthropic.claude-haiku-4-5`      |

## Feature availability

Claude in Amazon Bedrock supports features that run inside the model. Features that require Anthropic-operated infrastructure are not available.

**Supported:**

- Messages API (`/v1/messages`)
- Prompt caching
- Extended thinking
- Tool use (client-defined tools)
- Citations
- Structured outputs
- In-region inference (requests stay in a single AWS region)

**Not supported:**

- Anthropic-defined tools (Web Search, Web Fetch, Remote MCP, Memory, Files API, Computer Use, Skills, Code Execution)
- Claude Managed Agents
- Message Batches API
- `/v1/users` endpoint

## Regions

The research preview is available in `us-east-1` (IAD) only.

## Quotas

Default quota is 2 million input tokens per minute (TPM). You can request up to 4 million input TPM without additional Anthropic approval. AWS enforces requests-per-minute (RPM) limits on the Bedrock side; contact AWS support for RPM adjustments.

## Data retention

Data handling for this offering is governed by Amazon Bedrock. For details, see [Data protection in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html).

Zero data retention (ZDR) is available. To enable ZDR for your account, contact AWS support.

## Observability

Claude in Amazon Bedrock emits logs to both CloudWatch and CloudTrail. Anthropic recommends retaining activity logs on at least a 30-day rolling basis to understand usage patterns and investigate potential issues.

## Support

For research preview support, contact **bedrock-ant-eap@amazon.com**. Include your AWS account ID and the `request-id` from any failed API responses.

<Note>
**Claude Mythos Preview** is a research preview model available to invited customers on Amazon Bedrock. For more information, see [Project Glasswing](https://anthropic.com/glasswing).
</Note>
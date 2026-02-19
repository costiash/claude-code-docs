# Claude on Amazon Bedrock

Anthropic's Claude models are now generally available through Amazon Bedrock.

---

Calling Claude through Bedrock slightly differs from how you would call Claude when using Anthropic's client SDK's. This guide will walk you through the process of completing an API call to Claude on Bedrock in either Python or TypeScript.

Note that this guide assumes you have already signed up for an [AWS account](https://portal.aws.amazon.com/billing/signup) and configured programmatic access.

<Note>
The PHP SDK does not currently support Amazon Bedrock. For available SDK platform integrations, see [Client SDKs](/docs/en/api/client-sdks).
</Note>

## Install and configure the AWS CLI

1. [Install a version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) at or newer than version `2.13.23`
2. Configure your AWS credentials using the AWS configure command (see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)) or find your credentials by navigating to "Command line or programmatic access" within your AWS dashboard and following the directions in the popup modal.
3. Verify that your credentials are working:

```bash Shell
aws sts get-caller-identity
```

## Install an SDK for accessing Bedrock

Anthropic's [client SDKs](/docs/en/api/client-sdks) support Bedrock. You can also use an AWS SDK like `boto3` directly.

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

<Tab title="Java">
<CodeGroup>
```groovy Gradle
implementation("com.anthropic:anthropic-java-bedrock:2.+")
```

```xml Maven
<dependency>
    <groupId>com.anthropic</groupId>
    <artifactId>anthropic-java-bedrock</artifactId>
    <version>2.13.0</version>
</dependency>
```
</CodeGroup>
</Tab>

<Tab title="Go">
```bash
go get github.com/anthropics/anthropic-sdk-go/bedrock
```
</Tab>

<Tab title="C#">
```bash
dotnet add package Anthropic.Bedrock
```
</Tab>

<Tab title="Ruby">
```bash
# Gemfile
gem "anthropic"
gem "aws-sdk-bedrockruntime"
```
</Tab>

<Tab title="Boto3 (Python)">
```bash
pip install boto3>=1.28.59
```
</Tab>
</Tabs>

## Accessing Bedrock

### Subscribe to Anthropic models

Go to the [AWS Console > Bedrock > Model Access](https://console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess) and request access to Anthropic models. Note that Anthropic model availability varies by region. See [AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) for latest information.

#### API model IDs

| Model | Base Bedrock model ID | `global` | `us` | `eu` | `jp` | `apac` |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Claude Opus 4.6 | anthropic.claude-opus-4-6-v1 | Yes | Yes | Yes | Yes | Yes |
| Claude Sonnet 4.6 | anthropic.claude-sonnet-4-6 | Yes | Yes | Yes | Yes | No |
| Claude Sonnet 4.5 | anthropic.claude-sonnet-4-5-20250929-v1:0 | Yes | Yes | Yes | Yes | No |
| Claude Sonnet 4 | anthropic.claude-sonnet-4-20250514-v1:0 | Yes | Yes | Yes | No | Yes |
| Claude Sonnet 3.7 <Tooltip tooltipContent="Retired as of February 19, 2026.">⚠️</Tooltip> | anthropic.claude-3-7-sonnet-20250219-v1:0 | No | Yes | Yes | No | Yes |
| Claude Opus 4.5 | anthropic.claude-opus-4-5-20251101-v1:0 | Yes | Yes | Yes | No | No |
| Claude Opus 4.1 | anthropic.claude-opus-4-1-20250805-v1:0 | No | Yes | No | No | No |
| Claude Opus 4 | anthropic.claude-opus-4-20250514-v1:0 | No | Yes | No | No | No |
| Claude Haiku 4.5 | anthropic.claude-haiku-4-5-20251001-v1:0 | Yes | Yes | Yes | No | No |
| Claude Haiku 3.5 <Tooltip tooltipContent="Retired as of February 19, 2026.">⚠️</Tooltip> | anthropic.claude-3-5-haiku-20241022-v1:0 | No | Yes | No | No | No |
| Claude Haiku 3 <Tooltip tooltipContent="Deprecated as of February 19, 2026. Retiring April 19, 2026.">⚠️</Tooltip> | anthropic.claude-3-haiku-20240307-v1:0 | No | Yes | Yes | No | Yes |

For more information about regional vs global model IDs, see the [Global vs regional endpoints](#global-vs-regional-endpoints) section below.

### List available models

The following examples show how to print a list of all the Claude models available through Bedrock:

<CodeGroup>
  ```bash AWS CLI
  aws bedrock list-foundation-models --region=us-west-2 --by-provider anthropic --query "modelSummaries[*].modelId"
  ```

  ```python Boto3 (Python)
  import boto3

  bedrock = boto3.client(service_name="bedrock")
  response = bedrock.list_foundation_models(byProvider="anthropic")

  for summary in response["modelSummaries"]:
      print(summary["modelId"])
  ```
</CodeGroup>

### Making requests

The following examples show how to generate text from Claude on Bedrock:

<CodeGroup>
  ```python Python
  from anthropic import AnthropicBedrock

  client = AnthropicBedrock(
      # Authenticate by either providing the keys below or use the default AWS credential providers, such as
      # using ~/.aws/credentials or the "AWS_SECRET_ACCESS_KEY" and "AWS_ACCESS_KEY_ID" environment variables.
      aws_access_key="<access key>",
      aws_secret_key="<secret key>",
      # Temporary credentials can be used with aws_session_token.
      # Read more at https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html.
      aws_session_token="<session_token>",
      # aws_region changes the aws region to which the request is made. By default, we read AWS_REGION,
      # and if that's not present, we default to us-east-1. Note that we do not read ~/.aws/config for the region.
      aws_region="us-west-2",
  )

  message = client.messages.create(
      model="global.anthropic.claude-opus-4-6-v1",
      max_tokens=256,
      messages=[{"role": "user", "content": "Hello, world"}],
  )
  print(message.content)
  ```

  ```typescript TypeScript
  import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

  const client = new AnthropicBedrock({
    // Authenticate by either providing the keys below or use
    // the default AWS credential providers, such as
    // ~/.aws/credentials or the "AWS_SECRET_ACCESS_KEY" and
    // "AWS_ACCESS_KEY_ID" environment variables.
    awsAccessKey: "<access key>",
    awsSecretKey: "<secret key>",

    // Temporary credentials can be used with awsSessionToken.
    // Read more at https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html.
    awsSessionToken: "<session_token>",

    // awsRegion changes the aws region to which the request
    // is made. By default, we read AWS_REGION, and if that's
    // not present, we default to us-east-1. Note that we do
    // not read ~/.aws/config for the region.
    awsRegion: "us-west-2"
  });

  async function main() {
    const message = await client.messages.create({
      model: "global.anthropic.claude-opus-4-6-v1",
      max_tokens: 256,
      messages: [{ role: "user", content: "Hello, world" }]
    });
    console.log(message);
  }
  main().catch(console.error);
  ```

  ```java Java
  import com.anthropic.bedrock.backends.BedrockBackend;
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.Message;
  import com.anthropic.models.messages.MessageCreateParams;

  public class BedrockExample {

    public static void main(String[] args) {
      // Uses default AWS credential provider chain
      AnthropicClient client = AnthropicOkHttpClient.builder()
        .backend(BedrockBackend.fromEnv())
        .build();

      Message message = client
        .messages()
        .create(
          MessageCreateParams.builder()
            .model("global.anthropic.claude-opus-4-6-v1")
            .maxTokens(256)
            .addUserMessage("Hello, world")
            .build()
        );

      System.out.println(message.content());
    }
  }
  ```

  ```go Go
  package main

  import (
  	"context"
  	"fmt"

  	"github.com/anthropics/anthropic-sdk-go"
  	"github.com/anthropics/anthropic-sdk-go/bedrock"
  )

  func main() {
  	// Uses default AWS credential provider chain
  	client := anthropic.NewClient(
  		bedrock.WithLoadDefaultConfig(context.Background()),
  	)

  	message, err := client.Messages.New(context.Background(), anthropic.MessageNewParams{
  		Model:     "global.anthropic.claude-opus-4-6-v1",
  		MaxTokens: 256,
  		Messages: []anthropic.MessageParam{
  			anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, world")),
  		},
  	})
  	if err != nil {
  		panic(err)
  	}
  	fmt.Printf("%+v\n", message.Content)
  }
  ```

  ```csharp C#
  using Anthropic.Bedrock;
  using Anthropic.Models.Messages;

  AnthropicBedrockClient client = new(
      await AnthropicBedrockCredentialsHelper.FromEnv()
      ?? throw new InvalidOperationException("AWS credentials not configured.")
  );

  var response = await client.Messages.Create(new MessageCreateParams
  {
      Model = "global.anthropic.claude-opus-4-6-v1",
      MaxTokens = 256,
      Messages = [new() { Role = Role.User, Content = "Hello, world" }],
  });

  Console.WriteLine(
      string.Join("", response.Content
          .Where(c => c.Value is TextBlock)
          .Select(c => (c.Value as TextBlock)!.Text)));
  ```

  ```ruby Ruby
  require "anthropic"

  client = Anthropic::BedrockClient.new

  message = client.messages.create(
    model: "global.anthropic.claude-opus-4-6-v1",
    max_tokens: 256,
    messages: [{role: "user", content: "Hello, world"}]
  )

  puts message.content.first.text
  ```

  ```python Boto3 (Python)
  import boto3
  import json

  bedrock = boto3.client(service_name="bedrock-runtime")
  body = json.dumps(
      {
          "max_tokens": 256,
          "messages": [{"role": "user", "content": "Hello, world"}],
          "anthropic_version": "bedrock-2023-05-31",
      }
  )

  response = bedrock.invoke_model(
      body=body, modelId="global.anthropic.claude-opus-4-6-v1"
  )

  response_body = json.loads(response.get("body").read())
  print(response_body.get("content"))
  ```
</CodeGroup>

See the [client SDKs](/docs/en/api/client-sdks) for more details, and the [official Bedrock documentation](https://docs.aws.amazon.com/bedrock/).

### Bearer token authentication

You can authenticate with Bedrock using bearer tokens instead of AWS credentials. This is useful in corporate environments where teams need access to Bedrock without managing AWS credentials, IAM roles, or account-level permissions.

<Note>
Bearer token authentication is supported in the C#, Go, and Java SDKs. The Python, TypeScript, and Ruby SDKs use AWS SigV4 signing only.
</Note>

The simplest approach is to set the `AWS_BEARER_TOKEN_BEDROCK` environment variable, which is automatically detected by `fromEnv()` credential resolution.

To provide a token programmatically:

<CodeGroup>

```csharp C#
using Anthropic.Bedrock;
using Anthropic.Models.Messages;

var client = new AnthropicBedrockClient(
    new AnthropicBedrockApiTokenCredentials
    {
        BearerToken = "your-bearer-token",
        Region = "us-east-1",
    }
);

var response = await client.Messages.Create(new MessageCreateParams
{
    Model = "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    MaxTokens = 1024,
    Messages = [new() { Role = Role.User, Content = "Hello!" }],
});
```

```go Go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/bedrock"
	"github.com/aws/aws-sdk-go-v2/aws"
)

func main() {
	cfg := aws.Config{
		Region:                  "us-west-2",
		BearerAuthTokenProvider: bedrock.NewStaticBearerTokenProvider("your-bearer-token"),
	}
	client := anthropic.NewClient(
		bedrock.WithConfig(cfg),
	)

	message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("Hello!")),
		},
	})
	if err != nil {
		panic(err)
	}
	fmt.Println(message.Content[0].AsResponseTextBlock().Text)
}
```

```java Java
import com.anthropic.bedrock.backends.BedrockBackend;
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MessageCreateParams;

// Option 1: Set AWS_BEARER_TOKEN_BEDROCK environment variable and use fromEnv()
AnthropicClient client = AnthropicOkHttpClient.builder()
  .backend(BedrockBackend.fromEnv())
  .build();

// Option 2: Provide the token programmatically
client = AnthropicOkHttpClient.builder()
  .backend(BedrockBackend.builder()
    .apiKey("your-bearer-token")
    .build())
  .build();

MessageCreateParams params = MessageCreateParams.builder()
  .model("us.anthropic.claude-sonnet-4-5-20250929-v1:0")
  .maxTokens(1024)
  .addUserMessage("Hello!")
  .build();

client.messages().create(params).content().stream()
  .flatMap(block -> block.text().stream())
  .forEach(textBlock -> System.out.println(textBlock.text()));
```

</CodeGroup>

## Activity logging

Bedrock provides an [invocation logging service](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) that allows customers to log the prompts and completions associated with your usage.

Anthropic recommends that you log your activity on at least a 30-day rolling basis in order to understand your activity and investigate any potential misuse.

<Note>
Turning on this service does not give AWS or Anthropic any access to your content.
</Note>

## Feature support
For all currently supported features on Bedrock, see [API features overview](/docs/en/api/overview).

### PDF Support on Bedrock

PDF support is available on Amazon Bedrock through both the Converse API and InvokeModel API. For detailed information about PDF processing capabilities and limitations, see the [PDF support documentation](/docs/en/build-with-claude/pdf-support#amazon-bedrock-pdf-support).

**Important considerations for Converse API users:**
- Visual PDF analysis (charts, images, layouts) requires citations to be enabled
- Without citations, only basic text extraction is available
- For full control without forced citations, use the InvokeModel API

For more details on the two document processing modes and their limitations, refer to the [PDF support guide](/docs/en/build-with-claude/pdf-support#amazon-bedrock-pdf-support).

### 1M token context window

Claude Opus 4.6, Sonnet 4.5, and Sonnet 4 support the [1M token context window](/docs/en/build-with-claude/context-windows#1m-token-context-window) on Amazon Bedrock.

<Note>
The 1M token context window is currently in beta. To use the extended context window, include the `context-1m-2025-08-07` beta header in your [Bedrock API requests](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-request-response.html).
</Note>

## Global vs regional endpoints

Starting with **Claude Sonnet 4.5 and all future models**, Amazon Bedrock offers two endpoint types:

- **Global endpoints**: Dynamic routing for maximum availability
- **Regional endpoints**: Guaranteed data routing through specific geographic regions

Regional endpoints include a 10% pricing premium over global endpoints.

<Note>
This applies to Claude Sonnet 4.5 and future models only. Older models (Claude Sonnet 4, Opus 4, and earlier) maintain their existing pricing structures.
</Note>

### When to use each option

**Global endpoints (recommended):**
- Provide maximum availability and uptime
- Dynamically route requests to regions with available capacity
- No pricing premium
- Best for applications where data residency is flexible

**Regional endpoints (CRIS):**
- Route traffic through specific geographic regions
- Required for data residency and compliance requirements
- Available for US, EU, Japan, and Australia
- 10% pricing premium reflects infrastructure costs for dedicated regional capacity

### Implementation

**Using global endpoints (default for Opus 4.6, Sonnet 4.5, and Sonnet 4):**

The model IDs for Claude Sonnet 4.5 and 4 already include the `global.` prefix:

<CodeGroup>
```python Python
from anthropic import AnthropicBedrock

client = AnthropicBedrock(aws_region="us-west-2")

message = client.messages.create(
    model="global.anthropic.claude-opus-4-6-v1",
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello, world"}],
)
```

```typescript TypeScript
import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

const client = new AnthropicBedrock({
  awsRegion: "us-west-2"
});

const message = await client.messages.create({
  model: "global.anthropic.claude-opus-4-6-v1",
  max_tokens: 256,
  messages: [{ role: "user", content: "Hello, world" }]
});
```

```java Java
import com.anthropic.bedrock.backends.BedrockBackend;
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MessageCreateParams;

// Uses default AWS credential provider chain
AnthropicClient client = AnthropicOkHttpClient.builder()
  .backend(BedrockBackend.fromEnv())
  .build();

var message = client
  .messages()
  .create(
    MessageCreateParams.builder()
      .model("global.anthropic.claude-opus-4-6-v1")
      .maxTokens(256)
      .addUserMessage("Hello, world")
      .build()
  );
```

```go Go
package main

import (
	"context"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/bedrock"
)

func main() {
	// Uses default AWS credential provider chain
	client := anthropic.NewClient(
		bedrock.WithLoadDefaultConfig(context.Background()),
	)

	message, _ := client.Messages.New(context.Background(), anthropic.MessageNewParams{
		Model:     "global.anthropic.claude-opus-4-6-v1",
		MaxTokens: 256,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, world")),
		},
	})
	_ = message
}
```

```csharp C#
using Anthropic.Bedrock;
using Anthropic.Models.Messages;

// C# Bedrock client uses model IDs with region prefix for global routing
AnthropicBedrockClient client = new(
    await AnthropicBedrockCredentialsHelper.FromEnv()
    ?? throw new InvalidOperationException("AWS credentials not configured.")
);

var response = await client.Messages.Create(new MessageCreateParams
{
    // Use "global." prefix for global cross-region inference
    Model = "global.anthropic.claude-opus-4-6-v1",
    MaxTokens = 256,
    Messages = [new() { Role = Role.User, Content = "Hello, world" }],
});
```

```ruby Ruby
require "anthropic"

# Default credentials resolve region from AWS_REGION env var
client = Anthropic::BedrockClient.new

message = client.messages.create(
  # Use "global." prefix for global cross-region inference
  model: "global.anthropic.claude-opus-4-6-v1",
  max_tokens: 256,
  messages: [{role: "user", content: "Hello, world"}]
)
```
</CodeGroup>

**Using regional endpoints (CRIS):**

To use regional endpoints, remove the `global.` prefix from the model ID:

<CodeGroup>
```python Python
from anthropic import AnthropicBedrock

client = AnthropicBedrock(aws_region="us-west-2")

# Using US regional endpoint (CRIS)
message = client.messages.create(
    model="anthropic.claude-opus-4-6-v1",  # No global. prefix
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello, world"}],
)
```

```typescript TypeScript
import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

const client = new AnthropicBedrock({
  awsRegion: "us-west-2"
});

// Using US regional endpoint (CRIS)
const message = await client.messages.create({
  model: "anthropic.claude-opus-4-6-v1", // No global. prefix
  max_tokens: 256,
  messages: [{ role: "user", content: "Hello, world" }]
});
```

```java Java
import com.anthropic.bedrock.backends.BedrockBackend;
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MessageCreateParams;

// Uses default AWS credential provider chain
AnthropicClient client = AnthropicOkHttpClient.builder()
  .backend(BedrockBackend.fromEnv())
  .build();

// Using US regional endpoint (CRIS)
var message = client
  .messages()
  .create(
    MessageCreateParams.builder()
      .model("us.anthropic.claude-opus-4-6-v1") // Regional prefix
      .maxTokens(256)
      .addUserMessage("Hello, world")
      .build()
  );
```

```go Go
package main

import (
	"context"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/bedrock"
)

func main() {
	// Uses default AWS credential provider chain
	client := anthropic.NewClient(
		bedrock.WithLoadDefaultConfig(context.Background()),
	)

	// Using US regional endpoint (CRIS)
	message, _ := client.Messages.New(context.Background(), anthropic.MessageNewParams{
		Model:     "us.anthropic.claude-opus-4-6-v1", // Regional prefix
		MaxTokens: 256,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, world")),
		},
	})
	_ = message
}
```

```csharp C#
using Anthropic.Bedrock;
using Anthropic.Models.Messages;

AnthropicBedrockClient client = new(
    new AnthropicBedrockPrivateKeyCredentials { Region = "us-west-2" }
);

// Using US regional endpoint (CRIS)
var response = await client.Messages.Create(new MessageCreateParams
{
    Model = "anthropic.claude-opus-4-6-v1", // No global. prefix
    MaxTokens = 256,
    Messages = [new() { Role = Role.User, Content = "Hello, world" }],
});
```

```ruby Ruby
require "anthropic"

# Using US regional endpoint (CRIS)
client = Anthropic::BedrockClient.new(aws_region: "us-west-2")

message = client.messages.create(
  model: "anthropic.claude-opus-4-6-v1", # No global. prefix
  max_tokens: 256,
  messages: [{role: "user", content: "Hello, world"}]
)
```
</CodeGroup>

### Additional resources

- **AWS Bedrock pricing:** [aws.amazon.com/bedrock/pricing](https://aws.amazon.com/bedrock/pricing/)
- **AWS pricing documentation:** [Bedrock pricing guide](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-pricing.html)
- **AWS blog post:** [Introducing Claude Sonnet 4.5 in Amazon Bedrock](https://aws.amazon.com/blogs/aws/introducing-claude-sonnet-4-5-in-amazon-bedrock-anthropics-most-intelligent-model-best-for-coding-and-complex-agents/)
- **Anthropic pricing details:** [Pricing documentation](/docs/en/about-claude/pricing#third-party-platform-pricing)
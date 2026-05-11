# Claude in Microsoft Foundry

Access Claude models through Microsoft Foundry with Azure-native endpoints and authentication.

---

This guide walks you through the process of setting up and making API calls to Claude in Foundry using one of Anthropic's client SDKs or direct HTTP requests. When you can access Claude in Foundry, you are billed for Claude usage in the Microsoft Marketplace, allowing you to access Claude's latest capabilities while managing costs through your Azure subscription.

Regional availability: At launch, Claude is available as a Global Standard deployment type in Foundry resources. Pricing for Claude in the Microsoft Marketplace uses Anthropic's standard API pricing. Visit [Pricing](https://claude.com/pricing#api) for details.

<Note>
Foundry is supported by the C#, Java, PHP, Python, and TypeScript SDKs. The Go and Ruby SDKs do not currently support Microsoft Foundry. For available SDK platform integrations, see [Client SDKs](/docs/en/api/client-sdks).
</Note>

## Preview

In this preview platform integration, Claude models run on Anthropic's infrastructure. This is a commercial integration for billing and access through Azure. As an independent processor for Microsoft, customers using Claude through Microsoft Foundry are subject to Anthropic's data use terms. Anthropic continues to provide its industry-leading safety and data commitments, including zero data retention availability.

## Prerequisites

Before you begin, ensure you have:

- An active Azure subscription
- Access to [Foundry](https://ai.azure.com/)
- The [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed (optional, for resource management)

## Install an SDK

Anthropic's [client SDKs](/docs/en/api/client-sdks) support Foundry through a platform-specific package or client class.

<Tabs>
<Tab title="Python">
```bash
pip install -U "anthropic"
```
</Tab>

<Tab title="TypeScript">
```bash
npm install @anthropic-ai/foundry-sdk
```
</Tab>

<Tab title="C#">
```bash
dotnet add package Anthropic.Foundry
```
</Tab>

<Tab title="Java">
<Tabs>
<Tab title="Gradle">
```kotlin
implementation("com.anthropic:anthropic-java-foundry:2.30.0")
```
</Tab>
<Tab title="Maven">
```xml
<dependency>
    <groupId>com.anthropic</groupId>
    <artifactId>anthropic-java-foundry</artifactId>
    <version>2.30.0</version>
</dependency>
```
</Tab>
</Tabs>
</Tab>

<Tab title="PHP">
```bash
composer require anthropic-ai/sdk
```
</Tab>
</Tabs>

## Provisioning

Foundry uses a two-level hierarchy: **resources** contain your security and billing configuration, while **deployments** are the model instances you call via API. You'll first create a Foundry resource, then create one or more Claude deployments within it.

### Provisioning Foundry resources

Create a Foundry resource, which is required to use and manage services in Azure. You can follow these instructions to create a [Foundry resource](https://learn.microsoft.com/en-us/azure/ai-services/multi-service-resource?pivots=azportal#create-a-new-azure-ai-foundry-resource). Alternatively, you can start by creating a [Foundry project](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/create-projects?tabs=ai-foundry), which involves creating a Foundry resource.

To provision your resource:

1. Navigate to the [Foundry portal](https://ai.azure.com/)
2. Create a new Foundry resource or select an existing one
3. Configure access management using Azure-issued API keys or Entra ID (formerly Azure Active Directory) for role-based access control
4. Optionally configure the resource to be part of a private network (Azure Virtual Network) for enhanced security
5. Note your resource name. You'll use this as `{resource}` in API endpoints (for example, `https://{resource}.services.ai.azure.com/anthropic/v1/*`)

### Creating Foundry deployments

After creating your resource, deploy a Claude model to make it available for API calls:

1. In the Foundry portal, navigate to your resource
2. Go to **Models + endpoints** and select **+ Deploy model** > **Deploy base model**
3. Search for and select a Claude model (for example, `claude-sonnet-4-6`)
4. Configure deployment settings:
   - **Deployment name:** Defaults to the model ID, but you can customize it (for example, `my-claude-deployment`). The deployment name cannot be changed after it has been created.
   - **Deployment type:** Select Global Standard (recommended for Claude)
5. Select **Deploy** and wait for provisioning to complete
6. Once deployed, you can find your endpoint URL and keys under **Keys and Endpoint**

<Note>
  The deployment name you choose becomes the value you pass in the `model` parameter of your API requests. You can create multiple deployments of the same model with different names to manage separate configurations or rate limits.
</Note>

## Authentication

Claude in Foundry supports two authentication methods: API keys and Entra ID tokens. Both methods use Azure-hosted endpoints in the format `https://{resource}.services.ai.azure.com/anthropic/v1/*`.

### API key authentication

After provisioning your Foundry Claude resource, you can obtain an API key from the Foundry portal:

1. Navigate to your resource in the Foundry portal
2. Go to **Keys and Endpoint** section
3. Copy one of the provided API keys
4. Use either the `api-key` or `x-api-key` header in your requests, or provide it to the SDK

The Foundry SDKs require an API key and either a resource name or base URL. The C#, Java, PHP, Python, and TypeScript SDKs automatically read these from the following environment variables if they are defined:

- `ANTHROPIC_FOUNDRY_API_KEY` - Your API key
- `ANTHROPIC_FOUNDRY_RESOURCE` - Your resource name (for example, `example-resource`)
- `ANTHROPIC_FOUNDRY_BASE_URL` - Alternative to resource name; the full base URL (for example, `https://example-resource.services.ai.azure.com/anthropic/`)

<Note>
The `resource` and `base_url` parameters are mutually exclusive. Provide either the resource name (which the SDK uses to construct the URL as `https://{resource}.services.ai.azure.com/anthropic/`) or the full base URL directly.
</Note>

**Example using API key:**

<Tabs>
<Tab title="cURL">

```bash cURL nocheck
curl https://{resource}.services.ai.azure.com/anthropic/v1/messages \
  -H "content-type: application/json" \
  -H "api-key: YOUR_AZURE_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Hello!"}
    ]
  }'
```
</Tab>

<Tab title="CLI">

```bash CLI nocheck
# ant reads ANTHROPIC_API_KEY and sends it as x-api-key, which Foundry accepts
export ANTHROPIC_API_KEY="YOUR_AZURE_API_KEY"

ant messages create \
  --base-url https://example-resource.services.ai.azure.com/anthropic \
  --model claude-opus-4-7 \
  --max-tokens 1024 \
  --message '{role: user, content: "Hello!"}' \
  --transform content
```
</Tab>

<Tab title="Python">

```python nocheck
import os
from anthropic import AnthropicFoundry

client = AnthropicFoundry(
    api_key=os.environ.get("ANTHROPIC_FOUNDRY_API_KEY"),
    resource="example-resource",  # your resource name
)

message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(message.content)
```
</Tab>

<Tab title="TypeScript">

```typescript nocheck
import AnthropicFoundry from "@anthropic-ai/foundry-sdk";

const client = new AnthropicFoundry({
  apiKey: process.env.ANTHROPIC_FOUNDRY_API_KEY,
  resource: "example-resource" // your resource name
});

const message = await client.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello!" }]
});
console.log(message.content);
```
</Tab>

<Tab title="C#">

```csharp nocheck
using Anthropic.Foundry;
using Anthropic.Models.Messages;

var client = new AnthropicFoundryClient(
    new AnthropicFoundryApiKeyCredentials(
        Environment.GetEnvironmentVariable("ANTHROPIC_FOUNDRY_API_KEY")!,
        "example-resource"
    )
);

var response = await client.Messages.Create(new MessageCreateParams
{
    Model = "claude-opus-4-7",
    MaxTokens = 1024,
    Messages = [new() { Role = Role.User, Content = "Hello!" }],
});

Console.WriteLine(
    string.Join("", response.Content
        .Select(block => block.Value)
        .OfType<TextBlock>()
        .Select(textBlock => textBlock.Text)));
```
</Tab>

<Tab title="Java">

```java Java nocheck
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.foundry.backends.FoundryBackend;
import com.anthropic.models.messages.MessageCreateParams;

void main() {
    // Requires env vars: ANTHROPIC_FOUNDRY_API_KEY, ANTHROPIC_FOUNDRY_RESOURCE
    AnthropicClient client = AnthropicOkHttpClient.builder()
        .backend(FoundryBackend.fromEnv())
        .build();

    MessageCreateParams params = MessageCreateParams.builder()
        .model("claude-opus-4-7")
        .maxTokens(1024)
        .addUserMessage("Hello!")
        .build();

    client.messages().create(params).content().stream()
        .flatMap(block -> block.text().stream())
        .forEach(textBlock -> System.out.println(textBlock.text()));
}
```
</Tab>

<Tab title="PHP">

```php PHP nocheck
<?php

use Anthropic\Foundry;

$client = Foundry\Client::withCredentials(
    apiKey: getenv('ANTHROPIC_FOUNDRY_API_KEY'),
    baseUrl: 'https://example-resource.services.ai.azure.com/anthropic/v1',
);

$message = $client->messages->create(
    maxTokens: 1024,
    messages: [
        ['role' => 'user', 'content' => 'Hello!']
    ],
    model: 'claude-opus-4-7',
);
echo $message->content[0]->text;
```
</Tab>

<Tab title="Ruby">
<Note>
The Anthropic Ruby SDK does not currently support Microsoft Foundry. You can use the standard `Anthropic::Client` with a custom `base_url` pointing to your Foundry endpoint, but Azure-specific authentication (Entra ID) is not built in. For full Foundry support, use the C#, Java, PHP, Python, or TypeScript SDKs.
</Note>
</Tab>
</Tabs>

<Warning>
Keep your API keys secure. Never commit them to version control or share them publicly. Anyone with access to your API key can make requests to Claude through your Foundry resource.
</Warning>

### Microsoft Entra authentication

For enhanced security and centralized access management, you can use Entra ID tokens:

1. Enable Entra authentication for your Foundry resource
2. Obtain an access token from Entra ID
3. Use the token in the `Authorization: Bearer {TOKEN}` header

**Example using Entra ID:**

<Tabs>
<Tab title="cURL">

```bash cURL nocheck
# Get Microsoft Entra ID token
ACCESS_TOKEN=$(az account get-access-token --resource https://cognitiveservices.azure.com --query accessToken -o tsv)

# Make request with token. Replace {resource} with your resource name
curl https://{resource}.services.ai.azure.com/anthropic/v1/messages \
  -H "content-type: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Hello!"}
    ]
  }'
```
</Tab>

<Tab title="Python">

```python nocheck
import os
from anthropic import AnthropicFoundry
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Get Microsoft Entra ID token using token provider pattern
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

# Create client with Entra ID authentication
client = AnthropicFoundry(
    resource="example-resource",  # your resource name
    azure_ad_token_provider=token_provider,  # Use token provider for Entra ID auth
)

# Make request
message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(message.content)
```
</Tab>

<Tab title="TypeScript">

```typescript nocheck
import AnthropicFoundry from "@anthropic-ai/foundry-sdk";
import { DefaultAzureCredential, getBearerTokenProvider } from "@azure/identity";

// Get Entra ID token using token provider pattern
const credential = new DefaultAzureCredential();
const tokenProvider = getBearerTokenProvider(
  credential,
  "https://cognitiveservices.azure.com/.default"
);

// Create client with Entra ID authentication
const client = new AnthropicFoundry({
  resource: "example-resource", // your resource name
  azureADTokenProvider: tokenProvider // Use token provider for Entra ID auth
});

// Make request
const message = await client.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello!" }]
});
console.log(message.content);
```
</Tab>

<Tab title="C#">

```csharp nocheck
using Anthropic.Foundry;
using Anthropic.Models.Messages;
using Azure.Identity;

var client = new AnthropicFoundryClient(
    new AnthropicFoundryIdentityTokenCredentials(
        new DefaultAzureCredential(),
        "example-resource"
    )
);

var response = await client.Messages.Create(new MessageCreateParams
{
    Model = "claude-opus-4-7",
    MaxTokens = 1024,
    Messages = [new() { Role = Role.User, Content = "Hello!" }],
});

Console.WriteLine(
    string.Join("", response.Content
        .Select(block => block.Value)
        .OfType<TextBlock>()
        .Select(textBlock => textBlock.Text)));
```
</Tab>

<Tab title="Java">

```java Java nocheck hidelines={1..2,4,8}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.foundry.backends.FoundryBackend;
import com.anthropic.models.messages.MessageCreateParams;
import com.azure.identity.AuthenticationUtil;
import com.azure.identity.DefaultAzureCredentialBuilder;
import java.util.function.Supplier;

void main() {
    Supplier<String> bearerTokenSupplier = AuthenticationUtil.getBearerTokenSupplier(
        new DefaultAzureCredentialBuilder().build(),
        "https://cognitiveservices.azure.com/.default"
    );

    AnthropicClient client = AnthropicOkHttpClient.builder()
        .backend(FoundryBackend.builder()
            .bearerTokenSupplier(bearerTokenSupplier)
            .resource("example-resource")
            .build())
        .build();

    MessageCreateParams params = MessageCreateParams.builder()
        .model("claude-opus-4-7")
        .maxTokens(1024)
        .addUserMessage("Hello!")
        .build();

    client.messages().create(params).content().stream()
        .flatMap(block -> block.text().stream())
        .forEach(textBlock -> System.out.println(textBlock.text()));
}
```
</Tab>

<Tab title="PHP">

```php PHP nocheck
<?php

use Anthropic\Foundry;

// Obtain an Entra ID access token, for example via the Azure CLI:
//   az account get-access-token --resource https://cognitiveservices.azure.com \
//     --query accessToken -o tsv
$token = getenv('AZURE_ACCESS_TOKEN');

$client = Foundry\Client::withCredentials(
    authToken: $token,
    baseUrl: 'https://example-resource.services.ai.azure.com/anthropic/v1',
);

$message = $client->messages->create(
    maxTokens: 1024,
    messages: [
        ['role' => 'user', 'content' => 'Hello!']
    ],
    model: 'claude-opus-4-7',
);
echo $message->content[0]->text;
```
</Tab>

<Tab title="Ruby">
<Note>
The Anthropic Ruby SDK does not currently support Microsoft Foundry. You can use the standard `Anthropic::Client` with a custom `base_url` pointing to your Foundry endpoint, but Azure-specific authentication (Entra ID) is not built in. For full Foundry support, use the C#, Java, PHP, Python, or TypeScript SDKs.
</Note>
</Tab>
</Tabs>

<Note>
Microsoft Entra ID authentication allows you to manage access using Azure RBAC, integrate with your organization's identity management, and avoid managing API keys manually.
</Note>

## Correlation request IDs

Foundry includes request identifiers in HTTP response headers for debugging and tracing. When contacting support, provide both the `request-id` and `apim-request-id` values to help teams quickly locate and investigate your request across both Anthropic and Azure systems.

## Feature support

Claude in Foundry supports most of Claude's powerful features. You can find all the features currently supported in [Features overview](/docs/en/build-with-claude/overview).

### Context window

Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6 have a [1M-token context window](/docs/en/build-with-claude/context-windows) on Microsoft Foundry. Other Claude models, including Sonnet 4.5, have a 200k-token context window.

### Features not supported

- Admin API (`/v1/organizations/*` endpoints)
- Compliance API (`/v1/compliance/*` endpoints)
- Models API (`/v1/models`)
- Message Batches API (`/v1/messages/batches`)

## API responses

API responses from Claude in Foundry follow the standard [Claude API response format](/docs/en/api/messages/create). This includes the `usage` object in response bodies, which provides detailed token consumption information for your requests. The `usage` object is consistent across all platforms (Claude API, Foundry, Claude Platform on AWS, Amazon Bedrock, and Vertex AI).

For details on response headers specific to Foundry, see [Correlation request IDs](#correlation-request-ids).

## API model IDs and deployments

The following Claude models are available through Foundry. The latest generation models (Opus 4.7, Opus 4.6, Sonnet 4.6, and Haiku 4.5) offer the most advanced capabilities:

| Model             | Default deployment name     |
| :---------------- | :-------------------------- |
| Claude Opus 4.7   | `claude-opus-4-7`           |
| Claude Opus 4.6   | `claude-opus-4-6`           |
| Claude Opus 4.5   | `claude-opus-4-5`           |
| Claude Opus 4.1   | `claude-opus-4-1`           |
| Claude Sonnet 4.6 | `claude-sonnet-4-6`         |
| Claude Sonnet 4.5 | `claude-sonnet-4-5`         |
| Claude Haiku 4.5  | `claude-haiku-4-5`          |

By default, deployment names match the model IDs shown in the preceding table. However, you can create custom deployments with different names in the Foundry portal to manage different configurations, versions, or rate limits. Use the deployment name (not necessarily the model ID) in your API requests.

## Monitoring and logging

Azure provides comprehensive monitoring and logging capabilities for your Claude usage through standard Azure patterns:

- **Azure Monitor:** Track API usage, latency, and error rates
- **Azure Log Analytics:** Query and analyze request/response logs
- **Cost Management:** Monitor and forecast costs associated with Claude usage

Anthropic recommends logging your activity on at least a 30-day rolling basis to understand usage patterns and investigate any potential issues.

<Note>
Azure's logging services are configured within your Azure subscription. Enabling logging does not provide Microsoft or Anthropic access to your content beyond what's necessary for billing and service operation.
</Note>

## Troubleshooting

### Authentication errors

**Error:** `401 Unauthorized` or `Invalid API key`

- **Solution:** Verify your API key is correct. You can obtain a new API key from the Foundry portal under **Keys and Endpoint** for your Foundry resource.
- **Solution:** If using Microsoft Entra ID, ensure your access token is valid and hasn't expired. Tokens typically expire after 1 hour.

**Error:** `403 Forbidden`

- **Solution:** Your Azure account may lack the necessary permissions. Ensure you have the appropriate Azure RBAC role assigned (for example, "Cognitive Services OpenAI User").

### Rate limiting

**Error:** `429 Too Many Requests`

- **Solution:** You've exceeded your rate limit. Implement exponential backoff and retry logic in your application.
- **Solution:** Consider requesting rate limit increases through the Azure portal or Azure support.

#### Rate limit headers

Foundry does not include Anthropic's standard rate limit headers (`anthropic-ratelimit-tokens-limit`, `anthropic-ratelimit-tokens-remaining`, `anthropic-ratelimit-tokens-reset`, `anthropic-ratelimit-input-tokens-limit`, `anthropic-ratelimit-input-tokens-remaining`, `anthropic-ratelimit-input-tokens-reset`, `anthropic-ratelimit-output-tokens-limit`, `anthropic-ratelimit-output-tokens-remaining`, and `anthropic-ratelimit-output-tokens-reset`) in responses. Manage rate limiting through Azure's monitoring tools instead.

### Model and deployment errors

**Error:** `Model not found` or `Deployment not found`

- **Solution:** Verify you're using the correct deployment name. If you haven't created a custom deployment, use the default model ID (for example, `claude-sonnet-4-6`).
- **Solution:** Ensure the model/deployment is available in your Azure region.

**Error:** `Invalid model parameter`

- **Solution:** The model parameter should contain your deployment name, which can be customized in the Foundry portal. Verify the deployment exists and is properly configured.

<Info>
[Claude Mythos Preview](https://anthropic.com/glasswing) is a research preview available to invited customers on Microsoft Foundry. For more information, see [Project Glasswing](https://anthropic.com/glasswing).
</Info>

## Additional resources

- **Foundry documentation:** [ai.azure.com/catalog](https://ai.azure.com/catalog/publishers/anthropic)
- **Azure pricing:** [azure.microsoft.com/en-us/pricing/details/ai-foundry](https://azure.microsoft.com/en-us/pricing/details/ai-foundry/#pricing)
- **Anthropic pricing details:** [Model pricing](/docs/en/about-claude/pricing#model-pricing)
- **Authentication guide:** See [Authentication](#authentication)
- **Azure portal:** [portal.azure.com](https://portal.azure.com/)
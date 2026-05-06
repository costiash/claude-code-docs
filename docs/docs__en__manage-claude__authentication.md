# Authentication

Authenticate to the Claude API with API keys or Workload Identity Federation.

---

The Claude API supports two ways to authenticate requests:

| Method | Credential | Best for |
|---|---|---|
| [API key](#api-keys) | Long-lived `sk-ant-api...` secret in the `x-api-key` header | Local development, prototyping, scripts, and single-tenant servers where you control secret storage |
| [Workload Identity Federation](#workload-identity-federation) | Short-lived bearer token exchanged from your identity provider's identity token | Production workloads on cloud platforms (AWS, Google Cloud, Azure), CI/CD pipelines, and Kubernetes, where you want to eliminate static secrets |

Both methods grant the same access to Claude API endpoints. Choose API keys to get started quickly, and move to Workload Identity Federation when your workload already has a platform-issued identity you can federate.

## API keys

API keys are static secrets that you generate in the Claude Console and pass on every request.

- **Create a key:** Go to [Settings → API keys](https://platform.claude.com/settings/keys) in the Claude Console. Use [workspaces](https://platform.claude.com/settings/workspaces) to scope keys by project or environment.
- **Send the key:** Set the `x-api-key` header on direct HTTP requests, or set the `ANTHROPIC_API_KEY` environment variable and the [client SDKs](/docs/en/api/client-sdks) pick it up automatically.

```http
POST /v1/messages
x-api-key: YOUR_API_KEY
anthropic-version: 2023-06-01
content-type: application/json
```

API keys have no expiry. Store them in a secrets manager, rotate them periodically, and revoke any key you suspect has leaked.

<CodeGroup>

```bash cURL
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Hello, Claude"}]
  }'
```

```python Python hidelines={1..2}
from anthropic import Anthropic

client = Anthropic(api_key="my-anthropic-api-key")
# or, with ANTHROPIC_API_KEY set in the environment:
client = Anthropic()
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({ apiKey: "my-anthropic-api-key" });
// or, with ANTHROPIC_API_KEY set in the environment:
// const client = new Anthropic();
```

```go Go hidelines={1..8,12..13}
package main

import (
	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("sk-ant-api03-..."), // defaults to os.LookupEnv("ANTHROPIC_API_KEY")
	)
	_ = client
}
```

```java Java nocheck
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

// Explicit
AnthropicClient client = AnthropicOkHttpClient.builder()
  .apiKey("my-anthropic-api-key")
  .build();

// From ANTHROPIC_API_KEY (or anthropic.apiKey system property)
AnthropicClient clientFromEnv = AnthropicOkHttpClient.fromEnv();
```

```csharp C#
using Anthropic;

AnthropicClient client = new() { ApiKey = "my-anthropic-api-key" };
// Or, with ANTHROPIC_API_KEY set in the environment:
// AnthropicClient client = new();
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

// Reads ANTHROPIC_API_KEY from the environment
$client = new Client();
// Or pass the key explicitly:
$client = new Client(apiKey: 'my-anthropic-api-key');
```

```ruby Ruby hidelines={1..2}
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")
# or, with ANTHROPIC_API_KEY set in the environment:
anthropic = Anthropic::Client.new
```

```bash CLI
# See /docs/en/api/sdks/cli#api-key for zsh, bash, and Windows variants
export ANTHROPIC_API_KEY=sk-ant-api03-...
```

</CodeGroup>

## Workload Identity Federation

Workload Identity Federation (WIF) lets a workload authenticate with a short-lived identity token issued by an identity provider (IdP) you already trust, such as AWS IAM, Google Cloud, or any standards-compliant OIDC issuer (such as GitHub Actions, Kubernetes service accounts, SPIFFE, Microsoft Entra ID, or Okta). The workload exchanges its IdP-issued JWT at `POST /v1/oauth/token` for a short-lived Claude API access token, and the SDK refreshes that token automatically before it expires. There is no `sk-ant-api...` string to mint, distribute, or rotate.

Federation removes long-lived Claude API keys from your environment, which shrinks the blast radius of a leaked credential and lets you manage access with the same IdP controls you already use for cloud resources. It does not, on its own, guarantee end-to-end security: the trust chain is only as strong as your identity provider's configuration, and a long-lived secret one hop upstream (for example, a static cloud credential that can mint IdP tokens) can still undermine it. Pair federation with your provider's controls, such as IP allowlists, MFA, and audit logging.

To configure federation, you create three resources in the Claude Console (a service account, a federation issuer, and a federation rule) and then point your SDK at the rule. See [Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation) for the full setup walkthrough.

## Next steps

<CardGroup cols={2}>
  <Card title="Set up Workload Identity Federation" icon="lock" href="/docs/en/manage-claude/workload-identity-federation">
    Configure issuers, rules, and service accounts, then exchange tokens
  </Card>
  <Card title="Identity provider guides" icon="cloud" href="/docs/en/manage-claude/workload-identity-federation#identity-providers">
    Step-by-step guides for AWS, Google Cloud, Azure, GitHub Actions, Kubernetes, SPIFFE, and Okta
  </Card>
  <Card title="WIF reference" icon="book" href="/docs/en/manage-claude/wif-reference">
    Environment variables, validation rules, profile configuration, and error reference
  </Card>
  <Card title="Client SDKs" icon="code" href="/docs/en/api/client-sdks">
    Python, TypeScript, Go, Java, C#, Ruby, PHP, and the CLI
  </Card>
</CardGroup>
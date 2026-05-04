# Use WIF with Microsoft Azure

Federate Azure managed identities and Entra Workload Identity with the Claude API so your Azure workloads can call Claude without static API keys.

---

Azure workloads authenticate to the Claude API by presenting a JSON Web Token (JWT) issued by Microsoft Entra ID, then exchanging it for a short-lived Anthropic access token. There are two common ways to obtain the Entra-issued token:

- **Managed identity (VMs, App Service, Functions, Container Apps):** The workload calls the Azure Instance Metadata Service (IMDS) at `http://169.254.169.254/metadata/identity/oauth2/token` and receives a JWT for its assigned identity.
- **Entra Workload Identity (AKS pods):** Kubernetes projects a service account token (signed by the AKS cluster's OIDC issuer) into the pod at the path in `AZURE_FEDERATED_TOKEN_FILE`. The workload exchanges that token at Entra for an Entra-issued access token.

In both cases the Entra-issued token you present to Anthropic has the tenant-specific issuer `https://login.microsoftonline.com/<TENANT_ID>/v2.0` and carries the managed identity's object ID in the `sub` and `oid` claims. You register that issuer with Anthropic once, write a federation rule that matches the expected claims, and your workload exchanges its Entra token for an `sk-ant-oat01-...` access token at runtime.

<Tip>
AKS pods can alternatively skip the Entra exchange and present the Kubernetes-projected service account token to Anthropic directly. That path registers your AKS cluster's OIDC issuer with Anthropic instead of your Entra tenant. See [Kubernetes](/docs/en/build-with-claude/wif-providers/kubernetes) for that flow.
</Tip>

## Prerequisites

- Familiarity with [WIF concepts](/docs/en/build-with-claude/workload-identity-federation#concepts): service accounts, federation issuers, and federation rules.
- An Azure subscription with permission to assign managed identities (or configure Entra Workload Identity on AKS).
- Your Microsoft Entra tenant ID. Find it in the Azure portal under **Microsoft Entra ID → Overview → Tenant ID**.
- Permission to create service accounts, federation issuers, and federation rules in the Claude Console for your Anthropic organization.

## Configure Azure

Set up the identity that Azure will issue tokens for. Choose the path that matches where your workload runs.

<Tabs>
<Tab title="VM, App Service, Functions, Container Apps">

Enable a system-assigned or user-assigned managed identity on your Azure resource. In the Azure portal, open the resource, go to **Identity**, and turn on **System assigned** (or attach a user-assigned identity).

After the identity is created, note its **Object (principal) ID**. This GUID appears as both the `sub` and `oid` claims in the issued token, and your Anthropic federation rule will match on it. You can find it on the resource's **Identity** page, or under **Microsoft Entra ID → Enterprise applications** for user-assigned identities.

No further Azure-side configuration is required. The Azure Instance Metadata Service is reachable at `169.254.169.254` from inside the resource once the identity is attached.

</Tab>
<Tab title="Entra Workload Identity (AKS)">

Entra Workload Identity federates a Kubernetes service account with an Entra application so pods can exchange their cluster-issued service account token for an Entra-issued access token.

1. Enable the OIDC issuer on your AKS cluster (`az aks update --enable-oidc-issuer --enable-workload-identity ...`).
2. Deploy the `azure-workload-identity` mutating webhook.
3. Create a user-assigned managed identity and a federated credential that trusts the cluster's OIDC issuer for your Kubernetes service account.
4. Label your pod spec with `azure.workload.identity/use: "true"` and set `serviceAccountName` to the federated service account.

The webhook injects `AZURE_FEDERATED_TOKEN_FILE`, `AZURE_CLIENT_ID`, and `AZURE_TENANT_ID` into the pod. The file at `AZURE_FEDERATED_TOKEN_FILE` contains the Kubernetes-projected service account token, signed by the AKS cluster's OIDC issuer.

</Tab>
</Tabs>

### Token claims

An Entra-issued token for a managed identity carries these claims:

```json
{
  "iss": "https://login.microsoftonline.com/<TENANT_ID>/v2.0",
  "sub": "9f8e7d6c-1a2b-3c4d-5e6f-...",
  "aud": "https://api.anthropic.com",
  "oid": "9f8e7d6c-1a2b-3c4d-5e6f-...",
  "tid": "<TENANT_ID>",
  "azp": "<CLIENT_ID>",
  "exp": 1775527120
}
```

`sub` and `oid` are identical (the managed identity's object ID). `azp` is the application or client ID. Match on `oid` to authorize one specific identity, or on `azp` to authorize any identity associated with an application registration. The `tid` claim repeats your tenant ID; matching on it is defense in depth, because the issuer URL already pins the tenant.

## Configure Anthropic

Follow the [setup walkthrough](/docs/en/build-with-claude/workload-identity-federation#set-up-federation) to register a federation issuer, create an Anthropic service account, and create a federation rule in the Claude Console. In the Console, choose the **OIDC** provider option and supply the Entra-specific values that follow.

**Federation issuer:** Entra publishes an OIDC discovery document at the per-tenant issuer URL, so use discovery mode. Each Azure tenant you federate needs its own issuer record.

```json
{
  "name": "azure-prod-tenant",
  "issuer_url": "https://login.microsoftonline.com/<TENANT_ID>/v2.0",
  "jwks_source": "discovery"
}
```

<Note>
Depending on the token version, the `iss` claim may be `https://sts.windows.net/<TENANT_ID>/` instead. Decode your managed-identity token (the Verify section below shows how) and register whichever `iss` value it contains. The two URLs share the same JWKS, so discovery mode works for either.
</Note>

**Federation rule:** Match on the managed identity's object ID and your tenant ID.

```json
{
  "name": "azure-inference-worker",
  "issuer_id": "fdis_...",
  "match": {
    "audience": "https://api.anthropic.com",
    "claims": {
      "oid": "9f8e7d6c-1a2b-3c4d-5e6f-...",
      "tid": "<TENANT_ID>"
    }
  },
  "target": {
    "type": "service_account",
    "service_account_id": "svac_..."
  },
  "workspace_id": "wrkspc_...",
  "oauth_scope": "workspace:developer",
  "token_lifetime_seconds": 600
}
```

## Acquire and use the token

At runtime your workload fetches its Entra token, exchanges it at `POST /v1/oauth/token`, and uses the returned bearer token to call Claude. Each Anthropic SDK handles the exchange and refresh loop when you supply a token-provider callable, as shown in the following examples. The cURL tab shows the raw flow.

<CodeGroup>

```bash cURL nocheck
# 1. Fetch the Entra-issued token from IMDS (managed identity).
#    For AKS with Entra Workload Identity, use the two-hop exchange in the
#    "On AKS with Entra Workload Identity" section instead.
ENTRA_TOKEN=$(curl -sS -H "Metadata: true" \
  "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://api.anthropic.com" \
  | jq -r .access_token)

# 2. Exchange it for an Anthropic access token.
RESPONSE=$(curl -sS https://api.anthropic.com/v1/oauth/token \
  -H "content-type: application/json" \
  --data @- <<JSON
{
  "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
  "assertion": "$ENTRA_TOKEN",
  "federation_rule_id": "$ANTHROPIC_FEDERATION_RULE_ID",
  "organization_id": "$ANTHROPIC_ORGANIZATION_ID",
  "service_account_id": "$ANTHROPIC_SERVICE_ACCOUNT_ID"
}
JSON
)

ACCESS_TOKEN=$(echo "$RESPONSE" | jq -r .access_token)

# 3. Call the Claude API with the bearer token.
curl https://api.anthropic.com/v1/messages \
  -H "authorization: Bearer $ACCESS_TOKEN" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Hello from Azure"}]
  }' | jq -r '.content[0].text'
```

```python Python nocheck
import os

import anthropic
import requests
from anthropic import WorkloadIdentityCredentials

IMDS_URL = "http://169.254.169.254/metadata/identity/oauth2/token"


def fetch_entra_token() -> str:
    """Fetch a managed identity token from Azure IMDS."""
    response = requests.get(
        IMDS_URL,
        headers={"Metadata": "true"},
        params={"api-version": "2018-02-01", "resource": "https://api.anthropic.com"},
        timeout=5,
    )
    response.raise_for_status()
    return response.json()["access_token"]


client = anthropic.Anthropic(
    credentials=WorkloadIdentityCredentials(
        identity_token_provider=fetch_entra_token,
        federation_rule_id=os.environ["ANTHROPIC_FEDERATION_RULE_ID"],
        organization_id=os.environ["ANTHROPIC_ORGANIZATION_ID"],
        service_account_id=os.environ["ANTHROPIC_SERVICE_ACCOUNT_ID"],
    ),
)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello from Azure"}],
)
print(message.content[0].text)
```

```typescript TypeScript nocheck
import Anthropic from "@anthropic-ai/sdk";
import { oidcFederationProvider } from "@anthropic-ai/sdk/lib/credentials/oidc-federation";

const IMDS_URL =
  "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://api.anthropic.com";

async function fetchEntraToken(): Promise<string> {
  const response = await fetch(IMDS_URL, {
    headers: { Metadata: "true" }
  });
  const body = (await response.json()) as { access_token: string };
  return body.access_token;
}

const client = new Anthropic({
  credentials: oidcFederationProvider({
    identityTokenProvider: fetchEntraToken,
    federationRuleId: process.env.ANTHROPIC_FEDERATION_RULE_ID!,
    organizationId: process.env.ANTHROPIC_ORGANIZATION_ID!,
    serviceAccountId: process.env.ANTHROPIC_SERVICE_ACCOUNT_ID,
    baseURL: "https://api.anthropic.com",
    fetch
  })
});

const message = await client.messages.create({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello from Azure" }]
});
for (const block of message.content) {
  if (block.type === "text") {
    console.log(block.text);
  }
}
```

```go Go nocheck
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"os"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

const imdsURL = "http://169.254.169.254/metadata/identity/oauth2/token" +
	"?api-version=2018-02-01&resource=https://api.anthropic.com"

// azureIMDSToken fetches a managed identity token from Azure IMDS.
func azureIMDSToken(ctx context.Context) (string, error) {
	req, err := http.NewRequestWithContext(ctx, http.MethodGet, imdsURL, nil)
	if err != nil {
		return "", err
	}
	req.Header.Set("Metadata", "true")
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return "", fmt.Errorf("call IMDS: %w", err)
	}
	defer resp.Body.Close()
	var body struct {
		AccessToken string `json:"access_token"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&body); err != nil {
		return "", fmt.Errorf("decode IMDS response: %w", err)
	}
	return body.AccessToken, nil
}

func main() {
	client := anthropic.NewClient(
		option.WithFederationTokenProvider(azureIMDSToken, option.FederationOptions{
			FederationRuleID: os.Getenv("ANTHROPIC_FEDERATION_RULE_ID"),
			OrganizationID:   os.Getenv("ANTHROPIC_ORGANIZATION_ID"),
			ServiceAccountID: os.Getenv("ANTHROPIC_SERVICE_ACCOUNT_ID"),
		}),
	)

	message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeSonnet4_6,
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("Hello from Azure")),
		},
	})
	if err != nil {
		panic(err)
	}
	fmt.Println(message.Content[0].Text)
}
```

```java Java nocheck hidelines={1..12,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.credentials.IdentityTokenProvider;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

void main() {
    HttpClient http = HttpClient.newHttpClient();
    HttpRequest metadataRequest = HttpRequest.newBuilder()
            .uri(URI.create("http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://api.anthropic.com"))
            .header("Metadata", "true")
            .build();

    IdentityTokenProvider fetchEntraToken = () -> {
        try {
            var response = http.send(metadataRequest, HttpResponse.BodyHandlers.ofString());
            return new ObjectMapper().readTree(response.body()).get("access_token").asText();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    };

    AnthropicClient client = AnthropicOkHttpClient.builder()
            .federationTokenProvider(
                    fetchEntraToken,
                    System.getenv("ANTHROPIC_FEDERATION_RULE_ID"),
                    System.getenv("ANTHROPIC_ORGANIZATION_ID"),
                    System.getenv("ANTHROPIC_SERVICE_ACCOUNT_ID"))
            .build();

    var message = client.messages().create(MessageCreateParams.builder()
            .model(Model.CLAUDE_SONNET_4_6)
            .maxTokens(1024)
            .addUserMessage("Hello from Azure")
            .build());

    IO.println(message.content());
}
```

```csharp C# nocheck hidelines={1..4}
using System.Text.Json;
using Anthropic.Models.Messages;
using Anthropic.Oidc;

var credentials = new WorkloadIdentityCredentials(new WorkloadIdentityOptions
{
    FederationRuleId = Environment.GetEnvironmentVariable("ANTHROPIC_FEDERATION_RULE_ID")!,
    OrganizationId = Environment.GetEnvironmentVariable("ANTHROPIC_ORGANIZATION_ID"),
    ServiceAccountId = Environment.GetEnvironmentVariable("ANTHROPIC_SERVICE_ACCOUNT_ID"),
    IdentityTokenProvider = new EntraTokenProvider(),
});
using var client = new AnthropicOidcClient(credentials);

var message = await client.Messages.Create(new()
{
    Model = Model.ClaudeSonnet4_6,
    MaxTokens = 1024,
    Messages = [new() { Role = Role.User, Content = "Hello from Azure" }],
});
foreach (var block in message.Content)
{
    if (block.Value is TextBlock textBlock)
    {
        Console.WriteLine(textBlock.Text);
    }
}

class EntraTokenProvider : IIdentityTokenProvider
{
    private const string IMDS_URL =
        "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://api.anthropic.com";

    private static readonly HttpClient httpClient = new()
    {
        DefaultRequestHeaders = { { "Metadata", "true" } },
    };

    public async Task<string> GetIdentityTokenAsync(CancellationToken ct = default)
    {
        using var json = await JsonDocument.ParseAsync(
            await httpClient.GetStreamAsync(IMDS_URL, ct), default, ct);
        return json.RootElement.GetProperty("access_token").GetString()!;
    }
}
```

```php PHP nocheck hidelines={1..3}
<?php
require 'vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Credentials\WorkloadIdentityCredentials;

const IMDS_URL = 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://api.anthropic.com';

function fetchEntraToken(): string
{
    $context = stream_context_create([
        'http' => ['header' => "Metadata: true\r\n"],
    ]);
    $body = json_decode(file_get_contents(IMDS_URL, false, $context), true);
    return $body['access_token'];
}

$credentials = new WorkloadIdentityCredentials(
    identityTokenProvider: fetchEntraToken(...),
    federationRuleId: getenv('ANTHROPIC_FEDERATION_RULE_ID'),
    organizationId: getenv('ANTHROPIC_ORGANIZATION_ID'),
    serviceAccountId: getenv('ANTHROPIC_SERVICE_ACCOUNT_ID'),
);
$client = new Client(credentials: $credentials);

$message = $client->messages->create(
    model: 'claude-sonnet-4-6',
    maxTokens: 1024,
    messages: [['role' => 'user', 'content' => 'Hello from Azure']],
);
echo $message->content[0]->text, PHP_EOL;
```

```ruby Ruby nocheck
require "anthropic"
require "json"
require "net/http"

IMDS_URL = "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://api.anthropic.com"

def fetch_entra_token
  response = Net::HTTP.get(URI(IMDS_URL), {"Metadata" => "true"})
  JSON.parse(response).fetch("access_token")
end

credentials = Anthropic::WorkloadIdentityCredentials.new(
  identity_token_provider: -> { fetch_entra_token },
  federation_rule_id: ENV.fetch("ANTHROPIC_FEDERATION_RULE_ID"),
  organization_id: ENV.fetch("ANTHROPIC_ORGANIZATION_ID"),
  service_account_id: ENV.fetch("ANTHROPIC_SERVICE_ACCOUNT_ID")
)
client = Anthropic::Client.new(credentials: credentials)

message = client.messages.create(
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [{role: "user", content: "Hello from Azure"}]
)
puts message.content.first.text
```

```bash CLI nocheck
# Write the Entra-issued access token to a file the CLI can read
ANTHROPIC_IDENTITY_TOKEN_FILE=$(mktemp)
curl -sS -H "Metadata: true" \
  "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://api.anthropic.com" \
  | jq -r .access_token > "$ANTHROPIC_IDENTITY_TOKEN_FILE"
export ANTHROPIC_IDENTITY_TOKEN_FILE

# ANTHROPIC_FEDERATION_RULE_ID, ANTHROPIC_ORGANIZATION_ID, and
# ANTHROPIC_SERVICE_ACCOUNT_ID are read from the environment.
ant messages create \
  --model claude-sonnet-4-6 \
  --max-tokens 1024 \
  --message '{role: user, content: "Hello from Azure"}'
```

</CodeGroup>

### On AKS with Entra Workload Identity

On AKS, the file at `AZURE_FEDERATED_TOKEN_FILE` is a Kubernetes-projected service account token signed by your cluster's OIDC issuer, not an Entra-issued token. To stay on the Entra-mediated path described on this page, exchange that token at `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token` (federated `client_credentials` grant) first, then pass the resulting Entra access token to the Anthropic SDK as the identity token.

<CodeGroup>

```bash cURL nocheck
# 1. Exchange the Kubernetes-projected token (at $AZURE_FEDERATED_TOKEN_FILE)
#    for an Entra-issued JWT.
ENTRA_JWT=$(curl -sS "https://login.microsoftonline.com/$AZURE_TENANT_ID/oauth2/v2.0/token" \
  -d grant_type=client_credentials \
  -d "client_id=$AZURE_CLIENT_ID" \
  --data-urlencode "scope=https://api.anthropic.com/.default" \
  -d client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer \
  --data-urlencode "client_assertion@$AZURE_FEDERATED_TOKEN_FILE" \
  | jq -r .access_token)

# 2. Exchange the Entra JWT for an Anthropic access token.
ACCESS_TOKEN=$(curl -sS https://api.anthropic.com/v1/oauth/token \
  -H "content-type: application/json" \
  -d @- <<JSON | jq -r .access_token
{
  "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
  "assertion": "$ENTRA_JWT",
  "federation_rule_id": "$ANTHROPIC_FEDERATION_RULE_ID",
  "organization_id": "$ANTHROPIC_ORGANIZATION_ID",
  "service_account_id": "$ANTHROPIC_SERVICE_ACCOUNT_ID"
}
JSON
)

# 3. Call the Claude API.
curl -sS https://api.anthropic.com/v1/messages \
  -H "authorization: Bearer $ACCESS_TOKEN" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Hello from Azure"}]
  }' | jq -r '.content[0].text'
```

```python Python nocheck
import os
from pathlib import Path
import httpx
import anthropic
from anthropic import WorkloadIdentityCredentials


def fetch_entra_token_via_federation() -> str:
    federated_token = Path(os.environ["AZURE_FEDERATED_TOKEN_FILE"]).read_text()
    response = httpx.post(
        f"https://login.microsoftonline.com/{os.environ['AZURE_TENANT_ID']}/oauth2/v2.0/token",
        data={
            "client_id": os.environ["AZURE_CLIENT_ID"],
            "grant_type": "client_credentials",
            "scope": "https://api.anthropic.com/.default",
            "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            "client_assertion": federated_token,
        },
    )
    response.raise_for_status()
    return response.json()["access_token"]


client = anthropic.Anthropic(
    credentials=WorkloadIdentityCredentials(
        identity_token_provider=fetch_entra_token_via_federation,
        federation_rule_id=os.environ["ANTHROPIC_FEDERATION_RULE_ID"],
        organization_id=os.environ["ANTHROPIC_ORGANIZATION_ID"],
        service_account_id=os.environ["ANTHROPIC_SERVICE_ACCOUNT_ID"],
    ),
)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello from Azure"}],
)
print(message.content[0].text)
```

```typescript TypeScript nocheck
import Anthropic from "@anthropic-ai/sdk";
import { oidcFederationProvider } from "@anthropic-ai/sdk/lib/credentials/oidc-federation";
import { readFile } from "node:fs/promises";

async function fetchEntraTokenViaFederation(): Promise<string> {
  const federatedToken = await readFile(process.env.AZURE_FEDERATED_TOKEN_FILE!, "utf8");
  const response = await fetch(
    `https://login.microsoftonline.com/${process.env.AZURE_TENANT_ID}/oauth2/v2.0/token`,
    {
      method: "POST",
      headers: { "content-type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({
        client_id: process.env.AZURE_CLIENT_ID!,
        grant_type: "client_credentials",
        scope: "https://api.anthropic.com/.default",
        client_assertion_type: "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        client_assertion: federatedToken
      })
    }
  );
  const body = (await response.json()) as { access_token: string };
  return body.access_token;
}

const client = new Anthropic({
  credentials: oidcFederationProvider({
    identityTokenProvider: fetchEntraTokenViaFederation,
    federationRuleId: process.env.ANTHROPIC_FEDERATION_RULE_ID!,
    organizationId: process.env.ANTHROPIC_ORGANIZATION_ID!,
    serviceAccountId: process.env.ANTHROPIC_SERVICE_ACCOUNT_ID,
    baseURL: "https://api.anthropic.com",
    fetch
  })
});

const message = await client.messages.create({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello from Azure" }]
});
for (const block of message.content) {
  if (block.type === "text") {
    console.log(block.text);
  }
}
```

```go Go nocheck
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"net/url"
	"os"
	"strings"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func fetchEntraTokenViaFederation(ctx context.Context) (string, error) {
	federatedToken, err := os.ReadFile(os.Getenv("AZURE_FEDERATED_TOKEN_FILE"))
	if err != nil {
		return "", err
	}
	form := url.Values{
		"client_id":             {os.Getenv("AZURE_CLIENT_ID")},
		"grant_type":            {"client_credentials"},
		"scope":                 {"https://api.anthropic.com/.default"},
		"client_assertion_type": {"urn:ietf:params:oauth:client-assertion-type:jwt-bearer"},
		"client_assertion":      {strings.TrimSpace(string(federatedToken))},
	}
	tokenURL := "https://login.microsoftonline.com/" + os.Getenv("AZURE_TENANT_ID") + "/oauth2/v2.0/token"
	req, err := http.NewRequestWithContext(ctx, http.MethodPost, tokenURL, strings.NewReader(form.Encode()))
	if err != nil {
		return "", err
	}
	req.Header.Set("content-type", "application/x-www-form-urlencoded")
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()
	var body struct {
		AccessToken string `json:"access_token"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&body); err != nil {
		return "", err
	}
	return body.AccessToken, nil
}

func main() {
	client := anthropic.NewClient(
		option.WithFederationTokenProvider(option.IdentityTokenFunc(fetchEntraTokenViaFederation), option.FederationOptions{
			FederationRuleID: os.Getenv("ANTHROPIC_FEDERATION_RULE_ID"),
			OrganizationID:   os.Getenv("ANTHROPIC_ORGANIZATION_ID"),
			ServiceAccountID: os.Getenv("ANTHROPIC_SERVICE_ACCOUNT_ID"),
		}),
	)
	message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeSonnet4_6,
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("Hello from Azure")),
		},
	})
	if err != nil {
		panic(err)
	}
	fmt.Println(message.Content[0].Text)
}
```

```java Java nocheck hidelines={1..18,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.credentials.IdentityTokenProvider;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;
import java.util.stream.Collectors;
import static java.nio.charset.StandardCharsets.UTF_8;

void main() {
    IdentityTokenProvider fetchEntraTokenViaFederation = () -> {
        try {
            var form = Map.of(
                            "client_id", System.getenv("AZURE_CLIENT_ID"),
                            "grant_type", "client_credentials",
                            "scope", "https://api.anthropic.com/.default",
                            "client_assertion_type", "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
                            "client_assertion", Files.readString(Path.of(System.getenv("AZURE_FEDERATED_TOKEN_FILE"))))
                    .entrySet().stream()
                    .map(entry -> entry.getKey() + "=" + URLEncoder.encode(entry.getValue(), UTF_8))
                    .collect(Collectors.joining("&"));
            var request = HttpRequest.newBuilder(URI.create(
                            "https://login.microsoftonline.com/" + System.getenv("AZURE_TENANT_ID") + "/oauth2/v2.0/token"))
                    .header("content-type", "application/x-www-form-urlencoded")
                    .POST(HttpRequest.BodyPublishers.ofString(form))
                    .build();
            var response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
            return new ObjectMapper().readTree(response.body()).get("access_token").asText();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    };

    AnthropicClient client = AnthropicOkHttpClient.builder()
            .federationTokenProvider(
                    fetchEntraTokenViaFederation,
                    System.getenv("ANTHROPIC_FEDERATION_RULE_ID"),
                    System.getenv("ANTHROPIC_ORGANIZATION_ID"),
                    System.getenv("ANTHROPIC_SERVICE_ACCOUNT_ID"))
            .build();

    var message = client.messages().create(MessageCreateParams.builder()
            .model(Model.CLAUDE_SONNET_4_6)
            .maxTokens(1024)
            .addUserMessage("Hello from Azure")
            .build());

    IO.println(message.content());
}
```

```csharp C# nocheck hidelines={1..4}
using System.Text.Json;
using Anthropic.Models.Messages;
using Anthropic.Oidc;

var credentials = new WorkloadIdentityCredentials(new WorkloadIdentityOptions
{
    FederationRuleId = Environment.GetEnvironmentVariable("ANTHROPIC_FEDERATION_RULE_ID")!,
    OrganizationId = Environment.GetEnvironmentVariable("ANTHROPIC_ORGANIZATION_ID"),
    ServiceAccountId = Environment.GetEnvironmentVariable("ANTHROPIC_SERVICE_ACCOUNT_ID"),
    IdentityTokenProvider = new EntraFederationTokenProvider(),
});
using var client = new AnthropicOidcClient(credentials);

var message = await client.Messages.Create(new()
{
    Model = Model.ClaudeSonnet4_6,
    MaxTokens = 1024,
    Messages = [new() { Role = Role.User, Content = "Hello from Azure" }],
});
foreach (var block in message.Content)
{
    if (block.Value is TextBlock textBlock)
    {
        Console.WriteLine(textBlock.Text);
    }
}

class EntraFederationTokenProvider : IIdentityTokenProvider
{
    private static readonly HttpClient Http = new();

    public async Task<string> GetIdentityTokenAsync(CancellationToken ct = default)
    {
        var federatedToken = await File.ReadAllTextAsync(
            Environment.GetEnvironmentVariable("AZURE_FEDERATED_TOKEN_FILE")!, ct);
        var tenantId = Environment.GetEnvironmentVariable("AZURE_TENANT_ID");
        var form = new FormUrlEncodedContent(new Dictionary<string, string>
        {
            ["client_id"] = Environment.GetEnvironmentVariable("AZURE_CLIENT_ID")!,
            ["grant_type"] = "client_credentials",
            ["scope"] = "https://api.anthropic.com/.default",
            ["client_assertion_type"] = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            ["client_assertion"] = federatedToken,
        });
        var response = await Http.PostAsync(
            $"https://login.microsoftonline.com/{tenantId}/oauth2/v2.0/token", form, ct);
        response.EnsureSuccessStatusCode();
        using var json = await JsonDocument.ParseAsync(
            await response.Content.ReadAsStreamAsync(ct), default, ct);
        return json.RootElement.GetProperty("access_token").GetString()!;
    }
}
```

```php PHP nocheck hidelines={1..3}
<?php
require 'vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Credentials\WorkloadIdentityCredentials;

function fetchEntraTokenViaFederation(): string
{
    $ch = curl_init('https://login.microsoftonline.com/' . getenv('AZURE_TENANT_ID') . '/oauth2/v2.0/token');
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POSTFIELDS => http_build_query([
            'client_id' => getenv('AZURE_CLIENT_ID'),
            'grant_type' => 'client_credentials',
            'scope' => 'https://api.anthropic.com/.default',
            'client_assertion_type' => 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
            'client_assertion' => file_get_contents(getenv('AZURE_FEDERATED_TOKEN_FILE')),
        ]),
    ]);
    $body = json_decode(curl_exec($ch), true);
    curl_close($ch);
    return $body['access_token'];
}

$client = new Client(
    credentials: new WorkloadIdentityCredentials(
        identityTokenProvider: fetchEntraTokenViaFederation(...),
        federationRuleId: getenv('ANTHROPIC_FEDERATION_RULE_ID'),
        organizationId: getenv('ANTHROPIC_ORGANIZATION_ID'),
        serviceAccountId: getenv('ANTHROPIC_SERVICE_ACCOUNT_ID'),
    ),
);

$message = $client->messages->create(
    model: 'claude-sonnet-4-6',
    maxTokens: 1024,
    messages: [['role' => 'user', 'content' => 'Hello from Azure']],
);
echo $message->content[0]->text, PHP_EOL;
```

```ruby Ruby nocheck
require "anthropic"
require "json"
require "net/http"

def fetch_entra_token_via_federation
  tenant_id = ENV.fetch("AZURE_TENANT_ID")
  federated_token = File.read(ENV.fetch("AZURE_FEDERATED_TOKEN_FILE"))
  response = Net::HTTP.post_form(
    URI("https://login.microsoftonline.com/#{tenant_id}/oauth2/v2.0/token"),
    "client_id" => ENV.fetch("AZURE_CLIENT_ID"),
    "grant_type" => "client_credentials",
    "scope" => "https://api.anthropic.com/.default",
    "client_assertion_type" => "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    "client_assertion" => federated_token
  )
  JSON.parse(response.body).fetch("access_token")
end

client = Anthropic::Client.new(
  credentials: Anthropic::WorkloadIdentityCredentials.new(
    identity_token_provider: -> { fetch_entra_token_via_federation },
    federation_rule_id: ENV.fetch("ANTHROPIC_FEDERATION_RULE_ID"),
    organization_id: ENV.fetch("ANTHROPIC_ORGANIZATION_ID"),
    service_account_id: ENV.fetch("ANTHROPIC_SERVICE_ACCOUNT_ID")
  )
)

message = client.messages.create(
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [{role: "user", content: "Hello from Azure"}]
)
puts message.content.first.text
```

```bash CLI nocheck
# 1. Exchange the Kubernetes-projected token for an Entra-issued access
# token and write it to a temp file the CLI can read.
ANTHROPIC_IDENTITY_TOKEN_FILE=$(mktemp)
curl -sS "https://login.microsoftonline.com/$AZURE_TENANT_ID/oauth2/v2.0/token" \
  -d client_id="$AZURE_CLIENT_ID" \
  -d grant_type=client_credentials \
  --data-urlencode scope=https://api.anthropic.com/.default \
  -d client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer \
  --data-urlencode client_assertion@"$AZURE_FEDERATED_TOKEN_FILE" \
  | jq -r .access_token > "$ANTHROPIC_IDENTITY_TOKEN_FILE"
export ANTHROPIC_IDENTITY_TOKEN_FILE

# 2. Call the Claude API. ANTHROPIC_FEDERATION_RULE_ID,
# ANTHROPIC_ORGANIZATION_ID, and ANTHROPIC_SERVICE_ACCOUNT_ID are read
# from the environment.
ant messages create \
  --model claude-sonnet-4-6 \
  --max-tokens 1024 \
  --message '{role: user, content: "Hello from Azure"}'
```

</CodeGroup>

Alternatively, register your AKS cluster's OIDC issuer with Anthropic directly and skip the Entra hop. See [Kubernetes](/docs/en/build-with-claude/wif-providers/kubernetes) for that pattern.

## Verify the setup

From your Azure resource, run the cURL exchange shown earlier and confirm that `POST /v1/oauth/token` returns a `200` with an `access_token` beginning with `sk-ant-oat01-` and an `expires_in` value in seconds. On `400 invalid_grant`, see [Troubleshoot a failed exchange](/docs/en/api/authentication/wif-reference#troubleshoot-a-failed-exchange); the most common Azure-side cause is a mismatch between the `issuer_url` you registered and the `iss` claim in your decoded token. They must match exactly. For managed-identity tokens the `iss` value is either `https://login.microsoftonline.com/<TENANT_ID>/v2.0` or `https://sts.windows.net/<TENANT_ID>/`.

## Scope your rule

<Warning>
  The `oid` claim is a managed identity's GUID and has no stable prefix. A
  `subject_prefix` with `*` matches arbitrary identities in the tenant, so any
  workload that holds a managed identity could obtain a federated Anthropic
  token.
</Warning>

Lock the rule's `match` block to the narrowest scope that fits your use case:

- **Match `oid` as an exact value:** Set `claims.oid` to the managed identity's full object ID and never use `subject_prefix` for Azure tokens.
- **Pin `tid` as defense in depth:** The issuer URL already pins your tenant, but adding `claims.tid` guards against configuration drift if the issuer record is later edited.
- **Pin the audience:** Set `audience` to `https://api.anthropic.com` so tokens minted for other resources are rejected.
- **Use a separate rule per managed identity:** Create one rule per identity rather than one rule that authorizes several, so you can revoke a single workload's access without affecting others.

## Next steps

- Review the full configuration model in [Workload Identity Federation](/docs/en/build-with-claude/workload-identity-federation).
- See the [provider guides](/docs/en/build-with-claude/workload-identity-federation#identity-providers) for AWS, Google Cloud, GitHub Actions, and Kubernetes.
- For environment variables, profile files, and credential precedence, see the [WIF reference](/docs/en/api/authentication/wif-reference).
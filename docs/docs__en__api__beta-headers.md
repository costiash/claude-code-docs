# Beta headers

Access experimental features before general availability with the `anthropic-beta` header or the SDKs' `betas` parameter.

---

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

<Info>
  Each [client SDK](/docs/en/cli-sdks-libraries/overview) exposes a `beta` namespace for calling the API with beta features enabled.
</Info>

## How to use beta headers

To access beta features, include the `anthropic-beta` header in your API requests:

```http
POST /v1/messages
x-api-key: YOUR_API_KEY
anthropic-version: 2023-06-01
anthropic-beta: BETA_FEATURE_NAME
content-type: application/json
```

Each feature's documentation states the exact beta name to send. The [API overview](/docs/en/api/overview) lists the APIs currently in beta.

The following examples show the same request with cURL, the `ant` CLI, and the SDKs. The SDKs take beta names in the `betas` parameter and send the `anthropic-beta` header for you:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-4-8",
      "max_tokens": 1024,
      "messages": [
        {"role": "user", "content": "Hello, Claude"}
      ]
    }'
  ```

  ```bash CLI
  ant beta:messages create \
    --beta files-api-2025-04-14 \
    --model claude-opus-4-8 \
    --max-tokens 1024 \
    --message '{role: user, content: "Hello, Claude"}'
  ```

  ```python Python
  client = Anthropic()

  response = client.beta.messages.create(
      model="claude-opus-4-8",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude"}],
      betas=["files-api-2025-04-14"],
  )

  print(response.content)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const msg = await client.beta.messages.create({
    model: "claude-opus-4-8",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    betas: ["files-api-2025-04-14"]
  });

  console.log(msg.content);
  ```

  ```csharp C#
  var client = new AnthropicClient();

  var message = await client.Beta.Messages.Create(
      new MessageCreateParams
      {
          Model = "claude-opus-4-8",
          MaxTokens = 1024,
          Messages = [new() { Role = Role.User, Content = "Hello, Claude" }],
          Betas = ["files-api-2025-04-14"],
      }
  );

  Console.WriteLine(string.Join("\n", message.Content));
  ```

  ```go Go
  client := anthropic.NewClient()

  message, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
  	Model:     anthropic.ModelClaudeOpus4_8,
  	MaxTokens: 1024,
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hello, Claude")),
  	},
  	Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
  })
  if err != nil {
  	panic(err)
  }

  fmt.Printf("%+v\n", message.Content)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  MessageCreateParams params = MessageCreateParams.builder()
    .model(Model.CLAUDE_OPUS_4_8)
    .maxTokens(1024)
    .addUserMessage("Hello, Claude")
    .addBeta(AnthropicBeta.FILES_API_2025_04_14)
    .build();

  BetaMessage message = client.beta().messages().create(params);
  System.out.println(message.content());
  ```

  ```php PHP
  $client = new Client();

  $message = $client->beta->messages->create(
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      model: 'claude-opus-4-8',
      betas: ['files-api-2025-04-14'],
  );

  echo $message;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.beta.messages.create(
    model: "claude-opus-4-8",
    max_tokens: 1024,
    messages: [{role: "user", content: "Hello, Claude"}],
    betas: ["files-api-2025-04-14"]
  )

  puts(message.content)
  ```
</CodeGroup>

<Warning>
  Beta features are experimental and may:

  * Have breaking changes with notice
  * Be deprecated or removed
  * Have different rate limits or pricing
  * Not be available in all regions
</Warning>

### Multiple beta features

To use multiple beta features in a single request, include all feature names in the header separated by commas:

```http
anthropic-beta: feature1,feature2,feature3
```

When using an SDK, list each feature in the `betas` parameter (for example, `betas=["feature1", "feature2"]`). With the CLI, pass a single `--beta` flag with the feature names separated by commas (for example, `--beta feature1,feature2`). Avoid repeating the flag: currently only the first flag's value takes effect.

### Endpoint-specific headers

Some beta APIs are scoped to specific endpoints and require a feature-specific beta header on every request:

| Endpoints                                        | Beta header                 |
| ------------------------------------------------ | --------------------------- |
| `/v1/agents`, `/v1/sessions`, `/v1/environments` | `managed-agents-2026-04-01` |
| `/v1/tunnels`                                    | `mcp-tunnels-2026-06-22`    |
| `/v1/memory_stores` and sub-resources            | `agent-memory-2026-07-22`   |

The SDKs' `beta` namespaces add these headers automatically. Add them yourself only when making raw HTTP requests. See the [Managed Agents overview](/docs/en/managed-agents/overview), [Using agent memory](/docs/en/managed-agents/memory), and the [MCP tunnels reference](/docs/en/agents-and-tools/mcp-tunnels/reference#tunnels-api) for details.

Endpoint-specific headers that apply to the same endpoint aren't always combinable. On memory store endpoints, `agent-memory-2026-07-22` replaces `managed-agents-2026-04-01`: sending both on the same request returns a `400` error. The client SDKs send the correct header for each endpoint automatically.

### Version naming conventions

Beta feature names typically follow the pattern `feature-name-YYYY-MM-DD`, where the date indicates when the beta was released. Always use the exact beta feature name as documented.

## Error handling

If you use an invalid beta name, or a beta your organization doesn't have access to, you'll receive a `400` error response:

```json Output
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Unexpected value(s) `invalid-beta-name` for the `anthropic-beta` header. Please consult our documentation at platform.claude.com/docs or try again without the header."
  },
  "request_id": "req_011CcnGfC9fELffo2EALu4Wd"
}
```

## Getting help

For updates to beta features, see the [release notes](/docs/en/release-notes/overview). For help with production issues, contact [support](https://support.claude.com/).

## Next steps

<CardGroup cols={2}>
  <Card title="Errors" icon="info" href="/docs/en/api/errors">
    Understand the HTTP status codes, error response shape, and request IDs the Claude API returns, and handle errors with the SDKs' typed exceptions.
  </Card>

  <Card title="API overview" icon="compass" href="/docs/en/api/overview">
    Explore the Claude API's features, including the APIs currently in beta.
  </Card>
</CardGroup>

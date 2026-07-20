# Service tiers

Different tiers of service allow you to balance availability, performance, and predictable costs based on your application's needs.

---

<Warning>
  Priority Tier capacity commitments are no longer available for purchase. Organizations with an existing commitment can continue to use Priority Tier through their contract end date, and this page remains available as a reference for them. If you need guaranteed capacity, [contact sales](https://claude.com/contact-sales).
</Warning>

Anthropic offers three service tiers:

* **Priority Tier:** Available only to organizations with an existing capacity commitment
* **Standard:** Default tier for both piloting and scaling everyday use cases
* **Batch:** Best for asynchronous workflows that can wait or benefit from being outside your normal capacity

## Standard Tier

The standard tier is the default service tier for all API requests. The API prioritizes these requests alongside all other requests with best-effort availability.

## Priority Tier

The API prioritizes requests in this tier over all other requests. This prioritization helps minimize ["server overloaded" errors](/docs/en/api/errors#http-errors), even during peak times.

For more information, see [Existing Priority Tier commitments](#existing-priority-tier-commitments).

## How requests get assigned tiers

When handling a request, Anthropic decides to assign a request to Priority Tier in the following scenarios:

* Your organization has sufficient Priority Tier capacity **input** tokens per minute
* Your organization has sufficient Priority Tier capacity **output** tokens per minute

Anthropic counts usage against Priority Tier capacity as follows:

**Input tokens**

* Cache reads as 0.1 tokens per token read from the cache
* Cache writes as 1.25 tokens per token written to the cache with a 5 minute TTL
* Cache writes as 2.00 tokens per token written to the cache with a 1 hour TTL
* For [US-only inference](/docs/en/manage-claude/data-residency) (`inference_geo: "us"`) requests on Claude Opus 4.6, Claude Sonnet 4.6, and later models, input tokens are 1.1 tokens per token
* All other input tokens are 1 token per token

**Output tokens**

* For [US-only inference](/docs/en/manage-claude/data-residency) (`inference_geo: "us"`) requests on Claude Opus 4.6, Claude Sonnet 4.6, and later models, output tokens are 1.1 tokens per token
* All other output tokens are 1 token per token

Otherwise, requests proceed at standard tier.

<Note>
  These burndown rates reflect the relative pricing of each token type. For example, US-only inference is priced at 1.1x on Opus 4.6, Sonnet 4.6, and later models, so each token consumed with `inference_geo: "us"` draws down 1.1 tokens from your Priority Tier capacity.
</Note>

<Note>
  Requests assigned Priority Tier pull from both the Priority Tier capacity and the regular rate limits. If servicing the request would exceed the rate limits, the request is declined.
</Note>

## Using service tiers

You can control which service tiers can be used for a request by setting the `service_tier` parameter:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-4-8",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Hello, Claude!"}],
      "service_tier": "auto"
    }'
  ```

  ```bash CLI
  ant messages create \
    --transform usage.service_tier \
    --raw-output <<'YAML'
  model: claude-opus-4-8
  max_tokens: 1024
  messages:
    - role: user
      content: Hello, Claude!
  service_tier: auto  # Automatically use Priority Tier when available, fallback to standard
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  message = client.messages.create(
      model="claude-opus-4-8",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude!"}],
      service_tier="auto",  # Automatically use Priority Tier when available, fallback to standard
  )
  print(message.usage.service_tier)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const message = await client.messages.create({
    model: "claude-opus-4-8",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude!" }],
    service_tier: "auto" // Automatically use Priority Tier when available, fallback to standard
  });
  console.log(message.usage.service_tier);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var message = await client.Messages.Create(new MessageCreateParams
  {
      Model = Model.ClaudeOpus4_8,
      MaxTokens = 1024,
      Messages = [new() { Role = Role.User, Content = "Hello, Claude!" }],
      ServiceTier = ServiceTier.Auto, // Automatically use Priority Tier when available, fallback to standard
  });
  Console.WriteLine(message.Usage.ServiceTier);
  ```

  ```go Go
  client := anthropic.NewClient()

  message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus4_8,
  	MaxTokens: 1024,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude!")),
  	},
  	// Automatically use Priority Tier when available, fallback to standard
  	ServiceTier: anthropic.MessageNewParamsServiceTierAuto,
  })
  if err != nil {
  	log.Fatal(err)
  }
  fmt.Println(message.Usage.ServiceTier)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  MessageCreateParams params = MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_4_8)
      .maxTokens(1024L)
      .addUserMessage("Hello, Claude!")
      // Automatically use Priority Tier when available, fallback to standard
      .serviceTier(MessageCreateParams.ServiceTier.AUTO)
      .build();

  Message message = client.messages().create(params);
  IO.println(message.usage().serviceTier().orElseThrow());
  ```

  ```php PHP
  $client = new Client();

  $message = $client->messages->create(
      model: 'claude-opus-4-8',
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude!']],
      serviceTier: 'auto', // Automatically use Priority Tier when available, fallback to standard
  );
  echo $message->usage->serviceTier;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.messages.create(
    model: "claude-opus-4-8",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude!" }],
    service_tier: :auto # Automatically use Priority Tier when available, fallback to standard
  )
  puts(message.usage.service_tier)
  ```
</CodeGroup>

The `service_tier` parameter accepts the following values:

* `"auto"` (default) - Uses the Priority Tier capacity if available, falling back to your other capacity if not
* `"standard_only"` - Only use standard tier capacity, useful if you don't want to use your Priority Tier capacity

The response `usage` object also includes the service tier assigned to the request:

```json
{
  "usage": {
    "input_tokens": 410,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "output_tokens": 585,
    "service_tier": "priority"
  }
}
```

This allows you to determine which service tier was assigned to the request.

When requesting `service_tier="auto"` with a model with a Priority Tier commitment, these response headers provide insights:

```text wrap
anthropic-priority-input-tokens-limit: 10000
anthropic-priority-input-tokens-remaining: 9618
anthropic-priority-input-tokens-reset: 2025-01-12T23:11:59Z
anthropic-priority-output-tokens-limit: 10000
anthropic-priority-output-tokens-remaining: 6000
anthropic-priority-output-tokens-reset: 2025-01-12T23:12:21Z
```

You can use the presence of these headers to detect if your request was eligible for Priority Tier, even if it was over the limit.

## Existing Priority Tier commitments

A Priority Tier commitment consists of:

* A number of input tokens per minute
* A number of output tokens per minute
* A commitment duration (1, 3, 6, or 12 months)
* A specific model version

Priority Tier targets 99.5% uptime with prioritized computational resources. Requests beyond your committed capacity automatically fall back to standard tier.

### Supported models

Priority Tier is supported on all available Claude models (including Claude Fable 5 and Claude Opus 4.8) except Claude Sonnet 5, [Claude Mythos Preview](https://anthropic.com/glasswing), and Claude Mythos 5.

Check the [Models overview](/docs/en/about-claude/models/overview) for more details on available models.

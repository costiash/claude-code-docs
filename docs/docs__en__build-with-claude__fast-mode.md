# Fast mode (research preview)

Higher output speed for Claude Opus 4.6, delivering significantly faster token generation for latency-sensitive and agentic workflows.

---

Fast mode provides significantly faster output token generation for Claude Opus 4.6. By setting `speed: "fast"` in your API request, you get up to 2.5x higher output tokens per second from the same model at premium pricing.

<Note>
Fast mode is in research preview. [Join the waitlist](https://claude.com/fast-mode) to request access. Availability is limited while Anthropic gathers feedback.
</Note>

<Note>
This feature is eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/zero-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
</Note>

## Supported models

Fast mode is supported on the following models:

- Claude Opus 4.6 (`claude-opus-4-6`)

## How fast mode works

Fast mode runs the same model with a faster inference configuration. There is no change to intelligence or capabilities.

- Up to 2.5x higher output tokens per second compared to standard speed
- Speed benefits are focused on output tokens per second (OTPS), not time to first token (TTFT)
- Same model weights and behavior (not a different model)

## Basic usage

<CodeGroup>
```bash Shell
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: fast-mode-2026-02-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-6",
        "max_tokens": 4096,
        "speed": "fast",
        "messages": [{
            "role": "user",
            "content": "Refactor this module to use dependency injection"
        }]
    }'
```

```python Python nocheck
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[
        {"role": "user", "content": "Refactor this module to use dependency injection"}
    ],
)

print(response.content[0].text)
```

```typescript TypeScript hidelines={1..4}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const response = await client.beta.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 4096,
  speed: "fast",
  betas: ["fast-mode-2026-02-01"],
  messages: [
    {
      role: "user",
      content: "Refactor this module to use dependency injection"
    }
  ]
});

const textBlock = response.content.find(
  (block): block is Anthropic.Beta.Messages.BetaTextBlock => block.type === "text"
);
console.log(textBlock?.text);
```

```csharp C# hidelines={1..5}
using Anthropic;
using Anthropic.Models.Beta.Messages;

AnthropicClient client = new();

var response = await client.Beta.Messages.Create(new MessageCreateParams
{
    Model = "claude-opus-4-6",
    MaxTokens = 4096,
    Speed = Speed.Fast,
    Betas = ["fast-mode-2026-02-01"],
    Messages = [
        new() { Role = Role.User, Content = "Refactor this module to use dependency injection" }
    ],
});

Console.WriteLine(response);
```

```go Go hidelines={1..13,-1}
package main

import (
	"context"
	"fmt"
	"log"

	anthropic "github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 4096,
		Speed:     anthropic.BetaMessageNewParamsSpeedFast,
		Betas:     []anthropic.AnthropicBeta{anthropic.AnthropicBetaFastMode2026_02_01},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Refactor this module to use dependency injection")),
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response.Content[0].AsText().Text)
}
```

```java Java hidelines={1..10,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.AnthropicBeta;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

public class FastModeExample {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaMessage response = client.beta().messages().create(
                MessageCreateParams.builder()
                        .model(Model.CLAUDE_OPUS_4_6)
                        .maxTokens(4096L)
                        .speed(MessageCreateParams.Speed.FAST)
                        .addBeta(AnthropicBeta.FAST_MODE_2026_02_01)
                        .addUserMessage("Refactor this module to use dependency injection")
                        .build());

        System.out.println(response.content().get(0).text().get().text());
    }
}
```

```php PHP hidelines={1..6}
<?php

use Anthropic\Client;

$client = new Client();

$response = $client->beta->messages->create(
    model: 'claude-opus-4-6',
    maxTokens: 4096,
    speed: 'fast',
    betas: ['fast-mode-2026-02-01'],
    messages: [
        ['role' => 'user', 'content' => 'Refactor this module to use dependency injection'],
    ],
);

echo $response->content[0]->text;
```

```ruby Ruby
require "anthropic"

client = Anthropic::Client.new

response = client.beta.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 4096,
  speed: "fast",
  betas: ["fast-mode-2026-02-01"],
  messages: [{role: "user", content: "Refactor this module to use dependency injection"}]
)

puts response.content[0].text
```

</CodeGroup>

## Pricing

Fast mode is priced at 6x standard Opus rates across the full context window. The following table shows pricing for Claude Opus 4.6 with fast mode:

| Input | Output |
|:------|:-------|
| $30 / MTok | $150 / MTok |

Fast mode pricing stacks with other pricing modifiers:

- [Prompt caching multipliers](/docs/en/about-claude/pricing#model-pricing) apply on top of fast mode pricing
- [Data residency](/docs/en/build-with-claude/data-residency) multipliers apply on top of fast mode pricing

For complete pricing details, see the [pricing page](/docs/en/about-claude/pricing#fast-mode-pricing).

## Rate limits

Fast mode has a dedicated rate limit that is separate from standard Opus rate limits. Unlike standard speed, which has separate limits for ≤200K and >200K input tokens, fast mode uses a single rate limit that covers the full context range. When your fast mode rate limit is exceeded, the API returns a `429` error with a `retry-after` header indicating when capacity will be available.

The response includes headers that indicate your fast mode rate limit status:

| Header | Description |
|:-------|:------------|
| `anthropic-fast-input-tokens-limit` | Maximum fast mode input tokens per minute |
| `anthropic-fast-input-tokens-remaining` | Remaining fast mode input tokens |
| `anthropic-fast-input-tokens-reset` | Time when the fast mode input token limit resets |
| `anthropic-fast-output-tokens-limit` | Maximum fast mode output tokens per minute |
| `anthropic-fast-output-tokens-remaining` | Remaining fast mode output tokens |
| `anthropic-fast-output-tokens-reset` | Time when the fast mode output token limit resets |

For tier-specific rate limits, see the [rate limits page](/docs/en/api/rate-limits).

## Checking which speed was used

The response `usage` object includes a `speed` field that indicates which speed was used, either `"fast"` or `"standard"`:

<CodeGroup>
```bash Shell
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: fast-mode-2026-02-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-6",
        "max_tokens": 1024,
        "speed": "fast",
        "messages": [{"role": "user", "content": "Hello"}]
    }'

{
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  ...
  "usage": {
    "input_tokens": 523,
    "output_tokens": 1842,
    "speed": "fast"
  }
}
```

```python Python nocheck
response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[{"role": "user", "content": "Hello"}],
)

print(response.usage.speed)  # "fast" or "standard"
```

```typescript TypeScript
const response = await client.beta.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  speed: "fast",
  betas: ["fast-mode-2026-02-01"],
  messages: [{ role: "user", content: "Hello" }]
});

console.log(response.usage.speed); // "fast" or "standard"
```

```csharp C# hidelines={1..5}
using Anthropic;
using Anthropic.Models.Beta.Messages;

AnthropicClient client = new();

var response = await client.Beta.Messages.Create(new MessageCreateParams
{
    Model = "claude-opus-4-6",
    MaxTokens = 1024,
    Speed = Speed.Fast,
    Betas = ["fast-mode-2026-02-01"],
    Messages = [new() { Role = Role.User, Content = "Hello" }],
});

Console.WriteLine(response.Usage.Speed);  // "fast" or "standard"
```

```go Go hidelines={1..13,-1}
package main

import (
	"context"
	"fmt"
	"log"

	anthropic "github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 1024,
		Speed:     anthropic.BetaMessageNewParamsSpeedFast,
		Betas:     []anthropic.AnthropicBeta{anthropic.AnthropicBetaFastMode2026_02_01},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hello")),
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response.Usage.Speed) // "fast" or "standard"
}
```

```java Java hidelines={1..10,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.AnthropicBeta;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

public class FastModeUsage {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
                .model(Model.CLAUDE_OPUS_4_6)
                .maxTokens(1024L)
                .speed(MessageCreateParams.Speed.FAST)
                .addBeta(AnthropicBeta.FAST_MODE_2026_02_01)
                .addUserMessage("Hello")
                .build();

        BetaMessage response = client.beta().messages().create(params);
        System.out.println(response.usage().speed());  // "fast" or "standard"
    }
}
```

```php PHP hidelines={1..6}
<?php

use Anthropic\Client;

$client = new Client();

$response = $client->beta->messages->create(
    model: 'claude-opus-4-6',
    maxTokens: 1024,
    speed: 'fast',
    betas: ['fast-mode-2026-02-01'],
    messages: [['role' => 'user', 'content' => 'Hello']],
);

echo $response->usage->speed;  // "fast" or "standard"
```

```ruby Ruby nocheck
response = anthropic.beta.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 1024,
  speed: "fast",
  betas: ["fast-mode-2026-02-01"],
  messages: [{ role: "user", content: "Hello" }]
)

puts(response.usage.speed)  # "fast" or "standard"
```
</CodeGroup>

To track fast mode usage and costs across your organization, see the [Usage and Cost API](/docs/en/build-with-claude/usage-cost-api).

## Retries and fallback

### Automatic retries

When fast mode rate limits are exceeded, the API returns a `429` error with a `retry-after` header. The Anthropic SDKs automatically retry these requests up to 2 times by default (configurable via `max_retries`), waiting for the server-specified delay before each retry. Since fast mode uses continuous token replenishment, the `retry-after` delay is typically short and requests succeed once capacity is available.

### Falling back to standard speed

If you'd prefer to fall back to standard speed rather than wait for fast mode capacity, catch the rate limit error and retry without `speed: "fast"`. Set `max_retries` to `0` on the initial fast request to skip automatic retries and fail immediately on rate limit errors.

<Note>
Falling back from fast to standard speed will result in a [prompt cache](/docs/en/build-with-claude/prompt-caching) miss. Requests at different speeds do not share cached prefixes.
</Note>

Since setting `max_retries` to `0` also disables retries for other transient errors (overloaded, internal server errors), the examples below re-issue the original request with default retries for those cases.

<CodeGroup>

```python Python nocheck hidelines={1..4}
import anthropic

client = anthropic.Anthropic()


def create_message_with_fast_fallback(max_retries=None, max_attempts=3, **params):
    try:
        return client.beta.messages.create(**params, max_retries=max_retries)
    except anthropic.RateLimitError:
        if params.get("speed") == "fast":
            del params["speed"]
            return create_message_with_fast_fallback(**params)
        raise
    except (
        anthropic.InternalServerError,
        anthropic.OverloadedError,
        anthropic.APIConnectionError,
    ):
        if max_attempts > 1:
            return create_message_with_fast_fallback(
                max_attempts=max_attempts - 1, **params
            )
        raise


message = create_message_with_fast_fallback(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    betas=["fast-mode-2026-02-01"],
    speed="fast",
    max_retries=0,
)
```

```typescript TypeScript hidelines={1..3,-1}
import Anthropic from "@anthropic-ai/sdk";
const client = new Anthropic();
(async () => {
  async function createMessageWithFastFallback(
    params: Anthropic.Beta.MessageCreateParams,
    requestOptions?: Anthropic.RequestOptions,
    maxAttempts: number = 3
  ): Promise<Anthropic.Beta.Messages.BetaMessage> {
    try {
      return (await client.beta.messages.create(
        params,
        requestOptions
      )) as Anthropic.Beta.Messages.BetaMessage;
    } catch (e) {
      if (e instanceof Anthropic.RateLimitError && params.speed === "fast") {
        const { speed, ...rest } = params;
        return createMessageWithFastFallback(rest);
      }
      if (
        e instanceof Anthropic.InternalServerError ||
        e instanceof Anthropic.APIConnectionError
      ) {
        if (maxAttempts > 1) {
          return createMessageWithFastFallback(params, undefined, maxAttempts - 1);
        }
      }
      throw e;
    }
  }

  const message = await createMessageWithFastFallback(
    {
      model: "claude-opus-4-6",
      max_tokens: 1024,
      messages: [{ role: "user", content: "Hello" }],
      betas: ["fast-mode-2026-02-01"],
      speed: "fast"
    },
    { maxRetries: 0 }
  );
})();
```

```csharp C# hidelines={1..5}
using Anthropic;
using Anthropic.Models.Beta.Messages;

AnthropicClient client = new();

async Task<BetaMessage> CreateMessageWithFastFallback(
    MessageCreateParams parameters,
    int? maxRetries = null,
    int maxAttempts = 3)
{
    try
    {
        var requestClient = maxRetries is int retries
            ? client.WithOptions(o => o with { MaxRetries = retries })
            : client;
        return await requestClient.Beta.Messages.Create(parameters);
    }
    catch (AnthropicRateLimitException)
    {
        if (parameters.Speed is not null)
        {
            return await CreateMessageWithFastFallback(
                parameters with { Speed = null });
        }
        throw;
    }
    catch (Anthropic5xxException)
    {
        if (maxAttempts > 1)
        {
            return await CreateMessageWithFastFallback(
                parameters, maxAttempts: maxAttempts - 1);
        }
        throw;
    }
}

var message = await CreateMessageWithFastFallback(
    new MessageCreateParams
    {
        Model = "claude-opus-4-6",
        MaxTokens = 1024,
        Messages = [new() { Role = Role.User, Content = "Hello" }],
        Betas = ["fast-mode-2026-02-01"],
        Speed = Speed.Fast,
    },
    maxRetries: 0);
```

```go Go hidelines={1..11}
package main

import (
	"context"
	"errors"
	"fmt"

	anthropic "github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func createMessageWithFastFallback(
	ctx context.Context,
	client *anthropic.Client,
	params anthropic.BetaMessageNewParams,
	maxAttempts int,
	opts ...option.RequestOption,
) (*anthropic.BetaMessage, error) {
	message, err := client.Beta.Messages.New(ctx, params, opts...)
	if err != nil {
		var apierr *anthropic.Error
		if errors.As(err, &apierr) && apierr.StatusCode == 429 && params.Speed != "" {
			params.Speed = ""
			return createMessageWithFastFallback(ctx, client, params, maxAttempts)
		}
		if (errors.As(err, &apierr) && apierr.StatusCode >= 500) || !errors.As(err, &apierr) {
			if maxAttempts > 1 {
				return createMessageWithFastFallback(ctx, client, params, maxAttempts-1)
			}
		}
		return nil, err
	}
	return message, nil
}

func main() {
	client := anthropic.NewClient()
	message, err := createMessageWithFastFallback(
		context.TODO(),
		&client,
		anthropic.BetaMessageNewParams{
			Model:     anthropic.ModelClaudeOpus4_6,
			MaxTokens: 1024,
			Messages: []anthropic.BetaMessageParam{
				anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hello")),
			},
			Speed: "fast",
			Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaFastMode2026_02_01},
		},
		3,
		option.WithMaxRetries(0),
	)
	if err != nil {
		panic(err)
	}
	fmt.Println(message)
}
```

```java Java hidelines={1..11,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.RequestOptions;
import com.anthropic.errors.InternalServerException;
import com.anthropic.errors.RateLimitException;
import com.anthropic.models.beta.AnthropicBeta;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

public class FastModeFallback {
    static AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    static BetaMessage createMessageWithFastFallback(
            MessageCreateParams params,
            RequestOptions requestOptions,
            int maxAttempts) {
        try {
            return client.beta().messages().create(params, requestOptions);
        } catch (RateLimitException e) {
            if (params.speed().isPresent()) {
                MessageCreateParams retryParams = params.toBuilder()
                        .speed(null)
                        .build();
                return createMessageWithFastFallback(
                        retryParams, RequestOptions.none(), maxAttempts);
            }
            throw e;
        } catch (InternalServerException e) {
            if (maxAttempts > 1) {
                return createMessageWithFastFallback(
                        params, RequestOptions.none(), maxAttempts - 1);
            }
            throw e;
        }
    }

    public static void main(String[] args) {
        BetaMessage message = createMessageWithFastFallback(
                MessageCreateParams.builder()
                        .model(Model.CLAUDE_OPUS_4_6)
                        .maxTokens(1024L)
                        .addUserMessage("Hello")
                        .addBeta(AnthropicBeta.FAST_MODE_2026_02_01)
                        .speed(MessageCreateParams.Speed.FAST)
                        .build(),
                RequestOptions.builder().maxRetries(0).build(),
                3);
    }
}
```

```php PHP hidelines={1..10}
<?php

use Anthropic\Client;
use Anthropic\Core\Exceptions\APIConnectionException;
use Anthropic\Core\Exceptions\InternalServerException;
use Anthropic\Core\Exceptions\RateLimitException;
use Anthropic\RequestOptions;

$client = new Client();

function createMessageWithFastFallback(
    Client $client,
    array $params,
    ?RequestOptions $requestOptions = null,
    int $maxAttempts = 3,
) {
    try {
        return $client->beta->messages->create(
            ...$params,
            requestOptions: $requestOptions,
        );
    } catch (RateLimitException $e) {
        if (isset($params['speed'])) {
            unset($params['speed']);
            return createMessageWithFastFallback($client, $params);
        }
        throw $e;
    } catch (InternalServerException | APIConnectionException $e) {
        if ($maxAttempts > 1) {
            return createMessageWithFastFallback(
                $client, $params, maxAttempts: $maxAttempts - 1
            );
        }
        throw $e;
    }
}

$message = createMessageWithFastFallback(
    $client,
    [
        'model' => 'claude-opus-4-6',
        'maxTokens' => 1024,
        'messages' => [['role' => 'user', 'content' => 'Hello']],
        'betas' => ['fast-mode-2026-02-01'],
        'speed' => 'fast',
    ],
    RequestOptions::with(maxRetries: 0),
);
```

```ruby Ruby nocheck
require "anthropic"

anthropic = Anthropic::Client.new

def create_message_with_fast_fallback(client, request_options: {}, max_attempts: 3, **params)
  client.beta.messages.create(**params, request_options: request_options)
rescue Anthropic::Errors::RateLimitError
  raise unless params[:speed] == "fast"
  params.delete(:speed)
  create_message_with_fast_fallback(client, **params)
rescue Anthropic::Errors::InternalServerError, Anthropic::Errors::APIConnectionError
  raise unless max_attempts > 1
  create_message_with_fast_fallback(client, max_attempts: max_attempts - 1, **params)
end

message = create_message_with_fast_fallback(
  anthropic,
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello" }],
  betas: ["fast-mode-2026-02-01"],
  speed: "fast",
  request_options: { max_retries: 0 }
)
```
</CodeGroup>

## Considerations

- **Prompt caching:** Switching between fast and standard speed invalidates the prompt cache. Requests at different speeds do not share cached prefixes.
- **Supported models:** Fast mode is currently supported on Opus 4.6 only. Sending `speed: "fast"` with an unsupported model returns an error.
- **TTFT:** Fast mode's benefits are focused on output tokens per second (OTPS), not time to first token (TTFT).
- **Batch API:** Fast mode is not available with the [Batch API](/docs/en/build-with-claude/batch-processing).
- **Priority Tier:** Fast mode is not available with [Priority Tier](/docs/en/api/service-tiers).

## Next steps

<CardGroup>
  <Card title="Pricing" icon="dollar-sign" href="/docs/en/about-claude/pricing#fast-mode-pricing">
    View detailed fast mode pricing information.
  </Card>
  <Card title="Rate limits" icon="gauge" href="/docs/en/api/rate-limits">
    Check rate limit tiers for fast mode.
  </Card>
  <Card title="Effort parameter" icon="sliders" href="/docs/en/build-with-claude/effort">
    Control token usage with the effort parameter.
  </Card>
</CardGroup>
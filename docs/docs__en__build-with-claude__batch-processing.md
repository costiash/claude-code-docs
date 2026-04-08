# Batch processing

---

Batch processing is a powerful approach for handling large volumes of requests efficiently. Instead of processing requests one at a time with immediate responses, batch processing allows you to submit multiple requests together for asynchronous processing. This pattern is particularly useful when:

- You need to process large volumes of data
- Immediate responses are not required
- You want to optimize for cost efficiency
- You're running large-scale evaluations or analyses

The Message Batches API is Anthropic's first implementation of this pattern.

<Note>
This feature is **not** eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). Data is retained according to the feature's standard retention policy.
</Note>

---

# Message Batches API

The Message Batches API is a powerful, cost-effective way to asynchronously process large volumes of [Messages](/docs/en/api/messages/create) requests. This approach is well-suited to tasks that do not require immediate responses, with most batches finishing in less than 1 hour while reducing costs by 50% and increasing throughput.

You can [explore the API reference directly](/docs/en/api/creating-message-batches), in addition to this guide.

## How the Message Batches API works

When you send a request to the Message Batches API:

1. The system creates a new Message Batch with the provided Messages requests.
2. The batch is then processed asynchronously, with each request handled independently.
3. You can poll for the status of the batch and retrieve results when processing has ended for all requests.

This is especially useful for bulk operations that don't require immediate results, such as:
- Large-scale evaluations: Process thousands of test cases efficiently.
- Content moderation: Analyze large volumes of user-generated content asynchronously.
- Data analysis: Generate insights or summaries for large datasets.
- Bulk content generation: Create large amounts of text for various purposes (e.g., product descriptions, article summaries).

### Batch limitations
- A Message Batch is limited to either 100,000 Message requests or 256 MB in size, whichever is reached first.
- The system processes each batch as fast as possible, with most batches completing within 1 hour. You can access batch results when all messages have completed or after 24 hours, whichever comes first. Batches expire if processing does not complete within 24 hours.
- Batch results are available for 29 days after creation. After that, you may still view the Batch, but its results will no longer be available for download.
- Batches are scoped to a [Workspace](/settings/workspaces). You may view all batches (and their results) that were created within the Workspace that your API key belongs to.
- Rate limits apply to both Batches API HTTP requests and the number of requests within a batch waiting to be processed. See [Message Batches API rate limits](/docs/en/api/rate-limits#message-batches-api). Additionally, processing may be slowed down based on current demand and your request volume. In that case, you may see more requests expiring after 24 hours.
- Due to high throughput and concurrent processing, batches may go slightly over your Workspace's configured [spend limit](/settings/limits).

### Supported models

All [active models](/docs/en/about-claude/models/overview) support the Message Batches API.

### What can be batched
Any request that you can make to the Messages API can be included in a batch. This includes:

- Vision
- Tool use
- System messages
- Multi-turn conversations
- Any beta features

Since each request in the batch is processed independently, you can mix different types of requests within a single batch.

<Tip>
Since batches can take longer than 5 minutes to process, consider using the [1-hour cache duration](/docs/en/build-with-claude/prompt-caching#1-hour-cache-duration) with prompt caching for better cache hit rates when processing batches with shared context.
</Tip>

---
## Pricing

The Batches API offers significant cost savings. All usage is charged at 50% of the standard API prices.

| Model             | Batch input      | Batch output    |
|-------------------|------------------|-----------------|
| Claude Opus 4.6       | $2.50 / MTok     | $12.50 / MTok   |
| Claude Opus 4.5     | $2.50 / MTok     | $12.50 / MTok   |
| Claude Opus 4.1     | $7.50 / MTok     | $37.50 / MTok   |
| Claude Opus 4     | $7.50 / MTok     | $37.50 / MTok   |
| Claude Sonnet 4.6   | $1.50 / MTok     | $7.50 / MTok    |
| Claude Sonnet 4.5   | $1.50 / MTok     | $7.50 / MTok    |
| Claude Sonnet 4   | $1.50 / MTok     | $7.50 / MTok    |
| Claude Sonnet 3.7 ([deprecated](/docs/en/about-claude/model-deprecations)) | $1.50 / MTok     | $7.50 / MTok    |
| Claude Haiku 4.5  | $0.50 / MTok     | $2.50 / MTok    |
| Claude Haiku 3.5  | $0.40 / MTok     | $2 / MTok       |
| Claude Opus 3 ([deprecated](/docs/en/about-claude/model-deprecations))  | $7.50 / MTok     | $37.50 / MTok   |
| Claude Haiku 3    | $0.125 / MTok    | $0.625 / MTok   |

---
## How to use the Message Batches API

### Prepare and create your batch

A Message Batch is composed of a list of requests to create a Message. The shape of an individual request is comprised of:
- A unique `custom_id` for identifying the Messages request
- A `params` object with the standard [Messages API](/docs/en/api/messages/create) parameters

You can [create a batch](/docs/en/api/creating-message-batches) by passing this list into the `requests` parameter:

<CodeGroup>

```bash Shell
curl https://api.anthropic.com/v1/messages/batches \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
'{
    "requests": [
        {
            "custom_id": "my-first-request",
            "params": {
                "model": "claude-opus-4-6",
                "max_tokens": 1024,
                "messages": [
                    {"role": "user", "content": "Hello, world"}
                ]
            }
        },
        {
            "custom_id": "my-second-request",
            "params": {
                "model": "claude-opus-4-6",
                "max_tokens": 1024,
                "messages": [
                    {"role": "user", "content": "Hi again, friend"}
                ]
            }
        }
    ]
}'
```

```bash CLI
ant messages:batches create <<'YAML'
requests:
  - custom_id: my-first-request
    params:
      model: claude-opus-4-6
      max_tokens: 1024
      messages:
        - role: user
          content: Hello, world
  - custom_id: my-second-request
    params:
      model: claude-opus-4-6
      max_tokens: 1024
      messages:
        - role: user
          content: Hi again, friend
YAML
```

```python Python hidelines={1}
import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

client = anthropic.Anthropic()

message_batch = client.messages.batches.create(
    requests=[
        Request(
            custom_id="my-first-request",
            params=MessageCreateParamsNonStreaming(
                model="claude-opus-4-6",
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": "Hello, world",
                    }
                ],
            ),
        ),
        Request(
            custom_id="my-second-request",
            params=MessageCreateParamsNonStreaming(
                model="claude-opus-4-6",
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": "Hi again, friend",
                    }
                ],
            ),
        ),
    ]
)

print(message_batch)
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

const messageBatch = await anthropic.messages.batches.create({
  requests: [
    {
      custom_id: "my-first-request",
      params: {
        model: "claude-opus-4-6",
        max_tokens: 1024,
        messages: [{ role: "user", content: "Hello, world" }]
      }
    },
    {
      custom_id: "my-second-request",
      params: {
        model: "claude-opus-4-6",
        max_tokens: 1024,
        messages: [{ role: "user", content: "Hi again, friend" }]
      }
    }
  ]
});

console.log(messageBatch);
```

```csharp C#
using Anthropic;
using Anthropic.Models.Messages;
using Anthropic.Models.Messages.Batches;

AnthropicClient client = new();

var batch = await client.Messages.Batches.Create(new BatchCreateParams
{
    Requests =
    [
        new()
        {
            CustomID = "my-first-request",
            Params = new()
            {
                Model = Model.ClaudeOpus4_6,
                MaxTokens = 1024,
                Messages =
                [
                    new() { Role = Role.User, Content = "Hello, world" }
                ]
            }
        },
        new()
        {
            CustomID = "my-second-request",
            Params = new()
            {
                Model = Model.ClaudeOpus4_6,
                MaxTokens = 1024,
                Messages =
                [
                    new() { Role = Role.User, Content = "Hi again, friend" }
                ]
            }
        }
    ]
});

Console.WriteLine(batch);
```

```go Go hidelines={1..10,-1}
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	batch, _ := client.Messages.Batches.New(context.Background(),
		anthropic.MessageBatchNewParams{
			Requests: []anthropic.MessageBatchNewParamsRequest{
				{
					CustomID: "my-first-request",
					Params: anthropic.MessageBatchNewParamsRequestParams{
						Model:     anthropic.ModelClaudeOpus4_6,
						MaxTokens: 1024,
						Messages: []anthropic.MessageParam{
							anthropic.NewUserMessage(
								anthropic.NewTextBlock("Hello, world"),
							),
						},
					},
				},
				{
					CustomID: "my-second-request",
					Params: anthropic.MessageBatchNewParamsRequestParams{
						Model:     anthropic.ModelClaudeOpus4_6,
						MaxTokens: 1024,
						Messages: []anthropic.MessageParam{
							anthropic.NewUserMessage(
								anthropic.NewTextBlock("Hi again, friend"),
							),
						},
					},
				},
			},
		})

	fmt.Println(batch.ID)
}
```

```java Java hidelines={1..3,5..8,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.batches.*;

public class BatchExample {

  public static void main(String[] args) {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    BatchCreateParams params = BatchCreateParams.builder()
      .addRequest(
        BatchCreateParams.Request.builder()
          .customId("my-first-request")
          .params(
            BatchCreateParams.Request.Params.builder()
              .model(Model.CLAUDE_OPUS_4_6)
              .maxTokens(1024)
              .addUserMessage("Hello, world")
              .build()
          )
          .build()
      )
      .addRequest(
        BatchCreateParams.Request.builder()
          .customId("my-second-request")
          .params(
            BatchCreateParams.Request.Params.builder()
              .model(Model.CLAUDE_OPUS_4_6)
              .maxTokens(1024)
              .addUserMessage("Hi again, friend")
              .build()
          )
          .build()
      )
      .build();

    MessageBatch messageBatch = client.messages().batches().create(params);

    System.out.println(messageBatch);
  }
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(
    apiKey: getenv("ANTHROPIC_API_KEY")
);

$batch = $client->messages->batches->create(
    requests: [
        [
            'custom_id' => 'my-first-request',
            'params' => [
                'model' => 'claude-opus-4-6',
                'max_tokens' => 1024,
                'messages' => [
                    ['role' => 'user', 'content' => 'Hello, world']
                ]
            ]
        ],
        [
            'custom_id' => 'my-second-request',
            'params' => [
                'model' => 'claude-opus-4-6',
                'max_tokens' => 1024,
                'messages' => [
                    ['role' => 'user', 'content' => 'Hi again, friend']
                ]
            ]
        ]
    ],
);

print_r($batch);
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

batch = client.messages.batches.create(
  requests: [
    {
      custom_id: "my-first-request",
      params: {
        model: "claude-opus-4-6",
        max_tokens: 1024,
        messages: [
          { role: "user", content: "Hello, world" }
        ]
      }
    },
    {
      custom_id: "my-second-request",
      params: {
        model: "claude-opus-4-6",
        max_tokens: 1024,
        messages: [
          { role: "user", content: "Hi again, friend" }
        ]
      }
    }
  ]
)

puts batch
```

</CodeGroup>

In this example, two separate requests are batched together for asynchronous processing. Each request has a unique `custom_id` and contains the standard parameters you'd use for a Messages API call.

<Tip>
  **Test your batch requests with the Messages API**

Validation of the `params` object for each message request is performed asynchronously, and validation errors are returned when processing of the entire batch has ended. You can ensure that you are building your input correctly by verifying your request shape with the [Messages API](/docs/en/api/messages/create) first.
</Tip>

When a batch is first created, the response will have a processing status of `in_progress`.

```json Output
{
  "id": "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d",
  "type": "message_batch",
  "processing_status": "in_progress",
  "request_counts": {
    "processing": 2,
    "succeeded": 0,
    "errored": 0,
    "canceled": 0,
    "expired": 0
  },
  "ended_at": null,
  "created_at": "2024-09-24T18:37:24.100435Z",
  "expires_at": "2024-09-25T18:37:24.100435Z",
  "cancel_initiated_at": null,
  "results_url": null
}
```

### Tracking your batch

The Message Batch's `processing_status` field indicates the stage of processing the batch is in. It starts as `in_progress`, then updates to `ended` once all the requests in the batch have finished processing, and results are ready. You can monitor the state of your batch by visiting the [Console](/settings/workspaces/default/batches), or using the [retrieval endpoint](/docs/en/api/retrieving-message-batches).

#### Polling for Message Batch completion

To poll a Message Batch, you'll need its `id`, which is provided in the response when creating a batch or by listing batches. You can implement a polling loop that checks the batch status periodically until processing has ended:

<CodeGroup>
```bash Shell hidelines={2..16,23}
#!/bin/sh
MESSAGE_BATCH_ID=$(curl -s https://api.anthropic.com/v1/messages/batches \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --header "content-type: application/json" \
  --data '{
    "requests": [{
      "custom_id": "test-1",
      "params": {
        "model": "claude-opus-4-6",
        "max_tokens": 100,
        "messages": [{"role": "user", "content": "Hi"}]
      }
    }]
  }' | jq -r '.id')

until [[ $(curl -s "https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID" \
          --header "x-api-key: $ANTHROPIC_API_KEY" \
          --header "anthropic-version: 2023-06-01" \
          | grep -o '"processing_status":[[:space:]]*"[^"]*"' \
          | cut -d'"' -f4) == "ended" ]]; do
    echo "Batch $MESSAGE_BATCH_ID is still processing..."
    break
    sleep 60
done

echo "Batch $MESSAGE_BATCH_ID has finished processing"
```

```bash CLI hidelines={2..14,19}
#!/bin/bash
MESSAGE_BATCH_ID=$(ant messages:batches create \
  --transform id --format yaml <<'YAML'
requests:
  - custom_id: test-1
    params:
      model: claude-opus-4-6
      max_tokens: 100
      messages:
        - role: user
          content: Hi
YAML
)

until [[ $(ant messages:batches retrieve \
          --message-batch-id "$MESSAGE_BATCH_ID" \
          --transform processing_status --format yaml) == "ended" ]]; do
    echo "Batch $MESSAGE_BATCH_ID is still processing..."
    break
    sleep 60
done

echo "Batch $MESSAGE_BATCH_ID has finished processing"
```

```python Python nocheck hidelines={1}
import anthropic
import time

client = anthropic.Anthropic()

MESSAGE_BATCH_ID = "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d"

message_batch = None
while True:
    message_batch = client.messages.batches.retrieve(MESSAGE_BATCH_ID)
    if message_batch.processing_status == "ended":
        break

    print(f"Batch {MESSAGE_BATCH_ID} is still processing...")
    time.sleep(60)
print(message_batch)
```

```typescript TypeScript nocheck hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

const messageBatchId = "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d";

let messageBatch;
while (true) {
  messageBatch = await anthropic.messages.batches.retrieve(messageBatchId);
  if (messageBatch.processing_status === "ended") {
    break;
  }

  console.log(`Batch ${messageBatchId} is still processing... waiting`);
  await new Promise((resolve) => setTimeout(resolve, 60_000));
}
console.log(messageBatch);
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Messages.Batches;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();
        string messageBatchId = Environment.GetEnvironmentVariable("MESSAGE_BATCH_ID");

        MessageBatch messageBatch = null;
        while (true)
        {
            messageBatch = await client.Messages.Batches.Retrieve(messageBatchId);
            if (messageBatch.ProcessingStatus == "ended")
            {
                break;
            }

            Console.WriteLine($"Batch {messageBatchId} is still processing...");
            await Task.Delay(60000);
        }
        Console.WriteLine(messageBatch);
    }
}
```

```go Go nocheck hidelines={1..14,-1}
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"time"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()
	messageBatchID := os.Getenv("MESSAGE_BATCH_ID")

	var messageBatch *anthropic.MessageBatch
	for {
		var err error
		messageBatch, err = client.Messages.Batches.Get(context.TODO(), messageBatchID)
		if err != nil {
			log.Fatal(err)
		}
		if messageBatch.ProcessingStatus == "ended" {
			break
		}

		fmt.Printf("Batch %s is still processing...\n", messageBatchID)
		time.Sleep(60 * time.Second)
	}
	fmt.Println(messageBatch)
}
```

```java Java nocheck hidelines={1..2,4..6,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.MessageBatch;

public class MessageBatchPolling {
    public static void main(String[] args) throws InterruptedException {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();
        String messageBatchId = "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d";

        MessageBatch messageBatch = null;
        while (true) {
            messageBatch = client.messages().batches().retrieve(messageBatchId);
            if (messageBatch.processingStatus().equals(MessageBatch.ProcessingStatus.ENDED)) {
                break;
            }

            System.out.println("Batch " + messageBatchId + " is still processing...");
            Thread.sleep(60000);
        }
        System.out.println(messageBatch);
    }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));
$messageBatchId = getenv("MESSAGE_BATCH_ID");

$messageBatch = null;
while (true) {
    $messageBatch = $client->messages->batches->retrieve(
        messageBatchID: $messageBatchId,
    );
    if ($messageBatch->processingStatus === "ended") {
        break;
    }

    echo "Batch {$messageBatchId} is still processing...\n";
    sleep(60);
}
echo json_encode($messageBatch, JSON_PRETTY_PRINT);
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

message_batch_id = ENV["MESSAGE_BATCH_ID"]
message_batch = nil
loop do
  message_batch = client.messages.batches.retrieve(message_batch_id)
  break if message_batch.processing_status == :ended

  puts "Batch #{message_batch_id} is still processing..."
  sleep 60
end
puts message_batch
```

</CodeGroup>

### Listing all Message Batches

You can list all Message Batches in your Workspace using the [list endpoint](/docs/en/api/listing-message-batches). The API supports pagination, automatically fetching additional pages as needed:

<CodeGroup>
```bash Shell
#!/bin/sh

if ! command -v jq &> /dev/null; then
    echo "Error: This script requires jq. Please install it first."
    exit 1
fi

BASE_URL="https://api.anthropic.com/v1/messages/batches"

has_more=true
after_id=""

while [ "$has_more" = true ]; do
    # Construct URL with after_id if it exists
    if [ -n "$after_id" ]; then
        url="${BASE_URL}?limit=20&after_id=${after_id}"
    else
        url="$BASE_URL?limit=20"
    fi

    response=$(curl -s "$url" \
              --header "x-api-key: $ANTHROPIC_API_KEY" \
              --header "anthropic-version: 2023-06-01")

    # Extract values using jq
    has_more=$(echo "$response" | jq -r '.has_more')
    after_id=$(echo "$response" | jq -r '.last_id')

    # Process and print each entry in the data array
    echo "$response" | jq -c '.data[]' | while read -r entry; do
        echo "$entry" | jq '.'
    done
done
```

```bash CLI
# Automatically fetches more pages as needed
ant messages:batches list --limit 20
```

```python Python hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

# Automatically fetches more pages as needed.
for message_batch in client.messages.batches.list(limit=20):
    print(message_batch)
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

// Automatically fetches more pages as needed.
for await (const messageBatch of anthropic.messages.batches.list({
  limit: 20
})) {
  console.log(messageBatch);
}
```

```csharp C# hidelines={1..11,-2..}
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Messages.Batches;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var parameters = new BatchListParams
        {
            Limit = 20
        };

        // Automatically fetches more pages as needed
        var page = await client.Messages.Batches.List(parameters);
        await foreach (var messageBatch in page.Paginate())
        {
            Console.WriteLine(messageBatch);
        }
    }
}
```

```go Go hidelines={1..11,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	// Automatically fetches more pages as needed
	iter := client.Messages.Batches.ListAutoPaging(context.TODO(), anthropic.MessageBatchListParams{
		Limit: anthropic.Int(20),
	})

	for iter.Next() {
		messageBatch := iter.Current()
		fmt.Println(messageBatch)
	}

	if err := iter.Err(); err != nil {
		log.Fatal(err)
	}
}
```

```java Java hidelines={1..2,4..7,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.*;

public class BatchListExample {

  public static void main(String[] args) {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    // Automatically fetches more pages as needed
    for (MessageBatch messageBatch : client
      .messages()
      .batches()
      .list(BatchListParams.builder().limit(20).build())
      .autoPager()) {
      System.out.println(messageBatch);
    }
  }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

// Automatically fetches more pages as needed
foreach ($client->messages->batches->list(limit: 20)->pagingEachItem() as $messageBatch) {
    echo $messageBatch->id . "\n";
}
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

# Automatically fetches more pages as needed
client.messages.batches.list(limit: 20).auto_paging_each do |message_batch|
  puts message_batch
end
```

</CodeGroup>

### Retrieving batch results

Once batch processing has ended, each Messages request in the batch has a result. There are 4 result types:

| Result Type | Description |
|-------------|-------------|
| `succeeded` | Request was successful. Includes the message result. |
| `errored`   | Request encountered an error and a message was not created. Possible errors include invalid requests and internal server errors. You will not be billed for these requests. |
| `canceled`  | User canceled the batch before this request could be sent to the model. You will not be billed for these requests. |
| `expired`   | Batch reached its 24 hour expiration before this request could be sent to the model. You will not be billed for these requests. |

You will see an overview of your results with the batch's `request_counts`, which shows how many requests reached each of these four states.

Results of the batch are available for download at the `results_url` property on the Message Batch, and if the organization permission allows, in the Console. Because of the potentially large size of the results, it's recommended to [stream results](/docs/en/api/retrieving-message-batch-results) back rather than download them all at once.

<CodeGroup>

```bash Shell
#!/bin/sh
curl "https://api.anthropic.com/v1/messages/batches/msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  | grep -o '"results_url":[[:space:]]*"[^"]*"' \
  | cut -d'"' -f4 \
  | while read -r url; do
    curl -s "$url" \
      --header "anthropic-version: 2023-06-01" \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      | sed 's/}{/}\n{/g' \
      | while IFS= read -r line
    do
      result_type=$(echo "$line" | sed -n 's/.*"result":[[:space:]]*{[[:space:]]*"type":[[:space:]]*"\([^"]*\)".*/\1/p')
      custom_id=$(echo "$line" | sed -n 's/.*"custom_id":[[:space:]]*"\([^"]*\)".*/\1/p')
      error_type=$(echo "$line" | sed -n 's/.*"error":[[:space:]]*{[[:space:]]*"type":[[:space:]]*"\([^"]*\)".*/\1/p')

      case "$result_type" in
        "succeeded")
          echo "Success! $custom_id"
          ;;
        "errored")
          if [ "$error_type" = "invalid_request_error" ]; then
            # Request body must be fixed before re-sending request
            echo "Validation error: $custom_id"
          else
            # Request can be retried directly
            echo "Server error: $custom_id"
          fi
          ;;
        "expired")
          echo "Expired: $line"
          ;;
      esac
    done
  done

```

```bash CLI
ant messages:batches results \
  --message-batch-id msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d \
  --transform '{custom_id,"type":result.type,"error":result.error.error.type}' \
  --format jsonl \
  | while IFS= read -r line; do
    custom_id=${line#*'"custom_id":"'}; custom_id=${custom_id%%'"'*}
    case "$line" in
      *'"type":"succeeded"'*)
        printf 'Success! %s\n' "$custom_id" ;;
      *'"type":"errored"'*)
        case "$line" in
          *'"error":"invalid_request_error"'*)
            printf 'Validation error %s\n' "$custom_id" ;;
          *)
            printf 'Server error %s\n' "$custom_id" ;;
        esac ;;
      *'"type":"expired"'*)
        printf 'Request expired %s\n' "$custom_id" ;;
    esac
  done
```

```python Python nocheck hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

# Stream results file in memory-efficient chunks, processing one at a time
for result in client.messages.batches.results(
    "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d",
):
    match result.result.type:
        case "succeeded":
            print(f"Success! {result.custom_id}")
        case "errored":
            if result.result.error.error.type == "invalid_request_error":
                # Request body must be fixed before re-sending request
                print(f"Validation error {result.custom_id}")
            else:
                # Request can be retried directly
                print(f"Server error {result.custom_id}")
        case "expired":
            print(f"Request expired {result.custom_id}")
```

```typescript TypeScript nocheck hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

// Stream results file in memory-efficient chunks, processing one at a time
for await (const result of await anthropic.messages.batches.results(
  "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d"
)) {
  switch (result.result.type) {
    case "succeeded":
      console.log(`Success! ${result.custom_id}`);
      break;
    case "errored":
      if (result.result.error.type === "invalid_request_error") {
        // Request body must be fixed before re-sending request
        console.log(`Validation error: ${result.custom_id}`);
      } else {
        // Request can be retried directly
        console.log(`Server error: ${result.custom_id}`);
      }
      break;
    case "expired":
      console.log(`Request expired: ${result.custom_id}`);
      break;
  }
}
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Messages.Batches;

public class Program
{
    public static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        await foreach (var result in client.Messages.Batches.ResultsStreaming("msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d"))
        {
            switch (result.Result.Type)
            {
                case "succeeded":
                    Console.WriteLine($"Success! {result.CustomID}");
                    break;
                case "errored":
                    if (result.Result.Error?.Type == "invalid_request")
                    {
                        Console.WriteLine($"Validation error: {result.CustomID}");
                    }
                    else
                    {
                        Console.WriteLine($"Server error: {result.CustomID}");
                    }
                    break;
                case "expired":
                    Console.WriteLine($"Request expired: {result.CustomID}");
                    break;
            }
        }
    }
}
```

```go Go nocheck hidelines={1..11,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	stream := client.Messages.Batches.ResultsStreaming(context.TODO(), "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d")

	for stream.Next() {
		result := stream.Current()

		switch variant := result.Result.AsAny().(type) {
		case anthropic.MessageBatchSucceededResult:
			fmt.Printf("Success! %s\n", result.CustomID)
		case anthropic.MessageBatchErroredResult:
			fmt.Printf("Error: %s - %s\n", result.CustomID, variant.Error.Error.Message)
		case anthropic.MessageBatchExpiredResult:
			fmt.Printf("Request expired: %s\n", result.CustomID)
		}
	}

	if err := stream.Err(); err != nil {
		log.Fatal(err)
	}
}
```

```java Java nocheck hidelines={1..2,6..9,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.messages.batches.BatchResultsParams;
import com.anthropic.models.messages.batches.MessageBatchIndividualResponse;

public class BatchResultsExample {

  public static void main(String[] args) {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    // Stream results file in memory-efficient chunks, processing one at a time
    try (
      StreamResponse<MessageBatchIndividualResponse> streamResponse = client
        .messages()
        .batches()
        .resultsStreaming(
          BatchResultsParams.builder()
            .messageBatchId("msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d")
            .build()
        )
    ) {
      streamResponse
        .stream()
        .forEach(result -> {
          if (result.result().isSucceeded()) {
            System.out.println("Success! " + result.customId());
          } else if (result.result().isErrored()) {
            if (result.result().asErrored().error().error().isInvalidRequestError()) {
              // Request body must be fixed before re-sending request
              System.out.println("Validation error: " + result.customId());
            } else {
              // Request can be retried directly
              System.out.println("Server error: " + result.customId());
            }
          } else if (result.result().isExpired()) {
            System.out.println("Request expired: " + result.customId());
          }
        });
    }
  }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

foreach ($client->messages->batches->resultsStream(messageBatchID: 'msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d') as $result) {
    switch ($result->result->type) {
        case "succeeded":
            echo "Success! {$result->customID}\n";
            break;
        case "errored":
            if ($result->result->error->error->type === "invalid_request_error") {
                echo "Validation error: {$result->customID}\n";
            } else {
                echo "Server error: {$result->customID}\n";
            }
            break;
        case "expired":
            echo "Request expired: {$result->customID}\n";
            break;
    }
}
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

client.messages.batches.results_streaming("msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d").each do |result|
  case result.result.type
  when :succeeded
    puts "Success! #{result.custom_id}"
  when :errored
    if result.result.error.type == :invalid_request
      puts "Validation error: #{result.custom_id}"
    else
      puts "Server error: #{result.custom_id}"
    end
  when :expired
    puts "Request expired: #{result.custom_id}"
  end
end
```

</CodeGroup>

The results are in `.jsonl` format, where each line is a valid JSON object representing the result of a single request in the Message Batch. For each streamed result, you can do something different depending on its `custom_id` and result type. Here is an example set of results:

```jsonl .jsonl file
{"custom_id":"my-second-request","result":{"type":"succeeded","message":{"id":"msg_014VwiXbi91y3JMjcpyGBHX5","type":"message","role":"assistant","model":"claude-opus-4-6","content":[{"type":"text","text":"Hello again! It's nice to see you. How can I assist you today? Is there anything specific you'd like to chat about or any questions you have?"}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":11,"output_tokens":36}}}}
{"custom_id":"my-first-request","result":{"type":"succeeded","message":{"id":"msg_01FqfsLoHwgeFbguDgpz48m7","type":"message","role":"assistant","model":"claude-opus-4-6","content":[{"type":"text","text":"Hello! How can I assist you today? Feel free to ask me any questions or let me know if there's anything you'd like to chat about."}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":10,"output_tokens":34}}}}
```

If your result has an error, its `result.error` will be set to the standard [error shape](/docs/en/api/errors#error-shapes).

<Tip>
  **Batch results may not match input order**

Batch results can be returned in any order, and may not match the ordering of requests when the batch was created. In the above example, the result for the second batch request is returned before the first. To correctly match results with their corresponding requests, always use the `custom_id` field.
</Tip>

### Canceling a Message Batch

You can cancel a Message Batch that is currently processing using the [cancel endpoint](/docs/en/api/canceling-message-batches). Immediately after cancellation, a batch's `processing_status` will be `canceling`. You can use the same polling technique described above to wait until cancellation is finalized. Canceled batches end up with a status of `ended` and may contain partial results for requests that were processed before cancellation.

<CodeGroup>
```bash Shell hidelines={2..15}
#!/bin/sh
MESSAGE_BATCH_ID=$(curl -s https://api.anthropic.com/v1/messages/batches \
  --header "x-api-key: $ANTHROPIC_API_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --header "content-type: application/json" \
  --data '{
    "requests": [{
      "custom_id": "test-1",
      "params": {
        "model": "claude-opus-4-6",
        "max_tokens": 100,
        "messages": [{"role": "user", "content": "Hi"}]
      }
    }]
  }' | jq -r '.id')
curl --request POST https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID/cancel \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01"
```

```bash CLI hidelines={2..13}
#!/bin/bash
MESSAGE_BATCH_ID=$(ant messages:batches create \
  --transform id --format yaml <<'YAML'
requests:
  - custom_id: test-1
    params:
      model: claude-opus-4-6
      max_tokens: 100
      messages:
        - role: user
          content: Hi
YAML
)
ant messages:batches cancel --message-batch-id "$MESSAGE_BATCH_ID"
```

```python Python nocheck hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

MESSAGE_BATCH_ID = "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d"

message_batch = client.messages.batches.cancel(
    MESSAGE_BATCH_ID,
)
print(message_batch)
```

```typescript TypeScript nocheck hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

const messageBatch = await anthropic.messages.batches.cancel(MESSAGE_BATCH_ID);
console.log(messageBatch);
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Messages.Batches;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var messageBatch = await client.Messages.Batches.Cancel(MESSAGE_BATCH_ID);
        Console.WriteLine(messageBatch);
    }
}
```

```go Go nocheck hidelines={1..12,-1}
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()
	messageBatchID := os.Getenv("MESSAGE_BATCH_ID")

	messageBatch, err := client.Messages.Batches.Cancel(context.TODO(), messageBatchID)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(messageBatch)
}
```

```java Java nocheck hidelines={1..2,4..7,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.*;

public class BatchCancelExample {

  public static void main(String[] args) {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    MessageBatch messageBatch = client
      .messages()
      .batches()
      .cancel("msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d");
    System.out.println(messageBatch);
  }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$messageBatch = $client->messages->batches->cancel(
    messageBatchID: 'msgbatch_example_id',
);
echo $messageBatch;
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

message_batch_id = ENV.fetch("MESSAGE_BATCH_ID")
message_batch = client.messages.batches.cancel(message_batch_id)
puts message_batch
```

</CodeGroup>

The response will show the batch in a `canceling` state:

```json Output
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch",
  "processing_status": "canceling",
  "request_counts": {
    "processing": 2,
    "succeeded": 0,
    "errored": 0,
    "canceled": 0,
    "expired": 0
  },
  "ended_at": null,
  "created_at": "2024-09-24T18:37:24.100435Z",
  "expires_at": "2024-09-25T18:37:24.100435Z",
  "cancel_initiated_at": "2024-09-24T18:39:03.114875Z",
  "results_url": null
}
```

### Using prompt caching with Message Batches

The Message Batches API supports prompt caching, allowing you to potentially reduce costs and processing time for batch requests. The pricing discounts from prompt caching and Message Batches can stack, providing even greater cost savings when both features are used together. However, since batch requests are processed asynchronously and concurrently, cache hits are provided on a best-effort basis. Users typically experience cache hit rates ranging from 30% to 98%, depending on their traffic patterns.

To maximize the likelihood of cache hits in your batch requests:

1. Include identical `cache_control` blocks in every Message request within your batch
2. Maintain a steady stream of requests to prevent cache entries from expiring after their 5-minute lifetime
3. Structure your requests to share as much cached content as possible

Example of implementing prompt caching in a batch:

<CodeGroup>

```bash Shell
curl https://api.anthropic.com/v1/messages/batches \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
'{
    "requests": [
        {
            "custom_id": "my-first-request",
            "params": {
                "model": "claude-opus-4-6",
                "max_tokens": 1024,
                "system": [
                    {
                        "type": "text",
                        "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                    },
                    {
                        "type": "text",
                        "text": "<the entire contents of Pride and Prejudice>",
                        "cache_control": {"type": "ephemeral"}
                    }
                ],
                "messages": [
                    {"role": "user", "content": "Analyze the major themes in Pride and Prejudice."}
                ]
            }
        },
        {
            "custom_id": "my-second-request",
            "params": {
                "model": "claude-opus-4-6",
                "max_tokens": 1024,
                "system": [
                    {
                        "type": "text",
                        "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                    },
                    {
                        "type": "text",
                        "text": "<the entire contents of Pride and Prejudice>",
                        "cache_control": {"type": "ephemeral"}
                    }
                ],
                "messages": [
                    {"role": "user", "content": "Write a summary of Pride and Prejudice."}
                ]
            }
        }
    ]
}'
```

```bash CLI
ant messages:batches create <<'YAML'
requests:
  - custom_id: my-first-request
    params:
      model: claude-opus-4-6
      max_tokens: 1024
      system:
        - type: text
          text: >
            You are an AI assistant tasked with analyzing literary works. Your
            goal is to provide insightful commentary on themes, characters, and
            writing style.
        - type: text
          text: "<the entire contents of Pride and Prejudice>"
          cache_control:
            type: ephemeral
      messages:
        - role: user
          content: Analyze the major themes in Pride and Prejudice.
  - custom_id: my-second-request
    params:
      model: claude-opus-4-6
      max_tokens: 1024
      system:
        - type: text
          text: >
            You are an AI assistant tasked with analyzing literary works. Your
            goal is to provide insightful commentary on themes, characters, and
            writing style.
        - type: text
          text: "<the entire contents of Pride and Prejudice>"
          cache_control:
            type: ephemeral
      messages:
        - role: user
          content: Write a summary of Pride and Prejudice.
YAML
```

```python Python hidelines={1}
import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

client = anthropic.Anthropic()

message_batch = client.messages.batches.create(
    requests=[
        Request(
            custom_id="my-first-request",
            params=MessageCreateParamsNonStreaming(
                model="claude-opus-4-6",
                max_tokens=1024,
                system=[
                    {
                        "type": "text",
                        "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n",
                    },
                    {
                        "type": "text",
                        "text": "<the entire contents of Pride and Prejudice>",
                        "cache_control": {"type": "ephemeral"},
                    },
                ],
                messages=[
                    {
                        "role": "user",
                        "content": "Analyze the major themes in Pride and Prejudice.",
                    }
                ],
            ),
        ),
        Request(
            custom_id="my-second-request",
            params=MessageCreateParamsNonStreaming(
                model="claude-opus-4-6",
                max_tokens=1024,
                system=[
                    {
                        "type": "text",
                        "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n",
                    },
                    {
                        "type": "text",
                        "text": "<the entire contents of Pride and Prejudice>",
                        "cache_control": {"type": "ephemeral"},
                    },
                ],
                messages=[
                    {
                        "role": "user",
                        "content": "Write a summary of Pride and Prejudice.",
                    }
                ],
            ),
        ),
    ]
)
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

const messageBatch = await anthropic.messages.batches.create({
  requests: [
    {
      custom_id: "my-first-request",
      params: {
        model: "claude-opus-4-6",
        max_tokens: 1024,
        system: [
          {
            type: "text",
            text: "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
          },
          {
            type: "text",
            text: "<the entire contents of Pride and Prejudice>",
            cache_control: { type: "ephemeral" }
          }
        ],
        messages: [
          { role: "user", content: "Analyze the major themes in Pride and Prejudice." }
        ]
      }
    },
    {
      custom_id: "my-second-request",
      params: {
        model: "claude-opus-4-6",
        max_tokens: 1024,
        system: [
          {
            type: "text",
            text: "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
          },
          {
            type: "text",
            text: "<the entire contents of Pride and Prejudice>",
            cache_control: { type: "ephemeral" }
          }
        ],
        messages: [{ role: "user", content: "Write a summary of Pride and Prejudice." }]
      }
    }
  ]
});
```

```csharp C#
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Messages;
using Anthropic.Models.Messages.Batches;

public class Program
{
    public static async Task Main(string[] args)
    {
        AnthropicClient client = new()
        {
            ApiKey = Environment.GetEnvironmentVariable("ANTHROPIC_API_KEY")
        };

        var messageBatch = await client.Messages.Batches.Create(new BatchCreateParams
        {
            Requests =
            [
                new()
                {
                    CustomID = "my-first-request",
                    Params = new()
                    {
                        Model = Model.ClaudeOpus4_6,
                        MaxTokens = 1024,
                        System = new List<TextBlockParam>
                        {
                            new()
                            {
                                Text = "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                            },
                            new()
                            {
                                Text = "<the entire contents of Pride and Prejudice>",
                                CacheControl = new()
                            }
                        },
                        Messages =
                        [
                            new() { Role = Role.User, Content = "Analyze the major themes in Pride and Prejudice." }
                        ]
                    }
                },
                new()
                {
                    CustomID = "my-second-request",
                    Params = new()
                    {
                        Model = Model.ClaudeOpus4_6,
                        MaxTokens = 1024,
                        System = new List<TextBlockParam>
                        {
                            new()
                            {
                                Text = "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                            },
                            new()
                            {
                                Text = "<the entire contents of Pride and Prejudice>",
                                CacheControl = new()
                            }
                        },
                        Messages =
                        [
                            new() { Role = Role.User, Content = "Write a summary of Pride and Prejudice." }
                        ]
                    }
                }
            ]
        });
    }
}
```

```go Go hidelines={1..10,-1}
package main

import (
	"context"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	messageBatch, err := client.Messages.Batches.New(context.TODO(), anthropic.MessageBatchNewParams{
		Requests: []anthropic.MessageBatchNewParamsRequest{
			{
				CustomID: "my-first-request",
				Params: anthropic.MessageBatchNewParamsRequestParams{
					Model:     anthropic.ModelClaudeOpus4_6,
					MaxTokens: 1024,
					System: []anthropic.TextBlockParam{
						{
							Text: "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n",
						},
						{
							Text:         "<the entire contents of Pride and Prejudice>",
							CacheControl: anthropic.NewCacheControlEphemeralParam(),
						},
					},
					Messages: []anthropic.MessageParam{
						anthropic.NewUserMessage(anthropic.NewTextBlock("Analyze the major themes in Pride and Prejudice.")),
					},
				},
			},
			{
				CustomID: "my-second-request",
				Params: anthropic.MessageBatchNewParamsRequestParams{
					Model:     anthropic.ModelClaudeOpus4_6,
					MaxTokens: 1024,
					System: []anthropic.TextBlockParam{
						{
							Text: "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n",
						},
						{
							Text:         "<the entire contents of Pride and Prejudice>",
							CacheControl: anthropic.NewCacheControlEphemeralParam(),
						},
					},
					Messages: []anthropic.MessageParam{
						anthropic.NewUserMessage(anthropic.NewTextBlock("Write a summary of Pride and Prejudice.")),
					},
				},
			},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("%+v\n", messageBatch)
}
```

```java Java hidelines={1..2,4..5,7..11,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.CacheControlEphemeral;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.TextBlockParam;
import com.anthropic.models.messages.batches.*;
import java.util.List;

public class BatchExample {

  public static void main(String[] args) {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    BatchCreateParams createParams = BatchCreateParams.builder()
      .addRequest(
        BatchCreateParams.Request.builder()
          .customId("my-first-request")
          .params(
            BatchCreateParams.Request.Params.builder()
              .model(Model.CLAUDE_OPUS_4_6)
              .maxTokens(1024)
              .systemOfTextBlockParams(
                List.of(
                  TextBlockParam.builder()
                    .text(
                      "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                    )
                    .build(),
                  TextBlockParam.builder()
                    .text("<the entire contents of Pride and Prejudice>")
                    .cacheControl(CacheControlEphemeral.builder().build())
                    .build()
                )
              )
              .addUserMessage("Analyze the major themes in Pride and Prejudice.")
              .build()
          )
          .build()
      )
      .addRequest(
        BatchCreateParams.Request.builder()
          .customId("my-second-request")
          .params(
            BatchCreateParams.Request.Params.builder()
              .model(Model.CLAUDE_OPUS_4_6)
              .maxTokens(1024)
              .systemOfTextBlockParams(
                List.of(
                  TextBlockParam.builder()
                    .text(
                      "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
                    )
                    .build(),
                  TextBlockParam.builder()
                    .text("<the entire contents of Pride and Prejudice>")
                    .cacheControl(CacheControlEphemeral.builder().build())
                    .build()
                )
              )
              .addUserMessage("Write a summary of Pride and Prejudice.")
              .build()
          )
          .build()
      )
      .build();

    MessageBatch messageBatch = client.messages().batches().create(createParams);
  }
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$messageBatch = $client->messages->batches->create(
    requests: [
        [
            'custom_id' => 'my-first-request',
            'params' => [
                'model' => 'claude-opus-4-6',
                'max_tokens' => 1024,
                'system' => [
                    [
                        'type' => 'text',
                        'text' => 'You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n'
                    ],
                    [
                        'type' => 'text',
                        'text' => '<the entire contents of Pride and Prejudice>',
                        'cache_control' => ['type' => 'ephemeral']
                    ]
                ],
                'messages' => [
                    ['role' => 'user', 'content' => 'Analyze the major themes in Pride and Prejudice.']
                ]
            ]
        ],
        [
            'custom_id' => 'my-second-request',
            'params' => [
                'model' => 'claude-opus-4-6',
                'max_tokens' => 1024,
                'system' => [
                    [
                        'type' => 'text',
                        'text' => 'You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n'
                    ],
                    [
                        'type' => 'text',
                        'text' => '<the entire contents of Pride and Prejudice>',
                        'cache_control' => ['type' => 'ephemeral']
                    ]
                ],
                'messages' => [
                    ['role' => 'user', 'content' => 'Write a summary of Pride and Prejudice.']
                ]
            ]
        ]
    ],
);
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

message_batch = client.messages.batches.create(
  requests: [
    {
      custom_id: "my-first-request",
      params: {
        model: "claude-opus-4-6",
        max_tokens: 1024,
        system: [
          {
            type: "text",
            text: "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
          },
          {
            type: "text",
            text: "<the entire contents of Pride and Prejudice>",
            cache_control: { type: "ephemeral" }
          }
        ],
        messages: [
          { role: "user", content: "Analyze the major themes in Pride and Prejudice." }
        ]
      }
    },
    {
      custom_id: "my-second-request",
      params: {
        model: "claude-opus-4-6",
        max_tokens: 1024,
        system: [
          {
            type: "text",
            text: "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n"
          },
          {
            type: "text",
            text: "<the entire contents of Pride and Prejudice>",
            cache_control: { type: "ephemeral" }
          }
        ],
        messages: [
          { role: "user", content: "Write a summary of Pride and Prejudice." }
        ]
      }
    }
  ]
)
```

</CodeGroup>

In this example, both requests in the batch include identical system messages and the full text of Pride and Prejudice marked with `cache_control` to increase the likelihood of cache hits.

### Extended output (beta)

The `output-300k-2026-03-24` beta header raises the `max_tokens` cap to 300,000 for batch requests using Claude Opus 4.6 or Claude Sonnet 4.6. Include the header to generate outputs far longer than the standard limit (64k to 128k depending on model) in a single turn.

<Note>
Extended output is available on the Message Batches API only, not the synchronous Messages API. It is supported on the Claude API and is not available on Amazon Bedrock, Vertex AI, or Microsoft Foundry.
</Note>

Use extended output for long-form generation such as book-length drafts and technical documentation, exhaustive structured data extraction, large code-generation scaffolds, and long reasoning chains.

A single 300k-token generation can take over an hour to complete, so plan your batch submissions with the 24-hour processing window in mind. Standard batch pricing (50% of standard API prices) applies.

<CodeGroup>

```bash Shell
curl https://api.anthropic.com/v1/messages/batches \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "anthropic-beta: output-300k-2026-03-24" \
     --header "content-type: application/json" \
     --data \
'{
    "requests": [
        {
            "custom_id": "long-form-request",
            "params": {
                "model": "claude-opus-4-6",
                "max_tokens": 300000,
                "messages": [
                    {"role": "user", "content": "Write a comprehensive technical guide to building distributed systems, covering architecture patterns, consistency models, fault tolerance, and operational best practices."}
                ]
            }
        }
    ]
}'
```

```bash CLI
ant beta:messages:batches create --beta output-300k-2026-03-24 <<'YAML'
requests:
  - custom_id: long-form-request
    params:
      model: claude-opus-4-6
      max_tokens: 300000
      messages:
        - role: user
          content: >-
            Write a comprehensive technical guide to building distributed
            systems, covering architecture patterns, consistency models,
            fault tolerance, and operational best practices.
YAML
```

```python Python hidelines={1}
import anthropic
from anthropic.types.beta.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.beta.messages.batch_create_params import Request

client = anthropic.Anthropic()

message_batch = client.beta.messages.batches.create(
    betas=["output-300k-2026-03-24"],
    requests=[
        Request(
            custom_id="long-form-request",
            params=MessageCreateParamsNonStreaming(
                model="claude-opus-4-6",
                max_tokens=300_000,
                messages=[
                    {
                        "role": "user",
                        "content": "Write a comprehensive technical guide to building distributed systems, covering architecture patterns, consistency models, fault tolerance, and operational best practices.",
                    }
                ],
            ),
        ),
    ],
)

print(message_batch)
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

const messageBatch = await anthropic.beta.messages.batches.create({
  betas: ["output-300k-2026-03-24"],
  requests: [
    {
      custom_id: "long-form-request",
      params: {
        model: "claude-opus-4-6",
        max_tokens: 300000,
        messages: [
          {
            role: "user",
            content:
              "Write a comprehensive technical guide to building distributed systems, covering architecture patterns, consistency models, fault tolerance, and operational best practices."
          }
        ]
      }
    }
  ]
});

console.log(messageBatch);
```

```csharp C#
using Anthropic;
using Anthropic.Models.Beta.Messages;
using Anthropic.Models.Beta.Messages.Batches;

AnthropicClient client = new();

var batch = await client.Beta.Messages.Batches.Create(new BatchCreateParams
{
    Betas = ["output-300k-2026-03-24"],
    Requests =
    [
        new()
        {
            CustomID = "long-form-request",
            Params = new()
            {
                Model = "claude-opus-4-6",
                MaxTokens = 300_000,
                Messages =
                [
                    new() { Role = Role.User, Content = "Write a comprehensive technical guide to building distributed systems, covering architecture patterns, consistency models, fault tolerance, and operational best practices." }
                ]
            }
        }
    ]
});

Console.WriteLine(batch);
```

```go Go hidelines={1..10,-1}
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	batch, err := client.Beta.Messages.Batches.New(context.Background(),
		anthropic.BetaMessageBatchNewParams{
			Betas: []anthropic.AnthropicBeta{"output-300k-2026-03-24"},
			Requests: []anthropic.BetaMessageBatchNewParamsRequest{
				{
					CustomID: "long-form-request",
					Params: anthropic.BetaMessageBatchNewParamsRequestParams{
						Model:     anthropic.ModelClaudeOpus4_6,
						MaxTokens: 300_000,
						Messages: []anthropic.BetaMessageParam{
							anthropic.NewBetaUserMessage(
								anthropic.NewBetaTextBlock("Write a comprehensive technical guide to building distributed systems, covering architecture patterns, consistency models, fault tolerance, and operational best practices."),
							),
						},
					},
				},
			},
		})
	if err != nil {
		panic(err)
	}

	fmt.Println(batch.ID)
}
```

```java Java hidelines={1..3,5..6,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Model;
import com.anthropic.models.beta.messages.batches.*;

void main() {
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  BatchCreateParams params = BatchCreateParams.builder()
    .addBeta("output-300k-2026-03-24")
    .addRequest(
      BatchCreateParams.Request.builder()
        .customId("long-form-request")
        .params(
          BatchCreateParams.Request.Params.builder()
            .model(Model.CLAUDE_OPUS_4_6)
            .maxTokens(300_000L)
            .addUserMessage("Write a comprehensive technical guide to building distributed systems, covering architecture patterns, consistency models, fault tolerance, and operational best practices.")
            .build()
        )
        .build()
    )
    .build();

  BetaMessageBatch messageBatch = client.beta().messages().batches().create(params);

  IO.println(messageBatch);
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client();

$batch = $client->beta->messages->batches->create(
    betas: ['output-300k-2026-03-24'],
    requests: [
        [
            'custom_id' => 'long-form-request',
            'params' => [
                'model' => 'claude-opus-4-6',
                'max_tokens' => 300_000,
                'messages' => [
                    ['role' => 'user', 'content' => 'Write a comprehensive technical guide to building distributed systems, covering architecture patterns, consistency models, fault tolerance, and operational best practices.']
                ]
            ]
        ]
    ],
);

print_r($batch);
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

batch = client.beta.messages.batches.create(
  betas: ["output-300k-2026-03-24"],
  requests: [
    {
      custom_id: "long-form-request",
      params: {
        model: "claude-opus-4-6",
        max_tokens: 300_000,
        messages: [
          { role: "user", content: "Write a comprehensive technical guide to building distributed systems, covering architecture patterns, consistency models, fault tolerance, and operational best practices." }
        ]
      }
    }
  ]
)

puts batch
```

</CodeGroup>

### Best practices for effective batching

To get the most out of the Batches API:

- Monitor batch processing status regularly and implement appropriate retry logic for failed requests.
- Use meaningful `custom_id` values to easily match results with requests, since order is not guaranteed.
- Consider breaking very large datasets into multiple batches for better manageability.
- Dry run a single request shape with the Messages API to avoid validation errors.

### Troubleshooting common issues

If experiencing unexpected behavior:

- Verify that the total batch request size doesn't exceed 256 MB. If the request size is too large, you may get a 413 `request_too_large` error.
- Check that you're using [supported models](#supported-models) for all requests in the batch.
- Ensure each request in the batch has a unique `custom_id`.
- Ensure that it has been less than 29 days since batch `created_at` (not processing `ended_at`) time. If over 29 days have passed, results will no longer be viewable.
- Confirm that the batch has not been canceled.

Note that the failure of one request in a batch does not affect the processing of other requests.

---
## Batch storage and privacy

- **Workspace isolation**: Batches are isolated within the Workspace they are created in. They can only be accessed by API keys associated with that Workspace, or users with permission to view Workspace batches in the Console.

- **Result availability**: Batch results are available for 29 days after the batch is created, allowing ample time for retrieval and processing.

---
## Data retention

Batch processing stores request and response data for up to 29 days after batch creation. You can delete a message batch at any time after processing using the `DELETE /v1/messages/batches/{batch_id}` endpoint. To delete an in-progress batch, cancel it first. Asynchronous processing requires server-side storage of both inputs and outputs until batch completion and result retrieval.

For ZDR eligibility across all features, see [API and data retention](/docs/en/build-with-claude/api-and-data-retention).

## FAQ

  <section title="How long does it take for a batch to process?">

    Batches may take up to 24 hours for processing, but many finish sooner. Actual processing time depends on the size of the batch, current demand, and your request volume. It is possible for a batch to expire and not complete within 24 hours.
  
</section>

  <section title="Is the Batches API available for all models?">

    See [above](#supported-models) for the list of supported models.
  
</section>

  <section title="Can I use the Message Batches API with other API features?">

    Yes, the Message Batches API supports all features available in the Messages API, including beta features. However, streaming is not supported for batch requests.
  
</section>

  <section title="How does the Message Batches API affect pricing?">

    The Message Batches API offers a 50% discount on all usage compared to standard API prices. This applies to input tokens, output tokens, and any special tokens. For more on pricing, visit the [pricing page](https://claude.com/pricing#anthropic-api).
  
</section>

  <section title="Can I update a batch after it's been submitted?">

    No, once a batch has been submitted, it cannot be modified. If you need to make changes, you should cancel the current batch and submit a new one. Note that cancellation may not take immediate effect.
  
</section>

  <section title="Are there Message Batches API rate limits and do they interact with the Messages API rate limits?">

    The Message Batches API has HTTP requests-based rate limits in addition to limits on the number of requests in need of processing. See [Message Batches API rate limits](/docs/en/api/rate-limits#message-batches-api). Usage of the Batches API does not affect rate limits in the Messages API.
  
</section>

  <section title="How do I handle errors in my batch requests?">

    When you retrieve the results, each request will have a `result` field indicating whether it `succeeded`, `errored`, was `canceled`, or `expired`. For `errored` results, additional error information will be provided. View the error response object in the [API reference](/docs/en/api/creating-message-batches).
  
</section>

  <section title="How does the Message Batches API handle privacy and data separation?">

    The Message Batches API is designed with strong privacy and data separation measures:

    1. Batches and their results are isolated within the Workspace in which they were created. This means they can only be accessed by API keys from that same Workspace.
    2. Each request within a batch is processed independently, with no data leakage between requests.
    3. Results are only available for a limited time (29 days), and follow Anthropic's [data retention policy](https://support.claude.com/en/articles/7996866-how-long-do-you-store-personal-data).
    4. Downloading batch results in the Console can be disabled on the organization-level or on a per-workspace basis.
  
</section>

  <section title="Can I use prompt caching in the Message Batches API?">

    Yes, it is possible to use prompt caching with Message Batches API. However, because asynchronous batch requests can be processed concurrently and in any order, cache hits are provided on a best-effort basis.
  
</section>
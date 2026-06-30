# Batches

## Create a Message Batch

`$client->messages->batches->create(list<Request> requests, ?string userProfileID): MessageBatch`

**post** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `requests: list<Request>`

  List of requests for prompt completion. Each is an individual request to create a Message.

- `userProfileID?:optional string`

  The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

### Returns

- `MessageBatch`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$messageBatch = $client->messages->batches->create(
  requests: [
    [
      'customID' => 'my-custom-id-1',
      'params' => [
        'maxTokens' => 1024,
        'messages' => [['content' => 'Hello, world', 'role' => 'user']],
        'model' => 'claude-opus-4-6',
        'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
        'container' => 'container',
        'inferenceGeo' => 'inference_geo',
        'metadata' => ['userID' => '13803d75-b4b5-4c3e-b2a2-6f21399b021b'],
        'outputConfig' => [
          'effort' => 'low',
          'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
        ],
        'serviceTier' => 'auto',
        'stopSequences' => ['string'],
        'stream' => false,
        'system' => [
          [
            'text' => 'Today\'s date is 2024-06-01.',
            'type' => 'text',
            'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
            'citations' => [
              [
                'citedText' => 'cited_text',
                'documentIndex' => 0,
                'documentTitle' => 'x',
                'endCharIndex' => 0,
                'startCharIndex' => 0,
                'type' => 'char_location',
              ],
            ],
          ],
        ],
        'temperature' => 1,
        'thinking' => ['type' => 'adaptive', 'display' => 'summarized'],
        'toolChoice' => ['type' => 'auto', 'disableParallelToolUse' => true],
        'tools' => [
          [
            'inputSchema' => [
              'type' => 'object',
              'properties' => ['location' => 'bar', 'unit' => 'bar'],
              'required' => ['location'],
            ],
            'name' => 'name',
            'allowedCallers' => ['direct'],
            'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
            'deferLoading' => true,
            'description' => 'Get the current weather in a given location',
            'eagerInputStreaming' => true,
            'inputExamples' => [['foo' => 'bar']],
            'strict' => true,
            'type' => 'custom',
          ],
        ],
        'topK' => 5,
        'topP' => 0.7,
      ],
    ],
  ],
  userProfileID: 'anthropic-user-profile-id',
);

var_dump($messageBatch);
```

#### Response

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

## Retrieve a Message Batch

`$client->messages->batches->retrieve(string messageBatchID): MessageBatch`

**get** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

### Returns

- `MessageBatch`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$messageBatch = $client->messages->batches->retrieve('message_batch_id');

var_dump($messageBatch);
```

#### Response

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

## List Message Batches

`$client->messages->batches->list(?string afterID, ?string beforeID, ?int limit): Page<MessageBatch>`

**get** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `afterID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `beforeID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit?:optional int`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

### Returns

- `MessageBatch`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->messages->batches->list(
  afterID: 'after_id', beforeID: 'before_id', limit: 1
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
      "archived_at": "2024-08-20T18:37:24.100435Z",
      "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
      "created_at": "2024-08-20T18:37:24.100435Z",
      "ended_at": "2024-08-20T18:37:24.100435Z",
      "expires_at": "2024-08-20T18:37:24.100435Z",
      "processing_status": "in_progress",
      "request_counts": {
        "canceled": 10,
        "errored": 30,
        "expired": 10,
        "processing": 100,
        "succeeded": 50
      },
      "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
      "type": "message_batch"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Cancel a Message Batch

`$client->messages->batches->cancel(string messageBatchID): MessageBatch`

**post** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

### Returns

- `MessageBatch`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$messageBatch = $client->messages->batches->cancel('message_batch_id');

var_dump($messageBatch);
```

#### Response

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

## Delete a Message Batch

`$client->messages->batches->delete(string messageBatchID): DeletedMessageBatch`

**delete** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

### Returns

- `DeletedMessageBatch`

  - `string id`

    ID of the Message Batch.

  - `"message_batch_deleted" type`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$deletedMessageBatch = $client->messages->batches->delete('message_batch_id');

var_dump($deletedMessageBatch);
```

#### Response

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

## Retrieve Message Batch results

`$client->messages->batches->results(string messageBatchID): MessageBatchIndividualResponse`

**get** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

### Returns

- `MessageBatchIndividualResponse`

  - `string customID`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `MessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$messageBatchIndividualResponse = $client->messages->batches->resultsStream(
  'message_batch_id'
);

var_dump($messageBatchIndividualResponse);
```

## Domain Types

### Deleted Message Batch

- `DeletedMessageBatch`

  - `string id`

    ID of the Message Batch.

  - `"message_batch_deleted" type`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Message Batch

- `MessageBatch`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Message Batch Canceled Result

- `MessageBatchCanceledResult`

  - `"canceled" type`

### Message Batch Errored Result

- `MessageBatchErroredResult`

  - `ErrorResponse error`

  - `"errored" type`

### Message Batch Expired Result

- `MessageBatchExpiredResult`

  - `"expired" type`

### Message Batch Individual Response

- `MessageBatchIndividualResponse`

  - `string customID`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `MessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

### Message Batch Request Counts

- `MessageBatchRequestCounts`

  - `int canceled`

    Number of requests in the Message Batch that have been canceled.

    This is zero until processing of the entire Message Batch has ended.

  - `int errored`

    Number of requests in the Message Batch that encountered an error.

    This is zero until processing of the entire Message Batch has ended.

  - `int expired`

    Number of requests in the Message Batch that have expired.

    This is zero until processing of the entire Message Batch has ended.

  - `int processing`

    Number of requests in the Message Batch that are processing.

  - `int succeeded`

    Number of requests in the Message Batch that have completed successfully.

    This is zero until processing of the entire Message Batch has ended.

### Message Batch Result

- `MessageBatchResult`

  - `MessageBatchSucceededResult`

    - `Message message`

    - `"succeeded" type`

  - `MessageBatchErroredResult`

    - `ErrorResponse error`

    - `"errored" type`

  - `MessageBatchCanceledResult`

    - `"canceled" type`

  - `MessageBatchExpiredResult`

    - `"expired" type`

### Message Batch Succeeded Result

- `MessageBatchSucceededResult`

  - `Message message`

  - `"succeeded" type`

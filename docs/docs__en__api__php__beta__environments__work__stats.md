## Get Queue Statistics

`$client->beta->environments->work->stats(string environmentID, ?list<AnthropicBeta> betas): SelfHostedWorkQueueStats`

**get** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

### Parameters

- `environmentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SelfHostedWorkQueueStats`

  - `int depth`

    Number of work items waiting to be picked up (lag from consumer group)

  - `?string oldestQueuedAt`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `int pending`

    Number of work items being processed (polled but not acknowledged)

  - `"work_queue_stats" type`

    The type of object

  - `?int workersPolling`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSelfHostedWorkQueueStats = $client->beta->environments->work->stats(
  'env_011CZkZ9X2dpNyB7HsEFoRfW', betas: ['message-batches-2024-09-24']
);

var_dump($betaSelfHostedWorkQueueStats);
```

#### Response

```json
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```

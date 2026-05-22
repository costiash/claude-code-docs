## Record Heartbeat

`$client->beta->environments->work->heartbeat(string workID, string environmentID, ?int desiredTTLSeconds, ?string expectedLastHeartbeat, ?list<AnthropicBeta> betas): SelfHostedWorkHeartbeatResponse`

**post** `/v1/environments/{environment_id}/work/{work_id}/heartbeat`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

### Parameters

- `environmentID: string`

- `workID: string`

- `desiredTTLSeconds?:optional int`

  Desired TTL in seconds

- `expectedLastHeartbeat?:optional string`

  Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SelfHostedWorkHeartbeatResponse`

  - `string lastHeartbeat`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `bool leaseExtended`

    Whether the heartbeat succeeded in extending the lease

  - `State state`

    Current state of the work item (active/stopping/stopped)

  - `int ttlSeconds`

    Effective TTL applied to the lease

  - `"work_heartbeat" type`

    The type of response

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSelfHostedWorkHeartbeatResponse = $client
  ->beta
  ->environments
  ->work
  ->heartbeat(
  'work_id',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
  desiredTTLSeconds: 0,
  expectedLastHeartbeat: 'expected_last_heartbeat',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaSelfHostedWorkHeartbeatResponse);
```

#### Response

```json
{
  "last_heartbeat": "last_heartbeat",
  "lease_extended": true,
  "state": "queued",
  "ttl_seconds": 0,
  "type": "work_heartbeat"
}
```

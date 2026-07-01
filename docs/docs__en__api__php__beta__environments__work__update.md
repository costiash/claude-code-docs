## Update Work Item

`$client->beta->environments->work->update(string workID, string environmentID, array<string,string> metadata, ?list<AnthropicBeta> betas): SelfHostedWork`

**post** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

### Parameters

- `environmentID: string`

- `workID: string`

- `metadata: array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SelfHostedWork`

  - `string id`

    Work identifier (e.g., 'work_...')

  - `?string acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `string createdAt`

    RFC 3339 timestamp when work was created

  - `SessionWorkData data`

    The actual work to be performed

  - `string environmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `?string latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `array<string,string> metadata`

    User-provided metadata key-value pairs associated with this work item

  - `?string secret`

    Credential payload used by the environment worker to execute this work item. May be populated when polling for work; null on all other retrieval paths.

  - `?string startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

  - `?string stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `?string stoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `"work" type`

    The type of object (always 'work')

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSelfHostedWork = $client->beta->environments->work->update(
  'work_id',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
  metadata: ['foo' => 'string'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaSelfHostedWork);
```

#### Response

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "secret": "secret",
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

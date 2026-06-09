## List Deployment Runs

`$client->beta->deploymentRuns->list(?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?string deploymentID, ?bool hasError, ?int limit, ?string page, ?BetaManagedAgentsTriggerType triggerType, ?list<AnthropicBeta> betas): PageCursor<BetaManagedAgentsDeploymentRun>`

**get** `/v1/deployment_runs`

List Deployment Runs

### Parameters

- `createdAtGt?:optional \Datetime`

  Return runs created strictly after this time (exclusive).

- `createdAtGte?:optional \Datetime`

  Return runs created at or after this time (inclusive).

- `createdAtLt?:optional \Datetime`

  Return runs created strictly before this time (exclusive).

- `createdAtLte?:optional \Datetime`

  Return runs created at or before this time (inclusive).

- `deploymentID?:optional string`

  Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment_id returns 200 with empty data.

- `hasError?:optional bool`

  Filter: true for runs with non-null error, false for runs with non-null session_id. Omit for all.

- `limit?:optional int`

  Maximum results per page. Default 20, maximum 1000.

- `page?:optional string`

  Opaque pagination cursor. Pass next_page from the previous response. Invalid or expired cursors return 400.

- `triggerType?:optional BetaManagedAgentsTriggerType`

  Filter runs by what triggered them. Omit to return all runs.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeploymentRun`

  - `string id`

    Unique identifier for this run (`drun_...`).

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string deploymentID`

    ID of the deployment that produced this run.

  - `?Error error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

  - `?string sessionID`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `BetaManagedAgentsTriggerContext triggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->deploymentRuns->list(
  createdAtGt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  deploymentID: 'deployment_id',
  hasError: true,
  limit: 0,
  page: 'page',
  triggerType: BetaManagedAgentsTriggerType::SCHEDULE,
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "deployment_id": "deployment_id",
      "error": {
        "message": "message",
        "type": "environment_archived_error"
      },
      "session_id": "session_id",
      "trigger_context": {
        "scheduled_at": "2019-12-27T18:11:19.117Z",
        "type": "schedule"
      },
      "type": "deployment_run"
    }
  ],
  "next_page": "next_page"
}
```

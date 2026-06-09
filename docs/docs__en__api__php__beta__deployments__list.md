## List Deployments

`$client->beta->deployments->list(?string agentID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?BetaManagedAgentsDeploymentStatus status, ?list<AnthropicBeta> betas): PageCursor<BetaManagedAgentsDeployment>`

**get** `/v1/deployments`

List Deployments

### Parameters

- `agentID?:optional string`

  Filter by agent ID.

- `createdAtGte?:optional \Datetime`

  Return deployments created at or after this time (inclusive).

- `createdAtLte?:optional \Datetime`

  Return deployments created at or before this time (inclusive).

- `includeArchived?:optional bool`

  When true, includes archived deployments. Default: false (exclude archived).

- `limit?:optional int`

  Maximum results per page. Default 20, maximum 100.

- `page?:optional string`

  Opaque pagination cursor.

- `status?:optional BetaManagedAgentsDeploymentStatus`

  Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeployment`

  - `string id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string description`

    Description of what the deployment does.

  - `string environmentID`

    ID of the `environment` where sessions run.

  - `list<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `string name`

    Human-readable name.

  - `?BetaManagedAgentsDeploymentPausedReason pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `list<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

  - `?BetaManagedAgentsSchedule schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `list<string> vaultIDs`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->deployments->list(
  agentID: 'agent_id',
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  includeArchived: true,
  limit: 0,
  page: 'page',
  status: BetaManagedAgentsDeploymentStatus::ACTIVE,
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
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "environment_id": "environment_id",
      "initial_events": [
        {
          "content": [
            {
              "text": "Where is my order #1234?",
              "type": "text"
            }
          ],
          "type": "user.message"
        }
      ],
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "paused_reason": {
        "type": "manual"
      },
      "resources": [
        {
          "type": "github_repository",
          "url": "url",
          "checkout": {
            "name": "main",
            "type": "branch"
          },
          "mount_path": "mount_path"
        }
      ],
      "schedule": {
        "expression": "x",
        "timezone": "x",
        "type": "cron",
        "last_run_at": "2019-12-27T18:11:19.117Z",
        "upcoming_runs_at": [
          "2019-12-27T18:11:19.117Z"
        ]
      },
      "status": "active",
      "type": "deployment",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "vault_ids": [
        "string"
      ]
    }
  ],
  "next_page": "next_page"
}
```

# Deployments

## Create Deployment

`$client->beta->deployments->create(Agent agent, string environmentID, list<BetaManagedAgentsDeploymentInitialEventParams> initialEvents, string name, ?string description, ?array<string,string> metadata, ?list<Resource> resources, ?BetaManagedAgentsScheduleParams schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): BetaManagedAgentsDeployment`

**post** `/v1/deployments`

Create Deployment

### Parameters

- `agent: Agent`

  Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

- `environmentID: string`

  ID of the `environment` defining the container configuration for sessions created from this deployment.

- `initialEvents: list<BetaManagedAgentsDeploymentInitialEventParams>`

  Events to send to each session immediately after creation. At least 1, maximum 50.

- `name: string`

  Human-readable name for the deployment.

- `description?:optional string`

  Description of what the deployment does.

- `metadata?:optional array<string,string>`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources?:optional list<Resource>`

  Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

- `schedule?:optional BetaManagedAgentsScheduleParams`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

- `vaultIDs?:optional list<string>`

  Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

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

$betaManagedAgentsDeployment = $client->beta->deployments->create(
  agent: 'string',
  environmentID: 'x',
  initialEvents: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  name: 'x',
  description: 'description',
  metadata: ['foo' => 'string'],
  resources: [
    [
      'fileID' => 'file_011CNha8iCJcU1wXNR6q4V8w',
      'type' => 'file',
      'mountPath' => '/uploads/receipt.pdf',
    ],
  ],
  schedule: [
    'expression' => '0 9 * * 1-5',
    'timezone' => 'America/Los_Angeles',
    'type' => 'cron',
  ],
  vaultIDs: ['string'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
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
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

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
      "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Compiles yesterday's orders into a report every weekday morning.",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "initial_events": [
        {
          "content": [
            {
              "text": "Compile yesterday's orders into report.md.",
              "type": "text"
            }
          ],
          "type": "user.message"
        }
      ],
      "metadata": {},
      "name": "Daily order report",
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
        "expression": "0 9 * * 1-5",
        "timezone": "America/Los_Angeles",
        "type": "cron",
        "last_run_at": "2026-03-16T16:00:09Z",
        "upcoming_runs_at": [
          "2026-03-17T16:00:00Z",
          "2026-03-18T16:00:00Z"
        ]
      },
      "status": "active",
      "type": "deployment",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ]
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Deployment

`$client->beta->deployments->retrieve(string deploymentID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeployment`

**get** `/v1/deployments/{deployment_id}`

Get Deployment

### Parameters

- `deploymentID: string`

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

$betaManagedAgentsDeployment = $client->beta->deployments->retrieve(
  'depl_011CZkZcDH3vPqd7xnEfwTai', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
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
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Update Deployment

`$client->beta->deployments->update(string deploymentID, ?Agent agent, ?string description, ?string environmentID, ?list<BetaManagedAgentsDeploymentInitialEventParams> initialEvents, ?array<string,string> metadata, ?string name, ?list<Resource> resources, ?BetaManagedAgentsScheduleParams schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas): BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}`

Update Deployment

### Parameters

- `deploymentID: string`

- `agent?:optional Agent`

  Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

- `description?:optional string`

  Description. Omit to preserve; send empty string or null to clear.

- `environmentID?:optional string`

  ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

- `initialEvents?:optional list<BetaManagedAgentsDeploymentInitialEventParams>`

  Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name?:optional string`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

- `resources?:optional list<Resource>`

  Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

- `schedule?:optional BetaManagedAgentsScheduleParams`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

- `vaultIDs?:optional list<string>`

  Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

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

$betaManagedAgentsDeployment = $client->beta->deployments->update(
  'depl_011CZkZcDH3vPqd7xnEfwTai',
  agent: 'string',
  description: 'description',
  environmentID: 'environment_id',
  initialEvents: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  metadata: ['foo' => 'string'],
  name: 'name',
  resources: [
    [
      'fileID' => 'file_011CNha8iCJcU1wXNR6q4V8w',
      'type' => 'file',
      'mountPath' => '/uploads/receipt.pdf',
    ],
  ],
  schedule: [
    'expression' => '0 9 * * 1-5',
    'timezone' => 'America/Los_Angeles',
    'type' => 'cron',
  ],
  vaultIDs: ['string'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
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
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Archive Deployment

`$client->beta->deployments->archive(string deploymentID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Parameters

- `deploymentID: string`

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

$betaManagedAgentsDeployment = $client->beta->deployments->archive(
  'depl_011CZkZcDH3vPqd7xnEfwTai', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
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
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Run Deployment Now

`$client->beta->deployments->run(string deploymentID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeploymentRun`

**post** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `deploymentID: string`

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

$betaManagedAgentsDeploymentRun = $client->beta->deployments->run(
  'depl_011CZkZcDH3vPqd7xnEfwTai', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeploymentRun);
```

#### Response

```json
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
```

## Pause Deployment

`$client->beta->deployments->pause(string deploymentID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Parameters

- `deploymentID: string`

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

$betaManagedAgentsDeployment = $client->beta->deployments->pause(
  'depl_011CZkZcDH3vPqd7xnEfwTai', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
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
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Unpause Deployment

`$client->beta->deployments->unpause(string deploymentID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeployment`

**post** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Parameters

- `deploymentID: string`

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

$betaManagedAgentsDeployment = $client->beta->deployments->unpause(
  'depl_011CZkZcDH3vPqd7xnEfwTai', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeployment);
```

#### Response

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
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
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

## Domain Types

### Beta Managed Agents Agent Archived Deployment Paused Reason Error

- `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Cron Schedule

- `BetaManagedAgentsCronSchedule`

  - `string expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `string timezone`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `Type type`

  - `?\Datetime lastRunAt`

    A timestamp in RFC 3339 format

  - `?list<\Datetime> upcomingRunsAt`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `BetaManagedAgentsCronScheduleParams`

  - `string expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `string timezone`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `Type type`

### Beta Managed Agents Deployment

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

### Beta Managed Agents Deployment Initial Event

- `BetaManagedAgentsDeploymentInitialEvent`

  - `BetaManagedAgentsDeploymentUserMessageEvent`

    - `list<Content> content`

      Array of content blocks for the user message.

    - `Type type`

  - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

    - `string description`

      What the agent should produce. This is the task specification.

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

    - `?int maxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `BetaManagedAgentsDeploymentSystemMessageEvent`

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks to append. Text-only.

    - `Type type`

### Beta Managed Agents Deployment Initial Event Params

- `BetaManagedAgentsDeploymentInitialEventParams`

  - `ManagedAgentsUserMessageEventParams`

    - `list<Content> content`

      Array of content blocks for the user message.

    - `Type type`

  - `ManagedAgentsUserDefineOutcomeEventParams`

    - `string description`

      What the agent should produce. This is the task specification.

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `Type type`

    - `?int maxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `ManagedAgentsSystemMessageEventParams`

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks to append. Text-only.

    - `Type type`

### Beta Managed Agents Deployment Paused Reason

- `BetaManagedAgentsDeploymentPausedReason`

  - `BetaManagedAgentsManualDeploymentPausedReason`

    - `Type type`

  - `BetaManagedAgentsErrorDeploymentPausedReason`

    - `BetaManagedAgentsDeploymentPausedReasonError error`

      The error that triggered an auto-pause. Matches the failed run's `error.type`.

    - `Type type`

### Beta Managed Agents Deployment Paused Reason Error

- `BetaManagedAgentsDeploymentPausedReasonError`

  - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsUnknownDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

    - `Type type`

  - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

    - `Type type`

### Beta Managed Agents Deployment Status

- `BetaManagedAgentsDeploymentStatus`

  - `"active"`

  - `"paused"`

### Beta Managed Agents Deployment System Message Event

- `BetaManagedAgentsDeploymentSystemMessageEvent`

  - `list<BetaManagedAgentsSystemContentBlock> content`

    System content blocks to append. Text-only.

  - `Type type`

### Beta Managed Agents Deployment User Define Outcome Event

- `BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

  - `string description`

    What the agent should produce. This is the task specification.

  - `Rubric rubric`

    Rubric for grading the quality of an outcome.

  - `Type type`

  - `?int maxIterations`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents Deployment User Message Event

- `BetaManagedAgentsDeploymentUserMessageEvent`

  - `list<Content> content`

    Array of content blocks for the user message.

  - `Type type`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Error Deployment Paused Reason

- `BetaManagedAgentsErrorDeploymentPausedReason`

  - `BetaManagedAgentsDeploymentPausedReasonError error`

    The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `Type type`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents File Resource Config

- `BetaManagedAgentsFileResourceConfig`

  - `string fileID`

    ID of a previously uploaded file.

  - `Type type`

  - `?string mountPath`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `BetaManagedAgentsGitHubRepositoryResourceConfig`

  - `Type type`

  - `string url`

    Github URL of the repository

  - `?Checkout checkout`

    Branch or commit to check out. Defaults to the repository's default branch.

  - `?string mountPath`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `BetaManagedAgentsManualDeploymentPausedReason`

  - `Type type`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Memory Store Resource Config

- `BetaManagedAgentsMemoryStoreResourceConfig`

  - `string memoryStoreID`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `Type type`

  - `?Access access`

    Access mode for an attached memory store.

  - `?string instructions`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Schedule

- `BetaManagedAgentsSchedule`

  - `string expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `string timezone`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `Type type`

  - `?\Datetime lastRunAt`

    A timestamp in RFC 3339 format

  - `?list<\Datetime> upcomingRunsAt`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `BetaManagedAgentsScheduleParams`

  - `string expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `string timezone`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `Type type`

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Session Resource Config

- `BetaManagedAgentsSessionResourceConfig`

  - `BetaManagedAgentsGitHubRepositoryResourceConfig`

    - `Type type`

    - `string url`

      Github URL of the repository

    - `?Checkout checkout`

      Branch or commit to check out. Defaults to the repository's default branch.

    - `?string mountPath`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `BetaManagedAgentsFileResourceConfig`

    - `string fileID`

      ID of a previously uploaded file.

    - `Type type`

    - `?string mountPath`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `BetaManagedAgentsMemoryStoreResourceConfig`

    - `string memoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type type`

    - `?Access access`

      Access mode for an attached memory store.

    - `?string instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `BetaManagedAgentsUnknownDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

  - `Type type`

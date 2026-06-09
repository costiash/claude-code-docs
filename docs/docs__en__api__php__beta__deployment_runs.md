# Deployment Runs

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

## Get Deployment Run

`$client->beta->deploymentRuns->retrieve(string deploymentRunID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeploymentRun`

**get** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

### Parameters

- `deploymentRunID: string`

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

$betaManagedAgentsDeploymentRun = $client->beta->deploymentRuns->retrieve(
  'deployment_run_id', betas: ['message-batches-2024-09-24']
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

## Domain Types

### Beta Managed Agents Agent Archived Run Error

- `BetaManagedAgentsAgentArchivedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Deployment Run

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

### Beta Managed Agents Environment Archived Run Error

- `BetaManagedAgentsEnvironmentArchivedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Environment Not Found Run Error

- `BetaManagedAgentsEnvironmentNotFoundRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents File Not Found Run Error

- `BetaManagedAgentsFileNotFoundRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Manual Trigger Context

- `BetaManagedAgentsManualTriggerContext`

  - `Type type`

### Beta Managed Agents MCP Egress Blocked Run Error

- `BetaManagedAgentsMCPEgressBlockedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Memory Store Archived Run Error

- `BetaManagedAgentsMemoryStoreArchivedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Organization Disabled Run Error

- `BetaManagedAgentsOrganizationDisabledRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Schedule Trigger Context

- `BetaManagedAgentsScheduleTriggerContext`

  - `\Datetime scheduledAt`

    A timestamp in RFC 3339 format

  - `Type type`

### Beta Managed Agents Self Hosted Resources Unsupported Run Error

- `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Session Creation Rejected Run Error

- `BetaManagedAgentsSessionCreationRejectedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Session Rate Limited Run Error

- `BetaManagedAgentsSessionRateLimitedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Session Resource Not Found Run Error

- `BetaManagedAgentsSessionResourceNotFoundRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Skill Not Found Run Error

- `BetaManagedAgentsSkillNotFoundRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Trigger Context

- `BetaManagedAgentsTriggerContext`

  - `BetaManagedAgentsScheduleTriggerContext`

    - `\Datetime scheduledAt`

      A timestamp in RFC 3339 format

    - `Type type`

  - `BetaManagedAgentsManualTriggerContext`

    - `Type type`

### Beta Managed Agents Trigger Type

- `BetaManagedAgentsTriggerType`

  - `"schedule"`

  - `"manual"`

### Beta Managed Agents Unknown Run Error

- `BetaManagedAgentsUnknownRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Vault Archived Run Error

- `BetaManagedAgentsVaultArchivedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Vault Not Found Run Error

- `BetaManagedAgentsVaultNotFoundRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

### Beta Managed Agents Workspace Archived Run Error

- `BetaManagedAgentsWorkspaceArchivedRunError`

  - `string message`

    Human-readable error description.

  - `Type type`

## List Sessions

`$client->beta->sessions->list(?string agentID, ?int agentVersion, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?string deploymentID, ?bool includeArchived, ?int limit, ?string memoryStoreID, ?Order order, ?string page, ?list<Status> statuses, ?list<AnthropicBeta> betas): PageCursor<BetaManagedAgentsSession>`

**get** `/v1/sessions`

List Sessions

### Parameters

- `agentID?:optional string`

  Filter sessions created with this agent ID.

- `agentVersion?:optional int`

  Filter by agent version. Only applies when agent_id is also set.

- `createdAtGt?:optional \Datetime`

  Return sessions created after this time (exclusive).

- `createdAtGte?:optional \Datetime`

  Return sessions created at or after this time (inclusive).

- `createdAtLt?:optional \Datetime`

  Return sessions created before this time (exclusive).

- `createdAtLte?:optional \Datetime`

  Return sessions created at or before this time (inclusive).

- `deploymentID?:optional string`

  Filter sessions created by this deployment ID.

- `includeArchived?:optional bool`

  When true, includes archived sessions. Default: false (exclude archived).

- `limit?:optional int`

  Maximum number of results to return.

- `memoryStoreID?:optional string`

  Filter sessions whose resources contain a memory_store with this memory store ID.

- `order?:optional Order`

  Sort direction for results, ordered by created_at. Defaults to desc (newest first).

- `page?:optional string`

  Opaque pagination cursor from a previous response.

- `statuses?:optional list<Status>`

  Filter by session status. Repeat the parameter to match any of multiple statuses.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsSession`

  - `string id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string environmentID`

  - `array<string,string> metadata`

  - `list<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

  - `list<ManagedAgentsSessionResource> resources`

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for a session.

  - `Status status`

    SessionStatus enum

  - `?string title`

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for a session across all turns.

  - `list<string> vaultIDs`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `?string deploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->list(
  agentID: 'agent_id',
  agentVersion: 0,
  createdAtGt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  deploymentID: 'deployment_id',
  includeArchived: true,
  limit: 0,
  memoryStoreID: 'memory_store_id',
  order: 'asc',
  page: 'page',
  statuses: ['rescheduling'],
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "description": "A general-purpose starter agent.",
        "mcp_servers": [
          {
            "name": "example-mcp",
            "type": "url",
            "url": "https://example-server.modelcontextprotocol.io/sse"
          }
        ],
        "model": {
          "id": "claude-sonnet-4-6",
          "speed": "standard"
        },
        "multiagent": {
          "agents": [
            {
              "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
              "description": "A focused research subagent.",
              "mcp_servers": [
                {
                  "name": "example-mcp",
                  "type": "url",
                  "url": "https://example-server.modelcontextprotocol.io/sse"
                }
              ],
              "model": {
                "id": "claude-sonnet-4-6",
                "speed": "standard"
              },
              "name": "Researcher",
              "skills": [
                {
                  "skill_id": "xlsx",
                  "type": "anthropic",
                  "version": "1"
                }
              ],
              "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
              "tools": [
                {
                  "configs": [
                    {
                      "enabled": true,
                      "name": "bash",
                      "permission_policy": {
                        "type": "always_allow"
                      }
                    }
                  ],
                  "default_config": {
                    "enabled": true,
                    "permission_policy": {
                      "type": "always_ask"
                    }
                  },
                  "type": "agent_toolset_20260401"
                }
              ],
              "type": "agent",
              "version": 1
            }
          ],
          "type": "coordinator"
        },
        "name": "My First Agent",
        "skills": [
          {
            "skill_id": "xlsx",
            "type": "anthropic",
            "version": "1"
          },
          {
            "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
            "type": "custom",
            "version": "2"
          }
        ],
        "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
        "tools": [
          {
            "configs": [
              {
                "enabled": true,
                "name": "bash",
                "permission_policy": {
                  "type": "always_allow"
                }
              }
            ],
            "default_config": {
              "enabled": true,
              "permission_policy": {
                "type": "always_ask"
              }
            },
            "type": "agent_toolset_20260401"
          }
        ],
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "metadata": {},
      "outcome_evaluations": [
        {
          "completed_at": "2026-03-15T10:02:31Z",
          "description": "Produce a 2-page summary as summary.md",
          "explanation": "All five sections present with inline citations.",
          "iteration": 0,
          "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
          "result": "satisfied",
          "type": "outcome_evaluation"
        }
      ],
      "resources": [
        {
          "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
          "created_at": "2026-03-15T10:00:00Z",
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "mount_path": "/uploads/receipt.pdf",
          "type": "file",
          "updated_at": "2026-03-15T10:00:00Z"
        },
        {
          "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
          "created_at": "2026-03-15T10:00:00Z",
          "mount_path": "/workspace/example-repo",
          "type": "github_repository",
          "updated_at": "2026-03-15T10:00:00Z",
          "url": "https://github.com/example-org/example-repo",
          "checkout": {
            "name": "main",
            "type": "branch"
          }
        }
      ],
      "stats": {
        "active_seconds": 0,
        "duration_seconds": 0
      },
      "status": "idle",
      "title": "Order #1234 inquiry",
      "type": "session",
      "updated_at": "2026-03-15T10:00:00Z",
      "usage": {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
      },
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ],
      "deployment_id": "deployment_id"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

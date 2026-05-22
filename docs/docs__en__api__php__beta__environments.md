# Environments

## Create Environment

`$client->beta->environments->create(string name, ?Config config, ?string description, ?array<string,string> metadata, ?Scope scope, ?list<AnthropicBeta> betas): BetaEnvironment`

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `name: string`

  Human-readable name for the environment

- `config?:optional Config`

  Environment configuration

- `description?:optional string`

  Optional description of the environment

- `metadata?:optional array<string,string>`

  User-provided metadata key-value pairs

- `scope?:optional Scope`

  The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. Only applicable for self-hosted environments. If not specified, defaults based on organization type.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaEnvironment`

  - `string id`

    Environment identifier (e.g., 'env_...')

  - `?string archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

  - `string createdAt`

    RFC 3339 timestamp when environment was created

  - `string description`

    User-provided description for the environment

  - `array<string,string> metadata`

    User-provided metadata key-value pairs

  - `string name`

    Human-readable name for the environment

  - `"environment" type`

    The type of object (always 'environment')

  - `string updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `?Scope scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironment = $client->beta->environments->create(
  name: 'python-data-analysis',
  config: [
    'type' => 'cloud',
    'networking' => [
      'type' => 'limited',
      'allowMCPServers' => true,
      'allowPackageManagers' => true,
      'allowedHosts' => ['api.example.com'],
    ],
    'packages' => [
      'apt' => ['string'],
      'cargo' => ['string'],
      'gem' => ['string'],
      'go' => ['string'],
      'npm' => ['string'],
      'pip' => ['pandas', 'numpy'],
      'type' => 'packages',
    ],
  ],
  description: 'Python environment with data-analysis packages.',
  metadata: ['foo' => 'string'],
  scope: 'organization',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaEnvironment);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## List Environments

`$client->beta->environments->list(?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<BetaEnvironment>`

**get** `/v1/environments`

List environments with pagination support.

### Parameters

- `includeArchived?:optional bool`

  Include archived environments in the response

- `limit?:optional int`

  Maximum number of environments to return

- `page?:optional string`

  Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaEnvironment`

  - `string id`

    Environment identifier (e.g., 'env_...')

  - `?string archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

  - `string createdAt`

    RFC 3339 timestamp when environment was created

  - `string description`

    User-provided description for the environment

  - `array<string,string> metadata`

    User-provided metadata key-value pairs

  - `string name`

    Human-readable name for the environment

  - `"environment" type`

    The type of object (always 'environment')

  - `string updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `?Scope scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->environments->list(
  includeArchived: true,
  limit: 1,
  page: 'page',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "archived_at": null,
      "config": {
        "networking": {
          "allow_mcp_servers": false,
          "allow_package_managers": true,
          "allowed_hosts": [
            "api.example.com"
          ],
          "type": "limited"
        },
        "packages": {
          "apt": [
            "string"
          ],
          "cargo": [
            "string"
          ],
          "gem": [
            "string"
          ],
          "go": [
            "string"
          ],
          "npm": [
            "string"
          ],
          "pip": [
            "pandas",
            "numpy"
          ],
          "type": "packages"
        },
        "type": "cloud"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Python environment with data-analysis packages.",
      "metadata": {},
      "name": "python-data-analysis",
      "type": "environment",
      "updated_at": "2026-03-15T10:00:00Z",
      "scope": "organization"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Environment

`$client->beta->environments->retrieve(string environmentID, ?list<AnthropicBeta> betas): BetaEnvironment`

**get** `/v1/environments/{environment_id}`

Retrieve a specific environment by ID.

### Parameters

- `environmentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaEnvironment`

  - `string id`

    Environment identifier (e.g., 'env_...')

  - `?string archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

  - `string createdAt`

    RFC 3339 timestamp when environment was created

  - `string description`

    User-provided description for the environment

  - `array<string,string> metadata`

    User-provided metadata key-value pairs

  - `string name`

    Human-readable name for the environment

  - `"environment" type`

    The type of object (always 'environment')

  - `string updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `?Scope scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironment = $client->beta->environments->retrieve(
  'env_011CZkZ9X2dpNyB7HsEFoRfW', betas: ['message-batches-2024-09-24']
);

var_dump($betaEnvironment);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Update Environment

`$client->beta->environments->update(string environmentID, ?Config config, ?string description, ?array<string,string> metadata, ?string name, ?Scope scope, ?list<AnthropicBeta> betas): BetaEnvironment`

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `environmentID: string`

- `config?:optional Config`

  Updated environment configuration

- `description?:optional string`

  Updated description of the environment

- `metadata?:optional array<string,string>`

  User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

- `name?:optional string`

  Updated name for the environment

- `scope?:optional Scope`

  The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaEnvironment`

  - `string id`

    Environment identifier (e.g., 'env_...')

  - `?string archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

  - `string createdAt`

    RFC 3339 timestamp when environment was created

  - `string description`

    User-provided description for the environment

  - `array<string,string> metadata`

    User-provided metadata key-value pairs

  - `string name`

    Human-readable name for the environment

  - `"environment" type`

    The type of object (always 'environment')

  - `string updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `?Scope scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironment = $client->beta->environments->update(
  'env_011CZkZ9X2dpNyB7HsEFoRfW',
  config: [
    'type' => 'cloud',
    'networking' => [
      'type' => 'limited',
      'allowMCPServers' => true,
      'allowPackageManagers' => true,
      'allowedHosts' => ['api.example.com'],
    ],
    'packages' => [
      'apt' => ['string'],
      'cargo' => ['string'],
      'gem' => ['string'],
      'go' => ['string'],
      'npm' => ['string'],
      'pip' => ['pandas', 'numpy'],
      'type' => 'packages',
    ],
  ],
  description: 'Python environment with data-analysis packages.',
  metadata: ['foo' => 'string'],
  name: 'x',
  scope: 'organization',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaEnvironment);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Delete Environment

`$client->beta->environments->delete(string environmentID, ?list<AnthropicBeta> betas): BetaEnvironmentDeleteResponse`

**delete** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Parameters

- `environmentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaEnvironmentDeleteResponse`

  - `string id`

    Environment identifier

  - `"environment_deleted" type`

    The type of response

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironmentDeleteResponse = $client->beta->environments->delete(
  'env_011CZkZ9X2dpNyB7HsEFoRfW', betas: ['message-batches-2024-09-24']
);

var_dump($betaEnvironmentDeleteResponse);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```

## Archive Environment

`$client->beta->environments->archive(string environmentID, ?list<AnthropicBeta> betas): BetaEnvironment`

**post** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Parameters

- `environmentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaEnvironment`

  - `string id`

    Environment identifier (e.g., 'env_...')

  - `?string archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

  - `string createdAt`

    RFC 3339 timestamp when environment was created

  - `string description`

    User-provided description for the environment

  - `array<string,string> metadata`

    User-provided metadata key-value pairs

  - `string name`

    Human-readable name for the environment

  - `"environment" type`

    The type of object (always 'environment')

  - `string updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `?Scope scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironment = $client->beta->environments->archive(
  'env_011CZkZ9X2dpNyB7HsEFoRfW', betas: ['message-batches-2024-09-24']
);

var_dump($betaEnvironment);
```

#### Response

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Domain Types

### Beta Cloud Config

- `BetaCloudConfig`

  - `Networking networking`

    Network configuration policy.

  - `BetaPackages packages`

    Package manager configuration.

  - `"cloud" type`

    Environment type

### Beta Cloud Config Params

- `BetaCloudConfigParams`

  - `"cloud" type`

    Environment type

  - `?Networking networking`

    Network configuration policy. Omit on update to preserve the existing value.

  - `?BetaPackagesParams packages`

    Specify packages (and optionally their versions) available in this environment.

    When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

### Beta Environment

- `BetaEnvironment`

  - `string id`

    Environment identifier (e.g., 'env_...')

  - `?string archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

  - `string createdAt`

    RFC 3339 timestamp when environment was created

  - `string description`

    User-provided description for the environment

  - `array<string,string> metadata`

    User-provided metadata key-value pairs

  - `string name`

    Human-readable name for the environment

  - `"environment" type`

    The type of object (always 'environment')

  - `string updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `?Scope scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

### Beta Environment Delete Response

- `BetaEnvironmentDeleteResponse`

  - `string id`

    Environment identifier

  - `"environment_deleted" type`

    The type of response

### Beta Limited Network

- `BetaLimitedNetwork`

  - `bool allowMCPServers`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

  - `bool allowPackageManagers`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

  - `list<string> allowedHosts`

    Specifies domains the container can reach.

  - `"limited" type`

    Network policy type

### Beta Limited Network Params

- `BetaLimitedNetworkParams`

  - `"limited" type`

    Network policy type

  - `?bool allowMCPServers`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `?bool allowPackageManagers`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `?list<string> allowedHosts`

    Specifies domains the container can reach.

### Beta Packages

- `BetaPackages`

  - `list<string> apt`

    Ubuntu/Debian packages to install

  - `list<string> cargo`

    Rust packages to install

  - `list<string> gem`

    Ruby packages to install

  - `list<string> go`

    Go packages to install

  - `list<string> npm`

    Node.js packages to install

  - `list<string> pip`

    Python packages to install

  - `?Type type`

    Package configuration type

### Beta Packages Params

- `BetaPackagesParams`

  - `?list<string> apt`

    Ubuntu/Debian packages to install

  - `?list<string> cargo`

    Rust packages to install

  - `?list<string> gem`

    Ruby packages to install

  - `?list<string> go`

    Go packages to install

  - `?list<string> npm`

    Node.js packages to install

  - `?list<string> pip`

    Python packages to install

  - `?Type type`

    Package configuration type

### Beta Self Hosted Config

- `BetaSelfHostedConfig`

  - `"self_hosted" type`

    Environment type

### Beta Self Hosted Config Params

- `BetaSelfHostedConfigParams`

  - `"self_hosted" type`

    Environment type

### Beta Unrestricted Network

- `BetaUnrestrictedNetwork`

  - `"unrestricted" type`

    Network policy type

# Work

## Get Work Item

`$client->beta->environments->work->retrieve(string workID, string environmentID, ?list<AnthropicBeta> betas): SelfHostedWork`

**get** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

### Parameters

- `environmentID: string`

- `workID: string`

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

$betaSelfHostedWork = $client->beta->environments->work->retrieve(
  'work_id',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
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
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Poll for Work

`$client->beta->environments->work->poll(string environmentID, ?int blockMs, ?int reclaimOlderThanMs, ?list<AnthropicBeta> betas, ?string anthropicWorkerID): SelfHostedWork`

**get** `/v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

### Parameters

- `environmentID: string`

- `blockMs?:optional int`

  How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

- `reclaimOlderThanMs?:optional int`

  Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `anthropicWorkerID?:optional string`

  Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

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

$betaSelfHostedWork = $client->beta->environments->work->poll(
  'env_011CZkZ9X2dpNyB7HsEFoRfW',
  blockMs: 1,
  reclaimOlderThanMs: 1,
  betas: ['message-batches-2024-09-24'],
  anthropicWorkerID: 'Anthropic-Worker-ID',
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
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## Acknowledge Work

`$client->beta->environments->work->ack(string workID, string environmentID, ?list<AnthropicBeta> betas): SelfHostedWork`

**post** `/v1/environments/{environment_id}/work/{work_id}/ack`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Acknowledge receipt of a work item, transitioning it from 'queued' to 'starting' and removing it from the queue.

### Parameters

- `environmentID: string`

- `workID: string`

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

$betaSelfHostedWork = $client->beta->environments->work->ack(
  'work_id',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
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
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

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

## Stop Work

`$client->beta->environments->work->stop(string workID, string environmentID, ?bool force, ?list<AnthropicBeta> betas): SelfHostedWork`

**post** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

### Parameters

- `environmentID: string`

- `workID: string`

- `force?:optional bool`

  If true, immediately stop work without graceful shutdown

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

$betaSelfHostedWork = $client->beta->environments->work->stop(
  'work_id',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
  force: true,
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
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

## List Work Items

`$client->beta->environments->work->list(string environmentID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<SelfHostedWork>`

**get** `/v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

### Parameters

- `environmentID: string`

- `limit?:optional int`

  Maximum number of work items to return

- `page?:optional string`

  Opaque cursor from previous response for pagination

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

$page = $client->beta->environments->work->list(
  'env_011CZkZ9X2dpNyB7HsEFoRfW',
  limit: 1,
  page: 'page',
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
      "started_at": "started_at",
      "state": "queued",
      "stop_requested_at": "stop_requested_at",
      "stopped_at": "stopped_at",
      "type": "work"
    }
  ],
  "next_page": "next_page"
}
```

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
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

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

## Domain Types

### Beta Self Hosted Work

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

### Beta Self Hosted Work Heartbeat Response

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

### Beta Self Hosted Work List Response

- `SelfHostedWorkListResponse`

  - `list<SelfHostedWork> data`

    List of work items

  - `?string nextPage`

    Opaque cursor for fetching the next page of results

### Beta Self Hosted Work Queue Stats

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

### Beta Self Hosted Work Stop Request

- `SelfHostedWorkStopRequest`

  - `?bool force`

    If true, immediately stop work without graceful shutdown

### Beta Self Hosted Work Update Request

- `SelfHostedWorkUpdateRequest`

  - `array<string,string> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.

### Beta Session Work Data

- `SessionWorkData`

  - `string id`

    Session identifier (e.g., 'session_...')

  - `"session" type`

    Type of work data

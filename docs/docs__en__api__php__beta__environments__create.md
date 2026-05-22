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

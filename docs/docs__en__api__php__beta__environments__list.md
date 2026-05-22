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

## Delete Skill Version

`$client->beta->skills->versions->delete(string version, string skillID, ?list<AnthropicBeta> betas): VersionDeleteResponse`

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `VersionDeleteResponse`

  - `string id`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `string type`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$version = $client->beta->skills->versions->delete(
  'version', skillID: 'skill_id', betas: ['message-batches-2024-09-24']
);

var_dump($version);
```

#### Response

```json
{
  "id": "1759178010641129",
  "type": "type"
}
```

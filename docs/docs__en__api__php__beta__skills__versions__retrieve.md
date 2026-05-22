## Get Skill Version

`$client->beta->skills->versions->retrieve(string version, string skillID, ?list<AnthropicBeta> betas): VersionGetResponse`

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

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

- `VersionGetResponse`

  - `string id`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `string createdAt`

    ISO 8601 timestamp of when the skill version was created.

  - `string description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `string directory`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `string name`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `string skillID`

    Identifier for the skill that this version belongs to.

  - `string type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `string version`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$version = $client->beta->skills->versions->retrieve(
  'version', skillID: 'skill_id', betas: ['message-batches-2024-09-24']
);

var_dump($version);
```

#### Response

```json
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

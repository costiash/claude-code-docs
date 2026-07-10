# Skills

## Create Skill

`$client->beta->skills->create(list<string> files, ?string displayTitle, ?list<AnthropicBeta> betas): SkillNewResponse`

**post** `/v1/skills`

Create Skill

### Parameters

- `files: list<string>`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `displayTitle?:optional string`

  Display title for the skill.

  This is a human-readable label that is not included in the prompt sent to the model.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SkillNewResponse`

  - `string id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `string createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `?string displayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `?string latestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `string source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `string type`

    Object type.

    For Skills, this is always `"skill"`.

  - `string updatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$skill = $client->beta->skills->create(
  files: [
    FileParam::fromString('Example data', filename: uniqid('file-upload-', true)),
  ],
  displayTitle: 'display_title',
  betas: ['message-batches-2024-09-24'],
);

var_dump($skill);
```

#### Response

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

## List Skills

`$client->beta->skills->list(?int limit, ?string page, ?string source, ?list<AnthropicBeta> betas): PageCursor<SkillListResponse>`

**get** `/v1/skills`

List Skills

### Parameters

- `limit?:optional int`

  Number of results to return per page.

  Maximum value is 100. Defaults to 20.

- `page?:optional string`

  Pagination token for fetching a specific page of results.

  Pass the value from a previous response's `next_page` field to get the next page of results.

- `source?:optional string`

  Filter skills by source.

  If provided, only skills from the specified source will be returned:

  * `"custom"`: only return user-created skills
  * `"anthropic"`: only return Anthropic-created skills

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SkillListResponse`

  - `string id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `string createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `?string displayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `?string latestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `string source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `string type`

    Object type.

    For Skills, this is always `"skill"`.

  - `string updatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->skills->list(
  limit: 0,
  page: 'page',
  source: 'source',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_title": "My Custom Skill",
      "latest_version": "1759178010641129",
      "source": "custom",
      "type": "type",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Skill

`$client->beta->skills->retrieve(string skillID, ?list<AnthropicBeta> betas): SkillGetResponse`

**get** `/v1/skills/{skill_id}`

Get Skill

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SkillGetResponse`

  - `string id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `string createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `?string displayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `?string latestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `string source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `string type`

    Object type.

    For Skills, this is always `"skill"`.

  - `string updatedAt`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$skill = $client->beta->skills->retrieve(
  'skill_id', betas: ['message-batches-2024-09-24']
);

var_dump($skill);
```

#### Response

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

## Delete Skill

`$client->beta->skills->delete(string skillID, ?list<AnthropicBeta> betas): SkillDeleteResponse`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `SkillDeleteResponse`

  - `string id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `string type`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$skill = $client->beta->skills->delete(
  'skill_id', betas: ['message-batches-2024-09-24']
);

var_dump($skill);
```

#### Response

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

# Versions

## Create Skill Version

`$client->beta->skills->versions->create(string skillID, list<string> files, ?list<AnthropicBeta> betas): VersionNewResponse`

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `files: list<string>`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `VersionNewResponse`

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

$version = $client->beta->skills->versions->create(
  'skill_id',
  files: [
    FileParam::fromString('Example data', filename: uniqid('file-upload-', true)),
  ],
  betas: ['message-batches-2024-09-24'],
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

## List Skill Versions

`$client->beta->skills->versions->list(string skillID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<VersionListResponse>`

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `limit?:optional int`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `page?:optional string`

  Optionally set to the `next_page` token from the previous response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `VersionListResponse`

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

$page = $client->beta->skills->versions->list(
  'skill_id', limit: 0, page: 'page', betas: ['message-batches-2024-09-24']
);

var_dump($page);
```

#### Response

```json
{
  "data": [
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
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Download Skill Version Content

`$client->beta->skills->versions->download(string version, string skillID, ?list<AnthropicBeta> betas): download`

**get** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

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

- `mixed`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$response = $client->beta->skills->versions->download(
  'version', skillID: 'skill_id', betas: ['message-batches-2024-09-24']
);

var_dump($response);
```

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

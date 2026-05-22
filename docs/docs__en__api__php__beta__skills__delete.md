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

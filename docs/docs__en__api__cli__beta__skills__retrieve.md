## Retrieve

`$ ant beta:skills retrieve`

**get** `/v1/skills/{skill_id}`

Get Skill

### Parameters

- `--skill-id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSkillGetResponse: object { id, created_at, display_title, 4 more }`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: string`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: string`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: string`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: string`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: string`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```cli
ant beta:skills retrieve \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
```

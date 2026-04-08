## Retrieve

`$ ant beta:skills:versions retrieve`

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--version: string`

  Path param: Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSkillVersionGetResponse: object { id, created_at, description, 5 more }`

  - `id: string`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill version was created.

  - `description: string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: string`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: string`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: string`

    Identifier for the skill that this version belongs to.

  - `type: string`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```cli
ant beta:skills:versions retrieve \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --version version
```

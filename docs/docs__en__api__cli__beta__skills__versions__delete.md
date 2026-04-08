## Delete

`$ ant beta:skills:versions delete`

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

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

- `BetaSkillVersionDeleteResponse: object { id, type }`

  - `id: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `type: string`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```cli
ant beta:skills:versions delete \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --version version
```

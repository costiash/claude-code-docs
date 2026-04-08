# Skills

## Create

`$ ant beta:skills create`

**post** `/v1/skills`

Create Skill

### Parameters

- `--display-title: optional string`

  Body param: Display title for the skill.

  This is a human-readable label that is not included in the prompt sent to the model.

- `--file: optional array of string`

  Body param: Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSkillNewResponse: object { id, created_at, display_title, 4 more }`

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
ant beta:skills create \
  --api-key my-anthropic-api-key
```

## List

`$ ant beta:skills list`

**get** `/v1/skills`

List Skills

### Parameters

- `--limit: optional number`

  Query param: Number of results to return per page.

  Maximum value is 100. Defaults to 20.

- `--page: optional string`

  Query param: Pagination token for fetching a specific page of results.

  Pass the value from a previous response's `next_page` field to get the next page of results.

- `--source: optional string`

  Query param: Filter skills by source.

  If provided, only skills from the specified source will be returned:

  * `"custom"`: only return user-created skills
  * `"anthropic"`: only return Anthropic-created skills

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaListSkillsResponse: object { data, has_more, next_page }`

  - `data: array of object { id, created_at, display_title, 4 more }`

    List of skills.

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

  - `has_more: boolean`

    Whether there are more results available.

    If `true`, there are additional results that can be fetched using the `next_page` token.

  - `next_page: string`

    Token for fetching the next page of results.

    If `null`, there are no more results available. Pass this value to the `page_token` parameter in the next request to get the next page.

### Example

```cli
ant beta:skills list \
  --api-key my-anthropic-api-key
```

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

## Delete

`$ ant beta:skills delete`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `--skill-id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSkillDeleteResponse: object { id, type }`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: string`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```cli
ant beta:skills delete \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
```

# Versions

## Create

`$ ant beta:skills:versions create`

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--file: optional array of string`

  Body param: Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSkillVersionNewResponse: object { id, created_at, description, 5 more }`

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
ant beta:skills:versions create \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
```

## List

`$ ant beta:skills:versions list`

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `--page: optional string`

  Query param: Optionally set to the `next_page` token from the previous response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaListSkillVersionsResponse: object { data, has_more, next_page }`

  - `data: array of object { id, created_at, description, 5 more }`

    List of skill versions.

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

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```cli
ant beta:skills:versions list \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
```

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

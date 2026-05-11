# Model IDs and versioning

How Claude model IDs are structured and versioned, including the dateless format introduced with the Claude 4.6 generation and what it means for stability.

---

Each Claude model ID identifies a pinned version of the model. When you use a model ID in an API request, the underlying model remains constant for the lifetime of that ID. This guarantee covers model IDs, not the convenience aliases that the Claude API accepts for some earlier models (see [Before the 4.6 generation](#before-the-4-6-generation)).

## Model ID format

Claude model IDs follow a versioned naming scheme.

### The 4.6 generation and later

Starting with the Claude 4.6 generation, model IDs use a dateless format:

```text
claude-{name}-{major}-{minor}
```

For example: `claude-sonnet-4-6`, `claude-opus-4-6`, and `claude-opus-4-7`

On Amazon Bedrock, the corresponding format is:

```text
anthropic.claude-{name}-{major}-{minor}
```

For example: `anthropic.claude-sonnet-4-6`, `anthropic.claude-opus-4-7`

Claude Opus 4.6 is the last Bedrock model ID to include the `-v1` suffix (`anthropic.claude-opus-4-6-v1`). Anthropic dropped the suffix starting with Claude Sonnet 4.6.

On Google Cloud Vertex AI, the format matches the Claude API.

### Before the 4.6 generation

Models before the 4.6 generation include a snapshot date in the ID:

```text
claude-{name}-{major}-{minor}-{YYYYMMDD}
```

For example: `claude-sonnet-4-5-20250929`, `claude-haiku-4-5-20251001`

On Amazon Bedrock, these use the format:

```text
anthropic.claude-{name}-{major}-{minor}-{YYYYMMDD}-v1:0
```

For example: `anthropic.claude-sonnet-4-5-20250929-v1:0`

On Google Cloud Vertex AI, the date is separated with `@`:

```text
claude-{name}-{major}-{minor}@{YYYYMMDD}
```

For example: `claude-haiku-4-5@20251001`

On the Claude API, these models also have shorter aliases (for example, `claude-sonnet-4-5`) that point to the most recent dated snapshot for that minor version.

## Dateless IDs are pinned snapshots

A common misconception is that dateless model IDs such as `claude-sonnet-4-6` behave as evergreen pointers that route to the latest or best-performing version. That is not the case.

For the 4.6 generation and later, the dateless ID is the canonical model ID for that release. It maps to a single, fixed model snapshot. Anthropic does not update the weights or configuration of an existing model ID. When an updated version is available, it ships under a new model ID.

This differs from the dateless aliases that exist on the Claude API for earlier models. An alias such as `claude-sonnet-4-5` is a convenience pointer that resolves to the most recent dated snapshot for that minor version. A 4.6-generation ID such as `claude-sonnet-4-6` is not an alias. It is the snapshot.

Every model ID, whether dated or dateless, has its own distinct deprecation and retirement schedule.

## Model weights versus serving infrastructure

Model weights are fixed for a given ID, but the serving infrastructure around the model can change over time. This infrastructure includes components such as the request router, safety classifiers, and sampling logic.

Occasionally, infrastructure updates produce minor differences in observable behavior even when the model ID and weights have not changed. If you notice unexpected behavioral differences on a previously stable model ID, an infrastructure update is the most likely cause.

## Current model IDs

For the full list of current model IDs and their Amazon Bedrock and Google Cloud Vertex AI equivalents, see [Models overview](/docs/en/about-claude/models/overview).
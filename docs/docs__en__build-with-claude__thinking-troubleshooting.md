# Troubleshooting thinking

Diagnose and fix the most common thinking failures: configuration 400 errors, empty or missing thinking blocks, max_tokens stops, and cache misses.

---

<Note>
  For how zero data retention (ZDR) applies to this feature, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).
</Note>

This page covers the most common failures when configuring thinking or round-tripping thinking blocks (sending returned thinking blocks back in later requests). The first section maps each model to its supported thinking configurations and the ones it rejects; the sections after it each start from a symptom you observe, so you can match an error message or unexpected response directly to its cause and fix. For how thinking works, see the [Thinking](/docs/en/build-with-claude/thinking) overview.

## Configurations each model rejects

Most thinking configuration errors are a mismatch between the `thinking.type` value in the request and what the model supports. On current models, thinking runs as `thinking: {type: "adaptive"}`, and on the newest it is on by default. Some earlier models instead use [extended thinking](/docs/en/build-with-claude/extended-thinking), a legacy manual mode configured as `thinking: {type: "enabled", budget_tokens: N}`.

Extended thinking (`thinking.type: "enabled"` with `budget_tokens`) is deprecated on Claude Opus 4.6 and Claude Sonnet 4.6 (it still works there). Claude Opus 4.7, Claude Opus 4.8, Claude Sonnet 5, Claude Fable 5, and Claude Mythos 5 do not support it and reject requests that use it, returning a 400 error. On earlier models, including Claude Sonnet 4.5, Claude Opus 4.5, and Claude Haiku 4.5, extended thinking is the only thinking mode. Claude Mythos Preview supports both modes. Where both modes are available, use [adaptive thinking](/docs/en/build-with-claude/thinking-steering-and-cost) instead.

The table lists what each model supports, what it defaults to, and which `thinking.type` values it rejects with a 400 error; any value not listed as rejected is accepted.

| Model                        | Thinking types                   | Default   | Rejected with 400         |
| ---------------------------- | -------------------------------- | --------- | ------------------------- |
| Claude Fable 5               | Adaptive only                    | Always on | `"enabled"`, `"disabled"` |
| Claude Mythos 5              | Adaptive only                    | Always on | `"enabled"`, `"disabled"` |
| Claude Mythos Preview        | Adaptive, extended               | Always on | `"disabled"`              |
| Claude Opus 4.8              | Adaptive only                    | Off       | `"enabled"`               |
| Claude Opus 4.7              | Adaptive only                    | Off       | `"enabled"`               |
| Claude Sonnet 5              | Adaptive only                    | On        | `"enabled"`               |
| Claude Opus 4.6              | Adaptive, extended (deprecated)1 | Off       | None                      |
| Claude Sonnet 4.6            | Adaptive, extended (deprecated)1 | Off       | None                      |
| Claude Opus 4.5              | Extended only                    | Off       | `"adaptive"`              |
| Claude Haiku 4.5             | Extended only                    | Off       | `"adaptive"`              |
| Claude Sonnet 4.5            | Extended only                    | Off       | `"adaptive"`              |
| Claude Opus 4.1 (deprecated) | Extended only                    | Off       | `"adaptive"`              |

*1 `enabled` and `budget_tokens` still work on these models but are deprecated; use adaptive thinking instead.*

Models marked `Always on` cannot turn thinking off. Models marked `On` default to thinking but accept `thinking: {type: "disabled"}`.

Earlier Claude 4 models (Claude Sonnet 4 and Claude Opus 4) support extended thinking only; see [model deprecations](/docs/en/about-claude/model-deprecations) for their availability. Claude Fable 5 and Claude Mythos 5 are not available under [zero data retention](/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements).

## A 400 error says `"thinking.type.enabled"` is not supported

The request fails with a 400 error whose message reads:

```text wrap
"thinking.type.enabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```

This happens because the model you requested has removed extended thinking (see [Configurations each model rejects](#rejected-configurations)).

Switch the request to `thinking: {type: "adaptive"}` and steer thinking depth with `effort` instead of `budget_tokens`. [Migrating to adaptive thinking](/docs/en/build-with-claude/extended-thinking#migrating-to-adaptive-thinking) walks through the conversion.

## A 400 error says `"thinking.type.disabled"` is not supported

The request fails with a 400 error whose message reads:

```text wrap
"thinking.type.disabled" is not supported for this model. Thinking defaults to adaptive mode when not specified; use "thinking.type.enabled" with "budget_tokens" for extended thinking.
```

This happens on models where thinking is always on: Claude Fable 5, Claude Mythos 5, and Claude Mythos Preview reject `"disabled"`. On Claude Fable 5 and Claude Mythos 5, the error text's suggestion of `"thinking.type.enabled"` does not apply either: those models reject it too.

Omit the `thinking` parameter; these models think without any configuration. If your goal was to keep thinking text out of responses, use `display: "omitted"` instead of disabling thinking; see [Controlling thinking display](/docs/en/build-with-claude/thinking#controlling-thinking-display).

## A 400 error says adaptive thinking is not supported

The request fails with a 400 error whose message reads:

```text wrap
adaptive thinking is not supported on this model
```

This happens because the model supports only extended thinking (see [Configurations each model rejects](#rejected-configurations)).

Use `thinking: {type: "enabled", budget_tokens: N}` instead; see [Extended thinking](/docs/en/build-with-claude/extended-thinking) for the configuration.

## A 400 error says thinking blocks cannot be modified

A request that returns tool results fails with a 400 `invalid_request_error` whose message contains:

```text wrap
`thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified
```

In multi-turn and tool-use conversations you send previous assistant messages, including their `thinking` and `redacted_thinking` blocks, back to the API, and the API verifies they arrive unmodified. This error happens when the assistant message you send back differs from the one the API returned, most often because your code filters content blocks by type and drops `redacted_thinking` blocks, or rebuilds the assistant message instead of echoing it.

Echo the assistant turn back verbatim, thinking blocks included. See [Preserving thinking blocks](/docs/en/build-with-claude/thinking#preserving-thinking-blocks) for the rules, and the worked round trip in [Thinking in tool and multi-turn workflows](/docs/en/build-with-claude/thinking-tool-workflows#two-turn-tool-use-round-trip) for correct code in every SDK.

## The thinking field is empty in the response

The response contains `thinking` blocks, but their `thinking` field is an empty string and only the `signature` field is populated.

This happens because `display` defaults to `"omitted"` on newer models, which returns thinking blocks without their text.

Set `display: "summarized"` in your thinking configuration to receive the summarized thinking text; see [Controlling thinking display](/docs/en/build-with-claude/thinking#controlling-thinking-display) for the defaults per model.

## No thinking block appears on some turns

Some responses contain no `thinking` block at all, even though thinking is configured.

This is normal in adaptive mode: Claude skips thinking on requests it judges simple enough to answer directly.

If you want thinking more often or more deeply, raise `effort` or steer with prompting; see [Steering how often Claude thinks](/docs/en/build-with-claude/thinking-steering-and-cost#tuning-thinking-behavior).

## The response stops with `stop_reason: "max_tokens"`

The response ends with `stop_reason: "max_tokens"`, often with a truncated or missing text block.

This happens because thinking tokens count toward `max_tokens`, so a long thinking pass can consume the budget before the text response completes.

Raise `max_tokens` to leave room for both thinking and text, or lower `effort` so Claude spends less on thinking; see [Cost control](/docs/en/build-with-claude/thinking-steering-and-cost#cost-control) and [Thinking and the context window](/docs/en/build-with-claude/thinking#thinking-and-the-context-window).

## Cache hits drop after changing thinking settings

`cache_read_input_tokens` falls to zero on requests that previously hit the cache.

This happens because the thinking configuration and the effort level (or its default) are part of the cached prompt prefix, so changing any of them starts a new prefix: switching thinking modes, changing the effort value, and changing `budget_tokens` all invalidate message cache breakpoints, and can invalidate tool and system-prompt breakpoints too, depending on where the model renders the configuration.

Keep the thinking configuration and effort level constant across requests that share a conversation; setting a parameter explicitly to its default is equivalent to omitting it and does not invalidate. See [Thinking and prompt caching](/docs/en/build-with-claude/thinking#thinking-and-prompt-caching).

## Setting effort does not change thinking

You change `effort` but thinking frequency or depth stays the same.

This happens because effort is the primary thinking lever only in adaptive mode. On extended-thinking-only models, thinking depth is set by `budget_tokens` instead.

Adjust `budget_tokens` on those models, or check which mode your model runs in; see [Thinking and effort](/docs/en/build-with-claude/thinking#thinking-and-effort). On Claude Opus 4.5, the one extended-thinking-only model that supports effort, effort composes with the budget; see [Budget rules and tuning](/docs/en/build-with-claude/extended-thinking#budget-rules-and-tuning).

## Next steps

<CardGroup cols={3}>
  <Card title="Thinking" icon="brain" href="/docs/en/build-with-claude/thinking">
    The overview: what thinking is, how to configure it, and how it interacts with tools, caching, and streaming.
  </Card>

  <Card title="Errors" icon="book" href="/docs/en/api/errors">
    The full error reference, including the thinking configuration 400s with their exact server messages.
  </Card>

  <Card title="Migrating to adaptive thinking" icon="arrow-right" href="/docs/en/build-with-claude/extended-thinking#migrating-to-adaptive-thinking">
    Convert `budget_tokens` requests to adaptive thinking with effort.
  </Card>
</CardGroup>

# Completions

## Create

`$ ant completions create`

**post** `/v1/complete`

[Legacy] Create a Text Completion.

The Text Completions API is a legacy API. We recommend using the [Messages API](https://docs.claude.com/en/api/messages) going forward.

Future models and features will not be compatible with Text Completions. See our [migration guide](https://docs.claude.com/en/api/migrating-from-text-completions-to-messages) for guidance in migrating from Text Completions to Messages.

### Parameters

- `--max-tokens-to-sample: number`

  Body param: The maximum number of tokens to generate before stopping.

  Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

- `--model: "claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more or string`

  Body param: The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `--prompt: string`

  Body param: The prompt that you want Claude to complete.

  For proper response generation you will need to format your prompt using alternating `

  Human:`and`

  Assistant:` conversational turns. For example:

  ```
  "
  
  Human: {userQuestion}
  
  Assistant:"
  ```

  See [prompt validation](https://docs.claude.com/en/api/prompt-validation) and our guide to [prompt design](https://docs.claude.com/en/docs/intro-to-prompting) for more details.

- `--metadata: optional object { user_id }`

  Body param: An object describing metadata about the request.

- `--stop-sequence: optional array of string`

  Body param: Sequences that will cause the model to stop generating.

  Our models stop on `"

  Human:"`, and may include additional built-in stop sequences in the future. By providing the stop_sequences parameter, you may include additional strings that will cause the model to stop generating.

- `--temperature: optional number`

  Body param: Amount of randomness injected into the response.

  Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

  Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

- `--top-k: optional number`

  Body param: Only sample from the top K options for each subsequent token.

  Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

  Recommended for advanced use cases only. You usually only need to use `temperature`.

- `--top-p: optional number`

  Body param: Use nucleus sampling.

  In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

  Recommended for advanced use cases only. You usually only need to use `temperature`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `completion: object { id, completion, model, 2 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `completion: string`

    The resulting completion up to and excluding the stop sequences.

  - `model: "claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more or string`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-opus-4-7"`

      Frontier intelligence for long-running agents and coding

    - `"claude-mythos-preview"`

      New class of intelligence, strongest in coding and cybersecurity

    - `"claude-opus-4-6"`

      Frontier intelligence for long-running agents and coding

    - `"claude-sonnet-4-6"`

      Best combination of speed and intelligence

    - `"claude-haiku-4-5"`

      Fastest model with near-frontier intelligence

    - `"claude-haiku-4-5-20251001"`

      Fastest model with near-frontier intelligence

    - `"claude-opus-4-5"`

      Premium model combining maximum intelligence with practical performance

    - `"claude-opus-4-5-20251101"`

      Premium model combining maximum intelligence with practical performance

    - `"claude-sonnet-4-5"`

      High-performance model for agents and coding

    - `"claude-sonnet-4-5-20250929"`

      High-performance model for agents and coding

    - `"claude-opus-4-1"`

      Exceptional model for specialized complex tasks

    - `"claude-opus-4-1-20250805"`

      Exceptional model for specialized complex tasks

    - `"claude-opus-4-0"`

      Powerful model for complex tasks

    - `"claude-opus-4-20250514"`

      Powerful model for complex tasks

    - `"claude-sonnet-4-0"`

      High-performance model with extended thinking

    - `"claude-sonnet-4-20250514"`

      High-performance model with extended thinking

    - `"claude-3-haiku-20240307"`

      Fast and cost-effective model

  - `stop_reason: string`

    The reason that we stopped.

    This may be one the following values:

    * `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
    * `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

  - `type: "completion"`

    Object type.

    For Text Completions, this is always `"completion"`.

### Example

```cli
ant completions create \
  --api-key my-anthropic-api-key \
  --max-tokens-to-sample 256 \
  --model claude-opus-4-7 \
  --prompt '

Human: Hello, world!

Assistant:'
```

## Domain Types

### Completion

- `completion: object { id, completion, model, 2 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `completion: string`

    The resulting completion up to and excluding the stop sequences.

  - `model: "claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more or string`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-opus-4-7"`

      Frontier intelligence for long-running agents and coding

    - `"claude-mythos-preview"`

      New class of intelligence, strongest in coding and cybersecurity

    - `"claude-opus-4-6"`

      Frontier intelligence for long-running agents and coding

    - `"claude-sonnet-4-6"`

      Best combination of speed and intelligence

    - `"claude-haiku-4-5"`

      Fastest model with near-frontier intelligence

    - `"claude-haiku-4-5-20251001"`

      Fastest model with near-frontier intelligence

    - `"claude-opus-4-5"`

      Premium model combining maximum intelligence with practical performance

    - `"claude-opus-4-5-20251101"`

      Premium model combining maximum intelligence with practical performance

    - `"claude-sonnet-4-5"`

      High-performance model for agents and coding

    - `"claude-sonnet-4-5-20250929"`

      High-performance model for agents and coding

    - `"claude-opus-4-1"`

      Exceptional model for specialized complex tasks

    - `"claude-opus-4-1-20250805"`

      Exceptional model for specialized complex tasks

    - `"claude-opus-4-0"`

      Powerful model for complex tasks

    - `"claude-opus-4-20250514"`

      Powerful model for complex tasks

    - `"claude-sonnet-4-0"`

      High-performance model with extended thinking

    - `"claude-sonnet-4-20250514"`

      High-performance model with extended thinking

    - `"claude-3-haiku-20240307"`

      Fast and cost-effective model

  - `stop_reason: string`

    The reason that we stopped.

    This may be one the following values:

    * `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
    * `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

  - `type: "completion"`

    Object type.

    For Text Completions, this is always `"completion"`.

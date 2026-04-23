# Completions

## Create

`client.completions.create(CompletionCreateParamsparams, RequestOptionsoptions?): Completion | Stream<Completion>`

**post** `/v1/complete`

[Legacy] Create a Text Completion.

The Text Completions API is a legacy API. We recommend using the [Messages API](https://docs.claude.com/en/api/messages) going forward.

Future models and features will not be compatible with Text Completions. See our [migration guide](https://docs.claude.com/en/api/migrating-from-text-completions-to-messages) for guidance in migrating from Text Completions to Messages.

### Parameters

- `CompletionCreateParams = CompletionCreateParamsNonStreaming | CompletionCreateParamsStreaming`

  - `CompletionCreateParamsBase`

    - `max_tokens_to_sample: number`

      Body param: The maximum number of tokens to generate before stopping.

      Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

    - `model: Model`

      Body param: The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-7" | "claude-mythos-preview" | "claude-opus-4-6" | 14 more`

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

      - `(string & {})`

    - `prompt: string`

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

    - `metadata?: Metadata`

      Body param: An object describing metadata about the request.

      - `user_id?: string | null`

        An external identifier for the user who is associated with the request.

        This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

    - `stop_sequences?: Array<string>`

      Body param: Sequences that will cause the model to stop generating.

      Our models stop on `"

      Human:"`, and may include additional built-in stop sequences in the future. By providing the stop_sequences parameter, you may include additional strings that will cause the model to stop generating.

    - `stream?: false`

      Body param: Whether to incrementally stream the response using server-sent events.

      See [streaming](https://docs.claude.com/en/api/streaming) for details.

      - `false`

    - `temperature?: number`

      Body param: Amount of randomness injected into the response.

      Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

      Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

    - `top_k?: number`

      Body param: Only sample from the top K options for each subsequent token.

      Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

      Recommended for advanced use cases only.

    - `top_p?: number`

      Body param: Use nucleus sampling.

      In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

      Recommended for advanced use cases only.

    - `betas?: Array<AnthropicBeta>`

      Header param: Optional header to specify the beta version(s) you want to use.

      - `(string & {})`

      - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

        - `"message-batches-2024-09-24"`

        - `"prompt-caching-2024-07-31"`

        - `"computer-use-2024-10-22"`

        - `"computer-use-2025-01-24"`

        - `"pdfs-2024-09-25"`

        - `"token-counting-2024-11-01"`

        - `"token-efficient-tools-2025-02-19"`

        - `"output-128k-2025-02-19"`

        - `"files-api-2025-04-14"`

        - `"mcp-client-2025-04-04"`

        - `"mcp-client-2025-11-20"`

        - `"dev-full-thinking-2025-05-14"`

        - `"interleaved-thinking-2025-05-14"`

        - `"code-execution-2025-05-22"`

        - `"extended-cache-ttl-2025-04-11"`

        - `"context-1m-2025-08-07"`

        - `"context-management-2025-06-27"`

        - `"model-context-window-exceeded-2025-08-26"`

        - `"skills-2025-10-02"`

        - `"fast-mode-2026-02-01"`

        - `"output-300k-2026-03-24"`

        - `"advisor-tool-2026-03-01"`

  - `CompletionCreateParamsNonStreaming extends CompletionCreateParamsBase`

    - `stream?: false`

      Body param: Whether to incrementally stream the response using server-sent events.

      See [streaming](https://docs.claude.com/en/api/streaming) for details.

      - `false`

  - `CompletionCreateParamsStreaming extends CompletionCreateParamsBase`

    - `stream: true`

      Body param: Whether to incrementally stream the response using server-sent events.

      See [streaming](https://docs.claude.com/en/api/streaming) for details.

      - `true`

### Returns

- `Completion`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `completion: string`

    The resulting completion up to and excluding the stop sequences.

  - `model: Model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-opus-4-7" | "claude-mythos-preview" | "claude-opus-4-6" | 14 more`

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

    - `(string & {})`

  - `stop_reason: string | null`

    The reason that we stopped.

    This may be one the following values:

    * `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
    * `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

  - `type: "completion"`

    Object type.

    For Text Completions, this is always `"completion"`.

    - `"completion"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const completion = await client.completions.create({
  max_tokens_to_sample: 256,
  model: 'claude-2.1',
  prompt: '\n\nHuman: Hello, world!\n\nAssistant:',
});

console.log(completion.id);
```

## Domain Types

### Completion

- `Completion`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `completion: string`

    The resulting completion up to and excluding the stop sequences.

  - `model: Model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-opus-4-7" | "claude-mythos-preview" | "claude-opus-4-6" | 14 more`

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

    - `(string & {})`

  - `stop_reason: string | null`

    The reason that we stopped.

    This may be one the following values:

    * `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
    * `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

  - `type: "completion"`

    Object type.

    For Text Completions, this is always `"completion"`.

    - `"completion"`

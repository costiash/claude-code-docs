# Batches

## Create a Message Batch

`$ ant beta:messages:batches create`

**post** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--request: array of object { custom_id, params }`

  Body param: List of requests for prompt completion. Each is an individual request to create a Message.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_message_batch: object { id, archived_at, cancel_initiated_at, 7 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object { canceled, errored, expired, 2 more }`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```cli
ant beta:messages:batches create \
  --api-key my-anthropic-api-key \
  --request '{custom_id: my-custom-id-1, params: {max_tokens: 1024, messages: [{content: [{text: x, type: text}], role: user}], model: claude-opus-4-6}}'
```

#### Response

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

## Retrieve a Message Batch

`$ ant beta:messages:batches retrieve`

**get** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_message_batch: object { id, archived_at, cancel_initiated_at, 7 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object { canceled, errored, expired, 2 more }`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```cli
ant beta:messages:batches retrieve \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

#### Response

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

## List Message Batches

`$ ant beta:messages:batches list`

**get** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--after-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaListResponse_MessageBatch_: object { data, first_id, has_more, last_id }`

  - `data: array of BetaMessageBatch`

    - `id: string`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `archived_at: string`

      RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    - `cancel_initiated_at: string`

      RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    - `created_at: string`

      RFC 3339 datetime string representing the time at which the Message Batch was created.

    - `ended_at: string`

      RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

      Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    - `expires_at: string`

      RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    - `processing_status: "in_progress" or "canceling" or "ended"`

      Processing status of the Message Batch.

      - `"in_progress"`

      - `"canceling"`

      - `"ended"`

    - `request_counts: object { canceled, errored, expired, 2 more }`

      Tallies requests within the Message Batch, categorized by their status.

      Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

      - `canceled: number`

        Number of requests in the Message Batch that have been canceled.

        This is zero until processing of the entire Message Batch has ended.

      - `errored: number`

        Number of requests in the Message Batch that encountered an error.

        This is zero until processing of the entire Message Batch has ended.

      - `expired: number`

        Number of requests in the Message Batch that have expired.

        This is zero until processing of the entire Message Batch has ended.

      - `processing: number`

        Number of requests in the Message Batch that are processing.

      - `succeeded: number`

        Number of requests in the Message Batch that have completed successfully.

        This is zero until processing of the entire Message Batch has ended.

    - `results_url: string`

      URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

      Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

    - `type: "message_batch"`

      Object type.

      For Message Batches, this is always `"message_batch"`.

  - `first_id: string`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `last_id: string`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```cli
ant beta:messages:batches list \
  --api-key my-anthropic-api-key
```

#### Response

```json
{
  "data": [
    {
      "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
      "archived_at": "2024-08-20T18:37:24.100435Z",
      "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
      "created_at": "2024-08-20T18:37:24.100435Z",
      "ended_at": "2024-08-20T18:37:24.100435Z",
      "expires_at": "2024-08-20T18:37:24.100435Z",
      "processing_status": "in_progress",
      "request_counts": {
        "canceled": 10,
        "errored": 30,
        "expired": 10,
        "processing": 100,
        "succeeded": 50
      },
      "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
      "type": "message_batch"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Cancel a Message Batch

`$ ant beta:messages:batches cancel`

**post** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_message_batch: object { id, archived_at, cancel_initiated_at, 7 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object { canceled, errored, expired, 2 more }`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```cli
ant beta:messages:batches cancel \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

#### Response

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

## Delete a Message Batch

`$ ant beta:messages:batches delete`

**delete** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_deleted_message_batch: object { id, type }`

  - `id: string`

    ID of the Message Batch.

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Example

```cli
ant beta:messages:batches delete \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

#### Response

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

## Retrieve Message Batch results

`$ ant beta:messages:batches results`

**get** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_message_batch_individual_response: object { custom_id, result }`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `custom_id: string`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `result: BetaMessageBatchSucceededResult or BetaMessageBatchErroredResult or BetaMessageBatchCanceledResult or BetaMessageBatchExpiredResult`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `beta_message_batch_succeeded_result: object { message, type }`

      - `message: object { id, container, content, 9 more }`

        - `id: string`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `container: object { id, expires_at, skills }`

          Information about the container used in the request (for the code execution tool)

          - `id: string`

            Identifier for the container used in this request

          - `expires_at: string`

            The time at which the container will expire.

          - `skills: array of BetaSkill`

            Skills loaded in the container

            - `skill_id: string`

              Skill ID

            - `type: "anthropic" or "custom"`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `"anthropic"`

              - `"custom"`

            - `version: string`

              Skill version or 'latest' for most recent version

        - `content: array of BetaContentBlock`

          Content generated by the model.

          This is an array of content blocks, each of which has a `type` that determines its shape.

          Example:

          ```json
          [{"type": "text", "text": "Hi, I'm Claude."}]
          ```

          If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

          For example, if the input `messages` were:

          ```json
          [
            {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
            {"role": "assistant", "content": "The best answer is ("}
          ]
          ```

          Then the response `content` might be:

          ```json
          [{"type": "text", "text": "B)"}]
          ```

          - `beta_text_block: object { citations, text, type }`

            - `citations: array of BetaTextCitation`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `beta_citation_char_location: object { cited_text, document_index, document_title, 4 more }`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string`

                - `end_char_index: number`

                - `file_id: string`

                - `start_char_index: number`

                - `type: "char_location"`

              - `beta_citation_page_location: object { cited_text, document_index, document_title, 4 more }`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string`

                - `end_page_number: number`

                - `file_id: string`

                - `start_page_number: number`

                - `type: "page_location"`

              - `beta_citation_content_block_location: object { cited_text, document_index, document_title, 4 more }`

                - `cited_text: string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `document_index: number`

                - `document_title: string`

                - `end_block_index: number`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `file_id: string`

                - `start_block_index: number`

                  0-based index of the first cited block in the source's `content` array.

                - `type: "content_block_location"`

              - `beta_citations_web_search_result_location: object { cited_text, encrypted_index, title, 2 more }`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string`

                - `type: "web_search_result_location"`

                - `url: string`

              - `beta_citation_search_result_location: object { cited_text, end_block_index, search_result_index, 4 more }`

                - `cited_text: string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `end_block_index: number`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `search_result_index: number`

                  0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                  Counted separately from `document_index`; server-side web search results are not included in this count.

                - `source: string`

                - `start_block_index: number`

                  0-based index of the first cited block in the source's `content` array.

                - `title: string`

                - `type: "search_result_location"`

            - `text: string`

            - `type: "text"`

          - `beta_thinking_block: object { signature, thinking, type }`

            - `signature: string`

            - `thinking: string`

            - `type: "thinking"`

          - `beta_redacted_thinking_block: object { data, type }`

            - `data: string`

            - `type: "redacted_thinking"`

          - `beta_tool_use_block: object { id, input, name, 2 more }`

            - `id: string`

            - `input: map[unknown]`

            - `name: string`

            - `type: "tool_use"`

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              Tool invocation directly from the model.

              - `beta_direct_caller: object { type }`

                Tool invocation directly from the model.

                - `type: "direct"`

              - `beta_server_tool_caller: object { tool_id, type }`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

              - `beta_server_tool_caller_20260120: object { tool_id, type }`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

          - `beta_server_tool_use_block: object { id, input, name, 2 more }`

            - `id: string`

            - `input: map[unknown]`

            - `name: "advisor" or "web_search" or "web_fetch" or 5 more`

              - `"advisor"`

              - `"web_search"`

              - `"web_fetch"`

              - `"code_execution"`

              - `"bash_code_execution"`

              - `"text_editor_code_execution"`

              - `"tool_search_tool_regex"`

              - `"tool_search_tool_bm25"`

            - `type: "server_tool_use"`

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              Tool invocation directly from the model.

              - `beta_direct_caller: object { type }`

                Tool invocation directly from the model.

              - `beta_server_tool_caller: object { tool_id, type }`

                Tool invocation generated by a server-side tool.

              - `beta_server_tool_caller_20260120: object { tool_id, type }`

          - `beta_web_search_tool_result_block: object { content, tool_use_id, type, caller }`

            - `content: BetaWebSearchToolResultError or array of BetaWebSearchResultBlock`

              - `beta_web_search_tool_result_error: object { error_code, type }`

                - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"max_uses_exceeded"`

                  - `"too_many_requests"`

                  - `"query_too_long"`

                  - `"request_too_large"`

                - `type: "web_search_tool_result_error"`

              - `union_member_1: array of BetaWebSearchResultBlock`

                - `encrypted_content: string`

                - `page_age: string`

                - `title: string`

                - `type: "web_search_result"`

                - `url: string`

            - `tool_use_id: string`

            - `type: "web_search_tool_result"`

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              Tool invocation directly from the model.

              - `beta_direct_caller: object { type }`

                Tool invocation directly from the model.

              - `beta_server_tool_caller: object { tool_id, type }`

                Tool invocation generated by a server-side tool.

              - `beta_server_tool_caller_20260120: object { tool_id, type }`

          - `beta_web_fetch_tool_result_block: object { content, tool_use_id, type, caller }`

            - `content: BetaWebFetchToolResultErrorBlock or BetaWebFetchBlock`

              - `beta_web_fetch_tool_result_error_block: object { error_code, type }`

                - `error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 6 more`

                  - `"invalid_tool_input"`

                  - `"url_too_long"`

                  - `"url_not_allowed"`

                  - `"url_not_in_prior_context"`

                  - `"url_not_accessible"`

                  - `"unsupported_content_type"`

                  - `"too_many_requests"`

                  - `"max_uses_exceeded"`

                  - `"unavailable"`

                - `type: "web_fetch_tool_result_error"`

              - `beta_web_fetch_block: object { content, retrieved_at, type, url }`

                - `content: object { citations, source, title, type }`

                  - `citations: object { enabled }`

                    Citation configuration for the document

                    - `enabled: boolean`

                  - `source: BetaBase64PDFSource or BetaPlainTextSource`

                    - `beta_base64_pdf_source: object { data, media_type, type }`

                      - `data: string`

                      - `media_type: "application/pdf"`

                      - `type: "base64"`

                    - `beta_plain_text_source: object { data, media_type, type }`

                      - `data: string`

                      - `media_type: "text/plain"`

                      - `type: "text"`

                  - `title: string`

                    The title of the document

                  - `type: "document"`

                - `retrieved_at: string`

                  ISO 8601 timestamp when the content was retrieved

                - `type: "web_fetch_result"`

                - `url: string`

                  Fetched content URL

            - `tool_use_id: string`

            - `type: "web_fetch_tool_result"`

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              Tool invocation directly from the model.

              - `beta_direct_caller: object { type }`

                Tool invocation directly from the model.

              - `beta_server_tool_caller: object { tool_id, type }`

                Tool invocation generated by a server-side tool.

              - `beta_server_tool_caller_20260120: object { tool_id, type }`

          - `beta_advisor_tool_result_block: object { content, tool_use_id, type }`

            - `content: BetaAdvisorToolResultError or BetaAdvisorResultBlock or BetaAdvisorRedactedResultBlock`

              - `beta_advisor_tool_result_error: object { error_code, type }`

                - `error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 4 more`

                  - `"max_uses_exceeded"`

                  - `"prompt_too_long"`

                  - `"too_many_requests"`

                  - `"overloaded"`

                  - `"unavailable"`

                  - `"execution_time_exceeded"`

                  - `"model_not_found"`

                - `type: "advisor_tool_result_error"`

              - `beta_advisor_result_block: object { stop_reason, text, type }`

                - `stop_reason: string`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

                - `text: string`

                - `type: "advisor_result"`

              - `beta_advisor_redacted_result_block: object { encrypted_content, stop_reason, type }`

                - `encrypted_content: string`

                  Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

                - `stop_reason: string`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

                - `type: "advisor_redacted_result"`

            - `tool_use_id: string`

            - `type: "advisor_tool_result"`

          - `beta_code_execution_tool_result_block: object { content, tool_use_id, type }`

            - `content: BetaCodeExecutionToolResultError or BetaCodeExecutionResultBlock or BetaEncryptedCodeExecutionResultBlock`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `beta_code_execution_tool_result_error: object { error_code, type }`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `type: "code_execution_tool_result_error"`

              - `beta_code_execution_result_block: object { content, return_code, stderr, 2 more }`

                - `content: array of BetaCodeExecutionOutputBlock`

                  - `file_id: string`

                  - `type: "code_execution_output"`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

                - `type: "code_execution_result"`

              - `beta_encrypted_code_execution_result_block: object { content, encrypted_stdout, return_code, 2 more }`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `content: array of BetaCodeExecutionOutputBlock`

                  - `file_id: string`

                  - `type: "code_execution_output"`

                - `encrypted_stdout: string`

                - `return_code: number`

                - `stderr: string`

                - `type: "encrypted_code_execution_result"`

            - `tool_use_id: string`

            - `type: "code_execution_tool_result"`

          - `beta_bash_code_execution_tool_result_block: object { content, tool_use_id, type }`

            - `content: BetaBashCodeExecutionToolResultError or BetaBashCodeExecutionResultBlock`

              - `beta_bash_code_execution_tool_result_error: object { error_code, type }`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"output_file_too_large"`

                - `type: "bash_code_execution_tool_result_error"`

              - `beta_bash_code_execution_result_block: object { content, return_code, stderr, 2 more }`

                - `content: array of BetaBashCodeExecutionOutputBlock`

                  - `file_id: string`

                  - `type: "bash_code_execution_output"`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

                - `type: "bash_code_execution_result"`

            - `tool_use_id: string`

            - `type: "bash_code_execution_tool_result"`

          - `beta_text_editor_code_execution_tool_result_block: object { content, tool_use_id, type }`

            - `content: BetaTextEditorCodeExecutionToolResultError or BetaTextEditorCodeExecutionViewResultBlock or BetaTextEditorCodeExecutionCreateResultBlock or BetaTextEditorCodeExecutionStrReplaceResultBlock`

              - `beta_text_editor_code_execution_tool_result_error: object { error_code, error_message, type }`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"file_not_found"`

                - `error_message: string`

                - `type: "text_editor_code_execution_tool_result_error"`

              - `beta_text_editor_code_execution_view_result_block: object { content, file_type, num_lines, 3 more }`

                - `content: string`

                - `file_type: "text" or "image" or "pdf"`

                  - `"text"`

                  - `"image"`

                  - `"pdf"`

                - `num_lines: number`

                - `start_line: number`

                - `total_lines: number`

                - `type: "text_editor_code_execution_view_result"`

              - `beta_text_editor_code_execution_create_result_block: object { is_file_update, type }`

                - `is_file_update: boolean`

                - `type: "text_editor_code_execution_create_result"`

              - `beta_text_editor_code_execution_str_replace_result_block: object { lines, new_lines, new_start, 3 more }`

                - `lines: array of string`

                - `new_lines: number`

                - `new_start: number`

                - `old_lines: number`

                - `old_start: number`

                - `type: "text_editor_code_execution_str_replace_result"`

            - `tool_use_id: string`

            - `type: "text_editor_code_execution_tool_result"`

          - `beta_tool_search_tool_result_block: object { content, tool_use_id, type }`

            - `content: BetaToolSearchToolResultError or BetaToolSearchToolSearchResultBlock`

              - `beta_tool_search_tool_result_error: object { error_code, error_message, type }`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `error_message: string`

                - `type: "tool_search_tool_result_error"`

              - `beta_tool_search_tool_search_result_block: object { tool_references, type }`

                - `tool_references: array of BetaToolReferenceBlock`

                  - `tool_name: string`

                  - `type: "tool_reference"`

                - `type: "tool_search_tool_search_result"`

            - `tool_use_id: string`

            - `type: "tool_search_tool_result"`

          - `beta_mcp_tool_use_block: object { id, input, name, 2 more }`

            - `id: string`

            - `input: map[unknown]`

            - `name: string`

              The name of the MCP tool

            - `server_name: string`

              The name of the MCP server

            - `type: "mcp_tool_use"`

          - `beta_mcp_tool_result_block: object { content, is_error, tool_use_id, type }`

            - `content: string or array of BetaTextBlock`

              - `union_member_0: string`

              - `beta_mcp_tool_result_block_content: array of BetaTextBlock`

                - `citations: array of BetaTextCitation`

                  Citations supporting the text block.

                  The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

                - `text: string`

                - `type: "text"`

            - `is_error: boolean`

            - `tool_use_id: string`

            - `type: "mcp_tool_result"`

          - `beta_container_upload_block: object { file_id, type }`

            Response model for a file uploaded to the container.

            - `file_id: string`

            - `type: "container_upload"`

          - `beta_compaction_block: object { content, encrypted_content, type }`

            A compaction block returned when autocompact is triggered.

            When content is None, it indicates the compaction failed to produce a valid
            summary (e.g., malformed output from the model). Clients may round-trip
            compaction blocks with null content; the server treats them as no-ops.

            - `content: string`

              Summary of compacted content, or null if compaction failed

            - `encrypted_content: string`

              Opaque metadata from prior compaction, to be round-tripped verbatim

            - `type: "compaction"`

          - `beta_fallback_block: object { from, to, type }`

            Marks the point in `content` where one model's output gives way to the next.

            One block appears per hop where a preceding model actually ran this turn and
            declined. A turn routed directly by the sticky decision has no such boundary
            and carries no block — the signal for whether a fallback model served the
            response is the presence of a `fallback_message` entry in
            `usage.iterations`, not this block.

            The block is treated like a server-tool content block for streaming: it
            arrives via the standard `content_block_start` / `content_block_stop`
            pair and carries no deltas.

            - `from: object { model }`

              The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

              - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `"claude-fable-5"`

                  Next generation of intelligence for the hardest knowledge work and coding problems

                - `"claude-mythos-5"`

                  Most capable model for cybersecurity and biology research

                - `"claude-opus-4-8"`

                  Frontier intelligence for long-running agents and coding

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

            - `to: object { model }`

              The fallback model producing the content that follows this block. Its `model` is always the canonical id.

              - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `type: "fallback"`

        - `context_management: object { applied_edits }`

          Context management response.

          Information about context management strategies applied during the request.

          - `applied_edits: array of BetaClearToolUses20250919EditResponse or BetaClearThinking20251015EditResponse`

            List of context management edits that were applied.

            - `beta_clear_tool_uses_20250919_edit_response: object { cleared_input_tokens, cleared_tool_uses, type }`

              - `cleared_input_tokens: number`

                Number of input tokens cleared by this edit.

              - `cleared_tool_uses: number`

                Number of tool uses that were cleared.

              - `type: "clear_tool_uses_20250919"`

                The type of context management edit applied.

            - `beta_clear_thinking_20251015_edit_response: object { cleared_input_tokens, cleared_thinking_turns, type }`

              - `cleared_input_tokens: number`

                Number of input tokens cleared by this edit.

              - `cleared_thinking_turns: number`

                Number of thinking turns that were cleared.

              - `type: "clear_thinking_20251015"`

                The type of context management edit applied.

        - `diagnostics: object { cache_miss_reason }`

          Response envelope for request-level diagnostics. Present (possibly
          null) whenever the caller supplied `diagnostics` on the request.

          - `cache_miss_reason: BetaCacheMissModelChanged or BetaCacheMissSystemChanged or BetaCacheMissToolsChanged or 3 more`

            Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

            - `beta_cache_miss_model_changed: object { cache_missed_input_tokens, type }`

              - `cache_missed_input_tokens: number`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `type: "model_changed"`

            - `beta_cache_miss_system_changed: object { cache_missed_input_tokens, type }`

              - `cache_missed_input_tokens: number`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `type: "system_changed"`

            - `beta_cache_miss_tools_changed: object { cache_missed_input_tokens, type }`

              - `cache_missed_input_tokens: number`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `type: "tools_changed"`

            - `beta_cache_miss_messages_changed: object { cache_missed_input_tokens, type }`

              - `cache_missed_input_tokens: number`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `type: "messages_changed"`

            - `beta_cache_miss_previous_message_not_found: object { type }`

              - `type: "previous_message_not_found"`

            - `beta_cache_miss_unavailable: object { type }`

              - `type: "unavailable"`

        - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-mythos-5"`

            Most capable model for cybersecurity and biology research

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

        - `role: "assistant"`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `stop_details: object { category, explanation, fallback_credit_token, 3 more }`

          Structured information about a refusal.

          - `category: "cyber" or "bio" or "reasoning_extraction"`

            The policy category that triggered the refusal.

            `null` when the refusal doesn't map to a named category.

            - `"cyber"`

            - `"bio"`

            - `"reasoning_extraction"`

          - `explanation: string`

            Human-readable explanation of the refusal.

            This text is not guaranteed to be stable. `null` when no explanation is available for the category.

          - `fallback_credit_token: string`

            Opaque code that refunds the cache-miss cost when retrying this refused
            request on the fallback model. Pass it as `fallback_credit_token` on the
            retry request. Expires 5 minutes after the refusal.

            The retry is sent either with the same request body (`system`, `messages`,
            `tools`, and other render-shaping fields), or with the same body plus one
            appended `assistant` message whose content is the partial text (with any
            trailing whitespace stripped from the final text block) and paired
            server-tool blocks from this refusal — which also authorizes that
            appended turn as an assistant-prefill continuation on models that otherwise
            disallow prefill. A token minted mid-server-tool-loop whose partial content
            was continuable may only be redeemed the second way — if a same-body retry
            is rejected with a 400 saying the token must be redeemed by continuing the
            partial response, retry the second way instead. Either way: same workspace,
            same platform; a mismatch is a 400. Resending a token for an already-warm
            prefix is permitted but yields no additional credit.

            `null` when the refused model isn't eligible for a fallback credit.

          - `fallback_has_prefill_claim: boolean`

            Whether the accompanying `fallback_credit_token` may be redeemed with the
            appended-assistant retry form. Only set when `fallback_credit_token` is
            present.

            `true`: retry by resending the same request body plus one appended
            `assistant` message whose content is this response's `content` with any
            trailing whitespace stripped from the final text block and unpaired
            `tool_use` blocks omitted (the same appended-turn shape described on
            `fallback_credit_token`), with the token attached. `false`: retry by
            resending the original request body unchanged, with the token attached —
            the appended-assistant form is not available for this refusal (no
            continuable partial content, or the request uses `output_format` or a
            `tool_choice` that forces tool use). One exception: when the request used
            `output_format` or a forced `tool_choice` and the refusal arrived after
            server tools (including MCP connector tools) had already executed, the
            token may not be redeemable by either retry form; if the exact-body retry
            is then rejected with a 400 saying the token must be redeemed by
            continuing the partial response, discard the token and retry without it.

            Advisory: if an appended-assistant retry is rejected with a 400 despite
            `true`, fall back to resending the original request body with the token.

          - `recommended_model: string`

            The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

          - `type: "refusal"`

        - `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 5 more`

          The reason that we stopped.

          This may be one the following values:

          * `"end_turn"`: the model reached a natural stopping point
          * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
          * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
          * `"tool_use"`: the model invoked one or more tools
          * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
          * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

          In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

          - `"end_turn"`

          - `"max_tokens"`

          - `"stop_sequence"`

          - `"tool_use"`

          - `"pause_turn"`

          - `"compaction"`

          - `"refusal"`

          - `"model_context_window_exceeded"`

        - `stop_sequence: string`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `type: "message"`

          Object type.

          For Messages, this is always `"message"`.

        - `usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 8 more }`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

          - `cache_creation_input_tokens: number`

            The number of input tokens used to create the cache entry.

          - `cache_read_input_tokens: number`

            The number of input tokens read from the cache.

          - `inference_geo: string`

            The geographic region where inference was performed for this request.

          - `input_tokens: number`

            The number of input tokens which were used.

          - `iterations: array of BetaMessageIterationUsage or BetaCompactionIterationUsage or BetaAdvisorMessageIterationUsage or BetaFallbackMessageIterationUsage`

            Per-iteration token usage breakdown.

            Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

            - Determine which iterations exceeded long context thresholds (>=200k tokens)
            - Calculate the true context window size from the last iteration
            - Understand token accumulation across server-side tool use loops

            - `beta_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

              Token usage for a sampling iteration.

              - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

                Breakdown of cached tokens by TTL

                - `ephemeral_1h_input_tokens: number`

                  The number of input tokens used to create the 1 hour cache entry.

                - `ephemeral_5m_input_tokens: number`

                  The number of input tokens used to create the 5 minute cache entry.

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

              - `input_tokens: number`

                The number of input tokens which were used.

              - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `"claude-fable-5"`

                  Next generation of intelligence for the hardest knowledge work and coding problems

                - `"claude-mythos-5"`

                  Most capable model for cybersecurity and biology research

                - `"claude-opus-4-8"`

                  Frontier intelligence for long-running agents and coding

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

              - `output_tokens: number`

                The number of output tokens which were used.

              - `type: "message"`

                Usage for a sampling iteration

            - `beta_compaction_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }`

              Token usage for a compaction iteration.

              - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

                Breakdown of cached tokens by TTL

                - `ephemeral_1h_input_tokens: number`

                  The number of input tokens used to create the 1 hour cache entry.

                - `ephemeral_5m_input_tokens: number`

                  The number of input tokens used to create the 5 minute cache entry.

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

              - `input_tokens: number`

                The number of input tokens which were used.

              - `output_tokens: number`

                The number of output tokens which were used.

              - `type: "compaction"`

                Usage for a compaction iteration

            - `beta_advisor_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

              Token usage for an advisor sub-inference iteration.

              - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

                Breakdown of cached tokens by TTL

                - `ephemeral_1h_input_tokens: number`

                  The number of input tokens used to create the 1 hour cache entry.

                - `ephemeral_5m_input_tokens: number`

                  The number of input tokens used to create the 5 minute cache entry.

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

              - `input_tokens: number`

                The number of input tokens which were used.

              - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `"claude-fable-5"`

                  Next generation of intelligence for the hardest knowledge work and coding problems

                - `"claude-mythos-5"`

                  Most capable model for cybersecurity and biology research

                - `"claude-opus-4-8"`

                  Frontier intelligence for long-running agents and coding

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

              - `output_tokens: number`

                The number of output tokens which were used.

              - `type: "advisor_message"`

                Usage for an advisor sub-inference iteration

            - `beta_fallback_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

              Token usage for the fallback-model attempt of a server-side fallback request.

              Produced in place of a `message` entry for whichever hop served the
              response. A declined hop produces the existing `message` entry. Whether
              a fallback model served the response is signalled by the presence of this
              entry in `usage.iterations`.

              - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

                Breakdown of cached tokens by TTL

                - `ephemeral_1h_input_tokens: number`

                  The number of input tokens used to create the 1 hour cache entry.

                - `ephemeral_5m_input_tokens: number`

                  The number of input tokens used to create the 5 minute cache entry.

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

              - `input_tokens: number`

                The number of input tokens which were used.

              - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `"claude-fable-5"`

                  Next generation of intelligence for the hardest knowledge work and coding problems

                - `"claude-mythos-5"`

                  Most capable model for cybersecurity and biology research

                - `"claude-opus-4-8"`

                  Frontier intelligence for long-running agents and coding

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

              - `output_tokens: number`

                The number of output tokens which were used.

              - `type: "fallback_message"`

                Usage for the fallback-model attempt that served the response

          - `output_tokens: number`

            The number of output tokens which were used.

          - `output_tokens_details: object { thinking_tokens }`

            Breakdown of output tokens by category.

            `output_tokens` remains the inclusive, authoritative total used for billing.
            This object provides a read-only decomposition for observability — for example,
            how many of the billed output tokens were spent on internal reasoning that may
            have been summarized before being returned to you.

            - `thinking_tokens: number`

              Number of output tokens the model generated as internal reasoning, including
              the thinking-block delimiter tokens.

              Reflects the raw reasoning the model produced, not the (possibly shorter)
              summarized thinking text returned in the response body. Computed by
              re-tokenizing the raw reasoning text, so it may differ from the model's exact
              generation count by a small number of tokens. Always ≤ `output_tokens`;
              `output_tokens - thinking_tokens` approximates the non-reasoning output.

          - `server_tool_use: object { web_fetch_requests, web_search_requests }`

            The number of server tool requests.

            - `web_fetch_requests: number`

              The number of web fetch tool requests.

            - `web_search_requests: number`

              The number of web search tool requests.

          - `service_tier: "standard" or "priority" or "batch"`

            If the request used the priority, standard, or batch tier.

            - `"standard"`

            - `"priority"`

            - `"batch"`

          - `speed: "standard" or "fast"`

            The inference speed mode used for this request.

            - `"standard"`

            - `"fast"`

      - `type: "succeeded"`

    - `beta_message_batch_errored_result: object { error, type }`

      - `error: object { error, request_id, type }`

        - `error: BetaInvalidRequestError or BetaAuthenticationError or BetaBillingError or 6 more`

          - `beta_invalid_request_error: object { message, type }`

            - `message: string`

            - `type: "invalid_request_error"`

          - `beta_authentication_error: object { message, type }`

            - `message: string`

            - `type: "authentication_error"`

          - `beta_billing_error: object { message, type }`

            - `message: string`

            - `type: "billing_error"`

          - `beta_permission_error: object { message, type }`

            - `message: string`

            - `type: "permission_error"`

          - `beta_not_found_error: object { message, type }`

            - `message: string`

            - `type: "not_found_error"`

          - `beta_rate_limit_error: object { message, type }`

            - `message: string`

            - `type: "rate_limit_error"`

          - `beta_gateway_timeout_error: object { message, type }`

            - `message: string`

            - `type: "timeout_error"`

          - `beta_api_error: object { message, type }`

            - `message: string`

            - `type: "api_error"`

          - `beta_overloaded_error: object { message, type }`

            - `message: string`

            - `type: "overloaded_error"`

        - `request_id: string`

        - `type: "error"`

      - `type: "errored"`

    - `beta_message_batch_canceled_result: object { type }`

      - `type: "canceled"`

    - `beta_message_batch_expired_result: object { type }`

      - `type: "expired"`

### Example

```cli
ant beta:messages:batches results \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

## Domain Types

### Beta Deleted Message Batch

- `beta_deleted_message_batch: object { id, type }`

  - `id: string`

    ID of the Message Batch.

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Beta Message Batch

- `beta_message_batch: object { id, archived_at, cancel_initiated_at, 7 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object { canceled, errored, expired, 2 more }`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Beta Message Batch Canceled Result

- `beta_message_batch_canceled_result: object { type }`

  - `type: "canceled"`

### Beta Message Batch Errored Result

- `beta_message_batch_errored_result: object { error, type }`

  - `error: object { error, request_id, type }`

    - `error: BetaInvalidRequestError or BetaAuthenticationError or BetaBillingError or 6 more`

      - `beta_invalid_request_error: object { message, type }`

        - `message: string`

        - `type: "invalid_request_error"`

      - `beta_authentication_error: object { message, type }`

        - `message: string`

        - `type: "authentication_error"`

      - `beta_billing_error: object { message, type }`

        - `message: string`

        - `type: "billing_error"`

      - `beta_permission_error: object { message, type }`

        - `message: string`

        - `type: "permission_error"`

      - `beta_not_found_error: object { message, type }`

        - `message: string`

        - `type: "not_found_error"`

      - `beta_rate_limit_error: object { message, type }`

        - `message: string`

        - `type: "rate_limit_error"`

      - `beta_gateway_timeout_error: object { message, type }`

        - `message: string`

        - `type: "timeout_error"`

      - `beta_api_error: object { message, type }`

        - `message: string`

        - `type: "api_error"`

      - `beta_overloaded_error: object { message, type }`

        - `message: string`

        - `type: "overloaded_error"`

    - `request_id: string`

    - `type: "error"`

  - `type: "errored"`

### Beta Message Batch Expired Result

- `beta_message_batch_expired_result: object { type }`

  - `type: "expired"`

### Beta Message Batch Individual Response

- `beta_message_batch_individual_response: object { custom_id, result }`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `custom_id: string`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `result: BetaMessageBatchSucceededResult or BetaMessageBatchErroredResult or BetaMessageBatchCanceledResult or BetaMessageBatchExpiredResult`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `beta_message_batch_succeeded_result: object { message, type }`

      - `message: object { id, container, content, 9 more }`

        - `id: string`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `container: object { id, expires_at, skills }`

          Information about the container used in the request (for the code execution tool)

          - `id: string`

            Identifier for the container used in this request

          - `expires_at: string`

            The time at which the container will expire.

          - `skills: array of BetaSkill`

            Skills loaded in the container

            - `skill_id: string`

              Skill ID

            - `type: "anthropic" or "custom"`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `"anthropic"`

              - `"custom"`

            - `version: string`

              Skill version or 'latest' for most recent version

        - `content: array of BetaContentBlock`

          Content generated by the model.

          This is an array of content blocks, each of which has a `type` that determines its shape.

          Example:

          ```json
          [{"type": "text", "text": "Hi, I'm Claude."}]
          ```

          If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

          For example, if the input `messages` were:

          ```json
          [
            {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
            {"role": "assistant", "content": "The best answer is ("}
          ]
          ```

          Then the response `content` might be:

          ```json
          [{"type": "text", "text": "B)"}]
          ```

          - `beta_text_block: object { citations, text, type }`

            - `citations: array of BetaTextCitation`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `beta_citation_char_location: object { cited_text, document_index, document_title, 4 more }`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string`

                - `end_char_index: number`

                - `file_id: string`

                - `start_char_index: number`

                - `type: "char_location"`

              - `beta_citation_page_location: object { cited_text, document_index, document_title, 4 more }`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string`

                - `end_page_number: number`

                - `file_id: string`

                - `start_page_number: number`

                - `type: "page_location"`

              - `beta_citation_content_block_location: object { cited_text, document_index, document_title, 4 more }`

                - `cited_text: string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `document_index: number`

                - `document_title: string`

                - `end_block_index: number`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `file_id: string`

                - `start_block_index: number`

                  0-based index of the first cited block in the source's `content` array.

                - `type: "content_block_location"`

              - `beta_citations_web_search_result_location: object { cited_text, encrypted_index, title, 2 more }`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string`

                - `type: "web_search_result_location"`

                - `url: string`

              - `beta_citation_search_result_location: object { cited_text, end_block_index, search_result_index, 4 more }`

                - `cited_text: string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `end_block_index: number`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `search_result_index: number`

                  0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                  Counted separately from `document_index`; server-side web search results are not included in this count.

                - `source: string`

                - `start_block_index: number`

                  0-based index of the first cited block in the source's `content` array.

                - `title: string`

                - `type: "search_result_location"`

            - `text: string`

            - `type: "text"`

          - `beta_thinking_block: object { signature, thinking, type }`

            - `signature: string`

            - `thinking: string`

            - `type: "thinking"`

          - `beta_redacted_thinking_block: object { data, type }`

            - `data: string`

            - `type: "redacted_thinking"`

          - `beta_tool_use_block: object { id, input, name, 2 more }`

            - `id: string`

            - `input: map[unknown]`

            - `name: string`

            - `type: "tool_use"`

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              Tool invocation directly from the model.

              - `beta_direct_caller: object { type }`

                Tool invocation directly from the model.

                - `type: "direct"`

              - `beta_server_tool_caller: object { tool_id, type }`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

              - `beta_server_tool_caller_20260120: object { tool_id, type }`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

          - `beta_server_tool_use_block: object { id, input, name, 2 more }`

            - `id: string`

            - `input: map[unknown]`

            - `name: "advisor" or "web_search" or "web_fetch" or 5 more`

              - `"advisor"`

              - `"web_search"`

              - `"web_fetch"`

              - `"code_execution"`

              - `"bash_code_execution"`

              - `"text_editor_code_execution"`

              - `"tool_search_tool_regex"`

              - `"tool_search_tool_bm25"`

            - `type: "server_tool_use"`

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              Tool invocation directly from the model.

              - `beta_direct_caller: object { type }`

                Tool invocation directly from the model.

              - `beta_server_tool_caller: object { tool_id, type }`

                Tool invocation generated by a server-side tool.

              - `beta_server_tool_caller_20260120: object { tool_id, type }`

          - `beta_web_search_tool_result_block: object { content, tool_use_id, type, caller }`

            - `content: BetaWebSearchToolResultError or array of BetaWebSearchResultBlock`

              - `beta_web_search_tool_result_error: object { error_code, type }`

                - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"max_uses_exceeded"`

                  - `"too_many_requests"`

                  - `"query_too_long"`

                  - `"request_too_large"`

                - `type: "web_search_tool_result_error"`

              - `union_member_1: array of BetaWebSearchResultBlock`

                - `encrypted_content: string`

                - `page_age: string`

                - `title: string`

                - `type: "web_search_result"`

                - `url: string`

            - `tool_use_id: string`

            - `type: "web_search_tool_result"`

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              Tool invocation directly from the model.

              - `beta_direct_caller: object { type }`

                Tool invocation directly from the model.

              - `beta_server_tool_caller: object { tool_id, type }`

                Tool invocation generated by a server-side tool.

              - `beta_server_tool_caller_20260120: object { tool_id, type }`

          - `beta_web_fetch_tool_result_block: object { content, tool_use_id, type, caller }`

            - `content: BetaWebFetchToolResultErrorBlock or BetaWebFetchBlock`

              - `beta_web_fetch_tool_result_error_block: object { error_code, type }`

                - `error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 6 more`

                  - `"invalid_tool_input"`

                  - `"url_too_long"`

                  - `"url_not_allowed"`

                  - `"url_not_in_prior_context"`

                  - `"url_not_accessible"`

                  - `"unsupported_content_type"`

                  - `"too_many_requests"`

                  - `"max_uses_exceeded"`

                  - `"unavailable"`

                - `type: "web_fetch_tool_result_error"`

              - `beta_web_fetch_block: object { content, retrieved_at, type, url }`

                - `content: object { citations, source, title, type }`

                  - `citations: object { enabled }`

                    Citation configuration for the document

                    - `enabled: boolean`

                  - `source: BetaBase64PDFSource or BetaPlainTextSource`

                    - `beta_base64_pdf_source: object { data, media_type, type }`

                      - `data: string`

                      - `media_type: "application/pdf"`

                      - `type: "base64"`

                    - `beta_plain_text_source: object { data, media_type, type }`

                      - `data: string`

                      - `media_type: "text/plain"`

                      - `type: "text"`

                  - `title: string`

                    The title of the document

                  - `type: "document"`

                - `retrieved_at: string`

                  ISO 8601 timestamp when the content was retrieved

                - `type: "web_fetch_result"`

                - `url: string`

                  Fetched content URL

            - `tool_use_id: string`

            - `type: "web_fetch_tool_result"`

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              Tool invocation directly from the model.

              - `beta_direct_caller: object { type }`

                Tool invocation directly from the model.

              - `beta_server_tool_caller: object { tool_id, type }`

                Tool invocation generated by a server-side tool.

              - `beta_server_tool_caller_20260120: object { tool_id, type }`

          - `beta_advisor_tool_result_block: object { content, tool_use_id, type }`

            - `content: BetaAdvisorToolResultError or BetaAdvisorResultBlock or BetaAdvisorRedactedResultBlock`

              - `beta_advisor_tool_result_error: object { error_code, type }`

                - `error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 4 more`

                  - `"max_uses_exceeded"`

                  - `"prompt_too_long"`

                  - `"too_many_requests"`

                  - `"overloaded"`

                  - `"unavailable"`

                  - `"execution_time_exceeded"`

                  - `"model_not_found"`

                - `type: "advisor_tool_result_error"`

              - `beta_advisor_result_block: object { stop_reason, text, type }`

                - `stop_reason: string`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

                - `text: string`

                - `type: "advisor_result"`

              - `beta_advisor_redacted_result_block: object { encrypted_content, stop_reason, type }`

                - `encrypted_content: string`

                  Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

                - `stop_reason: string`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

                - `type: "advisor_redacted_result"`

            - `tool_use_id: string`

            - `type: "advisor_tool_result"`

          - `beta_code_execution_tool_result_block: object { content, tool_use_id, type }`

            - `content: BetaCodeExecutionToolResultError or BetaCodeExecutionResultBlock or BetaEncryptedCodeExecutionResultBlock`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `beta_code_execution_tool_result_error: object { error_code, type }`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `type: "code_execution_tool_result_error"`

              - `beta_code_execution_result_block: object { content, return_code, stderr, 2 more }`

                - `content: array of BetaCodeExecutionOutputBlock`

                  - `file_id: string`

                  - `type: "code_execution_output"`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

                - `type: "code_execution_result"`

              - `beta_encrypted_code_execution_result_block: object { content, encrypted_stdout, return_code, 2 more }`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `content: array of BetaCodeExecutionOutputBlock`

                  - `file_id: string`

                  - `type: "code_execution_output"`

                - `encrypted_stdout: string`

                - `return_code: number`

                - `stderr: string`

                - `type: "encrypted_code_execution_result"`

            - `tool_use_id: string`

            - `type: "code_execution_tool_result"`

          - `beta_bash_code_execution_tool_result_block: object { content, tool_use_id, type }`

            - `content: BetaBashCodeExecutionToolResultError or BetaBashCodeExecutionResultBlock`

              - `beta_bash_code_execution_tool_result_error: object { error_code, type }`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"output_file_too_large"`

                - `type: "bash_code_execution_tool_result_error"`

              - `beta_bash_code_execution_result_block: object { content, return_code, stderr, 2 more }`

                - `content: array of BetaBashCodeExecutionOutputBlock`

                  - `file_id: string`

                  - `type: "bash_code_execution_output"`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

                - `type: "bash_code_execution_result"`

            - `tool_use_id: string`

            - `type: "bash_code_execution_tool_result"`

          - `beta_text_editor_code_execution_tool_result_block: object { content, tool_use_id, type }`

            - `content: BetaTextEditorCodeExecutionToolResultError or BetaTextEditorCodeExecutionViewResultBlock or BetaTextEditorCodeExecutionCreateResultBlock or BetaTextEditorCodeExecutionStrReplaceResultBlock`

              - `beta_text_editor_code_execution_tool_result_error: object { error_code, error_message, type }`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"file_not_found"`

                - `error_message: string`

                - `type: "text_editor_code_execution_tool_result_error"`

              - `beta_text_editor_code_execution_view_result_block: object { content, file_type, num_lines, 3 more }`

                - `content: string`

                - `file_type: "text" or "image" or "pdf"`

                  - `"text"`

                  - `"image"`

                  - `"pdf"`

                - `num_lines: number`

                - `start_line: number`

                - `total_lines: number`

                - `type: "text_editor_code_execution_view_result"`

              - `beta_text_editor_code_execution_create_result_block: object { is_file_update, type }`

                - `is_file_update: boolean`

                - `type: "text_editor_code_execution_create_result"`

              - `beta_text_editor_code_execution_str_replace_result_block: object { lines, new_lines, new_start, 3 more }`

                - `lines: array of string`

                - `new_lines: number`

                - `new_start: number`

                - `old_lines: number`

                - `old_start: number`

                - `type: "text_editor_code_execution_str_replace_result"`

            - `tool_use_id: string`

            - `type: "text_editor_code_execution_tool_result"`

          - `beta_tool_search_tool_result_block: object { content, tool_use_id, type }`

            - `content: BetaToolSearchToolResultError or BetaToolSearchToolSearchResultBlock`

              - `beta_tool_search_tool_result_error: object { error_code, error_message, type }`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `error_message: string`

                - `type: "tool_search_tool_result_error"`

              - `beta_tool_search_tool_search_result_block: object { tool_references, type }`

                - `tool_references: array of BetaToolReferenceBlock`

                  - `tool_name: string`

                  - `type: "tool_reference"`

                - `type: "tool_search_tool_search_result"`

            - `tool_use_id: string`

            - `type: "tool_search_tool_result"`

          - `beta_mcp_tool_use_block: object { id, input, name, 2 more }`

            - `id: string`

            - `input: map[unknown]`

            - `name: string`

              The name of the MCP tool

            - `server_name: string`

              The name of the MCP server

            - `type: "mcp_tool_use"`

          - `beta_mcp_tool_result_block: object { content, is_error, tool_use_id, type }`

            - `content: string or array of BetaTextBlock`

              - `union_member_0: string`

              - `beta_mcp_tool_result_block_content: array of BetaTextBlock`

                - `citations: array of BetaTextCitation`

                  Citations supporting the text block.

                  The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

                - `text: string`

                - `type: "text"`

            - `is_error: boolean`

            - `tool_use_id: string`

            - `type: "mcp_tool_result"`

          - `beta_container_upload_block: object { file_id, type }`

            Response model for a file uploaded to the container.

            - `file_id: string`

            - `type: "container_upload"`

          - `beta_compaction_block: object { content, encrypted_content, type }`

            A compaction block returned when autocompact is triggered.

            When content is None, it indicates the compaction failed to produce a valid
            summary (e.g., malformed output from the model). Clients may round-trip
            compaction blocks with null content; the server treats them as no-ops.

            - `content: string`

              Summary of compacted content, or null if compaction failed

            - `encrypted_content: string`

              Opaque metadata from prior compaction, to be round-tripped verbatim

            - `type: "compaction"`

          - `beta_fallback_block: object { from, to, type }`

            Marks the point in `content` where one model's output gives way to the next.

            One block appears per hop where a preceding model actually ran this turn and
            declined. A turn routed directly by the sticky decision has no such boundary
            and carries no block — the signal for whether a fallback model served the
            response is the presence of a `fallback_message` entry in
            `usage.iterations`, not this block.

            The block is treated like a server-tool content block for streaming: it
            arrives via the standard `content_block_start` / `content_block_stop`
            pair and carries no deltas.

            - `from: object { model }`

              The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

              - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `"claude-fable-5"`

                  Next generation of intelligence for the hardest knowledge work and coding problems

                - `"claude-mythos-5"`

                  Most capable model for cybersecurity and biology research

                - `"claude-opus-4-8"`

                  Frontier intelligence for long-running agents and coding

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

            - `to: object { model }`

              The fallback model producing the content that follows this block. Its `model` is always the canonical id.

              - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `type: "fallback"`

        - `context_management: object { applied_edits }`

          Context management response.

          Information about context management strategies applied during the request.

          - `applied_edits: array of BetaClearToolUses20250919EditResponse or BetaClearThinking20251015EditResponse`

            List of context management edits that were applied.

            - `beta_clear_tool_uses_20250919_edit_response: object { cleared_input_tokens, cleared_tool_uses, type }`

              - `cleared_input_tokens: number`

                Number of input tokens cleared by this edit.

              - `cleared_tool_uses: number`

                Number of tool uses that were cleared.

              - `type: "clear_tool_uses_20250919"`

                The type of context management edit applied.

            - `beta_clear_thinking_20251015_edit_response: object { cleared_input_tokens, cleared_thinking_turns, type }`

              - `cleared_input_tokens: number`

                Number of input tokens cleared by this edit.

              - `cleared_thinking_turns: number`

                Number of thinking turns that were cleared.

              - `type: "clear_thinking_20251015"`

                The type of context management edit applied.

        - `diagnostics: object { cache_miss_reason }`

          Response envelope for request-level diagnostics. Present (possibly
          null) whenever the caller supplied `diagnostics` on the request.

          - `cache_miss_reason: BetaCacheMissModelChanged or BetaCacheMissSystemChanged or BetaCacheMissToolsChanged or 3 more`

            Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

            - `beta_cache_miss_model_changed: object { cache_missed_input_tokens, type }`

              - `cache_missed_input_tokens: number`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `type: "model_changed"`

            - `beta_cache_miss_system_changed: object { cache_missed_input_tokens, type }`

              - `cache_missed_input_tokens: number`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `type: "system_changed"`

            - `beta_cache_miss_tools_changed: object { cache_missed_input_tokens, type }`

              - `cache_missed_input_tokens: number`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `type: "tools_changed"`

            - `beta_cache_miss_messages_changed: object { cache_missed_input_tokens, type }`

              - `cache_missed_input_tokens: number`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `type: "messages_changed"`

            - `beta_cache_miss_previous_message_not_found: object { type }`

              - `type: "previous_message_not_found"`

            - `beta_cache_miss_unavailable: object { type }`

              - `type: "unavailable"`

        - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-mythos-5"`

            Most capable model for cybersecurity and biology research

          - `"claude-opus-4-8"`

            Frontier intelligence for long-running agents and coding

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

        - `role: "assistant"`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `stop_details: object { category, explanation, fallback_credit_token, 3 more }`

          Structured information about a refusal.

          - `category: "cyber" or "bio" or "reasoning_extraction"`

            The policy category that triggered the refusal.

            `null` when the refusal doesn't map to a named category.

            - `"cyber"`

            - `"bio"`

            - `"reasoning_extraction"`

          - `explanation: string`

            Human-readable explanation of the refusal.

            This text is not guaranteed to be stable. `null` when no explanation is available for the category.

          - `fallback_credit_token: string`

            Opaque code that refunds the cache-miss cost when retrying this refused
            request on the fallback model. Pass it as `fallback_credit_token` on the
            retry request. Expires 5 minutes after the refusal.

            The retry is sent either with the same request body (`system`, `messages`,
            `tools`, and other render-shaping fields), or with the same body plus one
            appended `assistant` message whose content is the partial text (with any
            trailing whitespace stripped from the final text block) and paired
            server-tool blocks from this refusal — which also authorizes that
            appended turn as an assistant-prefill continuation on models that otherwise
            disallow prefill. A token minted mid-server-tool-loop whose partial content
            was continuable may only be redeemed the second way — if a same-body retry
            is rejected with a 400 saying the token must be redeemed by continuing the
            partial response, retry the second way instead. Either way: same workspace,
            same platform; a mismatch is a 400. Resending a token for an already-warm
            prefix is permitted but yields no additional credit.

            `null` when the refused model isn't eligible for a fallback credit.

          - `fallback_has_prefill_claim: boolean`

            Whether the accompanying `fallback_credit_token` may be redeemed with the
            appended-assistant retry form. Only set when `fallback_credit_token` is
            present.

            `true`: retry by resending the same request body plus one appended
            `assistant` message whose content is this response's `content` with any
            trailing whitespace stripped from the final text block and unpaired
            `tool_use` blocks omitted (the same appended-turn shape described on
            `fallback_credit_token`), with the token attached. `false`: retry by
            resending the original request body unchanged, with the token attached —
            the appended-assistant form is not available for this refusal (no
            continuable partial content, or the request uses `output_format` or a
            `tool_choice` that forces tool use). One exception: when the request used
            `output_format` or a forced `tool_choice` and the refusal arrived after
            server tools (including MCP connector tools) had already executed, the
            token may not be redeemable by either retry form; if the exact-body retry
            is then rejected with a 400 saying the token must be redeemed by
            continuing the partial response, discard the token and retry without it.

            Advisory: if an appended-assistant retry is rejected with a 400 despite
            `true`, fall back to resending the original request body with the token.

          - `recommended_model: string`

            The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

          - `type: "refusal"`

        - `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 5 more`

          The reason that we stopped.

          This may be one the following values:

          * `"end_turn"`: the model reached a natural stopping point
          * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
          * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
          * `"tool_use"`: the model invoked one or more tools
          * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
          * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

          In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

          - `"end_turn"`

          - `"max_tokens"`

          - `"stop_sequence"`

          - `"tool_use"`

          - `"pause_turn"`

          - `"compaction"`

          - `"refusal"`

          - `"model_context_window_exceeded"`

        - `stop_sequence: string`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `type: "message"`

          Object type.

          For Messages, this is always `"message"`.

        - `usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 8 more }`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

          - `cache_creation_input_tokens: number`

            The number of input tokens used to create the cache entry.

          - `cache_read_input_tokens: number`

            The number of input tokens read from the cache.

          - `inference_geo: string`

            The geographic region where inference was performed for this request.

          - `input_tokens: number`

            The number of input tokens which were used.

          - `iterations: array of BetaMessageIterationUsage or BetaCompactionIterationUsage or BetaAdvisorMessageIterationUsage or BetaFallbackMessageIterationUsage`

            Per-iteration token usage breakdown.

            Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

            - Determine which iterations exceeded long context thresholds (>=200k tokens)
            - Calculate the true context window size from the last iteration
            - Understand token accumulation across server-side tool use loops

            - `beta_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

              Token usage for a sampling iteration.

              - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

                Breakdown of cached tokens by TTL

                - `ephemeral_1h_input_tokens: number`

                  The number of input tokens used to create the 1 hour cache entry.

                - `ephemeral_5m_input_tokens: number`

                  The number of input tokens used to create the 5 minute cache entry.

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

              - `input_tokens: number`

                The number of input tokens which were used.

              - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `"claude-fable-5"`

                  Next generation of intelligence for the hardest knowledge work and coding problems

                - `"claude-mythos-5"`

                  Most capable model for cybersecurity and biology research

                - `"claude-opus-4-8"`

                  Frontier intelligence for long-running agents and coding

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

              - `output_tokens: number`

                The number of output tokens which were used.

              - `type: "message"`

                Usage for a sampling iteration

            - `beta_compaction_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }`

              Token usage for a compaction iteration.

              - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

                Breakdown of cached tokens by TTL

                - `ephemeral_1h_input_tokens: number`

                  The number of input tokens used to create the 1 hour cache entry.

                - `ephemeral_5m_input_tokens: number`

                  The number of input tokens used to create the 5 minute cache entry.

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

              - `input_tokens: number`

                The number of input tokens which were used.

              - `output_tokens: number`

                The number of output tokens which were used.

              - `type: "compaction"`

                Usage for a compaction iteration

            - `beta_advisor_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

              Token usage for an advisor sub-inference iteration.

              - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

                Breakdown of cached tokens by TTL

                - `ephemeral_1h_input_tokens: number`

                  The number of input tokens used to create the 1 hour cache entry.

                - `ephemeral_5m_input_tokens: number`

                  The number of input tokens used to create the 5 minute cache entry.

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

              - `input_tokens: number`

                The number of input tokens which were used.

              - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `"claude-fable-5"`

                  Next generation of intelligence for the hardest knowledge work and coding problems

                - `"claude-mythos-5"`

                  Most capable model for cybersecurity and biology research

                - `"claude-opus-4-8"`

                  Frontier intelligence for long-running agents and coding

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

              - `output_tokens: number`

                The number of output tokens which were used.

              - `type: "advisor_message"`

                Usage for an advisor sub-inference iteration

            - `beta_fallback_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

              Token usage for the fallback-model attempt of a server-side fallback request.

              Produced in place of a `message` entry for whichever hop served the
              response. A declined hop produces the existing `message` entry. Whether
              a fallback model served the response is signalled by the presence of this
              entry in `usage.iterations`.

              - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

                Breakdown of cached tokens by TTL

                - `ephemeral_1h_input_tokens: number`

                  The number of input tokens used to create the 1 hour cache entry.

                - `ephemeral_5m_input_tokens: number`

                  The number of input tokens used to create the 5 minute cache entry.

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

              - `input_tokens: number`

                The number of input tokens which were used.

              - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `"claude-fable-5"`

                  Next generation of intelligence for the hardest knowledge work and coding problems

                - `"claude-mythos-5"`

                  Most capable model for cybersecurity and biology research

                - `"claude-opus-4-8"`

                  Frontier intelligence for long-running agents and coding

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

              - `output_tokens: number`

                The number of output tokens which were used.

              - `type: "fallback_message"`

                Usage for the fallback-model attempt that served the response

          - `output_tokens: number`

            The number of output tokens which were used.

          - `output_tokens_details: object { thinking_tokens }`

            Breakdown of output tokens by category.

            `output_tokens` remains the inclusive, authoritative total used for billing.
            This object provides a read-only decomposition for observability — for example,
            how many of the billed output tokens were spent on internal reasoning that may
            have been summarized before being returned to you.

            - `thinking_tokens: number`

              Number of output tokens the model generated as internal reasoning, including
              the thinking-block delimiter tokens.

              Reflects the raw reasoning the model produced, not the (possibly shorter)
              summarized thinking text returned in the response body. Computed by
              re-tokenizing the raw reasoning text, so it may differ from the model's exact
              generation count by a small number of tokens. Always ≤ `output_tokens`;
              `output_tokens - thinking_tokens` approximates the non-reasoning output.

          - `server_tool_use: object { web_fetch_requests, web_search_requests }`

            The number of server tool requests.

            - `web_fetch_requests: number`

              The number of web fetch tool requests.

            - `web_search_requests: number`

              The number of web search tool requests.

          - `service_tier: "standard" or "priority" or "batch"`

            If the request used the priority, standard, or batch tier.

            - `"standard"`

            - `"priority"`

            - `"batch"`

          - `speed: "standard" or "fast"`

            The inference speed mode used for this request.

            - `"standard"`

            - `"fast"`

      - `type: "succeeded"`

    - `beta_message_batch_errored_result: object { error, type }`

      - `error: object { error, request_id, type }`

        - `error: BetaInvalidRequestError or BetaAuthenticationError or BetaBillingError or 6 more`

          - `beta_invalid_request_error: object { message, type }`

            - `message: string`

            - `type: "invalid_request_error"`

          - `beta_authentication_error: object { message, type }`

            - `message: string`

            - `type: "authentication_error"`

          - `beta_billing_error: object { message, type }`

            - `message: string`

            - `type: "billing_error"`

          - `beta_permission_error: object { message, type }`

            - `message: string`

            - `type: "permission_error"`

          - `beta_not_found_error: object { message, type }`

            - `message: string`

            - `type: "not_found_error"`

          - `beta_rate_limit_error: object { message, type }`

            - `message: string`

            - `type: "rate_limit_error"`

          - `beta_gateway_timeout_error: object { message, type }`

            - `message: string`

            - `type: "timeout_error"`

          - `beta_api_error: object { message, type }`

            - `message: string`

            - `type: "api_error"`

          - `beta_overloaded_error: object { message, type }`

            - `message: string`

            - `type: "overloaded_error"`

        - `request_id: string`

        - `type: "error"`

      - `type: "errored"`

    - `beta_message_batch_canceled_result: object { type }`

      - `type: "canceled"`

    - `beta_message_batch_expired_result: object { type }`

      - `type: "expired"`

### Beta Message Batch Request Counts

- `beta_message_batch_request_counts: object { canceled, errored, expired, 2 more }`

  - `canceled: number`

    Number of requests in the Message Batch that have been canceled.

    This is zero until processing of the entire Message Batch has ended.

  - `errored: number`

    Number of requests in the Message Batch that encountered an error.

    This is zero until processing of the entire Message Batch has ended.

  - `expired: number`

    Number of requests in the Message Batch that have expired.

    This is zero until processing of the entire Message Batch has ended.

  - `processing: number`

    Number of requests in the Message Batch that are processing.

  - `succeeded: number`

    Number of requests in the Message Batch that have completed successfully.

    This is zero until processing of the entire Message Batch has ended.

### Beta Message Batch Result

- `beta_message_batch_result: BetaMessageBatchSucceededResult or BetaMessageBatchErroredResult or BetaMessageBatchCanceledResult or BetaMessageBatchExpiredResult`

  Processing result for this request.

  Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

  - `beta_message_batch_succeeded_result: object { message, type }`

    - `message: object { id, container, content, 9 more }`

      - `id: string`

        Unique object identifier.

        The format and length of IDs may change over time.

      - `container: object { id, expires_at, skills }`

        Information about the container used in the request (for the code execution tool)

        - `id: string`

          Identifier for the container used in this request

        - `expires_at: string`

          The time at which the container will expire.

        - `skills: array of BetaSkill`

          Skills loaded in the container

          - `skill_id: string`

            Skill ID

          - `type: "anthropic" or "custom"`

            Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

            - `"anthropic"`

            - `"custom"`

          - `version: string`

            Skill version or 'latest' for most recent version

      - `content: array of BetaContentBlock`

        Content generated by the model.

        This is an array of content blocks, each of which has a `type` that determines its shape.

        Example:

        ```json
        [{"type": "text", "text": "Hi, I'm Claude."}]
        ```

        If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

        For example, if the input `messages` were:

        ```json
        [
          {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
          {"role": "assistant", "content": "The best answer is ("}
        ]
        ```

        Then the response `content` might be:

        ```json
        [{"type": "text", "text": "B)"}]
        ```

        - `beta_text_block: object { citations, text, type }`

          - `citations: array of BetaTextCitation`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `beta_citation_char_location: object { cited_text, document_index, document_title, 4 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_char_index: number`

              - `file_id: string`

              - `start_char_index: number`

              - `type: "char_location"`

            - `beta_citation_page_location: object { cited_text, document_index, document_title, 4 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_page_number: number`

              - `file_id: string`

              - `start_page_number: number`

              - `type: "page_location"`

            - `beta_citation_content_block_location: object { cited_text, document_index, document_title, 4 more }`

              - `cited_text: string`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `document_index: number`

              - `document_title: string`

              - `end_block_index: number`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `file_id: string`

              - `start_block_index: number`

                0-based index of the first cited block in the source's `content` array.

              - `type: "content_block_location"`

            - `beta_citations_web_search_result_location: object { cited_text, encrypted_index, title, 2 more }`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string`

              - `type: "web_search_result_location"`

              - `url: string`

            - `beta_citation_search_result_location: object { cited_text, end_block_index, search_result_index, 4 more }`

              - `cited_text: string`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `end_block_index: number`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `search_result_index: number`

                0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                Counted separately from `document_index`; server-side web search results are not included in this count.

              - `source: string`

              - `start_block_index: number`

                0-based index of the first cited block in the source's `content` array.

              - `title: string`

              - `type: "search_result_location"`

          - `text: string`

          - `type: "text"`

        - `beta_thinking_block: object { signature, thinking, type }`

          - `signature: string`

          - `thinking: string`

          - `type: "thinking"`

        - `beta_redacted_thinking_block: object { data, type }`

          - `data: string`

          - `type: "redacted_thinking"`

        - `beta_tool_use_block: object { id, input, name, 2 more }`

          - `id: string`

          - `input: map[unknown]`

          - `name: string`

          - `type: "tool_use"`

          - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

            Tool invocation directly from the model.

            - `beta_direct_caller: object { type }`

              Tool invocation directly from the model.

              - `type: "direct"`

            - `beta_server_tool_caller: object { tool_id, type }`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

              - `type: "code_execution_20250825"`

            - `beta_server_tool_caller_20260120: object { tool_id, type }`

              - `tool_id: string`

              - `type: "code_execution_20260120"`

        - `beta_server_tool_use_block: object { id, input, name, 2 more }`

          - `id: string`

          - `input: map[unknown]`

          - `name: "advisor" or "web_search" or "web_fetch" or 5 more`

            - `"advisor"`

            - `"web_search"`

            - `"web_fetch"`

            - `"code_execution"`

            - `"bash_code_execution"`

            - `"text_editor_code_execution"`

            - `"tool_search_tool_regex"`

            - `"tool_search_tool_bm25"`

          - `type: "server_tool_use"`

          - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

            Tool invocation directly from the model.

            - `beta_direct_caller: object { type }`

              Tool invocation directly from the model.

            - `beta_server_tool_caller: object { tool_id, type }`

              Tool invocation generated by a server-side tool.

            - `beta_server_tool_caller_20260120: object { tool_id, type }`

        - `beta_web_search_tool_result_block: object { content, tool_use_id, type, caller }`

          - `content: BetaWebSearchToolResultError or array of BetaWebSearchResultBlock`

            - `beta_web_search_tool_result_error: object { error_code, type }`

              - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"max_uses_exceeded"`

                - `"too_many_requests"`

                - `"query_too_long"`

                - `"request_too_large"`

              - `type: "web_search_tool_result_error"`

            - `union_member_1: array of BetaWebSearchResultBlock`

              - `encrypted_content: string`

              - `page_age: string`

              - `title: string`

              - `type: "web_search_result"`

              - `url: string`

          - `tool_use_id: string`

          - `type: "web_search_tool_result"`

          - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

            Tool invocation directly from the model.

            - `beta_direct_caller: object { type }`

              Tool invocation directly from the model.

            - `beta_server_tool_caller: object { tool_id, type }`

              Tool invocation generated by a server-side tool.

            - `beta_server_tool_caller_20260120: object { tool_id, type }`

        - `beta_web_fetch_tool_result_block: object { content, tool_use_id, type, caller }`

          - `content: BetaWebFetchToolResultErrorBlock or BetaWebFetchBlock`

            - `beta_web_fetch_tool_result_error_block: object { error_code, type }`

              - `error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 6 more`

                - `"invalid_tool_input"`

                - `"url_too_long"`

                - `"url_not_allowed"`

                - `"url_not_in_prior_context"`

                - `"url_not_accessible"`

                - `"unsupported_content_type"`

                - `"too_many_requests"`

                - `"max_uses_exceeded"`

                - `"unavailable"`

              - `type: "web_fetch_tool_result_error"`

            - `beta_web_fetch_block: object { content, retrieved_at, type, url }`

              - `content: object { citations, source, title, type }`

                - `citations: object { enabled }`

                  Citation configuration for the document

                  - `enabled: boolean`

                - `source: BetaBase64PDFSource or BetaPlainTextSource`

                  - `beta_base64_pdf_source: object { data, media_type, type }`

                    - `data: string`

                    - `media_type: "application/pdf"`

                    - `type: "base64"`

                  - `beta_plain_text_source: object { data, media_type, type }`

                    - `data: string`

                    - `media_type: "text/plain"`

                    - `type: "text"`

                - `title: string`

                  The title of the document

                - `type: "document"`

              - `retrieved_at: string`

                ISO 8601 timestamp when the content was retrieved

              - `type: "web_fetch_result"`

              - `url: string`

                Fetched content URL

          - `tool_use_id: string`

          - `type: "web_fetch_tool_result"`

          - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

            Tool invocation directly from the model.

            - `beta_direct_caller: object { type }`

              Tool invocation directly from the model.

            - `beta_server_tool_caller: object { tool_id, type }`

              Tool invocation generated by a server-side tool.

            - `beta_server_tool_caller_20260120: object { tool_id, type }`

        - `beta_advisor_tool_result_block: object { content, tool_use_id, type }`

          - `content: BetaAdvisorToolResultError or BetaAdvisorResultBlock or BetaAdvisorRedactedResultBlock`

            - `beta_advisor_tool_result_error: object { error_code, type }`

              - `error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 4 more`

                - `"max_uses_exceeded"`

                - `"prompt_too_long"`

                - `"too_many_requests"`

                - `"overloaded"`

                - `"unavailable"`

                - `"execution_time_exceeded"`

                - `"model_not_found"`

              - `type: "advisor_tool_result_error"`

            - `beta_advisor_result_block: object { stop_reason, text, type }`

              - `stop_reason: string`

                The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

              - `text: string`

              - `type: "advisor_result"`

            - `beta_advisor_redacted_result_block: object { encrypted_content, stop_reason, type }`

              - `encrypted_content: string`

                Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

              - `stop_reason: string`

                The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

              - `type: "advisor_redacted_result"`

          - `tool_use_id: string`

          - `type: "advisor_tool_result"`

        - `beta_code_execution_tool_result_block: object { content, tool_use_id, type }`

          - `content: BetaCodeExecutionToolResultError or BetaCodeExecutionResultBlock or BetaEncryptedCodeExecutionResultBlock`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `beta_code_execution_tool_result_error: object { error_code, type }`

              - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

              - `type: "code_execution_tool_result_error"`

            - `beta_code_execution_result_block: object { content, return_code, stderr, 2 more }`

              - `content: array of BetaCodeExecutionOutputBlock`

                - `file_id: string`

                - `type: "code_execution_output"`

              - `return_code: number`

              - `stderr: string`

              - `stdout: string`

              - `type: "code_execution_result"`

            - `beta_encrypted_code_execution_result_block: object { content, encrypted_stdout, return_code, 2 more }`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `content: array of BetaCodeExecutionOutputBlock`

                - `file_id: string`

                - `type: "code_execution_output"`

              - `encrypted_stdout: string`

              - `return_code: number`

              - `stderr: string`

              - `type: "encrypted_code_execution_result"`

          - `tool_use_id: string`

          - `type: "code_execution_tool_result"`

        - `beta_bash_code_execution_tool_result_block: object { content, tool_use_id, type }`

          - `content: BetaBashCodeExecutionToolResultError or BetaBashCodeExecutionResultBlock`

            - `beta_bash_code_execution_tool_result_error: object { error_code, type }`

              - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

                - `"output_file_too_large"`

              - `type: "bash_code_execution_tool_result_error"`

            - `beta_bash_code_execution_result_block: object { content, return_code, stderr, 2 more }`

              - `content: array of BetaBashCodeExecutionOutputBlock`

                - `file_id: string`

                - `type: "bash_code_execution_output"`

              - `return_code: number`

              - `stderr: string`

              - `stdout: string`

              - `type: "bash_code_execution_result"`

          - `tool_use_id: string`

          - `type: "bash_code_execution_tool_result"`

        - `beta_text_editor_code_execution_tool_result_block: object { content, tool_use_id, type }`

          - `content: BetaTextEditorCodeExecutionToolResultError or BetaTextEditorCodeExecutionViewResultBlock or BetaTextEditorCodeExecutionCreateResultBlock or BetaTextEditorCodeExecutionStrReplaceResultBlock`

            - `beta_text_editor_code_execution_tool_result_error: object { error_code, error_message, type }`

              - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

                - `"file_not_found"`

              - `error_message: string`

              - `type: "text_editor_code_execution_tool_result_error"`

            - `beta_text_editor_code_execution_view_result_block: object { content, file_type, num_lines, 3 more }`

              - `content: string`

              - `file_type: "text" or "image" or "pdf"`

                - `"text"`

                - `"image"`

                - `"pdf"`

              - `num_lines: number`

              - `start_line: number`

              - `total_lines: number`

              - `type: "text_editor_code_execution_view_result"`

            - `beta_text_editor_code_execution_create_result_block: object { is_file_update, type }`

              - `is_file_update: boolean`

              - `type: "text_editor_code_execution_create_result"`

            - `beta_text_editor_code_execution_str_replace_result_block: object { lines, new_lines, new_start, 3 more }`

              - `lines: array of string`

              - `new_lines: number`

              - `new_start: number`

              - `old_lines: number`

              - `old_start: number`

              - `type: "text_editor_code_execution_str_replace_result"`

          - `tool_use_id: string`

          - `type: "text_editor_code_execution_tool_result"`

        - `beta_tool_search_tool_result_block: object { content, tool_use_id, type }`

          - `content: BetaToolSearchToolResultError or BetaToolSearchToolSearchResultBlock`

            - `beta_tool_search_tool_result_error: object { error_code, error_message, type }`

              - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

              - `error_message: string`

              - `type: "tool_search_tool_result_error"`

            - `beta_tool_search_tool_search_result_block: object { tool_references, type }`

              - `tool_references: array of BetaToolReferenceBlock`

                - `tool_name: string`

                - `type: "tool_reference"`

              - `type: "tool_search_tool_search_result"`

          - `tool_use_id: string`

          - `type: "tool_search_tool_result"`

        - `beta_mcp_tool_use_block: object { id, input, name, 2 more }`

          - `id: string`

          - `input: map[unknown]`

          - `name: string`

            The name of the MCP tool

          - `server_name: string`

            The name of the MCP server

          - `type: "mcp_tool_use"`

        - `beta_mcp_tool_result_block: object { content, is_error, tool_use_id, type }`

          - `content: string or array of BetaTextBlock`

            - `union_member_0: string`

            - `beta_mcp_tool_result_block_content: array of BetaTextBlock`

              - `citations: array of BetaTextCitation`

                Citations supporting the text block.

                The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `text: string`

              - `type: "text"`

          - `is_error: boolean`

          - `tool_use_id: string`

          - `type: "mcp_tool_result"`

        - `beta_container_upload_block: object { file_id, type }`

          Response model for a file uploaded to the container.

          - `file_id: string`

          - `type: "container_upload"`

        - `beta_compaction_block: object { content, encrypted_content, type }`

          A compaction block returned when autocompact is triggered.

          When content is None, it indicates the compaction failed to produce a valid
          summary (e.g., malformed output from the model). Clients may round-trip
          compaction blocks with null content; the server treats them as no-ops.

          - `content: string`

            Summary of compacted content, or null if compaction failed

          - `encrypted_content: string`

            Opaque metadata from prior compaction, to be round-tripped verbatim

          - `type: "compaction"`

        - `beta_fallback_block: object { from, to, type }`

          Marks the point in `content` where one model's output gives way to the next.

          One block appears per hop where a preceding model actually ran this turn and
          declined. A turn routed directly by the sticky decision has no such boundary
          and carries no block — the signal for whether a fallback model served the
          response is the presence of a `fallback_message` entry in
          `usage.iterations`, not this block.

          The block is treated like a server-tool content block for streaming: it
          arrives via the standard `content_block_start` / `content_block_stop`
          pair and carries no deltas.

          - `from: object { model }`

            The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

            - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

              The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `"claude-fable-5"`

                Next generation of intelligence for the hardest knowledge work and coding problems

              - `"claude-mythos-5"`

                Most capable model for cybersecurity and biology research

              - `"claude-opus-4-8"`

                Frontier intelligence for long-running agents and coding

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

          - `to: object { model }`

            The fallback model producing the content that follows this block. Its `model` is always the canonical id.

            - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

              The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `type: "fallback"`

      - `context_management: object { applied_edits }`

        Context management response.

        Information about context management strategies applied during the request.

        - `applied_edits: array of BetaClearToolUses20250919EditResponse or BetaClearThinking20251015EditResponse`

          List of context management edits that were applied.

          - `beta_clear_tool_uses_20250919_edit_response: object { cleared_input_tokens, cleared_tool_uses, type }`

            - `cleared_input_tokens: number`

              Number of input tokens cleared by this edit.

            - `cleared_tool_uses: number`

              Number of tool uses that were cleared.

            - `type: "clear_tool_uses_20250919"`

              The type of context management edit applied.

          - `beta_clear_thinking_20251015_edit_response: object { cleared_input_tokens, cleared_thinking_turns, type }`

            - `cleared_input_tokens: number`

              Number of input tokens cleared by this edit.

            - `cleared_thinking_turns: number`

              Number of thinking turns that were cleared.

            - `type: "clear_thinking_20251015"`

              The type of context management edit applied.

      - `diagnostics: object { cache_miss_reason }`

        Response envelope for request-level diagnostics. Present (possibly
        null) whenever the caller supplied `diagnostics` on the request.

        - `cache_miss_reason: BetaCacheMissModelChanged or BetaCacheMissSystemChanged or BetaCacheMissToolsChanged or 3 more`

          Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

          - `beta_cache_miss_model_changed: object { cache_missed_input_tokens, type }`

            - `cache_missed_input_tokens: number`

              Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `type: "model_changed"`

          - `beta_cache_miss_system_changed: object { cache_missed_input_tokens, type }`

            - `cache_missed_input_tokens: number`

              Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `type: "system_changed"`

          - `beta_cache_miss_tools_changed: object { cache_missed_input_tokens, type }`

            - `cache_missed_input_tokens: number`

              Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `type: "tools_changed"`

          - `beta_cache_miss_messages_changed: object { cache_missed_input_tokens, type }`

            - `cache_missed_input_tokens: number`

              Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `type: "messages_changed"`

          - `beta_cache_miss_previous_message_not_found: object { type }`

            - `type: "previous_message_not_found"`

          - `beta_cache_miss_unavailable: object { type }`

            - `type: "unavailable"`

      - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `"claude-mythos-5"`

          Most capable model for cybersecurity and biology research

        - `"claude-opus-4-8"`

          Frontier intelligence for long-running agents and coding

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

      - `role: "assistant"`

        Conversational role of the generated message.

        This will always be `"assistant"`.

      - `stop_details: object { category, explanation, fallback_credit_token, 3 more }`

        Structured information about a refusal.

        - `category: "cyber" or "bio" or "reasoning_extraction"`

          The policy category that triggered the refusal.

          `null` when the refusal doesn't map to a named category.

          - `"cyber"`

          - `"bio"`

          - `"reasoning_extraction"`

        - `explanation: string`

          Human-readable explanation of the refusal.

          This text is not guaranteed to be stable. `null` when no explanation is available for the category.

        - `fallback_credit_token: string`

          Opaque code that refunds the cache-miss cost when retrying this refused
          request on the fallback model. Pass it as `fallback_credit_token` on the
          retry request. Expires 5 minutes after the refusal.

          The retry is sent either with the same request body (`system`, `messages`,
          `tools`, and other render-shaping fields), or with the same body plus one
          appended `assistant` message whose content is the partial text (with any
          trailing whitespace stripped from the final text block) and paired
          server-tool blocks from this refusal — which also authorizes that
          appended turn as an assistant-prefill continuation on models that otherwise
          disallow prefill. A token minted mid-server-tool-loop whose partial content
          was continuable may only be redeemed the second way — if a same-body retry
          is rejected with a 400 saying the token must be redeemed by continuing the
          partial response, retry the second way instead. Either way: same workspace,
          same platform; a mismatch is a 400. Resending a token for an already-warm
          prefix is permitted but yields no additional credit.

          `null` when the refused model isn't eligible for a fallback credit.

        - `fallback_has_prefill_claim: boolean`

          Whether the accompanying `fallback_credit_token` may be redeemed with the
          appended-assistant retry form. Only set when `fallback_credit_token` is
          present.

          `true`: retry by resending the same request body plus one appended
          `assistant` message whose content is this response's `content` with any
          trailing whitespace stripped from the final text block and unpaired
          `tool_use` blocks omitted (the same appended-turn shape described on
          `fallback_credit_token`), with the token attached. `false`: retry by
          resending the original request body unchanged, with the token attached —
          the appended-assistant form is not available for this refusal (no
          continuable partial content, or the request uses `output_format` or a
          `tool_choice` that forces tool use). One exception: when the request used
          `output_format` or a forced `tool_choice` and the refusal arrived after
          server tools (including MCP connector tools) had already executed, the
          token may not be redeemable by either retry form; if the exact-body retry
          is then rejected with a 400 saying the token must be redeemed by
          continuing the partial response, discard the token and retry without it.

          Advisory: if an appended-assistant retry is rejected with a 400 despite
          `true`, fall back to resending the original request body with the token.

        - `recommended_model: string`

          The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

        - `type: "refusal"`

      - `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 5 more`

        The reason that we stopped.

        This may be one the following values:

        * `"end_turn"`: the model reached a natural stopping point
        * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
        * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
        * `"tool_use"`: the model invoked one or more tools
        * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
        * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

        In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

        - `"end_turn"`

        - `"max_tokens"`

        - `"stop_sequence"`

        - `"tool_use"`

        - `"pause_turn"`

        - `"compaction"`

        - `"refusal"`

        - `"model_context_window_exceeded"`

      - `stop_sequence: string`

        Which custom stop sequence was generated, if any.

        This value will be a non-null string if one of your custom stop sequences was generated.

      - `type: "message"`

        Object type.

        For Messages, this is always `"message"`.

      - `usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 8 more }`

        Billing and rate-limit usage.

        Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

        Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

        For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

        Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

        - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

          Breakdown of cached tokens by TTL

          - `ephemeral_1h_input_tokens: number`

            The number of input tokens used to create the 1 hour cache entry.

          - `ephemeral_5m_input_tokens: number`

            The number of input tokens used to create the 5 minute cache entry.

        - `cache_creation_input_tokens: number`

          The number of input tokens used to create the cache entry.

        - `cache_read_input_tokens: number`

          The number of input tokens read from the cache.

        - `inference_geo: string`

          The geographic region where inference was performed for this request.

        - `input_tokens: number`

          The number of input tokens which were used.

        - `iterations: array of BetaMessageIterationUsage or BetaCompactionIterationUsage or BetaAdvisorMessageIterationUsage or BetaFallbackMessageIterationUsage`

          Per-iteration token usage breakdown.

          Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

          - Determine which iterations exceeded long context thresholds (>=200k tokens)
          - Calculate the true context window size from the last iteration
          - Understand token accumulation across server-side tool use loops

          - `beta_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

            Token usage for a sampling iteration.

            - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

              Breakdown of cached tokens by TTL

              - `ephemeral_1h_input_tokens: number`

                The number of input tokens used to create the 1 hour cache entry.

              - `ephemeral_5m_input_tokens: number`

                The number of input tokens used to create the 5 minute cache entry.

            - `cache_creation_input_tokens: number`

              The number of input tokens used to create the cache entry.

            - `cache_read_input_tokens: number`

              The number of input tokens read from the cache.

            - `input_tokens: number`

              The number of input tokens which were used.

            - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

              The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `"claude-fable-5"`

                Next generation of intelligence for the hardest knowledge work and coding problems

              - `"claude-mythos-5"`

                Most capable model for cybersecurity and biology research

              - `"claude-opus-4-8"`

                Frontier intelligence for long-running agents and coding

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

            - `output_tokens: number`

              The number of output tokens which were used.

            - `type: "message"`

              Usage for a sampling iteration

          - `beta_compaction_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }`

            Token usage for a compaction iteration.

            - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

              Breakdown of cached tokens by TTL

              - `ephemeral_1h_input_tokens: number`

                The number of input tokens used to create the 1 hour cache entry.

              - `ephemeral_5m_input_tokens: number`

                The number of input tokens used to create the 5 minute cache entry.

            - `cache_creation_input_tokens: number`

              The number of input tokens used to create the cache entry.

            - `cache_read_input_tokens: number`

              The number of input tokens read from the cache.

            - `input_tokens: number`

              The number of input tokens which were used.

            - `output_tokens: number`

              The number of output tokens which were used.

            - `type: "compaction"`

              Usage for a compaction iteration

          - `beta_advisor_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

            Token usage for an advisor sub-inference iteration.

            - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

              Breakdown of cached tokens by TTL

              - `ephemeral_1h_input_tokens: number`

                The number of input tokens used to create the 1 hour cache entry.

              - `ephemeral_5m_input_tokens: number`

                The number of input tokens used to create the 5 minute cache entry.

            - `cache_creation_input_tokens: number`

              The number of input tokens used to create the cache entry.

            - `cache_read_input_tokens: number`

              The number of input tokens read from the cache.

            - `input_tokens: number`

              The number of input tokens which were used.

            - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

              The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `"claude-fable-5"`

                Next generation of intelligence for the hardest knowledge work and coding problems

              - `"claude-mythos-5"`

                Most capable model for cybersecurity and biology research

              - `"claude-opus-4-8"`

                Frontier intelligence for long-running agents and coding

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

            - `output_tokens: number`

              The number of output tokens which were used.

            - `type: "advisor_message"`

              Usage for an advisor sub-inference iteration

          - `beta_fallback_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

            Token usage for the fallback-model attempt of a server-side fallback request.

            Produced in place of a `message` entry for whichever hop served the
            response. A declined hop produces the existing `message` entry. Whether
            a fallback model served the response is signalled by the presence of this
            entry in `usage.iterations`.

            - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

              Breakdown of cached tokens by TTL

              - `ephemeral_1h_input_tokens: number`

                The number of input tokens used to create the 1 hour cache entry.

              - `ephemeral_5m_input_tokens: number`

                The number of input tokens used to create the 5 minute cache entry.

            - `cache_creation_input_tokens: number`

              The number of input tokens used to create the cache entry.

            - `cache_read_input_tokens: number`

              The number of input tokens read from the cache.

            - `input_tokens: number`

              The number of input tokens which were used.

            - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

              The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `"claude-fable-5"`

                Next generation of intelligence for the hardest knowledge work and coding problems

              - `"claude-mythos-5"`

                Most capable model for cybersecurity and biology research

              - `"claude-opus-4-8"`

                Frontier intelligence for long-running agents and coding

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

            - `output_tokens: number`

              The number of output tokens which were used.

            - `type: "fallback_message"`

              Usage for the fallback-model attempt that served the response

        - `output_tokens: number`

          The number of output tokens which were used.

        - `output_tokens_details: object { thinking_tokens }`

          Breakdown of output tokens by category.

          `output_tokens` remains the inclusive, authoritative total used for billing.
          This object provides a read-only decomposition for observability — for example,
          how many of the billed output tokens were spent on internal reasoning that may
          have been summarized before being returned to you.

          - `thinking_tokens: number`

            Number of output tokens the model generated as internal reasoning, including
            the thinking-block delimiter tokens.

            Reflects the raw reasoning the model produced, not the (possibly shorter)
            summarized thinking text returned in the response body. Computed by
            re-tokenizing the raw reasoning text, so it may differ from the model's exact
            generation count by a small number of tokens. Always ≤ `output_tokens`;
            `output_tokens - thinking_tokens` approximates the non-reasoning output.

        - `server_tool_use: object { web_fetch_requests, web_search_requests }`

          The number of server tool requests.

          - `web_fetch_requests: number`

            The number of web fetch tool requests.

          - `web_search_requests: number`

            The number of web search tool requests.

        - `service_tier: "standard" or "priority" or "batch"`

          If the request used the priority, standard, or batch tier.

          - `"standard"`

          - `"priority"`

          - `"batch"`

        - `speed: "standard" or "fast"`

          The inference speed mode used for this request.

          - `"standard"`

          - `"fast"`

    - `type: "succeeded"`

  - `beta_message_batch_errored_result: object { error, type }`

    - `error: object { error, request_id, type }`

      - `error: BetaInvalidRequestError or BetaAuthenticationError or BetaBillingError or 6 more`

        - `beta_invalid_request_error: object { message, type }`

          - `message: string`

          - `type: "invalid_request_error"`

        - `beta_authentication_error: object { message, type }`

          - `message: string`

          - `type: "authentication_error"`

        - `beta_billing_error: object { message, type }`

          - `message: string`

          - `type: "billing_error"`

        - `beta_permission_error: object { message, type }`

          - `message: string`

          - `type: "permission_error"`

        - `beta_not_found_error: object { message, type }`

          - `message: string`

          - `type: "not_found_error"`

        - `beta_rate_limit_error: object { message, type }`

          - `message: string`

          - `type: "rate_limit_error"`

        - `beta_gateway_timeout_error: object { message, type }`

          - `message: string`

          - `type: "timeout_error"`

        - `beta_api_error: object { message, type }`

          - `message: string`

          - `type: "api_error"`

        - `beta_overloaded_error: object { message, type }`

          - `message: string`

          - `type: "overloaded_error"`

      - `request_id: string`

      - `type: "error"`

    - `type: "errored"`

  - `beta_message_batch_canceled_result: object { type }`

    - `type: "canceled"`

  - `beta_message_batch_expired_result: object { type }`

    - `type: "expired"`

### Beta Message Batch Succeeded Result

- `beta_message_batch_succeeded_result: object { message, type }`

  - `message: object { id, container, content, 9 more }`

    - `id: string`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `container: object { id, expires_at, skills }`

      Information about the container used in the request (for the code execution tool)

      - `id: string`

        Identifier for the container used in this request

      - `expires_at: string`

        The time at which the container will expire.

      - `skills: array of BetaSkill`

        Skills loaded in the container

        - `skill_id: string`

          Skill ID

        - `type: "anthropic" or "custom"`

          Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

          - `"anthropic"`

          - `"custom"`

        - `version: string`

          Skill version or 'latest' for most recent version

    - `content: array of BetaContentBlock`

      Content generated by the model.

      This is an array of content blocks, each of which has a `type` that determines its shape.

      Example:

      ```json
      [{"type": "text", "text": "Hi, I'm Claude."}]
      ```

      If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

      For example, if the input `messages` were:

      ```json
      [
        {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
        {"role": "assistant", "content": "The best answer is ("}
      ]
      ```

      Then the response `content` might be:

      ```json
      [{"type": "text", "text": "B)"}]
      ```

      - `beta_text_block: object { citations, text, type }`

        - `citations: array of BetaTextCitation`

          Citations supporting the text block.

          The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `beta_citation_char_location: object { cited_text, document_index, document_title, 4 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_char_index: number`

            - `file_id: string`

            - `start_char_index: number`

            - `type: "char_location"`

          - `beta_citation_page_location: object { cited_text, document_index, document_title, 4 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_page_number: number`

            - `file_id: string`

            - `start_page_number: number`

            - `type: "page_location"`

          - `beta_citation_content_block_location: object { cited_text, document_index, document_title, 4 more }`

            - `cited_text: string`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `document_index: number`

            - `document_title: string`

            - `end_block_index: number`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `file_id: string`

            - `start_block_index: number`

              0-based index of the first cited block in the source's `content` array.

            - `type: "content_block_location"`

          - `beta_citations_web_search_result_location: object { cited_text, encrypted_index, title, 2 more }`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string`

            - `type: "web_search_result_location"`

            - `url: string`

          - `beta_citation_search_result_location: object { cited_text, end_block_index, search_result_index, 4 more }`

            - `cited_text: string`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `end_block_index: number`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `search_result_index: number`

              0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

              Counted separately from `document_index`; server-side web search results are not included in this count.

            - `source: string`

            - `start_block_index: number`

              0-based index of the first cited block in the source's `content` array.

            - `title: string`

            - `type: "search_result_location"`

        - `text: string`

        - `type: "text"`

      - `beta_thinking_block: object { signature, thinking, type }`

        - `signature: string`

        - `thinking: string`

        - `type: "thinking"`

      - `beta_redacted_thinking_block: object { data, type }`

        - `data: string`

        - `type: "redacted_thinking"`

      - `beta_tool_use_block: object { id, input, name, 2 more }`

        - `id: string`

        - `input: map[unknown]`

        - `name: string`

        - `type: "tool_use"`

        - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

          Tool invocation directly from the model.

          - `beta_direct_caller: object { type }`

            Tool invocation directly from the model.

            - `type: "direct"`

          - `beta_server_tool_caller: object { tool_id, type }`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

          - `beta_server_tool_caller_20260120: object { tool_id, type }`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

      - `beta_server_tool_use_block: object { id, input, name, 2 more }`

        - `id: string`

        - `input: map[unknown]`

        - `name: "advisor" or "web_search" or "web_fetch" or 5 more`

          - `"advisor"`

          - `"web_search"`

          - `"web_fetch"`

          - `"code_execution"`

          - `"bash_code_execution"`

          - `"text_editor_code_execution"`

          - `"tool_search_tool_regex"`

          - `"tool_search_tool_bm25"`

        - `type: "server_tool_use"`

        - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

          Tool invocation directly from the model.

          - `beta_direct_caller: object { type }`

            Tool invocation directly from the model.

          - `beta_server_tool_caller: object { tool_id, type }`

            Tool invocation generated by a server-side tool.

          - `beta_server_tool_caller_20260120: object { tool_id, type }`

      - `beta_web_search_tool_result_block: object { content, tool_use_id, type, caller }`

        - `content: BetaWebSearchToolResultError or array of BetaWebSearchResultBlock`

          - `beta_web_search_tool_result_error: object { error_code, type }`

            - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"max_uses_exceeded"`

              - `"too_many_requests"`

              - `"query_too_long"`

              - `"request_too_large"`

            - `type: "web_search_tool_result_error"`

          - `union_member_1: array of BetaWebSearchResultBlock`

            - `encrypted_content: string`

            - `page_age: string`

            - `title: string`

            - `type: "web_search_result"`

            - `url: string`

        - `tool_use_id: string`

        - `type: "web_search_tool_result"`

        - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

          Tool invocation directly from the model.

          - `beta_direct_caller: object { type }`

            Tool invocation directly from the model.

          - `beta_server_tool_caller: object { tool_id, type }`

            Tool invocation generated by a server-side tool.

          - `beta_server_tool_caller_20260120: object { tool_id, type }`

      - `beta_web_fetch_tool_result_block: object { content, tool_use_id, type, caller }`

        - `content: BetaWebFetchToolResultErrorBlock or BetaWebFetchBlock`

          - `beta_web_fetch_tool_result_error_block: object { error_code, type }`

            - `error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 6 more`

              - `"invalid_tool_input"`

              - `"url_too_long"`

              - `"url_not_allowed"`

              - `"url_not_in_prior_context"`

              - `"url_not_accessible"`

              - `"unsupported_content_type"`

              - `"too_many_requests"`

              - `"max_uses_exceeded"`

              - `"unavailable"`

            - `type: "web_fetch_tool_result_error"`

          - `beta_web_fetch_block: object { content, retrieved_at, type, url }`

            - `content: object { citations, source, title, type }`

              - `citations: object { enabled }`

                Citation configuration for the document

                - `enabled: boolean`

              - `source: BetaBase64PDFSource or BetaPlainTextSource`

                - `beta_base64_pdf_source: object { data, media_type, type }`

                  - `data: string`

                  - `media_type: "application/pdf"`

                  - `type: "base64"`

                - `beta_plain_text_source: object { data, media_type, type }`

                  - `data: string`

                  - `media_type: "text/plain"`

                  - `type: "text"`

              - `title: string`

                The title of the document

              - `type: "document"`

            - `retrieved_at: string`

              ISO 8601 timestamp when the content was retrieved

            - `type: "web_fetch_result"`

            - `url: string`

              Fetched content URL

        - `tool_use_id: string`

        - `type: "web_fetch_tool_result"`

        - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

          Tool invocation directly from the model.

          - `beta_direct_caller: object { type }`

            Tool invocation directly from the model.

          - `beta_server_tool_caller: object { tool_id, type }`

            Tool invocation generated by a server-side tool.

          - `beta_server_tool_caller_20260120: object { tool_id, type }`

      - `beta_advisor_tool_result_block: object { content, tool_use_id, type }`

        - `content: BetaAdvisorToolResultError or BetaAdvisorResultBlock or BetaAdvisorRedactedResultBlock`

          - `beta_advisor_tool_result_error: object { error_code, type }`

            - `error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 4 more`

              - `"max_uses_exceeded"`

              - `"prompt_too_long"`

              - `"too_many_requests"`

              - `"overloaded"`

              - `"unavailable"`

              - `"execution_time_exceeded"`

              - `"model_not_found"`

            - `type: "advisor_tool_result_error"`

          - `beta_advisor_result_block: object { stop_reason, text, type }`

            - `stop_reason: string`

              The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

            - `text: string`

            - `type: "advisor_result"`

          - `beta_advisor_redacted_result_block: object { encrypted_content, stop_reason, type }`

            - `encrypted_content: string`

              Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

            - `stop_reason: string`

              The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

            - `type: "advisor_redacted_result"`

        - `tool_use_id: string`

        - `type: "advisor_tool_result"`

      - `beta_code_execution_tool_result_block: object { content, tool_use_id, type }`

        - `content: BetaCodeExecutionToolResultError or BetaCodeExecutionResultBlock or BetaEncryptedCodeExecutionResultBlock`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `beta_code_execution_tool_result_error: object { error_code, type }`

            - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `type: "code_execution_tool_result_error"`

          - `beta_code_execution_result_block: object { content, return_code, stderr, 2 more }`

            - `content: array of BetaCodeExecutionOutputBlock`

              - `file_id: string`

              - `type: "code_execution_output"`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

            - `type: "code_execution_result"`

          - `beta_encrypted_code_execution_result_block: object { content, encrypted_stdout, return_code, 2 more }`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `content: array of BetaCodeExecutionOutputBlock`

              - `file_id: string`

              - `type: "code_execution_output"`

            - `encrypted_stdout: string`

            - `return_code: number`

            - `stderr: string`

            - `type: "encrypted_code_execution_result"`

        - `tool_use_id: string`

        - `type: "code_execution_tool_result"`

      - `beta_bash_code_execution_tool_result_block: object { content, tool_use_id, type }`

        - `content: BetaBashCodeExecutionToolResultError or BetaBashCodeExecutionResultBlock`

          - `beta_bash_code_execution_tool_result_error: object { error_code, type }`

            - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"output_file_too_large"`

            - `type: "bash_code_execution_tool_result_error"`

          - `beta_bash_code_execution_result_block: object { content, return_code, stderr, 2 more }`

            - `content: array of BetaBashCodeExecutionOutputBlock`

              - `file_id: string`

              - `type: "bash_code_execution_output"`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

            - `type: "bash_code_execution_result"`

        - `tool_use_id: string`

        - `type: "bash_code_execution_tool_result"`

      - `beta_text_editor_code_execution_tool_result_block: object { content, tool_use_id, type }`

        - `content: BetaTextEditorCodeExecutionToolResultError or BetaTextEditorCodeExecutionViewResultBlock or BetaTextEditorCodeExecutionCreateResultBlock or BetaTextEditorCodeExecutionStrReplaceResultBlock`

          - `beta_text_editor_code_execution_tool_result_error: object { error_code, error_message, type }`

            - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"file_not_found"`

            - `error_message: string`

            - `type: "text_editor_code_execution_tool_result_error"`

          - `beta_text_editor_code_execution_view_result_block: object { content, file_type, num_lines, 3 more }`

            - `content: string`

            - `file_type: "text" or "image" or "pdf"`

              - `"text"`

              - `"image"`

              - `"pdf"`

            - `num_lines: number`

            - `start_line: number`

            - `total_lines: number`

            - `type: "text_editor_code_execution_view_result"`

          - `beta_text_editor_code_execution_create_result_block: object { is_file_update, type }`

            - `is_file_update: boolean`

            - `type: "text_editor_code_execution_create_result"`

          - `beta_text_editor_code_execution_str_replace_result_block: object { lines, new_lines, new_start, 3 more }`

            - `lines: array of string`

            - `new_lines: number`

            - `new_start: number`

            - `old_lines: number`

            - `old_start: number`

            - `type: "text_editor_code_execution_str_replace_result"`

        - `tool_use_id: string`

        - `type: "text_editor_code_execution_tool_result"`

      - `beta_tool_search_tool_result_block: object { content, tool_use_id, type }`

        - `content: BetaToolSearchToolResultError or BetaToolSearchToolSearchResultBlock`

          - `beta_tool_search_tool_result_error: object { error_code, error_message, type }`

            - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `error_message: string`

            - `type: "tool_search_tool_result_error"`

          - `beta_tool_search_tool_search_result_block: object { tool_references, type }`

            - `tool_references: array of BetaToolReferenceBlock`

              - `tool_name: string`

              - `type: "tool_reference"`

            - `type: "tool_search_tool_search_result"`

        - `tool_use_id: string`

        - `type: "tool_search_tool_result"`

      - `beta_mcp_tool_use_block: object { id, input, name, 2 more }`

        - `id: string`

        - `input: map[unknown]`

        - `name: string`

          The name of the MCP tool

        - `server_name: string`

          The name of the MCP server

        - `type: "mcp_tool_use"`

      - `beta_mcp_tool_result_block: object { content, is_error, tool_use_id, type }`

        - `content: string or array of BetaTextBlock`

          - `union_member_0: string`

          - `beta_mcp_tool_result_block_content: array of BetaTextBlock`

            - `citations: array of BetaTextCitation`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `text: string`

            - `type: "text"`

        - `is_error: boolean`

        - `tool_use_id: string`

        - `type: "mcp_tool_result"`

      - `beta_container_upload_block: object { file_id, type }`

        Response model for a file uploaded to the container.

        - `file_id: string`

        - `type: "container_upload"`

      - `beta_compaction_block: object { content, encrypted_content, type }`

        A compaction block returned when autocompact is triggered.

        When content is None, it indicates the compaction failed to produce a valid
        summary (e.g., malformed output from the model). Clients may round-trip
        compaction blocks with null content; the server treats them as no-ops.

        - `content: string`

          Summary of compacted content, or null if compaction failed

        - `encrypted_content: string`

          Opaque metadata from prior compaction, to be round-tripped verbatim

        - `type: "compaction"`

      - `beta_fallback_block: object { from, to, type }`

        Marks the point in `content` where one model's output gives way to the next.

        One block appears per hop where a preceding model actually ran this turn and
        declined. A turn routed directly by the sticky decision has no such boundary
        and carries no block — the signal for whether a fallback model served the
        response is the presence of a `fallback_message` entry in
        `usage.iterations`, not this block.

        The block is treated like a server-tool content block for streaming: it
        arrives via the standard `content_block_start` / `content_block_stop`
        pair and carries no deltas.

        - `from: object { model }`

          The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

          - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-mythos-5"`

              Most capable model for cybersecurity and biology research

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

        - `to: object { model }`

          The fallback model producing the content that follows this block. Its `model` is always the canonical id.

          - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `type: "fallback"`

    - `context_management: object { applied_edits }`

      Context management response.

      Information about context management strategies applied during the request.

      - `applied_edits: array of BetaClearToolUses20250919EditResponse or BetaClearThinking20251015EditResponse`

        List of context management edits that were applied.

        - `beta_clear_tool_uses_20250919_edit_response: object { cleared_input_tokens, cleared_tool_uses, type }`

          - `cleared_input_tokens: number`

            Number of input tokens cleared by this edit.

          - `cleared_tool_uses: number`

            Number of tool uses that were cleared.

          - `type: "clear_tool_uses_20250919"`

            The type of context management edit applied.

        - `beta_clear_thinking_20251015_edit_response: object { cleared_input_tokens, cleared_thinking_turns, type }`

          - `cleared_input_tokens: number`

            Number of input tokens cleared by this edit.

          - `cleared_thinking_turns: number`

            Number of thinking turns that were cleared.

          - `type: "clear_thinking_20251015"`

            The type of context management edit applied.

    - `diagnostics: object { cache_miss_reason }`

      Response envelope for request-level diagnostics. Present (possibly
      null) whenever the caller supplied `diagnostics` on the request.

      - `cache_miss_reason: BetaCacheMissModelChanged or BetaCacheMissSystemChanged or BetaCacheMissToolsChanged or 3 more`

        Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

        - `beta_cache_miss_model_changed: object { cache_missed_input_tokens, type }`

          - `cache_missed_input_tokens: number`

            Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

          - `type: "model_changed"`

        - `beta_cache_miss_system_changed: object { cache_missed_input_tokens, type }`

          - `cache_missed_input_tokens: number`

            Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

          - `type: "system_changed"`

        - `beta_cache_miss_tools_changed: object { cache_missed_input_tokens, type }`

          - `cache_missed_input_tokens: number`

            Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

          - `type: "tools_changed"`

        - `beta_cache_miss_messages_changed: object { cache_missed_input_tokens, type }`

          - `cache_missed_input_tokens: number`

            Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

          - `type: "messages_changed"`

        - `beta_cache_miss_previous_message_not_found: object { type }`

          - `type: "previous_message_not_found"`

        - `beta_cache_miss_unavailable: object { type }`

          - `type: "unavailable"`

    - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5"`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `"claude-mythos-5"`

        Most capable model for cybersecurity and biology research

      - `"claude-opus-4-8"`

        Frontier intelligence for long-running agents and coding

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

    - `role: "assistant"`

      Conversational role of the generated message.

      This will always be `"assistant"`.

    - `stop_details: object { category, explanation, fallback_credit_token, 3 more }`

      Structured information about a refusal.

      - `category: "cyber" or "bio" or "reasoning_extraction"`

        The policy category that triggered the refusal.

        `null` when the refusal doesn't map to a named category.

        - `"cyber"`

        - `"bio"`

        - `"reasoning_extraction"`

      - `explanation: string`

        Human-readable explanation of the refusal.

        This text is not guaranteed to be stable. `null` when no explanation is available for the category.

      - `fallback_credit_token: string`

        Opaque code that refunds the cache-miss cost when retrying this refused
        request on the fallback model. Pass it as `fallback_credit_token` on the
        retry request. Expires 5 minutes after the refusal.

        The retry is sent either with the same request body (`system`, `messages`,
        `tools`, and other render-shaping fields), or with the same body plus one
        appended `assistant` message whose content is the partial text (with any
        trailing whitespace stripped from the final text block) and paired
        server-tool blocks from this refusal — which also authorizes that
        appended turn as an assistant-prefill continuation on models that otherwise
        disallow prefill. A token minted mid-server-tool-loop whose partial content
        was continuable may only be redeemed the second way — if a same-body retry
        is rejected with a 400 saying the token must be redeemed by continuing the
        partial response, retry the second way instead. Either way: same workspace,
        same platform; a mismatch is a 400. Resending a token for an already-warm
        prefix is permitted but yields no additional credit.

        `null` when the refused model isn't eligible for a fallback credit.

      - `fallback_has_prefill_claim: boolean`

        Whether the accompanying `fallback_credit_token` may be redeemed with the
        appended-assistant retry form. Only set when `fallback_credit_token` is
        present.

        `true`: retry by resending the same request body plus one appended
        `assistant` message whose content is this response's `content` with any
        trailing whitespace stripped from the final text block and unpaired
        `tool_use` blocks omitted (the same appended-turn shape described on
        `fallback_credit_token`), with the token attached. `false`: retry by
        resending the original request body unchanged, with the token attached —
        the appended-assistant form is not available for this refusal (no
        continuable partial content, or the request uses `output_format` or a
        `tool_choice` that forces tool use). One exception: when the request used
        `output_format` or a forced `tool_choice` and the refusal arrived after
        server tools (including MCP connector tools) had already executed, the
        token may not be redeemable by either retry form; if the exact-body retry
        is then rejected with a 400 saying the token must be redeemed by
        continuing the partial response, discard the token and retry without it.

        Advisory: if an appended-assistant retry is rejected with a 400 despite
        `true`, fall back to resending the original request body with the token.

      - `recommended_model: string`

        The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

      - `type: "refusal"`

    - `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 5 more`

      The reason that we stopped.

      This may be one the following values:

      * `"end_turn"`: the model reached a natural stopping point
      * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
      * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
      * `"tool_use"`: the model invoked one or more tools
      * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
      * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

      In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

      - `"end_turn"`

      - `"max_tokens"`

      - `"stop_sequence"`

      - `"tool_use"`

      - `"pause_turn"`

      - `"compaction"`

      - `"refusal"`

      - `"model_context_window_exceeded"`

    - `stop_sequence: string`

      Which custom stop sequence was generated, if any.

      This value will be a non-null string if one of your custom stop sequences was generated.

    - `type: "message"`

      Object type.

      For Messages, this is always `"message"`.

    - `usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 8 more }`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

        Breakdown of cached tokens by TTL

        - `ephemeral_1h_input_tokens: number`

          The number of input tokens used to create the 1 hour cache entry.

        - `ephemeral_5m_input_tokens: number`

          The number of input tokens used to create the 5 minute cache entry.

      - `cache_creation_input_tokens: number`

        The number of input tokens used to create the cache entry.

      - `cache_read_input_tokens: number`

        The number of input tokens read from the cache.

      - `inference_geo: string`

        The geographic region where inference was performed for this request.

      - `input_tokens: number`

        The number of input tokens which were used.

      - `iterations: array of BetaMessageIterationUsage or BetaCompactionIterationUsage or BetaAdvisorMessageIterationUsage or BetaFallbackMessageIterationUsage`

        Per-iteration token usage breakdown.

        Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

        - Determine which iterations exceeded long context thresholds (>=200k tokens)
        - Calculate the true context window size from the last iteration
        - Understand token accumulation across server-side tool use loops

        - `beta_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

          Token usage for a sampling iteration.

          - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

          - `cache_creation_input_tokens: number`

            The number of input tokens used to create the cache entry.

          - `cache_read_input_tokens: number`

            The number of input tokens read from the cache.

          - `input_tokens: number`

            The number of input tokens which were used.

          - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-mythos-5"`

              Most capable model for cybersecurity and biology research

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

          - `output_tokens: number`

            The number of output tokens which were used.

          - `type: "message"`

            Usage for a sampling iteration

        - `beta_compaction_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }`

          Token usage for a compaction iteration.

          - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

          - `cache_creation_input_tokens: number`

            The number of input tokens used to create the cache entry.

          - `cache_read_input_tokens: number`

            The number of input tokens read from the cache.

          - `input_tokens: number`

            The number of input tokens which were used.

          - `output_tokens: number`

            The number of output tokens which were used.

          - `type: "compaction"`

            Usage for a compaction iteration

        - `beta_advisor_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

          Token usage for an advisor sub-inference iteration.

          - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

          - `cache_creation_input_tokens: number`

            The number of input tokens used to create the cache entry.

          - `cache_read_input_tokens: number`

            The number of input tokens read from the cache.

          - `input_tokens: number`

            The number of input tokens which were used.

          - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-mythos-5"`

              Most capable model for cybersecurity and biology research

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

          - `output_tokens: number`

            The number of output tokens which were used.

          - `type: "advisor_message"`

            Usage for an advisor sub-inference iteration

        - `beta_fallback_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

          Token usage for the fallback-model attempt of a server-side fallback request.

          Produced in place of a `message` entry for whichever hop served the
          response. A declined hop produces the existing `message` entry. Whether
          a fallback model served the response is signalled by the presence of this
          entry in `usage.iterations`.

          - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

          - `cache_creation_input_tokens: number`

            The number of input tokens used to create the cache entry.

          - `cache_read_input_tokens: number`

            The number of input tokens read from the cache.

          - `input_tokens: number`

            The number of input tokens which were used.

          - `model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-mythos-5"`

              Most capable model for cybersecurity and biology research

            - `"claude-opus-4-8"`

              Frontier intelligence for long-running agents and coding

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

          - `output_tokens: number`

            The number of output tokens which were used.

          - `type: "fallback_message"`

            Usage for the fallback-model attempt that served the response

      - `output_tokens: number`

        The number of output tokens which were used.

      - `output_tokens_details: object { thinking_tokens }`

        Breakdown of output tokens by category.

        `output_tokens` remains the inclusive, authoritative total used for billing.
        This object provides a read-only decomposition for observability — for example,
        how many of the billed output tokens were spent on internal reasoning that may
        have been summarized before being returned to you.

        - `thinking_tokens: number`

          Number of output tokens the model generated as internal reasoning, including
          the thinking-block delimiter tokens.

          Reflects the raw reasoning the model produced, not the (possibly shorter)
          summarized thinking text returned in the response body. Computed by
          re-tokenizing the raw reasoning text, so it may differ from the model's exact
          generation count by a small number of tokens. Always ≤ `output_tokens`;
          `output_tokens - thinking_tokens` approximates the non-reasoning output.

      - `server_tool_use: object { web_fetch_requests, web_search_requests }`

        The number of server tool requests.

        - `web_fetch_requests: number`

          The number of web fetch tool requests.

        - `web_search_requests: number`

          The number of web search tool requests.

      - `service_tier: "standard" or "priority" or "batch"`

        If the request used the priority, standard, or batch tier.

        - `"standard"`

        - `"priority"`

        - `"batch"`

      - `speed: "standard" or "fast"`

        The inference speed mode used for this request.

        - `"standard"`

        - `"fast"`

  - `type: "succeeded"`

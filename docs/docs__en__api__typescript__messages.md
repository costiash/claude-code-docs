# Messages

## Create

`client.messages.create(MessageCreateParamsbody, RequestOptionsoptions?): Message | Stream<RawMessageStreamEvent>`

**post** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

### Parameters

- `MessageCreateParams = MessageCreateParamsNonStreaming | MessageCreateParamsStreaming`

  - `MessageCreateParamsBase`

    - `max_tokens: number`

      The maximum number of tokens to generate before stopping.

      Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

      Different models have different maximum values for this parameter.  See [models](https://docs.claude.com/en/docs/models-overview) for details.

    - `messages: Array<MessageParam>`

      Input messages.

      Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

      Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

      If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

      Example with a single `user` message:

      ```json
      [{"role": "user", "content": "Hello, Claude"}]
      ```

      Example with multiple conversational turns:

      ```json
      [
        {"role": "user", "content": "Hello there."},
        {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
        {"role": "user", "content": "Can you explain LLMs in plain English?"},
      ]
      ```

      Example with a partially-filled response from Claude:

      ```json
      [
        {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
        {"role": "assistant", "content": "The best answer is ("},
      ]
      ```

      Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

      ```json
      {"role": "user", "content": "Hello, Claude"}
      ```

      ```json
      {"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
      ```

      See [input examples](https://docs.claude.com/en/api/messages-examples).

      Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

      There is a limit of 100,000 messages in a single request.

      - `content: string | Array<ContentBlockParam>`

        - `string`

        - `Array<ContentBlockParam>`

          - `TextBlockParam`

            - `text: string`

            - `type: "text"`

              - `"text"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `citations?: Array<TextCitationParam> | null`

              - `CitationCharLocationParam`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_char_index: number`

                - `start_char_index: number`

                - `type: "char_location"`

                  - `"char_location"`

              - `CitationPageLocationParam`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_page_number: number`

                - `start_page_number: number`

                - `type: "page_location"`

                  - `"page_location"`

              - `CitationContentBlockLocationParam`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_block_index: number`

                - `start_block_index: number`

                - `type: "content_block_location"`

                  - `"content_block_location"`

              - `CitationWebSearchResultLocationParam`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string | null`

                - `type: "web_search_result_location"`

                  - `"web_search_result_location"`

                - `url: string`

              - `CitationSearchResultLocationParam`

                - `cited_text: string`

                - `end_block_index: number`

                - `search_result_index: number`

                - `source: string`

                - `start_block_index: number`

                - `title: string | null`

                - `type: "search_result_location"`

                  - `"search_result_location"`

          - `ImageBlockParam`

            - `source: Base64ImageSource | URLImageSource`

              - `Base64ImageSource`

                - `data: string`

                - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                  - `"image/jpeg"`

                  - `"image/png"`

                  - `"image/gif"`

                  - `"image/webp"`

                - `type: "base64"`

                  - `"base64"`

              - `URLImageSource`

                - `type: "url"`

                  - `"url"`

                - `url: string`

            - `type: "image"`

              - `"image"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

          - `DocumentBlockParam`

            - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

              - `Base64PDFSource`

                - `data: string`

                - `media_type: "application/pdf"`

                  - `"application/pdf"`

                - `type: "base64"`

                  - `"base64"`

              - `PlainTextSource`

                - `data: string`

                - `media_type: "text/plain"`

                  - `"text/plain"`

                - `type: "text"`

                  - `"text"`

              - `ContentBlockSource`

                - `content: string | Array<ContentBlockSourceContent>`

                  - `string`

                  - `Array<ContentBlockSourceContent>`

                    - `TextBlockParam`

                      - `text: string`

                      - `type: "text"`

                        - `"text"`

                      - `cache_control?: CacheControlEphemeral | null`

                        Create a cache control breakpoint at this content block.

                        - `type: "ephemeral"`

                          - `"ephemeral"`

                        - `ttl?: "5m" | "1h"`

                          The time-to-live for the cache control breakpoint.

                          This may be one the following values:

                          - `5m`: 5 minutes
                          - `1h`: 1 hour

                          Defaults to `5m`.

                          - `"5m"`

                          - `"1h"`

                      - `citations?: Array<TextCitationParam> | null`

                        - `CitationCharLocationParam`

                          - `cited_text: string`

                          - `document_index: number`

                          - `document_title: string | null`

                          - `end_char_index: number`

                          - `start_char_index: number`

                          - `type: "char_location"`

                            - `"char_location"`

                        - `CitationPageLocationParam`

                          - `cited_text: string`

                          - `document_index: number`

                          - `document_title: string | null`

                          - `end_page_number: number`

                          - `start_page_number: number`

                          - `type: "page_location"`

                            - `"page_location"`

                        - `CitationContentBlockLocationParam`

                          - `cited_text: string`

                          - `document_index: number`

                          - `document_title: string | null`

                          - `end_block_index: number`

                          - `start_block_index: number`

                          - `type: "content_block_location"`

                            - `"content_block_location"`

                        - `CitationWebSearchResultLocationParam`

                          - `cited_text: string`

                          - `encrypted_index: string`

                          - `title: string | null`

                          - `type: "web_search_result_location"`

                            - `"web_search_result_location"`

                          - `url: string`

                        - `CitationSearchResultLocationParam`

                          - `cited_text: string`

                          - `end_block_index: number`

                          - `search_result_index: number`

                          - `source: string`

                          - `start_block_index: number`

                          - `title: string | null`

                          - `type: "search_result_location"`

                            - `"search_result_location"`

                    - `ImageBlockParam`

                      - `source: Base64ImageSource | URLImageSource`

                        - `Base64ImageSource`

                          - `data: string`

                          - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                            - `"image/jpeg"`

                            - `"image/png"`

                            - `"image/gif"`

                            - `"image/webp"`

                          - `type: "base64"`

                            - `"base64"`

                        - `URLImageSource`

                          - `type: "url"`

                            - `"url"`

                          - `url: string`

                      - `type: "image"`

                        - `"image"`

                      - `cache_control?: CacheControlEphemeral | null`

                        Create a cache control breakpoint at this content block.

                        - `type: "ephemeral"`

                          - `"ephemeral"`

                        - `ttl?: "5m" | "1h"`

                          The time-to-live for the cache control breakpoint.

                          This may be one the following values:

                          - `5m`: 5 minutes
                          - `1h`: 1 hour

                          Defaults to `5m`.

                          - `"5m"`

                          - `"1h"`

                - `type: "content"`

                  - `"content"`

              - `URLPDFSource`

                - `type: "url"`

                  - `"url"`

                - `url: string`

            - `type: "document"`

              - `"document"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `citations?: CitationsConfigParam | null`

              - `enabled?: boolean`

            - `context?: string | null`

            - `title?: string | null`

          - `SearchResultBlockParam`

            - `content: Array<TextBlockParam>`

              - `text: string`

              - `type: "text"`

                - `"text"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations?: Array<TextCitationParam> | null`

                - `CitationCharLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_char_index: number`

                  - `start_char_index: number`

                  - `type: "char_location"`

                    - `"char_location"`

                - `CitationPageLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_page_number: number`

                  - `start_page_number: number`

                  - `type: "page_location"`

                    - `"page_location"`

                - `CitationContentBlockLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_block_index: number`

                  - `start_block_index: number`

                  - `type: "content_block_location"`

                    - `"content_block_location"`

                - `CitationWebSearchResultLocationParam`

                  - `cited_text: string`

                  - `encrypted_index: string`

                  - `title: string | null`

                  - `type: "web_search_result_location"`

                    - `"web_search_result_location"`

                  - `url: string`

                - `CitationSearchResultLocationParam`

                  - `cited_text: string`

                  - `end_block_index: number`

                  - `search_result_index: number`

                  - `source: string`

                  - `start_block_index: number`

                  - `title: string | null`

                  - `type: "search_result_location"`

                    - `"search_result_location"`

            - `source: string`

            - `title: string`

            - `type: "search_result"`

              - `"search_result"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `citations?: CitationsConfigParam`

              - `enabled?: boolean`

          - `ThinkingBlockParam`

            - `signature: string`

            - `thinking: string`

            - `type: "thinking"`

              - `"thinking"`

          - `RedactedThinkingBlockParam`

            - `data: string`

            - `type: "redacted_thinking"`

              - `"redacted_thinking"`

          - `ToolUseBlockParam`

            - `id: string`

            - `input: Record<string, unknown>`

            - `name: string`

            - `type: "tool_use"`

              - `"tool_use"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `DirectCaller`

                Tool invocation directly from the model.

                - `type: "direct"`

                  - `"direct"`

              - `ServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

                  - `"code_execution_20250825"`

              - `ServerToolCaller20260120`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

                  - `"code_execution_20260120"`

          - `ToolResultBlockParam`

            - `tool_use_id: string`

            - `type: "tool_result"`

              - `"tool_result"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `content?: string | Array<TextBlockParam | ImageBlockParam | SearchResultBlockParam | 2 more>`

              - `string`

              - `Array<TextBlockParam | ImageBlockParam | SearchResultBlockParam | 2 more>`

                - `TextBlockParam`

                  - `text: string`

                  - `type: "text"`

                    - `"text"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

                  - `citations?: Array<TextCitationParam> | null`

                    - `CitationCharLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_char_index: number`

                      - `start_char_index: number`

                      - `type: "char_location"`

                        - `"char_location"`

                    - `CitationPageLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_page_number: number`

                      - `start_page_number: number`

                      - `type: "page_location"`

                        - `"page_location"`

                    - `CitationContentBlockLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_block_index: number`

                      - `start_block_index: number`

                      - `type: "content_block_location"`

                        - `"content_block_location"`

                    - `CitationWebSearchResultLocationParam`

                      - `cited_text: string`

                      - `encrypted_index: string`

                      - `title: string | null`

                      - `type: "web_search_result_location"`

                        - `"web_search_result_location"`

                      - `url: string`

                    - `CitationSearchResultLocationParam`

                      - `cited_text: string`

                      - `end_block_index: number`

                      - `search_result_index: number`

                      - `source: string`

                      - `start_block_index: number`

                      - `title: string | null`

                      - `type: "search_result_location"`

                        - `"search_result_location"`

                - `ImageBlockParam`

                  - `source: Base64ImageSource | URLImageSource`

                    - `Base64ImageSource`

                      - `data: string`

                      - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                        - `"image/jpeg"`

                        - `"image/png"`

                        - `"image/gif"`

                        - `"image/webp"`

                      - `type: "base64"`

                        - `"base64"`

                    - `URLImageSource`

                      - `type: "url"`

                        - `"url"`

                      - `url: string`

                  - `type: "image"`

                    - `"image"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

                - `SearchResultBlockParam`

                  - `content: Array<TextBlockParam>`

                    - `text: string`

                    - `type: "text"`

                      - `"text"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

                    - `citations?: Array<TextCitationParam> | null`

                      - `CitationCharLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_char_index: number`

                        - `start_char_index: number`

                        - `type: "char_location"`

                          - `"char_location"`

                      - `CitationPageLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_page_number: number`

                        - `start_page_number: number`

                        - `type: "page_location"`

                          - `"page_location"`

                      - `CitationContentBlockLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_block_index: number`

                        - `start_block_index: number`

                        - `type: "content_block_location"`

                          - `"content_block_location"`

                      - `CitationWebSearchResultLocationParam`

                        - `cited_text: string`

                        - `encrypted_index: string`

                        - `title: string | null`

                        - `type: "web_search_result_location"`

                          - `"web_search_result_location"`

                        - `url: string`

                      - `CitationSearchResultLocationParam`

                        - `cited_text: string`

                        - `end_block_index: number`

                        - `search_result_index: number`

                        - `source: string`

                        - `start_block_index: number`

                        - `title: string | null`

                        - `type: "search_result_location"`

                          - `"search_result_location"`

                  - `source: string`

                  - `title: string`

                  - `type: "search_result"`

                    - `"search_result"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

                  - `citations?: CitationsConfigParam`

                    - `enabled?: boolean`

                - `DocumentBlockParam`

                  - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

                    - `Base64PDFSource`

                      - `data: string`

                      - `media_type: "application/pdf"`

                        - `"application/pdf"`

                      - `type: "base64"`

                        - `"base64"`

                    - `PlainTextSource`

                      - `data: string`

                      - `media_type: "text/plain"`

                        - `"text/plain"`

                      - `type: "text"`

                        - `"text"`

                    - `ContentBlockSource`

                      - `content: string | Array<ContentBlockSourceContent>`

                        - `string`

                        - `Array<ContentBlockSourceContent>`

                          - `TextBlockParam`

                            - `text: string`

                            - `type: "text"`

                              - `"text"`

                            - `cache_control?: CacheControlEphemeral | null`

                              Create a cache control breakpoint at this content block.

                              - `type: "ephemeral"`

                                - `"ephemeral"`

                              - `ttl?: "5m" | "1h"`

                                The time-to-live for the cache control breakpoint.

                                This may be one the following values:

                                - `5m`: 5 minutes
                                - `1h`: 1 hour

                                Defaults to `5m`.

                                - `"5m"`

                                - `"1h"`

                            - `citations?: Array<TextCitationParam> | null`

                              - `CitationCharLocationParam`

                                - `cited_text: string`

                                - `document_index: number`

                                - `document_title: string | null`

                                - `end_char_index: number`

                                - `start_char_index: number`

                                - `type: "char_location"`

                                  - `"char_location"`

                              - `CitationPageLocationParam`

                                - `cited_text: string`

                                - `document_index: number`

                                - `document_title: string | null`

                                - `end_page_number: number`

                                - `start_page_number: number`

                                - `type: "page_location"`

                                  - `"page_location"`

                              - `CitationContentBlockLocationParam`

                                - `cited_text: string`

                                - `document_index: number`

                                - `document_title: string | null`

                                - `end_block_index: number`

                                - `start_block_index: number`

                                - `type: "content_block_location"`

                                  - `"content_block_location"`

                              - `CitationWebSearchResultLocationParam`

                                - `cited_text: string`

                                - `encrypted_index: string`

                                - `title: string | null`

                                - `type: "web_search_result_location"`

                                  - `"web_search_result_location"`

                                - `url: string`

                              - `CitationSearchResultLocationParam`

                                - `cited_text: string`

                                - `end_block_index: number`

                                - `search_result_index: number`

                                - `source: string`

                                - `start_block_index: number`

                                - `title: string | null`

                                - `type: "search_result_location"`

                                  - `"search_result_location"`

                          - `ImageBlockParam`

                            - `source: Base64ImageSource | URLImageSource`

                              - `Base64ImageSource`

                                - `data: string`

                                - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                                  - `"image/jpeg"`

                                  - `"image/png"`

                                  - `"image/gif"`

                                  - `"image/webp"`

                                - `type: "base64"`

                                  - `"base64"`

                              - `URLImageSource`

                                - `type: "url"`

                                  - `"url"`

                                - `url: string`

                            - `type: "image"`

                              - `"image"`

                            - `cache_control?: CacheControlEphemeral | null`

                              Create a cache control breakpoint at this content block.

                              - `type: "ephemeral"`

                                - `"ephemeral"`

                              - `ttl?: "5m" | "1h"`

                                The time-to-live for the cache control breakpoint.

                                This may be one the following values:

                                - `5m`: 5 minutes
                                - `1h`: 1 hour

                                Defaults to `5m`.

                                - `"5m"`

                                - `"1h"`

                      - `type: "content"`

                        - `"content"`

                    - `URLPDFSource`

                      - `type: "url"`

                        - `"url"`

                      - `url: string`

                  - `type: "document"`

                    - `"document"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

                  - `citations?: CitationsConfigParam | null`

                    - `enabled?: boolean`

                  - `context?: string | null`

                  - `title?: string | null`

                - `ToolReferenceBlockParam`

                  Tool reference block that can be included in tool_result content.

                  - `tool_name: string`

                  - `type: "tool_reference"`

                    - `"tool_reference"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

            - `is_error?: boolean`

          - `ServerToolUseBlockParam`

            - `id: string`

            - `input: Record<string, unknown>`

            - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

              - `"web_search"`

              - `"web_fetch"`

              - `"code_execution"`

              - `"bash_code_execution"`

              - `"text_editor_code_execution"`

              - `"tool_search_tool_regex"`

              - `"tool_search_tool_bm25"`

            - `type: "server_tool_use"`

              - `"server_tool_use"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `DirectCaller`

                Tool invocation directly from the model.

                - `type: "direct"`

                  - `"direct"`

              - `ServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

                  - `"code_execution_20250825"`

              - `ServerToolCaller20260120`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

                  - `"code_execution_20260120"`

          - `WebSearchToolResultBlockParam`

            - `content: WebSearchToolResultBlockParamContent`

              - `Array<WebSearchResultBlockParam>`

                - `encrypted_content: string`

                - `title: string`

                - `type: "web_search_result"`

                  - `"web_search_result"`

                - `url: string`

                - `page_age?: string | null`

              - `WebSearchToolRequestError`

                - `error_code: WebSearchToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"max_uses_exceeded"`

                  - `"too_many_requests"`

                  - `"query_too_long"`

                  - `"request_too_large"`

                - `type: "web_search_tool_result_error"`

                  - `"web_search_tool_result_error"`

            - `tool_use_id: string`

            - `type: "web_search_tool_result"`

              - `"web_search_tool_result"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `DirectCaller`

                Tool invocation directly from the model.

                - `type: "direct"`

                  - `"direct"`

              - `ServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

                  - `"code_execution_20250825"`

              - `ServerToolCaller20260120`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

                  - `"code_execution_20260120"`

          - `WebFetchToolResultBlockParam`

            - `content: WebFetchToolResultErrorBlockParam | WebFetchBlockParam`

              - `WebFetchToolResultErrorBlockParam`

                - `error_code: WebFetchToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"url_too_long"`

                  - `"url_not_allowed"`

                  - `"url_not_accessible"`

                  - `"unsupported_content_type"`

                  - `"too_many_requests"`

                  - `"max_uses_exceeded"`

                  - `"unavailable"`

                - `type: "web_fetch_tool_result_error"`

                  - `"web_fetch_tool_result_error"`

              - `WebFetchBlockParam`

                - `content: DocumentBlockParam`

                  - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

                    - `Base64PDFSource`

                      - `data: string`

                      - `media_type: "application/pdf"`

                        - `"application/pdf"`

                      - `type: "base64"`

                        - `"base64"`

                    - `PlainTextSource`

                      - `data: string`

                      - `media_type: "text/plain"`

                        - `"text/plain"`

                      - `type: "text"`

                        - `"text"`

                    - `ContentBlockSource`

                      - `content: string | Array<ContentBlockSourceContent>`

                        - `string`

                        - `Array<ContentBlockSourceContent>`

                          - `TextBlockParam`

                            - `text: string`

                            - `type: "text"`

                              - `"text"`

                            - `cache_control?: CacheControlEphemeral | null`

                              Create a cache control breakpoint at this content block.

                              - `type: "ephemeral"`

                                - `"ephemeral"`

                              - `ttl?: "5m" | "1h"`

                                The time-to-live for the cache control breakpoint.

                                This may be one the following values:

                                - `5m`: 5 minutes
                                - `1h`: 1 hour

                                Defaults to `5m`.

                                - `"5m"`

                                - `"1h"`

                            - `citations?: Array<TextCitationParam> | null`

                              - `CitationCharLocationParam`

                                - `cited_text: string`

                                - `document_index: number`

                                - `document_title: string | null`

                                - `end_char_index: number`

                                - `start_char_index: number`

                                - `type: "char_location"`

                                  - `"char_location"`

                              - `CitationPageLocationParam`

                                - `cited_text: string`

                                - `document_index: number`

                                - `document_title: string | null`

                                - `end_page_number: number`

                                - `start_page_number: number`

                                - `type: "page_location"`

                                  - `"page_location"`

                              - `CitationContentBlockLocationParam`

                                - `cited_text: string`

                                - `document_index: number`

                                - `document_title: string | null`

                                - `end_block_index: number`

                                - `start_block_index: number`

                                - `type: "content_block_location"`

                                  - `"content_block_location"`

                              - `CitationWebSearchResultLocationParam`

                                - `cited_text: string`

                                - `encrypted_index: string`

                                - `title: string | null`

                                - `type: "web_search_result_location"`

                                  - `"web_search_result_location"`

                                - `url: string`

                              - `CitationSearchResultLocationParam`

                                - `cited_text: string`

                                - `end_block_index: number`

                                - `search_result_index: number`

                                - `source: string`

                                - `start_block_index: number`

                                - `title: string | null`

                                - `type: "search_result_location"`

                                  - `"search_result_location"`

                          - `ImageBlockParam`

                            - `source: Base64ImageSource | URLImageSource`

                              - `Base64ImageSource`

                                - `data: string`

                                - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                                  - `"image/jpeg"`

                                  - `"image/png"`

                                  - `"image/gif"`

                                  - `"image/webp"`

                                - `type: "base64"`

                                  - `"base64"`

                              - `URLImageSource`

                                - `type: "url"`

                                  - `"url"`

                                - `url: string`

                            - `type: "image"`

                              - `"image"`

                            - `cache_control?: CacheControlEphemeral | null`

                              Create a cache control breakpoint at this content block.

                              - `type: "ephemeral"`

                                - `"ephemeral"`

                              - `ttl?: "5m" | "1h"`

                                The time-to-live for the cache control breakpoint.

                                This may be one the following values:

                                - `5m`: 5 minutes
                                - `1h`: 1 hour

                                Defaults to `5m`.

                                - `"5m"`

                                - `"1h"`

                      - `type: "content"`

                        - `"content"`

                    - `URLPDFSource`

                      - `type: "url"`

                        - `"url"`

                      - `url: string`

                  - `type: "document"`

                    - `"document"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

                  - `citations?: CitationsConfigParam | null`

                    - `enabled?: boolean`

                  - `context?: string | null`

                  - `title?: string | null`

                - `type: "web_fetch_result"`

                  - `"web_fetch_result"`

                - `url: string`

                  Fetched content URL

                - `retrieved_at?: string | null`

                  ISO 8601 timestamp when the content was retrieved

            - `tool_use_id: string`

            - `type: "web_fetch_tool_result"`

              - `"web_fetch_tool_result"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `DirectCaller`

                Tool invocation directly from the model.

                - `type: "direct"`

                  - `"direct"`

              - `ServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

                  - `"code_execution_20250825"`

              - `ServerToolCaller20260120`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

                  - `"code_execution_20260120"`

          - `CodeExecutionToolResultBlockParam`

            - `content: CodeExecutionToolResultBlockParamContent`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `CodeExecutionToolResultErrorParam`

                - `error_code: CodeExecutionToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `type: "code_execution_tool_result_error"`

                  - `"code_execution_tool_result_error"`

              - `CodeExecutionResultBlockParam`

                - `content: Array<CodeExecutionOutputBlockParam>`

                  - `file_id: string`

                  - `type: "code_execution_output"`

                    - `"code_execution_output"`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

                - `type: "code_execution_result"`

                  - `"code_execution_result"`

              - `EncryptedCodeExecutionResultBlockParam`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `content: Array<CodeExecutionOutputBlockParam>`

                  - `file_id: string`

                  - `type: "code_execution_output"`

                    - `"code_execution_output"`

                - `encrypted_stdout: string`

                - `return_code: number`

                - `stderr: string`

                - `type: "encrypted_code_execution_result"`

                  - `"encrypted_code_execution_result"`

            - `tool_use_id: string`

            - `type: "code_execution_tool_result"`

              - `"code_execution_tool_result"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

          - `BashCodeExecutionToolResultBlockParam`

            - `content: BashCodeExecutionToolResultErrorParam | BashCodeExecutionResultBlockParam`

              - `BashCodeExecutionToolResultErrorParam`

                - `error_code: BashCodeExecutionToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"output_file_too_large"`

                - `type: "bash_code_execution_tool_result_error"`

                  - `"bash_code_execution_tool_result_error"`

              - `BashCodeExecutionResultBlockParam`

                - `content: Array<BashCodeExecutionOutputBlockParam>`

                  - `file_id: string`

                  - `type: "bash_code_execution_output"`

                    - `"bash_code_execution_output"`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

                - `type: "bash_code_execution_result"`

                  - `"bash_code_execution_result"`

            - `tool_use_id: string`

            - `type: "bash_code_execution_tool_result"`

              - `"bash_code_execution_tool_result"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

          - `TextEditorCodeExecutionToolResultBlockParam`

            - `content: TextEditorCodeExecutionToolResultErrorParam | TextEditorCodeExecutionViewResultBlockParam | TextEditorCodeExecutionCreateResultBlockParam | TextEditorCodeExecutionStrReplaceResultBlockParam`

              - `TextEditorCodeExecutionToolResultErrorParam`

                - `error_code: TextEditorCodeExecutionToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"file_not_found"`

                - `type: "text_editor_code_execution_tool_result_error"`

                  - `"text_editor_code_execution_tool_result_error"`

                - `error_message?: string | null`

              - `TextEditorCodeExecutionViewResultBlockParam`

                - `content: string`

                - `file_type: "text" | "image" | "pdf"`

                  - `"text"`

                  - `"image"`

                  - `"pdf"`

                - `type: "text_editor_code_execution_view_result"`

                  - `"text_editor_code_execution_view_result"`

                - `num_lines?: number | null`

                - `start_line?: number | null`

                - `total_lines?: number | null`

              - `TextEditorCodeExecutionCreateResultBlockParam`

                - `is_file_update: boolean`

                - `type: "text_editor_code_execution_create_result"`

                  - `"text_editor_code_execution_create_result"`

              - `TextEditorCodeExecutionStrReplaceResultBlockParam`

                - `type: "text_editor_code_execution_str_replace_result"`

                  - `"text_editor_code_execution_str_replace_result"`

                - `lines?: Array<string> | null`

                - `new_lines?: number | null`

                - `new_start?: number | null`

                - `old_lines?: number | null`

                - `old_start?: number | null`

            - `tool_use_id: string`

            - `type: "text_editor_code_execution_tool_result"`

              - `"text_editor_code_execution_tool_result"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

          - `ToolSearchToolResultBlockParam`

            - `content: ToolSearchToolResultErrorParam | ToolSearchToolSearchResultBlockParam`

              - `ToolSearchToolResultErrorParam`

                - `error_code: ToolSearchToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `type: "tool_search_tool_result_error"`

                  - `"tool_search_tool_result_error"`

              - `ToolSearchToolSearchResultBlockParam`

                - `tool_references: Array<ToolReferenceBlockParam>`

                  - `tool_name: string`

                  - `type: "tool_reference"`

                    - `"tool_reference"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

                - `type: "tool_search_tool_search_result"`

                  - `"tool_search_tool_search_result"`

            - `tool_use_id: string`

            - `type: "tool_search_tool_result"`

              - `"tool_search_tool_result"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

          - `ContainerUploadBlockParam`

            A content block that represents a file to be uploaded to the container
            Files uploaded via this block will be available in the container's input directory.

            - `file_id: string`

            - `type: "container_upload"`

              - `"container_upload"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

      - `role: "user" | "assistant"`

        - `"user"`

        - `"assistant"`

    - `model: Model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-opus-4-5-20251101" | 19 more`

        - `"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `"claude-sonnet-4-6"`

          Frontier intelligence at scale — built for coding, agents, and enterprise workflows

        - `"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `"claude-3-7-sonnet-latest"`

          High-performance model with early extended thinking

        - `"claude-3-7-sonnet-20250219"`

          High-performance model with early extended thinking

        - `"claude-3-5-haiku-latest"`

          Fastest and most compact model for near-instant responsiveness

        - `"claude-3-5-haiku-20241022"`

          Our fastest model

        - `"claude-haiku-4-5"`

          Hybrid model, capable of near-instant responses and extended thinking

        - `"claude-haiku-4-5-20251001"`

          Hybrid model, capable of near-instant responses and extended thinking

        - `"claude-sonnet-4-20250514"`

          High-performance model with extended thinking

        - `"claude-sonnet-4-0"`

          High-performance model with extended thinking

        - `"claude-4-sonnet-20250514"`

          High-performance model with extended thinking

        - `"claude-sonnet-4-5"`

          Our best model for real-world agents and coding

        - `"claude-sonnet-4-5-20250929"`

          Our best model for real-world agents and coding

        - `"claude-opus-4-0"`

          Our most capable model

        - `"claude-opus-4-20250514"`

          Our most capable model

        - `"claude-4-opus-20250514"`

          Our most capable model

        - `"claude-opus-4-1-20250805"`

          Our most capable model

        - `"claude-3-opus-latest"`

          Excels at writing and complex tasks

        - `"claude-3-opus-20240229"`

          Excels at writing and complex tasks

        - `"claude-3-haiku-20240307"`

          Our previous most fast and cost-effective

      - `(string & {})`

    - `cache_control?: CacheControlEphemeral | null`

      Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `container?: string | null`

      Container identifier for reuse across requests.

    - `inference_geo?: string | null`

      Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

    - `metadata?: Metadata`

      An object describing metadata about the request.

      - `user_id?: string | null`

        An external identifier for the user who is associated with the request.

        This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

    - `output_config?: OutputConfig`

      Configuration options for the model's output, such as the output format.

      - `effort?: "low" | "medium" | "high" | "max" | null`

        All possible effort levels.

        - `"low"`

        - `"medium"`

        - `"high"`

        - `"max"`

      - `format?: JSONOutputFormat | null`

        A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

        - `schema: Record<string, unknown>`

          The JSON schema of the format

        - `type: "json_schema"`

          - `"json_schema"`

    - `service_tier?: "auto" | "standard_only"`

      Determines whether to use priority capacity (if available) or standard capacity for this request.

      Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

      - `"auto"`

      - `"standard_only"`

    - `stop_sequences?: Array<string>`

      Custom text sequences that will cause the model to stop generating.

      Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

      If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

    - `stream?: false`

      Whether to incrementally stream the response using server-sent events.

      See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

      - `false`

    - `system?: string | Array<TextBlockParam>`

      System prompt.

      A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

      - `string`

      - `Array<TextBlockParam>`

        - `text: string`

        - `type: "text"`

          - `"text"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations?: Array<TextCitationParam> | null`

          - `CitationCharLocationParam`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_char_index: number`

            - `start_char_index: number`

            - `type: "char_location"`

              - `"char_location"`

          - `CitationPageLocationParam`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_page_number: number`

            - `start_page_number: number`

            - `type: "page_location"`

              - `"page_location"`

          - `CitationContentBlockLocationParam`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_block_index: number`

            - `start_block_index: number`

            - `type: "content_block_location"`

              - `"content_block_location"`

          - `CitationWebSearchResultLocationParam`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string | null`

            - `type: "web_search_result_location"`

              - `"web_search_result_location"`

            - `url: string`

          - `CitationSearchResultLocationParam`

            - `cited_text: string`

            - `end_block_index: number`

            - `search_result_index: number`

            - `source: string`

            - `start_block_index: number`

            - `title: string | null`

            - `type: "search_result_location"`

              - `"search_result_location"`

    - `temperature?: number`

      Amount of randomness injected into the response.

      Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

      Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

    - `thinking?: ThinkingConfigParam`

      Configuration for enabling Claude's extended thinking.

      When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

      See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

      - `ThinkingConfigEnabled`

        - `budget_tokens: number`

          Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

          Must be ≥1024 and less than `max_tokens`.

          See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

        - `type: "enabled"`

          - `"enabled"`

      - `ThinkingConfigDisabled`

        - `type: "disabled"`

          - `"disabled"`

      - `ThinkingConfigAdaptive`

        - `type: "adaptive"`

          - `"adaptive"`

    - `tool_choice?: ToolChoice`

      How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

      - `ToolChoiceAuto`

        The model will automatically decide whether to use tools.

        - `type: "auto"`

          - `"auto"`

        - `disable_parallel_tool_use?: boolean`

          Whether to disable parallel tool use.

          Defaults to `false`. If set to `true`, the model will output at most one tool use.

      - `ToolChoiceAny`

        The model will use any available tools.

        - `type: "any"`

          - `"any"`

        - `disable_parallel_tool_use?: boolean`

          Whether to disable parallel tool use.

          Defaults to `false`. If set to `true`, the model will output exactly one tool use.

      - `ToolChoiceTool`

        The model will use the specified tool with `tool_choice.name`.

        - `name: string`

          The name of the tool to use.

        - `type: "tool"`

          - `"tool"`

        - `disable_parallel_tool_use?: boolean`

          Whether to disable parallel tool use.

          Defaults to `false`. If set to `true`, the model will output exactly one tool use.

      - `ToolChoiceNone`

        The model will not be allowed to use tools.

        - `type: "none"`

          - `"none"`

    - `tools?: Array<ToolUnion>`

      Definitions of tools that the model may use.

      If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

      There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

      Each tool definition includes:

      * `name`: Name of the tool.
      * `description`: Optional, but strongly-recommended description of the tool.
      * `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

      For example, if you defined `tools` as:

      ```json
      [
        {
          "name": "get_stock_price",
          "description": "Get the current stock price for a given ticker symbol.",
          "input_schema": {
            "type": "object",
            "properties": {
              "ticker": {
                "type": "string",
                "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
              }
            },
            "required": ["ticker"]
          }
        }
      ]
      ```

      And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

      ```json
      [
        {
          "type": "tool_use",
          "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
          "name": "get_stock_price",
          "input": { "ticker": "^GSPC" }
        }
      ]
      ```

      You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

      ```json
      [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
          "content": "259.75 USD"
        }
      ]
      ```

      Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

      See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

      - `Tool`

        - `input_schema: InputSchema`

          [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

          This defines the shape of the `input` that your tool accepts and that the model will produce.

          - `type: "object"`

            - `"object"`

          - `properties?: Record<string, unknown> | null`

          - `required?: Array<string> | null`

        - `name: string`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `description?: string`

          Description of what this tool does.

          Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

        - `eager_input_streaming?: boolean | null`

          Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

        - `input_examples?: Array<Record<string, unknown>>`

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

        - `type?: "custom" | null`

          - `"custom"`

      - `ToolBash20250124`

        - `name: "bash"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"bash"`

        - `type: "bash_20250124"`

          - `"bash_20250124"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `input_examples?: Array<Record<string, unknown>>`

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

      - `CodeExecutionTool20250522`

        - `name: "code_execution"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"code_execution"`

        - `type: "code_execution_20250522"`

          - `"code_execution_20250522"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

      - `CodeExecutionTool20250825`

        - `name: "code_execution"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"code_execution"`

        - `type: "code_execution_20250825"`

          - `"code_execution_20250825"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

      - `CodeExecutionTool20260120`

        Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

        - `name: "code_execution"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"code_execution"`

        - `type: "code_execution_20260120"`

          - `"code_execution_20260120"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

      - `MemoryTool20250818`

        - `name: "memory"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"memory"`

        - `type: "memory_20250818"`

          - `"memory_20250818"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `input_examples?: Array<Record<string, unknown>>`

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

      - `ToolTextEditor20250124`

        - `name: "str_replace_editor"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"str_replace_editor"`

        - `type: "text_editor_20250124"`

          - `"text_editor_20250124"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `input_examples?: Array<Record<string, unknown>>`

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

      - `ToolTextEditor20250429`

        - `name: "str_replace_based_edit_tool"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"str_replace_based_edit_tool"`

        - `type: "text_editor_20250429"`

          - `"text_editor_20250429"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `input_examples?: Array<Record<string, unknown>>`

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

      - `ToolTextEditor20250728`

        - `name: "str_replace_based_edit_tool"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"str_replace_based_edit_tool"`

        - `type: "text_editor_20250728"`

          - `"text_editor_20250728"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `input_examples?: Array<Record<string, unknown>>`

        - `max_characters?: number | null`

          Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

      - `WebSearchTool20250305`

        - `name: "web_search"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"web_search"`

        - `type: "web_search_20250305"`

          - `"web_search_20250305"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `allowed_domains?: Array<string> | null`

          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

        - `blocked_domains?: Array<string> | null`

          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `max_uses?: number | null`

          Maximum number of times the tool can be used in the API request.

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

        - `user_location?: UserLocation | null`

          Parameters for the user's location. Used to provide more relevant search results.

          - `type: "approximate"`

            - `"approximate"`

          - `city?: string | null`

            The city of the user.

          - `country?: string | null`

            The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

          - `region?: string | null`

            The region of the user.

          - `timezone?: string | null`

            The [IANA timezone](https://nodatime.org/TimeZones) of the user.

      - `WebFetchTool20250910`

        - `name: "web_fetch"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"web_fetch"`

        - `type: "web_fetch_20250910"`

          - `"web_fetch_20250910"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `allowed_domains?: Array<string> | null`

          List of domains to allow fetching from

        - `blocked_domains?: Array<string> | null`

          List of domains to block fetching from

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations?: CitationsConfigParam | null`

          Citations configuration for fetched documents. Citations are disabled by default.

          - `enabled?: boolean`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `max_content_tokens?: number | null`

          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        - `max_uses?: number | null`

          Maximum number of times the tool can be used in the API request.

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

      - `WebSearchTool20260209`

        - `name: "web_search"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"web_search"`

        - `type: "web_search_20260209"`

          - `"web_search_20260209"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `allowed_domains?: Array<string> | null`

          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

        - `blocked_domains?: Array<string> | null`

          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `max_uses?: number | null`

          Maximum number of times the tool can be used in the API request.

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

        - `user_location?: UserLocation | null`

          Parameters for the user's location. Used to provide more relevant search results.

          - `type: "approximate"`

            - `"approximate"`

          - `city?: string | null`

            The city of the user.

          - `country?: string | null`

            The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

          - `region?: string | null`

            The region of the user.

          - `timezone?: string | null`

            The [IANA timezone](https://nodatime.org/TimeZones) of the user.

      - `WebFetchTool20260209`

        - `name: "web_fetch"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"web_fetch"`

        - `type: "web_fetch_20260209"`

          - `"web_fetch_20260209"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `allowed_domains?: Array<string> | null`

          List of domains to allow fetching from

        - `blocked_domains?: Array<string> | null`

          List of domains to block fetching from

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations?: CitationsConfigParam | null`

          Citations configuration for fetched documents. Citations are disabled by default.

          - `enabled?: boolean`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `max_content_tokens?: number | null`

          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        - `max_uses?: number | null`

          Maximum number of times the tool can be used in the API request.

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

      - `ToolSearchToolBm25_20251119`

        - `name: "tool_search_tool_bm25"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"tool_search_tool_bm25"`

        - `type: "tool_search_tool_bm25_20251119" | "tool_search_tool_bm25"`

          - `"tool_search_tool_bm25_20251119"`

          - `"tool_search_tool_bm25"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

      - `ToolSearchToolRegex20251119`

        - `name: "tool_search_tool_regex"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          - `"tool_search_tool_regex"`

        - `type: "tool_search_tool_regex_20251119" | "tool_search_tool_regex"`

          - `"tool_search_tool_regex_20251119"`

          - `"tool_search_tool_regex"`

        - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `defer_loading?: boolean`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `strict?: boolean`

          When true, guarantees schema validation on tool names and inputs

    - `top_k?: number`

      Only sample from the top K options for each subsequent token.

      Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

      Recommended for advanced use cases only. You usually only need to use `temperature`.

    - `top_p?: number`

      Use nucleus sampling.

      In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

      Recommended for advanced use cases only. You usually only need to use `temperature`.

  - `MessageCreateParamsNonStreaming extends MessageCreateParamsBase`

    - `stream?: false`

      Whether to incrementally stream the response using server-sent events.

      See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

      - `false`

  - `MessageCreateParamsNonStreaming extends MessageCreateParamsBase`

    - `stream?: false`

      Whether to incrementally stream the response using server-sent events.

      See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

      - `false`

### Returns

- `Message`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `container: Container | null`

    Information about the container used in the request (for the code execution tool)

    - `id: string`

      Identifier for the container used in this request

    - `expires_at: string`

      The time at which the container will expire.

  - `content: Array<ContentBlock>`

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

    - `TextBlock`

      - `citations: Array<TextCitation> | null`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `CitationCharLocation`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_char_index: number`

          - `file_id: string | null`

          - `start_char_index: number`

          - `type: "char_location"`

            - `"char_location"`

        - `CitationPageLocation`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_page_number: number`

          - `file_id: string | null`

          - `start_page_number: number`

          - `type: "page_location"`

            - `"page_location"`

        - `CitationContentBlockLocation`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_block_index: number`

          - `file_id: string | null`

          - `start_block_index: number`

          - `type: "content_block_location"`

            - `"content_block_location"`

        - `CitationsWebSearchResultLocation`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string | null`

          - `type: "web_search_result_location"`

            - `"web_search_result_location"`

          - `url: string`

        - `CitationsSearchResultLocation`

          - `cited_text: string`

          - `end_block_index: number`

          - `search_result_index: number`

          - `source: string`

          - `start_block_index: number`

          - `title: string | null`

          - `type: "search_result_location"`

            - `"search_result_location"`

      - `text: string`

      - `type: "text"`

        - `"text"`

    - `ThinkingBlock`

      - `signature: string`

      - `thinking: string`

      - `type: "thinking"`

        - `"thinking"`

    - `RedactedThinkingBlock`

      - `data: string`

      - `type: "redacted_thinking"`

        - `"redacted_thinking"`

    - `ToolUseBlock`

      - `id: string`

      - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `DirectCaller`

          Tool invocation directly from the model.

          - `type: "direct"`

            - `"direct"`

        - `ServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

            - `"code_execution_20250825"`

        - `ServerToolCaller20260120`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

            - `"code_execution_20260120"`

      - `input: Record<string, unknown>`

      - `name: string`

      - `type: "tool_use"`

        - `"tool_use"`

    - `ServerToolUseBlock`

      - `id: string`

      - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `DirectCaller`

          Tool invocation directly from the model.

          - `type: "direct"`

            - `"direct"`

        - `ServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

            - `"code_execution_20250825"`

        - `ServerToolCaller20260120`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

            - `"code_execution_20260120"`

      - `input: Record<string, unknown>`

      - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

        - `"web_search"`

        - `"web_fetch"`

        - `"code_execution"`

        - `"bash_code_execution"`

        - `"text_editor_code_execution"`

        - `"tool_search_tool_regex"`

        - `"tool_search_tool_bm25"`

      - `type: "server_tool_use"`

        - `"server_tool_use"`

    - `WebSearchToolResultBlock`

      - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `DirectCaller`

          Tool invocation directly from the model.

          - `type: "direct"`

            - `"direct"`

        - `ServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

            - `"code_execution_20250825"`

        - `ServerToolCaller20260120`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

            - `"code_execution_20260120"`

      - `content: WebSearchToolResultBlockContent`

        - `WebSearchToolResultError`

          - `error_code: WebSearchToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"max_uses_exceeded"`

            - `"too_many_requests"`

            - `"query_too_long"`

            - `"request_too_large"`

          - `type: "web_search_tool_result_error"`

            - `"web_search_tool_result_error"`

        - `Array<WebSearchResultBlock>`

          - `encrypted_content: string`

          - `page_age: string | null`

          - `title: string`

          - `type: "web_search_result"`

            - `"web_search_result"`

          - `url: string`

      - `tool_use_id: string`

      - `type: "web_search_tool_result"`

        - `"web_search_tool_result"`

    - `WebFetchToolResultBlock`

      - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `DirectCaller`

          Tool invocation directly from the model.

          - `type: "direct"`

            - `"direct"`

        - `ServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

            - `"code_execution_20250825"`

        - `ServerToolCaller20260120`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

            - `"code_execution_20260120"`

      - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

        - `WebFetchToolResultErrorBlock`

          - `error_code: WebFetchToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"url_too_long"`

            - `"url_not_allowed"`

            - `"url_not_accessible"`

            - `"unsupported_content_type"`

            - `"too_many_requests"`

            - `"max_uses_exceeded"`

            - `"unavailable"`

          - `type: "web_fetch_tool_result_error"`

            - `"web_fetch_tool_result_error"`

        - `WebFetchBlock`

          - `content: DocumentBlock`

            - `citations: CitationsConfig | null`

              Citation configuration for the document

              - `enabled: boolean`

            - `source: Base64PDFSource | PlainTextSource`

              - `Base64PDFSource`

                - `data: string`

                - `media_type: "application/pdf"`

                  - `"application/pdf"`

                - `type: "base64"`

                  - `"base64"`

              - `PlainTextSource`

                - `data: string`

                - `media_type: "text/plain"`

                  - `"text/plain"`

                - `type: "text"`

                  - `"text"`

            - `title: string | null`

              The title of the document

            - `type: "document"`

              - `"document"`

          - `retrieved_at: string | null`

            ISO 8601 timestamp when the content was retrieved

          - `type: "web_fetch_result"`

            - `"web_fetch_result"`

          - `url: string`

            Fetched content URL

      - `tool_use_id: string`

      - `type: "web_fetch_tool_result"`

        - `"web_fetch_tool_result"`

    - `CodeExecutionToolResultBlock`

      - `content: CodeExecutionToolResultBlockContent`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `CodeExecutionToolResultError`

          - `error_code: CodeExecutionToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `type: "code_execution_tool_result_error"`

            - `"code_execution_tool_result_error"`

        - `CodeExecutionResultBlock`

          - `content: Array<CodeExecutionOutputBlock>`

            - `file_id: string`

            - `type: "code_execution_output"`

              - `"code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "code_execution_result"`

            - `"code_execution_result"`

        - `EncryptedCodeExecutionResultBlock`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `content: Array<CodeExecutionOutputBlock>`

            - `file_id: string`

            - `type: "code_execution_output"`

              - `"code_execution_output"`

          - `encrypted_stdout: string`

          - `return_code: number`

          - `stderr: string`

          - `type: "encrypted_code_execution_result"`

            - `"encrypted_code_execution_result"`

      - `tool_use_id: string`

      - `type: "code_execution_tool_result"`

        - `"code_execution_tool_result"`

    - `BashCodeExecutionToolResultBlock`

      - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

        - `BashCodeExecutionToolResultError`

          - `error_code: BashCodeExecutionToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"output_file_too_large"`

          - `type: "bash_code_execution_tool_result_error"`

            - `"bash_code_execution_tool_result_error"`

        - `BashCodeExecutionResultBlock`

          - `content: Array<BashCodeExecutionOutputBlock>`

            - `file_id: string`

            - `type: "bash_code_execution_output"`

              - `"bash_code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "bash_code_execution_result"`

            - `"bash_code_execution_result"`

      - `tool_use_id: string`

      - `type: "bash_code_execution_tool_result"`

        - `"bash_code_execution_tool_result"`

    - `TextEditorCodeExecutionToolResultBlock`

      - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

        - `TextEditorCodeExecutionToolResultError`

          - `error_code: TextEditorCodeExecutionToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"file_not_found"`

          - `error_message: string | null`

          - `type: "text_editor_code_execution_tool_result_error"`

            - `"text_editor_code_execution_tool_result_error"`

        - `TextEditorCodeExecutionViewResultBlock`

          - `content: string`

          - `file_type: "text" | "image" | "pdf"`

            - `"text"`

            - `"image"`

            - `"pdf"`

          - `num_lines: number | null`

          - `start_line: number | null`

          - `total_lines: number | null`

          - `type: "text_editor_code_execution_view_result"`

            - `"text_editor_code_execution_view_result"`

        - `TextEditorCodeExecutionCreateResultBlock`

          - `is_file_update: boolean`

          - `type: "text_editor_code_execution_create_result"`

            - `"text_editor_code_execution_create_result"`

        - `TextEditorCodeExecutionStrReplaceResultBlock`

          - `lines: Array<string> | null`

          - `new_lines: number | null`

          - `new_start: number | null`

          - `old_lines: number | null`

          - `old_start: number | null`

          - `type: "text_editor_code_execution_str_replace_result"`

            - `"text_editor_code_execution_str_replace_result"`

      - `tool_use_id: string`

      - `type: "text_editor_code_execution_tool_result"`

        - `"text_editor_code_execution_tool_result"`

    - `ToolSearchToolResultBlock`

      - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

        - `ToolSearchToolResultError`

          - `error_code: ToolSearchToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `error_message: string | null`

          - `type: "tool_search_tool_result_error"`

            - `"tool_search_tool_result_error"`

        - `ToolSearchToolSearchResultBlock`

          - `tool_references: Array<ToolReferenceBlock>`

            - `tool_name: string`

            - `type: "tool_reference"`

              - `"tool_reference"`

          - `type: "tool_search_tool_search_result"`

            - `"tool_search_tool_search_result"`

      - `tool_use_id: string`

      - `type: "tool_search_tool_result"`

        - `"tool_search_tool_result"`

    - `ContainerUploadBlock`

      Response model for a file uploaded to the container.

      - `file_id: string`

      - `type: "container_upload"`

        - `"container_upload"`

  - `model: Model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-opus-4-5-20251101" | 19 more`

      - `"claude-opus-4-6"`

        Most intelligent model for building agents and coding

      - `"claude-sonnet-4-6"`

        Frontier intelligence at scale — built for coding, agents, and enterprise workflows

      - `"claude-opus-4-5-20251101"`

        Premium model combining maximum intelligence with practical performance

      - `"claude-opus-4-5"`

        Premium model combining maximum intelligence with practical performance

      - `"claude-3-7-sonnet-latest"`

        High-performance model with early extended thinking

      - `"claude-3-7-sonnet-20250219"`

        High-performance model with early extended thinking

      - `"claude-3-5-haiku-latest"`

        Fastest and most compact model for near-instant responsiveness

      - `"claude-3-5-haiku-20241022"`

        Our fastest model

      - `"claude-haiku-4-5"`

        Hybrid model, capable of near-instant responses and extended thinking

      - `"claude-haiku-4-5-20251001"`

        Hybrid model, capable of near-instant responses and extended thinking

      - `"claude-sonnet-4-20250514"`

        High-performance model with extended thinking

      - `"claude-sonnet-4-0"`

        High-performance model with extended thinking

      - `"claude-4-sonnet-20250514"`

        High-performance model with extended thinking

      - `"claude-sonnet-4-5"`

        Our best model for real-world agents and coding

      - `"claude-sonnet-4-5-20250929"`

        Our best model for real-world agents and coding

      - `"claude-opus-4-0"`

        Our most capable model

      - `"claude-opus-4-20250514"`

        Our most capable model

      - `"claude-4-opus-20250514"`

        Our most capable model

      - `"claude-opus-4-1-20250805"`

        Our most capable model

      - `"claude-3-opus-latest"`

        Excels at writing and complex tasks

      - `"claude-3-opus-20240229"`

        Excels at writing and complex tasks

      - `"claude-3-haiku-20240307"`

        Our previous most fast and cost-effective

    - `(string & {})`

  - `role: "assistant"`

    Conversational role of the generated message.

    This will always be `"assistant"`.

    - `"assistant"`

  - `stop_reason: StopReason | null`

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

    - `"refusal"`

  - `stop_sequence: string | null`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `type: "message"`

    Object type.

    For Messages, this is always `"message"`.

    - `"message"`

  - `usage: Usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `cache_creation: CacheCreation | null`

      Breakdown of cached tokens by TTL

      - `ephemeral_1h_input_tokens: number`

        The number of input tokens used to create the 1 hour cache entry.

      - `ephemeral_5m_input_tokens: number`

        The number of input tokens used to create the 5 minute cache entry.

    - `cache_creation_input_tokens: number | null`

      The number of input tokens used to create the cache entry.

    - `cache_read_input_tokens: number | null`

      The number of input tokens read from the cache.

    - `inference_geo: string | null`

      The geographic region where inference was performed for this request.

    - `input_tokens: number`

      The number of input tokens which were used.

    - `output_tokens: number`

      The number of output tokens which were used.

    - `server_tool_use: ServerToolUsage | null`

      The number of server tool requests.

      - `web_fetch_requests: number`

        The number of web fetch tool requests.

      - `web_search_requests: number`

        The number of web search tool requests.

    - `service_tier: "standard" | "priority" | "batch" | null`

      If the request used the priority, standard, or batch tier.

      - `"standard"`

      - `"priority"`

      - `"batch"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const message = await client.messages.create({
  max_tokens: 1024,
  messages: [{ content: 'Hello, world', role: 'user' }],
  model: 'claude-opus-4-6',
});

console.log(message.id);
```

## Count Tokens

`client.messages.countTokens(MessageCountTokensParamsbody, RequestOptionsoptions?): MessageTokensCount`

**post** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

### Parameters

- `body: MessageCountTokensParams`

  - `messages: Array<MessageParam>`

    Input messages.

    Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

    Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

    If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

    Example with a single `user` message:

    ```json
    [{"role": "user", "content": "Hello, Claude"}]
    ```

    Example with multiple conversational turns:

    ```json
    [
      {"role": "user", "content": "Hello there."},
      {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
      {"role": "user", "content": "Can you explain LLMs in plain English?"},
    ]
    ```

    Example with a partially-filled response from Claude:

    ```json
    [
      {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
      {"role": "assistant", "content": "The best answer is ("},
    ]
    ```

    Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

    ```json
    {"role": "user", "content": "Hello, Claude"}
    ```

    ```json
    {"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
    ```

    See [input examples](https://docs.claude.com/en/api/messages-examples).

    Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

    There is a limit of 100,000 messages in a single request.

    - `content: string | Array<ContentBlockParam>`

      - `string`

      - `Array<ContentBlockParam>`

        - `TextBlockParam`

          - `text: string`

          - `type: "text"`

            - `"text"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations?: Array<TextCitationParam> | null`

            - `CitationCharLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_char_index: number`

              - `start_char_index: number`

              - `type: "char_location"`

                - `"char_location"`

            - `CitationPageLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_page_number: number`

              - `start_page_number: number`

              - `type: "page_location"`

                - `"page_location"`

            - `CitationContentBlockLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_block_index: number`

              - `start_block_index: number`

              - `type: "content_block_location"`

                - `"content_block_location"`

            - `CitationWebSearchResultLocationParam`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string | null`

              - `type: "web_search_result_location"`

                - `"web_search_result_location"`

              - `url: string`

            - `CitationSearchResultLocationParam`

              - `cited_text: string`

              - `end_block_index: number`

              - `search_result_index: number`

              - `source: string`

              - `start_block_index: number`

              - `title: string | null`

              - `type: "search_result_location"`

                - `"search_result_location"`

        - `ImageBlockParam`

          - `source: Base64ImageSource | URLImageSource`

            - `Base64ImageSource`

              - `data: string`

              - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                - `"image/jpeg"`

                - `"image/png"`

                - `"image/gif"`

                - `"image/webp"`

              - `type: "base64"`

                - `"base64"`

            - `URLImageSource`

              - `type: "url"`

                - `"url"`

              - `url: string`

          - `type: "image"`

            - `"image"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

        - `DocumentBlockParam`

          - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

            - `Base64PDFSource`

              - `data: string`

              - `media_type: "application/pdf"`

                - `"application/pdf"`

              - `type: "base64"`

                - `"base64"`

            - `PlainTextSource`

              - `data: string`

              - `media_type: "text/plain"`

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `ContentBlockSource`

              - `content: string | Array<ContentBlockSourceContent>`

                - `string`

                - `Array<ContentBlockSourceContent>`

                  - `TextBlockParam`

                    - `text: string`

                    - `type: "text"`

                      - `"text"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

                    - `citations?: Array<TextCitationParam> | null`

                      - `CitationCharLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_char_index: number`

                        - `start_char_index: number`

                        - `type: "char_location"`

                          - `"char_location"`

                      - `CitationPageLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_page_number: number`

                        - `start_page_number: number`

                        - `type: "page_location"`

                          - `"page_location"`

                      - `CitationContentBlockLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_block_index: number`

                        - `start_block_index: number`

                        - `type: "content_block_location"`

                          - `"content_block_location"`

                      - `CitationWebSearchResultLocationParam`

                        - `cited_text: string`

                        - `encrypted_index: string`

                        - `title: string | null`

                        - `type: "web_search_result_location"`

                          - `"web_search_result_location"`

                        - `url: string`

                      - `CitationSearchResultLocationParam`

                        - `cited_text: string`

                        - `end_block_index: number`

                        - `search_result_index: number`

                        - `source: string`

                        - `start_block_index: number`

                        - `title: string | null`

                        - `type: "search_result_location"`

                          - `"search_result_location"`

                  - `ImageBlockParam`

                    - `source: Base64ImageSource | URLImageSource`

                      - `Base64ImageSource`

                        - `data: string`

                        - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                          - `"image/jpeg"`

                          - `"image/png"`

                          - `"image/gif"`

                          - `"image/webp"`

                        - `type: "base64"`

                          - `"base64"`

                      - `URLImageSource`

                        - `type: "url"`

                          - `"url"`

                        - `url: string`

                    - `type: "image"`

                      - `"image"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

              - `type: "content"`

                - `"content"`

            - `URLPDFSource`

              - `type: "url"`

                - `"url"`

              - `url: string`

          - `type: "document"`

            - `"document"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations?: CitationsConfigParam | null`

            - `enabled?: boolean`

          - `context?: string | null`

          - `title?: string | null`

        - `SearchResultBlockParam`

          - `content: Array<TextBlockParam>`

            - `text: string`

            - `type: "text"`

              - `"text"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `citations?: Array<TextCitationParam> | null`

              - `CitationCharLocationParam`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_char_index: number`

                - `start_char_index: number`

                - `type: "char_location"`

                  - `"char_location"`

              - `CitationPageLocationParam`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_page_number: number`

                - `start_page_number: number`

                - `type: "page_location"`

                  - `"page_location"`

              - `CitationContentBlockLocationParam`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_block_index: number`

                - `start_block_index: number`

                - `type: "content_block_location"`

                  - `"content_block_location"`

              - `CitationWebSearchResultLocationParam`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string | null`

                - `type: "web_search_result_location"`

                  - `"web_search_result_location"`

                - `url: string`

              - `CitationSearchResultLocationParam`

                - `cited_text: string`

                - `end_block_index: number`

                - `search_result_index: number`

                - `source: string`

                - `start_block_index: number`

                - `title: string | null`

                - `type: "search_result_location"`

                  - `"search_result_location"`

          - `source: string`

          - `title: string`

          - `type: "search_result"`

            - `"search_result"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations?: CitationsConfigParam`

            - `enabled?: boolean`

        - `ThinkingBlockParam`

          - `signature: string`

          - `thinking: string`

          - `type: "thinking"`

            - `"thinking"`

        - `RedactedThinkingBlockParam`

          - `data: string`

          - `type: "redacted_thinking"`

            - `"redacted_thinking"`

        - `ToolUseBlockParam`

          - `id: string`

          - `input: Record<string, unknown>`

          - `name: string`

          - `type: "tool_use"`

            - `"tool_use"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `DirectCaller`

              Tool invocation directly from the model.

              - `type: "direct"`

                - `"direct"`

            - `ServerToolCaller`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

              - `type: "code_execution_20250825"`

                - `"code_execution_20250825"`

            - `ServerToolCaller20260120`

              - `tool_id: string`

              - `type: "code_execution_20260120"`

                - `"code_execution_20260120"`

        - `ToolResultBlockParam`

          - `tool_use_id: string`

          - `type: "tool_result"`

            - `"tool_result"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `content?: string | Array<TextBlockParam | ImageBlockParam | SearchResultBlockParam | 2 more>`

            - `string`

            - `Array<TextBlockParam | ImageBlockParam | SearchResultBlockParam | 2 more>`

              - `TextBlockParam`

                - `text: string`

                - `type: "text"`

                  - `"text"`

                - `cache_control?: CacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

                  - `type: "ephemeral"`

                    - `"ephemeral"`

                  - `ttl?: "5m" | "1h"`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

                - `citations?: Array<TextCitationParam> | null`

                  - `CitationCharLocationParam`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string | null`

                    - `end_char_index: number`

                    - `start_char_index: number`

                    - `type: "char_location"`

                      - `"char_location"`

                  - `CitationPageLocationParam`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string | null`

                    - `end_page_number: number`

                    - `start_page_number: number`

                    - `type: "page_location"`

                      - `"page_location"`

                  - `CitationContentBlockLocationParam`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string | null`

                    - `end_block_index: number`

                    - `start_block_index: number`

                    - `type: "content_block_location"`

                      - `"content_block_location"`

                  - `CitationWebSearchResultLocationParam`

                    - `cited_text: string`

                    - `encrypted_index: string`

                    - `title: string | null`

                    - `type: "web_search_result_location"`

                      - `"web_search_result_location"`

                    - `url: string`

                  - `CitationSearchResultLocationParam`

                    - `cited_text: string`

                    - `end_block_index: number`

                    - `search_result_index: number`

                    - `source: string`

                    - `start_block_index: number`

                    - `title: string | null`

                    - `type: "search_result_location"`

                      - `"search_result_location"`

              - `ImageBlockParam`

                - `source: Base64ImageSource | URLImageSource`

                  - `Base64ImageSource`

                    - `data: string`

                    - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                      - `"image/jpeg"`

                      - `"image/png"`

                      - `"image/gif"`

                      - `"image/webp"`

                    - `type: "base64"`

                      - `"base64"`

                  - `URLImageSource`

                    - `type: "url"`

                      - `"url"`

                    - `url: string`

                - `type: "image"`

                  - `"image"`

                - `cache_control?: CacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

                  - `type: "ephemeral"`

                    - `"ephemeral"`

                  - `ttl?: "5m" | "1h"`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

              - `SearchResultBlockParam`

                - `content: Array<TextBlockParam>`

                  - `text: string`

                  - `type: "text"`

                    - `"text"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

                  - `citations?: Array<TextCitationParam> | null`

                    - `CitationCharLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_char_index: number`

                      - `start_char_index: number`

                      - `type: "char_location"`

                        - `"char_location"`

                    - `CitationPageLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_page_number: number`

                      - `start_page_number: number`

                      - `type: "page_location"`

                        - `"page_location"`

                    - `CitationContentBlockLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_block_index: number`

                      - `start_block_index: number`

                      - `type: "content_block_location"`

                        - `"content_block_location"`

                    - `CitationWebSearchResultLocationParam`

                      - `cited_text: string`

                      - `encrypted_index: string`

                      - `title: string | null`

                      - `type: "web_search_result_location"`

                        - `"web_search_result_location"`

                      - `url: string`

                    - `CitationSearchResultLocationParam`

                      - `cited_text: string`

                      - `end_block_index: number`

                      - `search_result_index: number`

                      - `source: string`

                      - `start_block_index: number`

                      - `title: string | null`

                      - `type: "search_result_location"`

                        - `"search_result_location"`

                - `source: string`

                - `title: string`

                - `type: "search_result"`

                  - `"search_result"`

                - `cache_control?: CacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

                  - `type: "ephemeral"`

                    - `"ephemeral"`

                  - `ttl?: "5m" | "1h"`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

                - `citations?: CitationsConfigParam`

                  - `enabled?: boolean`

              - `DocumentBlockParam`

                - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

                  - `Base64PDFSource`

                    - `data: string`

                    - `media_type: "application/pdf"`

                      - `"application/pdf"`

                    - `type: "base64"`

                      - `"base64"`

                  - `PlainTextSource`

                    - `data: string`

                    - `media_type: "text/plain"`

                      - `"text/plain"`

                    - `type: "text"`

                      - `"text"`

                  - `ContentBlockSource`

                    - `content: string | Array<ContentBlockSourceContent>`

                      - `string`

                      - `Array<ContentBlockSourceContent>`

                        - `TextBlockParam`

                          - `text: string`

                          - `type: "text"`

                            - `"text"`

                          - `cache_control?: CacheControlEphemeral | null`

                            Create a cache control breakpoint at this content block.

                            - `type: "ephemeral"`

                              - `"ephemeral"`

                            - `ttl?: "5m" | "1h"`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `"5m"`

                              - `"1h"`

                          - `citations?: Array<TextCitationParam> | null`

                            - `CitationCharLocationParam`

                              - `cited_text: string`

                              - `document_index: number`

                              - `document_title: string | null`

                              - `end_char_index: number`

                              - `start_char_index: number`

                              - `type: "char_location"`

                                - `"char_location"`

                            - `CitationPageLocationParam`

                              - `cited_text: string`

                              - `document_index: number`

                              - `document_title: string | null`

                              - `end_page_number: number`

                              - `start_page_number: number`

                              - `type: "page_location"`

                                - `"page_location"`

                            - `CitationContentBlockLocationParam`

                              - `cited_text: string`

                              - `document_index: number`

                              - `document_title: string | null`

                              - `end_block_index: number`

                              - `start_block_index: number`

                              - `type: "content_block_location"`

                                - `"content_block_location"`

                            - `CitationWebSearchResultLocationParam`

                              - `cited_text: string`

                              - `encrypted_index: string`

                              - `title: string | null`

                              - `type: "web_search_result_location"`

                                - `"web_search_result_location"`

                              - `url: string`

                            - `CitationSearchResultLocationParam`

                              - `cited_text: string`

                              - `end_block_index: number`

                              - `search_result_index: number`

                              - `source: string`

                              - `start_block_index: number`

                              - `title: string | null`

                              - `type: "search_result_location"`

                                - `"search_result_location"`

                        - `ImageBlockParam`

                          - `source: Base64ImageSource | URLImageSource`

                            - `Base64ImageSource`

                              - `data: string`

                              - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                                - `"image/jpeg"`

                                - `"image/png"`

                                - `"image/gif"`

                                - `"image/webp"`

                              - `type: "base64"`

                                - `"base64"`

                            - `URLImageSource`

                              - `type: "url"`

                                - `"url"`

                              - `url: string`

                          - `type: "image"`

                            - `"image"`

                          - `cache_control?: CacheControlEphemeral | null`

                            Create a cache control breakpoint at this content block.

                            - `type: "ephemeral"`

                              - `"ephemeral"`

                            - `ttl?: "5m" | "1h"`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `"5m"`

                              - `"1h"`

                    - `type: "content"`

                      - `"content"`

                  - `URLPDFSource`

                    - `type: "url"`

                      - `"url"`

                    - `url: string`

                - `type: "document"`

                  - `"document"`

                - `cache_control?: CacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

                  - `type: "ephemeral"`

                    - `"ephemeral"`

                  - `ttl?: "5m" | "1h"`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

                - `citations?: CitationsConfigParam | null`

                  - `enabled?: boolean`

                - `context?: string | null`

                - `title?: string | null`

              - `ToolReferenceBlockParam`

                Tool reference block that can be included in tool_result content.

                - `tool_name: string`

                - `type: "tool_reference"`

                  - `"tool_reference"`

                - `cache_control?: CacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

                  - `type: "ephemeral"`

                    - `"ephemeral"`

                  - `ttl?: "5m" | "1h"`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

          - `is_error?: boolean`

        - `ServerToolUseBlockParam`

          - `id: string`

          - `input: Record<string, unknown>`

          - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

            - `"web_search"`

            - `"web_fetch"`

            - `"code_execution"`

            - `"bash_code_execution"`

            - `"text_editor_code_execution"`

            - `"tool_search_tool_regex"`

            - `"tool_search_tool_bm25"`

          - `type: "server_tool_use"`

            - `"server_tool_use"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `DirectCaller`

              Tool invocation directly from the model.

              - `type: "direct"`

                - `"direct"`

            - `ServerToolCaller`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

              - `type: "code_execution_20250825"`

                - `"code_execution_20250825"`

            - `ServerToolCaller20260120`

              - `tool_id: string`

              - `type: "code_execution_20260120"`

                - `"code_execution_20260120"`

        - `WebSearchToolResultBlockParam`

          - `content: WebSearchToolResultBlockParamContent`

            - `Array<WebSearchResultBlockParam>`

              - `encrypted_content: string`

              - `title: string`

              - `type: "web_search_result"`

                - `"web_search_result"`

              - `url: string`

              - `page_age?: string | null`

            - `WebSearchToolRequestError`

              - `error_code: WebSearchToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"max_uses_exceeded"`

                - `"too_many_requests"`

                - `"query_too_long"`

                - `"request_too_large"`

              - `type: "web_search_tool_result_error"`

                - `"web_search_tool_result_error"`

          - `tool_use_id: string`

          - `type: "web_search_tool_result"`

            - `"web_search_tool_result"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `DirectCaller`

              Tool invocation directly from the model.

              - `type: "direct"`

                - `"direct"`

            - `ServerToolCaller`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

              - `type: "code_execution_20250825"`

                - `"code_execution_20250825"`

            - `ServerToolCaller20260120`

              - `tool_id: string`

              - `type: "code_execution_20260120"`

                - `"code_execution_20260120"`

        - `WebFetchToolResultBlockParam`

          - `content: WebFetchToolResultErrorBlockParam | WebFetchBlockParam`

            - `WebFetchToolResultErrorBlockParam`

              - `error_code: WebFetchToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"url_too_long"`

                - `"url_not_allowed"`

                - `"url_not_accessible"`

                - `"unsupported_content_type"`

                - `"too_many_requests"`

                - `"max_uses_exceeded"`

                - `"unavailable"`

              - `type: "web_fetch_tool_result_error"`

                - `"web_fetch_tool_result_error"`

            - `WebFetchBlockParam`

              - `content: DocumentBlockParam`

                - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

                  - `Base64PDFSource`

                    - `data: string`

                    - `media_type: "application/pdf"`

                      - `"application/pdf"`

                    - `type: "base64"`

                      - `"base64"`

                  - `PlainTextSource`

                    - `data: string`

                    - `media_type: "text/plain"`

                      - `"text/plain"`

                    - `type: "text"`

                      - `"text"`

                  - `ContentBlockSource`

                    - `content: string | Array<ContentBlockSourceContent>`

                      - `string`

                      - `Array<ContentBlockSourceContent>`

                        - `TextBlockParam`

                          - `text: string`

                          - `type: "text"`

                            - `"text"`

                          - `cache_control?: CacheControlEphemeral | null`

                            Create a cache control breakpoint at this content block.

                            - `type: "ephemeral"`

                              - `"ephemeral"`

                            - `ttl?: "5m" | "1h"`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `"5m"`

                              - `"1h"`

                          - `citations?: Array<TextCitationParam> | null`

                            - `CitationCharLocationParam`

                              - `cited_text: string`

                              - `document_index: number`

                              - `document_title: string | null`

                              - `end_char_index: number`

                              - `start_char_index: number`

                              - `type: "char_location"`

                                - `"char_location"`

                            - `CitationPageLocationParam`

                              - `cited_text: string`

                              - `document_index: number`

                              - `document_title: string | null`

                              - `end_page_number: number`

                              - `start_page_number: number`

                              - `type: "page_location"`

                                - `"page_location"`

                            - `CitationContentBlockLocationParam`

                              - `cited_text: string`

                              - `document_index: number`

                              - `document_title: string | null`

                              - `end_block_index: number`

                              - `start_block_index: number`

                              - `type: "content_block_location"`

                                - `"content_block_location"`

                            - `CitationWebSearchResultLocationParam`

                              - `cited_text: string`

                              - `encrypted_index: string`

                              - `title: string | null`

                              - `type: "web_search_result_location"`

                                - `"web_search_result_location"`

                              - `url: string`

                            - `CitationSearchResultLocationParam`

                              - `cited_text: string`

                              - `end_block_index: number`

                              - `search_result_index: number`

                              - `source: string`

                              - `start_block_index: number`

                              - `title: string | null`

                              - `type: "search_result_location"`

                                - `"search_result_location"`

                        - `ImageBlockParam`

                          - `source: Base64ImageSource | URLImageSource`

                            - `Base64ImageSource`

                              - `data: string`

                              - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                                - `"image/jpeg"`

                                - `"image/png"`

                                - `"image/gif"`

                                - `"image/webp"`

                              - `type: "base64"`

                                - `"base64"`

                            - `URLImageSource`

                              - `type: "url"`

                                - `"url"`

                              - `url: string`

                          - `type: "image"`

                            - `"image"`

                          - `cache_control?: CacheControlEphemeral | null`

                            Create a cache control breakpoint at this content block.

                            - `type: "ephemeral"`

                              - `"ephemeral"`

                            - `ttl?: "5m" | "1h"`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `"5m"`

                              - `"1h"`

                    - `type: "content"`

                      - `"content"`

                  - `URLPDFSource`

                    - `type: "url"`

                      - `"url"`

                    - `url: string`

                - `type: "document"`

                  - `"document"`

                - `cache_control?: CacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

                  - `type: "ephemeral"`

                    - `"ephemeral"`

                  - `ttl?: "5m" | "1h"`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

                - `citations?: CitationsConfigParam | null`

                  - `enabled?: boolean`

                - `context?: string | null`

                - `title?: string | null`

              - `type: "web_fetch_result"`

                - `"web_fetch_result"`

              - `url: string`

                Fetched content URL

              - `retrieved_at?: string | null`

                ISO 8601 timestamp when the content was retrieved

          - `tool_use_id: string`

          - `type: "web_fetch_tool_result"`

            - `"web_fetch_tool_result"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `DirectCaller`

              Tool invocation directly from the model.

              - `type: "direct"`

                - `"direct"`

            - `ServerToolCaller`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

              - `type: "code_execution_20250825"`

                - `"code_execution_20250825"`

            - `ServerToolCaller20260120`

              - `tool_id: string`

              - `type: "code_execution_20260120"`

                - `"code_execution_20260120"`

        - `CodeExecutionToolResultBlockParam`

          - `content: CodeExecutionToolResultBlockParamContent`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `CodeExecutionToolResultErrorParam`

              - `error_code: CodeExecutionToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

              - `type: "code_execution_tool_result_error"`

                - `"code_execution_tool_result_error"`

            - `CodeExecutionResultBlockParam`

              - `content: Array<CodeExecutionOutputBlockParam>`

                - `file_id: string`

                - `type: "code_execution_output"`

                  - `"code_execution_output"`

              - `return_code: number`

              - `stderr: string`

              - `stdout: string`

              - `type: "code_execution_result"`

                - `"code_execution_result"`

            - `EncryptedCodeExecutionResultBlockParam`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `content: Array<CodeExecutionOutputBlockParam>`

                - `file_id: string`

                - `type: "code_execution_output"`

                  - `"code_execution_output"`

              - `encrypted_stdout: string`

              - `return_code: number`

              - `stderr: string`

              - `type: "encrypted_code_execution_result"`

                - `"encrypted_code_execution_result"`

          - `tool_use_id: string`

          - `type: "code_execution_tool_result"`

            - `"code_execution_tool_result"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

        - `BashCodeExecutionToolResultBlockParam`

          - `content: BashCodeExecutionToolResultErrorParam | BashCodeExecutionResultBlockParam`

            - `BashCodeExecutionToolResultErrorParam`

              - `error_code: BashCodeExecutionToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

                - `"output_file_too_large"`

              - `type: "bash_code_execution_tool_result_error"`

                - `"bash_code_execution_tool_result_error"`

            - `BashCodeExecutionResultBlockParam`

              - `content: Array<BashCodeExecutionOutputBlockParam>`

                - `file_id: string`

                - `type: "bash_code_execution_output"`

                  - `"bash_code_execution_output"`

              - `return_code: number`

              - `stderr: string`

              - `stdout: string`

              - `type: "bash_code_execution_result"`

                - `"bash_code_execution_result"`

          - `tool_use_id: string`

          - `type: "bash_code_execution_tool_result"`

            - `"bash_code_execution_tool_result"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

        - `TextEditorCodeExecutionToolResultBlockParam`

          - `content: TextEditorCodeExecutionToolResultErrorParam | TextEditorCodeExecutionViewResultBlockParam | TextEditorCodeExecutionCreateResultBlockParam | TextEditorCodeExecutionStrReplaceResultBlockParam`

            - `TextEditorCodeExecutionToolResultErrorParam`

              - `error_code: TextEditorCodeExecutionToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

                - `"file_not_found"`

              - `type: "text_editor_code_execution_tool_result_error"`

                - `"text_editor_code_execution_tool_result_error"`

              - `error_message?: string | null`

            - `TextEditorCodeExecutionViewResultBlockParam`

              - `content: string`

              - `file_type: "text" | "image" | "pdf"`

                - `"text"`

                - `"image"`

                - `"pdf"`

              - `type: "text_editor_code_execution_view_result"`

                - `"text_editor_code_execution_view_result"`

              - `num_lines?: number | null`

              - `start_line?: number | null`

              - `total_lines?: number | null`

            - `TextEditorCodeExecutionCreateResultBlockParam`

              - `is_file_update: boolean`

              - `type: "text_editor_code_execution_create_result"`

                - `"text_editor_code_execution_create_result"`

            - `TextEditorCodeExecutionStrReplaceResultBlockParam`

              - `type: "text_editor_code_execution_str_replace_result"`

                - `"text_editor_code_execution_str_replace_result"`

              - `lines?: Array<string> | null`

              - `new_lines?: number | null`

              - `new_start?: number | null`

              - `old_lines?: number | null`

              - `old_start?: number | null`

          - `tool_use_id: string`

          - `type: "text_editor_code_execution_tool_result"`

            - `"text_editor_code_execution_tool_result"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

        - `ToolSearchToolResultBlockParam`

          - `content: ToolSearchToolResultErrorParam | ToolSearchToolSearchResultBlockParam`

            - `ToolSearchToolResultErrorParam`

              - `error_code: ToolSearchToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

              - `type: "tool_search_tool_result_error"`

                - `"tool_search_tool_result_error"`

            - `ToolSearchToolSearchResultBlockParam`

              - `tool_references: Array<ToolReferenceBlockParam>`

                - `tool_name: string`

                - `type: "tool_reference"`

                  - `"tool_reference"`

                - `cache_control?: CacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

                  - `type: "ephemeral"`

                    - `"ephemeral"`

                  - `ttl?: "5m" | "1h"`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

              - `type: "tool_search_tool_search_result"`

                - `"tool_search_tool_search_result"`

          - `tool_use_id: string`

          - `type: "tool_search_tool_result"`

            - `"tool_search_tool_result"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

        - `ContainerUploadBlockParam`

          A content block that represents a file to be uploaded to the container
          Files uploaded via this block will be available in the container's input directory.

          - `file_id: string`

          - `type: "container_upload"`

            - `"container_upload"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

    - `role: "user" | "assistant"`

      - `"user"`

      - `"assistant"`

  - `model: Model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-opus-4-5-20251101" | 19 more`

      - `"claude-opus-4-6"`

        Most intelligent model for building agents and coding

      - `"claude-sonnet-4-6"`

        Frontier intelligence at scale — built for coding, agents, and enterprise workflows

      - `"claude-opus-4-5-20251101"`

        Premium model combining maximum intelligence with practical performance

      - `"claude-opus-4-5"`

        Premium model combining maximum intelligence with practical performance

      - `"claude-3-7-sonnet-latest"`

        High-performance model with early extended thinking

      - `"claude-3-7-sonnet-20250219"`

        High-performance model with early extended thinking

      - `"claude-3-5-haiku-latest"`

        Fastest and most compact model for near-instant responsiveness

      - `"claude-3-5-haiku-20241022"`

        Our fastest model

      - `"claude-haiku-4-5"`

        Hybrid model, capable of near-instant responses and extended thinking

      - `"claude-haiku-4-5-20251001"`

        Hybrid model, capable of near-instant responses and extended thinking

      - `"claude-sonnet-4-20250514"`

        High-performance model with extended thinking

      - `"claude-sonnet-4-0"`

        High-performance model with extended thinking

      - `"claude-4-sonnet-20250514"`

        High-performance model with extended thinking

      - `"claude-sonnet-4-5"`

        Our best model for real-world agents and coding

      - `"claude-sonnet-4-5-20250929"`

        Our best model for real-world agents and coding

      - `"claude-opus-4-0"`

        Our most capable model

      - `"claude-opus-4-20250514"`

        Our most capable model

      - `"claude-4-opus-20250514"`

        Our most capable model

      - `"claude-opus-4-1-20250805"`

        Our most capable model

      - `"claude-3-opus-latest"`

        Excels at writing and complex tasks

      - `"claude-3-opus-20240229"`

        Excels at writing and complex tasks

      - `"claude-3-haiku-20240307"`

        Our previous most fast and cost-effective

    - `(string & {})`

  - `cache_control?: CacheControlEphemeral | null`

    Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `output_config?: OutputConfig`

    Configuration options for the model's output, such as the output format.

    - `effort?: "low" | "medium" | "high" | "max" | null`

      All possible effort levels.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"max"`

    - `format?: JSONOutputFormat | null`

      A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

      - `schema: Record<string, unknown>`

        The JSON schema of the format

      - `type: "json_schema"`

        - `"json_schema"`

  - `system?: string | Array<TextBlockParam>`

    System prompt.

    A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

    - `string`

    - `Array<TextBlockParam>`

      - `text: string`

      - `type: "text"`

        - `"text"`

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `citations?: Array<TextCitationParam> | null`

        - `CitationCharLocationParam`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_char_index: number`

          - `start_char_index: number`

          - `type: "char_location"`

            - `"char_location"`

        - `CitationPageLocationParam`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_page_number: number`

          - `start_page_number: number`

          - `type: "page_location"`

            - `"page_location"`

        - `CitationContentBlockLocationParam`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_block_index: number`

          - `start_block_index: number`

          - `type: "content_block_location"`

            - `"content_block_location"`

        - `CitationWebSearchResultLocationParam`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string | null`

          - `type: "web_search_result_location"`

            - `"web_search_result_location"`

          - `url: string`

        - `CitationSearchResultLocationParam`

          - `cited_text: string`

          - `end_block_index: number`

          - `search_result_index: number`

          - `source: string`

          - `start_block_index: number`

          - `title: string | null`

          - `type: "search_result_location"`

            - `"search_result_location"`

  - `thinking?: ThinkingConfigParam`

    Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

    See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

    - `ThinkingConfigEnabled`

      - `budget_tokens: number`

        Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

        Must be ≥1024 and less than `max_tokens`.

        See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

      - `type: "enabled"`

        - `"enabled"`

    - `ThinkingConfigDisabled`

      - `type: "disabled"`

        - `"disabled"`

    - `ThinkingConfigAdaptive`

      - `type: "adaptive"`

        - `"adaptive"`

  - `tool_choice?: ToolChoice`

    How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

    - `ToolChoiceAuto`

      The model will automatically decide whether to use tools.

      - `type: "auto"`

        - `"auto"`

      - `disable_parallel_tool_use?: boolean`

        Whether to disable parallel tool use.

        Defaults to `false`. If set to `true`, the model will output at most one tool use.

    - `ToolChoiceAny`

      The model will use any available tools.

      - `type: "any"`

        - `"any"`

      - `disable_parallel_tool_use?: boolean`

        Whether to disable parallel tool use.

        Defaults to `false`. If set to `true`, the model will output exactly one tool use.

    - `ToolChoiceTool`

      The model will use the specified tool with `tool_choice.name`.

      - `name: string`

        The name of the tool to use.

      - `type: "tool"`

        - `"tool"`

      - `disable_parallel_tool_use?: boolean`

        Whether to disable parallel tool use.

        Defaults to `false`. If set to `true`, the model will output exactly one tool use.

    - `ToolChoiceNone`

      The model will not be allowed to use tools.

      - `type: "none"`

        - `"none"`

  - `tools?: Array<MessageCountTokensTool>`

    Definitions of tools that the model may use.

    If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

    There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

    Each tool definition includes:

    * `name`: Name of the tool.
    * `description`: Optional, but strongly-recommended description of the tool.
    * `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

    For example, if you defined `tools` as:

    ```json
    [
      {
        "name": "get_stock_price",
        "description": "Get the current stock price for a given ticker symbol.",
        "input_schema": {
          "type": "object",
          "properties": {
            "ticker": {
              "type": "string",
              "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
            }
          },
          "required": ["ticker"]
        }
      }
    ]
    ```

    And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

    ```json
    [
      {
        "type": "tool_use",
        "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
        "name": "get_stock_price",
        "input": { "ticker": "^GSPC" }
      }
    ]
    ```

    You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

    ```json
    [
      {
        "type": "tool_result",
        "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
        "content": "259.75 USD"
      }
    ]
    ```

    Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

    See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

    - `Tool`

      - `input_schema: InputSchema`

        [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

        This defines the shape of the `input` that your tool accepts and that the model will produce.

        - `type: "object"`

          - `"object"`

        - `properties?: Record<string, unknown> | null`

        - `required?: Array<string> | null`

      - `name: string`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `description?: string`

        Description of what this tool does.

        Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

      - `eager_input_streaming?: boolean | null`

        Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

      - `type?: "custom" | null`

        - `"custom"`

    - `ToolBash20250124`

      - `name: "bash"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"bash"`

      - `type: "bash_20250124"`

        - `"bash_20250124"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `CodeExecutionTool20250522`

      - `name: "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"code_execution"`

      - `type: "code_execution_20250522"`

        - `"code_execution_20250522"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `CodeExecutionTool20250825`

      - `name: "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"code_execution"`

      - `type: "code_execution_20250825"`

        - `"code_execution_20250825"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `CodeExecutionTool20260120`

      Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

      - `name: "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"code_execution"`

      - `type: "code_execution_20260120"`

        - `"code_execution_20260120"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `MemoryTool20250818`

      - `name: "memory"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"memory"`

      - `type: "memory_20250818"`

        - `"memory_20250818"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `ToolTextEditor20250124`

      - `name: "str_replace_editor"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"str_replace_editor"`

      - `type: "text_editor_20250124"`

        - `"text_editor_20250124"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `ToolTextEditor20250429`

      - `name: "str_replace_based_edit_tool"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"str_replace_based_edit_tool"`

      - `type: "text_editor_20250429"`

        - `"text_editor_20250429"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `ToolTextEditor20250728`

      - `name: "str_replace_based_edit_tool"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"str_replace_based_edit_tool"`

      - `type: "text_editor_20250728"`

        - `"text_editor_20250728"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `input_examples?: Array<Record<string, unknown>>`

      - `max_characters?: number | null`

        Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `WebSearchTool20250305`

      - `name: "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"web_search"`

      - `type: "web_search_20250305"`

        - `"web_search_20250305"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `allowed_domains?: Array<string> | null`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `blocked_domains?: Array<string> | null`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `max_uses?: number | null`

        Maximum number of times the tool can be used in the API request.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

      - `user_location?: UserLocation | null`

        Parameters for the user's location. Used to provide more relevant search results.

        - `type: "approximate"`

          - `"approximate"`

        - `city?: string | null`

          The city of the user.

        - `country?: string | null`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        - `region?: string | null`

          The region of the user.

        - `timezone?: string | null`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

    - `WebFetchTool20250910`

      - `name: "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"web_fetch"`

      - `type: "web_fetch_20250910"`

        - `"web_fetch_20250910"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `allowed_domains?: Array<string> | null`

        List of domains to allow fetching from

      - `blocked_domains?: Array<string> | null`

        List of domains to block fetching from

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `citations?: CitationsConfigParam | null`

        Citations configuration for fetched documents. Citations are disabled by default.

        - `enabled?: boolean`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `max_content_tokens?: number | null`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      - `max_uses?: number | null`

        Maximum number of times the tool can be used in the API request.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `WebSearchTool20260209`

      - `name: "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"web_search"`

      - `type: "web_search_20260209"`

        - `"web_search_20260209"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `allowed_domains?: Array<string> | null`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `blocked_domains?: Array<string> | null`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `max_uses?: number | null`

        Maximum number of times the tool can be used in the API request.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

      - `user_location?: UserLocation | null`

        Parameters for the user's location. Used to provide more relevant search results.

        - `type: "approximate"`

          - `"approximate"`

        - `city?: string | null`

          The city of the user.

        - `country?: string | null`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        - `region?: string | null`

          The region of the user.

        - `timezone?: string | null`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

    - `WebFetchTool20260209`

      - `name: "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"web_fetch"`

      - `type: "web_fetch_20260209"`

        - `"web_fetch_20260209"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `allowed_domains?: Array<string> | null`

        List of domains to allow fetching from

      - `blocked_domains?: Array<string> | null`

        List of domains to block fetching from

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `citations?: CitationsConfigParam | null`

        Citations configuration for fetched documents. Citations are disabled by default.

        - `enabled?: boolean`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `max_content_tokens?: number | null`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      - `max_uses?: number | null`

        Maximum number of times the tool can be used in the API request.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `ToolSearchToolBm25_20251119`

      - `name: "tool_search_tool_bm25"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"tool_search_tool_bm25"`

      - `type: "tool_search_tool_bm25_20251119" | "tool_search_tool_bm25"`

        - `"tool_search_tool_bm25_20251119"`

        - `"tool_search_tool_bm25"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `ToolSearchToolRegex20251119`

      - `name: "tool_search_tool_regex"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `"tool_search_tool_regex"`

      - `type: "tool_search_tool_regex_20251119" | "tool_search_tool_regex"`

        - `"tool_search_tool_regex_20251119"`

        - `"tool_search_tool_regex"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

### Returns

- `MessageTokensCount`

  - `input_tokens: number`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const messageTokensCount = await client.messages.countTokens({
  messages: [{ content: 'string', role: 'user' }],
  model: 'claude-opus-4-6',
});

console.log(messageTokensCount.input_tokens);
```

## Domain Types

### Base64 Image Source

- `Base64ImageSource`

  - `data: string`

  - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

    - `"image/jpeg"`

    - `"image/png"`

    - `"image/gif"`

    - `"image/webp"`

  - `type: "base64"`

    - `"base64"`

### Base64 PDF Source

- `Base64PDFSource`

  - `data: string`

  - `media_type: "application/pdf"`

    - `"application/pdf"`

  - `type: "base64"`

    - `"base64"`

### Bash Code Execution Output Block

- `BashCodeExecutionOutputBlock`

  - `file_id: string`

  - `type: "bash_code_execution_output"`

    - `"bash_code_execution_output"`

### Bash Code Execution Output Block Param

- `BashCodeExecutionOutputBlockParam`

  - `file_id: string`

  - `type: "bash_code_execution_output"`

    - `"bash_code_execution_output"`

### Bash Code Execution Result Block

- `BashCodeExecutionResultBlock`

  - `content: Array<BashCodeExecutionOutputBlock>`

    - `file_id: string`

    - `type: "bash_code_execution_output"`

      - `"bash_code_execution_output"`

  - `return_code: number`

  - `stderr: string`

  - `stdout: string`

  - `type: "bash_code_execution_result"`

    - `"bash_code_execution_result"`

### Bash Code Execution Result Block Param

- `BashCodeExecutionResultBlockParam`

  - `content: Array<BashCodeExecutionOutputBlockParam>`

    - `file_id: string`

    - `type: "bash_code_execution_output"`

      - `"bash_code_execution_output"`

  - `return_code: number`

  - `stderr: string`

  - `stdout: string`

  - `type: "bash_code_execution_result"`

    - `"bash_code_execution_result"`

### Bash Code Execution Tool Result Block

- `BashCodeExecutionToolResultBlock`

  - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

    - `BashCodeExecutionToolResultError`

      - `error_code: BashCodeExecutionToolResultErrorCode`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

        - `"output_file_too_large"`

      - `type: "bash_code_execution_tool_result_error"`

        - `"bash_code_execution_tool_result_error"`

    - `BashCodeExecutionResultBlock`

      - `content: Array<BashCodeExecutionOutputBlock>`

        - `file_id: string`

        - `type: "bash_code_execution_output"`

          - `"bash_code_execution_output"`

      - `return_code: number`

      - `stderr: string`

      - `stdout: string`

      - `type: "bash_code_execution_result"`

        - `"bash_code_execution_result"`

  - `tool_use_id: string`

  - `type: "bash_code_execution_tool_result"`

    - `"bash_code_execution_tool_result"`

### Bash Code Execution Tool Result Block Param

- `BashCodeExecutionToolResultBlockParam`

  - `content: BashCodeExecutionToolResultErrorParam | BashCodeExecutionResultBlockParam`

    - `BashCodeExecutionToolResultErrorParam`

      - `error_code: BashCodeExecutionToolResultErrorCode`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

        - `"output_file_too_large"`

      - `type: "bash_code_execution_tool_result_error"`

        - `"bash_code_execution_tool_result_error"`

    - `BashCodeExecutionResultBlockParam`

      - `content: Array<BashCodeExecutionOutputBlockParam>`

        - `file_id: string`

        - `type: "bash_code_execution_output"`

          - `"bash_code_execution_output"`

      - `return_code: number`

      - `stderr: string`

      - `stdout: string`

      - `type: "bash_code_execution_result"`

        - `"bash_code_execution_result"`

  - `tool_use_id: string`

  - `type: "bash_code_execution_tool_result"`

    - `"bash_code_execution_tool_result"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Bash Code Execution Tool Result Error

- `BashCodeExecutionToolResultError`

  - `error_code: BashCodeExecutionToolResultErrorCode`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

    - `"output_file_too_large"`

  - `type: "bash_code_execution_tool_result_error"`

    - `"bash_code_execution_tool_result_error"`

### Bash Code Execution Tool Result Error Code

- `BashCodeExecutionToolResultErrorCode = "invalid_tool_input" | "unavailable" | "too_many_requests" | 2 more`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

  - `"output_file_too_large"`

### Bash Code Execution Tool Result Error Param

- `BashCodeExecutionToolResultErrorParam`

  - `error_code: BashCodeExecutionToolResultErrorCode`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

    - `"output_file_too_large"`

  - `type: "bash_code_execution_tool_result_error"`

    - `"bash_code_execution_tool_result_error"`

### Cache Control Ephemeral

- `CacheControlEphemeral`

  - `type: "ephemeral"`

    - `"ephemeral"`

  - `ttl?: "5m" | "1h"`

    The time-to-live for the cache control breakpoint.

    This may be one the following values:

    - `5m`: 5 minutes
    - `1h`: 1 hour

    Defaults to `5m`.

    - `"5m"`

    - `"1h"`

### Cache Creation

- `CacheCreation`

  - `ephemeral_1h_input_tokens: number`

    The number of input tokens used to create the 1 hour cache entry.

  - `ephemeral_5m_input_tokens: number`

    The number of input tokens used to create the 5 minute cache entry.

### Citation Char Location

- `CitationCharLocation`

  - `cited_text: string`

  - `document_index: number`

  - `document_title: string | null`

  - `end_char_index: number`

  - `file_id: string | null`

  - `start_char_index: number`

  - `type: "char_location"`

    - `"char_location"`

### Citation Char Location Param

- `CitationCharLocationParam`

  - `cited_text: string`

  - `document_index: number`

  - `document_title: string | null`

  - `end_char_index: number`

  - `start_char_index: number`

  - `type: "char_location"`

    - `"char_location"`

### Citation Content Block Location

- `CitationContentBlockLocation`

  - `cited_text: string`

  - `document_index: number`

  - `document_title: string | null`

  - `end_block_index: number`

  - `file_id: string | null`

  - `start_block_index: number`

  - `type: "content_block_location"`

    - `"content_block_location"`

### Citation Content Block Location Param

- `CitationContentBlockLocationParam`

  - `cited_text: string`

  - `document_index: number`

  - `document_title: string | null`

  - `end_block_index: number`

  - `start_block_index: number`

  - `type: "content_block_location"`

    - `"content_block_location"`

### Citation Page Location

- `CitationPageLocation`

  - `cited_text: string`

  - `document_index: number`

  - `document_title: string | null`

  - `end_page_number: number`

  - `file_id: string | null`

  - `start_page_number: number`

  - `type: "page_location"`

    - `"page_location"`

### Citation Page Location Param

- `CitationPageLocationParam`

  - `cited_text: string`

  - `document_index: number`

  - `document_title: string | null`

  - `end_page_number: number`

  - `start_page_number: number`

  - `type: "page_location"`

    - `"page_location"`

### Citation Search Result Location Param

- `CitationSearchResultLocationParam`

  - `cited_text: string`

  - `end_block_index: number`

  - `search_result_index: number`

  - `source: string`

  - `start_block_index: number`

  - `title: string | null`

  - `type: "search_result_location"`

    - `"search_result_location"`

### Citation Web Search Result Location Param

- `CitationWebSearchResultLocationParam`

  - `cited_text: string`

  - `encrypted_index: string`

  - `title: string | null`

  - `type: "web_search_result_location"`

    - `"web_search_result_location"`

  - `url: string`

### Citations Config

- `CitationsConfig`

  - `enabled: boolean`

### Citations Config Param

- `CitationsConfigParam`

  - `enabled?: boolean`

### Citations Delta

- `CitationsDelta`

  - `citation: CitationCharLocation | CitationPageLocation | CitationContentBlockLocation | 2 more`

    - `CitationCharLocation`

      - `cited_text: string`

      - `document_index: number`

      - `document_title: string | null`

      - `end_char_index: number`

      - `file_id: string | null`

      - `start_char_index: number`

      - `type: "char_location"`

        - `"char_location"`

    - `CitationPageLocation`

      - `cited_text: string`

      - `document_index: number`

      - `document_title: string | null`

      - `end_page_number: number`

      - `file_id: string | null`

      - `start_page_number: number`

      - `type: "page_location"`

        - `"page_location"`

    - `CitationContentBlockLocation`

      - `cited_text: string`

      - `document_index: number`

      - `document_title: string | null`

      - `end_block_index: number`

      - `file_id: string | null`

      - `start_block_index: number`

      - `type: "content_block_location"`

        - `"content_block_location"`

    - `CitationsWebSearchResultLocation`

      - `cited_text: string`

      - `encrypted_index: string`

      - `title: string | null`

      - `type: "web_search_result_location"`

        - `"web_search_result_location"`

      - `url: string`

    - `CitationsSearchResultLocation`

      - `cited_text: string`

      - `end_block_index: number`

      - `search_result_index: number`

      - `source: string`

      - `start_block_index: number`

      - `title: string | null`

      - `type: "search_result_location"`

        - `"search_result_location"`

  - `type: "citations_delta"`

    - `"citations_delta"`

### Citations Search Result Location

- `CitationsSearchResultLocation`

  - `cited_text: string`

  - `end_block_index: number`

  - `search_result_index: number`

  - `source: string`

  - `start_block_index: number`

  - `title: string | null`

  - `type: "search_result_location"`

    - `"search_result_location"`

### Citations Web Search Result Location

- `CitationsWebSearchResultLocation`

  - `cited_text: string`

  - `encrypted_index: string`

  - `title: string | null`

  - `type: "web_search_result_location"`

    - `"web_search_result_location"`

  - `url: string`

### Code Execution Output Block

- `CodeExecutionOutputBlock`

  - `file_id: string`

  - `type: "code_execution_output"`

    - `"code_execution_output"`

### Code Execution Output Block Param

- `CodeExecutionOutputBlockParam`

  - `file_id: string`

  - `type: "code_execution_output"`

    - `"code_execution_output"`

### Code Execution Result Block

- `CodeExecutionResultBlock`

  - `content: Array<CodeExecutionOutputBlock>`

    - `file_id: string`

    - `type: "code_execution_output"`

      - `"code_execution_output"`

  - `return_code: number`

  - `stderr: string`

  - `stdout: string`

  - `type: "code_execution_result"`

    - `"code_execution_result"`

### Code Execution Result Block Param

- `CodeExecutionResultBlockParam`

  - `content: Array<CodeExecutionOutputBlockParam>`

    - `file_id: string`

    - `type: "code_execution_output"`

      - `"code_execution_output"`

  - `return_code: number`

  - `stderr: string`

  - `stdout: string`

  - `type: "code_execution_result"`

    - `"code_execution_result"`

### Code Execution Tool 20250522

- `CodeExecutionTool20250522`

  - `name: "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution"`

  - `type: "code_execution_20250522"`

    - `"code_execution_20250522"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20250825

- `CodeExecutionTool20250825`

  - `name: "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution"`

  - `type: "code_execution_20250825"`

    - `"code_execution_20250825"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20260120

- `CodeExecutionTool20260120`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `name: "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"code_execution"`

  - `type: "code_execution_20260120"`

    - `"code_execution_20260120"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool Result Block

- `CodeExecutionToolResultBlock`

  - `content: CodeExecutionToolResultBlockContent`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `CodeExecutionToolResultError`

      - `error_code: CodeExecutionToolResultErrorCode`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

      - `type: "code_execution_tool_result_error"`

        - `"code_execution_tool_result_error"`

    - `CodeExecutionResultBlock`

      - `content: Array<CodeExecutionOutputBlock>`

        - `file_id: string`

        - `type: "code_execution_output"`

          - `"code_execution_output"`

      - `return_code: number`

      - `stderr: string`

      - `stdout: string`

      - `type: "code_execution_result"`

        - `"code_execution_result"`

    - `EncryptedCodeExecutionResultBlock`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `content: Array<CodeExecutionOutputBlock>`

        - `file_id: string`

        - `type: "code_execution_output"`

          - `"code_execution_output"`

      - `encrypted_stdout: string`

      - `return_code: number`

      - `stderr: string`

      - `type: "encrypted_code_execution_result"`

        - `"encrypted_code_execution_result"`

  - `tool_use_id: string`

  - `type: "code_execution_tool_result"`

    - `"code_execution_tool_result"`

### Code Execution Tool Result Block Content

- `CodeExecutionToolResultBlockContent = CodeExecutionToolResultError | CodeExecutionResultBlock | EncryptedCodeExecutionResultBlock`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `CodeExecutionToolResultError`

    - `error_code: CodeExecutionToolResultErrorCode`

      - `"invalid_tool_input"`

      - `"unavailable"`

      - `"too_many_requests"`

      - `"execution_time_exceeded"`

    - `type: "code_execution_tool_result_error"`

      - `"code_execution_tool_result_error"`

  - `CodeExecutionResultBlock`

    - `content: Array<CodeExecutionOutputBlock>`

      - `file_id: string`

      - `type: "code_execution_output"`

        - `"code_execution_output"`

    - `return_code: number`

    - `stderr: string`

    - `stdout: string`

    - `type: "code_execution_result"`

      - `"code_execution_result"`

  - `EncryptedCodeExecutionResultBlock`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `content: Array<CodeExecutionOutputBlock>`

      - `file_id: string`

      - `type: "code_execution_output"`

        - `"code_execution_output"`

    - `encrypted_stdout: string`

    - `return_code: number`

    - `stderr: string`

    - `type: "encrypted_code_execution_result"`

      - `"encrypted_code_execution_result"`

### Code Execution Tool Result Block Param

- `CodeExecutionToolResultBlockParam`

  - `content: CodeExecutionToolResultBlockParamContent`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `CodeExecutionToolResultErrorParam`

      - `error_code: CodeExecutionToolResultErrorCode`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

      - `type: "code_execution_tool_result_error"`

        - `"code_execution_tool_result_error"`

    - `CodeExecutionResultBlockParam`

      - `content: Array<CodeExecutionOutputBlockParam>`

        - `file_id: string`

        - `type: "code_execution_output"`

          - `"code_execution_output"`

      - `return_code: number`

      - `stderr: string`

      - `stdout: string`

      - `type: "code_execution_result"`

        - `"code_execution_result"`

    - `EncryptedCodeExecutionResultBlockParam`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `content: Array<CodeExecutionOutputBlockParam>`

        - `file_id: string`

        - `type: "code_execution_output"`

          - `"code_execution_output"`

      - `encrypted_stdout: string`

      - `return_code: number`

      - `stderr: string`

      - `type: "encrypted_code_execution_result"`

        - `"encrypted_code_execution_result"`

  - `tool_use_id: string`

  - `type: "code_execution_tool_result"`

    - `"code_execution_tool_result"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Code Execution Tool Result Block Param Content

- `CodeExecutionToolResultBlockParamContent = CodeExecutionToolResultErrorParam | CodeExecutionResultBlockParam | EncryptedCodeExecutionResultBlockParam`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `CodeExecutionToolResultErrorParam`

    - `error_code: CodeExecutionToolResultErrorCode`

      - `"invalid_tool_input"`

      - `"unavailable"`

      - `"too_many_requests"`

      - `"execution_time_exceeded"`

    - `type: "code_execution_tool_result_error"`

      - `"code_execution_tool_result_error"`

  - `CodeExecutionResultBlockParam`

    - `content: Array<CodeExecutionOutputBlockParam>`

      - `file_id: string`

      - `type: "code_execution_output"`

        - `"code_execution_output"`

    - `return_code: number`

    - `stderr: string`

    - `stdout: string`

    - `type: "code_execution_result"`

      - `"code_execution_result"`

  - `EncryptedCodeExecutionResultBlockParam`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `content: Array<CodeExecutionOutputBlockParam>`

      - `file_id: string`

      - `type: "code_execution_output"`

        - `"code_execution_output"`

    - `encrypted_stdout: string`

    - `return_code: number`

    - `stderr: string`

    - `type: "encrypted_code_execution_result"`

      - `"encrypted_code_execution_result"`

### Code Execution Tool Result Error

- `CodeExecutionToolResultError`

  - `error_code: CodeExecutionToolResultErrorCode`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

  - `type: "code_execution_tool_result_error"`

    - `"code_execution_tool_result_error"`

### Code Execution Tool Result Error Code

- `CodeExecutionToolResultErrorCode = "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded"`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

### Code Execution Tool Result Error Param

- `CodeExecutionToolResultErrorParam`

  - `error_code: CodeExecutionToolResultErrorCode`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

  - `type: "code_execution_tool_result_error"`

    - `"code_execution_tool_result_error"`

### Container

- `Container`

  Information about the container used in the request (for the code execution tool)

  - `id: string`

    Identifier for the container used in this request

  - `expires_at: string`

    The time at which the container will expire.

### Container Upload Block

- `ContainerUploadBlock`

  Response model for a file uploaded to the container.

  - `file_id: string`

  - `type: "container_upload"`

    - `"container_upload"`

### Container Upload Block Param

- `ContainerUploadBlockParam`

  A content block that represents a file to be uploaded to the container
  Files uploaded via this block will be available in the container's input directory.

  - `file_id: string`

  - `type: "container_upload"`

    - `"container_upload"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Content Block

- `ContentBlock = TextBlock | ThinkingBlock | RedactedThinkingBlock | 9 more`

  Response model for a file uploaded to the container.

  - `TextBlock`

    - `citations: Array<TextCitation> | null`

      Citations supporting the text block.

      The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

      - `CitationCharLocation`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_char_index: number`

        - `file_id: string | null`

        - `start_char_index: number`

        - `type: "char_location"`

          - `"char_location"`

      - `CitationPageLocation`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_page_number: number`

        - `file_id: string | null`

        - `start_page_number: number`

        - `type: "page_location"`

          - `"page_location"`

      - `CitationContentBlockLocation`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_block_index: number`

        - `file_id: string | null`

        - `start_block_index: number`

        - `type: "content_block_location"`

          - `"content_block_location"`

      - `CitationsWebSearchResultLocation`

        - `cited_text: string`

        - `encrypted_index: string`

        - `title: string | null`

        - `type: "web_search_result_location"`

          - `"web_search_result_location"`

        - `url: string`

      - `CitationsSearchResultLocation`

        - `cited_text: string`

        - `end_block_index: number`

        - `search_result_index: number`

        - `source: string`

        - `start_block_index: number`

        - `title: string | null`

        - `type: "search_result_location"`

          - `"search_result_location"`

    - `text: string`

    - `type: "text"`

      - `"text"`

  - `ThinkingBlock`

    - `signature: string`

    - `thinking: string`

    - `type: "thinking"`

      - `"thinking"`

  - `RedactedThinkingBlock`

    - `data: string`

    - `type: "redacted_thinking"`

      - `"redacted_thinking"`

  - `ToolUseBlock`

    - `id: string`

    - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `DirectCaller`

        Tool invocation directly from the model.

        - `type: "direct"`

          - `"direct"`

      - `ServerToolCaller`

        Tool invocation generated by a server-side tool.

        - `tool_id: string`

        - `type: "code_execution_20250825"`

          - `"code_execution_20250825"`

      - `ServerToolCaller20260120`

        - `tool_id: string`

        - `type: "code_execution_20260120"`

          - `"code_execution_20260120"`

    - `input: Record<string, unknown>`

    - `name: string`

    - `type: "tool_use"`

      - `"tool_use"`

  - `ServerToolUseBlock`

    - `id: string`

    - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `DirectCaller`

        Tool invocation directly from the model.

        - `type: "direct"`

          - `"direct"`

      - `ServerToolCaller`

        Tool invocation generated by a server-side tool.

        - `tool_id: string`

        - `type: "code_execution_20250825"`

          - `"code_execution_20250825"`

      - `ServerToolCaller20260120`

        - `tool_id: string`

        - `type: "code_execution_20260120"`

          - `"code_execution_20260120"`

    - `input: Record<string, unknown>`

    - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

      - `"web_search"`

      - `"web_fetch"`

      - `"code_execution"`

      - `"bash_code_execution"`

      - `"text_editor_code_execution"`

      - `"tool_search_tool_regex"`

      - `"tool_search_tool_bm25"`

    - `type: "server_tool_use"`

      - `"server_tool_use"`

  - `WebSearchToolResultBlock`

    - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `DirectCaller`

        Tool invocation directly from the model.

        - `type: "direct"`

          - `"direct"`

      - `ServerToolCaller`

        Tool invocation generated by a server-side tool.

        - `tool_id: string`

        - `type: "code_execution_20250825"`

          - `"code_execution_20250825"`

      - `ServerToolCaller20260120`

        - `tool_id: string`

        - `type: "code_execution_20260120"`

          - `"code_execution_20260120"`

    - `content: WebSearchToolResultBlockContent`

      - `WebSearchToolResultError`

        - `error_code: WebSearchToolResultErrorCode`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"max_uses_exceeded"`

          - `"too_many_requests"`

          - `"query_too_long"`

          - `"request_too_large"`

        - `type: "web_search_tool_result_error"`

          - `"web_search_tool_result_error"`

      - `Array<WebSearchResultBlock>`

        - `encrypted_content: string`

        - `page_age: string | null`

        - `title: string`

        - `type: "web_search_result"`

          - `"web_search_result"`

        - `url: string`

    - `tool_use_id: string`

    - `type: "web_search_tool_result"`

      - `"web_search_tool_result"`

  - `WebFetchToolResultBlock`

    - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `DirectCaller`

        Tool invocation directly from the model.

        - `type: "direct"`

          - `"direct"`

      - `ServerToolCaller`

        Tool invocation generated by a server-side tool.

        - `tool_id: string`

        - `type: "code_execution_20250825"`

          - `"code_execution_20250825"`

      - `ServerToolCaller20260120`

        - `tool_id: string`

        - `type: "code_execution_20260120"`

          - `"code_execution_20260120"`

    - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

      - `WebFetchToolResultErrorBlock`

        - `error_code: WebFetchToolResultErrorCode`

          - `"invalid_tool_input"`

          - `"url_too_long"`

          - `"url_not_allowed"`

          - `"url_not_accessible"`

          - `"unsupported_content_type"`

          - `"too_many_requests"`

          - `"max_uses_exceeded"`

          - `"unavailable"`

        - `type: "web_fetch_tool_result_error"`

          - `"web_fetch_tool_result_error"`

      - `WebFetchBlock`

        - `content: DocumentBlock`

          - `citations: CitationsConfig | null`

            Citation configuration for the document

            - `enabled: boolean`

          - `source: Base64PDFSource | PlainTextSource`

            - `Base64PDFSource`

              - `data: string`

              - `media_type: "application/pdf"`

                - `"application/pdf"`

              - `type: "base64"`

                - `"base64"`

            - `PlainTextSource`

              - `data: string`

              - `media_type: "text/plain"`

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

          - `title: string | null`

            The title of the document

          - `type: "document"`

            - `"document"`

        - `retrieved_at: string | null`

          ISO 8601 timestamp when the content was retrieved

        - `type: "web_fetch_result"`

          - `"web_fetch_result"`

        - `url: string`

          Fetched content URL

    - `tool_use_id: string`

    - `type: "web_fetch_tool_result"`

      - `"web_fetch_tool_result"`

  - `CodeExecutionToolResultBlock`

    - `content: CodeExecutionToolResultBlockContent`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `CodeExecutionToolResultError`

        - `error_code: CodeExecutionToolResultErrorCode`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

        - `type: "code_execution_tool_result_error"`

          - `"code_execution_tool_result_error"`

      - `CodeExecutionResultBlock`

        - `content: Array<CodeExecutionOutputBlock>`

          - `file_id: string`

          - `type: "code_execution_output"`

            - `"code_execution_output"`

        - `return_code: number`

        - `stderr: string`

        - `stdout: string`

        - `type: "code_execution_result"`

          - `"code_execution_result"`

      - `EncryptedCodeExecutionResultBlock`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `content: Array<CodeExecutionOutputBlock>`

          - `file_id: string`

          - `type: "code_execution_output"`

            - `"code_execution_output"`

        - `encrypted_stdout: string`

        - `return_code: number`

        - `stderr: string`

        - `type: "encrypted_code_execution_result"`

          - `"encrypted_code_execution_result"`

    - `tool_use_id: string`

    - `type: "code_execution_tool_result"`

      - `"code_execution_tool_result"`

  - `BashCodeExecutionToolResultBlock`

    - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

      - `BashCodeExecutionToolResultError`

        - `error_code: BashCodeExecutionToolResultErrorCode`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

          - `"output_file_too_large"`

        - `type: "bash_code_execution_tool_result_error"`

          - `"bash_code_execution_tool_result_error"`

      - `BashCodeExecutionResultBlock`

        - `content: Array<BashCodeExecutionOutputBlock>`

          - `file_id: string`

          - `type: "bash_code_execution_output"`

            - `"bash_code_execution_output"`

        - `return_code: number`

        - `stderr: string`

        - `stdout: string`

        - `type: "bash_code_execution_result"`

          - `"bash_code_execution_result"`

    - `tool_use_id: string`

    - `type: "bash_code_execution_tool_result"`

      - `"bash_code_execution_tool_result"`

  - `TextEditorCodeExecutionToolResultBlock`

    - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

      - `TextEditorCodeExecutionToolResultError`

        - `error_code: TextEditorCodeExecutionToolResultErrorCode`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

          - `"file_not_found"`

        - `error_message: string | null`

        - `type: "text_editor_code_execution_tool_result_error"`

          - `"text_editor_code_execution_tool_result_error"`

      - `TextEditorCodeExecutionViewResultBlock`

        - `content: string`

        - `file_type: "text" | "image" | "pdf"`

          - `"text"`

          - `"image"`

          - `"pdf"`

        - `num_lines: number | null`

        - `start_line: number | null`

        - `total_lines: number | null`

        - `type: "text_editor_code_execution_view_result"`

          - `"text_editor_code_execution_view_result"`

      - `TextEditorCodeExecutionCreateResultBlock`

        - `is_file_update: boolean`

        - `type: "text_editor_code_execution_create_result"`

          - `"text_editor_code_execution_create_result"`

      - `TextEditorCodeExecutionStrReplaceResultBlock`

        - `lines: Array<string> | null`

        - `new_lines: number | null`

        - `new_start: number | null`

        - `old_lines: number | null`

        - `old_start: number | null`

        - `type: "text_editor_code_execution_str_replace_result"`

          - `"text_editor_code_execution_str_replace_result"`

    - `tool_use_id: string`

    - `type: "text_editor_code_execution_tool_result"`

      - `"text_editor_code_execution_tool_result"`

  - `ToolSearchToolResultBlock`

    - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

      - `ToolSearchToolResultError`

        - `error_code: ToolSearchToolResultErrorCode`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

        - `error_message: string | null`

        - `type: "tool_search_tool_result_error"`

          - `"tool_search_tool_result_error"`

      - `ToolSearchToolSearchResultBlock`

        - `tool_references: Array<ToolReferenceBlock>`

          - `tool_name: string`

          - `type: "tool_reference"`

            - `"tool_reference"`

        - `type: "tool_search_tool_search_result"`

          - `"tool_search_tool_search_result"`

    - `tool_use_id: string`

    - `type: "tool_search_tool_result"`

      - `"tool_search_tool_result"`

  - `ContainerUploadBlock`

    Response model for a file uploaded to the container.

    - `file_id: string`

    - `type: "container_upload"`

      - `"container_upload"`

### Content Block Param

- `ContentBlockParam = TextBlockParam | ImageBlockParam | DocumentBlockParam | 13 more`

  Regular text content.

  - `TextBlockParam`

    - `text: string`

    - `type: "text"`

      - `"text"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations?: Array<TextCitationParam> | null`

      - `CitationCharLocationParam`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_char_index: number`

        - `start_char_index: number`

        - `type: "char_location"`

          - `"char_location"`

      - `CitationPageLocationParam`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_page_number: number`

        - `start_page_number: number`

        - `type: "page_location"`

          - `"page_location"`

      - `CitationContentBlockLocationParam`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_block_index: number`

        - `start_block_index: number`

        - `type: "content_block_location"`

          - `"content_block_location"`

      - `CitationWebSearchResultLocationParam`

        - `cited_text: string`

        - `encrypted_index: string`

        - `title: string | null`

        - `type: "web_search_result_location"`

          - `"web_search_result_location"`

        - `url: string`

      - `CitationSearchResultLocationParam`

        - `cited_text: string`

        - `end_block_index: number`

        - `search_result_index: number`

        - `source: string`

        - `start_block_index: number`

        - `title: string | null`

        - `type: "search_result_location"`

          - `"search_result_location"`

  - `ImageBlockParam`

    - `source: Base64ImageSource | URLImageSource`

      - `Base64ImageSource`

        - `data: string`

        - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

          - `"image/jpeg"`

          - `"image/png"`

          - `"image/gif"`

          - `"image/webp"`

        - `type: "base64"`

          - `"base64"`

      - `URLImageSource`

        - `type: "url"`

          - `"url"`

        - `url: string`

    - `type: "image"`

      - `"image"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `DocumentBlockParam`

    - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

      - `Base64PDFSource`

        - `data: string`

        - `media_type: "application/pdf"`

          - `"application/pdf"`

        - `type: "base64"`

          - `"base64"`

      - `PlainTextSource`

        - `data: string`

        - `media_type: "text/plain"`

          - `"text/plain"`

        - `type: "text"`

          - `"text"`

      - `ContentBlockSource`

        - `content: string | Array<ContentBlockSourceContent>`

          - `string`

          - `Array<ContentBlockSourceContent>`

            - `TextBlockParam`

              - `text: string`

              - `type: "text"`

                - `"text"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations?: Array<TextCitationParam> | null`

                - `CitationCharLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_char_index: number`

                  - `start_char_index: number`

                  - `type: "char_location"`

                    - `"char_location"`

                - `CitationPageLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_page_number: number`

                  - `start_page_number: number`

                  - `type: "page_location"`

                    - `"page_location"`

                - `CitationContentBlockLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_block_index: number`

                  - `start_block_index: number`

                  - `type: "content_block_location"`

                    - `"content_block_location"`

                - `CitationWebSearchResultLocationParam`

                  - `cited_text: string`

                  - `encrypted_index: string`

                  - `title: string | null`

                  - `type: "web_search_result_location"`

                    - `"web_search_result_location"`

                  - `url: string`

                - `CitationSearchResultLocationParam`

                  - `cited_text: string`

                  - `end_block_index: number`

                  - `search_result_index: number`

                  - `source: string`

                  - `start_block_index: number`

                  - `title: string | null`

                  - `type: "search_result_location"`

                    - `"search_result_location"`

            - `ImageBlockParam`

              - `source: Base64ImageSource | URLImageSource`

                - `Base64ImageSource`

                  - `data: string`

                  - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                    - `"image/jpeg"`

                    - `"image/png"`

                    - `"image/gif"`

                    - `"image/webp"`

                  - `type: "base64"`

                    - `"base64"`

                - `URLImageSource`

                  - `type: "url"`

                    - `"url"`

                  - `url: string`

              - `type: "image"`

                - `"image"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

        - `type: "content"`

          - `"content"`

      - `URLPDFSource`

        - `type: "url"`

          - `"url"`

        - `url: string`

    - `type: "document"`

      - `"document"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations?: CitationsConfigParam | null`

      - `enabled?: boolean`

    - `context?: string | null`

    - `title?: string | null`

  - `SearchResultBlockParam`

    - `content: Array<TextBlockParam>`

      - `text: string`

      - `type: "text"`

        - `"text"`

      - `cache_control?: CacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `citations?: Array<TextCitationParam> | null`

        - `CitationCharLocationParam`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_char_index: number`

          - `start_char_index: number`

          - `type: "char_location"`

            - `"char_location"`

        - `CitationPageLocationParam`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_page_number: number`

          - `start_page_number: number`

          - `type: "page_location"`

            - `"page_location"`

        - `CitationContentBlockLocationParam`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_block_index: number`

          - `start_block_index: number`

          - `type: "content_block_location"`

            - `"content_block_location"`

        - `CitationWebSearchResultLocationParam`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string | null`

          - `type: "web_search_result_location"`

            - `"web_search_result_location"`

          - `url: string`

        - `CitationSearchResultLocationParam`

          - `cited_text: string`

          - `end_block_index: number`

          - `search_result_index: number`

          - `source: string`

          - `start_block_index: number`

          - `title: string | null`

          - `type: "search_result_location"`

            - `"search_result_location"`

    - `source: string`

    - `title: string`

    - `type: "search_result"`

      - `"search_result"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations?: CitationsConfigParam`

      - `enabled?: boolean`

  - `ThinkingBlockParam`

    - `signature: string`

    - `thinking: string`

    - `type: "thinking"`

      - `"thinking"`

  - `RedactedThinkingBlockParam`

    - `data: string`

    - `type: "redacted_thinking"`

      - `"redacted_thinking"`

  - `ToolUseBlockParam`

    - `id: string`

    - `input: Record<string, unknown>`

    - `name: string`

    - `type: "tool_use"`

      - `"tool_use"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `DirectCaller`

        Tool invocation directly from the model.

        - `type: "direct"`

          - `"direct"`

      - `ServerToolCaller`

        Tool invocation generated by a server-side tool.

        - `tool_id: string`

        - `type: "code_execution_20250825"`

          - `"code_execution_20250825"`

      - `ServerToolCaller20260120`

        - `tool_id: string`

        - `type: "code_execution_20260120"`

          - `"code_execution_20260120"`

  - `ToolResultBlockParam`

    - `tool_use_id: string`

    - `type: "tool_result"`

      - `"tool_result"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `content?: string | Array<TextBlockParam | ImageBlockParam | SearchResultBlockParam | 2 more>`

      - `string`

      - `Array<TextBlockParam | ImageBlockParam | SearchResultBlockParam | 2 more>`

        - `TextBlockParam`

          - `text: string`

          - `type: "text"`

            - `"text"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations?: Array<TextCitationParam> | null`

            - `CitationCharLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_char_index: number`

              - `start_char_index: number`

              - `type: "char_location"`

                - `"char_location"`

            - `CitationPageLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_page_number: number`

              - `start_page_number: number`

              - `type: "page_location"`

                - `"page_location"`

            - `CitationContentBlockLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_block_index: number`

              - `start_block_index: number`

              - `type: "content_block_location"`

                - `"content_block_location"`

            - `CitationWebSearchResultLocationParam`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string | null`

              - `type: "web_search_result_location"`

                - `"web_search_result_location"`

              - `url: string`

            - `CitationSearchResultLocationParam`

              - `cited_text: string`

              - `end_block_index: number`

              - `search_result_index: number`

              - `source: string`

              - `start_block_index: number`

              - `title: string | null`

              - `type: "search_result_location"`

                - `"search_result_location"`

        - `ImageBlockParam`

          - `source: Base64ImageSource | URLImageSource`

            - `Base64ImageSource`

              - `data: string`

              - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                - `"image/jpeg"`

                - `"image/png"`

                - `"image/gif"`

                - `"image/webp"`

              - `type: "base64"`

                - `"base64"`

            - `URLImageSource`

              - `type: "url"`

                - `"url"`

              - `url: string`

          - `type: "image"`

            - `"image"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

        - `SearchResultBlockParam`

          - `content: Array<TextBlockParam>`

            - `text: string`

            - `type: "text"`

              - `"text"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `citations?: Array<TextCitationParam> | null`

              - `CitationCharLocationParam`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_char_index: number`

                - `start_char_index: number`

                - `type: "char_location"`

                  - `"char_location"`

              - `CitationPageLocationParam`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_page_number: number`

                - `start_page_number: number`

                - `type: "page_location"`

                  - `"page_location"`

              - `CitationContentBlockLocationParam`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_block_index: number`

                - `start_block_index: number`

                - `type: "content_block_location"`

                  - `"content_block_location"`

              - `CitationWebSearchResultLocationParam`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string | null`

                - `type: "web_search_result_location"`

                  - `"web_search_result_location"`

                - `url: string`

              - `CitationSearchResultLocationParam`

                - `cited_text: string`

                - `end_block_index: number`

                - `search_result_index: number`

                - `source: string`

                - `start_block_index: number`

                - `title: string | null`

                - `type: "search_result_location"`

                  - `"search_result_location"`

          - `source: string`

          - `title: string`

          - `type: "search_result"`

            - `"search_result"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations?: CitationsConfigParam`

            - `enabled?: boolean`

        - `DocumentBlockParam`

          - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

            - `Base64PDFSource`

              - `data: string`

              - `media_type: "application/pdf"`

                - `"application/pdf"`

              - `type: "base64"`

                - `"base64"`

            - `PlainTextSource`

              - `data: string`

              - `media_type: "text/plain"`

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `ContentBlockSource`

              - `content: string | Array<ContentBlockSourceContent>`

                - `string`

                - `Array<ContentBlockSourceContent>`

                  - `TextBlockParam`

                    - `text: string`

                    - `type: "text"`

                      - `"text"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

                    - `citations?: Array<TextCitationParam> | null`

                      - `CitationCharLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_char_index: number`

                        - `start_char_index: number`

                        - `type: "char_location"`

                          - `"char_location"`

                      - `CitationPageLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_page_number: number`

                        - `start_page_number: number`

                        - `type: "page_location"`

                          - `"page_location"`

                      - `CitationContentBlockLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_block_index: number`

                        - `start_block_index: number`

                        - `type: "content_block_location"`

                          - `"content_block_location"`

                      - `CitationWebSearchResultLocationParam`

                        - `cited_text: string`

                        - `encrypted_index: string`

                        - `title: string | null`

                        - `type: "web_search_result_location"`

                          - `"web_search_result_location"`

                        - `url: string`

                      - `CitationSearchResultLocationParam`

                        - `cited_text: string`

                        - `end_block_index: number`

                        - `search_result_index: number`

                        - `source: string`

                        - `start_block_index: number`

                        - `title: string | null`

                        - `type: "search_result_location"`

                          - `"search_result_location"`

                  - `ImageBlockParam`

                    - `source: Base64ImageSource | URLImageSource`

                      - `Base64ImageSource`

                        - `data: string`

                        - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                          - `"image/jpeg"`

                          - `"image/png"`

                          - `"image/gif"`

                          - `"image/webp"`

                        - `type: "base64"`

                          - `"base64"`

                      - `URLImageSource`

                        - `type: "url"`

                          - `"url"`

                        - `url: string`

                    - `type: "image"`

                      - `"image"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

              - `type: "content"`

                - `"content"`

            - `URLPDFSource`

              - `type: "url"`

                - `"url"`

              - `url: string`

          - `type: "document"`

            - `"document"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations?: CitationsConfigParam | null`

            - `enabled?: boolean`

          - `context?: string | null`

          - `title?: string | null`

        - `ToolReferenceBlockParam`

          Tool reference block that can be included in tool_result content.

          - `tool_name: string`

          - `type: "tool_reference"`

            - `"tool_reference"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

    - `is_error?: boolean`

  - `ServerToolUseBlockParam`

    - `id: string`

    - `input: Record<string, unknown>`

    - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

      - `"web_search"`

      - `"web_fetch"`

      - `"code_execution"`

      - `"bash_code_execution"`

      - `"text_editor_code_execution"`

      - `"tool_search_tool_regex"`

      - `"tool_search_tool_bm25"`

    - `type: "server_tool_use"`

      - `"server_tool_use"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `DirectCaller`

        Tool invocation directly from the model.

        - `type: "direct"`

          - `"direct"`

      - `ServerToolCaller`

        Tool invocation generated by a server-side tool.

        - `tool_id: string`

        - `type: "code_execution_20250825"`

          - `"code_execution_20250825"`

      - `ServerToolCaller20260120`

        - `tool_id: string`

        - `type: "code_execution_20260120"`

          - `"code_execution_20260120"`

  - `WebSearchToolResultBlockParam`

    - `content: WebSearchToolResultBlockParamContent`

      - `Array<WebSearchResultBlockParam>`

        - `encrypted_content: string`

        - `title: string`

        - `type: "web_search_result"`

          - `"web_search_result"`

        - `url: string`

        - `page_age?: string | null`

      - `WebSearchToolRequestError`

        - `error_code: WebSearchToolResultErrorCode`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"max_uses_exceeded"`

          - `"too_many_requests"`

          - `"query_too_long"`

          - `"request_too_large"`

        - `type: "web_search_tool_result_error"`

          - `"web_search_tool_result_error"`

    - `tool_use_id: string`

    - `type: "web_search_tool_result"`

      - `"web_search_tool_result"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `DirectCaller`

        Tool invocation directly from the model.

        - `type: "direct"`

          - `"direct"`

      - `ServerToolCaller`

        Tool invocation generated by a server-side tool.

        - `tool_id: string`

        - `type: "code_execution_20250825"`

          - `"code_execution_20250825"`

      - `ServerToolCaller20260120`

        - `tool_id: string`

        - `type: "code_execution_20260120"`

          - `"code_execution_20260120"`

  - `WebFetchToolResultBlockParam`

    - `content: WebFetchToolResultErrorBlockParam | WebFetchBlockParam`

      - `WebFetchToolResultErrorBlockParam`

        - `error_code: WebFetchToolResultErrorCode`

          - `"invalid_tool_input"`

          - `"url_too_long"`

          - `"url_not_allowed"`

          - `"url_not_accessible"`

          - `"unsupported_content_type"`

          - `"too_many_requests"`

          - `"max_uses_exceeded"`

          - `"unavailable"`

        - `type: "web_fetch_tool_result_error"`

          - `"web_fetch_tool_result_error"`

      - `WebFetchBlockParam`

        - `content: DocumentBlockParam`

          - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

            - `Base64PDFSource`

              - `data: string`

              - `media_type: "application/pdf"`

                - `"application/pdf"`

              - `type: "base64"`

                - `"base64"`

            - `PlainTextSource`

              - `data: string`

              - `media_type: "text/plain"`

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `ContentBlockSource`

              - `content: string | Array<ContentBlockSourceContent>`

                - `string`

                - `Array<ContentBlockSourceContent>`

                  - `TextBlockParam`

                    - `text: string`

                    - `type: "text"`

                      - `"text"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

                    - `citations?: Array<TextCitationParam> | null`

                      - `CitationCharLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_char_index: number`

                        - `start_char_index: number`

                        - `type: "char_location"`

                          - `"char_location"`

                      - `CitationPageLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_page_number: number`

                        - `start_page_number: number`

                        - `type: "page_location"`

                          - `"page_location"`

                      - `CitationContentBlockLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_block_index: number`

                        - `start_block_index: number`

                        - `type: "content_block_location"`

                          - `"content_block_location"`

                      - `CitationWebSearchResultLocationParam`

                        - `cited_text: string`

                        - `encrypted_index: string`

                        - `title: string | null`

                        - `type: "web_search_result_location"`

                          - `"web_search_result_location"`

                        - `url: string`

                      - `CitationSearchResultLocationParam`

                        - `cited_text: string`

                        - `end_block_index: number`

                        - `search_result_index: number`

                        - `source: string`

                        - `start_block_index: number`

                        - `title: string | null`

                        - `type: "search_result_location"`

                          - `"search_result_location"`

                  - `ImageBlockParam`

                    - `source: Base64ImageSource | URLImageSource`

                      - `Base64ImageSource`

                        - `data: string`

                        - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                          - `"image/jpeg"`

                          - `"image/png"`

                          - `"image/gif"`

                          - `"image/webp"`

                        - `type: "base64"`

                          - `"base64"`

                      - `URLImageSource`

                        - `type: "url"`

                          - `"url"`

                        - `url: string`

                    - `type: "image"`

                      - `"image"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

              - `type: "content"`

                - `"content"`

            - `URLPDFSource`

              - `type: "url"`

                - `"url"`

              - `url: string`

          - `type: "document"`

            - `"document"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations?: CitationsConfigParam | null`

            - `enabled?: boolean`

          - `context?: string | null`

          - `title?: string | null`

        - `type: "web_fetch_result"`

          - `"web_fetch_result"`

        - `url: string`

          Fetched content URL

        - `retrieved_at?: string | null`

          ISO 8601 timestamp when the content was retrieved

    - `tool_use_id: string`

    - `type: "web_fetch_tool_result"`

      - `"web_fetch_tool_result"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `DirectCaller`

        Tool invocation directly from the model.

        - `type: "direct"`

          - `"direct"`

      - `ServerToolCaller`

        Tool invocation generated by a server-side tool.

        - `tool_id: string`

        - `type: "code_execution_20250825"`

          - `"code_execution_20250825"`

      - `ServerToolCaller20260120`

        - `tool_id: string`

        - `type: "code_execution_20260120"`

          - `"code_execution_20260120"`

  - `CodeExecutionToolResultBlockParam`

    - `content: CodeExecutionToolResultBlockParamContent`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `CodeExecutionToolResultErrorParam`

        - `error_code: CodeExecutionToolResultErrorCode`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

        - `type: "code_execution_tool_result_error"`

          - `"code_execution_tool_result_error"`

      - `CodeExecutionResultBlockParam`

        - `content: Array<CodeExecutionOutputBlockParam>`

          - `file_id: string`

          - `type: "code_execution_output"`

            - `"code_execution_output"`

        - `return_code: number`

        - `stderr: string`

        - `stdout: string`

        - `type: "code_execution_result"`

          - `"code_execution_result"`

      - `EncryptedCodeExecutionResultBlockParam`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `content: Array<CodeExecutionOutputBlockParam>`

          - `file_id: string`

          - `type: "code_execution_output"`

            - `"code_execution_output"`

        - `encrypted_stdout: string`

        - `return_code: number`

        - `stderr: string`

        - `type: "encrypted_code_execution_result"`

          - `"encrypted_code_execution_result"`

    - `tool_use_id: string`

    - `type: "code_execution_tool_result"`

      - `"code_execution_tool_result"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `BashCodeExecutionToolResultBlockParam`

    - `content: BashCodeExecutionToolResultErrorParam | BashCodeExecutionResultBlockParam`

      - `BashCodeExecutionToolResultErrorParam`

        - `error_code: BashCodeExecutionToolResultErrorCode`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

          - `"output_file_too_large"`

        - `type: "bash_code_execution_tool_result_error"`

          - `"bash_code_execution_tool_result_error"`

      - `BashCodeExecutionResultBlockParam`

        - `content: Array<BashCodeExecutionOutputBlockParam>`

          - `file_id: string`

          - `type: "bash_code_execution_output"`

            - `"bash_code_execution_output"`

        - `return_code: number`

        - `stderr: string`

        - `stdout: string`

        - `type: "bash_code_execution_result"`

          - `"bash_code_execution_result"`

    - `tool_use_id: string`

    - `type: "bash_code_execution_tool_result"`

      - `"bash_code_execution_tool_result"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `TextEditorCodeExecutionToolResultBlockParam`

    - `content: TextEditorCodeExecutionToolResultErrorParam | TextEditorCodeExecutionViewResultBlockParam | TextEditorCodeExecutionCreateResultBlockParam | TextEditorCodeExecutionStrReplaceResultBlockParam`

      - `TextEditorCodeExecutionToolResultErrorParam`

        - `error_code: TextEditorCodeExecutionToolResultErrorCode`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

          - `"file_not_found"`

        - `type: "text_editor_code_execution_tool_result_error"`

          - `"text_editor_code_execution_tool_result_error"`

        - `error_message?: string | null`

      - `TextEditorCodeExecutionViewResultBlockParam`

        - `content: string`

        - `file_type: "text" | "image" | "pdf"`

          - `"text"`

          - `"image"`

          - `"pdf"`

        - `type: "text_editor_code_execution_view_result"`

          - `"text_editor_code_execution_view_result"`

        - `num_lines?: number | null`

        - `start_line?: number | null`

        - `total_lines?: number | null`

      - `TextEditorCodeExecutionCreateResultBlockParam`

        - `is_file_update: boolean`

        - `type: "text_editor_code_execution_create_result"`

          - `"text_editor_code_execution_create_result"`

      - `TextEditorCodeExecutionStrReplaceResultBlockParam`

        - `type: "text_editor_code_execution_str_replace_result"`

          - `"text_editor_code_execution_str_replace_result"`

        - `lines?: Array<string> | null`

        - `new_lines?: number | null`

        - `new_start?: number | null`

        - `old_lines?: number | null`

        - `old_start?: number | null`

    - `tool_use_id: string`

    - `type: "text_editor_code_execution_tool_result"`

      - `"text_editor_code_execution_tool_result"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `ToolSearchToolResultBlockParam`

    - `content: ToolSearchToolResultErrorParam | ToolSearchToolSearchResultBlockParam`

      - `ToolSearchToolResultErrorParam`

        - `error_code: ToolSearchToolResultErrorCode`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

        - `type: "tool_search_tool_result_error"`

          - `"tool_search_tool_result_error"`

      - `ToolSearchToolSearchResultBlockParam`

        - `tool_references: Array<ToolReferenceBlockParam>`

          - `tool_name: string`

          - `type: "tool_reference"`

            - `"tool_reference"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

        - `type: "tool_search_tool_search_result"`

          - `"tool_search_tool_search_result"`

    - `tool_use_id: string`

    - `type: "tool_search_tool_result"`

      - `"tool_search_tool_result"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `ContainerUploadBlockParam`

    A content block that represents a file to be uploaded to the container
    Files uploaded via this block will be available in the container's input directory.

    - `file_id: string`

    - `type: "container_upload"`

      - `"container_upload"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

### Content Block Source

- `ContentBlockSource`

  - `content: string | Array<ContentBlockSourceContent>`

    - `string`

    - `Array<ContentBlockSourceContent>`

      - `TextBlockParam`

        - `text: string`

        - `type: "text"`

          - `"text"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations?: Array<TextCitationParam> | null`

          - `CitationCharLocationParam`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_char_index: number`

            - `start_char_index: number`

            - `type: "char_location"`

              - `"char_location"`

          - `CitationPageLocationParam`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_page_number: number`

            - `start_page_number: number`

            - `type: "page_location"`

              - `"page_location"`

          - `CitationContentBlockLocationParam`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_block_index: number`

            - `start_block_index: number`

            - `type: "content_block_location"`

              - `"content_block_location"`

          - `CitationWebSearchResultLocationParam`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string | null`

            - `type: "web_search_result_location"`

              - `"web_search_result_location"`

            - `url: string`

          - `CitationSearchResultLocationParam`

            - `cited_text: string`

            - `end_block_index: number`

            - `search_result_index: number`

            - `source: string`

            - `start_block_index: number`

            - `title: string | null`

            - `type: "search_result_location"`

              - `"search_result_location"`

      - `ImageBlockParam`

        - `source: Base64ImageSource | URLImageSource`

          - `Base64ImageSource`

            - `data: string`

            - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

              - `"image/jpeg"`

              - `"image/png"`

              - `"image/gif"`

              - `"image/webp"`

            - `type: "base64"`

              - `"base64"`

          - `URLImageSource`

            - `type: "url"`

              - `"url"`

            - `url: string`

        - `type: "image"`

          - `"image"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

  - `type: "content"`

    - `"content"`

### Content Block Source Content

- `ContentBlockSourceContent = TextBlockParam | ImageBlockParam`

  - `TextBlockParam`

    - `text: string`

    - `type: "text"`

      - `"text"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations?: Array<TextCitationParam> | null`

      - `CitationCharLocationParam`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_char_index: number`

        - `start_char_index: number`

        - `type: "char_location"`

          - `"char_location"`

      - `CitationPageLocationParam`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_page_number: number`

        - `start_page_number: number`

        - `type: "page_location"`

          - `"page_location"`

      - `CitationContentBlockLocationParam`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_block_index: number`

        - `start_block_index: number`

        - `type: "content_block_location"`

          - `"content_block_location"`

      - `CitationWebSearchResultLocationParam`

        - `cited_text: string`

        - `encrypted_index: string`

        - `title: string | null`

        - `type: "web_search_result_location"`

          - `"web_search_result_location"`

        - `url: string`

      - `CitationSearchResultLocationParam`

        - `cited_text: string`

        - `end_block_index: number`

        - `search_result_index: number`

        - `source: string`

        - `start_block_index: number`

        - `title: string | null`

        - `type: "search_result_location"`

          - `"search_result_location"`

  - `ImageBlockParam`

    - `source: Base64ImageSource | URLImageSource`

      - `Base64ImageSource`

        - `data: string`

        - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

          - `"image/jpeg"`

          - `"image/png"`

          - `"image/gif"`

          - `"image/webp"`

        - `type: "base64"`

          - `"base64"`

      - `URLImageSource`

        - `type: "url"`

          - `"url"`

        - `url: string`

    - `type: "image"`

      - `"image"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

### Direct Caller

- `DirectCaller`

  Tool invocation directly from the model.

  - `type: "direct"`

    - `"direct"`

### Document Block

- `DocumentBlock`

  - `citations: CitationsConfig | null`

    Citation configuration for the document

    - `enabled: boolean`

  - `source: Base64PDFSource | PlainTextSource`

    - `Base64PDFSource`

      - `data: string`

      - `media_type: "application/pdf"`

        - `"application/pdf"`

      - `type: "base64"`

        - `"base64"`

    - `PlainTextSource`

      - `data: string`

      - `media_type: "text/plain"`

        - `"text/plain"`

      - `type: "text"`

        - `"text"`

  - `title: string | null`

    The title of the document

  - `type: "document"`

    - `"document"`

### Document Block Param

- `DocumentBlockParam`

  - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

    - `Base64PDFSource`

      - `data: string`

      - `media_type: "application/pdf"`

        - `"application/pdf"`

      - `type: "base64"`

        - `"base64"`

    - `PlainTextSource`

      - `data: string`

      - `media_type: "text/plain"`

        - `"text/plain"`

      - `type: "text"`

        - `"text"`

    - `ContentBlockSource`

      - `content: string | Array<ContentBlockSourceContent>`

        - `string`

        - `Array<ContentBlockSourceContent>`

          - `TextBlockParam`

            - `text: string`

            - `type: "text"`

              - `"text"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `citations?: Array<TextCitationParam> | null`

              - `CitationCharLocationParam`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_char_index: number`

                - `start_char_index: number`

                - `type: "char_location"`

                  - `"char_location"`

              - `CitationPageLocationParam`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_page_number: number`

                - `start_page_number: number`

                - `type: "page_location"`

                  - `"page_location"`

              - `CitationContentBlockLocationParam`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_block_index: number`

                - `start_block_index: number`

                - `type: "content_block_location"`

                  - `"content_block_location"`

              - `CitationWebSearchResultLocationParam`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string | null`

                - `type: "web_search_result_location"`

                  - `"web_search_result_location"`

                - `url: string`

              - `CitationSearchResultLocationParam`

                - `cited_text: string`

                - `end_block_index: number`

                - `search_result_index: number`

                - `source: string`

                - `start_block_index: number`

                - `title: string | null`

                - `type: "search_result_location"`

                  - `"search_result_location"`

          - `ImageBlockParam`

            - `source: Base64ImageSource | URLImageSource`

              - `Base64ImageSource`

                - `data: string`

                - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                  - `"image/jpeg"`

                  - `"image/png"`

                  - `"image/gif"`

                  - `"image/webp"`

                - `type: "base64"`

                  - `"base64"`

              - `URLImageSource`

                - `type: "url"`

                  - `"url"`

                - `url: string`

            - `type: "image"`

              - `"image"`

            - `cache_control?: CacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

                - `"ephemeral"`

              - `ttl?: "5m" | "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

      - `type: "content"`

        - `"content"`

    - `URLPDFSource`

      - `type: "url"`

        - `"url"`

      - `url: string`

  - `type: "document"`

    - `"document"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `citations?: CitationsConfigParam | null`

    - `enabled?: boolean`

  - `context?: string | null`

  - `title?: string | null`

### Encrypted Code Execution Result Block

- `EncryptedCodeExecutionResultBlock`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `content: Array<CodeExecutionOutputBlock>`

    - `file_id: string`

    - `type: "code_execution_output"`

      - `"code_execution_output"`

  - `encrypted_stdout: string`

  - `return_code: number`

  - `stderr: string`

  - `type: "encrypted_code_execution_result"`

    - `"encrypted_code_execution_result"`

### Encrypted Code Execution Result Block Param

- `EncryptedCodeExecutionResultBlockParam`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `content: Array<CodeExecutionOutputBlockParam>`

    - `file_id: string`

    - `type: "code_execution_output"`

      - `"code_execution_output"`

  - `encrypted_stdout: string`

  - `return_code: number`

  - `stderr: string`

  - `type: "encrypted_code_execution_result"`

    - `"encrypted_code_execution_result"`

### Image Block Param

- `ImageBlockParam`

  - `source: Base64ImageSource | URLImageSource`

    - `Base64ImageSource`

      - `data: string`

      - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

        - `"image/jpeg"`

        - `"image/png"`

        - `"image/gif"`

        - `"image/webp"`

      - `type: "base64"`

        - `"base64"`

    - `URLImageSource`

      - `type: "url"`

        - `"url"`

      - `url: string`

  - `type: "image"`

    - `"image"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Input JSON Delta

- `InputJSONDelta`

  - `partial_json: string`

  - `type: "input_json_delta"`

    - `"input_json_delta"`

### JSON Output Format

- `JSONOutputFormat`

  - `schema: Record<string, unknown>`

    The JSON schema of the format

  - `type: "json_schema"`

    - `"json_schema"`

### Memory Tool 20250818

- `MemoryTool20250818`

  - `name: "memory"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"memory"`

  - `type: "memory_20250818"`

    - `"memory_20250818"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples?: Array<Record<string, unknown>>`

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

### Message

- `Message`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `container: Container | null`

    Information about the container used in the request (for the code execution tool)

    - `id: string`

      Identifier for the container used in this request

    - `expires_at: string`

      The time at which the container will expire.

  - `content: Array<ContentBlock>`

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

    - `TextBlock`

      - `citations: Array<TextCitation> | null`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `CitationCharLocation`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_char_index: number`

          - `file_id: string | null`

          - `start_char_index: number`

          - `type: "char_location"`

            - `"char_location"`

        - `CitationPageLocation`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_page_number: number`

          - `file_id: string | null`

          - `start_page_number: number`

          - `type: "page_location"`

            - `"page_location"`

        - `CitationContentBlockLocation`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_block_index: number`

          - `file_id: string | null`

          - `start_block_index: number`

          - `type: "content_block_location"`

            - `"content_block_location"`

        - `CitationsWebSearchResultLocation`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string | null`

          - `type: "web_search_result_location"`

            - `"web_search_result_location"`

          - `url: string`

        - `CitationsSearchResultLocation`

          - `cited_text: string`

          - `end_block_index: number`

          - `search_result_index: number`

          - `source: string`

          - `start_block_index: number`

          - `title: string | null`

          - `type: "search_result_location"`

            - `"search_result_location"`

      - `text: string`

      - `type: "text"`

        - `"text"`

    - `ThinkingBlock`

      - `signature: string`

      - `thinking: string`

      - `type: "thinking"`

        - `"thinking"`

    - `RedactedThinkingBlock`

      - `data: string`

      - `type: "redacted_thinking"`

        - `"redacted_thinking"`

    - `ToolUseBlock`

      - `id: string`

      - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `DirectCaller`

          Tool invocation directly from the model.

          - `type: "direct"`

            - `"direct"`

        - `ServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

            - `"code_execution_20250825"`

        - `ServerToolCaller20260120`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

            - `"code_execution_20260120"`

      - `input: Record<string, unknown>`

      - `name: string`

      - `type: "tool_use"`

        - `"tool_use"`

    - `ServerToolUseBlock`

      - `id: string`

      - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `DirectCaller`

          Tool invocation directly from the model.

          - `type: "direct"`

            - `"direct"`

        - `ServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

            - `"code_execution_20250825"`

        - `ServerToolCaller20260120`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

            - `"code_execution_20260120"`

      - `input: Record<string, unknown>`

      - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

        - `"web_search"`

        - `"web_fetch"`

        - `"code_execution"`

        - `"bash_code_execution"`

        - `"text_editor_code_execution"`

        - `"tool_search_tool_regex"`

        - `"tool_search_tool_bm25"`

      - `type: "server_tool_use"`

        - `"server_tool_use"`

    - `WebSearchToolResultBlock`

      - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `DirectCaller`

          Tool invocation directly from the model.

          - `type: "direct"`

            - `"direct"`

        - `ServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

            - `"code_execution_20250825"`

        - `ServerToolCaller20260120`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

            - `"code_execution_20260120"`

      - `content: WebSearchToolResultBlockContent`

        - `WebSearchToolResultError`

          - `error_code: WebSearchToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"max_uses_exceeded"`

            - `"too_many_requests"`

            - `"query_too_long"`

            - `"request_too_large"`

          - `type: "web_search_tool_result_error"`

            - `"web_search_tool_result_error"`

        - `Array<WebSearchResultBlock>`

          - `encrypted_content: string`

          - `page_age: string | null`

          - `title: string`

          - `type: "web_search_result"`

            - `"web_search_result"`

          - `url: string`

      - `tool_use_id: string`

      - `type: "web_search_tool_result"`

        - `"web_search_tool_result"`

    - `WebFetchToolResultBlock`

      - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `DirectCaller`

          Tool invocation directly from the model.

          - `type: "direct"`

            - `"direct"`

        - `ServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

            - `"code_execution_20250825"`

        - `ServerToolCaller20260120`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

            - `"code_execution_20260120"`

      - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

        - `WebFetchToolResultErrorBlock`

          - `error_code: WebFetchToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"url_too_long"`

            - `"url_not_allowed"`

            - `"url_not_accessible"`

            - `"unsupported_content_type"`

            - `"too_many_requests"`

            - `"max_uses_exceeded"`

            - `"unavailable"`

          - `type: "web_fetch_tool_result_error"`

            - `"web_fetch_tool_result_error"`

        - `WebFetchBlock`

          - `content: DocumentBlock`

            - `citations: CitationsConfig | null`

              Citation configuration for the document

              - `enabled: boolean`

            - `source: Base64PDFSource | PlainTextSource`

              - `Base64PDFSource`

                - `data: string`

                - `media_type: "application/pdf"`

                  - `"application/pdf"`

                - `type: "base64"`

                  - `"base64"`

              - `PlainTextSource`

                - `data: string`

                - `media_type: "text/plain"`

                  - `"text/plain"`

                - `type: "text"`

                  - `"text"`

            - `title: string | null`

              The title of the document

            - `type: "document"`

              - `"document"`

          - `retrieved_at: string | null`

            ISO 8601 timestamp when the content was retrieved

          - `type: "web_fetch_result"`

            - `"web_fetch_result"`

          - `url: string`

            Fetched content URL

      - `tool_use_id: string`

      - `type: "web_fetch_tool_result"`

        - `"web_fetch_tool_result"`

    - `CodeExecutionToolResultBlock`

      - `content: CodeExecutionToolResultBlockContent`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `CodeExecutionToolResultError`

          - `error_code: CodeExecutionToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `type: "code_execution_tool_result_error"`

            - `"code_execution_tool_result_error"`

        - `CodeExecutionResultBlock`

          - `content: Array<CodeExecutionOutputBlock>`

            - `file_id: string`

            - `type: "code_execution_output"`

              - `"code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "code_execution_result"`

            - `"code_execution_result"`

        - `EncryptedCodeExecutionResultBlock`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `content: Array<CodeExecutionOutputBlock>`

            - `file_id: string`

            - `type: "code_execution_output"`

              - `"code_execution_output"`

          - `encrypted_stdout: string`

          - `return_code: number`

          - `stderr: string`

          - `type: "encrypted_code_execution_result"`

            - `"encrypted_code_execution_result"`

      - `tool_use_id: string`

      - `type: "code_execution_tool_result"`

        - `"code_execution_tool_result"`

    - `BashCodeExecutionToolResultBlock`

      - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

        - `BashCodeExecutionToolResultError`

          - `error_code: BashCodeExecutionToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"output_file_too_large"`

          - `type: "bash_code_execution_tool_result_error"`

            - `"bash_code_execution_tool_result_error"`

        - `BashCodeExecutionResultBlock`

          - `content: Array<BashCodeExecutionOutputBlock>`

            - `file_id: string`

            - `type: "bash_code_execution_output"`

              - `"bash_code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "bash_code_execution_result"`

            - `"bash_code_execution_result"`

      - `tool_use_id: string`

      - `type: "bash_code_execution_tool_result"`

        - `"bash_code_execution_tool_result"`

    - `TextEditorCodeExecutionToolResultBlock`

      - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

        - `TextEditorCodeExecutionToolResultError`

          - `error_code: TextEditorCodeExecutionToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"file_not_found"`

          - `error_message: string | null`

          - `type: "text_editor_code_execution_tool_result_error"`

            - `"text_editor_code_execution_tool_result_error"`

        - `TextEditorCodeExecutionViewResultBlock`

          - `content: string`

          - `file_type: "text" | "image" | "pdf"`

            - `"text"`

            - `"image"`

            - `"pdf"`

          - `num_lines: number | null`

          - `start_line: number | null`

          - `total_lines: number | null`

          - `type: "text_editor_code_execution_view_result"`

            - `"text_editor_code_execution_view_result"`

        - `TextEditorCodeExecutionCreateResultBlock`

          - `is_file_update: boolean`

          - `type: "text_editor_code_execution_create_result"`

            - `"text_editor_code_execution_create_result"`

        - `TextEditorCodeExecutionStrReplaceResultBlock`

          - `lines: Array<string> | null`

          - `new_lines: number | null`

          - `new_start: number | null`

          - `old_lines: number | null`

          - `old_start: number | null`

          - `type: "text_editor_code_execution_str_replace_result"`

            - `"text_editor_code_execution_str_replace_result"`

      - `tool_use_id: string`

      - `type: "text_editor_code_execution_tool_result"`

        - `"text_editor_code_execution_tool_result"`

    - `ToolSearchToolResultBlock`

      - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

        - `ToolSearchToolResultError`

          - `error_code: ToolSearchToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `error_message: string | null`

          - `type: "tool_search_tool_result_error"`

            - `"tool_search_tool_result_error"`

        - `ToolSearchToolSearchResultBlock`

          - `tool_references: Array<ToolReferenceBlock>`

            - `tool_name: string`

            - `type: "tool_reference"`

              - `"tool_reference"`

          - `type: "tool_search_tool_search_result"`

            - `"tool_search_tool_search_result"`

      - `tool_use_id: string`

      - `type: "tool_search_tool_result"`

        - `"tool_search_tool_result"`

    - `ContainerUploadBlock`

      Response model for a file uploaded to the container.

      - `file_id: string`

      - `type: "container_upload"`

        - `"container_upload"`

  - `model: Model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-opus-4-5-20251101" | 19 more`

      - `"claude-opus-4-6"`

        Most intelligent model for building agents and coding

      - `"claude-sonnet-4-6"`

        Frontier intelligence at scale — built for coding, agents, and enterprise workflows

      - `"claude-opus-4-5-20251101"`

        Premium model combining maximum intelligence with practical performance

      - `"claude-opus-4-5"`

        Premium model combining maximum intelligence with practical performance

      - `"claude-3-7-sonnet-latest"`

        High-performance model with early extended thinking

      - `"claude-3-7-sonnet-20250219"`

        High-performance model with early extended thinking

      - `"claude-3-5-haiku-latest"`

        Fastest and most compact model for near-instant responsiveness

      - `"claude-3-5-haiku-20241022"`

        Our fastest model

      - `"claude-haiku-4-5"`

        Hybrid model, capable of near-instant responses and extended thinking

      - `"claude-haiku-4-5-20251001"`

        Hybrid model, capable of near-instant responses and extended thinking

      - `"claude-sonnet-4-20250514"`

        High-performance model with extended thinking

      - `"claude-sonnet-4-0"`

        High-performance model with extended thinking

      - `"claude-4-sonnet-20250514"`

        High-performance model with extended thinking

      - `"claude-sonnet-4-5"`

        Our best model for real-world agents and coding

      - `"claude-sonnet-4-5-20250929"`

        Our best model for real-world agents and coding

      - `"claude-opus-4-0"`

        Our most capable model

      - `"claude-opus-4-20250514"`

        Our most capable model

      - `"claude-4-opus-20250514"`

        Our most capable model

      - `"claude-opus-4-1-20250805"`

        Our most capable model

      - `"claude-3-opus-latest"`

        Excels at writing and complex tasks

      - `"claude-3-opus-20240229"`

        Excels at writing and complex tasks

      - `"claude-3-haiku-20240307"`

        Our previous most fast and cost-effective

    - `(string & {})`

  - `role: "assistant"`

    Conversational role of the generated message.

    This will always be `"assistant"`.

    - `"assistant"`

  - `stop_reason: StopReason | null`

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

    - `"refusal"`

  - `stop_sequence: string | null`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `type: "message"`

    Object type.

    For Messages, this is always `"message"`.

    - `"message"`

  - `usage: Usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `cache_creation: CacheCreation | null`

      Breakdown of cached tokens by TTL

      - `ephemeral_1h_input_tokens: number`

        The number of input tokens used to create the 1 hour cache entry.

      - `ephemeral_5m_input_tokens: number`

        The number of input tokens used to create the 5 minute cache entry.

    - `cache_creation_input_tokens: number | null`

      The number of input tokens used to create the cache entry.

    - `cache_read_input_tokens: number | null`

      The number of input tokens read from the cache.

    - `inference_geo: string | null`

      The geographic region where inference was performed for this request.

    - `input_tokens: number`

      The number of input tokens which were used.

    - `output_tokens: number`

      The number of output tokens which were used.

    - `server_tool_use: ServerToolUsage | null`

      The number of server tool requests.

      - `web_fetch_requests: number`

        The number of web fetch tool requests.

      - `web_search_requests: number`

        The number of web search tool requests.

    - `service_tier: "standard" | "priority" | "batch" | null`

      If the request used the priority, standard, or batch tier.

      - `"standard"`

      - `"priority"`

      - `"batch"`

### Message Count Tokens Tool

- `MessageCountTokensTool = Tool | ToolBash20250124 | CodeExecutionTool20250522 | 12 more`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `Tool`

    - `input_schema: InputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

      - `type: "object"`

        - `"object"`

      - `properties?: Record<string, unknown> | null`

      - `required?: Array<string> | null`

    - `name: string`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `description?: string`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `eager_input_streaming?: boolean | null`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `input_examples?: Array<Record<string, unknown>>`

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

    - `type?: "custom" | null`

      - `"custom"`

  - `ToolBash20250124`

    - `name: "bash"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"bash"`

    - `type: "bash_20250124"`

      - `"bash_20250124"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples?: Array<Record<string, unknown>>`

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250522`

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"code_execution"`

    - `type: "code_execution_20250522"`

      - `"code_execution_20250522"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250825`

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"code_execution"`

    - `type: "code_execution_20250825"`

      - `"code_execution_20250825"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20260120`

    Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"code_execution"`

    - `type: "code_execution_20260120"`

      - `"code_execution_20260120"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `MemoryTool20250818`

    - `name: "memory"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"memory"`

    - `type: "memory_20250818"`

      - `"memory_20250818"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples?: Array<Record<string, unknown>>`

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250124`

    - `name: "str_replace_editor"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"str_replace_editor"`

    - `type: "text_editor_20250124"`

      - `"text_editor_20250124"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples?: Array<Record<string, unknown>>`

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250429`

    - `name: "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"str_replace_based_edit_tool"`

    - `type: "text_editor_20250429"`

      - `"text_editor_20250429"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples?: Array<Record<string, unknown>>`

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250728`

    - `name: "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"str_replace_based_edit_tool"`

    - `type: "text_editor_20250728"`

      - `"text_editor_20250728"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples?: Array<Record<string, unknown>>`

    - `max_characters?: number | null`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20250305`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_search"`

    - `type: "web_search_20250305"`

      - `"web_search_20250305"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains?: Array<string> | null`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains?: Array<string> | null`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses?: number | null`

      Maximum number of times the tool can be used in the API request.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location?: UserLocation | null`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: "approximate"`

        - `"approximate"`

      - `city?: string | null`

        The city of the user.

      - `country?: string | null`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      - `region?: string | null`

        The region of the user.

      - `timezone?: string | null`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

  - `WebFetchTool20250910`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_fetch"`

    - `type: "web_fetch_20250910"`

      - `"web_fetch_20250910"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains?: Array<string> | null`

      List of domains to allow fetching from

    - `blocked_domains?: Array<string> | null`

      List of domains to block fetching from

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations?: CitationsConfigParam | null`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled?: boolean`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens?: number | null`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `max_uses?: number | null`

      Maximum number of times the tool can be used in the API request.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20260209`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_search"`

    - `type: "web_search_20260209"`

      - `"web_search_20260209"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains?: Array<string> | null`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains?: Array<string> | null`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses?: number | null`

      Maximum number of times the tool can be used in the API request.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location?: UserLocation | null`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: "approximate"`

        - `"approximate"`

      - `city?: string | null`

        The city of the user.

      - `country?: string | null`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      - `region?: string | null`

        The region of the user.

      - `timezone?: string | null`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

  - `WebFetchTool20260209`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_fetch"`

    - `type: "web_fetch_20260209"`

      - `"web_fetch_20260209"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains?: Array<string> | null`

      List of domains to allow fetching from

    - `blocked_domains?: Array<string> | null`

      List of domains to block fetching from

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations?: CitationsConfigParam | null`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled?: boolean`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens?: number | null`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `max_uses?: number | null`

      Maximum number of times the tool can be used in the API request.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ToolSearchToolBm25_20251119`

    - `name: "tool_search_tool_bm25"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"tool_search_tool_bm25"`

    - `type: "tool_search_tool_bm25_20251119" | "tool_search_tool_bm25"`

      - `"tool_search_tool_bm25_20251119"`

      - `"tool_search_tool_bm25"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ToolSearchToolRegex20251119`

    - `name: "tool_search_tool_regex"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"tool_search_tool_regex"`

    - `type: "tool_search_tool_regex_20251119" | "tool_search_tool_regex"`

      - `"tool_search_tool_regex_20251119"`

      - `"tool_search_tool_regex"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

### Message Delta Usage

- `MessageDeltaUsage`

  - `cache_creation_input_tokens: number | null`

    The cumulative number of input tokens used to create the cache entry.

  - `cache_read_input_tokens: number | null`

    The cumulative number of input tokens read from the cache.

  - `input_tokens: number | null`

    The cumulative number of input tokens which were used.

  - `output_tokens: number`

    The cumulative number of output tokens which were used.

  - `server_tool_use: ServerToolUsage | null`

    The number of server tool requests.

    - `web_fetch_requests: number`

      The number of web fetch tool requests.

    - `web_search_requests: number`

      The number of web search tool requests.

### Message Param

- `MessageParam`

  - `content: string | Array<ContentBlockParam>`

    - `string`

    - `Array<ContentBlockParam>`

      - `TextBlockParam`

        - `text: string`

        - `type: "text"`

          - `"text"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations?: Array<TextCitationParam> | null`

          - `CitationCharLocationParam`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_char_index: number`

            - `start_char_index: number`

            - `type: "char_location"`

              - `"char_location"`

          - `CitationPageLocationParam`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_page_number: number`

            - `start_page_number: number`

            - `type: "page_location"`

              - `"page_location"`

          - `CitationContentBlockLocationParam`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_block_index: number`

            - `start_block_index: number`

            - `type: "content_block_location"`

              - `"content_block_location"`

          - `CitationWebSearchResultLocationParam`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string | null`

            - `type: "web_search_result_location"`

              - `"web_search_result_location"`

            - `url: string`

          - `CitationSearchResultLocationParam`

            - `cited_text: string`

            - `end_block_index: number`

            - `search_result_index: number`

            - `source: string`

            - `start_block_index: number`

            - `title: string | null`

            - `type: "search_result_location"`

              - `"search_result_location"`

      - `ImageBlockParam`

        - `source: Base64ImageSource | URLImageSource`

          - `Base64ImageSource`

            - `data: string`

            - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

              - `"image/jpeg"`

              - `"image/png"`

              - `"image/gif"`

              - `"image/webp"`

            - `type: "base64"`

              - `"base64"`

          - `URLImageSource`

            - `type: "url"`

              - `"url"`

            - `url: string`

        - `type: "image"`

          - `"image"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `DocumentBlockParam`

        - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

          - `Base64PDFSource`

            - `data: string`

            - `media_type: "application/pdf"`

              - `"application/pdf"`

            - `type: "base64"`

              - `"base64"`

          - `PlainTextSource`

            - `data: string`

            - `media_type: "text/plain"`

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `ContentBlockSource`

            - `content: string | Array<ContentBlockSourceContent>`

              - `string`

              - `Array<ContentBlockSourceContent>`

                - `TextBlockParam`

                  - `text: string`

                  - `type: "text"`

                    - `"text"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

                  - `citations?: Array<TextCitationParam> | null`

                    - `CitationCharLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_char_index: number`

                      - `start_char_index: number`

                      - `type: "char_location"`

                        - `"char_location"`

                    - `CitationPageLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_page_number: number`

                      - `start_page_number: number`

                      - `type: "page_location"`

                        - `"page_location"`

                    - `CitationContentBlockLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_block_index: number`

                      - `start_block_index: number`

                      - `type: "content_block_location"`

                        - `"content_block_location"`

                    - `CitationWebSearchResultLocationParam`

                      - `cited_text: string`

                      - `encrypted_index: string`

                      - `title: string | null`

                      - `type: "web_search_result_location"`

                        - `"web_search_result_location"`

                      - `url: string`

                    - `CitationSearchResultLocationParam`

                      - `cited_text: string`

                      - `end_block_index: number`

                      - `search_result_index: number`

                      - `source: string`

                      - `start_block_index: number`

                      - `title: string | null`

                      - `type: "search_result_location"`

                        - `"search_result_location"`

                - `ImageBlockParam`

                  - `source: Base64ImageSource | URLImageSource`

                    - `Base64ImageSource`

                      - `data: string`

                      - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                        - `"image/jpeg"`

                        - `"image/png"`

                        - `"image/gif"`

                        - `"image/webp"`

                      - `type: "base64"`

                        - `"base64"`

                    - `URLImageSource`

                      - `type: "url"`

                        - `"url"`

                      - `url: string`

                  - `type: "image"`

                    - `"image"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

            - `type: "content"`

              - `"content"`

          - `URLPDFSource`

            - `type: "url"`

              - `"url"`

            - `url: string`

        - `type: "document"`

          - `"document"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations?: CitationsConfigParam | null`

          - `enabled?: boolean`

        - `context?: string | null`

        - `title?: string | null`

      - `SearchResultBlockParam`

        - `content: Array<TextBlockParam>`

          - `text: string`

          - `type: "text"`

            - `"text"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations?: Array<TextCitationParam> | null`

            - `CitationCharLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_char_index: number`

              - `start_char_index: number`

              - `type: "char_location"`

                - `"char_location"`

            - `CitationPageLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_page_number: number`

              - `start_page_number: number`

              - `type: "page_location"`

                - `"page_location"`

            - `CitationContentBlockLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_block_index: number`

              - `start_block_index: number`

              - `type: "content_block_location"`

                - `"content_block_location"`

            - `CitationWebSearchResultLocationParam`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string | null`

              - `type: "web_search_result_location"`

                - `"web_search_result_location"`

              - `url: string`

            - `CitationSearchResultLocationParam`

              - `cited_text: string`

              - `end_block_index: number`

              - `search_result_index: number`

              - `source: string`

              - `start_block_index: number`

              - `title: string | null`

              - `type: "search_result_location"`

                - `"search_result_location"`

        - `source: string`

        - `title: string`

        - `type: "search_result"`

          - `"search_result"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations?: CitationsConfigParam`

          - `enabled?: boolean`

      - `ThinkingBlockParam`

        - `signature: string`

        - `thinking: string`

        - `type: "thinking"`

          - `"thinking"`

      - `RedactedThinkingBlockParam`

        - `data: string`

        - `type: "redacted_thinking"`

          - `"redacted_thinking"`

      - `ToolUseBlockParam`

        - `id: string`

        - `input: Record<string, unknown>`

        - `name: string`

        - `type: "tool_use"`

          - `"tool_use"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

      - `ToolResultBlockParam`

        - `tool_use_id: string`

        - `type: "tool_result"`

          - `"tool_result"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `content?: string | Array<TextBlockParam | ImageBlockParam | SearchResultBlockParam | 2 more>`

          - `string`

          - `Array<TextBlockParam | ImageBlockParam | SearchResultBlockParam | 2 more>`

            - `TextBlockParam`

              - `text: string`

              - `type: "text"`

                - `"text"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations?: Array<TextCitationParam> | null`

                - `CitationCharLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_char_index: number`

                  - `start_char_index: number`

                  - `type: "char_location"`

                    - `"char_location"`

                - `CitationPageLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_page_number: number`

                  - `start_page_number: number`

                  - `type: "page_location"`

                    - `"page_location"`

                - `CitationContentBlockLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_block_index: number`

                  - `start_block_index: number`

                  - `type: "content_block_location"`

                    - `"content_block_location"`

                - `CitationWebSearchResultLocationParam`

                  - `cited_text: string`

                  - `encrypted_index: string`

                  - `title: string | null`

                  - `type: "web_search_result_location"`

                    - `"web_search_result_location"`

                  - `url: string`

                - `CitationSearchResultLocationParam`

                  - `cited_text: string`

                  - `end_block_index: number`

                  - `search_result_index: number`

                  - `source: string`

                  - `start_block_index: number`

                  - `title: string | null`

                  - `type: "search_result_location"`

                    - `"search_result_location"`

            - `ImageBlockParam`

              - `source: Base64ImageSource | URLImageSource`

                - `Base64ImageSource`

                  - `data: string`

                  - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                    - `"image/jpeg"`

                    - `"image/png"`

                    - `"image/gif"`

                    - `"image/webp"`

                  - `type: "base64"`

                    - `"base64"`

                - `URLImageSource`

                  - `type: "url"`

                    - `"url"`

                  - `url: string`

              - `type: "image"`

                - `"image"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

            - `SearchResultBlockParam`

              - `content: Array<TextBlockParam>`

                - `text: string`

                - `type: "text"`

                  - `"text"`

                - `cache_control?: CacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

                  - `type: "ephemeral"`

                    - `"ephemeral"`

                  - `ttl?: "5m" | "1h"`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

                - `citations?: Array<TextCitationParam> | null`

                  - `CitationCharLocationParam`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string | null`

                    - `end_char_index: number`

                    - `start_char_index: number`

                    - `type: "char_location"`

                      - `"char_location"`

                  - `CitationPageLocationParam`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string | null`

                    - `end_page_number: number`

                    - `start_page_number: number`

                    - `type: "page_location"`

                      - `"page_location"`

                  - `CitationContentBlockLocationParam`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string | null`

                    - `end_block_index: number`

                    - `start_block_index: number`

                    - `type: "content_block_location"`

                      - `"content_block_location"`

                  - `CitationWebSearchResultLocationParam`

                    - `cited_text: string`

                    - `encrypted_index: string`

                    - `title: string | null`

                    - `type: "web_search_result_location"`

                      - `"web_search_result_location"`

                    - `url: string`

                  - `CitationSearchResultLocationParam`

                    - `cited_text: string`

                    - `end_block_index: number`

                    - `search_result_index: number`

                    - `source: string`

                    - `start_block_index: number`

                    - `title: string | null`

                    - `type: "search_result_location"`

                      - `"search_result_location"`

              - `source: string`

              - `title: string`

              - `type: "search_result"`

                - `"search_result"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations?: CitationsConfigParam`

                - `enabled?: boolean`

            - `DocumentBlockParam`

              - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

                - `Base64PDFSource`

                  - `data: string`

                  - `media_type: "application/pdf"`

                    - `"application/pdf"`

                  - `type: "base64"`

                    - `"base64"`

                - `PlainTextSource`

                  - `data: string`

                  - `media_type: "text/plain"`

                    - `"text/plain"`

                  - `type: "text"`

                    - `"text"`

                - `ContentBlockSource`

                  - `content: string | Array<ContentBlockSourceContent>`

                    - `string`

                    - `Array<ContentBlockSourceContent>`

                      - `TextBlockParam`

                        - `text: string`

                        - `type: "text"`

                          - `"text"`

                        - `cache_control?: CacheControlEphemeral | null`

                          Create a cache control breakpoint at this content block.

                          - `type: "ephemeral"`

                            - `"ephemeral"`

                          - `ttl?: "5m" | "1h"`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `"5m"`

                            - `"1h"`

                        - `citations?: Array<TextCitationParam> | null`

                          - `CitationCharLocationParam`

                            - `cited_text: string`

                            - `document_index: number`

                            - `document_title: string | null`

                            - `end_char_index: number`

                            - `start_char_index: number`

                            - `type: "char_location"`

                              - `"char_location"`

                          - `CitationPageLocationParam`

                            - `cited_text: string`

                            - `document_index: number`

                            - `document_title: string | null`

                            - `end_page_number: number`

                            - `start_page_number: number`

                            - `type: "page_location"`

                              - `"page_location"`

                          - `CitationContentBlockLocationParam`

                            - `cited_text: string`

                            - `document_index: number`

                            - `document_title: string | null`

                            - `end_block_index: number`

                            - `start_block_index: number`

                            - `type: "content_block_location"`

                              - `"content_block_location"`

                          - `CitationWebSearchResultLocationParam`

                            - `cited_text: string`

                            - `encrypted_index: string`

                            - `title: string | null`

                            - `type: "web_search_result_location"`

                              - `"web_search_result_location"`

                            - `url: string`

                          - `CitationSearchResultLocationParam`

                            - `cited_text: string`

                            - `end_block_index: number`

                            - `search_result_index: number`

                            - `source: string`

                            - `start_block_index: number`

                            - `title: string | null`

                            - `type: "search_result_location"`

                              - `"search_result_location"`

                      - `ImageBlockParam`

                        - `source: Base64ImageSource | URLImageSource`

                          - `Base64ImageSource`

                            - `data: string`

                            - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                              - `"image/jpeg"`

                              - `"image/png"`

                              - `"image/gif"`

                              - `"image/webp"`

                            - `type: "base64"`

                              - `"base64"`

                          - `URLImageSource`

                            - `type: "url"`

                              - `"url"`

                            - `url: string`

                        - `type: "image"`

                          - `"image"`

                        - `cache_control?: CacheControlEphemeral | null`

                          Create a cache control breakpoint at this content block.

                          - `type: "ephemeral"`

                            - `"ephemeral"`

                          - `ttl?: "5m" | "1h"`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `"5m"`

                            - `"1h"`

                  - `type: "content"`

                    - `"content"`

                - `URLPDFSource`

                  - `type: "url"`

                    - `"url"`

                  - `url: string`

              - `type: "document"`

                - `"document"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations?: CitationsConfigParam | null`

                - `enabled?: boolean`

              - `context?: string | null`

              - `title?: string | null`

            - `ToolReferenceBlockParam`

              Tool reference block that can be included in tool_result content.

              - `tool_name: string`

              - `type: "tool_reference"`

                - `"tool_reference"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

        - `is_error?: boolean`

      - `ServerToolUseBlockParam`

        - `id: string`

        - `input: Record<string, unknown>`

        - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

          - `"web_search"`

          - `"web_fetch"`

          - `"code_execution"`

          - `"bash_code_execution"`

          - `"text_editor_code_execution"`

          - `"tool_search_tool_regex"`

          - `"tool_search_tool_bm25"`

        - `type: "server_tool_use"`

          - `"server_tool_use"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

      - `WebSearchToolResultBlockParam`

        - `content: WebSearchToolResultBlockParamContent`

          - `Array<WebSearchResultBlockParam>`

            - `encrypted_content: string`

            - `title: string`

            - `type: "web_search_result"`

              - `"web_search_result"`

            - `url: string`

            - `page_age?: string | null`

          - `WebSearchToolRequestError`

            - `error_code: WebSearchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"max_uses_exceeded"`

              - `"too_many_requests"`

              - `"query_too_long"`

              - `"request_too_large"`

            - `type: "web_search_tool_result_error"`

              - `"web_search_tool_result_error"`

        - `tool_use_id: string`

        - `type: "web_search_tool_result"`

          - `"web_search_tool_result"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

      - `WebFetchToolResultBlockParam`

        - `content: WebFetchToolResultErrorBlockParam | WebFetchBlockParam`

          - `WebFetchToolResultErrorBlockParam`

            - `error_code: WebFetchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"url_too_long"`

              - `"url_not_allowed"`

              - `"url_not_accessible"`

              - `"unsupported_content_type"`

              - `"too_many_requests"`

              - `"max_uses_exceeded"`

              - `"unavailable"`

            - `type: "web_fetch_tool_result_error"`

              - `"web_fetch_tool_result_error"`

          - `WebFetchBlockParam`

            - `content: DocumentBlockParam`

              - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

                - `Base64PDFSource`

                  - `data: string`

                  - `media_type: "application/pdf"`

                    - `"application/pdf"`

                  - `type: "base64"`

                    - `"base64"`

                - `PlainTextSource`

                  - `data: string`

                  - `media_type: "text/plain"`

                    - `"text/plain"`

                  - `type: "text"`

                    - `"text"`

                - `ContentBlockSource`

                  - `content: string | Array<ContentBlockSourceContent>`

                    - `string`

                    - `Array<ContentBlockSourceContent>`

                      - `TextBlockParam`

                        - `text: string`

                        - `type: "text"`

                          - `"text"`

                        - `cache_control?: CacheControlEphemeral | null`

                          Create a cache control breakpoint at this content block.

                          - `type: "ephemeral"`

                            - `"ephemeral"`

                          - `ttl?: "5m" | "1h"`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `"5m"`

                            - `"1h"`

                        - `citations?: Array<TextCitationParam> | null`

                          - `CitationCharLocationParam`

                            - `cited_text: string`

                            - `document_index: number`

                            - `document_title: string | null`

                            - `end_char_index: number`

                            - `start_char_index: number`

                            - `type: "char_location"`

                              - `"char_location"`

                          - `CitationPageLocationParam`

                            - `cited_text: string`

                            - `document_index: number`

                            - `document_title: string | null`

                            - `end_page_number: number`

                            - `start_page_number: number`

                            - `type: "page_location"`

                              - `"page_location"`

                          - `CitationContentBlockLocationParam`

                            - `cited_text: string`

                            - `document_index: number`

                            - `document_title: string | null`

                            - `end_block_index: number`

                            - `start_block_index: number`

                            - `type: "content_block_location"`

                              - `"content_block_location"`

                          - `CitationWebSearchResultLocationParam`

                            - `cited_text: string`

                            - `encrypted_index: string`

                            - `title: string | null`

                            - `type: "web_search_result_location"`

                              - `"web_search_result_location"`

                            - `url: string`

                          - `CitationSearchResultLocationParam`

                            - `cited_text: string`

                            - `end_block_index: number`

                            - `search_result_index: number`

                            - `source: string`

                            - `start_block_index: number`

                            - `title: string | null`

                            - `type: "search_result_location"`

                              - `"search_result_location"`

                      - `ImageBlockParam`

                        - `source: Base64ImageSource | URLImageSource`

                          - `Base64ImageSource`

                            - `data: string`

                            - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                              - `"image/jpeg"`

                              - `"image/png"`

                              - `"image/gif"`

                              - `"image/webp"`

                            - `type: "base64"`

                              - `"base64"`

                          - `URLImageSource`

                            - `type: "url"`

                              - `"url"`

                            - `url: string`

                        - `type: "image"`

                          - `"image"`

                        - `cache_control?: CacheControlEphemeral | null`

                          Create a cache control breakpoint at this content block.

                          - `type: "ephemeral"`

                            - `"ephemeral"`

                          - `ttl?: "5m" | "1h"`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `"5m"`

                            - `"1h"`

                  - `type: "content"`

                    - `"content"`

                - `URLPDFSource`

                  - `type: "url"`

                    - `"url"`

                  - `url: string`

              - `type: "document"`

                - `"document"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations?: CitationsConfigParam | null`

                - `enabled?: boolean`

              - `context?: string | null`

              - `title?: string | null`

            - `type: "web_fetch_result"`

              - `"web_fetch_result"`

            - `url: string`

              Fetched content URL

            - `retrieved_at?: string | null`

              ISO 8601 timestamp when the content was retrieved

        - `tool_use_id: string`

        - `type: "web_fetch_tool_result"`

          - `"web_fetch_tool_result"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

      - `CodeExecutionToolResultBlockParam`

        - `content: CodeExecutionToolResultBlockParamContent`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `CodeExecutionToolResultErrorParam`

            - `error_code: CodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `type: "code_execution_tool_result_error"`

              - `"code_execution_tool_result_error"`

          - `CodeExecutionResultBlockParam`

            - `content: Array<CodeExecutionOutputBlockParam>`

              - `file_id: string`

              - `type: "code_execution_output"`

                - `"code_execution_output"`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

            - `type: "code_execution_result"`

              - `"code_execution_result"`

          - `EncryptedCodeExecutionResultBlockParam`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `content: Array<CodeExecutionOutputBlockParam>`

              - `file_id: string`

              - `type: "code_execution_output"`

                - `"code_execution_output"`

            - `encrypted_stdout: string`

            - `return_code: number`

            - `stderr: string`

            - `type: "encrypted_code_execution_result"`

              - `"encrypted_code_execution_result"`

        - `tool_use_id: string`

        - `type: "code_execution_tool_result"`

          - `"code_execution_tool_result"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `BashCodeExecutionToolResultBlockParam`

        - `content: BashCodeExecutionToolResultErrorParam | BashCodeExecutionResultBlockParam`

          - `BashCodeExecutionToolResultErrorParam`

            - `error_code: BashCodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"output_file_too_large"`

            - `type: "bash_code_execution_tool_result_error"`

              - `"bash_code_execution_tool_result_error"`

          - `BashCodeExecutionResultBlockParam`

            - `content: Array<BashCodeExecutionOutputBlockParam>`

              - `file_id: string`

              - `type: "bash_code_execution_output"`

                - `"bash_code_execution_output"`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

            - `type: "bash_code_execution_result"`

              - `"bash_code_execution_result"`

        - `tool_use_id: string`

        - `type: "bash_code_execution_tool_result"`

          - `"bash_code_execution_tool_result"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `TextEditorCodeExecutionToolResultBlockParam`

        - `content: TextEditorCodeExecutionToolResultErrorParam | TextEditorCodeExecutionViewResultBlockParam | TextEditorCodeExecutionCreateResultBlockParam | TextEditorCodeExecutionStrReplaceResultBlockParam`

          - `TextEditorCodeExecutionToolResultErrorParam`

            - `error_code: TextEditorCodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"file_not_found"`

            - `type: "text_editor_code_execution_tool_result_error"`

              - `"text_editor_code_execution_tool_result_error"`

            - `error_message?: string | null`

          - `TextEditorCodeExecutionViewResultBlockParam`

            - `content: string`

            - `file_type: "text" | "image" | "pdf"`

              - `"text"`

              - `"image"`

              - `"pdf"`

            - `type: "text_editor_code_execution_view_result"`

              - `"text_editor_code_execution_view_result"`

            - `num_lines?: number | null`

            - `start_line?: number | null`

            - `total_lines?: number | null`

          - `TextEditorCodeExecutionCreateResultBlockParam`

            - `is_file_update: boolean`

            - `type: "text_editor_code_execution_create_result"`

              - `"text_editor_code_execution_create_result"`

          - `TextEditorCodeExecutionStrReplaceResultBlockParam`

            - `type: "text_editor_code_execution_str_replace_result"`

              - `"text_editor_code_execution_str_replace_result"`

            - `lines?: Array<string> | null`

            - `new_lines?: number | null`

            - `new_start?: number | null`

            - `old_lines?: number | null`

            - `old_start?: number | null`

        - `tool_use_id: string`

        - `type: "text_editor_code_execution_tool_result"`

          - `"text_editor_code_execution_tool_result"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `ToolSearchToolResultBlockParam`

        - `content: ToolSearchToolResultErrorParam | ToolSearchToolSearchResultBlockParam`

          - `ToolSearchToolResultErrorParam`

            - `error_code: ToolSearchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `type: "tool_search_tool_result_error"`

              - `"tool_search_tool_result_error"`

          - `ToolSearchToolSearchResultBlockParam`

            - `tool_references: Array<ToolReferenceBlockParam>`

              - `tool_name: string`

              - `type: "tool_reference"`

                - `"tool_reference"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

            - `type: "tool_search_tool_search_result"`

              - `"tool_search_tool_search_result"`

        - `tool_use_id: string`

        - `type: "tool_search_tool_result"`

          - `"tool_search_tool_result"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `ContainerUploadBlockParam`

        A content block that represents a file to be uploaded to the container
        Files uploaded via this block will be available in the container's input directory.

        - `file_id: string`

        - `type: "container_upload"`

          - `"container_upload"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

  - `role: "user" | "assistant"`

    - `"user"`

    - `"assistant"`

### Message Tokens Count

- `MessageTokensCount`

  - `input_tokens: number`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Metadata

- `Metadata`

  - `user_id?: string | null`

    An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

### Model

- `Model = "claude-opus-4-6" | "claude-sonnet-4-6" | "claude-opus-4-5-20251101" | 19 more | (string & {})`

  The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-opus-4-5-20251101" | 19 more`

    - `"claude-opus-4-6"`

      Most intelligent model for building agents and coding

    - `"claude-sonnet-4-6"`

      Frontier intelligence at scale — built for coding, agents, and enterprise workflows

    - `"claude-opus-4-5-20251101"`

      Premium model combining maximum intelligence with practical performance

    - `"claude-opus-4-5"`

      Premium model combining maximum intelligence with practical performance

    - `"claude-3-7-sonnet-latest"`

      High-performance model with early extended thinking

    - `"claude-3-7-sonnet-20250219"`

      High-performance model with early extended thinking

    - `"claude-3-5-haiku-latest"`

      Fastest and most compact model for near-instant responsiveness

    - `"claude-3-5-haiku-20241022"`

      Our fastest model

    - `"claude-haiku-4-5"`

      Hybrid model, capable of near-instant responses and extended thinking

    - `"claude-haiku-4-5-20251001"`

      Hybrid model, capable of near-instant responses and extended thinking

    - `"claude-sonnet-4-20250514"`

      High-performance model with extended thinking

    - `"claude-sonnet-4-0"`

      High-performance model with extended thinking

    - `"claude-4-sonnet-20250514"`

      High-performance model with extended thinking

    - `"claude-sonnet-4-5"`

      Our best model for real-world agents and coding

    - `"claude-sonnet-4-5-20250929"`

      Our best model for real-world agents and coding

    - `"claude-opus-4-0"`

      Our most capable model

    - `"claude-opus-4-20250514"`

      Our most capable model

    - `"claude-4-opus-20250514"`

      Our most capable model

    - `"claude-opus-4-1-20250805"`

      Our most capable model

    - `"claude-3-opus-latest"`

      Excels at writing and complex tasks

    - `"claude-3-opus-20240229"`

      Excels at writing and complex tasks

    - `"claude-3-haiku-20240307"`

      Our previous most fast and cost-effective

  - `(string & {})`

### Output Config

- `OutputConfig`

  - `effort?: "low" | "medium" | "high" | "max" | null`

    All possible effort levels.

    - `"low"`

    - `"medium"`

    - `"high"`

    - `"max"`

  - `format?: JSONOutputFormat | null`

    A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

    - `schema: Record<string, unknown>`

      The JSON schema of the format

    - `type: "json_schema"`

      - `"json_schema"`

### Plain Text Source

- `PlainTextSource`

  - `data: string`

  - `media_type: "text/plain"`

    - `"text/plain"`

  - `type: "text"`

    - `"text"`

### Raw Content Block Delta

- `RawContentBlockDelta = TextDelta | InputJSONDelta | CitationsDelta | 2 more`

  - `TextDelta`

    - `text: string`

    - `type: "text_delta"`

      - `"text_delta"`

  - `InputJSONDelta`

    - `partial_json: string`

    - `type: "input_json_delta"`

      - `"input_json_delta"`

  - `CitationsDelta`

    - `citation: CitationCharLocation | CitationPageLocation | CitationContentBlockLocation | 2 more`

      - `CitationCharLocation`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_char_index: number`

        - `file_id: string | null`

        - `start_char_index: number`

        - `type: "char_location"`

          - `"char_location"`

      - `CitationPageLocation`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_page_number: number`

        - `file_id: string | null`

        - `start_page_number: number`

        - `type: "page_location"`

          - `"page_location"`

      - `CitationContentBlockLocation`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_block_index: number`

        - `file_id: string | null`

        - `start_block_index: number`

        - `type: "content_block_location"`

          - `"content_block_location"`

      - `CitationsWebSearchResultLocation`

        - `cited_text: string`

        - `encrypted_index: string`

        - `title: string | null`

        - `type: "web_search_result_location"`

          - `"web_search_result_location"`

        - `url: string`

      - `CitationsSearchResultLocation`

        - `cited_text: string`

        - `end_block_index: number`

        - `search_result_index: number`

        - `source: string`

        - `start_block_index: number`

        - `title: string | null`

        - `type: "search_result_location"`

          - `"search_result_location"`

    - `type: "citations_delta"`

      - `"citations_delta"`

  - `ThinkingDelta`

    - `thinking: string`

    - `type: "thinking_delta"`

      - `"thinking_delta"`

  - `SignatureDelta`

    - `signature: string`

    - `type: "signature_delta"`

      - `"signature_delta"`

### Raw Content Block Delta Event

- `RawContentBlockDeltaEvent`

  - `delta: RawContentBlockDelta`

    - `TextDelta`

      - `text: string`

      - `type: "text_delta"`

        - `"text_delta"`

    - `InputJSONDelta`

      - `partial_json: string`

      - `type: "input_json_delta"`

        - `"input_json_delta"`

    - `CitationsDelta`

      - `citation: CitationCharLocation | CitationPageLocation | CitationContentBlockLocation | 2 more`

        - `CitationCharLocation`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_char_index: number`

          - `file_id: string | null`

          - `start_char_index: number`

          - `type: "char_location"`

            - `"char_location"`

        - `CitationPageLocation`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_page_number: number`

          - `file_id: string | null`

          - `start_page_number: number`

          - `type: "page_location"`

            - `"page_location"`

        - `CitationContentBlockLocation`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_block_index: number`

          - `file_id: string | null`

          - `start_block_index: number`

          - `type: "content_block_location"`

            - `"content_block_location"`

        - `CitationsWebSearchResultLocation`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string | null`

          - `type: "web_search_result_location"`

            - `"web_search_result_location"`

          - `url: string`

        - `CitationsSearchResultLocation`

          - `cited_text: string`

          - `end_block_index: number`

          - `search_result_index: number`

          - `source: string`

          - `start_block_index: number`

          - `title: string | null`

          - `type: "search_result_location"`

            - `"search_result_location"`

      - `type: "citations_delta"`

        - `"citations_delta"`

    - `ThinkingDelta`

      - `thinking: string`

      - `type: "thinking_delta"`

        - `"thinking_delta"`

    - `SignatureDelta`

      - `signature: string`

      - `type: "signature_delta"`

        - `"signature_delta"`

  - `index: number`

  - `type: "content_block_delta"`

    - `"content_block_delta"`

### Raw Content Block Start Event

- `RawContentBlockStartEvent`

  - `content_block: TextBlock | ThinkingBlock | RedactedThinkingBlock | 9 more`

    Response model for a file uploaded to the container.

    - `TextBlock`

      - `citations: Array<TextCitation> | null`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `CitationCharLocation`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_char_index: number`

          - `file_id: string | null`

          - `start_char_index: number`

          - `type: "char_location"`

            - `"char_location"`

        - `CitationPageLocation`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_page_number: number`

          - `file_id: string | null`

          - `start_page_number: number`

          - `type: "page_location"`

            - `"page_location"`

        - `CitationContentBlockLocation`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string | null`

          - `end_block_index: number`

          - `file_id: string | null`

          - `start_block_index: number`

          - `type: "content_block_location"`

            - `"content_block_location"`

        - `CitationsWebSearchResultLocation`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string | null`

          - `type: "web_search_result_location"`

            - `"web_search_result_location"`

          - `url: string`

        - `CitationsSearchResultLocation`

          - `cited_text: string`

          - `end_block_index: number`

          - `search_result_index: number`

          - `source: string`

          - `start_block_index: number`

          - `title: string | null`

          - `type: "search_result_location"`

            - `"search_result_location"`

      - `text: string`

      - `type: "text"`

        - `"text"`

    - `ThinkingBlock`

      - `signature: string`

      - `thinking: string`

      - `type: "thinking"`

        - `"thinking"`

    - `RedactedThinkingBlock`

      - `data: string`

      - `type: "redacted_thinking"`

        - `"redacted_thinking"`

    - `ToolUseBlock`

      - `id: string`

      - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `DirectCaller`

          Tool invocation directly from the model.

          - `type: "direct"`

            - `"direct"`

        - `ServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

            - `"code_execution_20250825"`

        - `ServerToolCaller20260120`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

            - `"code_execution_20260120"`

      - `input: Record<string, unknown>`

      - `name: string`

      - `type: "tool_use"`

        - `"tool_use"`

    - `ServerToolUseBlock`

      - `id: string`

      - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `DirectCaller`

          Tool invocation directly from the model.

          - `type: "direct"`

            - `"direct"`

        - `ServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

            - `"code_execution_20250825"`

        - `ServerToolCaller20260120`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

            - `"code_execution_20260120"`

      - `input: Record<string, unknown>`

      - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

        - `"web_search"`

        - `"web_fetch"`

        - `"code_execution"`

        - `"bash_code_execution"`

        - `"text_editor_code_execution"`

        - `"tool_search_tool_regex"`

        - `"tool_search_tool_bm25"`

      - `type: "server_tool_use"`

        - `"server_tool_use"`

    - `WebSearchToolResultBlock`

      - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `DirectCaller`

          Tool invocation directly from the model.

          - `type: "direct"`

            - `"direct"`

        - `ServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

            - `"code_execution_20250825"`

        - `ServerToolCaller20260120`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

            - `"code_execution_20260120"`

      - `content: WebSearchToolResultBlockContent`

        - `WebSearchToolResultError`

          - `error_code: WebSearchToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"max_uses_exceeded"`

            - `"too_many_requests"`

            - `"query_too_long"`

            - `"request_too_large"`

          - `type: "web_search_tool_result_error"`

            - `"web_search_tool_result_error"`

        - `Array<WebSearchResultBlock>`

          - `encrypted_content: string`

          - `page_age: string | null`

          - `title: string`

          - `type: "web_search_result"`

            - `"web_search_result"`

          - `url: string`

      - `tool_use_id: string`

      - `type: "web_search_tool_result"`

        - `"web_search_tool_result"`

    - `WebFetchToolResultBlock`

      - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `DirectCaller`

          Tool invocation directly from the model.

          - `type: "direct"`

            - `"direct"`

        - `ServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

            - `"code_execution_20250825"`

        - `ServerToolCaller20260120`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

            - `"code_execution_20260120"`

      - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

        - `WebFetchToolResultErrorBlock`

          - `error_code: WebFetchToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"url_too_long"`

            - `"url_not_allowed"`

            - `"url_not_accessible"`

            - `"unsupported_content_type"`

            - `"too_many_requests"`

            - `"max_uses_exceeded"`

            - `"unavailable"`

          - `type: "web_fetch_tool_result_error"`

            - `"web_fetch_tool_result_error"`

        - `WebFetchBlock`

          - `content: DocumentBlock`

            - `citations: CitationsConfig | null`

              Citation configuration for the document

              - `enabled: boolean`

            - `source: Base64PDFSource | PlainTextSource`

              - `Base64PDFSource`

                - `data: string`

                - `media_type: "application/pdf"`

                  - `"application/pdf"`

                - `type: "base64"`

                  - `"base64"`

              - `PlainTextSource`

                - `data: string`

                - `media_type: "text/plain"`

                  - `"text/plain"`

                - `type: "text"`

                  - `"text"`

            - `title: string | null`

              The title of the document

            - `type: "document"`

              - `"document"`

          - `retrieved_at: string | null`

            ISO 8601 timestamp when the content was retrieved

          - `type: "web_fetch_result"`

            - `"web_fetch_result"`

          - `url: string`

            Fetched content URL

      - `tool_use_id: string`

      - `type: "web_fetch_tool_result"`

        - `"web_fetch_tool_result"`

    - `CodeExecutionToolResultBlock`

      - `content: CodeExecutionToolResultBlockContent`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `CodeExecutionToolResultError`

          - `error_code: CodeExecutionToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `type: "code_execution_tool_result_error"`

            - `"code_execution_tool_result_error"`

        - `CodeExecutionResultBlock`

          - `content: Array<CodeExecutionOutputBlock>`

            - `file_id: string`

            - `type: "code_execution_output"`

              - `"code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "code_execution_result"`

            - `"code_execution_result"`

        - `EncryptedCodeExecutionResultBlock`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `content: Array<CodeExecutionOutputBlock>`

            - `file_id: string`

            - `type: "code_execution_output"`

              - `"code_execution_output"`

          - `encrypted_stdout: string`

          - `return_code: number`

          - `stderr: string`

          - `type: "encrypted_code_execution_result"`

            - `"encrypted_code_execution_result"`

      - `tool_use_id: string`

      - `type: "code_execution_tool_result"`

        - `"code_execution_tool_result"`

    - `BashCodeExecutionToolResultBlock`

      - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

        - `BashCodeExecutionToolResultError`

          - `error_code: BashCodeExecutionToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"output_file_too_large"`

          - `type: "bash_code_execution_tool_result_error"`

            - `"bash_code_execution_tool_result_error"`

        - `BashCodeExecutionResultBlock`

          - `content: Array<BashCodeExecutionOutputBlock>`

            - `file_id: string`

            - `type: "bash_code_execution_output"`

              - `"bash_code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "bash_code_execution_result"`

            - `"bash_code_execution_result"`

      - `tool_use_id: string`

      - `type: "bash_code_execution_tool_result"`

        - `"bash_code_execution_tool_result"`

    - `TextEditorCodeExecutionToolResultBlock`

      - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

        - `TextEditorCodeExecutionToolResultError`

          - `error_code: TextEditorCodeExecutionToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"file_not_found"`

          - `error_message: string | null`

          - `type: "text_editor_code_execution_tool_result_error"`

            - `"text_editor_code_execution_tool_result_error"`

        - `TextEditorCodeExecutionViewResultBlock`

          - `content: string`

          - `file_type: "text" | "image" | "pdf"`

            - `"text"`

            - `"image"`

            - `"pdf"`

          - `num_lines: number | null`

          - `start_line: number | null`

          - `total_lines: number | null`

          - `type: "text_editor_code_execution_view_result"`

            - `"text_editor_code_execution_view_result"`

        - `TextEditorCodeExecutionCreateResultBlock`

          - `is_file_update: boolean`

          - `type: "text_editor_code_execution_create_result"`

            - `"text_editor_code_execution_create_result"`

        - `TextEditorCodeExecutionStrReplaceResultBlock`

          - `lines: Array<string> | null`

          - `new_lines: number | null`

          - `new_start: number | null`

          - `old_lines: number | null`

          - `old_start: number | null`

          - `type: "text_editor_code_execution_str_replace_result"`

            - `"text_editor_code_execution_str_replace_result"`

      - `tool_use_id: string`

      - `type: "text_editor_code_execution_tool_result"`

        - `"text_editor_code_execution_tool_result"`

    - `ToolSearchToolResultBlock`

      - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

        - `ToolSearchToolResultError`

          - `error_code: ToolSearchToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `error_message: string | null`

          - `type: "tool_search_tool_result_error"`

            - `"tool_search_tool_result_error"`

        - `ToolSearchToolSearchResultBlock`

          - `tool_references: Array<ToolReferenceBlock>`

            - `tool_name: string`

            - `type: "tool_reference"`

              - `"tool_reference"`

          - `type: "tool_search_tool_search_result"`

            - `"tool_search_tool_search_result"`

      - `tool_use_id: string`

      - `type: "tool_search_tool_result"`

        - `"tool_search_tool_result"`

    - `ContainerUploadBlock`

      Response model for a file uploaded to the container.

      - `file_id: string`

      - `type: "container_upload"`

        - `"container_upload"`

  - `index: number`

  - `type: "content_block_start"`

    - `"content_block_start"`

### Raw Content Block Stop Event

- `RawContentBlockStopEvent`

  - `index: number`

  - `type: "content_block_stop"`

    - `"content_block_stop"`

### Raw Message Delta Event

- `RawMessageDeltaEvent`

  - `delta: Delta`

    - `container: Container | null`

      Information about the container used in the request (for the code execution tool)

      - `id: string`

        Identifier for the container used in this request

      - `expires_at: string`

        The time at which the container will expire.

    - `stop_reason: StopReason | null`

      - `"end_turn"`

      - `"max_tokens"`

      - `"stop_sequence"`

      - `"tool_use"`

      - `"pause_turn"`

      - `"refusal"`

    - `stop_sequence: string | null`

  - `type: "message_delta"`

    - `"message_delta"`

  - `usage: MessageDeltaUsage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `cache_creation_input_tokens: number | null`

      The cumulative number of input tokens used to create the cache entry.

    - `cache_read_input_tokens: number | null`

      The cumulative number of input tokens read from the cache.

    - `input_tokens: number | null`

      The cumulative number of input tokens which were used.

    - `output_tokens: number`

      The cumulative number of output tokens which were used.

    - `server_tool_use: ServerToolUsage | null`

      The number of server tool requests.

      - `web_fetch_requests: number`

        The number of web fetch tool requests.

      - `web_search_requests: number`

        The number of web search tool requests.

### Raw Message Start Event

- `RawMessageStartEvent`

  - `message: Message`

    - `id: string`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `container: Container | null`

      Information about the container used in the request (for the code execution tool)

      - `id: string`

        Identifier for the container used in this request

      - `expires_at: string`

        The time at which the container will expire.

    - `content: Array<ContentBlock>`

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

      - `TextBlock`

        - `citations: Array<TextCitation> | null`

          Citations supporting the text block.

          The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `CitationCharLocation`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_char_index: number`

            - `file_id: string | null`

            - `start_char_index: number`

            - `type: "char_location"`

              - `"char_location"`

          - `CitationPageLocation`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_page_number: number`

            - `file_id: string | null`

            - `start_page_number: number`

            - `type: "page_location"`

              - `"page_location"`

          - `CitationContentBlockLocation`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_block_index: number`

            - `file_id: string | null`

            - `start_block_index: number`

            - `type: "content_block_location"`

              - `"content_block_location"`

          - `CitationsWebSearchResultLocation`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string | null`

            - `type: "web_search_result_location"`

              - `"web_search_result_location"`

            - `url: string`

          - `CitationsSearchResultLocation`

            - `cited_text: string`

            - `end_block_index: number`

            - `search_result_index: number`

            - `source: string`

            - `start_block_index: number`

            - `title: string | null`

            - `type: "search_result_location"`

              - `"search_result_location"`

        - `text: string`

        - `type: "text"`

          - `"text"`

      - `ThinkingBlock`

        - `signature: string`

        - `thinking: string`

        - `type: "thinking"`

          - `"thinking"`

      - `RedactedThinkingBlock`

        - `data: string`

        - `type: "redacted_thinking"`

          - `"redacted_thinking"`

      - `ToolUseBlock`

        - `id: string`

        - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

        - `input: Record<string, unknown>`

        - `name: string`

        - `type: "tool_use"`

          - `"tool_use"`

      - `ServerToolUseBlock`

        - `id: string`

        - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

        - `input: Record<string, unknown>`

        - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

          - `"web_search"`

          - `"web_fetch"`

          - `"code_execution"`

          - `"bash_code_execution"`

          - `"text_editor_code_execution"`

          - `"tool_search_tool_regex"`

          - `"tool_search_tool_bm25"`

        - `type: "server_tool_use"`

          - `"server_tool_use"`

      - `WebSearchToolResultBlock`

        - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

        - `content: WebSearchToolResultBlockContent`

          - `WebSearchToolResultError`

            - `error_code: WebSearchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"max_uses_exceeded"`

              - `"too_many_requests"`

              - `"query_too_long"`

              - `"request_too_large"`

            - `type: "web_search_tool_result_error"`

              - `"web_search_tool_result_error"`

          - `Array<WebSearchResultBlock>`

            - `encrypted_content: string`

            - `page_age: string | null`

            - `title: string`

            - `type: "web_search_result"`

              - `"web_search_result"`

            - `url: string`

        - `tool_use_id: string`

        - `type: "web_search_tool_result"`

          - `"web_search_tool_result"`

      - `WebFetchToolResultBlock`

        - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

        - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

          - `WebFetchToolResultErrorBlock`

            - `error_code: WebFetchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"url_too_long"`

              - `"url_not_allowed"`

              - `"url_not_accessible"`

              - `"unsupported_content_type"`

              - `"too_many_requests"`

              - `"max_uses_exceeded"`

              - `"unavailable"`

            - `type: "web_fetch_tool_result_error"`

              - `"web_fetch_tool_result_error"`

          - `WebFetchBlock`

            - `content: DocumentBlock`

              - `citations: CitationsConfig | null`

                Citation configuration for the document

                - `enabled: boolean`

              - `source: Base64PDFSource | PlainTextSource`

                - `Base64PDFSource`

                  - `data: string`

                  - `media_type: "application/pdf"`

                    - `"application/pdf"`

                  - `type: "base64"`

                    - `"base64"`

                - `PlainTextSource`

                  - `data: string`

                  - `media_type: "text/plain"`

                    - `"text/plain"`

                  - `type: "text"`

                    - `"text"`

              - `title: string | null`

                The title of the document

              - `type: "document"`

                - `"document"`

            - `retrieved_at: string | null`

              ISO 8601 timestamp when the content was retrieved

            - `type: "web_fetch_result"`

              - `"web_fetch_result"`

            - `url: string`

              Fetched content URL

        - `tool_use_id: string`

        - `type: "web_fetch_tool_result"`

          - `"web_fetch_tool_result"`

      - `CodeExecutionToolResultBlock`

        - `content: CodeExecutionToolResultBlockContent`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `CodeExecutionToolResultError`

            - `error_code: CodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `type: "code_execution_tool_result_error"`

              - `"code_execution_tool_result_error"`

          - `CodeExecutionResultBlock`

            - `content: Array<CodeExecutionOutputBlock>`

              - `file_id: string`

              - `type: "code_execution_output"`

                - `"code_execution_output"`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

            - `type: "code_execution_result"`

              - `"code_execution_result"`

          - `EncryptedCodeExecutionResultBlock`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `content: Array<CodeExecutionOutputBlock>`

              - `file_id: string`

              - `type: "code_execution_output"`

                - `"code_execution_output"`

            - `encrypted_stdout: string`

            - `return_code: number`

            - `stderr: string`

            - `type: "encrypted_code_execution_result"`

              - `"encrypted_code_execution_result"`

        - `tool_use_id: string`

        - `type: "code_execution_tool_result"`

          - `"code_execution_tool_result"`

      - `BashCodeExecutionToolResultBlock`

        - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

          - `BashCodeExecutionToolResultError`

            - `error_code: BashCodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"output_file_too_large"`

            - `type: "bash_code_execution_tool_result_error"`

              - `"bash_code_execution_tool_result_error"`

          - `BashCodeExecutionResultBlock`

            - `content: Array<BashCodeExecutionOutputBlock>`

              - `file_id: string`

              - `type: "bash_code_execution_output"`

                - `"bash_code_execution_output"`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

            - `type: "bash_code_execution_result"`

              - `"bash_code_execution_result"`

        - `tool_use_id: string`

        - `type: "bash_code_execution_tool_result"`

          - `"bash_code_execution_tool_result"`

      - `TextEditorCodeExecutionToolResultBlock`

        - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

          - `TextEditorCodeExecutionToolResultError`

            - `error_code: TextEditorCodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"file_not_found"`

            - `error_message: string | null`

            - `type: "text_editor_code_execution_tool_result_error"`

              - `"text_editor_code_execution_tool_result_error"`

          - `TextEditorCodeExecutionViewResultBlock`

            - `content: string`

            - `file_type: "text" | "image" | "pdf"`

              - `"text"`

              - `"image"`

              - `"pdf"`

            - `num_lines: number | null`

            - `start_line: number | null`

            - `total_lines: number | null`

            - `type: "text_editor_code_execution_view_result"`

              - `"text_editor_code_execution_view_result"`

          - `TextEditorCodeExecutionCreateResultBlock`

            - `is_file_update: boolean`

            - `type: "text_editor_code_execution_create_result"`

              - `"text_editor_code_execution_create_result"`

          - `TextEditorCodeExecutionStrReplaceResultBlock`

            - `lines: Array<string> | null`

            - `new_lines: number | null`

            - `new_start: number | null`

            - `old_lines: number | null`

            - `old_start: number | null`

            - `type: "text_editor_code_execution_str_replace_result"`

              - `"text_editor_code_execution_str_replace_result"`

        - `tool_use_id: string`

        - `type: "text_editor_code_execution_tool_result"`

          - `"text_editor_code_execution_tool_result"`

      - `ToolSearchToolResultBlock`

        - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

          - `ToolSearchToolResultError`

            - `error_code: ToolSearchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `error_message: string | null`

            - `type: "tool_search_tool_result_error"`

              - `"tool_search_tool_result_error"`

          - `ToolSearchToolSearchResultBlock`

            - `tool_references: Array<ToolReferenceBlock>`

              - `tool_name: string`

              - `type: "tool_reference"`

                - `"tool_reference"`

            - `type: "tool_search_tool_search_result"`

              - `"tool_search_tool_search_result"`

        - `tool_use_id: string`

        - `type: "tool_search_tool_result"`

          - `"tool_search_tool_result"`

      - `ContainerUploadBlock`

        Response model for a file uploaded to the container.

        - `file_id: string`

        - `type: "container_upload"`

          - `"container_upload"`

    - `model: Model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-opus-4-5-20251101" | 19 more`

        - `"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `"claude-sonnet-4-6"`

          Frontier intelligence at scale — built for coding, agents, and enterprise workflows

        - `"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `"claude-3-7-sonnet-latest"`

          High-performance model with early extended thinking

        - `"claude-3-7-sonnet-20250219"`

          High-performance model with early extended thinking

        - `"claude-3-5-haiku-latest"`

          Fastest and most compact model for near-instant responsiveness

        - `"claude-3-5-haiku-20241022"`

          Our fastest model

        - `"claude-haiku-4-5"`

          Hybrid model, capable of near-instant responses and extended thinking

        - `"claude-haiku-4-5-20251001"`

          Hybrid model, capable of near-instant responses and extended thinking

        - `"claude-sonnet-4-20250514"`

          High-performance model with extended thinking

        - `"claude-sonnet-4-0"`

          High-performance model with extended thinking

        - `"claude-4-sonnet-20250514"`

          High-performance model with extended thinking

        - `"claude-sonnet-4-5"`

          Our best model for real-world agents and coding

        - `"claude-sonnet-4-5-20250929"`

          Our best model for real-world agents and coding

        - `"claude-opus-4-0"`

          Our most capable model

        - `"claude-opus-4-20250514"`

          Our most capable model

        - `"claude-4-opus-20250514"`

          Our most capable model

        - `"claude-opus-4-1-20250805"`

          Our most capable model

        - `"claude-3-opus-latest"`

          Excels at writing and complex tasks

        - `"claude-3-opus-20240229"`

          Excels at writing and complex tasks

        - `"claude-3-haiku-20240307"`

          Our previous most fast and cost-effective

      - `(string & {})`

    - `role: "assistant"`

      Conversational role of the generated message.

      This will always be `"assistant"`.

      - `"assistant"`

    - `stop_reason: StopReason | null`

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

      - `"refusal"`

    - `stop_sequence: string | null`

      Which custom stop sequence was generated, if any.

      This value will be a non-null string if one of your custom stop sequences was generated.

    - `type: "message"`

      Object type.

      For Messages, this is always `"message"`.

      - `"message"`

    - `usage: Usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `cache_creation: CacheCreation | null`

        Breakdown of cached tokens by TTL

        - `ephemeral_1h_input_tokens: number`

          The number of input tokens used to create the 1 hour cache entry.

        - `ephemeral_5m_input_tokens: number`

          The number of input tokens used to create the 5 minute cache entry.

      - `cache_creation_input_tokens: number | null`

        The number of input tokens used to create the cache entry.

      - `cache_read_input_tokens: number | null`

        The number of input tokens read from the cache.

      - `inference_geo: string | null`

        The geographic region where inference was performed for this request.

      - `input_tokens: number`

        The number of input tokens which were used.

      - `output_tokens: number`

        The number of output tokens which were used.

      - `server_tool_use: ServerToolUsage | null`

        The number of server tool requests.

        - `web_fetch_requests: number`

          The number of web fetch tool requests.

        - `web_search_requests: number`

          The number of web search tool requests.

      - `service_tier: "standard" | "priority" | "batch" | null`

        If the request used the priority, standard, or batch tier.

        - `"standard"`

        - `"priority"`

        - `"batch"`

  - `type: "message_start"`

    - `"message_start"`

### Raw Message Stop Event

- `RawMessageStopEvent`

  - `type: "message_stop"`

    - `"message_stop"`

### Raw Message Stream Event

- `RawMessageStreamEvent = RawMessageStartEvent | RawMessageDeltaEvent | RawMessageStopEvent | 3 more`

  - `RawMessageStartEvent`

    - `message: Message`

      - `id: string`

        Unique object identifier.

        The format and length of IDs may change over time.

      - `container: Container | null`

        Information about the container used in the request (for the code execution tool)

        - `id: string`

          Identifier for the container used in this request

        - `expires_at: string`

          The time at which the container will expire.

      - `content: Array<ContentBlock>`

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

        - `TextBlock`

          - `citations: Array<TextCitation> | null`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `CitationCharLocation`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_char_index: number`

              - `file_id: string | null`

              - `start_char_index: number`

              - `type: "char_location"`

                - `"char_location"`

            - `CitationPageLocation`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_page_number: number`

              - `file_id: string | null`

              - `start_page_number: number`

              - `type: "page_location"`

                - `"page_location"`

            - `CitationContentBlockLocation`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_block_index: number`

              - `file_id: string | null`

              - `start_block_index: number`

              - `type: "content_block_location"`

                - `"content_block_location"`

            - `CitationsWebSearchResultLocation`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string | null`

              - `type: "web_search_result_location"`

                - `"web_search_result_location"`

              - `url: string`

            - `CitationsSearchResultLocation`

              - `cited_text: string`

              - `end_block_index: number`

              - `search_result_index: number`

              - `source: string`

              - `start_block_index: number`

              - `title: string | null`

              - `type: "search_result_location"`

                - `"search_result_location"`

          - `text: string`

          - `type: "text"`

            - `"text"`

        - `ThinkingBlock`

          - `signature: string`

          - `thinking: string`

          - `type: "thinking"`

            - `"thinking"`

        - `RedactedThinkingBlock`

          - `data: string`

          - `type: "redacted_thinking"`

            - `"redacted_thinking"`

        - `ToolUseBlock`

          - `id: string`

          - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `DirectCaller`

              Tool invocation directly from the model.

              - `type: "direct"`

                - `"direct"`

            - `ServerToolCaller`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

              - `type: "code_execution_20250825"`

                - `"code_execution_20250825"`

            - `ServerToolCaller20260120`

              - `tool_id: string`

              - `type: "code_execution_20260120"`

                - `"code_execution_20260120"`

          - `input: Record<string, unknown>`

          - `name: string`

          - `type: "tool_use"`

            - `"tool_use"`

        - `ServerToolUseBlock`

          - `id: string`

          - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `DirectCaller`

              Tool invocation directly from the model.

              - `type: "direct"`

                - `"direct"`

            - `ServerToolCaller`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

              - `type: "code_execution_20250825"`

                - `"code_execution_20250825"`

            - `ServerToolCaller20260120`

              - `tool_id: string`

              - `type: "code_execution_20260120"`

                - `"code_execution_20260120"`

          - `input: Record<string, unknown>`

          - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

            - `"web_search"`

            - `"web_fetch"`

            - `"code_execution"`

            - `"bash_code_execution"`

            - `"text_editor_code_execution"`

            - `"tool_search_tool_regex"`

            - `"tool_search_tool_bm25"`

          - `type: "server_tool_use"`

            - `"server_tool_use"`

        - `WebSearchToolResultBlock`

          - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `DirectCaller`

              Tool invocation directly from the model.

              - `type: "direct"`

                - `"direct"`

            - `ServerToolCaller`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

              - `type: "code_execution_20250825"`

                - `"code_execution_20250825"`

            - `ServerToolCaller20260120`

              - `tool_id: string`

              - `type: "code_execution_20260120"`

                - `"code_execution_20260120"`

          - `content: WebSearchToolResultBlockContent`

            - `WebSearchToolResultError`

              - `error_code: WebSearchToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"max_uses_exceeded"`

                - `"too_many_requests"`

                - `"query_too_long"`

                - `"request_too_large"`

              - `type: "web_search_tool_result_error"`

                - `"web_search_tool_result_error"`

            - `Array<WebSearchResultBlock>`

              - `encrypted_content: string`

              - `page_age: string | null`

              - `title: string`

              - `type: "web_search_result"`

                - `"web_search_result"`

              - `url: string`

          - `tool_use_id: string`

          - `type: "web_search_tool_result"`

            - `"web_search_tool_result"`

        - `WebFetchToolResultBlock`

          - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `DirectCaller`

              Tool invocation directly from the model.

              - `type: "direct"`

                - `"direct"`

            - `ServerToolCaller`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

              - `type: "code_execution_20250825"`

                - `"code_execution_20250825"`

            - `ServerToolCaller20260120`

              - `tool_id: string`

              - `type: "code_execution_20260120"`

                - `"code_execution_20260120"`

          - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

            - `WebFetchToolResultErrorBlock`

              - `error_code: WebFetchToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"url_too_long"`

                - `"url_not_allowed"`

                - `"url_not_accessible"`

                - `"unsupported_content_type"`

                - `"too_many_requests"`

                - `"max_uses_exceeded"`

                - `"unavailable"`

              - `type: "web_fetch_tool_result_error"`

                - `"web_fetch_tool_result_error"`

            - `WebFetchBlock`

              - `content: DocumentBlock`

                - `citations: CitationsConfig | null`

                  Citation configuration for the document

                  - `enabled: boolean`

                - `source: Base64PDFSource | PlainTextSource`

                  - `Base64PDFSource`

                    - `data: string`

                    - `media_type: "application/pdf"`

                      - `"application/pdf"`

                    - `type: "base64"`

                      - `"base64"`

                  - `PlainTextSource`

                    - `data: string`

                    - `media_type: "text/plain"`

                      - `"text/plain"`

                    - `type: "text"`

                      - `"text"`

                - `title: string | null`

                  The title of the document

                - `type: "document"`

                  - `"document"`

              - `retrieved_at: string | null`

                ISO 8601 timestamp when the content was retrieved

              - `type: "web_fetch_result"`

                - `"web_fetch_result"`

              - `url: string`

                Fetched content URL

          - `tool_use_id: string`

          - `type: "web_fetch_tool_result"`

            - `"web_fetch_tool_result"`

        - `CodeExecutionToolResultBlock`

          - `content: CodeExecutionToolResultBlockContent`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `CodeExecutionToolResultError`

              - `error_code: CodeExecutionToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

              - `type: "code_execution_tool_result_error"`

                - `"code_execution_tool_result_error"`

            - `CodeExecutionResultBlock`

              - `content: Array<CodeExecutionOutputBlock>`

                - `file_id: string`

                - `type: "code_execution_output"`

                  - `"code_execution_output"`

              - `return_code: number`

              - `stderr: string`

              - `stdout: string`

              - `type: "code_execution_result"`

                - `"code_execution_result"`

            - `EncryptedCodeExecutionResultBlock`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `content: Array<CodeExecutionOutputBlock>`

                - `file_id: string`

                - `type: "code_execution_output"`

                  - `"code_execution_output"`

              - `encrypted_stdout: string`

              - `return_code: number`

              - `stderr: string`

              - `type: "encrypted_code_execution_result"`

                - `"encrypted_code_execution_result"`

          - `tool_use_id: string`

          - `type: "code_execution_tool_result"`

            - `"code_execution_tool_result"`

        - `BashCodeExecutionToolResultBlock`

          - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

            - `BashCodeExecutionToolResultError`

              - `error_code: BashCodeExecutionToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

                - `"output_file_too_large"`

              - `type: "bash_code_execution_tool_result_error"`

                - `"bash_code_execution_tool_result_error"`

            - `BashCodeExecutionResultBlock`

              - `content: Array<BashCodeExecutionOutputBlock>`

                - `file_id: string`

                - `type: "bash_code_execution_output"`

                  - `"bash_code_execution_output"`

              - `return_code: number`

              - `stderr: string`

              - `stdout: string`

              - `type: "bash_code_execution_result"`

                - `"bash_code_execution_result"`

          - `tool_use_id: string`

          - `type: "bash_code_execution_tool_result"`

            - `"bash_code_execution_tool_result"`

        - `TextEditorCodeExecutionToolResultBlock`

          - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

            - `TextEditorCodeExecutionToolResultError`

              - `error_code: TextEditorCodeExecutionToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

                - `"file_not_found"`

              - `error_message: string | null`

              - `type: "text_editor_code_execution_tool_result_error"`

                - `"text_editor_code_execution_tool_result_error"`

            - `TextEditorCodeExecutionViewResultBlock`

              - `content: string`

              - `file_type: "text" | "image" | "pdf"`

                - `"text"`

                - `"image"`

                - `"pdf"`

              - `num_lines: number | null`

              - `start_line: number | null`

              - `total_lines: number | null`

              - `type: "text_editor_code_execution_view_result"`

                - `"text_editor_code_execution_view_result"`

            - `TextEditorCodeExecutionCreateResultBlock`

              - `is_file_update: boolean`

              - `type: "text_editor_code_execution_create_result"`

                - `"text_editor_code_execution_create_result"`

            - `TextEditorCodeExecutionStrReplaceResultBlock`

              - `lines: Array<string> | null`

              - `new_lines: number | null`

              - `new_start: number | null`

              - `old_lines: number | null`

              - `old_start: number | null`

              - `type: "text_editor_code_execution_str_replace_result"`

                - `"text_editor_code_execution_str_replace_result"`

          - `tool_use_id: string`

          - `type: "text_editor_code_execution_tool_result"`

            - `"text_editor_code_execution_tool_result"`

        - `ToolSearchToolResultBlock`

          - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

            - `ToolSearchToolResultError`

              - `error_code: ToolSearchToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

              - `error_message: string | null`

              - `type: "tool_search_tool_result_error"`

                - `"tool_search_tool_result_error"`

            - `ToolSearchToolSearchResultBlock`

              - `tool_references: Array<ToolReferenceBlock>`

                - `tool_name: string`

                - `type: "tool_reference"`

                  - `"tool_reference"`

              - `type: "tool_search_tool_search_result"`

                - `"tool_search_tool_search_result"`

          - `tool_use_id: string`

          - `type: "tool_search_tool_result"`

            - `"tool_search_tool_result"`

        - `ContainerUploadBlock`

          Response model for a file uploaded to the container.

          - `file_id: string`

          - `type: "container_upload"`

            - `"container_upload"`

      - `model: Model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-opus-4-5-20251101" | 19 more`

          - `"claude-opus-4-6"`

            Most intelligent model for building agents and coding

          - `"claude-sonnet-4-6"`

            Frontier intelligence at scale — built for coding, agents, and enterprise workflows

          - `"claude-opus-4-5-20251101"`

            Premium model combining maximum intelligence with practical performance

          - `"claude-opus-4-5"`

            Premium model combining maximum intelligence with practical performance

          - `"claude-3-7-sonnet-latest"`

            High-performance model with early extended thinking

          - `"claude-3-7-sonnet-20250219"`

            High-performance model with early extended thinking

          - `"claude-3-5-haiku-latest"`

            Fastest and most compact model for near-instant responsiveness

          - `"claude-3-5-haiku-20241022"`

            Our fastest model

          - `"claude-haiku-4-5"`

            Hybrid model, capable of near-instant responses and extended thinking

          - `"claude-haiku-4-5-20251001"`

            Hybrid model, capable of near-instant responses and extended thinking

          - `"claude-sonnet-4-20250514"`

            High-performance model with extended thinking

          - `"claude-sonnet-4-0"`

            High-performance model with extended thinking

          - `"claude-4-sonnet-20250514"`

            High-performance model with extended thinking

          - `"claude-sonnet-4-5"`

            Our best model for real-world agents and coding

          - `"claude-sonnet-4-5-20250929"`

            Our best model for real-world agents and coding

          - `"claude-opus-4-0"`

            Our most capable model

          - `"claude-opus-4-20250514"`

            Our most capable model

          - `"claude-4-opus-20250514"`

            Our most capable model

          - `"claude-opus-4-1-20250805"`

            Our most capable model

          - `"claude-3-opus-latest"`

            Excels at writing and complex tasks

          - `"claude-3-opus-20240229"`

            Excels at writing and complex tasks

          - `"claude-3-haiku-20240307"`

            Our previous most fast and cost-effective

        - `(string & {})`

      - `role: "assistant"`

        Conversational role of the generated message.

        This will always be `"assistant"`.

        - `"assistant"`

      - `stop_reason: StopReason | null`

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

        - `"refusal"`

      - `stop_sequence: string | null`

        Which custom stop sequence was generated, if any.

        This value will be a non-null string if one of your custom stop sequences was generated.

      - `type: "message"`

        Object type.

        For Messages, this is always `"message"`.

        - `"message"`

      - `usage: Usage`

        Billing and rate-limit usage.

        Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

        Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

        For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

        Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

        - `cache_creation: CacheCreation | null`

          Breakdown of cached tokens by TTL

          - `ephemeral_1h_input_tokens: number`

            The number of input tokens used to create the 1 hour cache entry.

          - `ephemeral_5m_input_tokens: number`

            The number of input tokens used to create the 5 minute cache entry.

        - `cache_creation_input_tokens: number | null`

          The number of input tokens used to create the cache entry.

        - `cache_read_input_tokens: number | null`

          The number of input tokens read from the cache.

        - `inference_geo: string | null`

          The geographic region where inference was performed for this request.

        - `input_tokens: number`

          The number of input tokens which were used.

        - `output_tokens: number`

          The number of output tokens which were used.

        - `server_tool_use: ServerToolUsage | null`

          The number of server tool requests.

          - `web_fetch_requests: number`

            The number of web fetch tool requests.

          - `web_search_requests: number`

            The number of web search tool requests.

        - `service_tier: "standard" | "priority" | "batch" | null`

          If the request used the priority, standard, or batch tier.

          - `"standard"`

          - `"priority"`

          - `"batch"`

    - `type: "message_start"`

      - `"message_start"`

  - `RawMessageDeltaEvent`

    - `delta: Delta`

      - `container: Container | null`

        Information about the container used in the request (for the code execution tool)

        - `id: string`

          Identifier for the container used in this request

        - `expires_at: string`

          The time at which the container will expire.

      - `stop_reason: StopReason | null`

        - `"end_turn"`

        - `"max_tokens"`

        - `"stop_sequence"`

        - `"tool_use"`

        - `"pause_turn"`

        - `"refusal"`

      - `stop_sequence: string | null`

    - `type: "message_delta"`

      - `"message_delta"`

    - `usage: MessageDeltaUsage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `cache_creation_input_tokens: number | null`

        The cumulative number of input tokens used to create the cache entry.

      - `cache_read_input_tokens: number | null`

        The cumulative number of input tokens read from the cache.

      - `input_tokens: number | null`

        The cumulative number of input tokens which were used.

      - `output_tokens: number`

        The cumulative number of output tokens which were used.

      - `server_tool_use: ServerToolUsage | null`

        The number of server tool requests.

        - `web_fetch_requests: number`

          The number of web fetch tool requests.

        - `web_search_requests: number`

          The number of web search tool requests.

  - `RawMessageStopEvent`

    - `type: "message_stop"`

      - `"message_stop"`

  - `RawContentBlockStartEvent`

    - `content_block: TextBlock | ThinkingBlock | RedactedThinkingBlock | 9 more`

      Response model for a file uploaded to the container.

      - `TextBlock`

        - `citations: Array<TextCitation> | null`

          Citations supporting the text block.

          The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `CitationCharLocation`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_char_index: number`

            - `file_id: string | null`

            - `start_char_index: number`

            - `type: "char_location"`

              - `"char_location"`

          - `CitationPageLocation`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_page_number: number`

            - `file_id: string | null`

            - `start_page_number: number`

            - `type: "page_location"`

              - `"page_location"`

          - `CitationContentBlockLocation`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_block_index: number`

            - `file_id: string | null`

            - `start_block_index: number`

            - `type: "content_block_location"`

              - `"content_block_location"`

          - `CitationsWebSearchResultLocation`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string | null`

            - `type: "web_search_result_location"`

              - `"web_search_result_location"`

            - `url: string`

          - `CitationsSearchResultLocation`

            - `cited_text: string`

            - `end_block_index: number`

            - `search_result_index: number`

            - `source: string`

            - `start_block_index: number`

            - `title: string | null`

            - `type: "search_result_location"`

              - `"search_result_location"`

        - `text: string`

        - `type: "text"`

          - `"text"`

      - `ThinkingBlock`

        - `signature: string`

        - `thinking: string`

        - `type: "thinking"`

          - `"thinking"`

      - `RedactedThinkingBlock`

        - `data: string`

        - `type: "redacted_thinking"`

          - `"redacted_thinking"`

      - `ToolUseBlock`

        - `id: string`

        - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

        - `input: Record<string, unknown>`

        - `name: string`

        - `type: "tool_use"`

          - `"tool_use"`

      - `ServerToolUseBlock`

        - `id: string`

        - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

        - `input: Record<string, unknown>`

        - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

          - `"web_search"`

          - `"web_fetch"`

          - `"code_execution"`

          - `"bash_code_execution"`

          - `"text_editor_code_execution"`

          - `"tool_search_tool_regex"`

          - `"tool_search_tool_bm25"`

        - `type: "server_tool_use"`

          - `"server_tool_use"`

      - `WebSearchToolResultBlock`

        - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

        - `content: WebSearchToolResultBlockContent`

          - `WebSearchToolResultError`

            - `error_code: WebSearchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"max_uses_exceeded"`

              - `"too_many_requests"`

              - `"query_too_long"`

              - `"request_too_large"`

            - `type: "web_search_tool_result_error"`

              - `"web_search_tool_result_error"`

          - `Array<WebSearchResultBlock>`

            - `encrypted_content: string`

            - `page_age: string | null`

            - `title: string`

            - `type: "web_search_result"`

              - `"web_search_result"`

            - `url: string`

        - `tool_use_id: string`

        - `type: "web_search_tool_result"`

          - `"web_search_tool_result"`

      - `WebFetchToolResultBlock`

        - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

        - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

          - `WebFetchToolResultErrorBlock`

            - `error_code: WebFetchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"url_too_long"`

              - `"url_not_allowed"`

              - `"url_not_accessible"`

              - `"unsupported_content_type"`

              - `"too_many_requests"`

              - `"max_uses_exceeded"`

              - `"unavailable"`

            - `type: "web_fetch_tool_result_error"`

              - `"web_fetch_tool_result_error"`

          - `WebFetchBlock`

            - `content: DocumentBlock`

              - `citations: CitationsConfig | null`

                Citation configuration for the document

                - `enabled: boolean`

              - `source: Base64PDFSource | PlainTextSource`

                - `Base64PDFSource`

                  - `data: string`

                  - `media_type: "application/pdf"`

                    - `"application/pdf"`

                  - `type: "base64"`

                    - `"base64"`

                - `PlainTextSource`

                  - `data: string`

                  - `media_type: "text/plain"`

                    - `"text/plain"`

                  - `type: "text"`

                    - `"text"`

              - `title: string | null`

                The title of the document

              - `type: "document"`

                - `"document"`

            - `retrieved_at: string | null`

              ISO 8601 timestamp when the content was retrieved

            - `type: "web_fetch_result"`

              - `"web_fetch_result"`

            - `url: string`

              Fetched content URL

        - `tool_use_id: string`

        - `type: "web_fetch_tool_result"`

          - `"web_fetch_tool_result"`

      - `CodeExecutionToolResultBlock`

        - `content: CodeExecutionToolResultBlockContent`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `CodeExecutionToolResultError`

            - `error_code: CodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `type: "code_execution_tool_result_error"`

              - `"code_execution_tool_result_error"`

          - `CodeExecutionResultBlock`

            - `content: Array<CodeExecutionOutputBlock>`

              - `file_id: string`

              - `type: "code_execution_output"`

                - `"code_execution_output"`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

            - `type: "code_execution_result"`

              - `"code_execution_result"`

          - `EncryptedCodeExecutionResultBlock`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `content: Array<CodeExecutionOutputBlock>`

              - `file_id: string`

              - `type: "code_execution_output"`

                - `"code_execution_output"`

            - `encrypted_stdout: string`

            - `return_code: number`

            - `stderr: string`

            - `type: "encrypted_code_execution_result"`

              - `"encrypted_code_execution_result"`

        - `tool_use_id: string`

        - `type: "code_execution_tool_result"`

          - `"code_execution_tool_result"`

      - `BashCodeExecutionToolResultBlock`

        - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

          - `BashCodeExecutionToolResultError`

            - `error_code: BashCodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"output_file_too_large"`

            - `type: "bash_code_execution_tool_result_error"`

              - `"bash_code_execution_tool_result_error"`

          - `BashCodeExecutionResultBlock`

            - `content: Array<BashCodeExecutionOutputBlock>`

              - `file_id: string`

              - `type: "bash_code_execution_output"`

                - `"bash_code_execution_output"`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

            - `type: "bash_code_execution_result"`

              - `"bash_code_execution_result"`

        - `tool_use_id: string`

        - `type: "bash_code_execution_tool_result"`

          - `"bash_code_execution_tool_result"`

      - `TextEditorCodeExecutionToolResultBlock`

        - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

          - `TextEditorCodeExecutionToolResultError`

            - `error_code: TextEditorCodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"file_not_found"`

            - `error_message: string | null`

            - `type: "text_editor_code_execution_tool_result_error"`

              - `"text_editor_code_execution_tool_result_error"`

          - `TextEditorCodeExecutionViewResultBlock`

            - `content: string`

            - `file_type: "text" | "image" | "pdf"`

              - `"text"`

              - `"image"`

              - `"pdf"`

            - `num_lines: number | null`

            - `start_line: number | null`

            - `total_lines: number | null`

            - `type: "text_editor_code_execution_view_result"`

              - `"text_editor_code_execution_view_result"`

          - `TextEditorCodeExecutionCreateResultBlock`

            - `is_file_update: boolean`

            - `type: "text_editor_code_execution_create_result"`

              - `"text_editor_code_execution_create_result"`

          - `TextEditorCodeExecutionStrReplaceResultBlock`

            - `lines: Array<string> | null`

            - `new_lines: number | null`

            - `new_start: number | null`

            - `old_lines: number | null`

            - `old_start: number | null`

            - `type: "text_editor_code_execution_str_replace_result"`

              - `"text_editor_code_execution_str_replace_result"`

        - `tool_use_id: string`

        - `type: "text_editor_code_execution_tool_result"`

          - `"text_editor_code_execution_tool_result"`

      - `ToolSearchToolResultBlock`

        - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

          - `ToolSearchToolResultError`

            - `error_code: ToolSearchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `error_message: string | null`

            - `type: "tool_search_tool_result_error"`

              - `"tool_search_tool_result_error"`

          - `ToolSearchToolSearchResultBlock`

            - `tool_references: Array<ToolReferenceBlock>`

              - `tool_name: string`

              - `type: "tool_reference"`

                - `"tool_reference"`

            - `type: "tool_search_tool_search_result"`

              - `"tool_search_tool_search_result"`

        - `tool_use_id: string`

        - `type: "tool_search_tool_result"`

          - `"tool_search_tool_result"`

      - `ContainerUploadBlock`

        Response model for a file uploaded to the container.

        - `file_id: string`

        - `type: "container_upload"`

          - `"container_upload"`

    - `index: number`

    - `type: "content_block_start"`

      - `"content_block_start"`

  - `RawContentBlockDeltaEvent`

    - `delta: RawContentBlockDelta`

      - `TextDelta`

        - `text: string`

        - `type: "text_delta"`

          - `"text_delta"`

      - `InputJSONDelta`

        - `partial_json: string`

        - `type: "input_json_delta"`

          - `"input_json_delta"`

      - `CitationsDelta`

        - `citation: CitationCharLocation | CitationPageLocation | CitationContentBlockLocation | 2 more`

          - `CitationCharLocation`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_char_index: number`

            - `file_id: string | null`

            - `start_char_index: number`

            - `type: "char_location"`

              - `"char_location"`

          - `CitationPageLocation`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_page_number: number`

            - `file_id: string | null`

            - `start_page_number: number`

            - `type: "page_location"`

              - `"page_location"`

          - `CitationContentBlockLocation`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_block_index: number`

            - `file_id: string | null`

            - `start_block_index: number`

            - `type: "content_block_location"`

              - `"content_block_location"`

          - `CitationsWebSearchResultLocation`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string | null`

            - `type: "web_search_result_location"`

              - `"web_search_result_location"`

            - `url: string`

          - `CitationsSearchResultLocation`

            - `cited_text: string`

            - `end_block_index: number`

            - `search_result_index: number`

            - `source: string`

            - `start_block_index: number`

            - `title: string | null`

            - `type: "search_result_location"`

              - `"search_result_location"`

        - `type: "citations_delta"`

          - `"citations_delta"`

      - `ThinkingDelta`

        - `thinking: string`

        - `type: "thinking_delta"`

          - `"thinking_delta"`

      - `SignatureDelta`

        - `signature: string`

        - `type: "signature_delta"`

          - `"signature_delta"`

    - `index: number`

    - `type: "content_block_delta"`

      - `"content_block_delta"`

  - `RawContentBlockStopEvent`

    - `index: number`

    - `type: "content_block_stop"`

      - `"content_block_stop"`

### Redacted Thinking Block

- `RedactedThinkingBlock`

  - `data: string`

  - `type: "redacted_thinking"`

    - `"redacted_thinking"`

### Redacted Thinking Block Param

- `RedactedThinkingBlockParam`

  - `data: string`

  - `type: "redacted_thinking"`

    - `"redacted_thinking"`

### Search Result Block Param

- `SearchResultBlockParam`

  - `content: Array<TextBlockParam>`

    - `text: string`

    - `type: "text"`

      - `"text"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations?: Array<TextCitationParam> | null`

      - `CitationCharLocationParam`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_char_index: number`

        - `start_char_index: number`

        - `type: "char_location"`

          - `"char_location"`

      - `CitationPageLocationParam`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_page_number: number`

        - `start_page_number: number`

        - `type: "page_location"`

          - `"page_location"`

      - `CitationContentBlockLocationParam`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string | null`

        - `end_block_index: number`

        - `start_block_index: number`

        - `type: "content_block_location"`

          - `"content_block_location"`

      - `CitationWebSearchResultLocationParam`

        - `cited_text: string`

        - `encrypted_index: string`

        - `title: string | null`

        - `type: "web_search_result_location"`

          - `"web_search_result_location"`

        - `url: string`

      - `CitationSearchResultLocationParam`

        - `cited_text: string`

        - `end_block_index: number`

        - `search_result_index: number`

        - `source: string`

        - `start_block_index: number`

        - `title: string | null`

        - `type: "search_result_location"`

          - `"search_result_location"`

  - `source: string`

  - `title: string`

  - `type: "search_result"`

    - `"search_result"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `citations?: CitationsConfigParam`

    - `enabled?: boolean`

### Server Tool Caller

- `ServerToolCaller`

  Tool invocation generated by a server-side tool.

  - `tool_id: string`

  - `type: "code_execution_20250825"`

    - `"code_execution_20250825"`

### Server Tool Caller 20260120

- `ServerToolCaller20260120`

  - `tool_id: string`

  - `type: "code_execution_20260120"`

    - `"code_execution_20260120"`

### Server Tool Usage

- `ServerToolUsage`

  - `web_fetch_requests: number`

    The number of web fetch tool requests.

  - `web_search_requests: number`

    The number of web search tool requests.

### Server Tool Use Block

- `ServerToolUseBlock`

  - `id: string`

  - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

    Tool invocation directly from the model.

    - `DirectCaller`

      Tool invocation directly from the model.

      - `type: "direct"`

        - `"direct"`

    - `ServerToolCaller`

      Tool invocation generated by a server-side tool.

      - `tool_id: string`

      - `type: "code_execution_20250825"`

        - `"code_execution_20250825"`

    - `ServerToolCaller20260120`

      - `tool_id: string`

      - `type: "code_execution_20260120"`

        - `"code_execution_20260120"`

  - `input: Record<string, unknown>`

  - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

    - `"web_search"`

    - `"web_fetch"`

    - `"code_execution"`

    - `"bash_code_execution"`

    - `"text_editor_code_execution"`

    - `"tool_search_tool_regex"`

    - `"tool_search_tool_bm25"`

  - `type: "server_tool_use"`

    - `"server_tool_use"`

### Server Tool Use Block Param

- `ServerToolUseBlockParam`

  - `id: string`

  - `input: Record<string, unknown>`

  - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

    - `"web_search"`

    - `"web_fetch"`

    - `"code_execution"`

    - `"bash_code_execution"`

    - `"text_editor_code_execution"`

    - `"tool_search_tool_regex"`

    - `"tool_search_tool_bm25"`

  - `type: "server_tool_use"`

    - `"server_tool_use"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

    Tool invocation directly from the model.

    - `DirectCaller`

      Tool invocation directly from the model.

      - `type: "direct"`

        - `"direct"`

    - `ServerToolCaller`

      Tool invocation generated by a server-side tool.

      - `tool_id: string`

      - `type: "code_execution_20250825"`

        - `"code_execution_20250825"`

    - `ServerToolCaller20260120`

      - `tool_id: string`

      - `type: "code_execution_20260120"`

        - `"code_execution_20260120"`

### Signature Delta

- `SignatureDelta`

  - `signature: string`

  - `type: "signature_delta"`

    - `"signature_delta"`

### Stop Reason

- `StopReason = "end_turn" | "max_tokens" | "stop_sequence" | 3 more`

  - `"end_turn"`

  - `"max_tokens"`

  - `"stop_sequence"`

  - `"tool_use"`

  - `"pause_turn"`

  - `"refusal"`

### Text Block

- `TextBlock`

  - `citations: Array<TextCitation> | null`

    Citations supporting the text block.

    The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

    - `CitationCharLocation`

      - `cited_text: string`

      - `document_index: number`

      - `document_title: string | null`

      - `end_char_index: number`

      - `file_id: string | null`

      - `start_char_index: number`

      - `type: "char_location"`

        - `"char_location"`

    - `CitationPageLocation`

      - `cited_text: string`

      - `document_index: number`

      - `document_title: string | null`

      - `end_page_number: number`

      - `file_id: string | null`

      - `start_page_number: number`

      - `type: "page_location"`

        - `"page_location"`

    - `CitationContentBlockLocation`

      - `cited_text: string`

      - `document_index: number`

      - `document_title: string | null`

      - `end_block_index: number`

      - `file_id: string | null`

      - `start_block_index: number`

      - `type: "content_block_location"`

        - `"content_block_location"`

    - `CitationsWebSearchResultLocation`

      - `cited_text: string`

      - `encrypted_index: string`

      - `title: string | null`

      - `type: "web_search_result_location"`

        - `"web_search_result_location"`

      - `url: string`

    - `CitationsSearchResultLocation`

      - `cited_text: string`

      - `end_block_index: number`

      - `search_result_index: number`

      - `source: string`

      - `start_block_index: number`

      - `title: string | null`

      - `type: "search_result_location"`

        - `"search_result_location"`

  - `text: string`

  - `type: "text"`

    - `"text"`

### Text Block Param

- `TextBlockParam`

  - `text: string`

  - `type: "text"`

    - `"text"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `citations?: Array<TextCitationParam> | null`

    - `CitationCharLocationParam`

      - `cited_text: string`

      - `document_index: number`

      - `document_title: string | null`

      - `end_char_index: number`

      - `start_char_index: number`

      - `type: "char_location"`

        - `"char_location"`

    - `CitationPageLocationParam`

      - `cited_text: string`

      - `document_index: number`

      - `document_title: string | null`

      - `end_page_number: number`

      - `start_page_number: number`

      - `type: "page_location"`

        - `"page_location"`

    - `CitationContentBlockLocationParam`

      - `cited_text: string`

      - `document_index: number`

      - `document_title: string | null`

      - `end_block_index: number`

      - `start_block_index: number`

      - `type: "content_block_location"`

        - `"content_block_location"`

    - `CitationWebSearchResultLocationParam`

      - `cited_text: string`

      - `encrypted_index: string`

      - `title: string | null`

      - `type: "web_search_result_location"`

        - `"web_search_result_location"`

      - `url: string`

    - `CitationSearchResultLocationParam`

      - `cited_text: string`

      - `end_block_index: number`

      - `search_result_index: number`

      - `source: string`

      - `start_block_index: number`

      - `title: string | null`

      - `type: "search_result_location"`

        - `"search_result_location"`

### Text Citation

- `TextCitation = CitationCharLocation | CitationPageLocation | CitationContentBlockLocation | 2 more`

  - `CitationCharLocation`

    - `cited_text: string`

    - `document_index: number`

    - `document_title: string | null`

    - `end_char_index: number`

    - `file_id: string | null`

    - `start_char_index: number`

    - `type: "char_location"`

      - `"char_location"`

  - `CitationPageLocation`

    - `cited_text: string`

    - `document_index: number`

    - `document_title: string | null`

    - `end_page_number: number`

    - `file_id: string | null`

    - `start_page_number: number`

    - `type: "page_location"`

      - `"page_location"`

  - `CitationContentBlockLocation`

    - `cited_text: string`

    - `document_index: number`

    - `document_title: string | null`

    - `end_block_index: number`

    - `file_id: string | null`

    - `start_block_index: number`

    - `type: "content_block_location"`

      - `"content_block_location"`

  - `CitationsWebSearchResultLocation`

    - `cited_text: string`

    - `encrypted_index: string`

    - `title: string | null`

    - `type: "web_search_result_location"`

      - `"web_search_result_location"`

    - `url: string`

  - `CitationsSearchResultLocation`

    - `cited_text: string`

    - `end_block_index: number`

    - `search_result_index: number`

    - `source: string`

    - `start_block_index: number`

    - `title: string | null`

    - `type: "search_result_location"`

      - `"search_result_location"`

### Text Citation Param

- `TextCitationParam = CitationCharLocationParam | CitationPageLocationParam | CitationContentBlockLocationParam | 2 more`

  - `CitationCharLocationParam`

    - `cited_text: string`

    - `document_index: number`

    - `document_title: string | null`

    - `end_char_index: number`

    - `start_char_index: number`

    - `type: "char_location"`

      - `"char_location"`

  - `CitationPageLocationParam`

    - `cited_text: string`

    - `document_index: number`

    - `document_title: string | null`

    - `end_page_number: number`

    - `start_page_number: number`

    - `type: "page_location"`

      - `"page_location"`

  - `CitationContentBlockLocationParam`

    - `cited_text: string`

    - `document_index: number`

    - `document_title: string | null`

    - `end_block_index: number`

    - `start_block_index: number`

    - `type: "content_block_location"`

      - `"content_block_location"`

  - `CitationWebSearchResultLocationParam`

    - `cited_text: string`

    - `encrypted_index: string`

    - `title: string | null`

    - `type: "web_search_result_location"`

      - `"web_search_result_location"`

    - `url: string`

  - `CitationSearchResultLocationParam`

    - `cited_text: string`

    - `end_block_index: number`

    - `search_result_index: number`

    - `source: string`

    - `start_block_index: number`

    - `title: string | null`

    - `type: "search_result_location"`

      - `"search_result_location"`

### Text Delta

- `TextDelta`

  - `text: string`

  - `type: "text_delta"`

    - `"text_delta"`

### Text Editor Code Execution Create Result Block

- `TextEditorCodeExecutionCreateResultBlock`

  - `is_file_update: boolean`

  - `type: "text_editor_code_execution_create_result"`

    - `"text_editor_code_execution_create_result"`

### Text Editor Code Execution Create Result Block Param

- `TextEditorCodeExecutionCreateResultBlockParam`

  - `is_file_update: boolean`

  - `type: "text_editor_code_execution_create_result"`

    - `"text_editor_code_execution_create_result"`

### Text Editor Code Execution Str Replace Result Block

- `TextEditorCodeExecutionStrReplaceResultBlock`

  - `lines: Array<string> | null`

  - `new_lines: number | null`

  - `new_start: number | null`

  - `old_lines: number | null`

  - `old_start: number | null`

  - `type: "text_editor_code_execution_str_replace_result"`

    - `"text_editor_code_execution_str_replace_result"`

### Text Editor Code Execution Str Replace Result Block Param

- `TextEditorCodeExecutionStrReplaceResultBlockParam`

  - `type: "text_editor_code_execution_str_replace_result"`

    - `"text_editor_code_execution_str_replace_result"`

  - `lines?: Array<string> | null`

  - `new_lines?: number | null`

  - `new_start?: number | null`

  - `old_lines?: number | null`

  - `old_start?: number | null`

### Text Editor Code Execution Tool Result Block

- `TextEditorCodeExecutionToolResultBlock`

  - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

    - `TextEditorCodeExecutionToolResultError`

      - `error_code: TextEditorCodeExecutionToolResultErrorCode`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

        - `"file_not_found"`

      - `error_message: string | null`

      - `type: "text_editor_code_execution_tool_result_error"`

        - `"text_editor_code_execution_tool_result_error"`

    - `TextEditorCodeExecutionViewResultBlock`

      - `content: string`

      - `file_type: "text" | "image" | "pdf"`

        - `"text"`

        - `"image"`

        - `"pdf"`

      - `num_lines: number | null`

      - `start_line: number | null`

      - `total_lines: number | null`

      - `type: "text_editor_code_execution_view_result"`

        - `"text_editor_code_execution_view_result"`

    - `TextEditorCodeExecutionCreateResultBlock`

      - `is_file_update: boolean`

      - `type: "text_editor_code_execution_create_result"`

        - `"text_editor_code_execution_create_result"`

    - `TextEditorCodeExecutionStrReplaceResultBlock`

      - `lines: Array<string> | null`

      - `new_lines: number | null`

      - `new_start: number | null`

      - `old_lines: number | null`

      - `old_start: number | null`

      - `type: "text_editor_code_execution_str_replace_result"`

        - `"text_editor_code_execution_str_replace_result"`

  - `tool_use_id: string`

  - `type: "text_editor_code_execution_tool_result"`

    - `"text_editor_code_execution_tool_result"`

### Text Editor Code Execution Tool Result Block Param

- `TextEditorCodeExecutionToolResultBlockParam`

  - `content: TextEditorCodeExecutionToolResultErrorParam | TextEditorCodeExecutionViewResultBlockParam | TextEditorCodeExecutionCreateResultBlockParam | TextEditorCodeExecutionStrReplaceResultBlockParam`

    - `TextEditorCodeExecutionToolResultErrorParam`

      - `error_code: TextEditorCodeExecutionToolResultErrorCode`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

        - `"file_not_found"`

      - `type: "text_editor_code_execution_tool_result_error"`

        - `"text_editor_code_execution_tool_result_error"`

      - `error_message?: string | null`

    - `TextEditorCodeExecutionViewResultBlockParam`

      - `content: string`

      - `file_type: "text" | "image" | "pdf"`

        - `"text"`

        - `"image"`

        - `"pdf"`

      - `type: "text_editor_code_execution_view_result"`

        - `"text_editor_code_execution_view_result"`

      - `num_lines?: number | null`

      - `start_line?: number | null`

      - `total_lines?: number | null`

    - `TextEditorCodeExecutionCreateResultBlockParam`

      - `is_file_update: boolean`

      - `type: "text_editor_code_execution_create_result"`

        - `"text_editor_code_execution_create_result"`

    - `TextEditorCodeExecutionStrReplaceResultBlockParam`

      - `type: "text_editor_code_execution_str_replace_result"`

        - `"text_editor_code_execution_str_replace_result"`

      - `lines?: Array<string> | null`

      - `new_lines?: number | null`

      - `new_start?: number | null`

      - `old_lines?: number | null`

      - `old_start?: number | null`

  - `tool_use_id: string`

  - `type: "text_editor_code_execution_tool_result"`

    - `"text_editor_code_execution_tool_result"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Text Editor Code Execution Tool Result Error

- `TextEditorCodeExecutionToolResultError`

  - `error_code: TextEditorCodeExecutionToolResultErrorCode`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

    - `"file_not_found"`

  - `error_message: string | null`

  - `type: "text_editor_code_execution_tool_result_error"`

    - `"text_editor_code_execution_tool_result_error"`

### Text Editor Code Execution Tool Result Error Code

- `TextEditorCodeExecutionToolResultErrorCode = "invalid_tool_input" | "unavailable" | "too_many_requests" | 2 more`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

  - `"file_not_found"`

### Text Editor Code Execution Tool Result Error Param

- `TextEditorCodeExecutionToolResultErrorParam`

  - `error_code: TextEditorCodeExecutionToolResultErrorCode`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

    - `"file_not_found"`

  - `type: "text_editor_code_execution_tool_result_error"`

    - `"text_editor_code_execution_tool_result_error"`

  - `error_message?: string | null`

### Text Editor Code Execution View Result Block

- `TextEditorCodeExecutionViewResultBlock`

  - `content: string`

  - `file_type: "text" | "image" | "pdf"`

    - `"text"`

    - `"image"`

    - `"pdf"`

  - `num_lines: number | null`

  - `start_line: number | null`

  - `total_lines: number | null`

  - `type: "text_editor_code_execution_view_result"`

    - `"text_editor_code_execution_view_result"`

### Text Editor Code Execution View Result Block Param

- `TextEditorCodeExecutionViewResultBlockParam`

  - `content: string`

  - `file_type: "text" | "image" | "pdf"`

    - `"text"`

    - `"image"`

    - `"pdf"`

  - `type: "text_editor_code_execution_view_result"`

    - `"text_editor_code_execution_view_result"`

  - `num_lines?: number | null`

  - `start_line?: number | null`

  - `total_lines?: number | null`

### Thinking Block

- `ThinkingBlock`

  - `signature: string`

  - `thinking: string`

  - `type: "thinking"`

    - `"thinking"`

### Thinking Block Param

- `ThinkingBlockParam`

  - `signature: string`

  - `thinking: string`

  - `type: "thinking"`

    - `"thinking"`

### Thinking Config Adaptive

- `ThinkingConfigAdaptive`

  - `type: "adaptive"`

    - `"adaptive"`

### Thinking Config Disabled

- `ThinkingConfigDisabled`

  - `type: "disabled"`

    - `"disabled"`

### Thinking Config Enabled

- `ThinkingConfigEnabled`

  - `budget_tokens: number`

    Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

    Must be ≥1024 and less than `max_tokens`.

    See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

  - `type: "enabled"`

    - `"enabled"`

### Thinking Config Param

- `ThinkingConfigParam = ThinkingConfigEnabled | ThinkingConfigDisabled | ThinkingConfigAdaptive`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

  - `ThinkingConfigEnabled`

    - `budget_tokens: number`

      Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

      Must be ≥1024 and less than `max_tokens`.

      See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

    - `type: "enabled"`

      - `"enabled"`

  - `ThinkingConfigDisabled`

    - `type: "disabled"`

      - `"disabled"`

  - `ThinkingConfigAdaptive`

    - `type: "adaptive"`

      - `"adaptive"`

### Thinking Delta

- `ThinkingDelta`

  - `thinking: string`

  - `type: "thinking_delta"`

    - `"thinking_delta"`

### Tool

- `Tool`

  - `input_schema: InputSchema`

    [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

    This defines the shape of the `input` that your tool accepts and that the model will produce.

    - `type: "object"`

      - `"object"`

    - `properties?: Record<string, unknown> | null`

    - `required?: Array<string> | null`

  - `name: string`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `description?: string`

    Description of what this tool does.

    Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

  - `eager_input_streaming?: boolean | null`

    Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

  - `input_examples?: Array<Record<string, unknown>>`

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

  - `type?: "custom" | null`

    - `"custom"`

### Tool Bash 20250124

- `ToolBash20250124`

  - `name: "bash"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"bash"`

  - `type: "bash_20250124"`

    - `"bash_20250124"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples?: Array<Record<string, unknown>>`

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

### Tool Choice

- `ToolChoice = ToolChoiceAuto | ToolChoiceAny | ToolChoiceTool | ToolChoiceNone`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `ToolChoiceAuto`

    The model will automatically decide whether to use tools.

    - `type: "auto"`

      - `"auto"`

    - `disable_parallel_tool_use?: boolean`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output at most one tool use.

  - `ToolChoiceAny`

    The model will use any available tools.

    - `type: "any"`

      - `"any"`

    - `disable_parallel_tool_use?: boolean`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `ToolChoiceTool`

    The model will use the specified tool with `tool_choice.name`.

    - `name: string`

      The name of the tool to use.

    - `type: "tool"`

      - `"tool"`

    - `disable_parallel_tool_use?: boolean`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `ToolChoiceNone`

    The model will not be allowed to use tools.

    - `type: "none"`

      - `"none"`

### Tool Choice Any

- `ToolChoiceAny`

  The model will use any available tools.

  - `type: "any"`

    - `"any"`

  - `disable_parallel_tool_use?: boolean`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Choice Auto

- `ToolChoiceAuto`

  The model will automatically decide whether to use tools.

  - `type: "auto"`

    - `"auto"`

  - `disable_parallel_tool_use?: boolean`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output at most one tool use.

### Tool Choice None

- `ToolChoiceNone`

  The model will not be allowed to use tools.

  - `type: "none"`

    - `"none"`

### Tool Choice Tool

- `ToolChoiceTool`

  The model will use the specified tool with `tool_choice.name`.

  - `name: string`

    The name of the tool to use.

  - `type: "tool"`

    - `"tool"`

  - `disable_parallel_tool_use?: boolean`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Reference Block

- `ToolReferenceBlock`

  - `tool_name: string`

  - `type: "tool_reference"`

    - `"tool_reference"`

### Tool Reference Block Param

- `ToolReferenceBlockParam`

  Tool reference block that can be included in tool_result content.

  - `tool_name: string`

  - `type: "tool_reference"`

    - `"tool_reference"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Tool Result Block Param

- `ToolResultBlockParam`

  - `tool_use_id: string`

  - `type: "tool_result"`

    - `"tool_result"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `content?: string | Array<TextBlockParam | ImageBlockParam | SearchResultBlockParam | 2 more>`

    - `string`

    - `Array<TextBlockParam | ImageBlockParam | SearchResultBlockParam | 2 more>`

      - `TextBlockParam`

        - `text: string`

        - `type: "text"`

          - `"text"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations?: Array<TextCitationParam> | null`

          - `CitationCharLocationParam`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_char_index: number`

            - `start_char_index: number`

            - `type: "char_location"`

              - `"char_location"`

          - `CitationPageLocationParam`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_page_number: number`

            - `start_page_number: number`

            - `type: "page_location"`

              - `"page_location"`

          - `CitationContentBlockLocationParam`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_block_index: number`

            - `start_block_index: number`

            - `type: "content_block_location"`

              - `"content_block_location"`

          - `CitationWebSearchResultLocationParam`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string | null`

            - `type: "web_search_result_location"`

              - `"web_search_result_location"`

            - `url: string`

          - `CitationSearchResultLocationParam`

            - `cited_text: string`

            - `end_block_index: number`

            - `search_result_index: number`

            - `source: string`

            - `start_block_index: number`

            - `title: string | null`

            - `type: "search_result_location"`

              - `"search_result_location"`

      - `ImageBlockParam`

        - `source: Base64ImageSource | URLImageSource`

          - `Base64ImageSource`

            - `data: string`

            - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

              - `"image/jpeg"`

              - `"image/png"`

              - `"image/gif"`

              - `"image/webp"`

            - `type: "base64"`

              - `"base64"`

          - `URLImageSource`

            - `type: "url"`

              - `"url"`

            - `url: string`

        - `type: "image"`

          - `"image"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `SearchResultBlockParam`

        - `content: Array<TextBlockParam>`

          - `text: string`

          - `type: "text"`

            - `"text"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations?: Array<TextCitationParam> | null`

            - `CitationCharLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_char_index: number`

              - `start_char_index: number`

              - `type: "char_location"`

                - `"char_location"`

            - `CitationPageLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_page_number: number`

              - `start_page_number: number`

              - `type: "page_location"`

                - `"page_location"`

            - `CitationContentBlockLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_block_index: number`

              - `start_block_index: number`

              - `type: "content_block_location"`

                - `"content_block_location"`

            - `CitationWebSearchResultLocationParam`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string | null`

              - `type: "web_search_result_location"`

                - `"web_search_result_location"`

              - `url: string`

            - `CitationSearchResultLocationParam`

              - `cited_text: string`

              - `end_block_index: number`

              - `search_result_index: number`

              - `source: string`

              - `start_block_index: number`

              - `title: string | null`

              - `type: "search_result_location"`

                - `"search_result_location"`

        - `source: string`

        - `title: string`

        - `type: "search_result"`

          - `"search_result"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations?: CitationsConfigParam`

          - `enabled?: boolean`

      - `DocumentBlockParam`

        - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

          - `Base64PDFSource`

            - `data: string`

            - `media_type: "application/pdf"`

              - `"application/pdf"`

            - `type: "base64"`

              - `"base64"`

          - `PlainTextSource`

            - `data: string`

            - `media_type: "text/plain"`

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `ContentBlockSource`

            - `content: string | Array<ContentBlockSourceContent>`

              - `string`

              - `Array<ContentBlockSourceContent>`

                - `TextBlockParam`

                  - `text: string`

                  - `type: "text"`

                    - `"text"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

                  - `citations?: Array<TextCitationParam> | null`

                    - `CitationCharLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_char_index: number`

                      - `start_char_index: number`

                      - `type: "char_location"`

                        - `"char_location"`

                    - `CitationPageLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_page_number: number`

                      - `start_page_number: number`

                      - `type: "page_location"`

                        - `"page_location"`

                    - `CitationContentBlockLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_block_index: number`

                      - `start_block_index: number`

                      - `type: "content_block_location"`

                        - `"content_block_location"`

                    - `CitationWebSearchResultLocationParam`

                      - `cited_text: string`

                      - `encrypted_index: string`

                      - `title: string | null`

                      - `type: "web_search_result_location"`

                        - `"web_search_result_location"`

                      - `url: string`

                    - `CitationSearchResultLocationParam`

                      - `cited_text: string`

                      - `end_block_index: number`

                      - `search_result_index: number`

                      - `source: string`

                      - `start_block_index: number`

                      - `title: string | null`

                      - `type: "search_result_location"`

                        - `"search_result_location"`

                - `ImageBlockParam`

                  - `source: Base64ImageSource | URLImageSource`

                    - `Base64ImageSource`

                      - `data: string`

                      - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                        - `"image/jpeg"`

                        - `"image/png"`

                        - `"image/gif"`

                        - `"image/webp"`

                      - `type: "base64"`

                        - `"base64"`

                    - `URLImageSource`

                      - `type: "url"`

                        - `"url"`

                      - `url: string`

                  - `type: "image"`

                    - `"image"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

            - `type: "content"`

              - `"content"`

          - `URLPDFSource`

            - `type: "url"`

              - `"url"`

            - `url: string`

        - `type: "document"`

          - `"document"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations?: CitationsConfigParam | null`

          - `enabled?: boolean`

        - `context?: string | null`

        - `title?: string | null`

      - `ToolReferenceBlockParam`

        Tool reference block that can be included in tool_result content.

        - `tool_name: string`

        - `type: "tool_reference"`

          - `"tool_reference"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

  - `is_error?: boolean`

### Tool Search Tool Bm25 20251119

- `ToolSearchToolBm25_20251119`

  - `name: "tool_search_tool_bm25"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"tool_search_tool_bm25"`

  - `type: "tool_search_tool_bm25_20251119" | "tool_search_tool_bm25"`

    - `"tool_search_tool_bm25_20251119"`

    - `"tool_search_tool_bm25"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Regex 20251119

- `ToolSearchToolRegex20251119`

  - `name: "tool_search_tool_regex"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"tool_search_tool_regex"`

  - `type: "tool_search_tool_regex_20251119" | "tool_search_tool_regex"`

    - `"tool_search_tool_regex_20251119"`

    - `"tool_search_tool_regex"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Result Block

- `ToolSearchToolResultBlock`

  - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

    - `ToolSearchToolResultError`

      - `error_code: ToolSearchToolResultErrorCode`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

      - `error_message: string | null`

      - `type: "tool_search_tool_result_error"`

        - `"tool_search_tool_result_error"`

    - `ToolSearchToolSearchResultBlock`

      - `tool_references: Array<ToolReferenceBlock>`

        - `tool_name: string`

        - `type: "tool_reference"`

          - `"tool_reference"`

      - `type: "tool_search_tool_search_result"`

        - `"tool_search_tool_search_result"`

  - `tool_use_id: string`

  - `type: "tool_search_tool_result"`

    - `"tool_search_tool_result"`

### Tool Search Tool Result Block Param

- `ToolSearchToolResultBlockParam`

  - `content: ToolSearchToolResultErrorParam | ToolSearchToolSearchResultBlockParam`

    - `ToolSearchToolResultErrorParam`

      - `error_code: ToolSearchToolResultErrorCode`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

      - `type: "tool_search_tool_result_error"`

        - `"tool_search_tool_result_error"`

    - `ToolSearchToolSearchResultBlockParam`

      - `tool_references: Array<ToolReferenceBlockParam>`

        - `tool_name: string`

        - `type: "tool_reference"`

          - `"tool_reference"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `type: "tool_search_tool_search_result"`

        - `"tool_search_tool_search_result"`

  - `tool_use_id: string`

  - `type: "tool_search_tool_result"`

    - `"tool_search_tool_result"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Tool Search Tool Result Error

- `ToolSearchToolResultError`

  - `error_code: ToolSearchToolResultErrorCode`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

  - `error_message: string | null`

  - `type: "tool_search_tool_result_error"`

    - `"tool_search_tool_result_error"`

### Tool Search Tool Result Error Code

- `ToolSearchToolResultErrorCode = "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded"`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

### Tool Search Tool Result Error Param

- `ToolSearchToolResultErrorParam`

  - `error_code: ToolSearchToolResultErrorCode`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

  - `type: "tool_search_tool_result_error"`

    - `"tool_search_tool_result_error"`

### Tool Search Tool Search Result Block

- `ToolSearchToolSearchResultBlock`

  - `tool_references: Array<ToolReferenceBlock>`

    - `tool_name: string`

    - `type: "tool_reference"`

      - `"tool_reference"`

  - `type: "tool_search_tool_search_result"`

    - `"tool_search_tool_search_result"`

### Tool Search Tool Search Result Block Param

- `ToolSearchToolSearchResultBlockParam`

  - `tool_references: Array<ToolReferenceBlockParam>`

    - `tool_name: string`

    - `type: "tool_reference"`

      - `"tool_reference"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `type: "tool_search_tool_search_result"`

    - `"tool_search_tool_search_result"`

### Tool Text Editor 20250124

- `ToolTextEditor20250124`

  - `name: "str_replace_editor"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"str_replace_editor"`

  - `type: "text_editor_20250124"`

    - `"text_editor_20250124"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples?: Array<Record<string, unknown>>`

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250429

- `ToolTextEditor20250429`

  - `name: "str_replace_based_edit_tool"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"str_replace_based_edit_tool"`

  - `type: "text_editor_20250429"`

    - `"text_editor_20250429"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples?: Array<Record<string, unknown>>`

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250728

- `ToolTextEditor20250728`

  - `name: "str_replace_based_edit_tool"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"str_replace_based_edit_tool"`

  - `type: "text_editor_20250728"`

    - `"text_editor_20250728"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples?: Array<Record<string, unknown>>`

  - `max_characters?: number | null`

    Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

### Tool Union

- `ToolUnion = Tool | ToolBash20250124 | CodeExecutionTool20250522 | 12 more`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `Tool`

    - `input_schema: InputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

      - `type: "object"`

        - `"object"`

      - `properties?: Record<string, unknown> | null`

      - `required?: Array<string> | null`

    - `name: string`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `description?: string`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `eager_input_streaming?: boolean | null`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `input_examples?: Array<Record<string, unknown>>`

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

    - `type?: "custom" | null`

      - `"custom"`

  - `ToolBash20250124`

    - `name: "bash"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"bash"`

    - `type: "bash_20250124"`

      - `"bash_20250124"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples?: Array<Record<string, unknown>>`

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250522`

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"code_execution"`

    - `type: "code_execution_20250522"`

      - `"code_execution_20250522"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250825`

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"code_execution"`

    - `type: "code_execution_20250825"`

      - `"code_execution_20250825"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20260120`

    Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"code_execution"`

    - `type: "code_execution_20260120"`

      - `"code_execution_20260120"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `MemoryTool20250818`

    - `name: "memory"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"memory"`

    - `type: "memory_20250818"`

      - `"memory_20250818"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples?: Array<Record<string, unknown>>`

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250124`

    - `name: "str_replace_editor"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"str_replace_editor"`

    - `type: "text_editor_20250124"`

      - `"text_editor_20250124"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples?: Array<Record<string, unknown>>`

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250429`

    - `name: "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"str_replace_based_edit_tool"`

    - `type: "text_editor_20250429"`

      - `"text_editor_20250429"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples?: Array<Record<string, unknown>>`

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250728`

    - `name: "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"str_replace_based_edit_tool"`

    - `type: "text_editor_20250728"`

      - `"text_editor_20250728"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples?: Array<Record<string, unknown>>`

    - `max_characters?: number | null`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20250305`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_search"`

    - `type: "web_search_20250305"`

      - `"web_search_20250305"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains?: Array<string> | null`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains?: Array<string> | null`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses?: number | null`

      Maximum number of times the tool can be used in the API request.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location?: UserLocation | null`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: "approximate"`

        - `"approximate"`

      - `city?: string | null`

        The city of the user.

      - `country?: string | null`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      - `region?: string | null`

        The region of the user.

      - `timezone?: string | null`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

  - `WebFetchTool20250910`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_fetch"`

    - `type: "web_fetch_20250910"`

      - `"web_fetch_20250910"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains?: Array<string> | null`

      List of domains to allow fetching from

    - `blocked_domains?: Array<string> | null`

      List of domains to block fetching from

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations?: CitationsConfigParam | null`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled?: boolean`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens?: number | null`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `max_uses?: number | null`

      Maximum number of times the tool can be used in the API request.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20260209`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_search"`

    - `type: "web_search_20260209"`

      - `"web_search_20260209"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains?: Array<string> | null`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains?: Array<string> | null`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses?: number | null`

      Maximum number of times the tool can be used in the API request.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location?: UserLocation | null`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: "approximate"`

        - `"approximate"`

      - `city?: string | null`

        The city of the user.

      - `country?: string | null`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      - `region?: string | null`

        The region of the user.

      - `timezone?: string | null`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

  - `WebFetchTool20260209`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_fetch"`

    - `type: "web_fetch_20260209"`

      - `"web_fetch_20260209"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains?: Array<string> | null`

      List of domains to allow fetching from

    - `blocked_domains?: Array<string> | null`

      List of domains to block fetching from

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations?: CitationsConfigParam | null`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled?: boolean`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens?: number | null`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `max_uses?: number | null`

      Maximum number of times the tool can be used in the API request.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ToolSearchToolBm25_20251119`

    - `name: "tool_search_tool_bm25"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"tool_search_tool_bm25"`

    - `type: "tool_search_tool_bm25_20251119" | "tool_search_tool_bm25"`

      - `"tool_search_tool_bm25_20251119"`

      - `"tool_search_tool_bm25"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ToolSearchToolRegex20251119`

    - `name: "tool_search_tool_regex"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"tool_search_tool_regex"`

    - `type: "tool_search_tool_regex_20251119" | "tool_search_tool_regex"`

      - `"tool_search_tool_regex_20251119"`

      - `"tool_search_tool_regex"`

    - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading?: boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict?: boolean`

      When true, guarantees schema validation on tool names and inputs

### Tool Use Block

- `ToolUseBlock`

  - `id: string`

  - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

    Tool invocation directly from the model.

    - `DirectCaller`

      Tool invocation directly from the model.

      - `type: "direct"`

        - `"direct"`

    - `ServerToolCaller`

      Tool invocation generated by a server-side tool.

      - `tool_id: string`

      - `type: "code_execution_20250825"`

        - `"code_execution_20250825"`

    - `ServerToolCaller20260120`

      - `tool_id: string`

      - `type: "code_execution_20260120"`

        - `"code_execution_20260120"`

  - `input: Record<string, unknown>`

  - `name: string`

  - `type: "tool_use"`

    - `"tool_use"`

### Tool Use Block Param

- `ToolUseBlockParam`

  - `id: string`

  - `input: Record<string, unknown>`

  - `name: string`

  - `type: "tool_use"`

    - `"tool_use"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

    Tool invocation directly from the model.

    - `DirectCaller`

      Tool invocation directly from the model.

      - `type: "direct"`

        - `"direct"`

    - `ServerToolCaller`

      Tool invocation generated by a server-side tool.

      - `tool_id: string`

      - `type: "code_execution_20250825"`

        - `"code_execution_20250825"`

    - `ServerToolCaller20260120`

      - `tool_id: string`

      - `type: "code_execution_20260120"`

        - `"code_execution_20260120"`

### URL Image Source

- `URLImageSource`

  - `type: "url"`

    - `"url"`

  - `url: string`

### URL PDF Source

- `URLPDFSource`

  - `type: "url"`

    - `"url"`

  - `url: string`

### Usage

- `Usage`

  - `cache_creation: CacheCreation | null`

    Breakdown of cached tokens by TTL

    - `ephemeral_1h_input_tokens: number`

      The number of input tokens used to create the 1 hour cache entry.

    - `ephemeral_5m_input_tokens: number`

      The number of input tokens used to create the 5 minute cache entry.

  - `cache_creation_input_tokens: number | null`

    The number of input tokens used to create the cache entry.

  - `cache_read_input_tokens: number | null`

    The number of input tokens read from the cache.

  - `inference_geo: string | null`

    The geographic region where inference was performed for this request.

  - `input_tokens: number`

    The number of input tokens which were used.

  - `output_tokens: number`

    The number of output tokens which were used.

  - `server_tool_use: ServerToolUsage | null`

    The number of server tool requests.

    - `web_fetch_requests: number`

      The number of web fetch tool requests.

    - `web_search_requests: number`

      The number of web search tool requests.

  - `service_tier: "standard" | "priority" | "batch" | null`

    If the request used the priority, standard, or batch tier.

    - `"standard"`

    - `"priority"`

    - `"batch"`

### User Location

- `UserLocation`

  - `type: "approximate"`

    - `"approximate"`

  - `city?: string | null`

    The city of the user.

  - `country?: string | null`

    The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

  - `region?: string | null`

    The region of the user.

  - `timezone?: string | null`

    The [IANA timezone](https://nodatime.org/TimeZones) of the user.

### Web Fetch Block

- `WebFetchBlock`

  - `content: DocumentBlock`

    - `citations: CitationsConfig | null`

      Citation configuration for the document

      - `enabled: boolean`

    - `source: Base64PDFSource | PlainTextSource`

      - `Base64PDFSource`

        - `data: string`

        - `media_type: "application/pdf"`

          - `"application/pdf"`

        - `type: "base64"`

          - `"base64"`

      - `PlainTextSource`

        - `data: string`

        - `media_type: "text/plain"`

          - `"text/plain"`

        - `type: "text"`

          - `"text"`

    - `title: string | null`

      The title of the document

    - `type: "document"`

      - `"document"`

  - `retrieved_at: string | null`

    ISO 8601 timestamp when the content was retrieved

  - `type: "web_fetch_result"`

    - `"web_fetch_result"`

  - `url: string`

    Fetched content URL

### Web Fetch Block Param

- `WebFetchBlockParam`

  - `content: DocumentBlockParam`

    - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

      - `Base64PDFSource`

        - `data: string`

        - `media_type: "application/pdf"`

          - `"application/pdf"`

        - `type: "base64"`

          - `"base64"`

      - `PlainTextSource`

        - `data: string`

        - `media_type: "text/plain"`

          - `"text/plain"`

        - `type: "text"`

          - `"text"`

      - `ContentBlockSource`

        - `content: string | Array<ContentBlockSourceContent>`

          - `string`

          - `Array<ContentBlockSourceContent>`

            - `TextBlockParam`

              - `text: string`

              - `type: "text"`

                - `"text"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations?: Array<TextCitationParam> | null`

                - `CitationCharLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_char_index: number`

                  - `start_char_index: number`

                  - `type: "char_location"`

                    - `"char_location"`

                - `CitationPageLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_page_number: number`

                  - `start_page_number: number`

                  - `type: "page_location"`

                    - `"page_location"`

                - `CitationContentBlockLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_block_index: number`

                  - `start_block_index: number`

                  - `type: "content_block_location"`

                    - `"content_block_location"`

                - `CitationWebSearchResultLocationParam`

                  - `cited_text: string`

                  - `encrypted_index: string`

                  - `title: string | null`

                  - `type: "web_search_result_location"`

                    - `"web_search_result_location"`

                  - `url: string`

                - `CitationSearchResultLocationParam`

                  - `cited_text: string`

                  - `end_block_index: number`

                  - `search_result_index: number`

                  - `source: string`

                  - `start_block_index: number`

                  - `title: string | null`

                  - `type: "search_result_location"`

                    - `"search_result_location"`

            - `ImageBlockParam`

              - `source: Base64ImageSource | URLImageSource`

                - `Base64ImageSource`

                  - `data: string`

                  - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                    - `"image/jpeg"`

                    - `"image/png"`

                    - `"image/gif"`

                    - `"image/webp"`

                  - `type: "base64"`

                    - `"base64"`

                - `URLImageSource`

                  - `type: "url"`

                    - `"url"`

                  - `url: string`

              - `type: "image"`

                - `"image"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

        - `type: "content"`

          - `"content"`

      - `URLPDFSource`

        - `type: "url"`

          - `"url"`

        - `url: string`

    - `type: "document"`

      - `"document"`

    - `cache_control?: CacheControlEphemeral | null`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

        - `"ephemeral"`

      - `ttl?: "5m" | "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations?: CitationsConfigParam | null`

      - `enabled?: boolean`

    - `context?: string | null`

    - `title?: string | null`

  - `type: "web_fetch_result"`

    - `"web_fetch_result"`

  - `url: string`

    Fetched content URL

  - `retrieved_at?: string | null`

    ISO 8601 timestamp when the content was retrieved

### Web Fetch Tool 20250910

- `WebFetchTool20250910`

  - `name: "web_fetch"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch"`

  - `type: "web_fetch_20250910"`

    - `"web_fetch_20250910"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `allowed_domains?: Array<string> | null`

    List of domains to allow fetching from

  - `blocked_domains?: Array<string> | null`

    List of domains to block fetching from

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `citations?: CitationsConfigParam | null`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `enabled?: boolean`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_content_tokens?: number | null`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `max_uses?: number | null`

    Maximum number of times the tool can be used in the API request.

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

### Web Fetch Tool 20260209

- `WebFetchTool20260209`

  - `name: "web_fetch"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_fetch"`

  - `type: "web_fetch_20260209"`

    - `"web_fetch_20260209"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `allowed_domains?: Array<string> | null`

    List of domains to allow fetching from

  - `blocked_domains?: Array<string> | null`

    List of domains to block fetching from

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `citations?: CitationsConfigParam | null`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `enabled?: boolean`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_content_tokens?: number | null`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `max_uses?: number | null`

    Maximum number of times the tool can be used in the API request.

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

### Web Fetch Tool Result Block

- `WebFetchToolResultBlock`

  - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

    Tool invocation directly from the model.

    - `DirectCaller`

      Tool invocation directly from the model.

      - `type: "direct"`

        - `"direct"`

    - `ServerToolCaller`

      Tool invocation generated by a server-side tool.

      - `tool_id: string`

      - `type: "code_execution_20250825"`

        - `"code_execution_20250825"`

    - `ServerToolCaller20260120`

      - `tool_id: string`

      - `type: "code_execution_20260120"`

        - `"code_execution_20260120"`

  - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

    - `WebFetchToolResultErrorBlock`

      - `error_code: WebFetchToolResultErrorCode`

        - `"invalid_tool_input"`

        - `"url_too_long"`

        - `"url_not_allowed"`

        - `"url_not_accessible"`

        - `"unsupported_content_type"`

        - `"too_many_requests"`

        - `"max_uses_exceeded"`

        - `"unavailable"`

      - `type: "web_fetch_tool_result_error"`

        - `"web_fetch_tool_result_error"`

    - `WebFetchBlock`

      - `content: DocumentBlock`

        - `citations: CitationsConfig | null`

          Citation configuration for the document

          - `enabled: boolean`

        - `source: Base64PDFSource | PlainTextSource`

          - `Base64PDFSource`

            - `data: string`

            - `media_type: "application/pdf"`

              - `"application/pdf"`

            - `type: "base64"`

              - `"base64"`

          - `PlainTextSource`

            - `data: string`

            - `media_type: "text/plain"`

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

        - `title: string | null`

          The title of the document

        - `type: "document"`

          - `"document"`

      - `retrieved_at: string | null`

        ISO 8601 timestamp when the content was retrieved

      - `type: "web_fetch_result"`

        - `"web_fetch_result"`

      - `url: string`

        Fetched content URL

  - `tool_use_id: string`

  - `type: "web_fetch_tool_result"`

    - `"web_fetch_tool_result"`

### Web Fetch Tool Result Block Param

- `WebFetchToolResultBlockParam`

  - `content: WebFetchToolResultErrorBlockParam | WebFetchBlockParam`

    - `WebFetchToolResultErrorBlockParam`

      - `error_code: WebFetchToolResultErrorCode`

        - `"invalid_tool_input"`

        - `"url_too_long"`

        - `"url_not_allowed"`

        - `"url_not_accessible"`

        - `"unsupported_content_type"`

        - `"too_many_requests"`

        - `"max_uses_exceeded"`

        - `"unavailable"`

      - `type: "web_fetch_tool_result_error"`

        - `"web_fetch_tool_result_error"`

    - `WebFetchBlockParam`

      - `content: DocumentBlockParam`

        - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

          - `Base64PDFSource`

            - `data: string`

            - `media_type: "application/pdf"`

              - `"application/pdf"`

            - `type: "base64"`

              - `"base64"`

          - `PlainTextSource`

            - `data: string`

            - `media_type: "text/plain"`

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `ContentBlockSource`

            - `content: string | Array<ContentBlockSourceContent>`

              - `string`

              - `Array<ContentBlockSourceContent>`

                - `TextBlockParam`

                  - `text: string`

                  - `type: "text"`

                    - `"text"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

                  - `citations?: Array<TextCitationParam> | null`

                    - `CitationCharLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_char_index: number`

                      - `start_char_index: number`

                      - `type: "char_location"`

                        - `"char_location"`

                    - `CitationPageLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_page_number: number`

                      - `start_page_number: number`

                      - `type: "page_location"`

                        - `"page_location"`

                    - `CitationContentBlockLocationParam`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string | null`

                      - `end_block_index: number`

                      - `start_block_index: number`

                      - `type: "content_block_location"`

                        - `"content_block_location"`

                    - `CitationWebSearchResultLocationParam`

                      - `cited_text: string`

                      - `encrypted_index: string`

                      - `title: string | null`

                      - `type: "web_search_result_location"`

                        - `"web_search_result_location"`

                      - `url: string`

                    - `CitationSearchResultLocationParam`

                      - `cited_text: string`

                      - `end_block_index: number`

                      - `search_result_index: number`

                      - `source: string`

                      - `start_block_index: number`

                      - `title: string | null`

                      - `type: "search_result_location"`

                        - `"search_result_location"`

                - `ImageBlockParam`

                  - `source: Base64ImageSource | URLImageSource`

                    - `Base64ImageSource`

                      - `data: string`

                      - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                        - `"image/jpeg"`

                        - `"image/png"`

                        - `"image/gif"`

                        - `"image/webp"`

                      - `type: "base64"`

                        - `"base64"`

                    - `URLImageSource`

                      - `type: "url"`

                        - `"url"`

                      - `url: string`

                  - `type: "image"`

                    - `"image"`

                  - `cache_control?: CacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                      - `"ephemeral"`

                    - `ttl?: "5m" | "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

            - `type: "content"`

              - `"content"`

          - `URLPDFSource`

            - `type: "url"`

              - `"url"`

            - `url: string`

        - `type: "document"`

          - `"document"`

        - `cache_control?: CacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl?: "5m" | "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations?: CitationsConfigParam | null`

          - `enabled?: boolean`

        - `context?: string | null`

        - `title?: string | null`

      - `type: "web_fetch_result"`

        - `"web_fetch_result"`

      - `url: string`

        Fetched content URL

      - `retrieved_at?: string | null`

        ISO 8601 timestamp when the content was retrieved

  - `tool_use_id: string`

  - `type: "web_fetch_tool_result"`

    - `"web_fetch_tool_result"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

    Tool invocation directly from the model.

    - `DirectCaller`

      Tool invocation directly from the model.

      - `type: "direct"`

        - `"direct"`

    - `ServerToolCaller`

      Tool invocation generated by a server-side tool.

      - `tool_id: string`

      - `type: "code_execution_20250825"`

        - `"code_execution_20250825"`

    - `ServerToolCaller20260120`

      - `tool_id: string`

      - `type: "code_execution_20260120"`

        - `"code_execution_20260120"`

### Web Fetch Tool Result Error Block

- `WebFetchToolResultErrorBlock`

  - `error_code: WebFetchToolResultErrorCode`

    - `"invalid_tool_input"`

    - `"url_too_long"`

    - `"url_not_allowed"`

    - `"url_not_accessible"`

    - `"unsupported_content_type"`

    - `"too_many_requests"`

    - `"max_uses_exceeded"`

    - `"unavailable"`

  - `type: "web_fetch_tool_result_error"`

    - `"web_fetch_tool_result_error"`

### Web Fetch Tool Result Error Block Param

- `WebFetchToolResultErrorBlockParam`

  - `error_code: WebFetchToolResultErrorCode`

    - `"invalid_tool_input"`

    - `"url_too_long"`

    - `"url_not_allowed"`

    - `"url_not_accessible"`

    - `"unsupported_content_type"`

    - `"too_many_requests"`

    - `"max_uses_exceeded"`

    - `"unavailable"`

  - `type: "web_fetch_tool_result_error"`

    - `"web_fetch_tool_result_error"`

### Web Fetch Tool Result Error Code

- `WebFetchToolResultErrorCode = "invalid_tool_input" | "url_too_long" | "url_not_allowed" | 5 more`

  - `"invalid_tool_input"`

  - `"url_too_long"`

  - `"url_not_allowed"`

  - `"url_not_accessible"`

  - `"unsupported_content_type"`

  - `"too_many_requests"`

  - `"max_uses_exceeded"`

  - `"unavailable"`

### Web Search Result Block

- `WebSearchResultBlock`

  - `encrypted_content: string`

  - `page_age: string | null`

  - `title: string`

  - `type: "web_search_result"`

    - `"web_search_result"`

  - `url: string`

### Web Search Result Block Param

- `WebSearchResultBlockParam`

  - `encrypted_content: string`

  - `title: string`

  - `type: "web_search_result"`

    - `"web_search_result"`

  - `url: string`

  - `page_age?: string | null`

### Web Search Tool 20250305

- `WebSearchTool20250305`

  - `name: "web_search"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_search"`

  - `type: "web_search_20250305"`

    - `"web_search_20250305"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `allowed_domains?: Array<string> | null`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `blocked_domains?: Array<string> | null`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_uses?: number | null`

    Maximum number of times the tool can be used in the API request.

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

  - `user_location?: UserLocation | null`

    Parameters for the user's location. Used to provide more relevant search results.

    - `type: "approximate"`

      - `"approximate"`

    - `city?: string | null`

      The city of the user.

    - `country?: string | null`

      The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

    - `region?: string | null`

      The region of the user.

    - `timezone?: string | null`

      The [IANA timezone](https://nodatime.org/TimeZones) of the user.

### Web Search Tool 20260209

- `WebSearchTool20260209`

  - `name: "web_search"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `"web_search"`

  - `type: "web_search_20260209"`

    - `"web_search_20260209"`

  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `allowed_domains?: Array<string> | null`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `blocked_domains?: Array<string> | null`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading?: boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_uses?: number | null`

    Maximum number of times the tool can be used in the API request.

  - `strict?: boolean`

    When true, guarantees schema validation on tool names and inputs

  - `user_location?: UserLocation | null`

    Parameters for the user's location. Used to provide more relevant search results.

    - `type: "approximate"`

      - `"approximate"`

    - `city?: string | null`

      The city of the user.

    - `country?: string | null`

      The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

    - `region?: string | null`

      The region of the user.

    - `timezone?: string | null`

      The [IANA timezone](https://nodatime.org/TimeZones) of the user.

### Web Search Tool Request Error

- `WebSearchToolRequestError`

  - `error_code: WebSearchToolResultErrorCode`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"max_uses_exceeded"`

    - `"too_many_requests"`

    - `"query_too_long"`

    - `"request_too_large"`

  - `type: "web_search_tool_result_error"`

    - `"web_search_tool_result_error"`

### Web Search Tool Result Block

- `WebSearchToolResultBlock`

  - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

    Tool invocation directly from the model.

    - `DirectCaller`

      Tool invocation directly from the model.

      - `type: "direct"`

        - `"direct"`

    - `ServerToolCaller`

      Tool invocation generated by a server-side tool.

      - `tool_id: string`

      - `type: "code_execution_20250825"`

        - `"code_execution_20250825"`

    - `ServerToolCaller20260120`

      - `tool_id: string`

      - `type: "code_execution_20260120"`

        - `"code_execution_20260120"`

  - `content: WebSearchToolResultBlockContent`

    - `WebSearchToolResultError`

      - `error_code: WebSearchToolResultErrorCode`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"max_uses_exceeded"`

        - `"too_many_requests"`

        - `"query_too_long"`

        - `"request_too_large"`

      - `type: "web_search_tool_result_error"`

        - `"web_search_tool_result_error"`

    - `Array<WebSearchResultBlock>`

      - `encrypted_content: string`

      - `page_age: string | null`

      - `title: string`

      - `type: "web_search_result"`

        - `"web_search_result"`

      - `url: string`

  - `tool_use_id: string`

  - `type: "web_search_tool_result"`

    - `"web_search_tool_result"`

### Web Search Tool Result Block Content

- `WebSearchToolResultBlockContent = WebSearchToolResultError | Array<WebSearchResultBlock>`

  - `WebSearchToolResultError`

    - `error_code: WebSearchToolResultErrorCode`

      - `"invalid_tool_input"`

      - `"unavailable"`

      - `"max_uses_exceeded"`

      - `"too_many_requests"`

      - `"query_too_long"`

      - `"request_too_large"`

    - `type: "web_search_tool_result_error"`

      - `"web_search_tool_result_error"`

  - `Array<WebSearchResultBlock>`

    - `encrypted_content: string`

    - `page_age: string | null`

    - `title: string`

    - `type: "web_search_result"`

      - `"web_search_result"`

    - `url: string`

### Web Search Tool Result Block Param

- `WebSearchToolResultBlockParam`

  - `content: WebSearchToolResultBlockParamContent`

    - `Array<WebSearchResultBlockParam>`

      - `encrypted_content: string`

      - `title: string`

      - `type: "web_search_result"`

        - `"web_search_result"`

      - `url: string`

      - `page_age?: string | null`

    - `WebSearchToolRequestError`

      - `error_code: WebSearchToolResultErrorCode`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"max_uses_exceeded"`

        - `"too_many_requests"`

        - `"query_too_long"`

        - `"request_too_large"`

      - `type: "web_search_tool_result_error"`

        - `"web_search_tool_result_error"`

  - `tool_use_id: string`

  - `type: "web_search_tool_result"`

    - `"web_search_tool_result"`

  - `cache_control?: CacheControlEphemeral | null`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

      - `"ephemeral"`

    - `ttl?: "5m" | "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

    Tool invocation directly from the model.

    - `DirectCaller`

      Tool invocation directly from the model.

      - `type: "direct"`

        - `"direct"`

    - `ServerToolCaller`

      Tool invocation generated by a server-side tool.

      - `tool_id: string`

      - `type: "code_execution_20250825"`

        - `"code_execution_20250825"`

    - `ServerToolCaller20260120`

      - `tool_id: string`

      - `type: "code_execution_20260120"`

        - `"code_execution_20260120"`

### Web Search Tool Result Block Param Content

- `WebSearchToolResultBlockParamContent = Array<WebSearchResultBlockParam> | WebSearchToolRequestError`

  - `Array<WebSearchResultBlockParam>`

    - `encrypted_content: string`

    - `title: string`

    - `type: "web_search_result"`

      - `"web_search_result"`

    - `url: string`

    - `page_age?: string | null`

  - `WebSearchToolRequestError`

    - `error_code: WebSearchToolResultErrorCode`

      - `"invalid_tool_input"`

      - `"unavailable"`

      - `"max_uses_exceeded"`

      - `"too_many_requests"`

      - `"query_too_long"`

      - `"request_too_large"`

    - `type: "web_search_tool_result_error"`

      - `"web_search_tool_result_error"`

### Web Search Tool Result Error

- `WebSearchToolResultError`

  - `error_code: WebSearchToolResultErrorCode`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"max_uses_exceeded"`

    - `"too_many_requests"`

    - `"query_too_long"`

    - `"request_too_large"`

  - `type: "web_search_tool_result_error"`

    - `"web_search_tool_result_error"`

### Web Search Tool Result Error Code

- `WebSearchToolResultErrorCode = "invalid_tool_input" | "unavailable" | "max_uses_exceeded" | 3 more`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"max_uses_exceeded"`

  - `"too_many_requests"`

  - `"query_too_long"`

  - `"request_too_large"`

# Batches

## Create

`client.messages.batches.create(BatchCreateParamsbody, RequestOptionsoptions?): MessageBatch`

**post** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `body: BatchCreateParams`

  - `requests: Array<Request>`

    List of requests for prompt completion. Each is an individual request to create a Message.

    - `custom_id: string`

      Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

      Must be unique for each request within the Message Batch.

    - `params: Params`

      Messages API creation parameters for the individual request.

      See the [Messages API reference](https://docs.claude.com/en/api/messages) for full documentation on available parameters.

      - `max_tokens: number`

        The maximum number of tokens to generate before stopping.

        Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

        Different models have different maximum values for this parameter.  See [models](https://docs.claude.com/en/docs/models-overview) for details.

      - `messages: Array<MessageParam>`

        Input messages.

        Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

        Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

        If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

        Example with a single `user` message:

        ```json
        [{"role": "user", "content": "Hello, Claude"}]
        ```

        Example with multiple conversational turns:

        ```json
        [
          {"role": "user", "content": "Hello there."},
          {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
          {"role": "user", "content": "Can you explain LLMs in plain English?"},
        ]
        ```

        Example with a partially-filled response from Claude:

        ```json
        [
          {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
          {"role": "assistant", "content": "The best answer is ("},
        ]
        ```

        Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

        ```json
        {"role": "user", "content": "Hello, Claude"}
        ```

        ```json
        {"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
        ```

        See [input examples](https://docs.claude.com/en/api/messages-examples).

        Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

        There is a limit of 100,000 messages in a single request.

        - `content: string | Array<ContentBlockParam>`

          - `string`

          - `Array<ContentBlockParam>`

            - `TextBlockParam`

              - `text: string`

              - `type: "text"`

                - `"text"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations?: Array<TextCitationParam> | null`

                - `CitationCharLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_char_index: number`

                  - `start_char_index: number`

                  - `type: "char_location"`

                    - `"char_location"`

                - `CitationPageLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_page_number: number`

                  - `start_page_number: number`

                  - `type: "page_location"`

                    - `"page_location"`

                - `CitationContentBlockLocationParam`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string | null`

                  - `end_block_index: number`

                  - `start_block_index: number`

                  - `type: "content_block_location"`

                    - `"content_block_location"`

                - `CitationWebSearchResultLocationParam`

                  - `cited_text: string`

                  - `encrypted_index: string`

                  - `title: string | null`

                  - `type: "web_search_result_location"`

                    - `"web_search_result_location"`

                  - `url: string`

                - `CitationSearchResultLocationParam`

                  - `cited_text: string`

                  - `end_block_index: number`

                  - `search_result_index: number`

                  - `source: string`

                  - `start_block_index: number`

                  - `title: string | null`

                  - `type: "search_result_location"`

                    - `"search_result_location"`

            - `ImageBlockParam`

              - `source: Base64ImageSource | URLImageSource`

                - `Base64ImageSource`

                  - `data: string`

                  - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                    - `"image/jpeg"`

                    - `"image/png"`

                    - `"image/gif"`

                    - `"image/webp"`

                  - `type: "base64"`

                    - `"base64"`

                - `URLImageSource`

                  - `type: "url"`

                    - `"url"`

                  - `url: string`

              - `type: "image"`

                - `"image"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

            - `DocumentBlockParam`

              - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

                - `Base64PDFSource`

                  - `data: string`

                  - `media_type: "application/pdf"`

                    - `"application/pdf"`

                  - `type: "base64"`

                    - `"base64"`

                - `PlainTextSource`

                  - `data: string`

                  - `media_type: "text/plain"`

                    - `"text/plain"`

                  - `type: "text"`

                    - `"text"`

                - `ContentBlockSource`

                  - `content: string | Array<ContentBlockSourceContent>`

                    - `string`

                    - `Array<ContentBlockSourceContent>`

                      - `TextBlockParam`

                        - `text: string`

                        - `type: "text"`

                          - `"text"`

                        - `cache_control?: CacheControlEphemeral | null`

                          Create a cache control breakpoint at this content block.

                          - `type: "ephemeral"`

                            - `"ephemeral"`

                          - `ttl?: "5m" | "1h"`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `"5m"`

                            - `"1h"`

                        - `citations?: Array<TextCitationParam> | null`

                          - `CitationCharLocationParam`

                            - `cited_text: string`

                            - `document_index: number`

                            - `document_title: string | null`

                            - `end_char_index: number`

                            - `start_char_index: number`

                            - `type: "char_location"`

                              - `"char_location"`

                          - `CitationPageLocationParam`

                            - `cited_text: string`

                            - `document_index: number`

                            - `document_title: string | null`

                            - `end_page_number: number`

                            - `start_page_number: number`

                            - `type: "page_location"`

                              - `"page_location"`

                          - `CitationContentBlockLocationParam`

                            - `cited_text: string`

                            - `document_index: number`

                            - `document_title: string | null`

                            - `end_block_index: number`

                            - `start_block_index: number`

                            - `type: "content_block_location"`

                              - `"content_block_location"`

                          - `CitationWebSearchResultLocationParam`

                            - `cited_text: string`

                            - `encrypted_index: string`

                            - `title: string | null`

                            - `type: "web_search_result_location"`

                              - `"web_search_result_location"`

                            - `url: string`

                          - `CitationSearchResultLocationParam`

                            - `cited_text: string`

                            - `end_block_index: number`

                            - `search_result_index: number`

                            - `source: string`

                            - `start_block_index: number`

                            - `title: string | null`

                            - `type: "search_result_location"`

                              - `"search_result_location"`

                      - `ImageBlockParam`

                        - `source: Base64ImageSource | URLImageSource`

                          - `Base64ImageSource`

                            - `data: string`

                            - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                              - `"image/jpeg"`

                              - `"image/png"`

                              - `"image/gif"`

                              - `"image/webp"`

                            - `type: "base64"`

                              - `"base64"`

                          - `URLImageSource`

                            - `type: "url"`

                              - `"url"`

                            - `url: string`

                        - `type: "image"`

                          - `"image"`

                        - `cache_control?: CacheControlEphemeral | null`

                          Create a cache control breakpoint at this content block.

                          - `type: "ephemeral"`

                            - `"ephemeral"`

                          - `ttl?: "5m" | "1h"`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `"5m"`

                            - `"1h"`

                  - `type: "content"`

                    - `"content"`

                - `URLPDFSource`

                  - `type: "url"`

                    - `"url"`

                  - `url: string`

              - `type: "document"`

                - `"document"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations?: CitationsConfigParam | null`

                - `enabled?: boolean`

              - `context?: string | null`

              - `title?: string | null`

            - `SearchResultBlockParam`

              - `content: Array<TextBlockParam>`

                - `text: string`

                - `type: "text"`

                  - `"text"`

                - `cache_control?: CacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

                  - `type: "ephemeral"`

                    - `"ephemeral"`

                  - `ttl?: "5m" | "1h"`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

                - `citations?: Array<TextCitationParam> | null`

                  - `CitationCharLocationParam`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string | null`

                    - `end_char_index: number`

                    - `start_char_index: number`

                    - `type: "char_location"`

                      - `"char_location"`

                  - `CitationPageLocationParam`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string | null`

                    - `end_page_number: number`

                    - `start_page_number: number`

                    - `type: "page_location"`

                      - `"page_location"`

                  - `CitationContentBlockLocationParam`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string | null`

                    - `end_block_index: number`

                    - `start_block_index: number`

                    - `type: "content_block_location"`

                      - `"content_block_location"`

                  - `CitationWebSearchResultLocationParam`

                    - `cited_text: string`

                    - `encrypted_index: string`

                    - `title: string | null`

                    - `type: "web_search_result_location"`

                      - `"web_search_result_location"`

                    - `url: string`

                  - `CitationSearchResultLocationParam`

                    - `cited_text: string`

                    - `end_block_index: number`

                    - `search_result_index: number`

                    - `source: string`

                    - `start_block_index: number`

                    - `title: string | null`

                    - `type: "search_result_location"`

                      - `"search_result_location"`

              - `source: string`

              - `title: string`

              - `type: "search_result"`

                - `"search_result"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations?: CitationsConfigParam`

                - `enabled?: boolean`

            - `ThinkingBlockParam`

              - `signature: string`

              - `thinking: string`

              - `type: "thinking"`

                - `"thinking"`

            - `RedactedThinkingBlockParam`

              - `data: string`

              - `type: "redacted_thinking"`

                - `"redacted_thinking"`

            - `ToolUseBlockParam`

              - `id: string`

              - `input: Record<string, unknown>`

              - `name: string`

              - `type: "tool_use"`

                - `"tool_use"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

                Tool invocation directly from the model.

                - `DirectCaller`

                  Tool invocation directly from the model.

                  - `type: "direct"`

                    - `"direct"`

                - `ServerToolCaller`

                  Tool invocation generated by a server-side tool.

                  - `tool_id: string`

                  - `type: "code_execution_20250825"`

                    - `"code_execution_20250825"`

                - `ServerToolCaller20260120`

                  - `tool_id: string`

                  - `type: "code_execution_20260120"`

                    - `"code_execution_20260120"`

            - `ToolResultBlockParam`

              - `tool_use_id: string`

              - `type: "tool_result"`

                - `"tool_result"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `content?: string | Array<TextBlockParam | ImageBlockParam | SearchResultBlockParam | 2 more>`

                - `string`

                - `Array<TextBlockParam | ImageBlockParam | SearchResultBlockParam | 2 more>`

                  - `TextBlockParam`

                    - `text: string`

                    - `type: "text"`

                      - `"text"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

                    - `citations?: Array<TextCitationParam> | null`

                      - `CitationCharLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_char_index: number`

                        - `start_char_index: number`

                        - `type: "char_location"`

                          - `"char_location"`

                      - `CitationPageLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_page_number: number`

                        - `start_page_number: number`

                        - `type: "page_location"`

                          - `"page_location"`

                      - `CitationContentBlockLocationParam`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string | null`

                        - `end_block_index: number`

                        - `start_block_index: number`

                        - `type: "content_block_location"`

                          - `"content_block_location"`

                      - `CitationWebSearchResultLocationParam`

                        - `cited_text: string`

                        - `encrypted_index: string`

                        - `title: string | null`

                        - `type: "web_search_result_location"`

                          - `"web_search_result_location"`

                        - `url: string`

                      - `CitationSearchResultLocationParam`

                        - `cited_text: string`

                        - `end_block_index: number`

                        - `search_result_index: number`

                        - `source: string`

                        - `start_block_index: number`

                        - `title: string | null`

                        - `type: "search_result_location"`

                          - `"search_result_location"`

                  - `ImageBlockParam`

                    - `source: Base64ImageSource | URLImageSource`

                      - `Base64ImageSource`

                        - `data: string`

                        - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                          - `"image/jpeg"`

                          - `"image/png"`

                          - `"image/gif"`

                          - `"image/webp"`

                        - `type: "base64"`

                          - `"base64"`

                      - `URLImageSource`

                        - `type: "url"`

                          - `"url"`

                        - `url: string`

                    - `type: "image"`

                      - `"image"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

                  - `SearchResultBlockParam`

                    - `content: Array<TextBlockParam>`

                      - `text: string`

                      - `type: "text"`

                        - `"text"`

                      - `cache_control?: CacheControlEphemeral | null`

                        Create a cache control breakpoint at this content block.

                        - `type: "ephemeral"`

                          - `"ephemeral"`

                        - `ttl?: "5m" | "1h"`

                          The time-to-live for the cache control breakpoint.

                          This may be one the following values:

                          - `5m`: 5 minutes
                          - `1h`: 1 hour

                          Defaults to `5m`.

                          - `"5m"`

                          - `"1h"`

                      - `citations?: Array<TextCitationParam> | null`

                        - `CitationCharLocationParam`

                          - `cited_text: string`

                          - `document_index: number`

                          - `document_title: string | null`

                          - `end_char_index: number`

                          - `start_char_index: number`

                          - `type: "char_location"`

                            - `"char_location"`

                        - `CitationPageLocationParam`

                          - `cited_text: string`

                          - `document_index: number`

                          - `document_title: string | null`

                          - `end_page_number: number`

                          - `start_page_number: number`

                          - `type: "page_location"`

                            - `"page_location"`

                        - `CitationContentBlockLocationParam`

                          - `cited_text: string`

                          - `document_index: number`

                          - `document_title: string | null`

                          - `end_block_index: number`

                          - `start_block_index: number`

                          - `type: "content_block_location"`

                            - `"content_block_location"`

                        - `CitationWebSearchResultLocationParam`

                          - `cited_text: string`

                          - `encrypted_index: string`

                          - `title: string | null`

                          - `type: "web_search_result_location"`

                            - `"web_search_result_location"`

                          - `url: string`

                        - `CitationSearchResultLocationParam`

                          - `cited_text: string`

                          - `end_block_index: number`

                          - `search_result_index: number`

                          - `source: string`

                          - `start_block_index: number`

                          - `title: string | null`

                          - `type: "search_result_location"`

                            - `"search_result_location"`

                    - `source: string`

                    - `title: string`

                    - `type: "search_result"`

                      - `"search_result"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

                    - `citations?: CitationsConfigParam`

                      - `enabled?: boolean`

                  - `DocumentBlockParam`

                    - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

                      - `Base64PDFSource`

                        - `data: string`

                        - `media_type: "application/pdf"`

                          - `"application/pdf"`

                        - `type: "base64"`

                          - `"base64"`

                      - `PlainTextSource`

                        - `data: string`

                        - `media_type: "text/plain"`

                          - `"text/plain"`

                        - `type: "text"`

                          - `"text"`

                      - `ContentBlockSource`

                        - `content: string | Array<ContentBlockSourceContent>`

                          - `string`

                          - `Array<ContentBlockSourceContent>`

                            - `TextBlockParam`

                              - `text: string`

                              - `type: "text"`

                                - `"text"`

                              - `cache_control?: CacheControlEphemeral | null`

                                Create a cache control breakpoint at this content block.

                                - `type: "ephemeral"`

                                  - `"ephemeral"`

                                - `ttl?: "5m" | "1h"`

                                  The time-to-live for the cache control breakpoint.

                                  This may be one the following values:

                                  - `5m`: 5 minutes
                                  - `1h`: 1 hour

                                  Defaults to `5m`.

                                  - `"5m"`

                                  - `"1h"`

                              - `citations?: Array<TextCitationParam> | null`

                                - `CitationCharLocationParam`

                                  - `cited_text: string`

                                  - `document_index: number`

                                  - `document_title: string | null`

                                  - `end_char_index: number`

                                  - `start_char_index: number`

                                  - `type: "char_location"`

                                    - `"char_location"`

                                - `CitationPageLocationParam`

                                  - `cited_text: string`

                                  - `document_index: number`

                                  - `document_title: string | null`

                                  - `end_page_number: number`

                                  - `start_page_number: number`

                                  - `type: "page_location"`

                                    - `"page_location"`

                                - `CitationContentBlockLocationParam`

                                  - `cited_text: string`

                                  - `document_index: number`

                                  - `document_title: string | null`

                                  - `end_block_index: number`

                                  - `start_block_index: number`

                                  - `type: "content_block_location"`

                                    - `"content_block_location"`

                                - `CitationWebSearchResultLocationParam`

                                  - `cited_text: string`

                                  - `encrypted_index: string`

                                  - `title: string | null`

                                  - `type: "web_search_result_location"`

                                    - `"web_search_result_location"`

                                  - `url: string`

                                - `CitationSearchResultLocationParam`

                                  - `cited_text: string`

                                  - `end_block_index: number`

                                  - `search_result_index: number`

                                  - `source: string`

                                  - `start_block_index: number`

                                  - `title: string | null`

                                  - `type: "search_result_location"`

                                    - `"search_result_location"`

                            - `ImageBlockParam`

                              - `source: Base64ImageSource | URLImageSource`

                                - `Base64ImageSource`

                                  - `data: string`

                                  - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                                    - `"image/jpeg"`

                                    - `"image/png"`

                                    - `"image/gif"`

                                    - `"image/webp"`

                                  - `type: "base64"`

                                    - `"base64"`

                                - `URLImageSource`

                                  - `type: "url"`

                                    - `"url"`

                                  - `url: string`

                              - `type: "image"`

                                - `"image"`

                              - `cache_control?: CacheControlEphemeral | null`

                                Create a cache control breakpoint at this content block.

                                - `type: "ephemeral"`

                                  - `"ephemeral"`

                                - `ttl?: "5m" | "1h"`

                                  The time-to-live for the cache control breakpoint.

                                  This may be one the following values:

                                  - `5m`: 5 minutes
                                  - `1h`: 1 hour

                                  Defaults to `5m`.

                                  - `"5m"`

                                  - `"1h"`

                        - `type: "content"`

                          - `"content"`

                      - `URLPDFSource`

                        - `type: "url"`

                          - `"url"`

                        - `url: string`

                    - `type: "document"`

                      - `"document"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

                    - `citations?: CitationsConfigParam | null`

                      - `enabled?: boolean`

                    - `context?: string | null`

                    - `title?: string | null`

                  - `ToolReferenceBlockParam`

                    Tool reference block that can be included in tool_result content.

                    - `tool_name: string`

                    - `type: "tool_reference"`

                      - `"tool_reference"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

              - `is_error?: boolean`

            - `ServerToolUseBlockParam`

              - `id: string`

              - `input: Record<string, unknown>`

              - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

                - `"web_search"`

                - `"web_fetch"`

                - `"code_execution"`

                - `"bash_code_execution"`

                - `"text_editor_code_execution"`

                - `"tool_search_tool_regex"`

                - `"tool_search_tool_bm25"`

              - `type: "server_tool_use"`

                - `"server_tool_use"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

                Tool invocation directly from the model.

                - `DirectCaller`

                  Tool invocation directly from the model.

                  - `type: "direct"`

                    - `"direct"`

                - `ServerToolCaller`

                  Tool invocation generated by a server-side tool.

                  - `tool_id: string`

                  - `type: "code_execution_20250825"`

                    - `"code_execution_20250825"`

                - `ServerToolCaller20260120`

                  - `tool_id: string`

                  - `type: "code_execution_20260120"`

                    - `"code_execution_20260120"`

            - `WebSearchToolResultBlockParam`

              - `content: WebSearchToolResultBlockParamContent`

                - `Array<WebSearchResultBlockParam>`

                  - `encrypted_content: string`

                  - `title: string`

                  - `type: "web_search_result"`

                    - `"web_search_result"`

                  - `url: string`

                  - `page_age?: string | null`

                - `WebSearchToolRequestError`

                  - `error_code: WebSearchToolResultErrorCode`

                    - `"invalid_tool_input"`

                    - `"unavailable"`

                    - `"max_uses_exceeded"`

                    - `"too_many_requests"`

                    - `"query_too_long"`

                    - `"request_too_large"`

                  - `type: "web_search_tool_result_error"`

                    - `"web_search_tool_result_error"`

              - `tool_use_id: string`

              - `type: "web_search_tool_result"`

                - `"web_search_tool_result"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

                Tool invocation directly from the model.

                - `DirectCaller`

                  Tool invocation directly from the model.

                  - `type: "direct"`

                    - `"direct"`

                - `ServerToolCaller`

                  Tool invocation generated by a server-side tool.

                  - `tool_id: string`

                  - `type: "code_execution_20250825"`

                    - `"code_execution_20250825"`

                - `ServerToolCaller20260120`

                  - `tool_id: string`

                  - `type: "code_execution_20260120"`

                    - `"code_execution_20260120"`

            - `WebFetchToolResultBlockParam`

              - `content: WebFetchToolResultErrorBlockParam | WebFetchBlockParam`

                - `WebFetchToolResultErrorBlockParam`

                  - `error_code: WebFetchToolResultErrorCode`

                    - `"invalid_tool_input"`

                    - `"url_too_long"`

                    - `"url_not_allowed"`

                    - `"url_not_accessible"`

                    - `"unsupported_content_type"`

                    - `"too_many_requests"`

                    - `"max_uses_exceeded"`

                    - `"unavailable"`

                  - `type: "web_fetch_tool_result_error"`

                    - `"web_fetch_tool_result_error"`

                - `WebFetchBlockParam`

                  - `content: DocumentBlockParam`

                    - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource`

                      - `Base64PDFSource`

                        - `data: string`

                        - `media_type: "application/pdf"`

                          - `"application/pdf"`

                        - `type: "base64"`

                          - `"base64"`

                      - `PlainTextSource`

                        - `data: string`

                        - `media_type: "text/plain"`

                          - `"text/plain"`

                        - `type: "text"`

                          - `"text"`

                      - `ContentBlockSource`

                        - `content: string | Array<ContentBlockSourceContent>`

                          - `string`

                          - `Array<ContentBlockSourceContent>`

                            - `TextBlockParam`

                              - `text: string`

                              - `type: "text"`

                                - `"text"`

                              - `cache_control?: CacheControlEphemeral | null`

                                Create a cache control breakpoint at this content block.

                                - `type: "ephemeral"`

                                  - `"ephemeral"`

                                - `ttl?: "5m" | "1h"`

                                  The time-to-live for the cache control breakpoint.

                                  This may be one the following values:

                                  - `5m`: 5 minutes
                                  - `1h`: 1 hour

                                  Defaults to `5m`.

                                  - `"5m"`

                                  - `"1h"`

                              - `citations?: Array<TextCitationParam> | null`

                                - `CitationCharLocationParam`

                                  - `cited_text: string`

                                  - `document_index: number`

                                  - `document_title: string | null`

                                  - `end_char_index: number`

                                  - `start_char_index: number`

                                  - `type: "char_location"`

                                    - `"char_location"`

                                - `CitationPageLocationParam`

                                  - `cited_text: string`

                                  - `document_index: number`

                                  - `document_title: string | null`

                                  - `end_page_number: number`

                                  - `start_page_number: number`

                                  - `type: "page_location"`

                                    - `"page_location"`

                                - `CitationContentBlockLocationParam`

                                  - `cited_text: string`

                                  - `document_index: number`

                                  - `document_title: string | null`

                                  - `end_block_index: number`

                                  - `start_block_index: number`

                                  - `type: "content_block_location"`

                                    - `"content_block_location"`

                                - `CitationWebSearchResultLocationParam`

                                  - `cited_text: string`

                                  - `encrypted_index: string`

                                  - `title: string | null`

                                  - `type: "web_search_result_location"`

                                    - `"web_search_result_location"`

                                  - `url: string`

                                - `CitationSearchResultLocationParam`

                                  - `cited_text: string`

                                  - `end_block_index: number`

                                  - `search_result_index: number`

                                  - `source: string`

                                  - `start_block_index: number`

                                  - `title: string | null`

                                  - `type: "search_result_location"`

                                    - `"search_result_location"`

                            - `ImageBlockParam`

                              - `source: Base64ImageSource | URLImageSource`

                                - `Base64ImageSource`

                                  - `data: string`

                                  - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                                    - `"image/jpeg"`

                                    - `"image/png"`

                                    - `"image/gif"`

                                    - `"image/webp"`

                                  - `type: "base64"`

                                    - `"base64"`

                                - `URLImageSource`

                                  - `type: "url"`

                                    - `"url"`

                                  - `url: string`

                              - `type: "image"`

                                - `"image"`

                              - `cache_control?: CacheControlEphemeral | null`

                                Create a cache control breakpoint at this content block.

                                - `type: "ephemeral"`

                                  - `"ephemeral"`

                                - `ttl?: "5m" | "1h"`

                                  The time-to-live for the cache control breakpoint.

                                  This may be one the following values:

                                  - `5m`: 5 minutes
                                  - `1h`: 1 hour

                                  Defaults to `5m`.

                                  - `"5m"`

                                  - `"1h"`

                        - `type: "content"`

                          - `"content"`

                      - `URLPDFSource`

                        - `type: "url"`

                          - `"url"`

                        - `url: string`

                    - `type: "document"`

                      - `"document"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

                    - `citations?: CitationsConfigParam | null`

                      - `enabled?: boolean`

                    - `context?: string | null`

                    - `title?: string | null`

                  - `type: "web_fetch_result"`

                    - `"web_fetch_result"`

                  - `url: string`

                    Fetched content URL

                  - `retrieved_at?: string | null`

                    ISO 8601 timestamp when the content was retrieved

              - `tool_use_id: string`

              - `type: "web_fetch_tool_result"`

                - `"web_fetch_tool_result"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

                Tool invocation directly from the model.

                - `DirectCaller`

                  Tool invocation directly from the model.

                  - `type: "direct"`

                    - `"direct"`

                - `ServerToolCaller`

                  Tool invocation generated by a server-side tool.

                  - `tool_id: string`

                  - `type: "code_execution_20250825"`

                    - `"code_execution_20250825"`

                - `ServerToolCaller20260120`

                  - `tool_id: string`

                  - `type: "code_execution_20260120"`

                    - `"code_execution_20260120"`

            - `CodeExecutionToolResultBlockParam`

              - `content: CodeExecutionToolResultBlockParamContent`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `CodeExecutionToolResultErrorParam`

                  - `error_code: CodeExecutionToolResultErrorCode`

                    - `"invalid_tool_input"`

                    - `"unavailable"`

                    - `"too_many_requests"`

                    - `"execution_time_exceeded"`

                  - `type: "code_execution_tool_result_error"`

                    - `"code_execution_tool_result_error"`

                - `CodeExecutionResultBlockParam`

                  - `content: Array<CodeExecutionOutputBlockParam>`

                    - `file_id: string`

                    - `type: "code_execution_output"`

                      - `"code_execution_output"`

                  - `return_code: number`

                  - `stderr: string`

                  - `stdout: string`

                  - `type: "code_execution_result"`

                    - `"code_execution_result"`

                - `EncryptedCodeExecutionResultBlockParam`

                  Code execution result with encrypted stdout for PFC + web_search results.

                  - `content: Array<CodeExecutionOutputBlockParam>`

                    - `file_id: string`

                    - `type: "code_execution_output"`

                      - `"code_execution_output"`

                  - `encrypted_stdout: string`

                  - `return_code: number`

                  - `stderr: string`

                  - `type: "encrypted_code_execution_result"`

                    - `"encrypted_code_execution_result"`

              - `tool_use_id: string`

              - `type: "code_execution_tool_result"`

                - `"code_execution_tool_result"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

            - `BashCodeExecutionToolResultBlockParam`

              - `content: BashCodeExecutionToolResultErrorParam | BashCodeExecutionResultBlockParam`

                - `BashCodeExecutionToolResultErrorParam`

                  - `error_code: BashCodeExecutionToolResultErrorCode`

                    - `"invalid_tool_input"`

                    - `"unavailable"`

                    - `"too_many_requests"`

                    - `"execution_time_exceeded"`

                    - `"output_file_too_large"`

                  - `type: "bash_code_execution_tool_result_error"`

                    - `"bash_code_execution_tool_result_error"`

                - `BashCodeExecutionResultBlockParam`

                  - `content: Array<BashCodeExecutionOutputBlockParam>`

                    - `file_id: string`

                    - `type: "bash_code_execution_output"`

                      - `"bash_code_execution_output"`

                  - `return_code: number`

                  - `stderr: string`

                  - `stdout: string`

                  - `type: "bash_code_execution_result"`

                    - `"bash_code_execution_result"`

              - `tool_use_id: string`

              - `type: "bash_code_execution_tool_result"`

                - `"bash_code_execution_tool_result"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

            - `TextEditorCodeExecutionToolResultBlockParam`

              - `content: TextEditorCodeExecutionToolResultErrorParam | TextEditorCodeExecutionViewResultBlockParam | TextEditorCodeExecutionCreateResultBlockParam | TextEditorCodeExecutionStrReplaceResultBlockParam`

                - `TextEditorCodeExecutionToolResultErrorParam`

                  - `error_code: TextEditorCodeExecutionToolResultErrorCode`

                    - `"invalid_tool_input"`

                    - `"unavailable"`

                    - `"too_many_requests"`

                    - `"execution_time_exceeded"`

                    - `"file_not_found"`

                  - `type: "text_editor_code_execution_tool_result_error"`

                    - `"text_editor_code_execution_tool_result_error"`

                  - `error_message?: string | null`

                - `TextEditorCodeExecutionViewResultBlockParam`

                  - `content: string`

                  - `file_type: "text" | "image" | "pdf"`

                    - `"text"`

                    - `"image"`

                    - `"pdf"`

                  - `type: "text_editor_code_execution_view_result"`

                    - `"text_editor_code_execution_view_result"`

                  - `num_lines?: number | null`

                  - `start_line?: number | null`

                  - `total_lines?: number | null`

                - `TextEditorCodeExecutionCreateResultBlockParam`

                  - `is_file_update: boolean`

                  - `type: "text_editor_code_execution_create_result"`

                    - `"text_editor_code_execution_create_result"`

                - `TextEditorCodeExecutionStrReplaceResultBlockParam`

                  - `type: "text_editor_code_execution_str_replace_result"`

                    - `"text_editor_code_execution_str_replace_result"`

                  - `lines?: Array<string> | null`

                  - `new_lines?: number | null`

                  - `new_start?: number | null`

                  - `old_lines?: number | null`

                  - `old_start?: number | null`

              - `tool_use_id: string`

              - `type: "text_editor_code_execution_tool_result"`

                - `"text_editor_code_execution_tool_result"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

            - `ToolSearchToolResultBlockParam`

              - `content: ToolSearchToolResultErrorParam | ToolSearchToolSearchResultBlockParam`

                - `ToolSearchToolResultErrorParam`

                  - `error_code: ToolSearchToolResultErrorCode`

                    - `"invalid_tool_input"`

                    - `"unavailable"`

                    - `"too_many_requests"`

                    - `"execution_time_exceeded"`

                  - `type: "tool_search_tool_result_error"`

                    - `"tool_search_tool_result_error"`

                - `ToolSearchToolSearchResultBlockParam`

                  - `tool_references: Array<ToolReferenceBlockParam>`

                    - `tool_name: string`

                    - `type: "tool_reference"`

                      - `"tool_reference"`

                    - `cache_control?: CacheControlEphemeral | null`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                        - `"ephemeral"`

                      - `ttl?: "5m" | "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

                  - `type: "tool_search_tool_search_result"`

                    - `"tool_search_tool_search_result"`

              - `tool_use_id: string`

              - `type: "tool_search_tool_result"`

                - `"tool_search_tool_result"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

            - `ContainerUploadBlockParam`

              A content block that represents a file to be uploaded to the container
              Files uploaded via this block will be available in the container's input directory.

              - `file_id: string`

              - `type: "container_upload"`

                - `"container_upload"`

              - `cache_control?: CacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                  - `"ephemeral"`

                - `ttl?: "5m" | "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

        - `role: "user" | "assistant"`

          - `"user"`

          - `"assistant"`

      - `model: Model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-opus-4-5-20251101" | 19 more`

          - `"claude-opus-4-6"`

            Most intelligent model for building agents and coding

          - `"claude-sonnet-4-6"`

            Frontier intelligence at scale — built for coding, agents, and enterprise workflows

          - `"claude-opus-4-5-20251101"`

            Premium model combining maximum intelligence with practical performance

          - `"claude-opus-4-5"`

            Premium model combining maximum intelligence with practical performance

          - `"claude-3-7-sonnet-latest"`

            High-performance model with early extended thinking

          - `"claude-3-7-sonnet-20250219"`

            High-performance model with early extended thinking

          - `"claude-3-5-haiku-latest"`

            Fastest and most compact model for near-instant responsiveness

          - `"claude-3-5-haiku-20241022"`

            Our fastest model

          - `"claude-haiku-4-5"`

            Hybrid model, capable of near-instant responses and extended thinking

          - `"claude-haiku-4-5-20251001"`

            Hybrid model, capable of near-instant responses and extended thinking

          - `"claude-sonnet-4-20250514"`

            High-performance model with extended thinking

          - `"claude-sonnet-4-0"`

            High-performance model with extended thinking

          - `"claude-4-sonnet-20250514"`

            High-performance model with extended thinking

          - `"claude-sonnet-4-5"`

            Our best model for real-world agents and coding

          - `"claude-sonnet-4-5-20250929"`

            Our best model for real-world agents and coding

          - `"claude-opus-4-0"`

            Our most capable model

          - `"claude-opus-4-20250514"`

            Our most capable model

          - `"claude-4-opus-20250514"`

            Our most capable model

          - `"claude-opus-4-1-20250805"`

            Our most capable model

          - `"claude-3-opus-latest"`

            Excels at writing and complex tasks

          - `"claude-3-opus-20240229"`

            Excels at writing and complex tasks

          - `"claude-3-haiku-20240307"`

            Our previous most fast and cost-effective

        - `(string & {})`

      - `cache_control?: CacheControlEphemeral | null`

        Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

        - `type: "ephemeral"`

          - `"ephemeral"`

        - `ttl?: "5m" | "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `container?: string | null`

        Container identifier for reuse across requests.

      - `inference_geo?: string | null`

        Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

      - `metadata?: Metadata`

        An object describing metadata about the request.

        - `user_id?: string | null`

          An external identifier for the user who is associated with the request.

          This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

      - `output_config?: OutputConfig`

        Configuration options for the model's output, such as the output format.

        - `effort?: "low" | "medium" | "high" | "max" | null`

          All possible effort levels.

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"max"`

        - `format?: JSONOutputFormat | null`

          A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

          - `schema: Record<string, unknown>`

            The JSON schema of the format

          - `type: "json_schema"`

            - `"json_schema"`

      - `service_tier?: "auto" | "standard_only"`

        Determines whether to use priority capacity (if available) or standard capacity for this request.

        Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

        - `"auto"`

        - `"standard_only"`

      - `stop_sequences?: Array<string>`

        Custom text sequences that will cause the model to stop generating.

        Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

        If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

      - `stream?: boolean`

        Whether to incrementally stream the response using server-sent events.

        See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

      - `system?: string | Array<TextBlockParam>`

        System prompt.

        A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

        - `string`

        - `Array<TextBlockParam>`

          - `text: string`

          - `type: "text"`

            - `"text"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations?: Array<TextCitationParam> | null`

            - `CitationCharLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_char_index: number`

              - `start_char_index: number`

              - `type: "char_location"`

                - `"char_location"`

            - `CitationPageLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_page_number: number`

              - `start_page_number: number`

              - `type: "page_location"`

                - `"page_location"`

            - `CitationContentBlockLocationParam`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_block_index: number`

              - `start_block_index: number`

              - `type: "content_block_location"`

                - `"content_block_location"`

            - `CitationWebSearchResultLocationParam`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string | null`

              - `type: "web_search_result_location"`

                - `"web_search_result_location"`

              - `url: string`

            - `CitationSearchResultLocationParam`

              - `cited_text: string`

              - `end_block_index: number`

              - `search_result_index: number`

              - `source: string`

              - `start_block_index: number`

              - `title: string | null`

              - `type: "search_result_location"`

                - `"search_result_location"`

      - `temperature?: number`

        Amount of randomness injected into the response.

        Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

        Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

      - `thinking?: ThinkingConfigParam`

        Configuration for enabling Claude's extended thinking.

        When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

        See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

        - `ThinkingConfigEnabled`

          - `budget_tokens: number`

            Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

            Must be ≥1024 and less than `max_tokens`.

            See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

          - `type: "enabled"`

            - `"enabled"`

        - `ThinkingConfigDisabled`

          - `type: "disabled"`

            - `"disabled"`

        - `ThinkingConfigAdaptive`

          - `type: "adaptive"`

            - `"adaptive"`

      - `tool_choice?: ToolChoice`

        How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

        - `ToolChoiceAuto`

          The model will automatically decide whether to use tools.

          - `type: "auto"`

            - `"auto"`

          - `disable_parallel_tool_use?: boolean`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output at most one tool use.

        - `ToolChoiceAny`

          The model will use any available tools.

          - `type: "any"`

            - `"any"`

          - `disable_parallel_tool_use?: boolean`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `ToolChoiceTool`

          The model will use the specified tool with `tool_choice.name`.

          - `name: string`

            The name of the tool to use.

          - `type: "tool"`

            - `"tool"`

          - `disable_parallel_tool_use?: boolean`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `ToolChoiceNone`

          The model will not be allowed to use tools.

          - `type: "none"`

            - `"none"`

      - `tools?: Array<ToolUnion>`

        Definitions of tools that the model may use.

        If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

        There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

        Each tool definition includes:

        * `name`: Name of the tool.
        * `description`: Optional, but strongly-recommended description of the tool.
        * `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

        For example, if you defined `tools` as:

        ```json
        [
          {
            "name": "get_stock_price",
            "description": "Get the current stock price for a given ticker symbol.",
            "input_schema": {
              "type": "object",
              "properties": {
                "ticker": {
                  "type": "string",
                  "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
                }
              },
              "required": ["ticker"]
            }
          }
        ]
        ```

        And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

        ```json
        [
          {
            "type": "tool_use",
            "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
            "name": "get_stock_price",
            "input": { "ticker": "^GSPC" }
          }
        ]
        ```

        You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

        ```json
        [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
            "content": "259.75 USD"
          }
        ]
        ```

        Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

        See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

        - `Tool`

          - `input_schema: InputSchema`

            [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

            This defines the shape of the `input` that your tool accepts and that the model will produce.

            - `type: "object"`

              - `"object"`

            - `properties?: Record<string, unknown> | null`

            - `required?: Array<string> | null`

          - `name: string`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `description?: string`

            Description of what this tool does.

            Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

          - `eager_input_streaming?: boolean | null`

            Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

          - `input_examples?: Array<Record<string, unknown>>`

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

          - `type?: "custom" | null`

            - `"custom"`

        - `ToolBash20250124`

          - `name: "bash"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"bash"`

          - `type: "bash_20250124"`

            - `"bash_20250124"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `input_examples?: Array<Record<string, unknown>>`

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

        - `CodeExecutionTool20250522`

          - `name: "code_execution"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"code_execution"`

          - `type: "code_execution_20250522"`

            - `"code_execution_20250522"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

        - `CodeExecutionTool20250825`

          - `name: "code_execution"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"code_execution"`

          - `type: "code_execution_20250825"`

            - `"code_execution_20250825"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

        - `CodeExecutionTool20260120`

          Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

          - `name: "code_execution"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"code_execution"`

          - `type: "code_execution_20260120"`

            - `"code_execution_20260120"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

        - `MemoryTool20250818`

          - `name: "memory"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"memory"`

          - `type: "memory_20250818"`

            - `"memory_20250818"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `input_examples?: Array<Record<string, unknown>>`

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

        - `ToolTextEditor20250124`

          - `name: "str_replace_editor"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"str_replace_editor"`

          - `type: "text_editor_20250124"`

            - `"text_editor_20250124"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `input_examples?: Array<Record<string, unknown>>`

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

        - `ToolTextEditor20250429`

          - `name: "str_replace_based_edit_tool"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"str_replace_based_edit_tool"`

          - `type: "text_editor_20250429"`

            - `"text_editor_20250429"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `input_examples?: Array<Record<string, unknown>>`

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

        - `ToolTextEditor20250728`

          - `name: "str_replace_based_edit_tool"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"str_replace_based_edit_tool"`

          - `type: "text_editor_20250728"`

            - `"text_editor_20250728"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `input_examples?: Array<Record<string, unknown>>`

          - `max_characters?: number | null`

            Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

        - `WebSearchTool20250305`

          - `name: "web_search"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"web_search"`

          - `type: "web_search_20250305"`

            - `"web_search_20250305"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `allowed_domains?: Array<string> | null`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `blocked_domains?: Array<string> | null`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `max_uses?: number | null`

            Maximum number of times the tool can be used in the API request.

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

          - `user_location?: UserLocation | null`

            Parameters for the user's location. Used to provide more relevant search results.

            - `type: "approximate"`

              - `"approximate"`

            - `city?: string | null`

              The city of the user.

            - `country?: string | null`

              The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

            - `region?: string | null`

              The region of the user.

            - `timezone?: string | null`

              The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        - `WebFetchTool20250910`

          - `name: "web_fetch"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"web_fetch"`

          - `type: "web_fetch_20250910"`

            - `"web_fetch_20250910"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `allowed_domains?: Array<string> | null`

            List of domains to allow fetching from

          - `blocked_domains?: Array<string> | null`

            List of domains to block fetching from

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations?: CitationsConfigParam | null`

            Citations configuration for fetched documents. Citations are disabled by default.

            - `enabled?: boolean`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `max_content_tokens?: number | null`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          - `max_uses?: number | null`

            Maximum number of times the tool can be used in the API request.

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

        - `WebSearchTool20260209`

          - `name: "web_search"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"web_search"`

          - `type: "web_search_20260209"`

            - `"web_search_20260209"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `allowed_domains?: Array<string> | null`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `blocked_domains?: Array<string> | null`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `max_uses?: number | null`

            Maximum number of times the tool can be used in the API request.

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

          - `user_location?: UserLocation | null`

            Parameters for the user's location. Used to provide more relevant search results.

            - `type: "approximate"`

              - `"approximate"`

            - `city?: string | null`

              The city of the user.

            - `country?: string | null`

              The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

            - `region?: string | null`

              The region of the user.

            - `timezone?: string | null`

              The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        - `WebFetchTool20260209`

          - `name: "web_fetch"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"web_fetch"`

          - `type: "web_fetch_20260209"`

            - `"web_fetch_20260209"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `allowed_domains?: Array<string> | null`

            List of domains to allow fetching from

          - `blocked_domains?: Array<string> | null`

            List of domains to block fetching from

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations?: CitationsConfigParam | null`

            Citations configuration for fetched documents. Citations are disabled by default.

            - `enabled?: boolean`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `max_content_tokens?: number | null`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          - `max_uses?: number | null`

            Maximum number of times the tool can be used in the API request.

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

        - `ToolSearchToolBm25_20251119`

          - `name: "tool_search_tool_bm25"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"tool_search_tool_bm25"`

          - `type: "tool_search_tool_bm25_20251119" | "tool_search_tool_bm25"`

            - `"tool_search_tool_bm25_20251119"`

            - `"tool_search_tool_bm25"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

        - `ToolSearchToolRegex20251119`

          - `name: "tool_search_tool_regex"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `"tool_search_tool_regex"`

          - `type: "tool_search_tool_regex_20251119" | "tool_search_tool_regex"`

            - `"tool_search_tool_regex_20251119"`

            - `"tool_search_tool_regex"`

          - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120">`

            - `"direct"`

            - `"code_execution_20250825"`

            - `"code_execution_20260120"`

          - `cache_control?: CacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

              - `"ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `defer_loading?: boolean`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `strict?: boolean`

            When true, guarantees schema validation on tool names and inputs

      - `top_k?: number`

        Only sample from the top K options for each subsequent token.

        Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

        Recommended for advanced use cases only. You usually only need to use `temperature`.

      - `top_p?: number`

        Use nucleus sampling.

        In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

        Recommended for advanced use cases only. You usually only need to use `temperature`.

### Returns

- `MessageBatch`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string | null`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `cancel_initiated_at: string | null`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `ended_at: string | null`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `processing_status: "in_progress" | "canceling" | "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: MessageBatchRequestCounts`

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

  - `results_url: string | null`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    - `"message_batch"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const messageBatch = await client.messages.batches.create({
  requests: [
    {
      custom_id: 'my-custom-id-1',
      params: {
        max_tokens: 1024,
        messages: [{ content: 'Hello, world', role: 'user' }],
        model: 'claude-opus-4-6',
      },
    },
  ],
});

console.log(messageBatch.id);
```

## Retrieve

`client.messages.batches.retrieve(stringmessageBatchID, RequestOptionsoptions?): MessageBatch`

**get** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

### Returns

- `MessageBatch`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string | null`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `cancel_initiated_at: string | null`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `ended_at: string | null`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `processing_status: "in_progress" | "canceling" | "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: MessageBatchRequestCounts`

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

  - `results_url: string | null`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    - `"message_batch"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const messageBatch = await client.messages.batches.retrieve('message_batch_id');

console.log(messageBatch.id);
```

## List

`client.messages.batches.list(BatchListParamsquery?, RequestOptionsoptions?): Page<MessageBatch>`

**get** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `query: BatchListParams`

  - `after_id?: string`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `before_id?: string`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `limit?: number`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

### Returns

- `MessageBatch`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string | null`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `cancel_initiated_at: string | null`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `ended_at: string | null`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `processing_status: "in_progress" | "canceling" | "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: MessageBatchRequestCounts`

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

  - `results_url: string | null`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    - `"message_batch"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const messageBatch of client.messages.batches.list()) {
  console.log(messageBatch.id);
}
```

## Cancel

`client.messages.batches.cancel(stringmessageBatchID, RequestOptionsoptions?): MessageBatch`

**post** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

### Returns

- `MessageBatch`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string | null`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `cancel_initiated_at: string | null`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `ended_at: string | null`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `processing_status: "in_progress" | "canceling" | "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: MessageBatchRequestCounts`

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

  - `results_url: string | null`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    - `"message_batch"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const messageBatch = await client.messages.batches.cancel('message_batch_id');

console.log(messageBatch.id);
```

## Delete

`client.messages.batches.delete(stringmessageBatchID, RequestOptionsoptions?): DeletedMessageBatch`

**delete** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

### Returns

- `DeletedMessageBatch`

  - `id: string`

    ID of the Message Batch.

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

    - `"message_batch_deleted"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const deletedMessageBatch = await client.messages.batches.delete('message_batch_id');

console.log(deletedMessageBatch.id);
```

## Results

`client.messages.batches.results(stringmessageBatchID, RequestOptionsoptions?): MessageBatchIndividualResponse | Stream<MessageBatchIndividualResponse>`

**get** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

### Returns

- `MessageBatchIndividualResponse`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `custom_id: string`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `result: MessageBatchResult`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `MessageBatchSucceededResult`

      - `message: Message`

        - `id: string`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `container: Container | null`

          Information about the container used in the request (for the code execution tool)

          - `id: string`

            Identifier for the container used in this request

          - `expires_at: string`

            The time at which the container will expire.

        - `content: Array<ContentBlock>`

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

          - `TextBlock`

            - `citations: Array<TextCitation> | null`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `CitationCharLocation`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_char_index: number`

                - `file_id: string | null`

                - `start_char_index: number`

                - `type: "char_location"`

                  - `"char_location"`

              - `CitationPageLocation`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_page_number: number`

                - `file_id: string | null`

                - `start_page_number: number`

                - `type: "page_location"`

                  - `"page_location"`

              - `CitationContentBlockLocation`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_block_index: number`

                - `file_id: string | null`

                - `start_block_index: number`

                - `type: "content_block_location"`

                  - `"content_block_location"`

              - `CitationsWebSearchResultLocation`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string | null`

                - `type: "web_search_result_location"`

                  - `"web_search_result_location"`

                - `url: string`

              - `CitationsSearchResultLocation`

                - `cited_text: string`

                - `end_block_index: number`

                - `search_result_index: number`

                - `source: string`

                - `start_block_index: number`

                - `title: string | null`

                - `type: "search_result_location"`

                  - `"search_result_location"`

            - `text: string`

            - `type: "text"`

              - `"text"`

          - `ThinkingBlock`

            - `signature: string`

            - `thinking: string`

            - `type: "thinking"`

              - `"thinking"`

          - `RedactedThinkingBlock`

            - `data: string`

            - `type: "redacted_thinking"`

              - `"redacted_thinking"`

          - `ToolUseBlock`

            - `id: string`

            - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `DirectCaller`

                Tool invocation directly from the model.

                - `type: "direct"`

                  - `"direct"`

              - `ServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

                  - `"code_execution_20250825"`

              - `ServerToolCaller20260120`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

                  - `"code_execution_20260120"`

            - `input: Record<string, unknown>`

            - `name: string`

            - `type: "tool_use"`

              - `"tool_use"`

          - `ServerToolUseBlock`

            - `id: string`

            - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `DirectCaller`

                Tool invocation directly from the model.

                - `type: "direct"`

                  - `"direct"`

              - `ServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

                  - `"code_execution_20250825"`

              - `ServerToolCaller20260120`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

                  - `"code_execution_20260120"`

            - `input: Record<string, unknown>`

            - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

              - `"web_search"`

              - `"web_fetch"`

              - `"code_execution"`

              - `"bash_code_execution"`

              - `"text_editor_code_execution"`

              - `"tool_search_tool_regex"`

              - `"tool_search_tool_bm25"`

            - `type: "server_tool_use"`

              - `"server_tool_use"`

          - `WebSearchToolResultBlock`

            - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `DirectCaller`

                Tool invocation directly from the model.

                - `type: "direct"`

                  - `"direct"`

              - `ServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

                  - `"code_execution_20250825"`

              - `ServerToolCaller20260120`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

                  - `"code_execution_20260120"`

            - `content: WebSearchToolResultBlockContent`

              - `WebSearchToolResultError`

                - `error_code: WebSearchToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"max_uses_exceeded"`

                  - `"too_many_requests"`

                  - `"query_too_long"`

                  - `"request_too_large"`

                - `type: "web_search_tool_result_error"`

                  - `"web_search_tool_result_error"`

              - `Array<WebSearchResultBlock>`

                - `encrypted_content: string`

                - `page_age: string | null`

                - `title: string`

                - `type: "web_search_result"`

                  - `"web_search_result"`

                - `url: string`

            - `tool_use_id: string`

            - `type: "web_search_tool_result"`

              - `"web_search_tool_result"`

          - `WebFetchToolResultBlock`

            - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `DirectCaller`

                Tool invocation directly from the model.

                - `type: "direct"`

                  - `"direct"`

              - `ServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

                  - `"code_execution_20250825"`

              - `ServerToolCaller20260120`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

                  - `"code_execution_20260120"`

            - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

              - `WebFetchToolResultErrorBlock`

                - `error_code: WebFetchToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"url_too_long"`

                  - `"url_not_allowed"`

                  - `"url_not_accessible"`

                  - `"unsupported_content_type"`

                  - `"too_many_requests"`

                  - `"max_uses_exceeded"`

                  - `"unavailable"`

                - `type: "web_fetch_tool_result_error"`

                  - `"web_fetch_tool_result_error"`

              - `WebFetchBlock`

                - `content: DocumentBlock`

                  - `citations: CitationsConfig | null`

                    Citation configuration for the document

                    - `enabled: boolean`

                  - `source: Base64PDFSource | PlainTextSource`

                    - `Base64PDFSource`

                      - `data: string`

                      - `media_type: "application/pdf"`

                        - `"application/pdf"`

                      - `type: "base64"`

                        - `"base64"`

                    - `PlainTextSource`

                      - `data: string`

                      - `media_type: "text/plain"`

                        - `"text/plain"`

                      - `type: "text"`

                        - `"text"`

                  - `title: string | null`

                    The title of the document

                  - `type: "document"`

                    - `"document"`

                - `retrieved_at: string | null`

                  ISO 8601 timestamp when the content was retrieved

                - `type: "web_fetch_result"`

                  - `"web_fetch_result"`

                - `url: string`

                  Fetched content URL

            - `tool_use_id: string`

            - `type: "web_fetch_tool_result"`

              - `"web_fetch_tool_result"`

          - `CodeExecutionToolResultBlock`

            - `content: CodeExecutionToolResultBlockContent`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `CodeExecutionToolResultError`

                - `error_code: CodeExecutionToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `type: "code_execution_tool_result_error"`

                  - `"code_execution_tool_result_error"`

              - `CodeExecutionResultBlock`

                - `content: Array<CodeExecutionOutputBlock>`

                  - `file_id: string`

                  - `type: "code_execution_output"`

                    - `"code_execution_output"`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

                - `type: "code_execution_result"`

                  - `"code_execution_result"`

              - `EncryptedCodeExecutionResultBlock`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `content: Array<CodeExecutionOutputBlock>`

                  - `file_id: string`

                  - `type: "code_execution_output"`

                    - `"code_execution_output"`

                - `encrypted_stdout: string`

                - `return_code: number`

                - `stderr: string`

                - `type: "encrypted_code_execution_result"`

                  - `"encrypted_code_execution_result"`

            - `tool_use_id: string`

            - `type: "code_execution_tool_result"`

              - `"code_execution_tool_result"`

          - `BashCodeExecutionToolResultBlock`

            - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

              - `BashCodeExecutionToolResultError`

                - `error_code: BashCodeExecutionToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"output_file_too_large"`

                - `type: "bash_code_execution_tool_result_error"`

                  - `"bash_code_execution_tool_result_error"`

              - `BashCodeExecutionResultBlock`

                - `content: Array<BashCodeExecutionOutputBlock>`

                  - `file_id: string`

                  - `type: "bash_code_execution_output"`

                    - `"bash_code_execution_output"`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

                - `type: "bash_code_execution_result"`

                  - `"bash_code_execution_result"`

            - `tool_use_id: string`

            - `type: "bash_code_execution_tool_result"`

              - `"bash_code_execution_tool_result"`

          - `TextEditorCodeExecutionToolResultBlock`

            - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

              - `TextEditorCodeExecutionToolResultError`

                - `error_code: TextEditorCodeExecutionToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"file_not_found"`

                - `error_message: string | null`

                - `type: "text_editor_code_execution_tool_result_error"`

                  - `"text_editor_code_execution_tool_result_error"`

              - `TextEditorCodeExecutionViewResultBlock`

                - `content: string`

                - `file_type: "text" | "image" | "pdf"`

                  - `"text"`

                  - `"image"`

                  - `"pdf"`

                - `num_lines: number | null`

                - `start_line: number | null`

                - `total_lines: number | null`

                - `type: "text_editor_code_execution_view_result"`

                  - `"text_editor_code_execution_view_result"`

              - `TextEditorCodeExecutionCreateResultBlock`

                - `is_file_update: boolean`

                - `type: "text_editor_code_execution_create_result"`

                  - `"text_editor_code_execution_create_result"`

              - `TextEditorCodeExecutionStrReplaceResultBlock`

                - `lines: Array<string> | null`

                - `new_lines: number | null`

                - `new_start: number | null`

                - `old_lines: number | null`

                - `old_start: number | null`

                - `type: "text_editor_code_execution_str_replace_result"`

                  - `"text_editor_code_execution_str_replace_result"`

            - `tool_use_id: string`

            - `type: "text_editor_code_execution_tool_result"`

              - `"text_editor_code_execution_tool_result"`

          - `ToolSearchToolResultBlock`

            - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

              - `ToolSearchToolResultError`

                - `error_code: ToolSearchToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `error_message: string | null`

                - `type: "tool_search_tool_result_error"`

                  - `"tool_search_tool_result_error"`

              - `ToolSearchToolSearchResultBlock`

                - `tool_references: Array<ToolReferenceBlock>`

                  - `tool_name: string`

                  - `type: "tool_reference"`

                    - `"tool_reference"`

                - `type: "tool_search_tool_search_result"`

                  - `"tool_search_tool_search_result"`

            - `tool_use_id: string`

            - `type: "tool_search_tool_result"`

              - `"tool_search_tool_result"`

          - `ContainerUploadBlock`

            Response model for a file uploaded to the container.

            - `file_id: string`

            - `type: "container_upload"`

              - `"container_upload"`

        - `model: Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-opus-4-5-20251101" | 19 more`

            - `"claude-opus-4-6"`

              Most intelligent model for building agents and coding

            - `"claude-sonnet-4-6"`

              Frontier intelligence at scale — built for coding, agents, and enterprise workflows

            - `"claude-opus-4-5-20251101"`

              Premium model combining maximum intelligence with practical performance

            - `"claude-opus-4-5"`

              Premium model combining maximum intelligence with practical performance

            - `"claude-3-7-sonnet-latest"`

              High-performance model with early extended thinking

            - `"claude-3-7-sonnet-20250219"`

              High-performance model with early extended thinking

            - `"claude-3-5-haiku-latest"`

              Fastest and most compact model for near-instant responsiveness

            - `"claude-3-5-haiku-20241022"`

              Our fastest model

            - `"claude-haiku-4-5"`

              Hybrid model, capable of near-instant responses and extended thinking

            - `"claude-haiku-4-5-20251001"`

              Hybrid model, capable of near-instant responses and extended thinking

            - `"claude-sonnet-4-20250514"`

              High-performance model with extended thinking

            - `"claude-sonnet-4-0"`

              High-performance model with extended thinking

            - `"claude-4-sonnet-20250514"`

              High-performance model with extended thinking

            - `"claude-sonnet-4-5"`

              Our best model for real-world agents and coding

            - `"claude-sonnet-4-5-20250929"`

              Our best model for real-world agents and coding

            - `"claude-opus-4-0"`

              Our most capable model

            - `"claude-opus-4-20250514"`

              Our most capable model

            - `"claude-4-opus-20250514"`

              Our most capable model

            - `"claude-opus-4-1-20250805"`

              Our most capable model

            - `"claude-3-opus-latest"`

              Excels at writing and complex tasks

            - `"claude-3-opus-20240229"`

              Excels at writing and complex tasks

            - `"claude-3-haiku-20240307"`

              Our previous most fast and cost-effective

          - `(string & {})`

        - `role: "assistant"`

          Conversational role of the generated message.

          This will always be `"assistant"`.

          - `"assistant"`

        - `stop_reason: StopReason | null`

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

          - `"refusal"`

        - `stop_sequence: string | null`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `type: "message"`

          Object type.

          For Messages, this is always `"message"`.

          - `"message"`

        - `usage: Usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `cache_creation: CacheCreation | null`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

          - `cache_creation_input_tokens: number | null`

            The number of input tokens used to create the cache entry.

          - `cache_read_input_tokens: number | null`

            The number of input tokens read from the cache.

          - `inference_geo: string | null`

            The geographic region where inference was performed for this request.

          - `input_tokens: number`

            The number of input tokens which were used.

          - `output_tokens: number`

            The number of output tokens which were used.

          - `server_tool_use: ServerToolUsage | null`

            The number of server tool requests.

            - `web_fetch_requests: number`

              The number of web fetch tool requests.

            - `web_search_requests: number`

              The number of web search tool requests.

          - `service_tier: "standard" | "priority" | "batch" | null`

            If the request used the priority, standard, or batch tier.

            - `"standard"`

            - `"priority"`

            - `"batch"`

      - `type: "succeeded"`

        - `"succeeded"`

    - `MessageBatchErroredResult`

      - `error: ErrorResponse`

        - `error: ErrorObject`

          - `InvalidRequestError`

            - `message: string`

            - `type: "invalid_request_error"`

              - `"invalid_request_error"`

          - `AuthenticationError`

            - `message: string`

            - `type: "authentication_error"`

              - `"authentication_error"`

          - `BillingError`

            - `message: string`

            - `type: "billing_error"`

              - `"billing_error"`

          - `PermissionError`

            - `message: string`

            - `type: "permission_error"`

              - `"permission_error"`

          - `NotFoundError`

            - `message: string`

            - `type: "not_found_error"`

              - `"not_found_error"`

          - `RateLimitError`

            - `message: string`

            - `type: "rate_limit_error"`

              - `"rate_limit_error"`

          - `GatewayTimeoutError`

            - `message: string`

            - `type: "timeout_error"`

              - `"timeout_error"`

          - `APIErrorObject`

            - `message: string`

            - `type: "api_error"`

              - `"api_error"`

          - `OverloadedError`

            - `message: string`

            - `type: "overloaded_error"`

              - `"overloaded_error"`

        - `request_id: string | null`

        - `type: "error"`

          - `"error"`

      - `type: "errored"`

        - `"errored"`

    - `MessageBatchCanceledResult`

      - `type: "canceled"`

        - `"canceled"`

    - `MessageBatchExpiredResult`

      - `type: "expired"`

        - `"expired"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const messageBatchIndividualResponse = await client.messages.batches.results('message_batch_id');

console.log(messageBatchIndividualResponse.custom_id);
```

## Domain Types

### Deleted Message Batch

- `DeletedMessageBatch`

  - `id: string`

    ID of the Message Batch.

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

    - `"message_batch_deleted"`

### Message Batch

- `MessageBatch`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string | null`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `cancel_initiated_at: string | null`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `ended_at: string | null`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `processing_status: "in_progress" | "canceling" | "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: MessageBatchRequestCounts`

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

  - `results_url: string | null`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    - `"message_batch"`

### Message Batch Canceled Result

- `MessageBatchCanceledResult`

  - `type: "canceled"`

    - `"canceled"`

### Message Batch Errored Result

- `MessageBatchErroredResult`

  - `error: ErrorResponse`

    - `error: ErrorObject`

      - `InvalidRequestError`

        - `message: string`

        - `type: "invalid_request_error"`

          - `"invalid_request_error"`

      - `AuthenticationError`

        - `message: string`

        - `type: "authentication_error"`

          - `"authentication_error"`

      - `BillingError`

        - `message: string`

        - `type: "billing_error"`

          - `"billing_error"`

      - `PermissionError`

        - `message: string`

        - `type: "permission_error"`

          - `"permission_error"`

      - `NotFoundError`

        - `message: string`

        - `type: "not_found_error"`

          - `"not_found_error"`

      - `RateLimitError`

        - `message: string`

        - `type: "rate_limit_error"`

          - `"rate_limit_error"`

      - `GatewayTimeoutError`

        - `message: string`

        - `type: "timeout_error"`

          - `"timeout_error"`

      - `APIErrorObject`

        - `message: string`

        - `type: "api_error"`

          - `"api_error"`

      - `OverloadedError`

        - `message: string`

        - `type: "overloaded_error"`

          - `"overloaded_error"`

    - `request_id: string | null`

    - `type: "error"`

      - `"error"`

  - `type: "errored"`

    - `"errored"`

### Message Batch Expired Result

- `MessageBatchExpiredResult`

  - `type: "expired"`

    - `"expired"`

### Message Batch Individual Response

- `MessageBatchIndividualResponse`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `custom_id: string`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `result: MessageBatchResult`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `MessageBatchSucceededResult`

      - `message: Message`

        - `id: string`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `container: Container | null`

          Information about the container used in the request (for the code execution tool)

          - `id: string`

            Identifier for the container used in this request

          - `expires_at: string`

            The time at which the container will expire.

        - `content: Array<ContentBlock>`

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

          - `TextBlock`

            - `citations: Array<TextCitation> | null`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `CitationCharLocation`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_char_index: number`

                - `file_id: string | null`

                - `start_char_index: number`

                - `type: "char_location"`

                  - `"char_location"`

              - `CitationPageLocation`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_page_number: number`

                - `file_id: string | null`

                - `start_page_number: number`

                - `type: "page_location"`

                  - `"page_location"`

              - `CitationContentBlockLocation`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string | null`

                - `end_block_index: number`

                - `file_id: string | null`

                - `start_block_index: number`

                - `type: "content_block_location"`

                  - `"content_block_location"`

              - `CitationsWebSearchResultLocation`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string | null`

                - `type: "web_search_result_location"`

                  - `"web_search_result_location"`

                - `url: string`

              - `CitationsSearchResultLocation`

                - `cited_text: string`

                - `end_block_index: number`

                - `search_result_index: number`

                - `source: string`

                - `start_block_index: number`

                - `title: string | null`

                - `type: "search_result_location"`

                  - `"search_result_location"`

            - `text: string`

            - `type: "text"`

              - `"text"`

          - `ThinkingBlock`

            - `signature: string`

            - `thinking: string`

            - `type: "thinking"`

              - `"thinking"`

          - `RedactedThinkingBlock`

            - `data: string`

            - `type: "redacted_thinking"`

              - `"redacted_thinking"`

          - `ToolUseBlock`

            - `id: string`

            - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `DirectCaller`

                Tool invocation directly from the model.

                - `type: "direct"`

                  - `"direct"`

              - `ServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

                  - `"code_execution_20250825"`

              - `ServerToolCaller20260120`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

                  - `"code_execution_20260120"`

            - `input: Record<string, unknown>`

            - `name: string`

            - `type: "tool_use"`

              - `"tool_use"`

          - `ServerToolUseBlock`

            - `id: string`

            - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `DirectCaller`

                Tool invocation directly from the model.

                - `type: "direct"`

                  - `"direct"`

              - `ServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

                  - `"code_execution_20250825"`

              - `ServerToolCaller20260120`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

                  - `"code_execution_20260120"`

            - `input: Record<string, unknown>`

            - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

              - `"web_search"`

              - `"web_fetch"`

              - `"code_execution"`

              - `"bash_code_execution"`

              - `"text_editor_code_execution"`

              - `"tool_search_tool_regex"`

              - `"tool_search_tool_bm25"`

            - `type: "server_tool_use"`

              - `"server_tool_use"`

          - `WebSearchToolResultBlock`

            - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `DirectCaller`

                Tool invocation directly from the model.

                - `type: "direct"`

                  - `"direct"`

              - `ServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

                  - `"code_execution_20250825"`

              - `ServerToolCaller20260120`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

                  - `"code_execution_20260120"`

            - `content: WebSearchToolResultBlockContent`

              - `WebSearchToolResultError`

                - `error_code: WebSearchToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"max_uses_exceeded"`

                  - `"too_many_requests"`

                  - `"query_too_long"`

                  - `"request_too_large"`

                - `type: "web_search_tool_result_error"`

                  - `"web_search_tool_result_error"`

              - `Array<WebSearchResultBlock>`

                - `encrypted_content: string`

                - `page_age: string | null`

                - `title: string`

                - `type: "web_search_result"`

                  - `"web_search_result"`

                - `url: string`

            - `tool_use_id: string`

            - `type: "web_search_tool_result"`

              - `"web_search_tool_result"`

          - `WebFetchToolResultBlock`

            - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `DirectCaller`

                Tool invocation directly from the model.

                - `type: "direct"`

                  - `"direct"`

              - `ServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                - `type: "code_execution_20250825"`

                  - `"code_execution_20250825"`

              - `ServerToolCaller20260120`

                - `tool_id: string`

                - `type: "code_execution_20260120"`

                  - `"code_execution_20260120"`

            - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

              - `WebFetchToolResultErrorBlock`

                - `error_code: WebFetchToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"url_too_long"`

                  - `"url_not_allowed"`

                  - `"url_not_accessible"`

                  - `"unsupported_content_type"`

                  - `"too_many_requests"`

                  - `"max_uses_exceeded"`

                  - `"unavailable"`

                - `type: "web_fetch_tool_result_error"`

                  - `"web_fetch_tool_result_error"`

              - `WebFetchBlock`

                - `content: DocumentBlock`

                  - `citations: CitationsConfig | null`

                    Citation configuration for the document

                    - `enabled: boolean`

                  - `source: Base64PDFSource | PlainTextSource`

                    - `Base64PDFSource`

                      - `data: string`

                      - `media_type: "application/pdf"`

                        - `"application/pdf"`

                      - `type: "base64"`

                        - `"base64"`

                    - `PlainTextSource`

                      - `data: string`

                      - `media_type: "text/plain"`

                        - `"text/plain"`

                      - `type: "text"`

                        - `"text"`

                  - `title: string | null`

                    The title of the document

                  - `type: "document"`

                    - `"document"`

                - `retrieved_at: string | null`

                  ISO 8601 timestamp when the content was retrieved

                - `type: "web_fetch_result"`

                  - `"web_fetch_result"`

                - `url: string`

                  Fetched content URL

            - `tool_use_id: string`

            - `type: "web_fetch_tool_result"`

              - `"web_fetch_tool_result"`

          - `CodeExecutionToolResultBlock`

            - `content: CodeExecutionToolResultBlockContent`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `CodeExecutionToolResultError`

                - `error_code: CodeExecutionToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `type: "code_execution_tool_result_error"`

                  - `"code_execution_tool_result_error"`

              - `CodeExecutionResultBlock`

                - `content: Array<CodeExecutionOutputBlock>`

                  - `file_id: string`

                  - `type: "code_execution_output"`

                    - `"code_execution_output"`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

                - `type: "code_execution_result"`

                  - `"code_execution_result"`

              - `EncryptedCodeExecutionResultBlock`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `content: Array<CodeExecutionOutputBlock>`

                  - `file_id: string`

                  - `type: "code_execution_output"`

                    - `"code_execution_output"`

                - `encrypted_stdout: string`

                - `return_code: number`

                - `stderr: string`

                - `type: "encrypted_code_execution_result"`

                  - `"encrypted_code_execution_result"`

            - `tool_use_id: string`

            - `type: "code_execution_tool_result"`

              - `"code_execution_tool_result"`

          - `BashCodeExecutionToolResultBlock`

            - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

              - `BashCodeExecutionToolResultError`

                - `error_code: BashCodeExecutionToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"output_file_too_large"`

                - `type: "bash_code_execution_tool_result_error"`

                  - `"bash_code_execution_tool_result_error"`

              - `BashCodeExecutionResultBlock`

                - `content: Array<BashCodeExecutionOutputBlock>`

                  - `file_id: string`

                  - `type: "bash_code_execution_output"`

                    - `"bash_code_execution_output"`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

                - `type: "bash_code_execution_result"`

                  - `"bash_code_execution_result"`

            - `tool_use_id: string`

            - `type: "bash_code_execution_tool_result"`

              - `"bash_code_execution_tool_result"`

          - `TextEditorCodeExecutionToolResultBlock`

            - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

              - `TextEditorCodeExecutionToolResultError`

                - `error_code: TextEditorCodeExecutionToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"file_not_found"`

                - `error_message: string | null`

                - `type: "text_editor_code_execution_tool_result_error"`

                  - `"text_editor_code_execution_tool_result_error"`

              - `TextEditorCodeExecutionViewResultBlock`

                - `content: string`

                - `file_type: "text" | "image" | "pdf"`

                  - `"text"`

                  - `"image"`

                  - `"pdf"`

                - `num_lines: number | null`

                - `start_line: number | null`

                - `total_lines: number | null`

                - `type: "text_editor_code_execution_view_result"`

                  - `"text_editor_code_execution_view_result"`

              - `TextEditorCodeExecutionCreateResultBlock`

                - `is_file_update: boolean`

                - `type: "text_editor_code_execution_create_result"`

                  - `"text_editor_code_execution_create_result"`

              - `TextEditorCodeExecutionStrReplaceResultBlock`

                - `lines: Array<string> | null`

                - `new_lines: number | null`

                - `new_start: number | null`

                - `old_lines: number | null`

                - `old_start: number | null`

                - `type: "text_editor_code_execution_str_replace_result"`

                  - `"text_editor_code_execution_str_replace_result"`

            - `tool_use_id: string`

            - `type: "text_editor_code_execution_tool_result"`

              - `"text_editor_code_execution_tool_result"`

          - `ToolSearchToolResultBlock`

            - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

              - `ToolSearchToolResultError`

                - `error_code: ToolSearchToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `error_message: string | null`

                - `type: "tool_search_tool_result_error"`

                  - `"tool_search_tool_result_error"`

              - `ToolSearchToolSearchResultBlock`

                - `tool_references: Array<ToolReferenceBlock>`

                  - `tool_name: string`

                  - `type: "tool_reference"`

                    - `"tool_reference"`

                - `type: "tool_search_tool_search_result"`

                  - `"tool_search_tool_search_result"`

            - `tool_use_id: string`

            - `type: "tool_search_tool_result"`

              - `"tool_search_tool_result"`

          - `ContainerUploadBlock`

            Response model for a file uploaded to the container.

            - `file_id: string`

            - `type: "container_upload"`

              - `"container_upload"`

        - `model: Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-opus-4-5-20251101" | 19 more`

            - `"claude-opus-4-6"`

              Most intelligent model for building agents and coding

            - `"claude-sonnet-4-6"`

              Frontier intelligence at scale — built for coding, agents, and enterprise workflows

            - `"claude-opus-4-5-20251101"`

              Premium model combining maximum intelligence with practical performance

            - `"claude-opus-4-5"`

              Premium model combining maximum intelligence with practical performance

            - `"claude-3-7-sonnet-latest"`

              High-performance model with early extended thinking

            - `"claude-3-7-sonnet-20250219"`

              High-performance model with early extended thinking

            - `"claude-3-5-haiku-latest"`

              Fastest and most compact model for near-instant responsiveness

            - `"claude-3-5-haiku-20241022"`

              Our fastest model

            - `"claude-haiku-4-5"`

              Hybrid model, capable of near-instant responses and extended thinking

            - `"claude-haiku-4-5-20251001"`

              Hybrid model, capable of near-instant responses and extended thinking

            - `"claude-sonnet-4-20250514"`

              High-performance model with extended thinking

            - `"claude-sonnet-4-0"`

              High-performance model with extended thinking

            - `"claude-4-sonnet-20250514"`

              High-performance model with extended thinking

            - `"claude-sonnet-4-5"`

              Our best model for real-world agents and coding

            - `"claude-sonnet-4-5-20250929"`

              Our best model for real-world agents and coding

            - `"claude-opus-4-0"`

              Our most capable model

            - `"claude-opus-4-20250514"`

              Our most capable model

            - `"claude-4-opus-20250514"`

              Our most capable model

            - `"claude-opus-4-1-20250805"`

              Our most capable model

            - `"claude-3-opus-latest"`

              Excels at writing and complex tasks

            - `"claude-3-opus-20240229"`

              Excels at writing and complex tasks

            - `"claude-3-haiku-20240307"`

              Our previous most fast and cost-effective

          - `(string & {})`

        - `role: "assistant"`

          Conversational role of the generated message.

          This will always be `"assistant"`.

          - `"assistant"`

        - `stop_reason: StopReason | null`

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

          - `"refusal"`

        - `stop_sequence: string | null`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `type: "message"`

          Object type.

          For Messages, this is always `"message"`.

          - `"message"`

        - `usage: Usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `cache_creation: CacheCreation | null`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

          - `cache_creation_input_tokens: number | null`

            The number of input tokens used to create the cache entry.

          - `cache_read_input_tokens: number | null`

            The number of input tokens read from the cache.

          - `inference_geo: string | null`

            The geographic region where inference was performed for this request.

          - `input_tokens: number`

            The number of input tokens which were used.

          - `output_tokens: number`

            The number of output tokens which were used.

          - `server_tool_use: ServerToolUsage | null`

            The number of server tool requests.

            - `web_fetch_requests: number`

              The number of web fetch tool requests.

            - `web_search_requests: number`

              The number of web search tool requests.

          - `service_tier: "standard" | "priority" | "batch" | null`

            If the request used the priority, standard, or batch tier.

            - `"standard"`

            - `"priority"`

            - `"batch"`

      - `type: "succeeded"`

        - `"succeeded"`

    - `MessageBatchErroredResult`

      - `error: ErrorResponse`

        - `error: ErrorObject`

          - `InvalidRequestError`

            - `message: string`

            - `type: "invalid_request_error"`

              - `"invalid_request_error"`

          - `AuthenticationError`

            - `message: string`

            - `type: "authentication_error"`

              - `"authentication_error"`

          - `BillingError`

            - `message: string`

            - `type: "billing_error"`

              - `"billing_error"`

          - `PermissionError`

            - `message: string`

            - `type: "permission_error"`

              - `"permission_error"`

          - `NotFoundError`

            - `message: string`

            - `type: "not_found_error"`

              - `"not_found_error"`

          - `RateLimitError`

            - `message: string`

            - `type: "rate_limit_error"`

              - `"rate_limit_error"`

          - `GatewayTimeoutError`

            - `message: string`

            - `type: "timeout_error"`

              - `"timeout_error"`

          - `APIErrorObject`

            - `message: string`

            - `type: "api_error"`

              - `"api_error"`

          - `OverloadedError`

            - `message: string`

            - `type: "overloaded_error"`

              - `"overloaded_error"`

        - `request_id: string | null`

        - `type: "error"`

          - `"error"`

      - `type: "errored"`

        - `"errored"`

    - `MessageBatchCanceledResult`

      - `type: "canceled"`

        - `"canceled"`

    - `MessageBatchExpiredResult`

      - `type: "expired"`

        - `"expired"`

### Message Batch Request Counts

- `MessageBatchRequestCounts`

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

### Message Batch Result

- `MessageBatchResult = MessageBatchSucceededResult | MessageBatchErroredResult | MessageBatchCanceledResult | MessageBatchExpiredResult`

  Processing result for this request.

  Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

  - `MessageBatchSucceededResult`

    - `message: Message`

      - `id: string`

        Unique object identifier.

        The format and length of IDs may change over time.

      - `container: Container | null`

        Information about the container used in the request (for the code execution tool)

        - `id: string`

          Identifier for the container used in this request

        - `expires_at: string`

          The time at which the container will expire.

      - `content: Array<ContentBlock>`

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

        - `TextBlock`

          - `citations: Array<TextCitation> | null`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `CitationCharLocation`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_char_index: number`

              - `file_id: string | null`

              - `start_char_index: number`

              - `type: "char_location"`

                - `"char_location"`

            - `CitationPageLocation`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_page_number: number`

              - `file_id: string | null`

              - `start_page_number: number`

              - `type: "page_location"`

                - `"page_location"`

            - `CitationContentBlockLocation`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string | null`

              - `end_block_index: number`

              - `file_id: string | null`

              - `start_block_index: number`

              - `type: "content_block_location"`

                - `"content_block_location"`

            - `CitationsWebSearchResultLocation`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string | null`

              - `type: "web_search_result_location"`

                - `"web_search_result_location"`

              - `url: string`

            - `CitationsSearchResultLocation`

              - `cited_text: string`

              - `end_block_index: number`

              - `search_result_index: number`

              - `source: string`

              - `start_block_index: number`

              - `title: string | null`

              - `type: "search_result_location"`

                - `"search_result_location"`

          - `text: string`

          - `type: "text"`

            - `"text"`

        - `ThinkingBlock`

          - `signature: string`

          - `thinking: string`

          - `type: "thinking"`

            - `"thinking"`

        - `RedactedThinkingBlock`

          - `data: string`

          - `type: "redacted_thinking"`

            - `"redacted_thinking"`

        - `ToolUseBlock`

          - `id: string`

          - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `DirectCaller`

              Tool invocation directly from the model.

              - `type: "direct"`

                - `"direct"`

            - `ServerToolCaller`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

              - `type: "code_execution_20250825"`

                - `"code_execution_20250825"`

            - `ServerToolCaller20260120`

              - `tool_id: string`

              - `type: "code_execution_20260120"`

                - `"code_execution_20260120"`

          - `input: Record<string, unknown>`

          - `name: string`

          - `type: "tool_use"`

            - `"tool_use"`

        - `ServerToolUseBlock`

          - `id: string`

          - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `DirectCaller`

              Tool invocation directly from the model.

              - `type: "direct"`

                - `"direct"`

            - `ServerToolCaller`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

              - `type: "code_execution_20250825"`

                - `"code_execution_20250825"`

            - `ServerToolCaller20260120`

              - `tool_id: string`

              - `type: "code_execution_20260120"`

                - `"code_execution_20260120"`

          - `input: Record<string, unknown>`

          - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

            - `"web_search"`

            - `"web_fetch"`

            - `"code_execution"`

            - `"bash_code_execution"`

            - `"text_editor_code_execution"`

            - `"tool_search_tool_regex"`

            - `"tool_search_tool_bm25"`

          - `type: "server_tool_use"`

            - `"server_tool_use"`

        - `WebSearchToolResultBlock`

          - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `DirectCaller`

              Tool invocation directly from the model.

              - `type: "direct"`

                - `"direct"`

            - `ServerToolCaller`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

              - `type: "code_execution_20250825"`

                - `"code_execution_20250825"`

            - `ServerToolCaller20260120`

              - `tool_id: string`

              - `type: "code_execution_20260120"`

                - `"code_execution_20260120"`

          - `content: WebSearchToolResultBlockContent`

            - `WebSearchToolResultError`

              - `error_code: WebSearchToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"max_uses_exceeded"`

                - `"too_many_requests"`

                - `"query_too_long"`

                - `"request_too_large"`

              - `type: "web_search_tool_result_error"`

                - `"web_search_tool_result_error"`

            - `Array<WebSearchResultBlock>`

              - `encrypted_content: string`

              - `page_age: string | null`

              - `title: string`

              - `type: "web_search_result"`

                - `"web_search_result"`

              - `url: string`

          - `tool_use_id: string`

          - `type: "web_search_tool_result"`

            - `"web_search_tool_result"`

        - `WebFetchToolResultBlock`

          - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `DirectCaller`

              Tool invocation directly from the model.

              - `type: "direct"`

                - `"direct"`

            - `ServerToolCaller`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

              - `type: "code_execution_20250825"`

                - `"code_execution_20250825"`

            - `ServerToolCaller20260120`

              - `tool_id: string`

              - `type: "code_execution_20260120"`

                - `"code_execution_20260120"`

          - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

            - `WebFetchToolResultErrorBlock`

              - `error_code: WebFetchToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"url_too_long"`

                - `"url_not_allowed"`

                - `"url_not_accessible"`

                - `"unsupported_content_type"`

                - `"too_many_requests"`

                - `"max_uses_exceeded"`

                - `"unavailable"`

              - `type: "web_fetch_tool_result_error"`

                - `"web_fetch_tool_result_error"`

            - `WebFetchBlock`

              - `content: DocumentBlock`

                - `citations: CitationsConfig | null`

                  Citation configuration for the document

                  - `enabled: boolean`

                - `source: Base64PDFSource | PlainTextSource`

                  - `Base64PDFSource`

                    - `data: string`

                    - `media_type: "application/pdf"`

                      - `"application/pdf"`

                    - `type: "base64"`

                      - `"base64"`

                  - `PlainTextSource`

                    - `data: string`

                    - `media_type: "text/plain"`

                      - `"text/plain"`

                    - `type: "text"`

                      - `"text"`

                - `title: string | null`

                  The title of the document

                - `type: "document"`

                  - `"document"`

              - `retrieved_at: string | null`

                ISO 8601 timestamp when the content was retrieved

              - `type: "web_fetch_result"`

                - `"web_fetch_result"`

              - `url: string`

                Fetched content URL

          - `tool_use_id: string`

          - `type: "web_fetch_tool_result"`

            - `"web_fetch_tool_result"`

        - `CodeExecutionToolResultBlock`

          - `content: CodeExecutionToolResultBlockContent`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `CodeExecutionToolResultError`

              - `error_code: CodeExecutionToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

              - `type: "code_execution_tool_result_error"`

                - `"code_execution_tool_result_error"`

            - `CodeExecutionResultBlock`

              - `content: Array<CodeExecutionOutputBlock>`

                - `file_id: string`

                - `type: "code_execution_output"`

                  - `"code_execution_output"`

              - `return_code: number`

              - `stderr: string`

              - `stdout: string`

              - `type: "code_execution_result"`

                - `"code_execution_result"`

            - `EncryptedCodeExecutionResultBlock`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `content: Array<CodeExecutionOutputBlock>`

                - `file_id: string`

                - `type: "code_execution_output"`

                  - `"code_execution_output"`

              - `encrypted_stdout: string`

              - `return_code: number`

              - `stderr: string`

              - `type: "encrypted_code_execution_result"`

                - `"encrypted_code_execution_result"`

          - `tool_use_id: string`

          - `type: "code_execution_tool_result"`

            - `"code_execution_tool_result"`

        - `BashCodeExecutionToolResultBlock`

          - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

            - `BashCodeExecutionToolResultError`

              - `error_code: BashCodeExecutionToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

                - `"output_file_too_large"`

              - `type: "bash_code_execution_tool_result_error"`

                - `"bash_code_execution_tool_result_error"`

            - `BashCodeExecutionResultBlock`

              - `content: Array<BashCodeExecutionOutputBlock>`

                - `file_id: string`

                - `type: "bash_code_execution_output"`

                  - `"bash_code_execution_output"`

              - `return_code: number`

              - `stderr: string`

              - `stdout: string`

              - `type: "bash_code_execution_result"`

                - `"bash_code_execution_result"`

          - `tool_use_id: string`

          - `type: "bash_code_execution_tool_result"`

            - `"bash_code_execution_tool_result"`

        - `TextEditorCodeExecutionToolResultBlock`

          - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

            - `TextEditorCodeExecutionToolResultError`

              - `error_code: TextEditorCodeExecutionToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

                - `"file_not_found"`

              - `error_message: string | null`

              - `type: "text_editor_code_execution_tool_result_error"`

                - `"text_editor_code_execution_tool_result_error"`

            - `TextEditorCodeExecutionViewResultBlock`

              - `content: string`

              - `file_type: "text" | "image" | "pdf"`

                - `"text"`

                - `"image"`

                - `"pdf"`

              - `num_lines: number | null`

              - `start_line: number | null`

              - `total_lines: number | null`

              - `type: "text_editor_code_execution_view_result"`

                - `"text_editor_code_execution_view_result"`

            - `TextEditorCodeExecutionCreateResultBlock`

              - `is_file_update: boolean`

              - `type: "text_editor_code_execution_create_result"`

                - `"text_editor_code_execution_create_result"`

            - `TextEditorCodeExecutionStrReplaceResultBlock`

              - `lines: Array<string> | null`

              - `new_lines: number | null`

              - `new_start: number | null`

              - `old_lines: number | null`

              - `old_start: number | null`

              - `type: "text_editor_code_execution_str_replace_result"`

                - `"text_editor_code_execution_str_replace_result"`

          - `tool_use_id: string`

          - `type: "text_editor_code_execution_tool_result"`

            - `"text_editor_code_execution_tool_result"`

        - `ToolSearchToolResultBlock`

          - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

            - `ToolSearchToolResultError`

              - `error_code: ToolSearchToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

              - `error_message: string | null`

              - `type: "tool_search_tool_result_error"`

                - `"tool_search_tool_result_error"`

            - `ToolSearchToolSearchResultBlock`

              - `tool_references: Array<ToolReferenceBlock>`

                - `tool_name: string`

                - `type: "tool_reference"`

                  - `"tool_reference"`

              - `type: "tool_search_tool_search_result"`

                - `"tool_search_tool_search_result"`

          - `tool_use_id: string`

          - `type: "tool_search_tool_result"`

            - `"tool_search_tool_result"`

        - `ContainerUploadBlock`

          Response model for a file uploaded to the container.

          - `file_id: string`

          - `type: "container_upload"`

            - `"container_upload"`

      - `model: Model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-opus-4-5-20251101" | 19 more`

          - `"claude-opus-4-6"`

            Most intelligent model for building agents and coding

          - `"claude-sonnet-4-6"`

            Frontier intelligence at scale — built for coding, agents, and enterprise workflows

          - `"claude-opus-4-5-20251101"`

            Premium model combining maximum intelligence with practical performance

          - `"claude-opus-4-5"`

            Premium model combining maximum intelligence with practical performance

          - `"claude-3-7-sonnet-latest"`

            High-performance model with early extended thinking

          - `"claude-3-7-sonnet-20250219"`

            High-performance model with early extended thinking

          - `"claude-3-5-haiku-latest"`

            Fastest and most compact model for near-instant responsiveness

          - `"claude-3-5-haiku-20241022"`

            Our fastest model

          - `"claude-haiku-4-5"`

            Hybrid model, capable of near-instant responses and extended thinking

          - `"claude-haiku-4-5-20251001"`

            Hybrid model, capable of near-instant responses and extended thinking

          - `"claude-sonnet-4-20250514"`

            High-performance model with extended thinking

          - `"claude-sonnet-4-0"`

            High-performance model with extended thinking

          - `"claude-4-sonnet-20250514"`

            High-performance model with extended thinking

          - `"claude-sonnet-4-5"`

            Our best model for real-world agents and coding

          - `"claude-sonnet-4-5-20250929"`

            Our best model for real-world agents and coding

          - `"claude-opus-4-0"`

            Our most capable model

          - `"claude-opus-4-20250514"`

            Our most capable model

          - `"claude-4-opus-20250514"`

            Our most capable model

          - `"claude-opus-4-1-20250805"`

            Our most capable model

          - `"claude-3-opus-latest"`

            Excels at writing and complex tasks

          - `"claude-3-opus-20240229"`

            Excels at writing and complex tasks

          - `"claude-3-haiku-20240307"`

            Our previous most fast and cost-effective

        - `(string & {})`

      - `role: "assistant"`

        Conversational role of the generated message.

        This will always be `"assistant"`.

        - `"assistant"`

      - `stop_reason: StopReason | null`

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

        - `"refusal"`

      - `stop_sequence: string | null`

        Which custom stop sequence was generated, if any.

        This value will be a non-null string if one of your custom stop sequences was generated.

      - `type: "message"`

        Object type.

        For Messages, this is always `"message"`.

        - `"message"`

      - `usage: Usage`

        Billing and rate-limit usage.

        Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

        Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

        For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

        Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

        - `cache_creation: CacheCreation | null`

          Breakdown of cached tokens by TTL

          - `ephemeral_1h_input_tokens: number`

            The number of input tokens used to create the 1 hour cache entry.

          - `ephemeral_5m_input_tokens: number`

            The number of input tokens used to create the 5 minute cache entry.

        - `cache_creation_input_tokens: number | null`

          The number of input tokens used to create the cache entry.

        - `cache_read_input_tokens: number | null`

          The number of input tokens read from the cache.

        - `inference_geo: string | null`

          The geographic region where inference was performed for this request.

        - `input_tokens: number`

          The number of input tokens which were used.

        - `output_tokens: number`

          The number of output tokens which were used.

        - `server_tool_use: ServerToolUsage | null`

          The number of server tool requests.

          - `web_fetch_requests: number`

            The number of web fetch tool requests.

          - `web_search_requests: number`

            The number of web search tool requests.

        - `service_tier: "standard" | "priority" | "batch" | null`

          If the request used the priority, standard, or batch tier.

          - `"standard"`

          - `"priority"`

          - `"batch"`

    - `type: "succeeded"`

      - `"succeeded"`

  - `MessageBatchErroredResult`

    - `error: ErrorResponse`

      - `error: ErrorObject`

        - `InvalidRequestError`

          - `message: string`

          - `type: "invalid_request_error"`

            - `"invalid_request_error"`

        - `AuthenticationError`

          - `message: string`

          - `type: "authentication_error"`

            - `"authentication_error"`

        - `BillingError`

          - `message: string`

          - `type: "billing_error"`

            - `"billing_error"`

        - `PermissionError`

          - `message: string`

          - `type: "permission_error"`

            - `"permission_error"`

        - `NotFoundError`

          - `message: string`

          - `type: "not_found_error"`

            - `"not_found_error"`

        - `RateLimitError`

          - `message: string`

          - `type: "rate_limit_error"`

            - `"rate_limit_error"`

        - `GatewayTimeoutError`

          - `message: string`

          - `type: "timeout_error"`

            - `"timeout_error"`

        - `APIErrorObject`

          - `message: string`

          - `type: "api_error"`

            - `"api_error"`

        - `OverloadedError`

          - `message: string`

          - `type: "overloaded_error"`

            - `"overloaded_error"`

      - `request_id: string | null`

      - `type: "error"`

        - `"error"`

    - `type: "errored"`

      - `"errored"`

  - `MessageBatchCanceledResult`

    - `type: "canceled"`

      - `"canceled"`

  - `MessageBatchExpiredResult`

    - `type: "expired"`

      - `"expired"`

### Message Batch Succeeded Result

- `MessageBatchSucceededResult`

  - `message: Message`

    - `id: string`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `container: Container | null`

      Information about the container used in the request (for the code execution tool)

      - `id: string`

        Identifier for the container used in this request

      - `expires_at: string`

        The time at which the container will expire.

    - `content: Array<ContentBlock>`

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

      - `TextBlock`

        - `citations: Array<TextCitation> | null`

          Citations supporting the text block.

          The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `CitationCharLocation`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_char_index: number`

            - `file_id: string | null`

            - `start_char_index: number`

            - `type: "char_location"`

              - `"char_location"`

          - `CitationPageLocation`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_page_number: number`

            - `file_id: string | null`

            - `start_page_number: number`

            - `type: "page_location"`

              - `"page_location"`

          - `CitationContentBlockLocation`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string | null`

            - `end_block_index: number`

            - `file_id: string | null`

            - `start_block_index: number`

            - `type: "content_block_location"`

              - `"content_block_location"`

          - `CitationsWebSearchResultLocation`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string | null`

            - `type: "web_search_result_location"`

              - `"web_search_result_location"`

            - `url: string`

          - `CitationsSearchResultLocation`

            - `cited_text: string`

            - `end_block_index: number`

            - `search_result_index: number`

            - `source: string`

            - `start_block_index: number`

            - `title: string | null`

            - `type: "search_result_location"`

              - `"search_result_location"`

        - `text: string`

        - `type: "text"`

          - `"text"`

      - `ThinkingBlock`

        - `signature: string`

        - `thinking: string`

        - `type: "thinking"`

          - `"thinking"`

      - `RedactedThinkingBlock`

        - `data: string`

        - `type: "redacted_thinking"`

          - `"redacted_thinking"`

      - `ToolUseBlock`

        - `id: string`

        - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

        - `input: Record<string, unknown>`

        - `name: string`

        - `type: "tool_use"`

          - `"tool_use"`

      - `ServerToolUseBlock`

        - `id: string`

        - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

        - `input: Record<string, unknown>`

        - `name: "web_search" | "web_fetch" | "code_execution" | 4 more`

          - `"web_search"`

          - `"web_fetch"`

          - `"code_execution"`

          - `"bash_code_execution"`

          - `"text_editor_code_execution"`

          - `"tool_search_tool_regex"`

          - `"tool_search_tool_bm25"`

        - `type: "server_tool_use"`

          - `"server_tool_use"`

      - `WebSearchToolResultBlock`

        - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

        - `content: WebSearchToolResultBlockContent`

          - `WebSearchToolResultError`

            - `error_code: WebSearchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"max_uses_exceeded"`

              - `"too_many_requests"`

              - `"query_too_long"`

              - `"request_too_large"`

            - `type: "web_search_tool_result_error"`

              - `"web_search_tool_result_error"`

          - `Array<WebSearchResultBlock>`

            - `encrypted_content: string`

            - `page_age: string | null`

            - `title: string`

            - `type: "web_search_result"`

              - `"web_search_result"`

            - `url: string`

        - `tool_use_id: string`

        - `type: "web_search_tool_result"`

          - `"web_search_tool_result"`

      - `WebFetchToolResultBlock`

        - `caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

        - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

          - `WebFetchToolResultErrorBlock`

            - `error_code: WebFetchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"url_too_long"`

              - `"url_not_allowed"`

              - `"url_not_accessible"`

              - `"unsupported_content_type"`

              - `"too_many_requests"`

              - `"max_uses_exceeded"`

              - `"unavailable"`

            - `type: "web_fetch_tool_result_error"`

              - `"web_fetch_tool_result_error"`

          - `WebFetchBlock`

            - `content: DocumentBlock`

              - `citations: CitationsConfig | null`

                Citation configuration for the document

                - `enabled: boolean`

              - `source: Base64PDFSource | PlainTextSource`

                - `Base64PDFSource`

                  - `data: string`

                  - `media_type: "application/pdf"`

                    - `"application/pdf"`

                  - `type: "base64"`

                    - `"base64"`

                - `PlainTextSource`

                  - `data: string`

                  - `media_type: "text/plain"`

                    - `"text/plain"`

                  - `type: "text"`

                    - `"text"`

              - `title: string | null`

                The title of the document

              - `type: "document"`

                - `"document"`

            - `retrieved_at: string | null`

              ISO 8601 timestamp when the content was retrieved

            - `type: "web_fetch_result"`

              - `"web_fetch_result"`

            - `url: string`

              Fetched content URL

        - `tool_use_id: string`

        - `type: "web_fetch_tool_result"`

          - `"web_fetch_tool_result"`

      - `CodeExecutionToolResultBlock`

        - `content: CodeExecutionToolResultBlockContent`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `CodeExecutionToolResultError`

            - `error_code: CodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `type: "code_execution_tool_result_error"`

              - `"code_execution_tool_result_error"`

          - `CodeExecutionResultBlock`

            - `content: Array<CodeExecutionOutputBlock>`

              - `file_id: string`

              - `type: "code_execution_output"`

                - `"code_execution_output"`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

            - `type: "code_execution_result"`

              - `"code_execution_result"`

          - `EncryptedCodeExecutionResultBlock`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `content: Array<CodeExecutionOutputBlock>`

              - `file_id: string`

              - `type: "code_execution_output"`

                - `"code_execution_output"`

            - `encrypted_stdout: string`

            - `return_code: number`

            - `stderr: string`

            - `type: "encrypted_code_execution_result"`

              - `"encrypted_code_execution_result"`

        - `tool_use_id: string`

        - `type: "code_execution_tool_result"`

          - `"code_execution_tool_result"`

      - `BashCodeExecutionToolResultBlock`

        - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

          - `BashCodeExecutionToolResultError`

            - `error_code: BashCodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"output_file_too_large"`

            - `type: "bash_code_execution_tool_result_error"`

              - `"bash_code_execution_tool_result_error"`

          - `BashCodeExecutionResultBlock`

            - `content: Array<BashCodeExecutionOutputBlock>`

              - `file_id: string`

              - `type: "bash_code_execution_output"`

                - `"bash_code_execution_output"`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

            - `type: "bash_code_execution_result"`

              - `"bash_code_execution_result"`

        - `tool_use_id: string`

        - `type: "bash_code_execution_tool_result"`

          - `"bash_code_execution_tool_result"`

      - `TextEditorCodeExecutionToolResultBlock`

        - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

          - `TextEditorCodeExecutionToolResultError`

            - `error_code: TextEditorCodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"file_not_found"`

            - `error_message: string | null`

            - `type: "text_editor_code_execution_tool_result_error"`

              - `"text_editor_code_execution_tool_result_error"`

          - `TextEditorCodeExecutionViewResultBlock`

            - `content: string`

            - `file_type: "text" | "image" | "pdf"`

              - `"text"`

              - `"image"`

              - `"pdf"`

            - `num_lines: number | null`

            - `start_line: number | null`

            - `total_lines: number | null`

            - `type: "text_editor_code_execution_view_result"`

              - `"text_editor_code_execution_view_result"`

          - `TextEditorCodeExecutionCreateResultBlock`

            - `is_file_update: boolean`

            - `type: "text_editor_code_execution_create_result"`

              - `"text_editor_code_execution_create_result"`

          - `TextEditorCodeExecutionStrReplaceResultBlock`

            - `lines: Array<string> | null`

            - `new_lines: number | null`

            - `new_start: number | null`

            - `old_lines: number | null`

            - `old_start: number | null`

            - `type: "text_editor_code_execution_str_replace_result"`

              - `"text_editor_code_execution_str_replace_result"`

        - `tool_use_id: string`

        - `type: "text_editor_code_execution_tool_result"`

          - `"text_editor_code_execution_tool_result"`

      - `ToolSearchToolResultBlock`

        - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

          - `ToolSearchToolResultError`

            - `error_code: ToolSearchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `error_message: string | null`

            - `type: "tool_search_tool_result_error"`

              - `"tool_search_tool_result_error"`

          - `ToolSearchToolSearchResultBlock`

            - `tool_references: Array<ToolReferenceBlock>`

              - `tool_name: string`

              - `type: "tool_reference"`

                - `"tool_reference"`

            - `type: "tool_search_tool_search_result"`

              - `"tool_search_tool_search_result"`

        - `tool_use_id: string`

        - `type: "tool_search_tool_result"`

          - `"tool_search_tool_result"`

      - `ContainerUploadBlock`

        Response model for a file uploaded to the container.

        - `file_id: string`

        - `type: "container_upload"`

          - `"container_upload"`

    - `model: Model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-opus-4-5-20251101" | 19 more`

        - `"claude-opus-4-6"`

          Most intelligent model for building agents and coding

        - `"claude-sonnet-4-6"`

          Frontier intelligence at scale — built for coding, agents, and enterprise workflows

        - `"claude-opus-4-5-20251101"`

          Premium model combining maximum intelligence with practical performance

        - `"claude-opus-4-5"`

          Premium model combining maximum intelligence with practical performance

        - `"claude-3-7-sonnet-latest"`

          High-performance model with early extended thinking

        - `"claude-3-7-sonnet-20250219"`

          High-performance model with early extended thinking

        - `"claude-3-5-haiku-latest"`

          Fastest and most compact model for near-instant responsiveness

        - `"claude-3-5-haiku-20241022"`

          Our fastest model

        - `"claude-haiku-4-5"`

          Hybrid model, capable of near-instant responses and extended thinking

        - `"claude-haiku-4-5-20251001"`

          Hybrid model, capable of near-instant responses and extended thinking

        - `"claude-sonnet-4-20250514"`

          High-performance model with extended thinking

        - `"claude-sonnet-4-0"`

          High-performance model with extended thinking

        - `"claude-4-sonnet-20250514"`

          High-performance model with extended thinking

        - `"claude-sonnet-4-5"`

          Our best model for real-world agents and coding

        - `"claude-sonnet-4-5-20250929"`

          Our best model for real-world agents and coding

        - `"claude-opus-4-0"`

          Our most capable model

        - `"claude-opus-4-20250514"`

          Our most capable model

        - `"claude-4-opus-20250514"`

          Our most capable model

        - `"claude-opus-4-1-20250805"`

          Our most capable model

        - `"claude-3-opus-latest"`

          Excels at writing and complex tasks

        - `"claude-3-opus-20240229"`

          Excels at writing and complex tasks

        - `"claude-3-haiku-20240307"`

          Our previous most fast and cost-effective

      - `(string & {})`

    - `role: "assistant"`

      Conversational role of the generated message.

      This will always be `"assistant"`.

      - `"assistant"`

    - `stop_reason: StopReason | null`

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

      - `"refusal"`

    - `stop_sequence: string | null`

      Which custom stop sequence was generated, if any.

      This value will be a non-null string if one of your custom stop sequences was generated.

    - `type: "message"`

      Object type.

      For Messages, this is always `"message"`.

      - `"message"`

    - `usage: Usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `cache_creation: CacheCreation | null`

        Breakdown of cached tokens by TTL

        - `ephemeral_1h_input_tokens: number`

          The number of input tokens used to create the 1 hour cache entry.

        - `ephemeral_5m_input_tokens: number`

          The number of input tokens used to create the 5 minute cache entry.

      - `cache_creation_input_tokens: number | null`

        The number of input tokens used to create the cache entry.

      - `cache_read_input_tokens: number | null`

        The number of input tokens read from the cache.

      - `inference_geo: string | null`

        The geographic region where inference was performed for this request.

      - `input_tokens: number`

        The number of input tokens which were used.

      - `output_tokens: number`

        The number of output tokens which were used.

      - `server_tool_use: ServerToolUsage | null`

        The number of server tool requests.

        - `web_fetch_requests: number`

          The number of web fetch tool requests.

        - `web_search_requests: number`

          The number of web search tool requests.

      - `service_tier: "standard" | "priority" | "batch" | null`

        If the request used the priority, standard, or batch tier.

        - `"standard"`

        - `"priority"`

        - `"batch"`

  - `type: "succeeded"`

    - `"succeeded"`

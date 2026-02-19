# Batches

## Create

`MessageBatch Messages.Batches.Create(BatchCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `BatchCreateParams parameters`

  - `required IReadOnlyList<Request> requests`

    List of requests for prompt completion. Each is an individual request to create a Message.

    - `required string CustomID`

      Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

      Must be unique for each request within the Message Batch.

    - `required Params Params`

      Messages API creation parameters for the individual request.

      See the [Messages API reference](https://docs.claude.com/en/api/messages) for full documentation on available parameters.

      - `required Long MaxTokens`

        The maximum number of tokens to generate before stopping.

        Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

        Different models have different maximum values for this parameter.  See [models](https://docs.claude.com/en/docs/models-overview) for details.

      - `required IReadOnlyList<MessageParam> Messages`

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

        - `required Content Content`

          - `string`

          - `IReadOnlyList<ContentBlockParam>`

            - `class TextBlockParam:`

              - `required string Text`

              - `JsonElement Type "text"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

              - `IReadOnlyList<TextCitationParam>? Citations`

                - `class CitationCharLocationParam:`

                  - `required string CitedText`

                  - `required Long DocumentIndex`

                  - `required string? DocumentTitle`

                  - `required Long EndCharIndex`

                  - `required Long StartCharIndex`

                  - `JsonElement Type "char_location"constant`

                - `class CitationPageLocationParam:`

                  - `required string CitedText`

                  - `required Long DocumentIndex`

                  - `required string? DocumentTitle`

                  - `required Long EndPageNumber`

                  - `required Long StartPageNumber`

                  - `JsonElement Type "page_location"constant`

                - `class CitationContentBlockLocationParam:`

                  - `required string CitedText`

                  - `required Long DocumentIndex`

                  - `required string? DocumentTitle`

                  - `required Long EndBlockIndex`

                  - `required Long StartBlockIndex`

                  - `JsonElement Type "content_block_location"constant`

                - `class CitationWebSearchResultLocationParam:`

                  - `required string CitedText`

                  - `required string EncryptedIndex`

                  - `required string? Title`

                  - `JsonElement Type "web_search_result_location"constant`

                  - `required string Url`

                - `class CitationSearchResultLocationParam:`

                  - `required string CitedText`

                  - `required Long EndBlockIndex`

                  - `required Long SearchResultIndex`

                  - `required string Source`

                  - `required Long StartBlockIndex`

                  - `required string? Title`

                  - `JsonElement Type "search_result_location"constant`

            - `class ImageBlockParam:`

              - `required Source Source`

                - `class Base64ImageSource:`

                  - `required string Data`

                  - `required MediaType MediaType`

                    - `"image/jpeg"ImageJpeg`

                    - `"image/png"ImagePng`

                    - `"image/gif"ImageGif`

                    - `"image/webp"ImageWebP`

                  - `JsonElement Type "base64"constant`

                - `class UrlImageSource:`

                  - `JsonElement Type "url"constant`

                  - `required string Url`

              - `JsonElement Type "image"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

            - `class DocumentBlockParam:`

              - `required Source Source`

                - `class Base64PdfSource:`

                  - `required string Data`

                  - `JsonElement MediaType "application/pdf"constant`

                  - `JsonElement Type "base64"constant`

                - `class PlainTextSource:`

                  - `required string Data`

                  - `JsonElement MediaType "text/plain"constant`

                  - `JsonElement Type "text"constant`

                - `class ContentBlockSource:`

                  - `required Content Content`

                    - `string`

                    - `IReadOnlyList<ContentBlockSourceContent>`

                      - `class TextBlockParam:`

                        - `required string Text`

                        - `JsonElement Type "text"constant`

                        - `CacheControlEphemeral? CacheControl`

                          Create a cache control breakpoint at this content block.

                          - `JsonElement Type "ephemeral"constant`

                          - `Ttl Ttl`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `"5m"Ttl5m`

                            - `"1h"Ttl1h`

                        - `IReadOnlyList<TextCitationParam>? Citations`

                          - `class CitationCharLocationParam:`

                            - `required string CitedText`

                            - `required Long DocumentIndex`

                            - `required string? DocumentTitle`

                            - `required Long EndCharIndex`

                            - `required Long StartCharIndex`

                            - `JsonElement Type "char_location"constant`

                          - `class CitationPageLocationParam:`

                            - `required string CitedText`

                            - `required Long DocumentIndex`

                            - `required string? DocumentTitle`

                            - `required Long EndPageNumber`

                            - `required Long StartPageNumber`

                            - `JsonElement Type "page_location"constant`

                          - `class CitationContentBlockLocationParam:`

                            - `required string CitedText`

                            - `required Long DocumentIndex`

                            - `required string? DocumentTitle`

                            - `required Long EndBlockIndex`

                            - `required Long StartBlockIndex`

                            - `JsonElement Type "content_block_location"constant`

                          - `class CitationWebSearchResultLocationParam:`

                            - `required string CitedText`

                            - `required string EncryptedIndex`

                            - `required string? Title`

                            - `JsonElement Type "web_search_result_location"constant`

                            - `required string Url`

                          - `class CitationSearchResultLocationParam:`

                            - `required string CitedText`

                            - `required Long EndBlockIndex`

                            - `required Long SearchResultIndex`

                            - `required string Source`

                            - `required Long StartBlockIndex`

                            - `required string? Title`

                            - `JsonElement Type "search_result_location"constant`

                      - `class ImageBlockParam:`

                        - `required Source Source`

                          - `class Base64ImageSource:`

                            - `required string Data`

                            - `required MediaType MediaType`

                              - `"image/jpeg"ImageJpeg`

                              - `"image/png"ImagePng`

                              - `"image/gif"ImageGif`

                              - `"image/webp"ImageWebP`

                            - `JsonElement Type "base64"constant`

                          - `class UrlImageSource:`

                            - `JsonElement Type "url"constant`

                            - `required string Url`

                        - `JsonElement Type "image"constant`

                        - `CacheControlEphemeral? CacheControl`

                          Create a cache control breakpoint at this content block.

                          - `JsonElement Type "ephemeral"constant`

                          - `Ttl Ttl`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `"5m"Ttl5m`

                            - `"1h"Ttl1h`

                  - `JsonElement Type "content"constant`

                - `class UrlPdfSource:`

                  - `JsonElement Type "url"constant`

                  - `required string Url`

              - `JsonElement Type "document"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

              - `CitationsConfigParam? Citations`

                - `Boolean Enabled`

              - `string? Context`

              - `string? Title`

            - `class SearchResultBlockParam:`

              - `required IReadOnlyList<TextBlockParam> Content`

                - `required string Text`

                - `JsonElement Type "text"constant`

                - `CacheControlEphemeral? CacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonElement Type "ephemeral"constant`

                  - `Ttl Ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"Ttl5m`

                    - `"1h"Ttl1h`

                - `IReadOnlyList<TextCitationParam>? Citations`

                  - `class CitationCharLocationParam:`

                    - `required string CitedText`

                    - `required Long DocumentIndex`

                    - `required string? DocumentTitle`

                    - `required Long EndCharIndex`

                    - `required Long StartCharIndex`

                    - `JsonElement Type "char_location"constant`

                  - `class CitationPageLocationParam:`

                    - `required string CitedText`

                    - `required Long DocumentIndex`

                    - `required string? DocumentTitle`

                    - `required Long EndPageNumber`

                    - `required Long StartPageNumber`

                    - `JsonElement Type "page_location"constant`

                  - `class CitationContentBlockLocationParam:`

                    - `required string CitedText`

                    - `required Long DocumentIndex`

                    - `required string? DocumentTitle`

                    - `required Long EndBlockIndex`

                    - `required Long StartBlockIndex`

                    - `JsonElement Type "content_block_location"constant`

                  - `class CitationWebSearchResultLocationParam:`

                    - `required string CitedText`

                    - `required string EncryptedIndex`

                    - `required string? Title`

                    - `JsonElement Type "web_search_result_location"constant`

                    - `required string Url`

                  - `class CitationSearchResultLocationParam:`

                    - `required string CitedText`

                    - `required Long EndBlockIndex`

                    - `required Long SearchResultIndex`

                    - `required string Source`

                    - `required Long StartBlockIndex`

                    - `required string? Title`

                    - `JsonElement Type "search_result_location"constant`

              - `required string Source`

              - `required string Title`

              - `JsonElement Type "search_result"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

              - `CitationsConfigParam Citations`

                - `Boolean Enabled`

            - `class ThinkingBlockParam:`

              - `required string Signature`

              - `required string Thinking`

              - `JsonElement Type "thinking"constant`

            - `class RedactedThinkingBlockParam:`

              - `required string Data`

              - `JsonElement Type "redacted_thinking"constant`

            - `class ToolUseBlockParam:`

              - `required string ID`

              - `required IReadOnlyDictionary<string, JsonElement> Input`

              - `required string Name`

              - `JsonElement Type "tool_use"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

              - `Caller Caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                  - `JsonElement Type "direct"constant`

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                  - `required string ToolID`

                  - `JsonElement Type "code_execution_20250825"constant`

                - `class ServerToolCaller20260120:`

                  - `required string ToolID`

                  - `JsonElement Type "code_execution_20260120"constant`

            - `class ToolResultBlockParam:`

              - `required string ToolUseID`

              - `JsonElement Type "tool_result"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

              - `Content Content`

                - `string`

                - `IReadOnlyList<Block>`

                  - `class TextBlockParam:`

                    - `required string Text`

                    - `JsonElement Type "text"constant`

                    - `CacheControlEphemeral? CacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonElement Type "ephemeral"constant`

                      - `Ttl Ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"Ttl5m`

                        - `"1h"Ttl1h`

                    - `IReadOnlyList<TextCitationParam>? Citations`

                      - `class CitationCharLocationParam:`

                        - `required string CitedText`

                        - `required Long DocumentIndex`

                        - `required string? DocumentTitle`

                        - `required Long EndCharIndex`

                        - `required Long StartCharIndex`

                        - `JsonElement Type "char_location"constant`

                      - `class CitationPageLocationParam:`

                        - `required string CitedText`

                        - `required Long DocumentIndex`

                        - `required string? DocumentTitle`

                        - `required Long EndPageNumber`

                        - `required Long StartPageNumber`

                        - `JsonElement Type "page_location"constant`

                      - `class CitationContentBlockLocationParam:`

                        - `required string CitedText`

                        - `required Long DocumentIndex`

                        - `required string? DocumentTitle`

                        - `required Long EndBlockIndex`

                        - `required Long StartBlockIndex`

                        - `JsonElement Type "content_block_location"constant`

                      - `class CitationWebSearchResultLocationParam:`

                        - `required string CitedText`

                        - `required string EncryptedIndex`

                        - `required string? Title`

                        - `JsonElement Type "web_search_result_location"constant`

                        - `required string Url`

                      - `class CitationSearchResultLocationParam:`

                        - `required string CitedText`

                        - `required Long EndBlockIndex`

                        - `required Long SearchResultIndex`

                        - `required string Source`

                        - `required Long StartBlockIndex`

                        - `required string? Title`

                        - `JsonElement Type "search_result_location"constant`

                  - `class ImageBlockParam:`

                    - `required Source Source`

                      - `class Base64ImageSource:`

                        - `required string Data`

                        - `required MediaType MediaType`

                          - `"image/jpeg"ImageJpeg`

                          - `"image/png"ImagePng`

                          - `"image/gif"ImageGif`

                          - `"image/webp"ImageWebP`

                        - `JsonElement Type "base64"constant`

                      - `class UrlImageSource:`

                        - `JsonElement Type "url"constant`

                        - `required string Url`

                    - `JsonElement Type "image"constant`

                    - `CacheControlEphemeral? CacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonElement Type "ephemeral"constant`

                      - `Ttl Ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"Ttl5m`

                        - `"1h"Ttl1h`

                  - `class SearchResultBlockParam:`

                    - `required IReadOnlyList<TextBlockParam> Content`

                      - `required string Text`

                      - `JsonElement Type "text"constant`

                      - `CacheControlEphemeral? CacheControl`

                        Create a cache control breakpoint at this content block.

                        - `JsonElement Type "ephemeral"constant`

                        - `Ttl Ttl`

                          The time-to-live for the cache control breakpoint.

                          This may be one the following values:

                          - `5m`: 5 minutes
                          - `1h`: 1 hour

                          Defaults to `5m`.

                          - `"5m"Ttl5m`

                          - `"1h"Ttl1h`

                      - `IReadOnlyList<TextCitationParam>? Citations`

                        - `class CitationCharLocationParam:`

                          - `required string CitedText`

                          - `required Long DocumentIndex`

                          - `required string? DocumentTitle`

                          - `required Long EndCharIndex`

                          - `required Long StartCharIndex`

                          - `JsonElement Type "char_location"constant`

                        - `class CitationPageLocationParam:`

                          - `required string CitedText`

                          - `required Long DocumentIndex`

                          - `required string? DocumentTitle`

                          - `required Long EndPageNumber`

                          - `required Long StartPageNumber`

                          - `JsonElement Type "page_location"constant`

                        - `class CitationContentBlockLocationParam:`

                          - `required string CitedText`

                          - `required Long DocumentIndex`

                          - `required string? DocumentTitle`

                          - `required Long EndBlockIndex`

                          - `required Long StartBlockIndex`

                          - `JsonElement Type "content_block_location"constant`

                        - `class CitationWebSearchResultLocationParam:`

                          - `required string CitedText`

                          - `required string EncryptedIndex`

                          - `required string? Title`

                          - `JsonElement Type "web_search_result_location"constant`

                          - `required string Url`

                        - `class CitationSearchResultLocationParam:`

                          - `required string CitedText`

                          - `required Long EndBlockIndex`

                          - `required Long SearchResultIndex`

                          - `required string Source`

                          - `required Long StartBlockIndex`

                          - `required string? Title`

                          - `JsonElement Type "search_result_location"constant`

                    - `required string Source`

                    - `required string Title`

                    - `JsonElement Type "search_result"constant`

                    - `CacheControlEphemeral? CacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonElement Type "ephemeral"constant`

                      - `Ttl Ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"Ttl5m`

                        - `"1h"Ttl1h`

                    - `CitationsConfigParam Citations`

                      - `Boolean Enabled`

                  - `class DocumentBlockParam:`

                    - `required Source Source`

                      - `class Base64PdfSource:`

                        - `required string Data`

                        - `JsonElement MediaType "application/pdf"constant`

                        - `JsonElement Type "base64"constant`

                      - `class PlainTextSource:`

                        - `required string Data`

                        - `JsonElement MediaType "text/plain"constant`

                        - `JsonElement Type "text"constant`

                      - `class ContentBlockSource:`

                        - `required Content Content`

                          - `string`

                          - `IReadOnlyList<ContentBlockSourceContent>`

                            - `class TextBlockParam:`

                              - `required string Text`

                              - `JsonElement Type "text"constant`

                              - `CacheControlEphemeral? CacheControl`

                                Create a cache control breakpoint at this content block.

                                - `JsonElement Type "ephemeral"constant`

                                - `Ttl Ttl`

                                  The time-to-live for the cache control breakpoint.

                                  This may be one the following values:

                                  - `5m`: 5 minutes
                                  - `1h`: 1 hour

                                  Defaults to `5m`.

                                  - `"5m"Ttl5m`

                                  - `"1h"Ttl1h`

                              - `IReadOnlyList<TextCitationParam>? Citations`

                                - `class CitationCharLocationParam:`

                                  - `required string CitedText`

                                  - `required Long DocumentIndex`

                                  - `required string? DocumentTitle`

                                  - `required Long EndCharIndex`

                                  - `required Long StartCharIndex`

                                  - `JsonElement Type "char_location"constant`

                                - `class CitationPageLocationParam:`

                                  - `required string CitedText`

                                  - `required Long DocumentIndex`

                                  - `required string? DocumentTitle`

                                  - `required Long EndPageNumber`

                                  - `required Long StartPageNumber`

                                  - `JsonElement Type "page_location"constant`

                                - `class CitationContentBlockLocationParam:`

                                  - `required string CitedText`

                                  - `required Long DocumentIndex`

                                  - `required string? DocumentTitle`

                                  - `required Long EndBlockIndex`

                                  - `required Long StartBlockIndex`

                                  - `JsonElement Type "content_block_location"constant`

                                - `class CitationWebSearchResultLocationParam:`

                                  - `required string CitedText`

                                  - `required string EncryptedIndex`

                                  - `required string? Title`

                                  - `JsonElement Type "web_search_result_location"constant`

                                  - `required string Url`

                                - `class CitationSearchResultLocationParam:`

                                  - `required string CitedText`

                                  - `required Long EndBlockIndex`

                                  - `required Long SearchResultIndex`

                                  - `required string Source`

                                  - `required Long StartBlockIndex`

                                  - `required string? Title`

                                  - `JsonElement Type "search_result_location"constant`

                            - `class ImageBlockParam:`

                              - `required Source Source`

                                - `class Base64ImageSource:`

                                  - `required string Data`

                                  - `required MediaType MediaType`

                                    - `"image/jpeg"ImageJpeg`

                                    - `"image/png"ImagePng`

                                    - `"image/gif"ImageGif`

                                    - `"image/webp"ImageWebP`

                                  - `JsonElement Type "base64"constant`

                                - `class UrlImageSource:`

                                  - `JsonElement Type "url"constant`

                                  - `required string Url`

                              - `JsonElement Type "image"constant`

                              - `CacheControlEphemeral? CacheControl`

                                Create a cache control breakpoint at this content block.

                                - `JsonElement Type "ephemeral"constant`

                                - `Ttl Ttl`

                                  The time-to-live for the cache control breakpoint.

                                  This may be one the following values:

                                  - `5m`: 5 minutes
                                  - `1h`: 1 hour

                                  Defaults to `5m`.

                                  - `"5m"Ttl5m`

                                  - `"1h"Ttl1h`

                        - `JsonElement Type "content"constant`

                      - `class UrlPdfSource:`

                        - `JsonElement Type "url"constant`

                        - `required string Url`

                    - `JsonElement Type "document"constant`

                    - `CacheControlEphemeral? CacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonElement Type "ephemeral"constant`

                      - `Ttl Ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"Ttl5m`

                        - `"1h"Ttl1h`

                    - `CitationsConfigParam? Citations`

                      - `Boolean Enabled`

                    - `string? Context`

                    - `string? Title`

                  - `class ToolReferenceBlockParam:`

                    Tool reference block that can be included in tool_result content.

                    - `required string ToolName`

                    - `JsonElement Type "tool_reference"constant`

                    - `CacheControlEphemeral? CacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonElement Type "ephemeral"constant`

                      - `Ttl Ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"Ttl5m`

                        - `"1h"Ttl1h`

              - `Boolean IsError`

            - `class ServerToolUseBlockParam:`

              - `required string ID`

              - `required IReadOnlyDictionary<string, JsonElement> Input`

              - `required Name Name`

                - `"web_search"WebSearch`

                - `"web_fetch"WebFetch`

                - `"code_execution"CodeExecution`

                - `"bash_code_execution"BashCodeExecution`

                - `"text_editor_code_execution"TextEditorCodeExecution`

                - `"tool_search_tool_regex"ToolSearchToolRegex`

                - `"tool_search_tool_bm25"ToolSearchToolBm25`

              - `JsonElement Type "server_tool_use"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

              - `Caller Caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                  - `JsonElement Type "direct"constant`

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                  - `required string ToolID`

                  - `JsonElement Type "code_execution_20250825"constant`

                - `class ServerToolCaller20260120:`

                  - `required string ToolID`

                  - `JsonElement Type "code_execution_20260120"constant`

            - `class WebSearchToolResultBlockParam:`

              - `required WebSearchToolResultBlockParamContent Content`

                - `IReadOnlyList<WebSearchResultBlockParam>`

                  - `required string EncryptedContent`

                  - `required string Title`

                  - `JsonElement Type "web_search_result"constant`

                  - `required string Url`

                  - `string? PageAge`

                - `class WebSearchToolRequestError:`

                  - `required WebSearchToolResultErrorCode ErrorCode`

                    - `"invalid_tool_input"InvalidToolInput`

                    - `"unavailable"Unavailable`

                    - `"max_uses_exceeded"MaxUsesExceeded`

                    - `"too_many_requests"TooManyRequests`

                    - `"query_too_long"QueryTooLong`

                    - `"request_too_large"RequestTooLarge`

                  - `JsonElement Type "web_search_tool_result_error"constant`

              - `required string ToolUseID`

              - `JsonElement Type "web_search_tool_result"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

              - `Caller Caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                  - `JsonElement Type "direct"constant`

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                  - `required string ToolID`

                  - `JsonElement Type "code_execution_20250825"constant`

                - `class ServerToolCaller20260120:`

                  - `required string ToolID`

                  - `JsonElement Type "code_execution_20260120"constant`

            - `class WebFetchToolResultBlockParam:`

              - `required Content Content`

                - `class WebFetchToolResultErrorBlockParam:`

                  - `required WebFetchToolResultErrorCode ErrorCode`

                    - `"invalid_tool_input"InvalidToolInput`

                    - `"url_too_long"UrlTooLong`

                    - `"url_not_allowed"UrlNotAllowed`

                    - `"url_not_accessible"UrlNotAccessible`

                    - `"unsupported_content_type"UnsupportedContentType`

                    - `"too_many_requests"TooManyRequests`

                    - `"max_uses_exceeded"MaxUsesExceeded`

                    - `"unavailable"Unavailable`

                  - `JsonElement Type "web_fetch_tool_result_error"constant`

                - `class WebFetchBlockParam:`

                  - `required DocumentBlockParam Content`

                    - `required Source Source`

                      - `class Base64PdfSource:`

                        - `required string Data`

                        - `JsonElement MediaType "application/pdf"constant`

                        - `JsonElement Type "base64"constant`

                      - `class PlainTextSource:`

                        - `required string Data`

                        - `JsonElement MediaType "text/plain"constant`

                        - `JsonElement Type "text"constant`

                      - `class ContentBlockSource:`

                        - `required Content Content`

                          - `string`

                          - `IReadOnlyList<ContentBlockSourceContent>`

                            - `class TextBlockParam:`

                              - `required string Text`

                              - `JsonElement Type "text"constant`

                              - `CacheControlEphemeral? CacheControl`

                                Create a cache control breakpoint at this content block.

                                - `JsonElement Type "ephemeral"constant`

                                - `Ttl Ttl`

                                  The time-to-live for the cache control breakpoint.

                                  This may be one the following values:

                                  - `5m`: 5 minutes
                                  - `1h`: 1 hour

                                  Defaults to `5m`.

                                  - `"5m"Ttl5m`

                                  - `"1h"Ttl1h`

                              - `IReadOnlyList<TextCitationParam>? Citations`

                                - `class CitationCharLocationParam:`

                                  - `required string CitedText`

                                  - `required Long DocumentIndex`

                                  - `required string? DocumentTitle`

                                  - `required Long EndCharIndex`

                                  - `required Long StartCharIndex`

                                  - `JsonElement Type "char_location"constant`

                                - `class CitationPageLocationParam:`

                                  - `required string CitedText`

                                  - `required Long DocumentIndex`

                                  - `required string? DocumentTitle`

                                  - `required Long EndPageNumber`

                                  - `required Long StartPageNumber`

                                  - `JsonElement Type "page_location"constant`

                                - `class CitationContentBlockLocationParam:`

                                  - `required string CitedText`

                                  - `required Long DocumentIndex`

                                  - `required string? DocumentTitle`

                                  - `required Long EndBlockIndex`

                                  - `required Long StartBlockIndex`

                                  - `JsonElement Type "content_block_location"constant`

                                - `class CitationWebSearchResultLocationParam:`

                                  - `required string CitedText`

                                  - `required string EncryptedIndex`

                                  - `required string? Title`

                                  - `JsonElement Type "web_search_result_location"constant`

                                  - `required string Url`

                                - `class CitationSearchResultLocationParam:`

                                  - `required string CitedText`

                                  - `required Long EndBlockIndex`

                                  - `required Long SearchResultIndex`

                                  - `required string Source`

                                  - `required Long StartBlockIndex`

                                  - `required string? Title`

                                  - `JsonElement Type "search_result_location"constant`

                            - `class ImageBlockParam:`

                              - `required Source Source`

                                - `class Base64ImageSource:`

                                  - `required string Data`

                                  - `required MediaType MediaType`

                                    - `"image/jpeg"ImageJpeg`

                                    - `"image/png"ImagePng`

                                    - `"image/gif"ImageGif`

                                    - `"image/webp"ImageWebP`

                                  - `JsonElement Type "base64"constant`

                                - `class UrlImageSource:`

                                  - `JsonElement Type "url"constant`

                                  - `required string Url`

                              - `JsonElement Type "image"constant`

                              - `CacheControlEphemeral? CacheControl`

                                Create a cache control breakpoint at this content block.

                                - `JsonElement Type "ephemeral"constant`

                                - `Ttl Ttl`

                                  The time-to-live for the cache control breakpoint.

                                  This may be one the following values:

                                  - `5m`: 5 minutes
                                  - `1h`: 1 hour

                                  Defaults to `5m`.

                                  - `"5m"Ttl5m`

                                  - `"1h"Ttl1h`

                        - `JsonElement Type "content"constant`

                      - `class UrlPdfSource:`

                        - `JsonElement Type "url"constant`

                        - `required string Url`

                    - `JsonElement Type "document"constant`

                    - `CacheControlEphemeral? CacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonElement Type "ephemeral"constant`

                      - `Ttl Ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"Ttl5m`

                        - `"1h"Ttl1h`

                    - `CitationsConfigParam? Citations`

                      - `Boolean Enabled`

                    - `string? Context`

                    - `string? Title`

                  - `JsonElement Type "web_fetch_result"constant`

                  - `required string Url`

                    Fetched content URL

                  - `string? RetrievedAt`

                    ISO 8601 timestamp when the content was retrieved

              - `required string ToolUseID`

              - `JsonElement Type "web_fetch_tool_result"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

              - `Caller Caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                  - `JsonElement Type "direct"constant`

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                  - `required string ToolID`

                  - `JsonElement Type "code_execution_20250825"constant`

                - `class ServerToolCaller20260120:`

                  - `required string ToolID`

                  - `JsonElement Type "code_execution_20260120"constant`

            - `class CodeExecutionToolResultBlockParam:`

              - `required CodeExecutionToolResultBlockParamContent Content`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `class CodeExecutionToolResultErrorParam:`

                  - `required CodeExecutionToolResultErrorCode ErrorCode`

                    - `"invalid_tool_input"InvalidToolInput`

                    - `"unavailable"Unavailable`

                    - `"too_many_requests"TooManyRequests`

                    - `"execution_time_exceeded"ExecutionTimeExceeded`

                  - `JsonElement Type "code_execution_tool_result_error"constant`

                - `class CodeExecutionResultBlockParam:`

                  - `required IReadOnlyList<CodeExecutionOutputBlockParam> Content`

                    - `required string FileID`

                    - `JsonElement Type "code_execution_output"constant`

                  - `required Long ReturnCode`

                  - `required string Stderr`

                  - `required string Stdout`

                  - `JsonElement Type "code_execution_result"constant`

                - `class EncryptedCodeExecutionResultBlockParam:`

                  Code execution result with encrypted stdout for PFC + web_search results.

                  - `required IReadOnlyList<CodeExecutionOutputBlockParam> Content`

                    - `required string FileID`

                    - `JsonElement Type "code_execution_output"constant`

                  - `required string EncryptedStdout`

                  - `required Long ReturnCode`

                  - `required string Stderr`

                  - `JsonElement Type "encrypted_code_execution_result"constant`

              - `required string ToolUseID`

              - `JsonElement Type "code_execution_tool_result"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

            - `class BashCodeExecutionToolResultBlockParam:`

              - `required Content Content`

                - `class BashCodeExecutionToolResultErrorParam:`

                  - `required BashCodeExecutionToolResultErrorCode ErrorCode`

                    - `"invalid_tool_input"InvalidToolInput`

                    - `"unavailable"Unavailable`

                    - `"too_many_requests"TooManyRequests`

                    - `"execution_time_exceeded"ExecutionTimeExceeded`

                    - `"output_file_too_large"OutputFileTooLarge`

                  - `JsonElement Type "bash_code_execution_tool_result_error"constant`

                - `class BashCodeExecutionResultBlockParam:`

                  - `required IReadOnlyList<BashCodeExecutionOutputBlockParam> Content`

                    - `required string FileID`

                    - `JsonElement Type "bash_code_execution_output"constant`

                  - `required Long ReturnCode`

                  - `required string Stderr`

                  - `required string Stdout`

                  - `JsonElement Type "bash_code_execution_result"constant`

              - `required string ToolUseID`

              - `JsonElement Type "bash_code_execution_tool_result"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

            - `class TextEditorCodeExecutionToolResultBlockParam:`

              - `required Content Content`

                - `class TextEditorCodeExecutionToolResultErrorParam:`

                  - `required TextEditorCodeExecutionToolResultErrorCode ErrorCode`

                    - `"invalid_tool_input"InvalidToolInput`

                    - `"unavailable"Unavailable`

                    - `"too_many_requests"TooManyRequests`

                    - `"execution_time_exceeded"ExecutionTimeExceeded`

                    - `"file_not_found"FileNotFound`

                  - `JsonElement Type "text_editor_code_execution_tool_result_error"constant`

                  - `string? ErrorMessage`

                - `class TextEditorCodeExecutionViewResultBlockParam:`

                  - `required string Content`

                  - `required FileType FileType`

                    - `"text"Text`

                    - `"image"Image`

                    - `"pdf"Pdf`

                  - `JsonElement Type "text_editor_code_execution_view_result"constant`

                  - `Long? NumLines`

                  - `Long? StartLine`

                  - `Long? TotalLines`

                - `class TextEditorCodeExecutionCreateResultBlockParam:`

                  - `required Boolean IsFileUpdate`

                  - `JsonElement Type "text_editor_code_execution_create_result"constant`

                - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

                  - `JsonElement Type "text_editor_code_execution_str_replace_result"constant`

                  - `IReadOnlyList<string>? Lines`

                  - `Long? NewLines`

                  - `Long? NewStart`

                  - `Long? OldLines`

                  - `Long? OldStart`

              - `required string ToolUseID`

              - `JsonElement Type "text_editor_code_execution_tool_result"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

            - `class ToolSearchToolResultBlockParam:`

              - `required Content Content`

                - `class ToolSearchToolResultErrorParam:`

                  - `required ToolSearchToolResultErrorCode ErrorCode`

                    - `"invalid_tool_input"InvalidToolInput`

                    - `"unavailable"Unavailable`

                    - `"too_many_requests"TooManyRequests`

                    - `"execution_time_exceeded"ExecutionTimeExceeded`

                  - `JsonElement Type "tool_search_tool_result_error"constant`

                - `class ToolSearchToolSearchResultBlockParam:`

                  - `required IReadOnlyList<ToolReferenceBlockParam> ToolReferences`

                    - `required string ToolName`

                    - `JsonElement Type "tool_reference"constant`

                    - `CacheControlEphemeral? CacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonElement Type "ephemeral"constant`

                      - `Ttl Ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"Ttl5m`

                        - `"1h"Ttl1h`

                  - `JsonElement Type "tool_search_tool_search_result"constant`

              - `required string ToolUseID`

              - `JsonElement Type "tool_search_tool_result"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

            - `class ContainerUploadBlockParam:`

              A content block that represents a file to be uploaded to the container
              Files uploaded via this block will be available in the container's input directory.

              - `required string FileID`

              - `JsonElement Type "container_upload"constant`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type "ephemeral"constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"Ttl5m`

                  - `"1h"Ttl1h`

        - `required Role Role`

          - `"user"User`

          - `"assistant"Assistant`

      - `required Model Model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-opus-4-6"ClaudeOpus4_6`

          Most intelligent model for building agents and coding

        - `"claude-sonnet-4-6"ClaudeSonnet4_6`

          Frontier intelligence at scale — built for coding, agents, and enterprise workflows

        - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

          Premium model combining maximum intelligence with practical performance

        - `"claude-opus-4-5"ClaudeOpus4_5`

          Premium model combining maximum intelligence with practical performance

        - `"claude-3-7-sonnet-latest"Claude3_7SonnetLatest`

          High-performance model with early extended thinking

        - `"claude-3-7-sonnet-20250219"Claude3_7Sonnet20250219`

          High-performance model with early extended thinking

        - `"claude-3-5-haiku-latest"Claude3_5HaikuLatest`

          Fastest and most compact model for near-instant responsiveness

        - `"claude-3-5-haiku-20241022"Claude3_5Haiku20241022`

          Our fastest model

        - `"claude-haiku-4-5"ClaudeHaiku4_5`

          Hybrid model, capable of near-instant responses and extended thinking

        - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

          Hybrid model, capable of near-instant responses and extended thinking

        - `"claude-sonnet-4-20250514"ClaudeSonnet4_20250514`

          High-performance model with extended thinking

        - `"claude-sonnet-4-0"ClaudeSonnet4_0`

          High-performance model with extended thinking

        - `"claude-4-sonnet-20250514"Claude4Sonnet20250514`

          High-performance model with extended thinking

        - `"claude-sonnet-4-5"ClaudeSonnet4_5`

          Our best model for real-world agents and coding

        - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

          Our best model for real-world agents and coding

        - `"claude-opus-4-0"ClaudeOpus4_0`

          Our most capable model

        - `"claude-opus-4-20250514"ClaudeOpus4_20250514`

          Our most capable model

        - `"claude-4-opus-20250514"Claude4Opus20250514`

          Our most capable model

        - `"claude-opus-4-1-20250805"ClaudeOpus4_1_20250805`

          Our most capable model

        - `"claude-3-opus-latest"Claude3OpusLatest`

          Excels at writing and complex tasks

        - `"claude-3-opus-20240229"Claude_3_Opus_20240229`

          Excels at writing and complex tasks

        - `"claude-3-haiku-20240307"Claude_3_Haiku_20240307`

          Our previous most fast and cost-effective

      - `CacheControlEphemeral? CacheControl`

        Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

        - `JsonElement Type "ephemeral"constant`

        - `Ttl Ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"Ttl5m`

          - `"1h"Ttl1h`

      - `string? Container`

        Container identifier for reuse across requests.

      - `string? InferenceGeo`

        Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

      - `Metadata Metadata`

        An object describing metadata about the request.

        - `string? UserID`

          An external identifier for the user who is associated with the request.

          This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

      - `OutputConfig OutputConfig`

        Configuration options for the model's output, such as the output format.

        - `Effort? Effort`

          All possible effort levels.

          - `"low"Low`

          - `"medium"Medium`

          - `"high"High`

          - `"max"Max`

        - `JsonOutputFormat? Format`

          A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

          - `required IReadOnlyDictionary<string, JsonElement> Schema`

            The JSON schema of the format

          - `JsonElement Type "json_schema"constant`

      - `ServiceTier ServiceTier`

        Determines whether to use priority capacity (if available) or standard capacity for this request.

        Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

        - `"auto"Auto`

        - `"standard_only"StandardOnly`

      - `IReadOnlyList<string> StopSequences`

        Custom text sequences that will cause the model to stop generating.

        Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

        If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

      - `Boolean Stream`

        Whether to incrementally stream the response using server-sent events.

        See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

      - `System System`

        System prompt.

        A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

        - `string`

        - `IReadOnlyList<TextBlockParam>`

          - `required string Text`

          - `JsonElement Type "text"constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `IReadOnlyList<TextCitationParam>? Citations`

            - `class CitationCharLocationParam:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndCharIndex`

              - `required Long StartCharIndex`

              - `JsonElement Type "char_location"constant`

            - `class CitationPageLocationParam:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndPageNumber`

              - `required Long StartPageNumber`

              - `JsonElement Type "page_location"constant`

            - `class CitationContentBlockLocationParam:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndBlockIndex`

              - `required Long StartBlockIndex`

              - `JsonElement Type "content_block_location"constant`

            - `class CitationWebSearchResultLocationParam:`

              - `required string CitedText`

              - `required string EncryptedIndex`

              - `required string? Title`

              - `JsonElement Type "web_search_result_location"constant`

              - `required string Url`

            - `class CitationSearchResultLocationParam:`

              - `required string CitedText`

              - `required Long EndBlockIndex`

              - `required Long SearchResultIndex`

              - `required string Source`

              - `required Long StartBlockIndex`

              - `required string? Title`

              - `JsonElement Type "search_result_location"constant`

      - `Double Temperature`

        Amount of randomness injected into the response.

        Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

        Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

      - `ThinkingConfigParam Thinking`

        Configuration for enabling Claude's extended thinking.

        When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

        See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

        - `class ThinkingConfigEnabled:`

          - `required Long BudgetTokens`

            Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

            Must be ≥1024 and less than `max_tokens`.

            See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

          - `JsonElement Type "enabled"constant`

        - `class ThinkingConfigDisabled:`

          - `JsonElement Type "disabled"constant`

        - `class ThinkingConfigAdaptive:`

          - `JsonElement Type "adaptive"constant`

      - `ToolChoice ToolChoice`

        How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

        - `class ToolChoiceAuto:`

          The model will automatically decide whether to use tools.

          - `JsonElement Type "auto"constant`

          - `Boolean DisableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output at most one tool use.

        - `class ToolChoiceAny:`

          The model will use any available tools.

          - `JsonElement Type "any"constant`

          - `Boolean DisableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `class ToolChoiceTool:`

          The model will use the specified tool with `tool_choice.name`.

          - `required string Name`

            The name of the tool to use.

          - `JsonElement Type "tool"constant`

          - `Boolean DisableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `class ToolChoiceNone:`

          The model will not be allowed to use tools.

          - `JsonElement Type "none"constant`

      - `IReadOnlyList<ToolUnion> Tools`

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

        - `class Tool:`

          - `required InputSchema InputSchema`

            [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

            This defines the shape of the `input` that your tool accepts and that the model will produce.

            - `JsonElement Type "object"constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `string Description`

            Description of what this tool does.

            Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

          - `Boolean? EagerInputStreaming`

            Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

          - `Type? Type`

            - `"custom"Custom`

        - `class ToolBash20250124:`

          - `JsonElement Name "bash"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type "bash_20250124"constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20250522:`

          - `JsonElement Name "code_execution"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type "code_execution_20250522"constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20250825:`

          - `JsonElement Name "code_execution"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type "code_execution_20250825"constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20260120:`

          Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

          - `JsonElement Name "code_execution"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type "code_execution_20260120"constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class MemoryTool20250818:`

          - `JsonElement Name "memory"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type "memory_20250818"constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolTextEditor20250124:`

          - `JsonElement Name "str_replace_editor"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type "text_editor_20250124"constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolTextEditor20250429:`

          - `JsonElement Name "str_replace_based_edit_tool"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type "text_editor_20250429"constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolTextEditor20250728:`

          - `JsonElement Name "str_replace_based_edit_tool"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type "text_editor_20250728"constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `Long? MaxCharacters`

            Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class WebSearchTool20250305:`

          - `JsonElement Name "web_search"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type "web_search_20250305"constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `IReadOnlyList<string>? AllowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `IReadOnlyList<string>? BlockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Long? MaxUses`

            Maximum number of times the tool can be used in the API request.

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

          - `UserLocation? UserLocation`

            Parameters for the user's location. Used to provide more relevant search results.

            - `JsonElement Type "approximate"constant`

            - `string? City`

              The city of the user.

            - `string? Country`

              The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

            - `string? Region`

              The region of the user.

            - `string? Timezone`

              The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        - `class WebFetchTool20250910:`

          - `JsonElement Name "web_fetch"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type "web_fetch_20250910"constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `IReadOnlyList<string>? AllowedDomains`

            List of domains to allow fetching from

          - `IReadOnlyList<string>? BlockedDomains`

            List of domains to block fetching from

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `CitationsConfigParam? Citations`

            Citations configuration for fetched documents. Citations are disabled by default.

            - `Boolean Enabled`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Long? MaxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          - `Long? MaxUses`

            Maximum number of times the tool can be used in the API request.

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class WebSearchTool20260209:`

          - `JsonElement Name "web_search"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type "web_search_20260209"constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `IReadOnlyList<string>? AllowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `IReadOnlyList<string>? BlockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Long? MaxUses`

            Maximum number of times the tool can be used in the API request.

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

          - `UserLocation? UserLocation`

            Parameters for the user's location. Used to provide more relevant search results.

            - `JsonElement Type "approximate"constant`

            - `string? City`

              The city of the user.

            - `string? Country`

              The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

            - `string? Region`

              The region of the user.

            - `string? Timezone`

              The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        - `class WebFetchTool20260209:`

          - `JsonElement Name "web_fetch"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type "web_fetch_20260209"constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `IReadOnlyList<string>? AllowedDomains`

            List of domains to allow fetching from

          - `IReadOnlyList<string>? BlockedDomains`

            List of domains to block fetching from

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `CitationsConfigParam? Citations`

            Citations configuration for fetched documents. Citations are disabled by default.

            - `Boolean Enabled`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Long? MaxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          - `Long? MaxUses`

            Maximum number of times the tool can be used in the API request.

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolSearchToolBm25_20251119:`

          - `JsonElement Name "tool_search_tool_bm25"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `required Type Type`

            - `"tool_search_tool_bm25_20251119"ToolSearchToolBm25_20251119`

            - `"tool_search_tool_bm25"ToolSearchToolBm25`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolSearchToolRegex20251119:`

          - `JsonElement Name "tool_search_tool_regex"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `required Type Type`

            - `"tool_search_tool_regex_20251119"ToolSearchToolRegex20251119`

            - `"tool_search_tool_regex"ToolSearchToolRegex`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `"direct"Direct`

            - `"code_execution_20250825"CodeExecution20250825`

            - `"code_execution_20260120"CodeExecution20260120`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `Boolean DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Boolean Strict`

            When true, guarantees schema validation on tool names and inputs

      - `Long TopK`

        Only sample from the top K options for each subsequent token.

        Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

        Recommended for advanced use cases only. You usually only need to use `temperature`.

      - `Double TopP`

        Use nucleus sampling.

        In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

        Recommended for advanced use cases only. You usually only need to use `temperature`.

### Returns

- `class MessageBatch:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `required DateTimeOffset? CancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `required DateTimeOffset? EndedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `required ProcessingStatus ProcessingStatus`

    Processing status of the Message Batch.

    - `"in_progress"InProgress`

    - `"canceling"Canceling`

    - `"ended"Ended`

  - `required MessageBatchRequestCounts RequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `required Long Canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `required Long Errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `required Long Expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `required Long Processing`

      Number of requests in the Message Batch that are processing.

    - `required Long Succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `required string? ResultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonElement Type "message_batch"constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```csharp
BatchCreateParams parameters = new()
{
    Requests =
    [
        new()
        {
            CustomID = "my-custom-id-1",
            Params = new()
            {
                MaxTokens = 1024,
                Messages =
                [
                    new()
                    {
                        Content = "Hello, world",
                        Role = Role.User,
                    },
                ],
                Model = Model.ClaudeOpus4_6,
                CacheControl = new() { Ttl = Ttl.Ttl5m },
                Container = "container",
                InferenceGeo = "inference_geo",
                Metadata = new()
                {
                    UserID = "13803d75-b4b5-4c3e-b2a2-6f21399b021b"
                },
                OutputConfig = new()
                {
                    Effort = Effort.Low,
                    Format = new()
                    {
                        Schema = new Dictionary<string, JsonElement>()
                        {
                            { "foo", JsonSerializer.SerializeToElement("bar") }
                        },
                    },
                },
                ServiceTier = ServiceTier.Auto,
                StopSequences =
                [
                    "string"
                ],
                Stream = true,
                System = new(

                    [
                        new TextBlockParam()
                        {
                            Text = "Today's date is 2024-06-01.",
                            CacheControl = new() { Ttl = Ttl.Ttl5m },
                            Citations =
                            [
                                new CitationCharLocationParam()
                                {
                                    CitedText = "cited_text",
                                    DocumentIndex = 0,
                                    DocumentTitle = "x",
                                    EndCharIndex = 0,
                                    StartCharIndex = 0,
                                },
                            ],
                        },
                    ]
                ),
                Temperature = 1,
                Thinking = new ThinkingConfigEnabled(1024),
                ToolChoice = new ToolChoiceAuto()
                {
                    DisableParallelToolUse = true
                },
                Tools =
                [
                    new Tool()
                    {
                        InputSchema = new()
                        {
                            Properties = new Dictionary<string, JsonElement>()
                            {
                                { "location", JsonSerializer.SerializeToElement("bar") },
                                { "unit", JsonSerializer.SerializeToElement("bar") },
                            },
                            Required =
                            [
                                "location"
                            ],
                        },
                        Name = "name",
                        AllowedCallers =
                        [
                            AllowedCaller.Direct
                        ],
                        CacheControl = new() { Ttl = Ttl.Ttl5m },
                        DeferLoading = true,
                        Description = "Get the current weather in a given location",
                        EagerInputStreaming = true,
                        InputExamples =
                        [
                            new Dictionary<string, JsonElement>()
                            {
                                { "foo", JsonSerializer.SerializeToElement("bar") },
                            },
                        ],
                        Strict = true,
                        Type = Type.Custom,
                    },
                ],
                TopK = 5,
                TopP = 0.7,
            },
        },
    ],
};

var messageBatch = await client.Messages.Batches.Create(parameters);

Console.WriteLine(messageBatch);
```

## Retrieve

`MessageBatch Messages.Batches.Retrieve(BatchRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `BatchRetrieveParams parameters`

  - `required string messageBatchID`

    ID of the Message Batch.

### Returns

- `class MessageBatch:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `required DateTimeOffset? CancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `required DateTimeOffset? EndedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `required ProcessingStatus ProcessingStatus`

    Processing status of the Message Batch.

    - `"in_progress"InProgress`

    - `"canceling"Canceling`

    - `"ended"Ended`

  - `required MessageBatchRequestCounts RequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `required Long Canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `required Long Errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `required Long Expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `required Long Processing`

      Number of requests in the Message Batch that are processing.

    - `required Long Succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `required string? ResultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonElement Type "message_batch"constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```csharp
BatchRetrieveParams parameters = new() { MessageBatchID = "message_batch_id" };

var messageBatch = await client.Messages.Batches.Retrieve(parameters);

Console.WriteLine(messageBatch);
```

## List

`BatchListPageResponse Messages.Batches.List(BatchListParams?parameters, CancellationTokencancellationToken = default)`

**get** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `BatchListParams parameters`

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

### Returns

- `class BatchListPageResponse:`

  - `required IReadOnlyList<MessageBatch> Data`

    - `required string ID`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `required DateTimeOffset? ArchivedAt`

      RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    - `required DateTimeOffset? CancelInitiatedAt`

      RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    - `required DateTimeOffset CreatedAt`

      RFC 3339 datetime string representing the time at which the Message Batch was created.

    - `required DateTimeOffset? EndedAt`

      RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

      Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    - `required DateTimeOffset ExpiresAt`

      RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    - `required ProcessingStatus ProcessingStatus`

      Processing status of the Message Batch.

      - `"in_progress"InProgress`

      - `"canceling"Canceling`

      - `"ended"Ended`

    - `required MessageBatchRequestCounts RequestCounts`

      Tallies requests within the Message Batch, categorized by their status.

      Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

      - `required Long Canceled`

        Number of requests in the Message Batch that have been canceled.

        This is zero until processing of the entire Message Batch has ended.

      - `required Long Errored`

        Number of requests in the Message Batch that encountered an error.

        This is zero until processing of the entire Message Batch has ended.

      - `required Long Expired`

        Number of requests in the Message Batch that have expired.

        This is zero until processing of the entire Message Batch has ended.

      - `required Long Processing`

        Number of requests in the Message Batch that are processing.

      - `required Long Succeeded`

        Number of requests in the Message Batch that have completed successfully.

        This is zero until processing of the entire Message Batch has ended.

    - `required string? ResultsUrl`

      URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

      Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

    - `JsonElement Type "message_batch"constant`

      Object type.

      For Message Batches, this is always `"message_batch"`.

  - `required string? FirstID`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `required Boolean HasMore`

    Indicates if there are more results in the requested page direction.

  - `required string? LastID`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```csharp
BatchListParams parameters = new();

var page = await client.Messages.Batches.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

## Cancel

`MessageBatch Messages.Batches.Cancel(BatchCancelParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `BatchCancelParams parameters`

  - `required string messageBatchID`

    ID of the Message Batch.

### Returns

- `class MessageBatch:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `required DateTimeOffset? CancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `required DateTimeOffset? EndedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `required ProcessingStatus ProcessingStatus`

    Processing status of the Message Batch.

    - `"in_progress"InProgress`

    - `"canceling"Canceling`

    - `"ended"Ended`

  - `required MessageBatchRequestCounts RequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `required Long Canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `required Long Errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `required Long Expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `required Long Processing`

      Number of requests in the Message Batch that are processing.

    - `required Long Succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `required string? ResultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonElement Type "message_batch"constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```csharp
BatchCancelParams parameters = new() { MessageBatchID = "message_batch_id" };

var messageBatch = await client.Messages.Batches.Cancel(parameters);

Console.WriteLine(messageBatch);
```

## Delete

`DeletedMessageBatch Messages.Batches.Delete(BatchDeleteParamsparameters, CancellationTokencancellationToken = default)`

**delete** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `BatchDeleteParams parameters`

  - `required string messageBatchID`

    ID of the Message Batch.

### Returns

- `class DeletedMessageBatch:`

  - `required string ID`

    ID of the Message Batch.

  - `JsonElement Type "message_batch_deleted"constant`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Example

```csharp
BatchDeleteParams parameters = new() { MessageBatchID = "message_batch_id" };

var deletedMessageBatch = await client.Messages.Batches.Delete(parameters);

Console.WriteLine(deletedMessageBatch);
```

## Results

`MessageBatchIndividualResponse Messages.Batches.ResultsStreaming(BatchResultsParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `BatchResultsParams parameters`

  - `required string messageBatchID`

    ID of the Message Batch.

### Returns

- `class MessageBatchIndividualResponse:`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `required string CustomID`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `required MessageBatchResult Result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `class MessageBatchSucceededResult:`

      - `required Message Message`

        - `required string ID`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `required Container? Container`

          Information about the container used in the request (for the code execution tool)

          - `required string ID`

            Identifier for the container used in this request

          - `required DateTimeOffset ExpiresAt`

            The time at which the container will expire.

        - `required IReadOnlyList<ContentBlock> Content`

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

          - `class TextBlock:`

            - `required IReadOnlyList<TextCitation>? Citations`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `class CitationCharLocation:`

                - `required string CitedText`

                - `required Long DocumentIndex`

                - `required string? DocumentTitle`

                - `required Long EndCharIndex`

                - `required string? FileID`

                - `required Long StartCharIndex`

                - `JsonElement Type "char_location"constant`

              - `class CitationPageLocation:`

                - `required string CitedText`

                - `required Long DocumentIndex`

                - `required string? DocumentTitle`

                - `required Long EndPageNumber`

                - `required string? FileID`

                - `required Long StartPageNumber`

                - `JsonElement Type "page_location"constant`

              - `class CitationContentBlockLocation:`

                - `required string CitedText`

                - `required Long DocumentIndex`

                - `required string? DocumentTitle`

                - `required Long EndBlockIndex`

                - `required string? FileID`

                - `required Long StartBlockIndex`

                - `JsonElement Type "content_block_location"constant`

              - `class CitationsWebSearchResultLocation:`

                - `required string CitedText`

                - `required string EncryptedIndex`

                - `required string? Title`

                - `JsonElement Type "web_search_result_location"constant`

                - `required string Url`

              - `class CitationsSearchResultLocation:`

                - `required string CitedText`

                - `required Long EndBlockIndex`

                - `required Long SearchResultIndex`

                - `required string Source`

                - `required Long StartBlockIndex`

                - `required string? Title`

                - `JsonElement Type "search_result_location"constant`

            - `required string Text`

            - `JsonElement Type "text"constant`

          - `class ThinkingBlock:`

            - `required string Signature`

            - `required string Thinking`

            - `JsonElement Type "thinking"constant`

          - `class RedactedThinkingBlock:`

            - `required string Data`

            - `JsonElement Type "redacted_thinking"constant`

          - `class ToolUseBlock:`

            - `required string ID`

            - `required Caller Caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonElement Type "direct"constant`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `required string ToolID`

                - `JsonElement Type "code_execution_20250825"constant`

              - `class ServerToolCaller20260120:`

                - `required string ToolID`

                - `JsonElement Type "code_execution_20260120"constant`

            - `required IReadOnlyDictionary<string, JsonElement> Input`

            - `required string Name`

            - `JsonElement Type "tool_use"constant`

          - `class ServerToolUseBlock:`

            - `required string ID`

            - `required Caller Caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonElement Type "direct"constant`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `required string ToolID`

                - `JsonElement Type "code_execution_20250825"constant`

              - `class ServerToolCaller20260120:`

                - `required string ToolID`

                - `JsonElement Type "code_execution_20260120"constant`

            - `required IReadOnlyDictionary<string, JsonElement> Input`

            - `required Name Name`

              - `"web_search"WebSearch`

              - `"web_fetch"WebFetch`

              - `"code_execution"CodeExecution`

              - `"bash_code_execution"BashCodeExecution`

              - `"text_editor_code_execution"TextEditorCodeExecution`

              - `"tool_search_tool_regex"ToolSearchToolRegex`

              - `"tool_search_tool_bm25"ToolSearchToolBm25`

            - `JsonElement Type "server_tool_use"constant`

          - `class WebSearchToolResultBlock:`

            - `required Caller Caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonElement Type "direct"constant`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `required string ToolID`

                - `JsonElement Type "code_execution_20250825"constant`

              - `class ServerToolCaller20260120:`

                - `required string ToolID`

                - `JsonElement Type "code_execution_20260120"constant`

            - `required WebSearchToolResultBlockContent Content`

              - `class WebSearchToolResultError:`

                - `required WebSearchToolResultErrorCode ErrorCode`

                  - `"invalid_tool_input"InvalidToolInput`

                  - `"unavailable"Unavailable`

                  - `"max_uses_exceeded"MaxUsesExceeded`

                  - `"too_many_requests"TooManyRequests`

                  - `"query_too_long"QueryTooLong`

                  - `"request_too_large"RequestTooLarge`

                - `JsonElement Type "web_search_tool_result_error"constant`

              - `IReadOnlyList<WebSearchResultBlock>`

                - `required string EncryptedContent`

                - `required string? PageAge`

                - `required string Title`

                - `JsonElement Type "web_search_result"constant`

                - `required string Url`

            - `required string ToolUseID`

            - `JsonElement Type "web_search_tool_result"constant`

          - `class WebFetchToolResultBlock:`

            - `required Caller Caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonElement Type "direct"constant`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `required string ToolID`

                - `JsonElement Type "code_execution_20250825"constant`

              - `class ServerToolCaller20260120:`

                - `required string ToolID`

                - `JsonElement Type "code_execution_20260120"constant`

            - `required Content Content`

              - `class WebFetchToolResultErrorBlock:`

                - `required WebFetchToolResultErrorCode ErrorCode`

                  - `"invalid_tool_input"InvalidToolInput`

                  - `"url_too_long"UrlTooLong`

                  - `"url_not_allowed"UrlNotAllowed`

                  - `"url_not_accessible"UrlNotAccessible`

                  - `"unsupported_content_type"UnsupportedContentType`

                  - `"too_many_requests"TooManyRequests`

                  - `"max_uses_exceeded"MaxUsesExceeded`

                  - `"unavailable"Unavailable`

                - `JsonElement Type "web_fetch_tool_result_error"constant`

              - `class WebFetchBlock:`

                - `required DocumentBlock Content`

                  - `required CitationsConfig? Citations`

                    Citation configuration for the document

                    - `required Boolean Enabled`

                  - `required Source Source`

                    - `class Base64PdfSource:`

                      - `required string Data`

                      - `JsonElement MediaType "application/pdf"constant`

                      - `JsonElement Type "base64"constant`

                    - `class PlainTextSource:`

                      - `required string Data`

                      - `JsonElement MediaType "text/plain"constant`

                      - `JsonElement Type "text"constant`

                  - `required string? Title`

                    The title of the document

                  - `JsonElement Type "document"constant`

                - `required string? RetrievedAt`

                  ISO 8601 timestamp when the content was retrieved

                - `JsonElement Type "web_fetch_result"constant`

                - `required string Url`

                  Fetched content URL

            - `required string ToolUseID`

            - `JsonElement Type "web_fetch_tool_result"constant`

          - `class CodeExecutionToolResultBlock:`

            - `required CodeExecutionToolResultBlockContent Content`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `class CodeExecutionToolResultError:`

                - `required CodeExecutionToolResultErrorCode ErrorCode`

                  - `"invalid_tool_input"InvalidToolInput`

                  - `"unavailable"Unavailable`

                  - `"too_many_requests"TooManyRequests`

                  - `"execution_time_exceeded"ExecutionTimeExceeded`

                - `JsonElement Type "code_execution_tool_result_error"constant`

              - `class CodeExecutionResultBlock:`

                - `required IReadOnlyList<CodeExecutionOutputBlock> Content`

                  - `required string FileID`

                  - `JsonElement Type "code_execution_output"constant`

                - `required Long ReturnCode`

                - `required string Stderr`

                - `required string Stdout`

                - `JsonElement Type "code_execution_result"constant`

              - `class EncryptedCodeExecutionResultBlock:`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `required IReadOnlyList<CodeExecutionOutputBlock> Content`

                  - `required string FileID`

                  - `JsonElement Type "code_execution_output"constant`

                - `required string EncryptedStdout`

                - `required Long ReturnCode`

                - `required string Stderr`

                - `JsonElement Type "encrypted_code_execution_result"constant`

            - `required string ToolUseID`

            - `JsonElement Type "code_execution_tool_result"constant`

          - `class BashCodeExecutionToolResultBlock:`

            - `required Content Content`

              - `class BashCodeExecutionToolResultError:`

                - `required BashCodeExecutionToolResultErrorCode ErrorCode`

                  - `"invalid_tool_input"InvalidToolInput`

                  - `"unavailable"Unavailable`

                  - `"too_many_requests"TooManyRequests`

                  - `"execution_time_exceeded"ExecutionTimeExceeded`

                  - `"output_file_too_large"OutputFileTooLarge`

                - `JsonElement Type "bash_code_execution_tool_result_error"constant`

              - `class BashCodeExecutionResultBlock:`

                - `required IReadOnlyList<BashCodeExecutionOutputBlock> Content`

                  - `required string FileID`

                  - `JsonElement Type "bash_code_execution_output"constant`

                - `required Long ReturnCode`

                - `required string Stderr`

                - `required string Stdout`

                - `JsonElement Type "bash_code_execution_result"constant`

            - `required string ToolUseID`

            - `JsonElement Type "bash_code_execution_tool_result"constant`

          - `class TextEditorCodeExecutionToolResultBlock:`

            - `required Content Content`

              - `class TextEditorCodeExecutionToolResultError:`

                - `required TextEditorCodeExecutionToolResultErrorCode ErrorCode`

                  - `"invalid_tool_input"InvalidToolInput`

                  - `"unavailable"Unavailable`

                  - `"too_many_requests"TooManyRequests`

                  - `"execution_time_exceeded"ExecutionTimeExceeded`

                  - `"file_not_found"FileNotFound`

                - `required string? ErrorMessage`

                - `JsonElement Type "text_editor_code_execution_tool_result_error"constant`

              - `class TextEditorCodeExecutionViewResultBlock:`

                - `required string Content`

                - `required FileType FileType`

                  - `"text"Text`

                  - `"image"Image`

                  - `"pdf"Pdf`

                - `required Long? NumLines`

                - `required Long? StartLine`

                - `required Long? TotalLines`

                - `JsonElement Type "text_editor_code_execution_view_result"constant`

              - `class TextEditorCodeExecutionCreateResultBlock:`

                - `required Boolean IsFileUpdate`

                - `JsonElement Type "text_editor_code_execution_create_result"constant`

              - `class TextEditorCodeExecutionStrReplaceResultBlock:`

                - `required IReadOnlyList<string>? Lines`

                - `required Long? NewLines`

                - `required Long? NewStart`

                - `required Long? OldLines`

                - `required Long? OldStart`

                - `JsonElement Type "text_editor_code_execution_str_replace_result"constant`

            - `required string ToolUseID`

            - `JsonElement Type "text_editor_code_execution_tool_result"constant`

          - `class ToolSearchToolResultBlock:`

            - `required Content Content`

              - `class ToolSearchToolResultError:`

                - `required ToolSearchToolResultErrorCode ErrorCode`

                  - `"invalid_tool_input"InvalidToolInput`

                  - `"unavailable"Unavailable`

                  - `"too_many_requests"TooManyRequests`

                  - `"execution_time_exceeded"ExecutionTimeExceeded`

                - `required string? ErrorMessage`

                - `JsonElement Type "tool_search_tool_result_error"constant`

              - `class ToolSearchToolSearchResultBlock:`

                - `required IReadOnlyList<ToolReferenceBlock> ToolReferences`

                  - `required string ToolName`

                  - `JsonElement Type "tool_reference"constant`

                - `JsonElement Type "tool_search_tool_search_result"constant`

            - `required string ToolUseID`

            - `JsonElement Type "tool_search_tool_result"constant`

          - `class ContainerUploadBlock:`

            Response model for a file uploaded to the container.

            - `required string FileID`

            - `JsonElement Type "container_upload"constant`

        - `required Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-opus-4-6"ClaudeOpus4_6`

            Most intelligent model for building agents and coding

          - `"claude-sonnet-4-6"ClaudeSonnet4_6`

            Frontier intelligence at scale — built for coding, agents, and enterprise workflows

          - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

            Premium model combining maximum intelligence with practical performance

          - `"claude-opus-4-5"ClaudeOpus4_5`

            Premium model combining maximum intelligence with practical performance

          - `"claude-3-7-sonnet-latest"Claude3_7SonnetLatest`

            High-performance model with early extended thinking

          - `"claude-3-7-sonnet-20250219"Claude3_7Sonnet20250219`

            High-performance model with early extended thinking

          - `"claude-3-5-haiku-latest"Claude3_5HaikuLatest`

            Fastest and most compact model for near-instant responsiveness

          - `"claude-3-5-haiku-20241022"Claude3_5Haiku20241022`

            Our fastest model

          - `"claude-haiku-4-5"ClaudeHaiku4_5`

            Hybrid model, capable of near-instant responses and extended thinking

          - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

            Hybrid model, capable of near-instant responses and extended thinking

          - `"claude-sonnet-4-20250514"ClaudeSonnet4_20250514`

            High-performance model with extended thinking

          - `"claude-sonnet-4-0"ClaudeSonnet4_0`

            High-performance model with extended thinking

          - `"claude-4-sonnet-20250514"Claude4Sonnet20250514`

            High-performance model with extended thinking

          - `"claude-sonnet-4-5"ClaudeSonnet4_5`

            Our best model for real-world agents and coding

          - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

            Our best model for real-world agents and coding

          - `"claude-opus-4-0"ClaudeOpus4_0`

            Our most capable model

          - `"claude-opus-4-20250514"ClaudeOpus4_20250514`

            Our most capable model

          - `"claude-4-opus-20250514"Claude4Opus20250514`

            Our most capable model

          - `"claude-opus-4-1-20250805"ClaudeOpus4_1_20250805`

            Our most capable model

          - `"claude-3-opus-latest"Claude3OpusLatest`

            Excels at writing and complex tasks

          - `"claude-3-opus-20240229"Claude_3_Opus_20240229`

            Excels at writing and complex tasks

          - `"claude-3-haiku-20240307"Claude_3_Haiku_20240307`

            Our previous most fast and cost-effective

        - `JsonElement Role "assistant"constant`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `required StopReason? StopReason`

          The reason that we stopped.

          This may be one the following values:

          * `"end_turn"`: the model reached a natural stopping point
          * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
          * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
          * `"tool_use"`: the model invoked one or more tools
          * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
          * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

          In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

          - `"end_turn"EndTurn`

          - `"max_tokens"MaxTokens`

          - `"stop_sequence"StopSequence`

          - `"tool_use"ToolUse`

          - `"pause_turn"PauseTurn`

          - `"refusal"Refusal`

        - `required string? StopSequence`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `JsonElement Type "message"constant`

          Object type.

          For Messages, this is always `"message"`.

        - `required Usage Usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `required CacheCreation? CacheCreation`

            Breakdown of cached tokens by TTL

            - `required Long Ephemeral1hInputTokens`

              The number of input tokens used to create the 1 hour cache entry.

            - `required Long Ephemeral5mInputTokens`

              The number of input tokens used to create the 5 minute cache entry.

          - `required Long? CacheCreationInputTokens`

            The number of input tokens used to create the cache entry.

          - `required Long? CacheReadInputTokens`

            The number of input tokens read from the cache.

          - `required string? InferenceGeo`

            The geographic region where inference was performed for this request.

          - `required Long InputTokens`

            The number of input tokens which were used.

          - `required Long OutputTokens`

            The number of output tokens which were used.

          - `required ServerToolUsage? ServerToolUse`

            The number of server tool requests.

            - `required Long WebFetchRequests`

              The number of web fetch tool requests.

            - `required Long WebSearchRequests`

              The number of web search tool requests.

          - `required ServiceTier? ServiceTier`

            If the request used the priority, standard, or batch tier.

            - `"standard"Standard`

            - `"priority"Priority`

            - `"batch"Batch`

      - `JsonElement Type "succeeded"constant`

    - `class MessageBatchErroredResult:`

      - `required ErrorResponse Error`

        - `required ErrorObject Error`

          - `class InvalidRequestError:`

            - `required string Message`

            - `JsonElement Type "invalid_request_error"constant`

          - `class AuthenticationError:`

            - `required string Message`

            - `JsonElement Type "authentication_error"constant`

          - `class BillingError:`

            - `required string Message`

            - `JsonElement Type "billing_error"constant`

          - `class PermissionError:`

            - `required string Message`

            - `JsonElement Type "permission_error"constant`

          - `class NotFoundError:`

            - `required string Message`

            - `JsonElement Type "not_found_error"constant`

          - `class RateLimitError:`

            - `required string Message`

            - `JsonElement Type "rate_limit_error"constant`

          - `class GatewayTimeoutError:`

            - `required string Message`

            - `JsonElement Type "timeout_error"constant`

          - `class ApiErrorObject:`

            - `required string Message`

            - `JsonElement Type "api_error"constant`

          - `class OverloadedError:`

            - `required string Message`

            - `JsonElement Type "overloaded_error"constant`

        - `required string? RequestID`

        - `JsonElement Type "error"constant`

      - `JsonElement Type "errored"constant`

    - `class MessageBatchCanceledResult:`

      - `JsonElement Type "canceled"constant`

    - `class MessageBatchExpiredResult:`

      - `JsonElement Type "expired"constant`

### Example

```csharp
BatchResultsParams parameters = new() { MessageBatchID = "message_batch_id" };

await foreach (var messageBatchIndividualResponse in client.Messages.Batches.ResultsStreaming(parameters))
{
    Console.WriteLine(messageBatchIndividualResponse);
}
```

## Domain Types

### Deleted Message Batch

- `class DeletedMessageBatch:`

  - `required string ID`

    ID of the Message Batch.

  - `JsonElement Type "message_batch_deleted"constant`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Message Batch

- `class MessageBatch:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `required DateTimeOffset? CancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `required DateTimeOffset? EndedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `required ProcessingStatus ProcessingStatus`

    Processing status of the Message Batch.

    - `"in_progress"InProgress`

    - `"canceling"Canceling`

    - `"ended"Ended`

  - `required MessageBatchRequestCounts RequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `required Long Canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `required Long Errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `required Long Expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `required Long Processing`

      Number of requests in the Message Batch that are processing.

    - `required Long Succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `required string? ResultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonElement Type "message_batch"constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Message Batch Canceled Result

- `class MessageBatchCanceledResult:`

  - `JsonElement Type "canceled"constant`

### Message Batch Errored Result

- `class MessageBatchErroredResult:`

  - `required ErrorResponse Error`

    - `required ErrorObject Error`

      - `class InvalidRequestError:`

        - `required string Message`

        - `JsonElement Type "invalid_request_error"constant`

      - `class AuthenticationError:`

        - `required string Message`

        - `JsonElement Type "authentication_error"constant`

      - `class BillingError:`

        - `required string Message`

        - `JsonElement Type "billing_error"constant`

      - `class PermissionError:`

        - `required string Message`

        - `JsonElement Type "permission_error"constant`

      - `class NotFoundError:`

        - `required string Message`

        - `JsonElement Type "not_found_error"constant`

      - `class RateLimitError:`

        - `required string Message`

        - `JsonElement Type "rate_limit_error"constant`

      - `class GatewayTimeoutError:`

        - `required string Message`

        - `JsonElement Type "timeout_error"constant`

      - `class ApiErrorObject:`

        - `required string Message`

        - `JsonElement Type "api_error"constant`

      - `class OverloadedError:`

        - `required string Message`

        - `JsonElement Type "overloaded_error"constant`

    - `required string? RequestID`

    - `JsonElement Type "error"constant`

  - `JsonElement Type "errored"constant`

### Message Batch Expired Result

- `class MessageBatchExpiredResult:`

  - `JsonElement Type "expired"constant`

### Message Batch Individual Response

- `class MessageBatchIndividualResponse:`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `required string CustomID`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `required MessageBatchResult Result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `class MessageBatchSucceededResult:`

      - `required Message Message`

        - `required string ID`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `required Container? Container`

          Information about the container used in the request (for the code execution tool)

          - `required string ID`

            Identifier for the container used in this request

          - `required DateTimeOffset ExpiresAt`

            The time at which the container will expire.

        - `required IReadOnlyList<ContentBlock> Content`

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

          - `class TextBlock:`

            - `required IReadOnlyList<TextCitation>? Citations`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `class CitationCharLocation:`

                - `required string CitedText`

                - `required Long DocumentIndex`

                - `required string? DocumentTitle`

                - `required Long EndCharIndex`

                - `required string? FileID`

                - `required Long StartCharIndex`

                - `JsonElement Type "char_location"constant`

              - `class CitationPageLocation:`

                - `required string CitedText`

                - `required Long DocumentIndex`

                - `required string? DocumentTitle`

                - `required Long EndPageNumber`

                - `required string? FileID`

                - `required Long StartPageNumber`

                - `JsonElement Type "page_location"constant`

              - `class CitationContentBlockLocation:`

                - `required string CitedText`

                - `required Long DocumentIndex`

                - `required string? DocumentTitle`

                - `required Long EndBlockIndex`

                - `required string? FileID`

                - `required Long StartBlockIndex`

                - `JsonElement Type "content_block_location"constant`

              - `class CitationsWebSearchResultLocation:`

                - `required string CitedText`

                - `required string EncryptedIndex`

                - `required string? Title`

                - `JsonElement Type "web_search_result_location"constant`

                - `required string Url`

              - `class CitationsSearchResultLocation:`

                - `required string CitedText`

                - `required Long EndBlockIndex`

                - `required Long SearchResultIndex`

                - `required string Source`

                - `required Long StartBlockIndex`

                - `required string? Title`

                - `JsonElement Type "search_result_location"constant`

            - `required string Text`

            - `JsonElement Type "text"constant`

          - `class ThinkingBlock:`

            - `required string Signature`

            - `required string Thinking`

            - `JsonElement Type "thinking"constant`

          - `class RedactedThinkingBlock:`

            - `required string Data`

            - `JsonElement Type "redacted_thinking"constant`

          - `class ToolUseBlock:`

            - `required string ID`

            - `required Caller Caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonElement Type "direct"constant`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `required string ToolID`

                - `JsonElement Type "code_execution_20250825"constant`

              - `class ServerToolCaller20260120:`

                - `required string ToolID`

                - `JsonElement Type "code_execution_20260120"constant`

            - `required IReadOnlyDictionary<string, JsonElement> Input`

            - `required string Name`

            - `JsonElement Type "tool_use"constant`

          - `class ServerToolUseBlock:`

            - `required string ID`

            - `required Caller Caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonElement Type "direct"constant`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `required string ToolID`

                - `JsonElement Type "code_execution_20250825"constant`

              - `class ServerToolCaller20260120:`

                - `required string ToolID`

                - `JsonElement Type "code_execution_20260120"constant`

            - `required IReadOnlyDictionary<string, JsonElement> Input`

            - `required Name Name`

              - `"web_search"WebSearch`

              - `"web_fetch"WebFetch`

              - `"code_execution"CodeExecution`

              - `"bash_code_execution"BashCodeExecution`

              - `"text_editor_code_execution"TextEditorCodeExecution`

              - `"tool_search_tool_regex"ToolSearchToolRegex`

              - `"tool_search_tool_bm25"ToolSearchToolBm25`

            - `JsonElement Type "server_tool_use"constant`

          - `class WebSearchToolResultBlock:`

            - `required Caller Caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonElement Type "direct"constant`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `required string ToolID`

                - `JsonElement Type "code_execution_20250825"constant`

              - `class ServerToolCaller20260120:`

                - `required string ToolID`

                - `JsonElement Type "code_execution_20260120"constant`

            - `required WebSearchToolResultBlockContent Content`

              - `class WebSearchToolResultError:`

                - `required WebSearchToolResultErrorCode ErrorCode`

                  - `"invalid_tool_input"InvalidToolInput`

                  - `"unavailable"Unavailable`

                  - `"max_uses_exceeded"MaxUsesExceeded`

                  - `"too_many_requests"TooManyRequests`

                  - `"query_too_long"QueryTooLong`

                  - `"request_too_large"RequestTooLarge`

                - `JsonElement Type "web_search_tool_result_error"constant`

              - `IReadOnlyList<WebSearchResultBlock>`

                - `required string EncryptedContent`

                - `required string? PageAge`

                - `required string Title`

                - `JsonElement Type "web_search_result"constant`

                - `required string Url`

            - `required string ToolUseID`

            - `JsonElement Type "web_search_tool_result"constant`

          - `class WebFetchToolResultBlock:`

            - `required Caller Caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonElement Type "direct"constant`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `required string ToolID`

                - `JsonElement Type "code_execution_20250825"constant`

              - `class ServerToolCaller20260120:`

                - `required string ToolID`

                - `JsonElement Type "code_execution_20260120"constant`

            - `required Content Content`

              - `class WebFetchToolResultErrorBlock:`

                - `required WebFetchToolResultErrorCode ErrorCode`

                  - `"invalid_tool_input"InvalidToolInput`

                  - `"url_too_long"UrlTooLong`

                  - `"url_not_allowed"UrlNotAllowed`

                  - `"url_not_accessible"UrlNotAccessible`

                  - `"unsupported_content_type"UnsupportedContentType`

                  - `"too_many_requests"TooManyRequests`

                  - `"max_uses_exceeded"MaxUsesExceeded`

                  - `"unavailable"Unavailable`

                - `JsonElement Type "web_fetch_tool_result_error"constant`

              - `class WebFetchBlock:`

                - `required DocumentBlock Content`

                  - `required CitationsConfig? Citations`

                    Citation configuration for the document

                    - `required Boolean Enabled`

                  - `required Source Source`

                    - `class Base64PdfSource:`

                      - `required string Data`

                      - `JsonElement MediaType "application/pdf"constant`

                      - `JsonElement Type "base64"constant`

                    - `class PlainTextSource:`

                      - `required string Data`

                      - `JsonElement MediaType "text/plain"constant`

                      - `JsonElement Type "text"constant`

                  - `required string? Title`

                    The title of the document

                  - `JsonElement Type "document"constant`

                - `required string? RetrievedAt`

                  ISO 8601 timestamp when the content was retrieved

                - `JsonElement Type "web_fetch_result"constant`

                - `required string Url`

                  Fetched content URL

            - `required string ToolUseID`

            - `JsonElement Type "web_fetch_tool_result"constant`

          - `class CodeExecutionToolResultBlock:`

            - `required CodeExecutionToolResultBlockContent Content`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `class CodeExecutionToolResultError:`

                - `required CodeExecutionToolResultErrorCode ErrorCode`

                  - `"invalid_tool_input"InvalidToolInput`

                  - `"unavailable"Unavailable`

                  - `"too_many_requests"TooManyRequests`

                  - `"execution_time_exceeded"ExecutionTimeExceeded`

                - `JsonElement Type "code_execution_tool_result_error"constant`

              - `class CodeExecutionResultBlock:`

                - `required IReadOnlyList<CodeExecutionOutputBlock> Content`

                  - `required string FileID`

                  - `JsonElement Type "code_execution_output"constant`

                - `required Long ReturnCode`

                - `required string Stderr`

                - `required string Stdout`

                - `JsonElement Type "code_execution_result"constant`

              - `class EncryptedCodeExecutionResultBlock:`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `required IReadOnlyList<CodeExecutionOutputBlock> Content`

                  - `required string FileID`

                  - `JsonElement Type "code_execution_output"constant`

                - `required string EncryptedStdout`

                - `required Long ReturnCode`

                - `required string Stderr`

                - `JsonElement Type "encrypted_code_execution_result"constant`

            - `required string ToolUseID`

            - `JsonElement Type "code_execution_tool_result"constant`

          - `class BashCodeExecutionToolResultBlock:`

            - `required Content Content`

              - `class BashCodeExecutionToolResultError:`

                - `required BashCodeExecutionToolResultErrorCode ErrorCode`

                  - `"invalid_tool_input"InvalidToolInput`

                  - `"unavailable"Unavailable`

                  - `"too_many_requests"TooManyRequests`

                  - `"execution_time_exceeded"ExecutionTimeExceeded`

                  - `"output_file_too_large"OutputFileTooLarge`

                - `JsonElement Type "bash_code_execution_tool_result_error"constant`

              - `class BashCodeExecutionResultBlock:`

                - `required IReadOnlyList<BashCodeExecutionOutputBlock> Content`

                  - `required string FileID`

                  - `JsonElement Type "bash_code_execution_output"constant`

                - `required Long ReturnCode`

                - `required string Stderr`

                - `required string Stdout`

                - `JsonElement Type "bash_code_execution_result"constant`

            - `required string ToolUseID`

            - `JsonElement Type "bash_code_execution_tool_result"constant`

          - `class TextEditorCodeExecutionToolResultBlock:`

            - `required Content Content`

              - `class TextEditorCodeExecutionToolResultError:`

                - `required TextEditorCodeExecutionToolResultErrorCode ErrorCode`

                  - `"invalid_tool_input"InvalidToolInput`

                  - `"unavailable"Unavailable`

                  - `"too_many_requests"TooManyRequests`

                  - `"execution_time_exceeded"ExecutionTimeExceeded`

                  - `"file_not_found"FileNotFound`

                - `required string? ErrorMessage`

                - `JsonElement Type "text_editor_code_execution_tool_result_error"constant`

              - `class TextEditorCodeExecutionViewResultBlock:`

                - `required string Content`

                - `required FileType FileType`

                  - `"text"Text`

                  - `"image"Image`

                  - `"pdf"Pdf`

                - `required Long? NumLines`

                - `required Long? StartLine`

                - `required Long? TotalLines`

                - `JsonElement Type "text_editor_code_execution_view_result"constant`

              - `class TextEditorCodeExecutionCreateResultBlock:`

                - `required Boolean IsFileUpdate`

                - `JsonElement Type "text_editor_code_execution_create_result"constant`

              - `class TextEditorCodeExecutionStrReplaceResultBlock:`

                - `required IReadOnlyList<string>? Lines`

                - `required Long? NewLines`

                - `required Long? NewStart`

                - `required Long? OldLines`

                - `required Long? OldStart`

                - `JsonElement Type "text_editor_code_execution_str_replace_result"constant`

            - `required string ToolUseID`

            - `JsonElement Type "text_editor_code_execution_tool_result"constant`

          - `class ToolSearchToolResultBlock:`

            - `required Content Content`

              - `class ToolSearchToolResultError:`

                - `required ToolSearchToolResultErrorCode ErrorCode`

                  - `"invalid_tool_input"InvalidToolInput`

                  - `"unavailable"Unavailable`

                  - `"too_many_requests"TooManyRequests`

                  - `"execution_time_exceeded"ExecutionTimeExceeded`

                - `required string? ErrorMessage`

                - `JsonElement Type "tool_search_tool_result_error"constant`

              - `class ToolSearchToolSearchResultBlock:`

                - `required IReadOnlyList<ToolReferenceBlock> ToolReferences`

                  - `required string ToolName`

                  - `JsonElement Type "tool_reference"constant`

                - `JsonElement Type "tool_search_tool_search_result"constant`

            - `required string ToolUseID`

            - `JsonElement Type "tool_search_tool_result"constant`

          - `class ContainerUploadBlock:`

            Response model for a file uploaded to the container.

            - `required string FileID`

            - `JsonElement Type "container_upload"constant`

        - `required Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-opus-4-6"ClaudeOpus4_6`

            Most intelligent model for building agents and coding

          - `"claude-sonnet-4-6"ClaudeSonnet4_6`

            Frontier intelligence at scale — built for coding, agents, and enterprise workflows

          - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

            Premium model combining maximum intelligence with practical performance

          - `"claude-opus-4-5"ClaudeOpus4_5`

            Premium model combining maximum intelligence with practical performance

          - `"claude-3-7-sonnet-latest"Claude3_7SonnetLatest`

            High-performance model with early extended thinking

          - `"claude-3-7-sonnet-20250219"Claude3_7Sonnet20250219`

            High-performance model with early extended thinking

          - `"claude-3-5-haiku-latest"Claude3_5HaikuLatest`

            Fastest and most compact model for near-instant responsiveness

          - `"claude-3-5-haiku-20241022"Claude3_5Haiku20241022`

            Our fastest model

          - `"claude-haiku-4-5"ClaudeHaiku4_5`

            Hybrid model, capable of near-instant responses and extended thinking

          - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

            Hybrid model, capable of near-instant responses and extended thinking

          - `"claude-sonnet-4-20250514"ClaudeSonnet4_20250514`

            High-performance model with extended thinking

          - `"claude-sonnet-4-0"ClaudeSonnet4_0`

            High-performance model with extended thinking

          - `"claude-4-sonnet-20250514"Claude4Sonnet20250514`

            High-performance model with extended thinking

          - `"claude-sonnet-4-5"ClaudeSonnet4_5`

            Our best model for real-world agents and coding

          - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

            Our best model for real-world agents and coding

          - `"claude-opus-4-0"ClaudeOpus4_0`

            Our most capable model

          - `"claude-opus-4-20250514"ClaudeOpus4_20250514`

            Our most capable model

          - `"claude-4-opus-20250514"Claude4Opus20250514`

            Our most capable model

          - `"claude-opus-4-1-20250805"ClaudeOpus4_1_20250805`

            Our most capable model

          - `"claude-3-opus-latest"Claude3OpusLatest`

            Excels at writing and complex tasks

          - `"claude-3-opus-20240229"Claude_3_Opus_20240229`

            Excels at writing and complex tasks

          - `"claude-3-haiku-20240307"Claude_3_Haiku_20240307`

            Our previous most fast and cost-effective

        - `JsonElement Role "assistant"constant`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `required StopReason? StopReason`

          The reason that we stopped.

          This may be one the following values:

          * `"end_turn"`: the model reached a natural stopping point
          * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
          * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
          * `"tool_use"`: the model invoked one or more tools
          * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
          * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

          In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

          - `"end_turn"EndTurn`

          - `"max_tokens"MaxTokens`

          - `"stop_sequence"StopSequence`

          - `"tool_use"ToolUse`

          - `"pause_turn"PauseTurn`

          - `"refusal"Refusal`

        - `required string? StopSequence`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `JsonElement Type "message"constant`

          Object type.

          For Messages, this is always `"message"`.

        - `required Usage Usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `required CacheCreation? CacheCreation`

            Breakdown of cached tokens by TTL

            - `required Long Ephemeral1hInputTokens`

              The number of input tokens used to create the 1 hour cache entry.

            - `required Long Ephemeral5mInputTokens`

              The number of input tokens used to create the 5 minute cache entry.

          - `required Long? CacheCreationInputTokens`

            The number of input tokens used to create the cache entry.

          - `required Long? CacheReadInputTokens`

            The number of input tokens read from the cache.

          - `required string? InferenceGeo`

            The geographic region where inference was performed for this request.

          - `required Long InputTokens`

            The number of input tokens which were used.

          - `required Long OutputTokens`

            The number of output tokens which were used.

          - `required ServerToolUsage? ServerToolUse`

            The number of server tool requests.

            - `required Long WebFetchRequests`

              The number of web fetch tool requests.

            - `required Long WebSearchRequests`

              The number of web search tool requests.

          - `required ServiceTier? ServiceTier`

            If the request used the priority, standard, or batch tier.

            - `"standard"Standard`

            - `"priority"Priority`

            - `"batch"Batch`

      - `JsonElement Type "succeeded"constant`

    - `class MessageBatchErroredResult:`

      - `required ErrorResponse Error`

        - `required ErrorObject Error`

          - `class InvalidRequestError:`

            - `required string Message`

            - `JsonElement Type "invalid_request_error"constant`

          - `class AuthenticationError:`

            - `required string Message`

            - `JsonElement Type "authentication_error"constant`

          - `class BillingError:`

            - `required string Message`

            - `JsonElement Type "billing_error"constant`

          - `class PermissionError:`

            - `required string Message`

            - `JsonElement Type "permission_error"constant`

          - `class NotFoundError:`

            - `required string Message`

            - `JsonElement Type "not_found_error"constant`

          - `class RateLimitError:`

            - `required string Message`

            - `JsonElement Type "rate_limit_error"constant`

          - `class GatewayTimeoutError:`

            - `required string Message`

            - `JsonElement Type "timeout_error"constant`

          - `class ApiErrorObject:`

            - `required string Message`

            - `JsonElement Type "api_error"constant`

          - `class OverloadedError:`

            - `required string Message`

            - `JsonElement Type "overloaded_error"constant`

        - `required string? RequestID`

        - `JsonElement Type "error"constant`

      - `JsonElement Type "errored"constant`

    - `class MessageBatchCanceledResult:`

      - `JsonElement Type "canceled"constant`

    - `class MessageBatchExpiredResult:`

      - `JsonElement Type "expired"constant`

### Message Batch Request Counts

- `class MessageBatchRequestCounts:`

  - `required Long Canceled`

    Number of requests in the Message Batch that have been canceled.

    This is zero until processing of the entire Message Batch has ended.

  - `required Long Errored`

    Number of requests in the Message Batch that encountered an error.

    This is zero until processing of the entire Message Batch has ended.

  - `required Long Expired`

    Number of requests in the Message Batch that have expired.

    This is zero until processing of the entire Message Batch has ended.

  - `required Long Processing`

    Number of requests in the Message Batch that are processing.

  - `required Long Succeeded`

    Number of requests in the Message Batch that have completed successfully.

    This is zero until processing of the entire Message Batch has ended.

### Message Batch Result

- `class MessageBatchResult: A class that can be one of several variants.union`

  Processing result for this request.

  Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

  - `class MessageBatchSucceededResult:`

    - `required Message Message`

      - `required string ID`

        Unique object identifier.

        The format and length of IDs may change over time.

      - `required Container? Container`

        Information about the container used in the request (for the code execution tool)

        - `required string ID`

          Identifier for the container used in this request

        - `required DateTimeOffset ExpiresAt`

          The time at which the container will expire.

      - `required IReadOnlyList<ContentBlock> Content`

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

        - `class TextBlock:`

          - `required IReadOnlyList<TextCitation>? Citations`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `class CitationCharLocation:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndCharIndex`

              - `required string? FileID`

              - `required Long StartCharIndex`

              - `JsonElement Type "char_location"constant`

            - `class CitationPageLocation:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndPageNumber`

              - `required string? FileID`

              - `required Long StartPageNumber`

              - `JsonElement Type "page_location"constant`

            - `class CitationContentBlockLocation:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndBlockIndex`

              - `required string? FileID`

              - `required Long StartBlockIndex`

              - `JsonElement Type "content_block_location"constant`

            - `class CitationsWebSearchResultLocation:`

              - `required string CitedText`

              - `required string EncryptedIndex`

              - `required string? Title`

              - `JsonElement Type "web_search_result_location"constant`

              - `required string Url`

            - `class CitationsSearchResultLocation:`

              - `required string CitedText`

              - `required Long EndBlockIndex`

              - `required Long SearchResultIndex`

              - `required string Source`

              - `required Long StartBlockIndex`

              - `required string? Title`

              - `JsonElement Type "search_result_location"constant`

          - `required string Text`

          - `JsonElement Type "text"constant`

        - `class ThinkingBlock:`

          - `required string Signature`

          - `required string Thinking`

          - `JsonElement Type "thinking"constant`

        - `class RedactedThinkingBlock:`

          - `required string Data`

          - `JsonElement Type "redacted_thinking"constant`

        - `class ToolUseBlock:`

          - `required string ID`

          - `required Caller Caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonElement Type "direct"constant`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `required string ToolID`

              - `JsonElement Type "code_execution_20250825"constant`

            - `class ServerToolCaller20260120:`

              - `required string ToolID`

              - `JsonElement Type "code_execution_20260120"constant`

          - `required IReadOnlyDictionary<string, JsonElement> Input`

          - `required string Name`

          - `JsonElement Type "tool_use"constant`

        - `class ServerToolUseBlock:`

          - `required string ID`

          - `required Caller Caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonElement Type "direct"constant`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `required string ToolID`

              - `JsonElement Type "code_execution_20250825"constant`

            - `class ServerToolCaller20260120:`

              - `required string ToolID`

              - `JsonElement Type "code_execution_20260120"constant`

          - `required IReadOnlyDictionary<string, JsonElement> Input`

          - `required Name Name`

            - `"web_search"WebSearch`

            - `"web_fetch"WebFetch`

            - `"code_execution"CodeExecution`

            - `"bash_code_execution"BashCodeExecution`

            - `"text_editor_code_execution"TextEditorCodeExecution`

            - `"tool_search_tool_regex"ToolSearchToolRegex`

            - `"tool_search_tool_bm25"ToolSearchToolBm25`

          - `JsonElement Type "server_tool_use"constant`

        - `class WebSearchToolResultBlock:`

          - `required Caller Caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonElement Type "direct"constant`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `required string ToolID`

              - `JsonElement Type "code_execution_20250825"constant`

            - `class ServerToolCaller20260120:`

              - `required string ToolID`

              - `JsonElement Type "code_execution_20260120"constant`

          - `required WebSearchToolResultBlockContent Content`

            - `class WebSearchToolResultError:`

              - `required WebSearchToolResultErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"max_uses_exceeded"MaxUsesExceeded`

                - `"too_many_requests"TooManyRequests`

                - `"query_too_long"QueryTooLong`

                - `"request_too_large"RequestTooLarge`

              - `JsonElement Type "web_search_tool_result_error"constant`

            - `IReadOnlyList<WebSearchResultBlock>`

              - `required string EncryptedContent`

              - `required string? PageAge`

              - `required string Title`

              - `JsonElement Type "web_search_result"constant`

              - `required string Url`

          - `required string ToolUseID`

          - `JsonElement Type "web_search_tool_result"constant`

        - `class WebFetchToolResultBlock:`

          - `required Caller Caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonElement Type "direct"constant`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `required string ToolID`

              - `JsonElement Type "code_execution_20250825"constant`

            - `class ServerToolCaller20260120:`

              - `required string ToolID`

              - `JsonElement Type "code_execution_20260120"constant`

          - `required Content Content`

            - `class WebFetchToolResultErrorBlock:`

              - `required WebFetchToolResultErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"url_too_long"UrlTooLong`

                - `"url_not_allowed"UrlNotAllowed`

                - `"url_not_accessible"UrlNotAccessible`

                - `"unsupported_content_type"UnsupportedContentType`

                - `"too_many_requests"TooManyRequests`

                - `"max_uses_exceeded"MaxUsesExceeded`

                - `"unavailable"Unavailable`

              - `JsonElement Type "web_fetch_tool_result_error"constant`

            - `class WebFetchBlock:`

              - `required DocumentBlock Content`

                - `required CitationsConfig? Citations`

                  Citation configuration for the document

                  - `required Boolean Enabled`

                - `required Source Source`

                  - `class Base64PdfSource:`

                    - `required string Data`

                    - `JsonElement MediaType "application/pdf"constant`

                    - `JsonElement Type "base64"constant`

                  - `class PlainTextSource:`

                    - `required string Data`

                    - `JsonElement MediaType "text/plain"constant`

                    - `JsonElement Type "text"constant`

                - `required string? Title`

                  The title of the document

                - `JsonElement Type "document"constant`

              - `required string? RetrievedAt`

                ISO 8601 timestamp when the content was retrieved

              - `JsonElement Type "web_fetch_result"constant`

              - `required string Url`

                Fetched content URL

          - `required string ToolUseID`

          - `JsonElement Type "web_fetch_tool_result"constant`

        - `class CodeExecutionToolResultBlock:`

          - `required CodeExecutionToolResultBlockContent Content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class CodeExecutionToolResultError:`

              - `required CodeExecutionToolResultErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"too_many_requests"TooManyRequests`

                - `"execution_time_exceeded"ExecutionTimeExceeded`

              - `JsonElement Type "code_execution_tool_result_error"constant`

            - `class CodeExecutionResultBlock:`

              - `required IReadOnlyList<CodeExecutionOutputBlock> Content`

                - `required string FileID`

                - `JsonElement Type "code_execution_output"constant`

              - `required Long ReturnCode`

              - `required string Stderr`

              - `required string Stdout`

              - `JsonElement Type "code_execution_result"constant`

            - `class EncryptedCodeExecutionResultBlock:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `required IReadOnlyList<CodeExecutionOutputBlock> Content`

                - `required string FileID`

                - `JsonElement Type "code_execution_output"constant`

              - `required string EncryptedStdout`

              - `required Long ReturnCode`

              - `required string Stderr`

              - `JsonElement Type "encrypted_code_execution_result"constant`

          - `required string ToolUseID`

          - `JsonElement Type "code_execution_tool_result"constant`

        - `class BashCodeExecutionToolResultBlock:`

          - `required Content Content`

            - `class BashCodeExecutionToolResultError:`

              - `required BashCodeExecutionToolResultErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"too_many_requests"TooManyRequests`

                - `"execution_time_exceeded"ExecutionTimeExceeded`

                - `"output_file_too_large"OutputFileTooLarge`

              - `JsonElement Type "bash_code_execution_tool_result_error"constant`

            - `class BashCodeExecutionResultBlock:`

              - `required IReadOnlyList<BashCodeExecutionOutputBlock> Content`

                - `required string FileID`

                - `JsonElement Type "bash_code_execution_output"constant`

              - `required Long ReturnCode`

              - `required string Stderr`

              - `required string Stdout`

              - `JsonElement Type "bash_code_execution_result"constant`

          - `required string ToolUseID`

          - `JsonElement Type "bash_code_execution_tool_result"constant`

        - `class TextEditorCodeExecutionToolResultBlock:`

          - `required Content Content`

            - `class TextEditorCodeExecutionToolResultError:`

              - `required TextEditorCodeExecutionToolResultErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"too_many_requests"TooManyRequests`

                - `"execution_time_exceeded"ExecutionTimeExceeded`

                - `"file_not_found"FileNotFound`

              - `required string? ErrorMessage`

              - `JsonElement Type "text_editor_code_execution_tool_result_error"constant`

            - `class TextEditorCodeExecutionViewResultBlock:`

              - `required string Content`

              - `required FileType FileType`

                - `"text"Text`

                - `"image"Image`

                - `"pdf"Pdf`

              - `required Long? NumLines`

              - `required Long? StartLine`

              - `required Long? TotalLines`

              - `JsonElement Type "text_editor_code_execution_view_result"constant`

            - `class TextEditorCodeExecutionCreateResultBlock:`

              - `required Boolean IsFileUpdate`

              - `JsonElement Type "text_editor_code_execution_create_result"constant`

            - `class TextEditorCodeExecutionStrReplaceResultBlock:`

              - `required IReadOnlyList<string>? Lines`

              - `required Long? NewLines`

              - `required Long? NewStart`

              - `required Long? OldLines`

              - `required Long? OldStart`

              - `JsonElement Type "text_editor_code_execution_str_replace_result"constant`

          - `required string ToolUseID`

          - `JsonElement Type "text_editor_code_execution_tool_result"constant`

        - `class ToolSearchToolResultBlock:`

          - `required Content Content`

            - `class ToolSearchToolResultError:`

              - `required ToolSearchToolResultErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"too_many_requests"TooManyRequests`

                - `"execution_time_exceeded"ExecutionTimeExceeded`

              - `required string? ErrorMessage`

              - `JsonElement Type "tool_search_tool_result_error"constant`

            - `class ToolSearchToolSearchResultBlock:`

              - `required IReadOnlyList<ToolReferenceBlock> ToolReferences`

                - `required string ToolName`

                - `JsonElement Type "tool_reference"constant`

              - `JsonElement Type "tool_search_tool_search_result"constant`

          - `required string ToolUseID`

          - `JsonElement Type "tool_search_tool_result"constant`

        - `class ContainerUploadBlock:`

          Response model for a file uploaded to the container.

          - `required string FileID`

          - `JsonElement Type "container_upload"constant`

      - `required Model Model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-opus-4-6"ClaudeOpus4_6`

          Most intelligent model for building agents and coding

        - `"claude-sonnet-4-6"ClaudeSonnet4_6`

          Frontier intelligence at scale — built for coding, agents, and enterprise workflows

        - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

          Premium model combining maximum intelligence with practical performance

        - `"claude-opus-4-5"ClaudeOpus4_5`

          Premium model combining maximum intelligence with practical performance

        - `"claude-3-7-sonnet-latest"Claude3_7SonnetLatest`

          High-performance model with early extended thinking

        - `"claude-3-7-sonnet-20250219"Claude3_7Sonnet20250219`

          High-performance model with early extended thinking

        - `"claude-3-5-haiku-latest"Claude3_5HaikuLatest`

          Fastest and most compact model for near-instant responsiveness

        - `"claude-3-5-haiku-20241022"Claude3_5Haiku20241022`

          Our fastest model

        - `"claude-haiku-4-5"ClaudeHaiku4_5`

          Hybrid model, capable of near-instant responses and extended thinking

        - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

          Hybrid model, capable of near-instant responses and extended thinking

        - `"claude-sonnet-4-20250514"ClaudeSonnet4_20250514`

          High-performance model with extended thinking

        - `"claude-sonnet-4-0"ClaudeSonnet4_0`

          High-performance model with extended thinking

        - `"claude-4-sonnet-20250514"Claude4Sonnet20250514`

          High-performance model with extended thinking

        - `"claude-sonnet-4-5"ClaudeSonnet4_5`

          Our best model for real-world agents and coding

        - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

          Our best model for real-world agents and coding

        - `"claude-opus-4-0"ClaudeOpus4_0`

          Our most capable model

        - `"claude-opus-4-20250514"ClaudeOpus4_20250514`

          Our most capable model

        - `"claude-4-opus-20250514"Claude4Opus20250514`

          Our most capable model

        - `"claude-opus-4-1-20250805"ClaudeOpus4_1_20250805`

          Our most capable model

        - `"claude-3-opus-latest"Claude3OpusLatest`

          Excels at writing and complex tasks

        - `"claude-3-opus-20240229"Claude_3_Opus_20240229`

          Excels at writing and complex tasks

        - `"claude-3-haiku-20240307"Claude_3_Haiku_20240307`

          Our previous most fast and cost-effective

      - `JsonElement Role "assistant"constant`

        Conversational role of the generated message.

        This will always be `"assistant"`.

      - `required StopReason? StopReason`

        The reason that we stopped.

        This may be one the following values:

        * `"end_turn"`: the model reached a natural stopping point
        * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
        * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
        * `"tool_use"`: the model invoked one or more tools
        * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
        * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

        In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

        - `"end_turn"EndTurn`

        - `"max_tokens"MaxTokens`

        - `"stop_sequence"StopSequence`

        - `"tool_use"ToolUse`

        - `"pause_turn"PauseTurn`

        - `"refusal"Refusal`

      - `required string? StopSequence`

        Which custom stop sequence was generated, if any.

        This value will be a non-null string if one of your custom stop sequences was generated.

      - `JsonElement Type "message"constant`

        Object type.

        For Messages, this is always `"message"`.

      - `required Usage Usage`

        Billing and rate-limit usage.

        Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

        Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

        For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

        Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

        - `required CacheCreation? CacheCreation`

          Breakdown of cached tokens by TTL

          - `required Long Ephemeral1hInputTokens`

            The number of input tokens used to create the 1 hour cache entry.

          - `required Long Ephemeral5mInputTokens`

            The number of input tokens used to create the 5 minute cache entry.

        - `required Long? CacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

        - `required Long? CacheReadInputTokens`

          The number of input tokens read from the cache.

        - `required string? InferenceGeo`

          The geographic region where inference was performed for this request.

        - `required Long InputTokens`

          The number of input tokens which were used.

        - `required Long OutputTokens`

          The number of output tokens which were used.

        - `required ServerToolUsage? ServerToolUse`

          The number of server tool requests.

          - `required Long WebFetchRequests`

            The number of web fetch tool requests.

          - `required Long WebSearchRequests`

            The number of web search tool requests.

        - `required ServiceTier? ServiceTier`

          If the request used the priority, standard, or batch tier.

          - `"standard"Standard`

          - `"priority"Priority`

          - `"batch"Batch`

    - `JsonElement Type "succeeded"constant`

  - `class MessageBatchErroredResult:`

    - `required ErrorResponse Error`

      - `required ErrorObject Error`

        - `class InvalidRequestError:`

          - `required string Message`

          - `JsonElement Type "invalid_request_error"constant`

        - `class AuthenticationError:`

          - `required string Message`

          - `JsonElement Type "authentication_error"constant`

        - `class BillingError:`

          - `required string Message`

          - `JsonElement Type "billing_error"constant`

        - `class PermissionError:`

          - `required string Message`

          - `JsonElement Type "permission_error"constant`

        - `class NotFoundError:`

          - `required string Message`

          - `JsonElement Type "not_found_error"constant`

        - `class RateLimitError:`

          - `required string Message`

          - `JsonElement Type "rate_limit_error"constant`

        - `class GatewayTimeoutError:`

          - `required string Message`

          - `JsonElement Type "timeout_error"constant`

        - `class ApiErrorObject:`

          - `required string Message`

          - `JsonElement Type "api_error"constant`

        - `class OverloadedError:`

          - `required string Message`

          - `JsonElement Type "overloaded_error"constant`

      - `required string? RequestID`

      - `JsonElement Type "error"constant`

    - `JsonElement Type "errored"constant`

  - `class MessageBatchCanceledResult:`

    - `JsonElement Type "canceled"constant`

  - `class MessageBatchExpiredResult:`

    - `JsonElement Type "expired"constant`

### Message Batch Succeeded Result

- `class MessageBatchSucceededResult:`

  - `required Message Message`

    - `required string ID`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `required Container? Container`

      Information about the container used in the request (for the code execution tool)

      - `required string ID`

        Identifier for the container used in this request

      - `required DateTimeOffset ExpiresAt`

        The time at which the container will expire.

    - `required IReadOnlyList<ContentBlock> Content`

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

      - `class TextBlock:`

        - `required IReadOnlyList<TextCitation>? Citations`

          Citations supporting the text block.

          The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `class CitationCharLocation:`

            - `required string CitedText`

            - `required Long DocumentIndex`

            - `required string? DocumentTitle`

            - `required Long EndCharIndex`

            - `required string? FileID`

            - `required Long StartCharIndex`

            - `JsonElement Type "char_location"constant`

          - `class CitationPageLocation:`

            - `required string CitedText`

            - `required Long DocumentIndex`

            - `required string? DocumentTitle`

            - `required Long EndPageNumber`

            - `required string? FileID`

            - `required Long StartPageNumber`

            - `JsonElement Type "page_location"constant`

          - `class CitationContentBlockLocation:`

            - `required string CitedText`

            - `required Long DocumentIndex`

            - `required string? DocumentTitle`

            - `required Long EndBlockIndex`

            - `required string? FileID`

            - `required Long StartBlockIndex`

            - `JsonElement Type "content_block_location"constant`

          - `class CitationsWebSearchResultLocation:`

            - `required string CitedText`

            - `required string EncryptedIndex`

            - `required string? Title`

            - `JsonElement Type "web_search_result_location"constant`

            - `required string Url`

          - `class CitationsSearchResultLocation:`

            - `required string CitedText`

            - `required Long EndBlockIndex`

            - `required Long SearchResultIndex`

            - `required string Source`

            - `required Long StartBlockIndex`

            - `required string? Title`

            - `JsonElement Type "search_result_location"constant`

        - `required string Text`

        - `JsonElement Type "text"constant`

      - `class ThinkingBlock:`

        - `required string Signature`

        - `required string Thinking`

        - `JsonElement Type "thinking"constant`

      - `class RedactedThinkingBlock:`

        - `required string Data`

        - `JsonElement Type "redacted_thinking"constant`

      - `class ToolUseBlock:`

        - `required string ID`

        - `required Caller Caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonElement Type "direct"constant`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `required string ToolID`

            - `JsonElement Type "code_execution_20250825"constant`

          - `class ServerToolCaller20260120:`

            - `required string ToolID`

            - `JsonElement Type "code_execution_20260120"constant`

        - `required IReadOnlyDictionary<string, JsonElement> Input`

        - `required string Name`

        - `JsonElement Type "tool_use"constant`

      - `class ServerToolUseBlock:`

        - `required string ID`

        - `required Caller Caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonElement Type "direct"constant`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `required string ToolID`

            - `JsonElement Type "code_execution_20250825"constant`

          - `class ServerToolCaller20260120:`

            - `required string ToolID`

            - `JsonElement Type "code_execution_20260120"constant`

        - `required IReadOnlyDictionary<string, JsonElement> Input`

        - `required Name Name`

          - `"web_search"WebSearch`

          - `"web_fetch"WebFetch`

          - `"code_execution"CodeExecution`

          - `"bash_code_execution"BashCodeExecution`

          - `"text_editor_code_execution"TextEditorCodeExecution`

          - `"tool_search_tool_regex"ToolSearchToolRegex`

          - `"tool_search_tool_bm25"ToolSearchToolBm25`

        - `JsonElement Type "server_tool_use"constant`

      - `class WebSearchToolResultBlock:`

        - `required Caller Caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonElement Type "direct"constant`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `required string ToolID`

            - `JsonElement Type "code_execution_20250825"constant`

          - `class ServerToolCaller20260120:`

            - `required string ToolID`

            - `JsonElement Type "code_execution_20260120"constant`

        - `required WebSearchToolResultBlockContent Content`

          - `class WebSearchToolResultError:`

            - `required WebSearchToolResultErrorCode ErrorCode`

              - `"invalid_tool_input"InvalidToolInput`

              - `"unavailable"Unavailable`

              - `"max_uses_exceeded"MaxUsesExceeded`

              - `"too_many_requests"TooManyRequests`

              - `"query_too_long"QueryTooLong`

              - `"request_too_large"RequestTooLarge`

            - `JsonElement Type "web_search_tool_result_error"constant`

          - `IReadOnlyList<WebSearchResultBlock>`

            - `required string EncryptedContent`

            - `required string? PageAge`

            - `required string Title`

            - `JsonElement Type "web_search_result"constant`

            - `required string Url`

        - `required string ToolUseID`

        - `JsonElement Type "web_search_tool_result"constant`

      - `class WebFetchToolResultBlock:`

        - `required Caller Caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonElement Type "direct"constant`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `required string ToolID`

            - `JsonElement Type "code_execution_20250825"constant`

          - `class ServerToolCaller20260120:`

            - `required string ToolID`

            - `JsonElement Type "code_execution_20260120"constant`

        - `required Content Content`

          - `class WebFetchToolResultErrorBlock:`

            - `required WebFetchToolResultErrorCode ErrorCode`

              - `"invalid_tool_input"InvalidToolInput`

              - `"url_too_long"UrlTooLong`

              - `"url_not_allowed"UrlNotAllowed`

              - `"url_not_accessible"UrlNotAccessible`

              - `"unsupported_content_type"UnsupportedContentType`

              - `"too_many_requests"TooManyRequests`

              - `"max_uses_exceeded"MaxUsesExceeded`

              - `"unavailable"Unavailable`

            - `JsonElement Type "web_fetch_tool_result_error"constant`

          - `class WebFetchBlock:`

            - `required DocumentBlock Content`

              - `required CitationsConfig? Citations`

                Citation configuration for the document

                - `required Boolean Enabled`

              - `required Source Source`

                - `class Base64PdfSource:`

                  - `required string Data`

                  - `JsonElement MediaType "application/pdf"constant`

                  - `JsonElement Type "base64"constant`

                - `class PlainTextSource:`

                  - `required string Data`

                  - `JsonElement MediaType "text/plain"constant`

                  - `JsonElement Type "text"constant`

              - `required string? Title`

                The title of the document

              - `JsonElement Type "document"constant`

            - `required string? RetrievedAt`

              ISO 8601 timestamp when the content was retrieved

            - `JsonElement Type "web_fetch_result"constant`

            - `required string Url`

              Fetched content URL

        - `required string ToolUseID`

        - `JsonElement Type "web_fetch_tool_result"constant`

      - `class CodeExecutionToolResultBlock:`

        - `required CodeExecutionToolResultBlockContent Content`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `class CodeExecutionToolResultError:`

            - `required CodeExecutionToolResultErrorCode ErrorCode`

              - `"invalid_tool_input"InvalidToolInput`

              - `"unavailable"Unavailable`

              - `"too_many_requests"TooManyRequests`

              - `"execution_time_exceeded"ExecutionTimeExceeded`

            - `JsonElement Type "code_execution_tool_result_error"constant`

          - `class CodeExecutionResultBlock:`

            - `required IReadOnlyList<CodeExecutionOutputBlock> Content`

              - `required string FileID`

              - `JsonElement Type "code_execution_output"constant`

            - `required Long ReturnCode`

            - `required string Stderr`

            - `required string Stdout`

            - `JsonElement Type "code_execution_result"constant`

          - `class EncryptedCodeExecutionResultBlock:`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `required IReadOnlyList<CodeExecutionOutputBlock> Content`

              - `required string FileID`

              - `JsonElement Type "code_execution_output"constant`

            - `required string EncryptedStdout`

            - `required Long ReturnCode`

            - `required string Stderr`

            - `JsonElement Type "encrypted_code_execution_result"constant`

        - `required string ToolUseID`

        - `JsonElement Type "code_execution_tool_result"constant`

      - `class BashCodeExecutionToolResultBlock:`

        - `required Content Content`

          - `class BashCodeExecutionToolResultError:`

            - `required BashCodeExecutionToolResultErrorCode ErrorCode`

              - `"invalid_tool_input"InvalidToolInput`

              - `"unavailable"Unavailable`

              - `"too_many_requests"TooManyRequests`

              - `"execution_time_exceeded"ExecutionTimeExceeded`

              - `"output_file_too_large"OutputFileTooLarge`

            - `JsonElement Type "bash_code_execution_tool_result_error"constant`

          - `class BashCodeExecutionResultBlock:`

            - `required IReadOnlyList<BashCodeExecutionOutputBlock> Content`

              - `required string FileID`

              - `JsonElement Type "bash_code_execution_output"constant`

            - `required Long ReturnCode`

            - `required string Stderr`

            - `required string Stdout`

            - `JsonElement Type "bash_code_execution_result"constant`

        - `required string ToolUseID`

        - `JsonElement Type "bash_code_execution_tool_result"constant`

      - `class TextEditorCodeExecutionToolResultBlock:`

        - `required Content Content`

          - `class TextEditorCodeExecutionToolResultError:`

            - `required TextEditorCodeExecutionToolResultErrorCode ErrorCode`

              - `"invalid_tool_input"InvalidToolInput`

              - `"unavailable"Unavailable`

              - `"too_many_requests"TooManyRequests`

              - `"execution_time_exceeded"ExecutionTimeExceeded`

              - `"file_not_found"FileNotFound`

            - `required string? ErrorMessage`

            - `JsonElement Type "text_editor_code_execution_tool_result_error"constant`

          - `class TextEditorCodeExecutionViewResultBlock:`

            - `required string Content`

            - `required FileType FileType`

              - `"text"Text`

              - `"image"Image`

              - `"pdf"Pdf`

            - `required Long? NumLines`

            - `required Long? StartLine`

            - `required Long? TotalLines`

            - `JsonElement Type "text_editor_code_execution_view_result"constant`

          - `class TextEditorCodeExecutionCreateResultBlock:`

            - `required Boolean IsFileUpdate`

            - `JsonElement Type "text_editor_code_execution_create_result"constant`

          - `class TextEditorCodeExecutionStrReplaceResultBlock:`

            - `required IReadOnlyList<string>? Lines`

            - `required Long? NewLines`

            - `required Long? NewStart`

            - `required Long? OldLines`

            - `required Long? OldStart`

            - `JsonElement Type "text_editor_code_execution_str_replace_result"constant`

        - `required string ToolUseID`

        - `JsonElement Type "text_editor_code_execution_tool_result"constant`

      - `class ToolSearchToolResultBlock:`

        - `required Content Content`

          - `class ToolSearchToolResultError:`

            - `required ToolSearchToolResultErrorCode ErrorCode`

              - `"invalid_tool_input"InvalidToolInput`

              - `"unavailable"Unavailable`

              - `"too_many_requests"TooManyRequests`

              - `"execution_time_exceeded"ExecutionTimeExceeded`

            - `required string? ErrorMessage`

            - `JsonElement Type "tool_search_tool_result_error"constant`

          - `class ToolSearchToolSearchResultBlock:`

            - `required IReadOnlyList<ToolReferenceBlock> ToolReferences`

              - `required string ToolName`

              - `JsonElement Type "tool_reference"constant`

            - `JsonElement Type "tool_search_tool_search_result"constant`

        - `required string ToolUseID`

        - `JsonElement Type "tool_search_tool_result"constant`

      - `class ContainerUploadBlock:`

        Response model for a file uploaded to the container.

        - `required string FileID`

        - `JsonElement Type "container_upload"constant`

    - `required Model Model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-opus-4-6"ClaudeOpus4_6`

        Most intelligent model for building agents and coding

      - `"claude-sonnet-4-6"ClaudeSonnet4_6`

        Frontier intelligence at scale — built for coding, agents, and enterprise workflows

      - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

        Premium model combining maximum intelligence with practical performance

      - `"claude-opus-4-5"ClaudeOpus4_5`

        Premium model combining maximum intelligence with practical performance

      - `"claude-3-7-sonnet-latest"Claude3_7SonnetLatest`

        High-performance model with early extended thinking

      - `"claude-3-7-sonnet-20250219"Claude3_7Sonnet20250219`

        High-performance model with early extended thinking

      - `"claude-3-5-haiku-latest"Claude3_5HaikuLatest`

        Fastest and most compact model for near-instant responsiveness

      - `"claude-3-5-haiku-20241022"Claude3_5Haiku20241022`

        Our fastest model

      - `"claude-haiku-4-5"ClaudeHaiku4_5`

        Hybrid model, capable of near-instant responses and extended thinking

      - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

        Hybrid model, capable of near-instant responses and extended thinking

      - `"claude-sonnet-4-20250514"ClaudeSonnet4_20250514`

        High-performance model with extended thinking

      - `"claude-sonnet-4-0"ClaudeSonnet4_0`

        High-performance model with extended thinking

      - `"claude-4-sonnet-20250514"Claude4Sonnet20250514`

        High-performance model with extended thinking

      - `"claude-sonnet-4-5"ClaudeSonnet4_5`

        Our best model for real-world agents and coding

      - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

        Our best model for real-world agents and coding

      - `"claude-opus-4-0"ClaudeOpus4_0`

        Our most capable model

      - `"claude-opus-4-20250514"ClaudeOpus4_20250514`

        Our most capable model

      - `"claude-4-opus-20250514"Claude4Opus20250514`

        Our most capable model

      - `"claude-opus-4-1-20250805"ClaudeOpus4_1_20250805`

        Our most capable model

      - `"claude-3-opus-latest"Claude3OpusLatest`

        Excels at writing and complex tasks

      - `"claude-3-opus-20240229"Claude_3_Opus_20240229`

        Excels at writing and complex tasks

      - `"claude-3-haiku-20240307"Claude_3_Haiku_20240307`

        Our previous most fast and cost-effective

    - `JsonElement Role "assistant"constant`

      Conversational role of the generated message.

      This will always be `"assistant"`.

    - `required StopReason? StopReason`

      The reason that we stopped.

      This may be one the following values:

      * `"end_turn"`: the model reached a natural stopping point
      * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
      * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
      * `"tool_use"`: the model invoked one or more tools
      * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
      * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

      In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

      - `"end_turn"EndTurn`

      - `"max_tokens"MaxTokens`

      - `"stop_sequence"StopSequence`

      - `"tool_use"ToolUse`

      - `"pause_turn"PauseTurn`

      - `"refusal"Refusal`

    - `required string? StopSequence`

      Which custom stop sequence was generated, if any.

      This value will be a non-null string if one of your custom stop sequences was generated.

    - `JsonElement Type "message"constant`

      Object type.

      For Messages, this is always `"message"`.

    - `required Usage Usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `required CacheCreation? CacheCreation`

        Breakdown of cached tokens by TTL

        - `required Long Ephemeral1hInputTokens`

          The number of input tokens used to create the 1 hour cache entry.

        - `required Long Ephemeral5mInputTokens`

          The number of input tokens used to create the 5 minute cache entry.

      - `required Long? CacheCreationInputTokens`

        The number of input tokens used to create the cache entry.

      - `required Long? CacheReadInputTokens`

        The number of input tokens read from the cache.

      - `required string? InferenceGeo`

        The geographic region where inference was performed for this request.

      - `required Long InputTokens`

        The number of input tokens which were used.

      - `required Long OutputTokens`

        The number of output tokens which were used.

      - `required ServerToolUsage? ServerToolUse`

        The number of server tool requests.

        - `required Long WebFetchRequests`

          The number of web fetch tool requests.

        - `required Long WebSearchRequests`

          The number of web search tool requests.

      - `required ServiceTier? ServiceTier`

        If the request used the priority, standard, or batch tier.

        - `"standard"Standard`

        - `"priority"Priority`

        - `"batch"Batch`

  - `JsonElement Type "succeeded"constant`

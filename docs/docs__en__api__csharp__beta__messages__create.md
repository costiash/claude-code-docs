## Create

`BetaMessage Beta.Messages.Create(MessageCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

### Parameters

- `MessageCreateParams parameters`

  - `required Long maxTokens`

    Body param: The maximum number of tokens to generate before stopping.

    Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

    Different models have different maximum values for this parameter.  See [models](https://docs.claude.com/en/docs/models-overview) for details.

  - `required IReadOnlyList<BetaMessageParam> messages`

    Body param: Input messages.

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

      - `IReadOnlyList<BetaContentBlockParam>`

        - `class BetaTextBlockParam:`

          - `required string Text`

          - `JsonElement Type "text"constant`

          - `BetaCacheControlEphemeral? CacheControl`

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

          - `IReadOnlyList<BetaTextCitationParam>? Citations`

            - `class BetaCitationCharLocationParam:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndCharIndex`

              - `required Long StartCharIndex`

              - `JsonElement Type "char_location"constant`

            - `class BetaCitationPageLocationParam:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndPageNumber`

              - `required Long StartPageNumber`

              - `JsonElement Type "page_location"constant`

            - `class BetaCitationContentBlockLocationParam:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndBlockIndex`

              - `required Long StartBlockIndex`

              - `JsonElement Type "content_block_location"constant`

            - `class BetaCitationWebSearchResultLocationParam:`

              - `required string CitedText`

              - `required string EncryptedIndex`

              - `required string? Title`

              - `JsonElement Type "web_search_result_location"constant`

              - `required string Url`

            - `class BetaCitationSearchResultLocationParam:`

              - `required string CitedText`

              - `required Long EndBlockIndex`

              - `required Long SearchResultIndex`

              - `required string Source`

              - `required Long StartBlockIndex`

              - `required string? Title`

              - `JsonElement Type "search_result_location"constant`

        - `class BetaImageBlockParam:`

          - `required Source Source`

            - `class BetaBase64ImageSource:`

              - `required string Data`

              - `required MediaType MediaType`

                - `"image/jpeg"ImageJpeg`

                - `"image/png"ImagePng`

                - `"image/gif"ImageGif`

                - `"image/webp"ImageWebP`

              - `JsonElement Type "base64"constant`

            - `class BetaUrlImageSource:`

              - `JsonElement Type "url"constant`

              - `required string Url`

            - `class BetaFileImageSource:`

              - `required string FileID`

              - `JsonElement Type "file"constant`

          - `JsonElement Type "image"constant`

          - `BetaCacheControlEphemeral? CacheControl`

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

        - `class BetaRequestDocumentBlock:`

          - `required Source Source`

            - `class BetaBase64PdfSource:`

              - `required string Data`

              - `JsonElement MediaType "application/pdf"constant`

              - `JsonElement Type "base64"constant`

            - `class BetaPlainTextSource:`

              - `required string Data`

              - `JsonElement MediaType "text/plain"constant`

              - `JsonElement Type "text"constant`

            - `class BetaContentBlockSource:`

              - `required Content Content`

                - `string`

                - `IReadOnlyList<BetaContentBlockSourceContent>`

                  - `class BetaTextBlockParam:`

                    - `required string Text`

                    - `JsonElement Type "text"constant`

                    - `BetaCacheControlEphemeral? CacheControl`

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

                    - `IReadOnlyList<BetaTextCitationParam>? Citations`

                      - `class BetaCitationCharLocationParam:`

                        - `required string CitedText`

                        - `required Long DocumentIndex`

                        - `required string? DocumentTitle`

                        - `required Long EndCharIndex`

                        - `required Long StartCharIndex`

                        - `JsonElement Type "char_location"constant`

                      - `class BetaCitationPageLocationParam:`

                        - `required string CitedText`

                        - `required Long DocumentIndex`

                        - `required string? DocumentTitle`

                        - `required Long EndPageNumber`

                        - `required Long StartPageNumber`

                        - `JsonElement Type "page_location"constant`

                      - `class BetaCitationContentBlockLocationParam:`

                        - `required string CitedText`

                        - `required Long DocumentIndex`

                        - `required string? DocumentTitle`

                        - `required Long EndBlockIndex`

                        - `required Long StartBlockIndex`

                        - `JsonElement Type "content_block_location"constant`

                      - `class BetaCitationWebSearchResultLocationParam:`

                        - `required string CitedText`

                        - `required string EncryptedIndex`

                        - `required string? Title`

                        - `JsonElement Type "web_search_result_location"constant`

                        - `required string Url`

                      - `class BetaCitationSearchResultLocationParam:`

                        - `required string CitedText`

                        - `required Long EndBlockIndex`

                        - `required Long SearchResultIndex`

                        - `required string Source`

                        - `required Long StartBlockIndex`

                        - `required string? Title`

                        - `JsonElement Type "search_result_location"constant`

                  - `class BetaImageBlockParam:`

                    - `required Source Source`

                      - `class BetaBase64ImageSource:`

                        - `required string Data`

                        - `required MediaType MediaType`

                          - `"image/jpeg"ImageJpeg`

                          - `"image/png"ImagePng`

                          - `"image/gif"ImageGif`

                          - `"image/webp"ImageWebP`

                        - `JsonElement Type "base64"constant`

                      - `class BetaUrlImageSource:`

                        - `JsonElement Type "url"constant`

                        - `required string Url`

                      - `class BetaFileImageSource:`

                        - `required string FileID`

                        - `JsonElement Type "file"constant`

                    - `JsonElement Type "image"constant`

                    - `BetaCacheControlEphemeral? CacheControl`

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

            - `class BetaUrlPdfSource:`

              - `JsonElement Type "url"constant`

              - `required string Url`

            - `class BetaFileDocumentSource:`

              - `required string FileID`

              - `JsonElement Type "file"constant`

          - `JsonElement Type "document"constant`

          - `BetaCacheControlEphemeral? CacheControl`

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

          - `BetaCitationsConfigParam? Citations`

            - `Boolean Enabled`

          - `string? Context`

          - `string? Title`

        - `class BetaSearchResultBlockParam:`

          - `required IReadOnlyList<BetaTextBlockParam> Content`

            - `required string Text`

            - `JsonElement Type "text"constant`

            - `BetaCacheControlEphemeral? CacheControl`

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

            - `IReadOnlyList<BetaTextCitationParam>? Citations`

              - `class BetaCitationCharLocationParam:`

                - `required string CitedText`

                - `required Long DocumentIndex`

                - `required string? DocumentTitle`

                - `required Long EndCharIndex`

                - `required Long StartCharIndex`

                - `JsonElement Type "char_location"constant`

              - `class BetaCitationPageLocationParam:`

                - `required string CitedText`

                - `required Long DocumentIndex`

                - `required string? DocumentTitle`

                - `required Long EndPageNumber`

                - `required Long StartPageNumber`

                - `JsonElement Type "page_location"constant`

              - `class BetaCitationContentBlockLocationParam:`

                - `required string CitedText`

                - `required Long DocumentIndex`

                - `required string? DocumentTitle`

                - `required Long EndBlockIndex`

                - `required Long StartBlockIndex`

                - `JsonElement Type "content_block_location"constant`

              - `class BetaCitationWebSearchResultLocationParam:`

                - `required string CitedText`

                - `required string EncryptedIndex`

                - `required string? Title`

                - `JsonElement Type "web_search_result_location"constant`

                - `required string Url`

              - `class BetaCitationSearchResultLocationParam:`

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

          - `BetaCacheControlEphemeral? CacheControl`

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

          - `BetaCitationsConfigParam Citations`

            - `Boolean Enabled`

        - `class BetaThinkingBlockParam:`

          - `required string Signature`

          - `required string Thinking`

          - `JsonElement Type "thinking"constant`

        - `class BetaRedactedThinkingBlockParam:`

          - `required string Data`

          - `JsonElement Type "redacted_thinking"constant`

        - `class BetaToolUseBlockParam:`

          - `required string ID`

          - `required IReadOnlyDictionary<string, JsonElement> Input`

          - `required string Name`

          - `JsonElement Type "tool_use"constant`

          - `BetaCacheControlEphemeral? CacheControl`

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

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

              - `JsonElement Type "direct"constant`

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `required string ToolID`

              - `JsonElement Type "code_execution_20250825"constant`

            - `class BetaServerToolCaller20260120:`

              - `required string ToolID`

              - `JsonElement Type "code_execution_20260120"constant`

        - `class BetaToolResultBlockParam:`

          - `required string ToolUseID`

          - `JsonElement Type "tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

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

              - `class BetaTextBlockParam:`

                - `required string Text`

                - `JsonElement Type "text"constant`

                - `BetaCacheControlEphemeral? CacheControl`

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

                - `IReadOnlyList<BetaTextCitationParam>? Citations`

                  - `class BetaCitationCharLocationParam:`

                    - `required string CitedText`

                    - `required Long DocumentIndex`

                    - `required string? DocumentTitle`

                    - `required Long EndCharIndex`

                    - `required Long StartCharIndex`

                    - `JsonElement Type "char_location"constant`

                  - `class BetaCitationPageLocationParam:`

                    - `required string CitedText`

                    - `required Long DocumentIndex`

                    - `required string? DocumentTitle`

                    - `required Long EndPageNumber`

                    - `required Long StartPageNumber`

                    - `JsonElement Type "page_location"constant`

                  - `class BetaCitationContentBlockLocationParam:`

                    - `required string CitedText`

                    - `required Long DocumentIndex`

                    - `required string? DocumentTitle`

                    - `required Long EndBlockIndex`

                    - `required Long StartBlockIndex`

                    - `JsonElement Type "content_block_location"constant`

                  - `class BetaCitationWebSearchResultLocationParam:`

                    - `required string CitedText`

                    - `required string EncryptedIndex`

                    - `required string? Title`

                    - `JsonElement Type "web_search_result_location"constant`

                    - `required string Url`

                  - `class BetaCitationSearchResultLocationParam:`

                    - `required string CitedText`

                    - `required Long EndBlockIndex`

                    - `required Long SearchResultIndex`

                    - `required string Source`

                    - `required Long StartBlockIndex`

                    - `required string? Title`

                    - `JsonElement Type "search_result_location"constant`

              - `class BetaImageBlockParam:`

                - `required Source Source`

                  - `class BetaBase64ImageSource:`

                    - `required string Data`

                    - `required MediaType MediaType`

                      - `"image/jpeg"ImageJpeg`

                      - `"image/png"ImagePng`

                      - `"image/gif"ImageGif`

                      - `"image/webp"ImageWebP`

                    - `JsonElement Type "base64"constant`

                  - `class BetaUrlImageSource:`

                    - `JsonElement Type "url"constant`

                    - `required string Url`

                  - `class BetaFileImageSource:`

                    - `required string FileID`

                    - `JsonElement Type "file"constant`

                - `JsonElement Type "image"constant`

                - `BetaCacheControlEphemeral? CacheControl`

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

              - `class BetaSearchResultBlockParam:`

                - `required IReadOnlyList<BetaTextBlockParam> Content`

                  - `required string Text`

                  - `JsonElement Type "text"constant`

                  - `BetaCacheControlEphemeral? CacheControl`

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

                  - `IReadOnlyList<BetaTextCitationParam>? Citations`

                    - `class BetaCitationCharLocationParam:`

                      - `required string CitedText`

                      - `required Long DocumentIndex`

                      - `required string? DocumentTitle`

                      - `required Long EndCharIndex`

                      - `required Long StartCharIndex`

                      - `JsonElement Type "char_location"constant`

                    - `class BetaCitationPageLocationParam:`

                      - `required string CitedText`

                      - `required Long DocumentIndex`

                      - `required string? DocumentTitle`

                      - `required Long EndPageNumber`

                      - `required Long StartPageNumber`

                      - `JsonElement Type "page_location"constant`

                    - `class BetaCitationContentBlockLocationParam:`

                      - `required string CitedText`

                      - `required Long DocumentIndex`

                      - `required string? DocumentTitle`

                      - `required Long EndBlockIndex`

                      - `required Long StartBlockIndex`

                      - `JsonElement Type "content_block_location"constant`

                    - `class BetaCitationWebSearchResultLocationParam:`

                      - `required string CitedText`

                      - `required string EncryptedIndex`

                      - `required string? Title`

                      - `JsonElement Type "web_search_result_location"constant`

                      - `required string Url`

                    - `class BetaCitationSearchResultLocationParam:`

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

                - `BetaCacheControlEphemeral? CacheControl`

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

                - `BetaCitationsConfigParam Citations`

                  - `Boolean Enabled`

              - `class BetaRequestDocumentBlock:`

                - `required Source Source`

                  - `class BetaBase64PdfSource:`

                    - `required string Data`

                    - `JsonElement MediaType "application/pdf"constant`

                    - `JsonElement Type "base64"constant`

                  - `class BetaPlainTextSource:`

                    - `required string Data`

                    - `JsonElement MediaType "text/plain"constant`

                    - `JsonElement Type "text"constant`

                  - `class BetaContentBlockSource:`

                    - `required Content Content`

                      - `string`

                      - `IReadOnlyList<BetaContentBlockSourceContent>`

                        - `class BetaTextBlockParam:`

                          - `required string Text`

                          - `JsonElement Type "text"constant`

                          - `BetaCacheControlEphemeral? CacheControl`

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

                          - `IReadOnlyList<BetaTextCitationParam>? Citations`

                            - `class BetaCitationCharLocationParam:`

                              - `required string CitedText`

                              - `required Long DocumentIndex`

                              - `required string? DocumentTitle`

                              - `required Long EndCharIndex`

                              - `required Long StartCharIndex`

                              - `JsonElement Type "char_location"constant`

                            - `class BetaCitationPageLocationParam:`

                              - `required string CitedText`

                              - `required Long DocumentIndex`

                              - `required string? DocumentTitle`

                              - `required Long EndPageNumber`

                              - `required Long StartPageNumber`

                              - `JsonElement Type "page_location"constant`

                            - `class BetaCitationContentBlockLocationParam:`

                              - `required string CitedText`

                              - `required Long DocumentIndex`

                              - `required string? DocumentTitle`

                              - `required Long EndBlockIndex`

                              - `required Long StartBlockIndex`

                              - `JsonElement Type "content_block_location"constant`

                            - `class BetaCitationWebSearchResultLocationParam:`

                              - `required string CitedText`

                              - `required string EncryptedIndex`

                              - `required string? Title`

                              - `JsonElement Type "web_search_result_location"constant`

                              - `required string Url`

                            - `class BetaCitationSearchResultLocationParam:`

                              - `required string CitedText`

                              - `required Long EndBlockIndex`

                              - `required Long SearchResultIndex`

                              - `required string Source`

                              - `required Long StartBlockIndex`

                              - `required string? Title`

                              - `JsonElement Type "search_result_location"constant`

                        - `class BetaImageBlockParam:`

                          - `required Source Source`

                            - `class BetaBase64ImageSource:`

                              - `required string Data`

                              - `required MediaType MediaType`

                                - `"image/jpeg"ImageJpeg`

                                - `"image/png"ImagePng`

                                - `"image/gif"ImageGif`

                                - `"image/webp"ImageWebP`

                              - `JsonElement Type "base64"constant`

                            - `class BetaUrlImageSource:`

                              - `JsonElement Type "url"constant`

                              - `required string Url`

                            - `class BetaFileImageSource:`

                              - `required string FileID`

                              - `JsonElement Type "file"constant`

                          - `JsonElement Type "image"constant`

                          - `BetaCacheControlEphemeral? CacheControl`

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

                  - `class BetaUrlPdfSource:`

                    - `JsonElement Type "url"constant`

                    - `required string Url`

                  - `class BetaFileDocumentSource:`

                    - `required string FileID`

                    - `JsonElement Type "file"constant`

                - `JsonElement Type "document"constant`

                - `BetaCacheControlEphemeral? CacheControl`

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

                - `BetaCitationsConfigParam? Citations`

                  - `Boolean Enabled`

                - `string? Context`

                - `string? Title`

              - `class BetaToolReferenceBlockParam:`

                Tool reference block that can be included in tool_result content.

                - `required string ToolName`

                - `JsonElement Type "tool_reference"constant`

                - `BetaCacheControlEphemeral? CacheControl`

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

        - `class BetaServerToolUseBlockParam:`

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

          - `BetaCacheControlEphemeral? CacheControl`

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

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

              - `JsonElement Type "direct"constant`

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `required string ToolID`

              - `JsonElement Type "code_execution_20250825"constant`

            - `class BetaServerToolCaller20260120:`

              - `required string ToolID`

              - `JsonElement Type "code_execution_20260120"constant`

        - `class BetaWebSearchToolResultBlockParam:`

          - `required BetaWebSearchToolResultBlockParamContent Content`

            - `IReadOnlyList<BetaWebSearchResultBlockParam>`

              - `required string EncryptedContent`

              - `required string Title`

              - `JsonElement Type "web_search_result"constant`

              - `required string Url`

              - `string? PageAge`

            - `class BetaWebSearchToolRequestError:`

              - `required BetaWebSearchToolResultErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"max_uses_exceeded"MaxUsesExceeded`

                - `"too_many_requests"TooManyRequests`

                - `"query_too_long"QueryTooLong`

                - `"request_too_large"RequestTooLarge`

              - `JsonElement Type "web_search_tool_result_error"constant`

          - `required string ToolUseID`

          - `JsonElement Type "web_search_tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

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

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

              - `JsonElement Type "direct"constant`

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `required string ToolID`

              - `JsonElement Type "code_execution_20250825"constant`

            - `class BetaServerToolCaller20260120:`

              - `required string ToolID`

              - `JsonElement Type "code_execution_20260120"constant`

        - `class BetaWebFetchToolResultBlockParam:`

          - `required Content Content`

            - `class BetaWebFetchToolResultErrorBlockParam:`

              - `required BetaWebFetchToolResultErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"url_too_long"UrlTooLong`

                - `"url_not_allowed"UrlNotAllowed`

                - `"url_not_accessible"UrlNotAccessible`

                - `"unsupported_content_type"UnsupportedContentType`

                - `"too_many_requests"TooManyRequests`

                - `"max_uses_exceeded"MaxUsesExceeded`

                - `"unavailable"Unavailable`

              - `JsonElement Type "web_fetch_tool_result_error"constant`

            - `class BetaWebFetchBlockParam:`

              - `required BetaRequestDocumentBlock Content`

                - `required Source Source`

                  - `class BetaBase64PdfSource:`

                    - `required string Data`

                    - `JsonElement MediaType "application/pdf"constant`

                    - `JsonElement Type "base64"constant`

                  - `class BetaPlainTextSource:`

                    - `required string Data`

                    - `JsonElement MediaType "text/plain"constant`

                    - `JsonElement Type "text"constant`

                  - `class BetaContentBlockSource:`

                    - `required Content Content`

                      - `string`

                      - `IReadOnlyList<BetaContentBlockSourceContent>`

                        - `class BetaTextBlockParam:`

                          - `required string Text`

                          - `JsonElement Type "text"constant`

                          - `BetaCacheControlEphemeral? CacheControl`

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

                          - `IReadOnlyList<BetaTextCitationParam>? Citations`

                            - `class BetaCitationCharLocationParam:`

                              - `required string CitedText`

                              - `required Long DocumentIndex`

                              - `required string? DocumentTitle`

                              - `required Long EndCharIndex`

                              - `required Long StartCharIndex`

                              - `JsonElement Type "char_location"constant`

                            - `class BetaCitationPageLocationParam:`

                              - `required string CitedText`

                              - `required Long DocumentIndex`

                              - `required string? DocumentTitle`

                              - `required Long EndPageNumber`

                              - `required Long StartPageNumber`

                              - `JsonElement Type "page_location"constant`

                            - `class BetaCitationContentBlockLocationParam:`

                              - `required string CitedText`

                              - `required Long DocumentIndex`

                              - `required string? DocumentTitle`

                              - `required Long EndBlockIndex`

                              - `required Long StartBlockIndex`

                              - `JsonElement Type "content_block_location"constant`

                            - `class BetaCitationWebSearchResultLocationParam:`

                              - `required string CitedText`

                              - `required string EncryptedIndex`

                              - `required string? Title`

                              - `JsonElement Type "web_search_result_location"constant`

                              - `required string Url`

                            - `class BetaCitationSearchResultLocationParam:`

                              - `required string CitedText`

                              - `required Long EndBlockIndex`

                              - `required Long SearchResultIndex`

                              - `required string Source`

                              - `required Long StartBlockIndex`

                              - `required string? Title`

                              - `JsonElement Type "search_result_location"constant`

                        - `class BetaImageBlockParam:`

                          - `required Source Source`

                            - `class BetaBase64ImageSource:`

                              - `required string Data`

                              - `required MediaType MediaType`

                                - `"image/jpeg"ImageJpeg`

                                - `"image/png"ImagePng`

                                - `"image/gif"ImageGif`

                                - `"image/webp"ImageWebP`

                              - `JsonElement Type "base64"constant`

                            - `class BetaUrlImageSource:`

                              - `JsonElement Type "url"constant`

                              - `required string Url`

                            - `class BetaFileImageSource:`

                              - `required string FileID`

                              - `JsonElement Type "file"constant`

                          - `JsonElement Type "image"constant`

                          - `BetaCacheControlEphemeral? CacheControl`

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

                  - `class BetaUrlPdfSource:`

                    - `JsonElement Type "url"constant`

                    - `required string Url`

                  - `class BetaFileDocumentSource:`

                    - `required string FileID`

                    - `JsonElement Type "file"constant`

                - `JsonElement Type "document"constant`

                - `BetaCacheControlEphemeral? CacheControl`

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

                - `BetaCitationsConfigParam? Citations`

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

          - `BetaCacheControlEphemeral? CacheControl`

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

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

              - `JsonElement Type "direct"constant`

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `required string ToolID`

              - `JsonElement Type "code_execution_20250825"constant`

            - `class BetaServerToolCaller20260120:`

              - `required string ToolID`

              - `JsonElement Type "code_execution_20260120"constant`

        - `class BetaCodeExecutionToolResultBlockParam:`

          - `required BetaCodeExecutionToolResultBlockParamContent Content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class BetaCodeExecutionToolResultErrorParam:`

              - `required BetaCodeExecutionToolResultErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"too_many_requests"TooManyRequests`

                - `"execution_time_exceeded"ExecutionTimeExceeded`

              - `JsonElement Type "code_execution_tool_result_error"constant`

            - `class BetaCodeExecutionResultBlockParam:`

              - `required IReadOnlyList<BetaCodeExecutionOutputBlockParam> Content`

                - `required string FileID`

                - `JsonElement Type "code_execution_output"constant`

              - `required Long ReturnCode`

              - `required string Stderr`

              - `required string Stdout`

              - `JsonElement Type "code_execution_result"constant`

            - `class BetaEncryptedCodeExecutionResultBlockParam:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `required IReadOnlyList<BetaCodeExecutionOutputBlockParam> Content`

                - `required string FileID`

                - `JsonElement Type "code_execution_output"constant`

              - `required string EncryptedStdout`

              - `required Long ReturnCode`

              - `required string Stderr`

              - `JsonElement Type "encrypted_code_execution_result"constant`

          - `required string ToolUseID`

          - `JsonElement Type "code_execution_tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

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

        - `class BetaBashCodeExecutionToolResultBlockParam:`

          - `required Content Content`

            - `class BetaBashCodeExecutionToolResultErrorParam:`

              - `required ErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"too_many_requests"TooManyRequests`

                - `"execution_time_exceeded"ExecutionTimeExceeded`

                - `"output_file_too_large"OutputFileTooLarge`

              - `JsonElement Type "bash_code_execution_tool_result_error"constant`

            - `class BetaBashCodeExecutionResultBlockParam:`

              - `required IReadOnlyList<BetaBashCodeExecutionOutputBlockParam> Content`

                - `required string FileID`

                - `JsonElement Type "bash_code_execution_output"constant`

              - `required Long ReturnCode`

              - `required string Stderr`

              - `required string Stdout`

              - `JsonElement Type "bash_code_execution_result"constant`

          - `required string ToolUseID`

          - `JsonElement Type "bash_code_execution_tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

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

        - `class BetaTextEditorCodeExecutionToolResultBlockParam:`

          - `required Content Content`

            - `class BetaTextEditorCodeExecutionToolResultErrorParam:`

              - `required ErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"too_many_requests"TooManyRequests`

                - `"execution_time_exceeded"ExecutionTimeExceeded`

                - `"file_not_found"FileNotFound`

              - `JsonElement Type "text_editor_code_execution_tool_result_error"constant`

              - `string? ErrorMessage`

            - `class BetaTextEditorCodeExecutionViewResultBlockParam:`

              - `required string Content`

              - `required FileType FileType`

                - `"text"Text`

                - `"image"Image`

                - `"pdf"Pdf`

              - `JsonElement Type "text_editor_code_execution_view_result"constant`

              - `Long? NumLines`

              - `Long? StartLine`

              - `Long? TotalLines`

            - `class BetaTextEditorCodeExecutionCreateResultBlockParam:`

              - `required Boolean IsFileUpdate`

              - `JsonElement Type "text_editor_code_execution_create_result"constant`

            - `class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:`

              - `JsonElement Type "text_editor_code_execution_str_replace_result"constant`

              - `IReadOnlyList<string>? Lines`

              - `Long? NewLines`

              - `Long? NewStart`

              - `Long? OldLines`

              - `Long? OldStart`

          - `required string ToolUseID`

          - `JsonElement Type "text_editor_code_execution_tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

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

        - `class BetaToolSearchToolResultBlockParam:`

          - `required Content Content`

            - `class BetaToolSearchToolResultErrorParam:`

              - `required ErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"too_many_requests"TooManyRequests`

                - `"execution_time_exceeded"ExecutionTimeExceeded`

              - `JsonElement Type "tool_search_tool_result_error"constant`

            - `class BetaToolSearchToolSearchResultBlockParam:`

              - `required IReadOnlyList<BetaToolReferenceBlockParam> ToolReferences`

                - `required string ToolName`

                - `JsonElement Type "tool_reference"constant`

                - `BetaCacheControlEphemeral? CacheControl`

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

          - `BetaCacheControlEphemeral? CacheControl`

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

        - `class BetaMcpToolUseBlockParam:`

          - `required string ID`

          - `required IReadOnlyDictionary<string, JsonElement> Input`

          - `required string Name`

          - `required string ServerName`

            The name of the MCP server

          - `JsonElement Type "mcp_tool_use"constant`

          - `BetaCacheControlEphemeral? CacheControl`

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

        - `class BetaRequestMcpToolResultBlockParam:`

          - `required string ToolUseID`

          - `JsonElement Type "mcp_tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

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

            - `IReadOnlyList<BetaTextBlockParam>`

              - `required string Text`

              - `JsonElement Type "text"constant`

              - `BetaCacheControlEphemeral? CacheControl`

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

              - `IReadOnlyList<BetaTextCitationParam>? Citations`

                - `class BetaCitationCharLocationParam:`

                  - `required string CitedText`

                  - `required Long DocumentIndex`

                  - `required string? DocumentTitle`

                  - `required Long EndCharIndex`

                  - `required Long StartCharIndex`

                  - `JsonElement Type "char_location"constant`

                - `class BetaCitationPageLocationParam:`

                  - `required string CitedText`

                  - `required Long DocumentIndex`

                  - `required string? DocumentTitle`

                  - `required Long EndPageNumber`

                  - `required Long StartPageNumber`

                  - `JsonElement Type "page_location"constant`

                - `class BetaCitationContentBlockLocationParam:`

                  - `required string CitedText`

                  - `required Long DocumentIndex`

                  - `required string? DocumentTitle`

                  - `required Long EndBlockIndex`

                  - `required Long StartBlockIndex`

                  - `JsonElement Type "content_block_location"constant`

                - `class BetaCitationWebSearchResultLocationParam:`

                  - `required string CitedText`

                  - `required string EncryptedIndex`

                  - `required string? Title`

                  - `JsonElement Type "web_search_result_location"constant`

                  - `required string Url`

                - `class BetaCitationSearchResultLocationParam:`

                  - `required string CitedText`

                  - `required Long EndBlockIndex`

                  - `required Long SearchResultIndex`

                  - `required string Source`

                  - `required Long StartBlockIndex`

                  - `required string? Title`

                  - `JsonElement Type "search_result_location"constant`

          - `Boolean IsError`

        - `class BetaContainerUploadBlockParam:`

          A content block that represents a file to be uploaded to the container
          Files uploaded via this block will be available in the container's input directory.

          - `required string FileID`

          - `JsonElement Type "container_upload"constant`

          - `BetaCacheControlEphemeral? CacheControl`

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

        - `class BetaCompactionBlockParam:`

          A compaction block containing summary of previous context.

          Users should round-trip these blocks from responses to subsequent requests
          to maintain context across compaction boundaries.

          When content is None, the block represents a failed compaction. The server
          treats these as no-ops. Empty string content is not allowed.

          - `required string? Content`

            Summary of previously compacted content, or null if compaction failed

          - `JsonElement Type "compaction"constant`

          - `BetaCacheControlEphemeral? CacheControl`

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

  - `required Model model`

    Body param: The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `BetaCacheControlEphemeral? cacheControl`

    Body param: Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

  - `Container? container`

    Body param: Container identifier for reuse across requests.

    - `class BetaContainerParams:`

      Container parameters with skills to be loaded.

      - `string? ID`

        Container id

      - `IReadOnlyList<BetaSkillParams>? Skills`

        List of skills to load in the container

        - `required string SkillID`

          Skill ID

        - `required Type Type`

          Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

          - `"anthropic"Anthropic`

          - `"custom"Custom`

        - `string Version`

          Skill version or 'latest' for most recent version

    - `string`

  - `BetaContextManagementConfig? contextManagement`

    Body param: Context management configuration.

    This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

  - `string? inferenceGeo`

    Body param: Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

  - `IReadOnlyList<BetaRequestMcpServerUrlDefinition> mcpServers`

    Body param: MCP servers to be utilized in this request

    - `required string Name`

    - `JsonElement Type "url"constant`

    - `required string Url`

    - `string? AuthorizationToken`

    - `BetaRequestMcpServerToolConfiguration? ToolConfiguration`

      - `IReadOnlyList<string>? AllowedTools`

      - `Boolean? Enabled`

  - `BetaMetadata metadata`

    Body param: An object describing metadata about the request.

  - `BetaOutputConfig outputConfig`

    Body param: Configuration options for the model's output, such as the output format.

  - `BetaJsonOutputFormat? outputFormat`

    Body param: Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

    A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

  - `ServiceTier serviceTier`

    Body param: Determines whether to use priority capacity (if available) or standard capacity for this request.

    Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

    - `"auto"Auto`

    - `"standard_only"StandardOnly`

  - `Speed? speed`

    Body param: The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

    - `"standard"Standard`

    - `"fast"Fast`

  - `IReadOnlyList<string> stopSequences`

    Body param: Custom text sequences that will cause the model to stop generating.

    Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

    If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

  - `System system`

    Body param: System prompt.

    A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

    - `string`

    - `IReadOnlyList<BetaTextBlockParam>`

      - `required string Text`

      - `JsonElement Type "text"constant`

      - `BetaCacheControlEphemeral? CacheControl`

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

      - `IReadOnlyList<BetaTextCitationParam>? Citations`

        - `class BetaCitationCharLocationParam:`

          - `required string CitedText`

          - `required Long DocumentIndex`

          - `required string? DocumentTitle`

          - `required Long EndCharIndex`

          - `required Long StartCharIndex`

          - `JsonElement Type "char_location"constant`

        - `class BetaCitationPageLocationParam:`

          - `required string CitedText`

          - `required Long DocumentIndex`

          - `required string? DocumentTitle`

          - `required Long EndPageNumber`

          - `required Long StartPageNumber`

          - `JsonElement Type "page_location"constant`

        - `class BetaCitationContentBlockLocationParam:`

          - `required string CitedText`

          - `required Long DocumentIndex`

          - `required string? DocumentTitle`

          - `required Long EndBlockIndex`

          - `required Long StartBlockIndex`

          - `JsonElement Type "content_block_location"constant`

        - `class BetaCitationWebSearchResultLocationParam:`

          - `required string CitedText`

          - `required string EncryptedIndex`

          - `required string? Title`

          - `JsonElement Type "web_search_result_location"constant`

          - `required string Url`

        - `class BetaCitationSearchResultLocationParam:`

          - `required string CitedText`

          - `required Long EndBlockIndex`

          - `required Long SearchResultIndex`

          - `required string Source`

          - `required Long StartBlockIndex`

          - `required string? Title`

          - `JsonElement Type "search_result_location"constant`

  - `Double temperature`

    Body param: Amount of randomness injected into the response.

    Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

    Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

  - `BetaThinkingConfigParam thinking`

    Body param: Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

    See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

  - `BetaToolChoice toolChoice`

    Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `IReadOnlyList<BetaToolUnion> tools`

    Body param: Definitions of tools that the model may use.

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

    - `class BetaTool:`

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

      - `BetaCacheControlEphemeral? CacheControl`

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

    - `class BetaToolBash20241022:`

      - `JsonElement Name "bash"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "bash_20241022"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

      - `BetaCacheControlEphemeral? CacheControl`

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

    - `class BetaToolBash20250124:`

      - `JsonElement Name "bash"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "bash_20250124"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

      - `BetaCacheControlEphemeral? CacheControl`

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

    - `class BetaCodeExecutionTool20250522:`

      - `JsonElement Name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "code_execution_20250522"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

      - `BetaCacheControlEphemeral? CacheControl`

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

    - `class BetaCodeExecutionTool20250825:`

      - `JsonElement Name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "code_execution_20250825"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

      - `BetaCacheControlEphemeral? CacheControl`

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

    - `class BetaCodeExecutionTool20260120:`

      Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

      - `JsonElement Name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "code_execution_20260120"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

      - `BetaCacheControlEphemeral? CacheControl`

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

    - `class BetaToolComputerUse20241022:`

      - `required Long DisplayHeightPx`

        The height of the display in pixels.

      - `required Long DisplayWidthPx`

        The width of the display in pixels.

      - `JsonElement Name "computer"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "computer_20241022"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

      - `BetaCacheControlEphemeral? CacheControl`

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

      - `Long? DisplayNumber`

        The X11 display number (e.g. 0, 1) for the display.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaMemoryTool20250818:`

      - `JsonElement Name "memory"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "memory_20250818"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

      - `BetaCacheControlEphemeral? CacheControl`

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

    - `class BetaToolComputerUse20250124:`

      - `required Long DisplayHeightPx`

        The height of the display in pixels.

      - `required Long DisplayWidthPx`

        The width of the display in pixels.

      - `JsonElement Name "computer"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "computer_20250124"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

      - `BetaCacheControlEphemeral? CacheControl`

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

      - `Long? DisplayNumber`

        The X11 display number (e.g. 0, 1) for the display.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolTextEditor20241022:`

      - `JsonElement Name "str_replace_editor"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "text_editor_20241022"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

      - `BetaCacheControlEphemeral? CacheControl`

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

    - `class BetaToolComputerUse20251124:`

      - `required Long DisplayHeightPx`

        The height of the display in pixels.

      - `required Long DisplayWidthPx`

        The width of the display in pixels.

      - `JsonElement Name "computer"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "computer_20251124"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

      - `BetaCacheControlEphemeral? CacheControl`

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

      - `Long? DisplayNumber`

        The X11 display number (e.g. 0, 1) for the display.

      - `Boolean EnableZoom`

        Whether to enable an action to take a zoomed-in screenshot of the screen.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolTextEditor20250124:`

      - `JsonElement Name "str_replace_editor"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "text_editor_20250124"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

      - `BetaCacheControlEphemeral? CacheControl`

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

    - `class BetaToolTextEditor20250429:`

      - `JsonElement Name "str_replace_based_edit_tool"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "text_editor_20250429"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

      - `BetaCacheControlEphemeral? CacheControl`

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

    - `class BetaToolTextEditor20250728:`

      - `JsonElement Name "str_replace_based_edit_tool"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "text_editor_20250728"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

      - `BetaCacheControlEphemeral? CacheControl`

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

    - `class BetaWebSearchTool20250305:`

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

      - `BetaCacheControlEphemeral? CacheControl`

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

      - `BetaUserLocation? UserLocation`

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

    - `class BetaWebFetchTool20250910:`

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

      - `BetaCacheControlEphemeral? CacheControl`

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

      - `BetaCitationsConfigParam? Citations`

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

    - `class BetaWebSearchTool20260209:`

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

      - `BetaCacheControlEphemeral? CacheControl`

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

      - `BetaUserLocation? UserLocation`

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

    - `class BetaWebFetchTool20260209:`

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

      - `BetaCacheControlEphemeral? CacheControl`

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

      - `BetaCitationsConfigParam? Citations`

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

    - `class BetaToolSearchToolBm25_20251119:`

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

      - `BetaCacheControlEphemeral? CacheControl`

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

    - `class BetaToolSearchToolRegex20251119:`

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

      - `BetaCacheControlEphemeral? CacheControl`

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

    - `class BetaMcpToolset:`

      Configuration for a group of tools from an MCP server.

      Allows configuring enabled status and defer_loading for all tools
      from an MCP server, with optional per-tool overrides.

      - `required string McpServerName`

        Name of the MCP server to configure tools for

      - `JsonElement Type "mcp_toolset"constant`

      - `BetaCacheControlEphemeral? CacheControl`

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

      - `IReadOnlyDictionary<string, BetaMcpToolConfig>? Configs`

        Configuration overrides for specific tools, keyed by tool name

        - `Boolean DeferLoading`

        - `Boolean Enabled`

      - `BetaMcpToolDefaultConfig DefaultConfig`

        Default configuration applied to all tools from this server

        - `Boolean DeferLoading`

        - `Boolean Enabled`

  - `Long topK`

    Body param: Only sample from the top K options for each subsequent token.

    Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

    Recommended for advanced use cases only. You usually only need to use `temperature`.

  - `Double topP`

    Body param: Use nucleus sampling.

    In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

    Recommended for advanced use cases only. You usually only need to use `temperature`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

### Returns

- `class BetaMessage:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required BetaContainer? Container`

    Information about the container used in the request (for the code execution tool)

    - `required string ID`

      Identifier for the container used in this request

    - `required DateTimeOffset ExpiresAt`

      The time at which the container will expire.

    - `required IReadOnlyList<BetaSkill>? Skills`

      Skills loaded in the container

      - `required string SkillID`

        Skill ID

      - `required Type Type`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `"anthropic"Anthropic`

        - `"custom"Custom`

      - `required string Version`

        Skill version or 'latest' for most recent version

  - `required IReadOnlyList<BetaContentBlock> Content`

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

    - `class BetaTextBlock:`

      - `required IReadOnlyList<BetaTextCitation>? Citations`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class BetaCitationCharLocation:`

          - `required string CitedText`

          - `required Long DocumentIndex`

          - `required string? DocumentTitle`

          - `required Long EndCharIndex`

          - `required string? FileID`

          - `required Long StartCharIndex`

          - `JsonElement Type "char_location"constant`

        - `class BetaCitationPageLocation:`

          - `required string CitedText`

          - `required Long DocumentIndex`

          - `required string? DocumentTitle`

          - `required Long EndPageNumber`

          - `required string? FileID`

          - `required Long StartPageNumber`

          - `JsonElement Type "page_location"constant`

        - `class BetaCitationContentBlockLocation:`

          - `required string CitedText`

          - `required Long DocumentIndex`

          - `required string? DocumentTitle`

          - `required Long EndBlockIndex`

          - `required string? FileID`

          - `required Long StartBlockIndex`

          - `JsonElement Type "content_block_location"constant`

        - `class BetaCitationsWebSearchResultLocation:`

          - `required string CitedText`

          - `required string EncryptedIndex`

          - `required string? Title`

          - `JsonElement Type "web_search_result_location"constant`

          - `required string Url`

        - `class BetaCitationSearchResultLocation:`

          - `required string CitedText`

          - `required Long EndBlockIndex`

          - `required Long SearchResultIndex`

          - `required string Source`

          - `required Long StartBlockIndex`

          - `required string? Title`

          - `JsonElement Type "search_result_location"constant`

      - `required string Text`

      - `JsonElement Type "text"constant`

    - `class BetaThinkingBlock:`

      - `required string Signature`

      - `required string Thinking`

      - `JsonElement Type "thinking"constant`

    - `class BetaRedactedThinkingBlock:`

      - `required string Data`

      - `JsonElement Type "redacted_thinking"constant`

    - `class BetaToolUseBlock:`

      - `required string ID`

      - `required IReadOnlyDictionary<string, JsonElement> Input`

      - `required string Name`

      - `JsonElement Type "tool_use"constant`

      - `Caller Caller`

        Tool invocation directly from the model.

        - `class BetaDirectCaller:`

          Tool invocation directly from the model.

          - `JsonElement Type "direct"constant`

        - `class BetaServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `required string ToolID`

          - `JsonElement Type "code_execution_20250825"constant`

        - `class BetaServerToolCaller20260120:`

          - `required string ToolID`

          - `JsonElement Type "code_execution_20260120"constant`

    - `class BetaServerToolUseBlock:`

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

      - `Caller Caller`

        Tool invocation directly from the model.

        - `class BetaDirectCaller:`

          Tool invocation directly from the model.

          - `JsonElement Type "direct"constant`

        - `class BetaServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `required string ToolID`

          - `JsonElement Type "code_execution_20250825"constant`

        - `class BetaServerToolCaller20260120:`

          - `required string ToolID`

          - `JsonElement Type "code_execution_20260120"constant`

    - `class BetaWebSearchToolResultBlock:`

      - `required BetaWebSearchToolResultBlockContent Content`

        - `class BetaWebSearchToolResultError:`

          - `required BetaWebSearchToolResultErrorCode ErrorCode`

            - `"invalid_tool_input"InvalidToolInput`

            - `"unavailable"Unavailable`

            - `"max_uses_exceeded"MaxUsesExceeded`

            - `"too_many_requests"TooManyRequests`

            - `"query_too_long"QueryTooLong`

            - `"request_too_large"RequestTooLarge`

          - `JsonElement Type "web_search_tool_result_error"constant`

        - `IReadOnlyList<BetaWebSearchResultBlock>`

          - `required string EncryptedContent`

          - `required string? PageAge`

          - `required string Title`

          - `JsonElement Type "web_search_result"constant`

          - `required string Url`

      - `required string ToolUseID`

      - `JsonElement Type "web_search_tool_result"constant`

      - `Caller Caller`

        Tool invocation directly from the model.

        - `class BetaDirectCaller:`

          Tool invocation directly from the model.

          - `JsonElement Type "direct"constant`

        - `class BetaServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `required string ToolID`

          - `JsonElement Type "code_execution_20250825"constant`

        - `class BetaServerToolCaller20260120:`

          - `required string ToolID`

          - `JsonElement Type "code_execution_20260120"constant`

    - `class BetaWebFetchToolResultBlock:`

      - `required Content Content`

        - `class BetaWebFetchToolResultErrorBlock:`

          - `required BetaWebFetchToolResultErrorCode ErrorCode`

            - `"invalid_tool_input"InvalidToolInput`

            - `"url_too_long"UrlTooLong`

            - `"url_not_allowed"UrlNotAllowed`

            - `"url_not_accessible"UrlNotAccessible`

            - `"unsupported_content_type"UnsupportedContentType`

            - `"too_many_requests"TooManyRequests`

            - `"max_uses_exceeded"MaxUsesExceeded`

            - `"unavailable"Unavailable`

          - `JsonElement Type "web_fetch_tool_result_error"constant`

        - `class BetaWebFetchBlock:`

          - `required BetaDocumentBlock Content`

            - `required BetaCitationConfig? Citations`

              Citation configuration for the document

              - `required Boolean Enabled`

            - `required Source Source`

              - `class BetaBase64PdfSource:`

                - `required string Data`

                - `JsonElement MediaType "application/pdf"constant`

                - `JsonElement Type "base64"constant`

              - `class BetaPlainTextSource:`

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

      - `Caller Caller`

        Tool invocation directly from the model.

        - `class BetaDirectCaller:`

          Tool invocation directly from the model.

          - `JsonElement Type "direct"constant`

        - `class BetaServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `required string ToolID`

          - `JsonElement Type "code_execution_20250825"constant`

        - `class BetaServerToolCaller20260120:`

          - `required string ToolID`

          - `JsonElement Type "code_execution_20260120"constant`

    - `class BetaCodeExecutionToolResultBlock:`

      - `required BetaCodeExecutionToolResultBlockContent Content`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class BetaCodeExecutionToolResultError:`

          - `required BetaCodeExecutionToolResultErrorCode ErrorCode`

            - `"invalid_tool_input"InvalidToolInput`

            - `"unavailable"Unavailable`

            - `"too_many_requests"TooManyRequests`

            - `"execution_time_exceeded"ExecutionTimeExceeded`

          - `JsonElement Type "code_execution_tool_result_error"constant`

        - `class BetaCodeExecutionResultBlock:`

          - `required IReadOnlyList<BetaCodeExecutionOutputBlock> Content`

            - `required string FileID`

            - `JsonElement Type "code_execution_output"constant`

          - `required Long ReturnCode`

          - `required string Stderr`

          - `required string Stdout`

          - `JsonElement Type "code_execution_result"constant`

        - `class BetaEncryptedCodeExecutionResultBlock:`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `required IReadOnlyList<BetaCodeExecutionOutputBlock> Content`

            - `required string FileID`

            - `JsonElement Type "code_execution_output"constant`

          - `required string EncryptedStdout`

          - `required Long ReturnCode`

          - `required string Stderr`

          - `JsonElement Type "encrypted_code_execution_result"constant`

      - `required string ToolUseID`

      - `JsonElement Type "code_execution_tool_result"constant`

    - `class BetaBashCodeExecutionToolResultBlock:`

      - `required Content Content`

        - `class BetaBashCodeExecutionToolResultError:`

          - `required ErrorCode ErrorCode`

            - `"invalid_tool_input"InvalidToolInput`

            - `"unavailable"Unavailable`

            - `"too_many_requests"TooManyRequests`

            - `"execution_time_exceeded"ExecutionTimeExceeded`

            - `"output_file_too_large"OutputFileTooLarge`

          - `JsonElement Type "bash_code_execution_tool_result_error"constant`

        - `class BetaBashCodeExecutionResultBlock:`

          - `required IReadOnlyList<BetaBashCodeExecutionOutputBlock> Content`

            - `required string FileID`

            - `JsonElement Type "bash_code_execution_output"constant`

          - `required Long ReturnCode`

          - `required string Stderr`

          - `required string Stdout`

          - `JsonElement Type "bash_code_execution_result"constant`

      - `required string ToolUseID`

      - `JsonElement Type "bash_code_execution_tool_result"constant`

    - `class BetaTextEditorCodeExecutionToolResultBlock:`

      - `required Content Content`

        - `class BetaTextEditorCodeExecutionToolResultError:`

          - `required ErrorCode ErrorCode`

            - `"invalid_tool_input"InvalidToolInput`

            - `"unavailable"Unavailable`

            - `"too_many_requests"TooManyRequests`

            - `"execution_time_exceeded"ExecutionTimeExceeded`

            - `"file_not_found"FileNotFound`

          - `required string? ErrorMessage`

          - `JsonElement Type "text_editor_code_execution_tool_result_error"constant`

        - `class BetaTextEditorCodeExecutionViewResultBlock:`

          - `required string Content`

          - `required FileType FileType`

            - `"text"Text`

            - `"image"Image`

            - `"pdf"Pdf`

          - `required Long? NumLines`

          - `required Long? StartLine`

          - `required Long? TotalLines`

          - `JsonElement Type "text_editor_code_execution_view_result"constant`

        - `class BetaTextEditorCodeExecutionCreateResultBlock:`

          - `required Boolean IsFileUpdate`

          - `JsonElement Type "text_editor_code_execution_create_result"constant`

        - `class BetaTextEditorCodeExecutionStrReplaceResultBlock:`

          - `required IReadOnlyList<string>? Lines`

          - `required Long? NewLines`

          - `required Long? NewStart`

          - `required Long? OldLines`

          - `required Long? OldStart`

          - `JsonElement Type "text_editor_code_execution_str_replace_result"constant`

      - `required string ToolUseID`

      - `JsonElement Type "text_editor_code_execution_tool_result"constant`

    - `class BetaToolSearchToolResultBlock:`

      - `required Content Content`

        - `class BetaToolSearchToolResultError:`

          - `required ErrorCode ErrorCode`

            - `"invalid_tool_input"InvalidToolInput`

            - `"unavailable"Unavailable`

            - `"too_many_requests"TooManyRequests`

            - `"execution_time_exceeded"ExecutionTimeExceeded`

          - `required string? ErrorMessage`

          - `JsonElement Type "tool_search_tool_result_error"constant`

        - `class BetaToolSearchToolSearchResultBlock:`

          - `required IReadOnlyList<BetaToolReferenceBlock> ToolReferences`

            - `required string ToolName`

            - `JsonElement Type "tool_reference"constant`

          - `JsonElement Type "tool_search_tool_search_result"constant`

      - `required string ToolUseID`

      - `JsonElement Type "tool_search_tool_result"constant`

    - `class BetaMcpToolUseBlock:`

      - `required string ID`

      - `required IReadOnlyDictionary<string, JsonElement> Input`

      - `required string Name`

        The name of the MCP tool

      - `required string ServerName`

        The name of the MCP server

      - `JsonElement Type "mcp_tool_use"constant`

    - `class BetaMcpToolResultBlock:`

      - `required Content Content`

        - `string`

        - `IReadOnlyList<BetaTextBlock>`

          - `required IReadOnlyList<BetaTextCitation>? Citations`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `class BetaCitationCharLocation:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndCharIndex`

              - `required string? FileID`

              - `required Long StartCharIndex`

              - `JsonElement Type "char_location"constant`

            - `class BetaCitationPageLocation:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndPageNumber`

              - `required string? FileID`

              - `required Long StartPageNumber`

              - `JsonElement Type "page_location"constant`

            - `class BetaCitationContentBlockLocation:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndBlockIndex`

              - `required string? FileID`

              - `required Long StartBlockIndex`

              - `JsonElement Type "content_block_location"constant`

            - `class BetaCitationsWebSearchResultLocation:`

              - `required string CitedText`

              - `required string EncryptedIndex`

              - `required string? Title`

              - `JsonElement Type "web_search_result_location"constant`

              - `required string Url`

            - `class BetaCitationSearchResultLocation:`

              - `required string CitedText`

              - `required Long EndBlockIndex`

              - `required Long SearchResultIndex`

              - `required string Source`

              - `required Long StartBlockIndex`

              - `required string? Title`

              - `JsonElement Type "search_result_location"constant`

          - `required string Text`

          - `JsonElement Type "text"constant`

      - `required Boolean IsError`

      - `required string ToolUseID`

      - `JsonElement Type "mcp_tool_result"constant`

    - `class BetaContainerUploadBlock:`

      Response model for a file uploaded to the container.

      - `required string FileID`

      - `JsonElement Type "container_upload"constant`

    - `class BetaCompactionBlock:`

      A compaction block returned when autocompact is triggered.

      When content is None, it indicates the compaction failed to produce a valid
      summary (e.g., malformed output from the model). Clients may round-trip
      compaction blocks with null content; the server treats them as no-ops.

      - `required string? Content`

        Summary of compacted content, or null if compaction failed

      - `JsonElement Type "compaction"constant`

  - `required BetaContextManagementResponse? ContextManagement`

    Context management response.

    Information about context management strategies applied during the request.

    - `required IReadOnlyList<AppliedEdit> AppliedEdits`

      List of context management edits that were applied.

      - `class BetaClearToolUses20250919EditResponse:`

        - `required Long ClearedInputTokens`

          Number of input tokens cleared by this edit.

        - `required Long ClearedToolUses`

          Number of tool uses that were cleared.

        - `JsonElement Type "clear_tool_uses_20250919"constant`

          The type of context management edit applied.

      - `class BetaClearThinking20251015EditResponse:`

        - `required Long ClearedInputTokens`

          Number of input tokens cleared by this edit.

        - `required Long ClearedThinkingTurns`

          Number of thinking turns that were cleared.

        - `JsonElement Type "clear_thinking_20251015"constant`

          The type of context management edit applied.

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

  - `required BetaStopReason? StopReason`

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

    - `"compaction"Compaction`

    - `"refusal"Refusal`

    - `"model_context_window_exceeded"ModelContextWindowExceeded`

  - `required string? StopSequence`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `JsonElement Type "message"constant`

    Object type.

    For Messages, this is always `"message"`.

  - `required BetaUsage Usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `required BetaCacheCreation? CacheCreation`

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

    - `required IReadOnlyList<BetaIterationsUsageItems>? Iterations`

      Per-iteration token usage breakdown.

      Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

      - Determine which iterations exceeded long context thresholds (>=200k tokens)
      - Calculate the true context window size from the last iteration
      - Understand token accumulation across server-side tool use loops

      - `class BetaMessageIterationUsage:`

        Token usage for a sampling iteration.

        - `required BetaCacheCreation? CacheCreation`

          Breakdown of cached tokens by TTL

          - `required Long Ephemeral1hInputTokens`

            The number of input tokens used to create the 1 hour cache entry.

          - `required Long Ephemeral5mInputTokens`

            The number of input tokens used to create the 5 minute cache entry.

        - `required Long CacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

        - `required Long CacheReadInputTokens`

          The number of input tokens read from the cache.

        - `required Long InputTokens`

          The number of input tokens which were used.

        - `required Long OutputTokens`

          The number of output tokens which were used.

        - `JsonElement Type "message"constant`

          Usage for a sampling iteration

      - `class BetaCompactionIterationUsage:`

        Token usage for a compaction iteration.

        - `required BetaCacheCreation? CacheCreation`

          Breakdown of cached tokens by TTL

          - `required Long Ephemeral1hInputTokens`

            The number of input tokens used to create the 1 hour cache entry.

          - `required Long Ephemeral5mInputTokens`

            The number of input tokens used to create the 5 minute cache entry.

        - `required Long CacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

        - `required Long CacheReadInputTokens`

          The number of input tokens read from the cache.

        - `required Long InputTokens`

          The number of input tokens which were used.

        - `required Long OutputTokens`

          The number of output tokens which were used.

        - `JsonElement Type "compaction"constant`

          Usage for a compaction iteration

    - `required Long OutputTokens`

      The number of output tokens which were used.

    - `required BetaServerToolUsage? ServerToolUse`

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

    - `required Speed? Speed`

      The inference speed mode used for this request.

      - `"standard"Standard`

      - `"fast"Fast`

### Example

```csharp
MessageCreateParams parameters = new()
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
};

var betaMessage = await client.Beta.Messages.Create(parameters);

Console.WriteLine(betaMessage);
```

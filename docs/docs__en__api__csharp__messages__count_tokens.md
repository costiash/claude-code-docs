## Count Tokens

`MessageTokensCount Messages.CountTokens(MessageCountTokensParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

### Parameters

- `MessageCountTokensParams parameters`

  - `required IReadOnlyList<MessageParam> messages`

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

  - `required Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `CacheControlEphemeral? cacheControl`

    Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

  - `OutputConfig outputConfig`

    Configuration options for the model's output, such as the output format.

  - `System system`

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

  - `ThinkingConfigParam thinking`

    Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

    See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

  - `ToolChoice toolChoice`

    How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `IReadOnlyList<MessageCountTokensTool> tools`

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

### Returns

- `class MessageTokensCount:`

  - `required Long InputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Example

```csharp
MessageCountTokensParams parameters = new()
{
    Messages =
    [
        new()
        {
            Content = "string",
            Role = Role.User,
        },
    ],
    Model = Model.ClaudeOpus4_6,
};

var messageTokensCount = await client.Messages.CountTokens(parameters);

Console.WriteLine(messageTokensCount);
```

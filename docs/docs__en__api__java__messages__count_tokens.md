## Count Tokens

`MessageTokensCount messages().countTokens(MessageCountTokensParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

### Parameters

- `MessageCountTokensParams params`

  - `List<MessageParam> messages`

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

    - `Content content`

      - `String`

      - `List<ContentBlockParam>`

        - `class TextBlockParam:`

          - `String text`

          - `JsonValue; type "text"constant`

            - `TEXT("text")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<List<TextCitationParam>> citations`

            - `class CitationCharLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endCharIndex`

              - `long startCharIndex`

              - `JsonValue; type "char_location"constant`

                - `CHAR_LOCATION("char_location")`

            - `class CitationPageLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endPageNumber`

              - `long startPageNumber`

              - `JsonValue; type "page_location"constant`

                - `PAGE_LOCATION("page_location")`

            - `class CitationContentBlockLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endBlockIndex`

              - `long startBlockIndex`

              - `JsonValue; type "content_block_location"constant`

                - `CONTENT_BLOCK_LOCATION("content_block_location")`

            - `class CitationWebSearchResultLocationParam:`

              - `String citedText`

              - `String encryptedIndex`

              - `Optional<String> title`

              - `JsonValue; type "web_search_result_location"constant`

                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

              - `String url`

            - `class CitationSearchResultLocationParam:`

              - `String citedText`

              - `long endBlockIndex`

              - `long searchResultIndex`

              - `String source`

              - `long startBlockIndex`

              - `Optional<String> title`

              - `JsonValue; type "search_result_location"constant`

                - `SEARCH_RESULT_LOCATION("search_result_location")`

        - `class ImageBlockParam:`

          - `Source source`

            - `class Base64ImageSource:`

              - `String data`

              - `MediaType mediaType`

                - `IMAGE_JPEG("image/jpeg")`

                - `IMAGE_PNG("image/png")`

                - `IMAGE_GIF("image/gif")`

                - `IMAGE_WEBP("image/webp")`

              - `JsonValue; type "base64"constant`

                - `BASE64("base64")`

            - `class UrlImageSource:`

              - `JsonValue; type "url"constant`

                - `URL("url")`

              - `String url`

          - `JsonValue; type "image"constant`

            - `IMAGE("image")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class DocumentBlockParam:`

          - `Source source`

            - `class Base64PdfSource:`

              - `String data`

              - `JsonValue; mediaType "application/pdf"constant`

                - `APPLICATION_PDF("application/pdf")`

              - `JsonValue; type "base64"constant`

                - `BASE64("base64")`

            - `class PlainTextSource:`

              - `String data`

              - `JsonValue; mediaType "text/plain"constant`

                - `TEXT_PLAIN("text/plain")`

              - `JsonValue; type "text"constant`

                - `TEXT("text")`

            - `class ContentBlockSource:`

              - `Content content`

                - `String`

                - `List<ContentBlockSourceContent>`

                  - `class TextBlockParam:`

                    - `String text`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

                    - `Optional<List<TextCitationParam>> citations`

                      - `class CitationCharLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endCharIndex`

                        - `long startCharIndex`

                        - `JsonValue; type "char_location"constant`

                          - `CHAR_LOCATION("char_location")`

                      - `class CitationPageLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endPageNumber`

                        - `long startPageNumber`

                        - `JsonValue; type "page_location"constant`

                          - `PAGE_LOCATION("page_location")`

                      - `class CitationContentBlockLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endBlockIndex`

                        - `long startBlockIndex`

                        - `JsonValue; type "content_block_location"constant`

                          - `CONTENT_BLOCK_LOCATION("content_block_location")`

                      - `class CitationWebSearchResultLocationParam:`

                        - `String citedText`

                        - `String encryptedIndex`

                        - `Optional<String> title`

                        - `JsonValue; type "web_search_result_location"constant`

                          - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                        - `String url`

                      - `class CitationSearchResultLocationParam:`

                        - `String citedText`

                        - `long endBlockIndex`

                        - `long searchResultIndex`

                        - `String source`

                        - `long startBlockIndex`

                        - `Optional<String> title`

                        - `JsonValue; type "search_result_location"constant`

                          - `SEARCH_RESULT_LOCATION("search_result_location")`

                  - `class ImageBlockParam:`

                    - `Source source`

                      - `class Base64ImageSource:`

                        - `String data`

                        - `MediaType mediaType`

                          - `IMAGE_JPEG("image/jpeg")`

                          - `IMAGE_PNG("image/png")`

                          - `IMAGE_GIF("image/gif")`

                          - `IMAGE_WEBP("image/webp")`

                        - `JsonValue; type "base64"constant`

                          - `BASE64("base64")`

                      - `class UrlImageSource:`

                        - `JsonValue; type "url"constant`

                          - `URL("url")`

                        - `String url`

                    - `JsonValue; type "image"constant`

                      - `IMAGE("image")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

              - `JsonValue; type "content"constant`

                - `CONTENT("content")`

            - `class UrlPdfSource:`

              - `JsonValue; type "url"constant`

                - `URL("url")`

              - `String url`

          - `JsonValue; type "document"constant`

            - `DOCUMENT("document")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<CitationsConfigParam> citations`

            - `Optional<Boolean> enabled`

          - `Optional<String> context`

          - `Optional<String> title`

        - `class SearchResultBlockParam:`

          - `List<TextBlockParam> content`

            - `String text`

            - `JsonValue; type "text"constant`

              - `TEXT("text")`

            - `Optional<CacheControlEphemeral> cacheControl`

              Create a cache control breakpoint at this content block.

              - `JsonValue; type "ephemeral"constant`

                - `EPHEMERAL("ephemeral")`

              - `Optional<Ttl> ttl`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `TTL_5M("5m")`

                - `TTL_1H("1h")`

            - `Optional<List<TextCitationParam>> citations`

              - `class CitationCharLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endCharIndex`

                - `long startCharIndex`

                - `JsonValue; type "char_location"constant`

                  - `CHAR_LOCATION("char_location")`

              - `class CitationPageLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endPageNumber`

                - `long startPageNumber`

                - `JsonValue; type "page_location"constant`

                  - `PAGE_LOCATION("page_location")`

              - `class CitationContentBlockLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endBlockIndex`

                - `long startBlockIndex`

                - `JsonValue; type "content_block_location"constant`

                  - `CONTENT_BLOCK_LOCATION("content_block_location")`

              - `class CitationWebSearchResultLocationParam:`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                - `JsonValue; type "web_search_result_location"constant`

                  - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                - `String url`

              - `class CitationSearchResultLocationParam:`

                - `String citedText`

                - `long endBlockIndex`

                - `long searchResultIndex`

                - `String source`

                - `long startBlockIndex`

                - `Optional<String> title`

                - `JsonValue; type "search_result_location"constant`

                  - `SEARCH_RESULT_LOCATION("search_result_location")`

          - `String source`

          - `String title`

          - `JsonValue; type "search_result"constant`

            - `SEARCH_RESULT("search_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<CitationsConfigParam> citations`

            - `Optional<Boolean> enabled`

        - `class ThinkingBlockParam:`

          - `String signature`

          - `String thinking`

          - `JsonValue; type "thinking"constant`

            - `THINKING("thinking")`

        - `class RedactedThinkingBlockParam:`

          - `String data`

          - `JsonValue; type "redacted_thinking"constant`

            - `REDACTED_THINKING("redacted_thinking")`

        - `class ToolUseBlockParam:`

          - `String id`

          - `Input input`

          - `String name`

          - `JsonValue; type "tool_use"constant`

            - `TOOL_USE("tool_use")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `class ToolResultBlockParam:`

          - `String toolUseId`

          - `JsonValue; type "tool_result"constant`

            - `TOOL_RESULT("tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Content> content`

            - `String`

            - `List<Block>`

              - `class TextBlockParam:`

                - `String text`

                - `JsonValue; type "text"constant`

                  - `TEXT("text")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<List<TextCitationParam>> citations`

                  - `class CitationCharLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endCharIndex`

                    - `long startCharIndex`

                    - `JsonValue; type "char_location"constant`

                      - `CHAR_LOCATION("char_location")`

                  - `class CitationPageLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endPageNumber`

                    - `long startPageNumber`

                    - `JsonValue; type "page_location"constant`

                      - `PAGE_LOCATION("page_location")`

                  - `class CitationContentBlockLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endBlockIndex`

                    - `long startBlockIndex`

                    - `JsonValue; type "content_block_location"constant`

                      - `CONTENT_BLOCK_LOCATION("content_block_location")`

                  - `class CitationWebSearchResultLocationParam:`

                    - `String citedText`

                    - `String encryptedIndex`

                    - `Optional<String> title`

                    - `JsonValue; type "web_search_result_location"constant`

                      - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                    - `String url`

                  - `class CitationSearchResultLocationParam:`

                    - `String citedText`

                    - `long endBlockIndex`

                    - `long searchResultIndex`

                    - `String source`

                    - `long startBlockIndex`

                    - `Optional<String> title`

                    - `JsonValue; type "search_result_location"constant`

                      - `SEARCH_RESULT_LOCATION("search_result_location")`

              - `class ImageBlockParam:`

                - `Source source`

                  - `class Base64ImageSource:`

                    - `String data`

                    - `MediaType mediaType`

                      - `IMAGE_JPEG("image/jpeg")`

                      - `IMAGE_PNG("image/png")`

                      - `IMAGE_GIF("image/gif")`

                      - `IMAGE_WEBP("image/webp")`

                    - `JsonValue; type "base64"constant`

                      - `BASE64("base64")`

                  - `class UrlImageSource:`

                    - `JsonValue; type "url"constant`

                      - `URL("url")`

                    - `String url`

                - `JsonValue; type "image"constant`

                  - `IMAGE("image")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

              - `class SearchResultBlockParam:`

                - `List<TextBlockParam> content`

                  - `String text`

                  - `JsonValue; type "text"constant`

                    - `TEXT("text")`

                  - `Optional<CacheControlEphemeral> cacheControl`

                    Create a cache control breakpoint at this content block.

                    - `JsonValue; type "ephemeral"constant`

                      - `EPHEMERAL("ephemeral")`

                    - `Optional<Ttl> ttl`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `TTL_5M("5m")`

                      - `TTL_1H("1h")`

                  - `Optional<List<TextCitationParam>> citations`

                    - `class CitationCharLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endCharIndex`

                      - `long startCharIndex`

                      - `JsonValue; type "char_location"constant`

                        - `CHAR_LOCATION("char_location")`

                    - `class CitationPageLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endPageNumber`

                      - `long startPageNumber`

                      - `JsonValue; type "page_location"constant`

                        - `PAGE_LOCATION("page_location")`

                    - `class CitationContentBlockLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endBlockIndex`

                      - `long startBlockIndex`

                      - `JsonValue; type "content_block_location"constant`

                        - `CONTENT_BLOCK_LOCATION("content_block_location")`

                    - `class CitationWebSearchResultLocationParam:`

                      - `String citedText`

                      - `String encryptedIndex`

                      - `Optional<String> title`

                      - `JsonValue; type "web_search_result_location"constant`

                        - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                      - `String url`

                    - `class CitationSearchResultLocationParam:`

                      - `String citedText`

                      - `long endBlockIndex`

                      - `long searchResultIndex`

                      - `String source`

                      - `long startBlockIndex`

                      - `Optional<String> title`

                      - `JsonValue; type "search_result_location"constant`

                        - `SEARCH_RESULT_LOCATION("search_result_location")`

                - `String source`

                - `String title`

                - `JsonValue; type "search_result"constant`

                  - `SEARCH_RESULT("search_result")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<CitationsConfigParam> citations`

                  - `Optional<Boolean> enabled`

              - `class DocumentBlockParam:`

                - `Source source`

                  - `class Base64PdfSource:`

                    - `String data`

                    - `JsonValue; mediaType "application/pdf"constant`

                      - `APPLICATION_PDF("application/pdf")`

                    - `JsonValue; type "base64"constant`

                      - `BASE64("base64")`

                  - `class PlainTextSource:`

                    - `String data`

                    - `JsonValue; mediaType "text/plain"constant`

                      - `TEXT_PLAIN("text/plain")`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                  - `class ContentBlockSource:`

                    - `Content content`

                      - `String`

                      - `List<ContentBlockSourceContent>`

                        - `class TextBlockParam:`

                          - `String text`

                          - `JsonValue; type "text"constant`

                            - `TEXT("text")`

                          - `Optional<CacheControlEphemeral> cacheControl`

                            Create a cache control breakpoint at this content block.

                            - `JsonValue; type "ephemeral"constant`

                              - `EPHEMERAL("ephemeral")`

                            - `Optional<Ttl> ttl`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `TTL_5M("5m")`

                              - `TTL_1H("1h")`

                          - `Optional<List<TextCitationParam>> citations`

                            - `class CitationCharLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endCharIndex`

                              - `long startCharIndex`

                              - `JsonValue; type "char_location"constant`

                                - `CHAR_LOCATION("char_location")`

                            - `class CitationPageLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endPageNumber`

                              - `long startPageNumber`

                              - `JsonValue; type "page_location"constant`

                                - `PAGE_LOCATION("page_location")`

                            - `class CitationContentBlockLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endBlockIndex`

                              - `long startBlockIndex`

                              - `JsonValue; type "content_block_location"constant`

                                - `CONTENT_BLOCK_LOCATION("content_block_location")`

                            - `class CitationWebSearchResultLocationParam:`

                              - `String citedText`

                              - `String encryptedIndex`

                              - `Optional<String> title`

                              - `JsonValue; type "web_search_result_location"constant`

                                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                              - `String url`

                            - `class CitationSearchResultLocationParam:`

                              - `String citedText`

                              - `long endBlockIndex`

                              - `long searchResultIndex`

                              - `String source`

                              - `long startBlockIndex`

                              - `Optional<String> title`

                              - `JsonValue; type "search_result_location"constant`

                                - `SEARCH_RESULT_LOCATION("search_result_location")`

                        - `class ImageBlockParam:`

                          - `Source source`

                            - `class Base64ImageSource:`

                              - `String data`

                              - `MediaType mediaType`

                                - `IMAGE_JPEG("image/jpeg")`

                                - `IMAGE_PNG("image/png")`

                                - `IMAGE_GIF("image/gif")`

                                - `IMAGE_WEBP("image/webp")`

                              - `JsonValue; type "base64"constant`

                                - `BASE64("base64")`

                            - `class UrlImageSource:`

                              - `JsonValue; type "url"constant`

                                - `URL("url")`

                              - `String url`

                          - `JsonValue; type "image"constant`

                            - `IMAGE("image")`

                          - `Optional<CacheControlEphemeral> cacheControl`

                            Create a cache control breakpoint at this content block.

                            - `JsonValue; type "ephemeral"constant`

                              - `EPHEMERAL("ephemeral")`

                            - `Optional<Ttl> ttl`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `TTL_5M("5m")`

                              - `TTL_1H("1h")`

                    - `JsonValue; type "content"constant`

                      - `CONTENT("content")`

                  - `class UrlPdfSource:`

                    - `JsonValue; type "url"constant`

                      - `URL("url")`

                    - `String url`

                - `JsonValue; type "document"constant`

                  - `DOCUMENT("document")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<CitationsConfigParam> citations`

                  - `Optional<Boolean> enabled`

                - `Optional<String> context`

                - `Optional<String> title`

              - `class ToolReferenceBlockParam:`

                Tool reference block that can be included in tool_result content.

                - `String toolName`

                - `JsonValue; type "tool_reference"constant`

                  - `TOOL_REFERENCE("tool_reference")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

          - `Optional<Boolean> isError`

        - `class ServerToolUseBlockParam:`

          - `String id`

          - `Input input`

          - `Name name`

            - `WEB_SEARCH("web_search")`

            - `WEB_FETCH("web_fetch")`

            - `CODE_EXECUTION("code_execution")`

            - `BASH_CODE_EXECUTION("bash_code_execution")`

            - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

            - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

            - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `JsonValue; type "server_tool_use"constant`

            - `SERVER_TOOL_USE("server_tool_use")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `class WebSearchToolResultBlockParam:`

          - `WebSearchToolResultBlockParamContent content`

            - `List<WebSearchResultBlockParam>`

              - `String encryptedContent`

              - `String title`

              - `JsonValue; type "web_search_result"constant`

                - `WEB_SEARCH_RESULT("web_search_result")`

              - `String url`

              - `Optional<String> pageAge`

            - `class WebSearchToolRequestError:`

              - `WebSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `QUERY_TOO_LONG("query_too_long")`

                - `REQUEST_TOO_LARGE("request_too_large")`

              - `JsonValue; type "web_search_tool_result_error"constant`

                - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

          - `String toolUseId`

          - `JsonValue; type "web_search_tool_result"constant`

            - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `class WebFetchToolResultBlockParam:`

          - `Content content`

            - `class WebFetchToolResultErrorBlockParam:`

              - `WebFetchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `URL_TOO_LONG("url_too_long")`

                - `URL_NOT_ALLOWED("url_not_allowed")`

                - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `UNAVAILABLE("unavailable")`

              - `JsonValue; type "web_fetch_tool_result_error"constant`

                - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

            - `class WebFetchBlockParam:`

              - `DocumentBlockParam content`

                - `Source source`

                  - `class Base64PdfSource:`

                    - `String data`

                    - `JsonValue; mediaType "application/pdf"constant`

                      - `APPLICATION_PDF("application/pdf")`

                    - `JsonValue; type "base64"constant`

                      - `BASE64("base64")`

                  - `class PlainTextSource:`

                    - `String data`

                    - `JsonValue; mediaType "text/plain"constant`

                      - `TEXT_PLAIN("text/plain")`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                  - `class ContentBlockSource:`

                    - `Content content`

                      - `String`

                      - `List<ContentBlockSourceContent>`

                        - `class TextBlockParam:`

                          - `String text`

                          - `JsonValue; type "text"constant`

                            - `TEXT("text")`

                          - `Optional<CacheControlEphemeral> cacheControl`

                            Create a cache control breakpoint at this content block.

                            - `JsonValue; type "ephemeral"constant`

                              - `EPHEMERAL("ephemeral")`

                            - `Optional<Ttl> ttl`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `TTL_5M("5m")`

                              - `TTL_1H("1h")`

                          - `Optional<List<TextCitationParam>> citations`

                            - `class CitationCharLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endCharIndex`

                              - `long startCharIndex`

                              - `JsonValue; type "char_location"constant`

                                - `CHAR_LOCATION("char_location")`

                            - `class CitationPageLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endPageNumber`

                              - `long startPageNumber`

                              - `JsonValue; type "page_location"constant`

                                - `PAGE_LOCATION("page_location")`

                            - `class CitationContentBlockLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endBlockIndex`

                              - `long startBlockIndex`

                              - `JsonValue; type "content_block_location"constant`

                                - `CONTENT_BLOCK_LOCATION("content_block_location")`

                            - `class CitationWebSearchResultLocationParam:`

                              - `String citedText`

                              - `String encryptedIndex`

                              - `Optional<String> title`

                              - `JsonValue; type "web_search_result_location"constant`

                                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                              - `String url`

                            - `class CitationSearchResultLocationParam:`

                              - `String citedText`

                              - `long endBlockIndex`

                              - `long searchResultIndex`

                              - `String source`

                              - `long startBlockIndex`

                              - `Optional<String> title`

                              - `JsonValue; type "search_result_location"constant`

                                - `SEARCH_RESULT_LOCATION("search_result_location")`

                        - `class ImageBlockParam:`

                          - `Source source`

                            - `class Base64ImageSource:`

                              - `String data`

                              - `MediaType mediaType`

                                - `IMAGE_JPEG("image/jpeg")`

                                - `IMAGE_PNG("image/png")`

                                - `IMAGE_GIF("image/gif")`

                                - `IMAGE_WEBP("image/webp")`

                              - `JsonValue; type "base64"constant`

                                - `BASE64("base64")`

                            - `class UrlImageSource:`

                              - `JsonValue; type "url"constant`

                                - `URL("url")`

                              - `String url`

                          - `JsonValue; type "image"constant`

                            - `IMAGE("image")`

                          - `Optional<CacheControlEphemeral> cacheControl`

                            Create a cache control breakpoint at this content block.

                            - `JsonValue; type "ephemeral"constant`

                              - `EPHEMERAL("ephemeral")`

                            - `Optional<Ttl> ttl`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `TTL_5M("5m")`

                              - `TTL_1H("1h")`

                    - `JsonValue; type "content"constant`

                      - `CONTENT("content")`

                  - `class UrlPdfSource:`

                    - `JsonValue; type "url"constant`

                      - `URL("url")`

                    - `String url`

                - `JsonValue; type "document"constant`

                  - `DOCUMENT("document")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<CitationsConfigParam> citations`

                  - `Optional<Boolean> enabled`

                - `Optional<String> context`

                - `Optional<String> title`

              - `JsonValue; type "web_fetch_result"constant`

                - `WEB_FETCH_RESULT("web_fetch_result")`

              - `String url`

                Fetched content URL

              - `Optional<String> retrievedAt`

                ISO 8601 timestamp when the content was retrieved

          - `String toolUseId`

          - `JsonValue; type "web_fetch_tool_result"constant`

            - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `class CodeExecutionToolResultBlockParam:`

          - `CodeExecutionToolResultBlockParamContent content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class CodeExecutionToolResultErrorParam:`

              - `CodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue; type "code_execution_tool_result_error"constant`

                - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

            - `class CodeExecutionResultBlockParam:`

              - `List<CodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue; type "code_execution_output"constant`

                  - `CODE_EXECUTION_OUTPUT("code_execution_output")`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue; type "code_execution_result"constant`

                - `CODE_EXECUTION_RESULT("code_execution_result")`

            - `class EncryptedCodeExecutionResultBlockParam:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `List<CodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue; type "code_execution_output"constant`

                  - `CODE_EXECUTION_OUTPUT("code_execution_output")`

              - `String encryptedStdout`

              - `long returnCode`

              - `String stderr`

              - `JsonValue; type "encrypted_code_execution_result"constant`

                - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

          - `String toolUseId`

          - `JsonValue; type "code_execution_tool_result"constant`

            - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class BashCodeExecutionToolResultBlockParam:`

          - `Content content`

            - `class BashCodeExecutionToolResultErrorParam:`

              - `BashCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

              - `JsonValue; type "bash_code_execution_tool_result_error"constant`

                - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

            - `class BashCodeExecutionResultBlockParam:`

              - `List<BashCodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue; type "bash_code_execution_output"constant`

                  - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue; type "bash_code_execution_result"constant`

                - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

          - `String toolUseId`

          - `JsonValue; type "bash_code_execution_tool_result"constant`

            - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class TextEditorCodeExecutionToolResultBlockParam:`

          - `Content content`

            - `class TextEditorCodeExecutionToolResultErrorParam:`

              - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `FILE_NOT_FOUND("file_not_found")`

              - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

              - `Optional<String> errorMessage`

            - `class TextEditorCodeExecutionViewResultBlockParam:`

              - `String content`

              - `FileType fileType`

                - `TEXT("text")`

                - `IMAGE("image")`

                - `PDF("pdf")`

              - `JsonValue; type "text_editor_code_execution_view_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

              - `Optional<Long> numLines`

              - `Optional<Long> startLine`

              - `Optional<Long> totalLines`

            - `class TextEditorCodeExecutionCreateResultBlockParam:`

              - `boolean isFileUpdate`

              - `JsonValue; type "text_editor_code_execution_create_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

            - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

              - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

              - `Optional<List<String>> lines`

              - `Optional<Long> newLines`

              - `Optional<Long> newStart`

              - `Optional<Long> oldLines`

              - `Optional<Long> oldStart`

          - `String toolUseId`

          - `JsonValue; type "text_editor_code_execution_tool_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class ToolSearchToolResultBlockParam:`

          - `Content content`

            - `class ToolSearchToolResultErrorParam:`

              - `ToolSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue; type "tool_search_tool_result_error"constant`

                - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

            - `class ToolSearchToolSearchResultBlockParam:`

              - `List<ToolReferenceBlockParam> toolReferences`

                - `String toolName`

                - `JsonValue; type "tool_reference"constant`

                  - `TOOL_REFERENCE("tool_reference")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

              - `JsonValue; type "tool_search_tool_search_result"constant`

                - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

          - `String toolUseId`

          - `JsonValue; type "tool_search_tool_result"constant`

            - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class ContainerUploadBlockParam:`

          A content block that represents a file to be uploaded to the container
          Files uploaded via this block will be available in the container's input directory.

          - `String fileId`

          - `JsonValue; type "container_upload"constant`

            - `CONTAINER_UPLOAD("container_upload")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

    - `Role role`

      - `USER("user")`

      - `ASSISTANT("assistant")`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `Optional<CacheControlEphemeral> cacheControl`

    Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

  - `Optional<OutputConfig> outputConfig`

    Configuration options for the model's output, such as the output format.

  - `Optional<System> system`

    System prompt.

    A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

    - `String`

    - `List<TextBlockParam>`

      - `String text`

      - `JsonValue; type "text"constant`

        - `TEXT("text")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<List<TextCitationParam>> citations`

        - `class CitationCharLocationParam:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endCharIndex`

          - `long startCharIndex`

          - `JsonValue; type "char_location"constant`

            - `CHAR_LOCATION("char_location")`

        - `class CitationPageLocationParam:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endPageNumber`

          - `long startPageNumber`

          - `JsonValue; type "page_location"constant`

            - `PAGE_LOCATION("page_location")`

        - `class CitationContentBlockLocationParam:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endBlockIndex`

          - `long startBlockIndex`

          - `JsonValue; type "content_block_location"constant`

            - `CONTENT_BLOCK_LOCATION("content_block_location")`

        - `class CitationWebSearchResultLocationParam:`

          - `String citedText`

          - `String encryptedIndex`

          - `Optional<String> title`

          - `JsonValue; type "web_search_result_location"constant`

            - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

          - `String url`

        - `class CitationSearchResultLocationParam:`

          - `String citedText`

          - `long endBlockIndex`

          - `long searchResultIndex`

          - `String source`

          - `long startBlockIndex`

          - `Optional<String> title`

          - `JsonValue; type "search_result_location"constant`

            - `SEARCH_RESULT_LOCATION("search_result_location")`

  - `Optional<ThinkingConfigParam> thinking`

    Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

    See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

  - `Optional<ToolChoice> toolChoice`

    How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `Optional<List<MessageCountTokensTool>> tools`

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

      - `InputSchema inputSchema`

        [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

        This defines the shape of the `input` that your tool accepts and that the model will produce.

        - `JsonValue; type "object"constant`

          - `OBJECT("object")`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<String> description`

        Description of what this tool does.

        Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

      - `Optional<Boolean> eagerInputStreaming`

        Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<Type> type`

        - `CUSTOM("custom")`

    - `class ToolBash20250124:`

      - `JsonValue; name "bash"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `BASH("bash")`

      - `JsonValue; type "bash_20250124"constant`

        - `BASH_20250124("bash_20250124")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20250522:`

      - `JsonValue; name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `CODE_EXECUTION("code_execution")`

      - `JsonValue; type "code_execution_20250522"constant`

        - `CODE_EXECUTION_20250522("code_execution_20250522")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20250825:`

      - `JsonValue; name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `CODE_EXECUTION("code_execution")`

      - `JsonValue; type "code_execution_20250825"constant`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20260120:`

      Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

      - `JsonValue; name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `CODE_EXECUTION("code_execution")`

      - `JsonValue; type "code_execution_20260120"constant`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class MemoryTool20250818:`

      - `JsonValue; name "memory"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `MEMORY("memory")`

      - `JsonValue; type "memory_20250818"constant`

        - `MEMORY_20250818("memory_20250818")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250124:`

      - `JsonValue; name "str_replace_editor"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `STR_REPLACE_EDITOR("str_replace_editor")`

      - `JsonValue; type "text_editor_20250124"constant`

        - `TEXT_EDITOR_20250124("text_editor_20250124")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250429:`

      - `JsonValue; name "str_replace_based_edit_tool"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

      - `JsonValue; type "text_editor_20250429"constant`

        - `TEXT_EDITOR_20250429("text_editor_20250429")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250728:`

      - `JsonValue; name "str_replace_based_edit_tool"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

      - `JsonValue; type "text_editor_20250728"constant`

        - `TEXT_EDITOR_20250728("text_editor_20250728")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Long> maxCharacters`

        Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebSearchTool20250305:`

      - `JsonValue; name "web_search"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `WEB_SEARCH("web_search")`

      - `JsonValue; type "web_search_20250305"constant`

        - `WEB_SEARCH_20250305("web_search_20250305")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<String>> allowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `Optional<List<String>> blockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<UserLocation> userLocation`

        Parameters for the user's location. Used to provide more relevant search results.

        - `JsonValue; type "approximate"constant`

          - `APPROXIMATE("approximate")`

        - `Optional<String> city`

          The city of the user.

        - `Optional<String> country`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        - `Optional<String> region`

          The region of the user.

        - `Optional<String> timezone`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

    - `class WebFetchTool20250910:`

      - `JsonValue; name "web_fetch"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `WEB_FETCH("web_fetch")`

      - `JsonValue; type "web_fetch_20250910"constant`

        - `WEB_FETCH_20250910("web_fetch_20250910")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

        - `Optional<Boolean> enabled`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebSearchTool20260209:`

      - `JsonValue; name "web_search"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `WEB_SEARCH("web_search")`

      - `JsonValue; type "web_search_20260209"constant`

        - `WEB_SEARCH_20260209("web_search_20260209")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<String>> allowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `Optional<List<String>> blockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<UserLocation> userLocation`

        Parameters for the user's location. Used to provide more relevant search results.

        - `JsonValue; type "approximate"constant`

          - `APPROXIMATE("approximate")`

        - `Optional<String> city`

          The city of the user.

        - `Optional<String> country`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        - `Optional<String> region`

          The region of the user.

        - `Optional<String> timezone`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

    - `class WebFetchTool20260209:`

      - `JsonValue; name "web_fetch"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `WEB_FETCH("web_fetch")`

      - `JsonValue; type "web_fetch_20260209"constant`

        - `WEB_FETCH_20260209("web_fetch_20260209")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

        - `Optional<Boolean> enabled`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolSearchToolBm25_20251119:`

      - `JsonValue; name "tool_search_tool_bm25"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `Type type`

        - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolSearchToolRegex20251119:`

      - `JsonValue; name "tool_search_tool_regex"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

      - `Type type`

        - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

### Returns

- `class MessageTokensCount:`

  - `long inputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MessageCountTokensParams;
import com.anthropic.models.messages.MessageTokensCount;
import com.anthropic.models.messages.Model;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCountTokensParams params = MessageCountTokensParams.builder()
            .addUserMessage("Hello, world")
            .model(Model.CLAUDE_OPUS_4_6)
            .build();
        MessageTokensCount messageTokensCount = client.messages().countTokens(params);
    }
}
```

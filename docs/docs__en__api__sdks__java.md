# Java SDK

Install and configure the Anthropic Java SDK with builder patterns and async support

---

The Anthropic Java SDK provides convenient access to the Anthropic REST API from applications written in Java. It uses the builder pattern for creating requests and supports both synchronous and asynchronous operations.

<Info>
For API feature documentation with code examples, see the [API reference](/docs/en/api/overview). This page covers Java-specific SDK features and configuration.
</Info>

## Installation

<Tabs>
<Tab title="Gradle">
```kotlin
implementation("com.anthropic:anthropic-java:2.14.0")
```
</Tab>
<Tab title="Maven">
```xml
<dependency>
    <groupId>com.anthropic</groupId>
    <artifactId>anthropic-java</artifactId>
    <version>2.14.0</version>
</dependency>
```
</Tab>
</Tabs>

## Requirements

This library requires Java 8 or later.

## Quick start

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

// Configures using the `anthropic.apiKey`, `anthropic.authToken` and `anthropic.baseUrl` system properties
// Or configures using the `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` and `ANTHROPIC_BASE_URL` environment variables
AnthropicClient client = AnthropicOkHttpClient.fromEnv();

MessageCreateParams params = MessageCreateParams.builder()
  .maxTokens(1024L)
  .addUserMessage("Hello, Claude")
  .model(Model.CLAUDE_OPUS_4_6)
  .build();

Message message = client.messages().create(params);
```

## Client configuration

### API key setup

Configure the client using system properties or environment variables:

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

// Configures using the `anthropic.apiKey`, `anthropic.authToken` and `anthropic.baseUrl` system properties
// Or configures using the `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` and `ANTHROPIC_BASE_URL` environment variables
AnthropicClient client = AnthropicOkHttpClient.fromEnv();
```

Or configure manually:

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

AnthropicClient client = AnthropicOkHttpClient.builder()
  .apiKey("my-anthropic-api-key")
  .build();
```

Or use a combination of both approaches:

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

AnthropicClient client = AnthropicOkHttpClient.builder()
  // Configures using system properties or environment variables
  .fromEnv()
  .apiKey("my-anthropic-api-key")
  .build();
```

### Configuration options

| Setter      | System property       | Environment variable   | Required | Default value                 |
| ----------- | --------------------- | ---------------------- | -------- | ----------------------------- |
| `apiKey`    | `anthropic.apiKey`    | `ANTHROPIC_API_KEY`    | false    | -                             |
| `authToken` | `anthropic.authToken` | `ANTHROPIC_AUTH_TOKEN` | false    | -                             |
| `baseUrl`   | `anthropic.baseUrl`   | `ANTHROPIC_BASE_URL`   | true     | `"https://api.anthropic.com"` |

System properties take precedence over environment variables.

<Tip>
Don't create more than one client in the same application. Each client has a connection pool and thread pools, which are more efficient to share between requests.
</Tip>

### Modifying configuration

To temporarily use a modified client configuration while reusing the same connection and thread pools, call `withOptions()` on any client or service:

```java
import com.anthropic.client.AnthropicClient;

AnthropicClient clientWithOptions = client.withOptions(optionsBuilder -> {
  optionsBuilder.baseUrl("https://example.com");
  optionsBuilder.maxRetries(42);
});
```

The `withOptions()` method does not affect the original client or service.

## Async usage

The default client is synchronous. To switch to asynchronous execution, call the `async()` method:

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import java.util.concurrent.CompletableFuture;

AnthropicClient client = AnthropicOkHttpClient.fromEnv();

MessageCreateParams params = MessageCreateParams.builder()
  .maxTokens(1024L)
  .addUserMessage("Hello, Claude")
  .model(Model.CLAUDE_OPUS_4_6)
  .build();

CompletableFuture<Message> message = client.async().messages().create(params);
```

Or create an asynchronous client from the beginning:

```java
import com.anthropic.client.AnthropicClientAsync;
import com.anthropic.client.okhttp.AnthropicOkHttpClientAsync;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import java.util.concurrent.CompletableFuture;

AnthropicClientAsync client = AnthropicOkHttpClientAsync.fromEnv();

MessageCreateParams params = MessageCreateParams.builder()
  .maxTokens(1024L)
  .addUserMessage("Hello, Claude")
  .model(Model.CLAUDE_OPUS_4_6)
  .build();

CompletableFuture<Message> message = client.messages().create(params);
```

The asynchronous client supports the same options as the synchronous one, except most methods return `CompletableFuture`s.

## Streaming

The SDK defines methods that return response "chunk" streams, where each chunk can be individually processed as soon as it arrives instead of waiting on the full response.

### Synchronous streaming

These streaming methods return `StreamResponse` for synchronous clients:

```java
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.messages.RawMessageStreamEvent;

try (StreamResponse<RawMessageStreamEvent> streamResponse = client.messages().createStreaming(params)) {
    streamResponse.stream().forEach(chunk -> {
        System.out.println(chunk);
    });
    System.out.println("No more chunks!");
}
```

### Asynchronous streaming

For asynchronous clients, the method returns `AsyncStreamResponse`:

```java
import com.anthropic.core.http.AsyncStreamResponse;
import com.anthropic.models.messages.RawMessageStreamEvent;
import java.util.Optional;

client.async().messages().createStreaming(params).subscribe(chunk -> {
    System.out.println(chunk);
});

// If you need to handle errors or completion of the stream
client.async().messages().createStreaming(params).subscribe(new AsyncStreamResponse.Handler<>() {
    @Override
    public void onNext(RawMessageStreamEvent chunk) {
        System.out.println(chunk);
    }

    @Override
    public void onComplete(Optional<Throwable> error) {
        if (error.isPresent()) {
            System.out.println("Something went wrong!");
            throw new RuntimeException(error.get());
        } else {
            System.out.println("No more chunks!");
        }
    }
});

// Or use futures
client.async().messages().createStreaming(params)
    .subscribe(chunk -> {
        System.out.println(chunk);
    })
    .onCompleteFuture()
    .whenComplete((unused, error) -> {
        if (error != null) {
            System.out.println("Something went wrong!");
            throw new RuntimeException(error);
        } else {
            System.out.println("No more chunks!");
        }
    });
```

Async streaming uses a dedicated per-client cached thread pool `Executor` to stream without blocking the current thread. To use a different `Executor`:

```java
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;

Executor executor = Executors.newFixedThreadPool(4);
client.async().messages().createStreaming(params).subscribe(
    chunk -> System.out.println(chunk), executor
);
```

Or configure the client globally using the `streamHandlerExecutor` method:

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import java.util.concurrent.Executors;

AnthropicClient client = AnthropicOkHttpClient.builder()
  .fromEnv()
  .streamHandlerExecutor(Executors.newFixedThreadPool(4))
  .build();
```

### Streaming with message accumulator

A `MessageAccumulator` can record the stream of events in the response as they are processed and accumulate a `Message` object similar to what would have been returned by the non-streaming API.

For a synchronous response, add a `Stream.peek()` call to the stream pipeline to accumulate each event:

```java
import com.anthropic.core.http.StreamResponse;
import com.anthropic.helpers.MessageAccumulator;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.RawMessageStreamEvent;

MessageAccumulator messageAccumulator = MessageAccumulator.create();

try (StreamResponse<RawMessageStreamEvent> streamResponse =
         client.messages().createStreaming(createParams)) {
    streamResponse.stream()
            .peek(messageAccumulator::accumulate)
            .flatMap(event -> event.contentBlockDelta().stream())
            .flatMap(deltaEvent -> deltaEvent.delta().text().stream())
            .forEach(textDelta -> System.out.print(textDelta.text()));
}

Message message = messageAccumulator.message();
```

For an asynchronous response, add the `MessageAccumulator` to the `subscribe()` call:

```java
import com.anthropic.helpers.MessageAccumulator;
import com.anthropic.models.messages.Message;

MessageAccumulator messageAccumulator = MessageAccumulator.create();

client.messages()
        .createStreaming(createParams)
        .subscribe(event -> messageAccumulator.accumulate(event).contentBlockDelta().stream()
                .flatMap(deltaEvent -> deltaEvent.delta().text().stream())
                .forEach(textDelta -> System.out.print(textDelta.text())))
        .onCompleteFuture()
        .join();

Message message = messageAccumulator.message();
```

A `BetaMessageAccumulator` is also available for the accumulation of a `BetaMessage` object. It is used in the same manner as the `MessageAccumulator`.

## Structured outputs

For complete structured outputs documentation including Java examples, see [Structured Outputs](/docs/en/build-with-claude/structured-outputs).

## Tool use

[Tool Use](/docs/en/agents-and-tools/tool-use/overview) lets you integrate external tools and functions directly into the AI model's responses. Instead of producing plain text, the model can output instructions (with parameters) for invoking a tool or calling a function when appropriate. You define JSON schemas for tools, and the model uses the schemas to decide when and how to use these tools.

The tool use feature supports a "strict" mode (beta) that guarantees that the JSON output from the AI model will conform to the JSON schema you provide in the input parameters.

The SDK can derive a tool and its parameters automatically from the structure of an arbitrary Java class: the class's name (converted to snake case) provides the tool name, and the class's fields define the tool's parameters.

### Defining tools with annotations

```java
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;

enum Unit {
  CELSIUS,
  FAHRENHEIT;

  public String toString() {
    switch (this) {
      case CELSIUS:
        return "C";
      case FAHRENHEIT:
      default:
        return "F";
    }
  }

  public double fromKelvin(double temperatureK) {
    switch (this) {
      case CELSIUS:
        return temperatureK - 273.15;
      case FAHRENHEIT:
      default:
        return (temperatureK - 273.15) * 1.8 + 32.0;
    }
  }
}

@JsonClassDescription("Get the weather in a given location")
static class GetWeather {

  @JsonPropertyDescription("The city and state, e.g. San Francisco, CA")
  public String location;

  @JsonPropertyDescription("The unit of temperature")
  public Unit unit;

  public Weather execute() {
    double temperatureK;
    switch (location) {
      case "San Francisco, CA":
        temperatureK = 300.0;
        break;
      case "New York, NY":
        temperatureK = 310.0;
        break;
      case "Dallas, TX":
        temperatureK = 305.0;
        break;
      default:
        temperatureK = 295;
        break;
    }
    return new Weather(String.format("%.0f%s", unit.fromKelvin(temperatureK), unit));
  }
}

static class Weather {

  public String temperature;

  public Weather(String temperature) {
    this.temperature = temperature;
  }
}
```

### Calling tools

When your tool classes are defined, add them to the message parameters using `MessageCreateParams.addTool(Class<T>)` and then call them if requested to do so in the AI model's response. `BetaToolUseBlock.input(Class<T>)` can be used to parse a tool's parameters in JSON form to an instance of your tool-defining class.

After invoking the tool, use `BetaToolResultBlockParam.Builder.contentAsJson(Object)` to pass the tool's result back to the AI model:

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.*;
import com.anthropic.models.messages.Model;
import java.util.List;

AnthropicClient client = AnthropicOkHttpClient.fromEnv();

MessageCreateParams.Builder createParamsBuilder = MessageCreateParams.builder()
        .model(Model.CLAUDE_OPUS_4_6)
        .maxTokens(2048)
        .addTool(GetWeather.class)
        .addUserMessage("What's the temperature in New York?");

client.beta().messages().create(createParamsBuilder.build()).content().stream()
        .flatMap(contentBlock -> contentBlock.toolUse().stream())
        .forEach(toolUseBlock -> createParamsBuilder
              // Add a message indicating that the tool use was requested.
              .addAssistantMessageOfBetaContentBlockParams(
                      List.of(BetaContentBlockParam.ofToolUse(BetaToolUseBlockParam.builder()
                              .name(toolUseBlock.name())
                              .id(toolUseBlock.id())
                              .input(toolUseBlock._input())
                              .build())))
              // Add a message with the result of the requested tool use.
              .addUserMessageOfBetaContentBlockParams(
                      List.of(BetaContentBlockParam.ofToolResult(BetaToolResultBlockParam.builder()
                              .toolUseId(toolUseBlock.id())
                              .contentAsJson(callTool(toolUseBlock))
                              .build()))));

client.beta().messages().create(createParamsBuilder.build()).content().stream()
        .flatMap(contentBlock -> contentBlock.text().stream())
        .forEach(textBlock -> System.out.println(textBlock.text()));

private static Object callTool(BetaToolUseBlock toolUseBlock) {
  if (!"get_weather".equals(toolUseBlock.name())) {
    throw new IllegalArgumentException("Unknown tool: " + toolUseBlock.name());
  }

  GetWeather tool = toolUseBlock.input(GetWeather.class);
  return tool != null ? tool.execute() : new Weather("unknown");
}
```

### Tool name conversion

Tool names are derived from the camel case tool class names (e.g., `GetWeather`) and converted to snake case (e.g., `get_weather`). Word boundaries begin where the current character is not the first character, is upper-case, and either the preceding character is lower-case, or the following character is lower-case. For example, `MyJSONParser` becomes `my_json_parser` and `ParseJSON` becomes `parse_json`. This conversion can be overridden using the `@JsonTypeName` annotation.

### Local tool JSON schema validation

Like for structured outputs, you can perform local validation to check that the JSON schema derived from your tool class respects Anthropic's restrictions. Local validation is enabled by default, but it can be disabled:

```java
MessageCreateParams.Builder createParamsBuilder = MessageCreateParams.builder()
  .model(Model.CLAUDE_OPUS_4_6)
  .maxTokens(2048)
  .addTool(GetWeather.class, JsonSchemaLocalValidation.NO)
  .addUserMessage("What's the temperature in New York?");
```

### Annotating tool classes

You can use annotations to add further information about tools to the JSON schemas:

- `@JsonClassDescription` - Add a description to a tool class detailing when and how to use that tool.
- `@JsonTypeName` - Set the tool name to something other than the simple name of the class converted to snake case.
- `@JsonPropertyDescription` - Add a detailed description to a tool parameter.
- `@JsonIgnore` - Exclude a `public` field or getter method from the generated JSON schema for a tool's parameters.
- `@JsonProperty` - Include a non-`public` field or getter method in the generated JSON schema for a tool's parameters.

## Message batches

The SDK provides support for the [Message Batches API](/docs/en/build-with-claude/batch-processing) under the `client.messages().batches()` namespace. See the [pagination section](#pagination) for how to iterate through batch results.

## File uploads

The SDK defines methods that accept files through the `MultipartField` interface:

```java
import com.anthropic.core.MultipartField;
import com.anthropic.models.beta.AnthropicBeta;
import com.anthropic.models.beta.files.FileMetadata;
import com.anthropic.models.beta.files.FileUploadParams;
import java.io.InputStream;
import java.nio.file.Paths;

FileUploadParams params = FileUploadParams.builder()
  .file(
    MultipartField.<InputStream>builder()
      .value(Files.newInputStream(Paths.get("/path/to/file.pdf")))
      .contentType("application/pdf")
      .build()
  )
  .addBeta(AnthropicBeta.FILES_API_2025_04_14)
  .build();

FileMetadata fileMetadata = client.beta().files().upload(params);
```

Or from an `InputStream`:

```java
import com.anthropic.core.MultipartField;
import com.anthropic.models.beta.AnthropicBeta;
import com.anthropic.models.beta.files.FileMetadata;
import com.anthropic.models.beta.files.FileUploadParams;
import java.io.InputStream;
import java.net.URL;

FileUploadParams params = FileUploadParams.builder()
  .file(
    MultipartField.<InputStream>builder()
      .value(new URL("https://example.com/path/to/file").openStream())
      .filename("document.pdf")
      .contentType("application/pdf")
      .build()
  )
  .addBeta(AnthropicBeta.FILES_API_2025_04_14)
  .build();

FileMetadata fileMetadata = client.beta().files().upload(params);
```

Or a `byte[]` array:

```java
import com.anthropic.core.MultipartField;
import com.anthropic.models.beta.AnthropicBeta;
import com.anthropic.models.beta.files.FileMetadata;
import com.anthropic.models.beta.files.FileUploadParams;

FileUploadParams params = FileUploadParams.builder()
  .file(
    MultipartField.<byte[]>builder()
      .value("content".getBytes())
      .filename("document.txt")
      .contentType("text/plain")
      .build()
  )
  .addBeta(AnthropicBeta.FILES_API_2025_04_14)
  .build();

FileMetadata fileMetadata = client.beta().files().upload(params);
```

### Binary responses

The SDK defines methods that return binary responses for API responses that aren't necessarily parsed as JSON:

```java
import com.anthropic.core.http.HttpResponse;
import com.anthropic.models.beta.files.FileDownloadParams;

HttpResponse response = client.beta().files().download("file_id");
```

To save the response content to a file:

```java
import com.anthropic.core.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

try (HttpResponse response = client.beta().files().download(params)) {
    Files.copy(
        response.body(),
        Paths.get(path),
        StandardCopyOption.REPLACE_EXISTING
    );
} catch (Exception e) {
    System.out.println("Something went wrong!");
    throw new RuntimeException(e);
}
```

Or transfer the response content to any `OutputStream`:

```java
import com.anthropic.core.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

try (HttpResponse response = client.beta().files().download(params)) {
    response.body().transferTo(Files.newOutputStream(Paths.get(path)));
} catch (Exception e) {
    System.out.println("Something went wrong!");
    throw new RuntimeException(e);
}
```

## Error handling

The SDK throws custom unchecked exception types:

- `AnthropicServiceException` - Base class for HTTP errors.
- `AnthropicIoException` - I/O networking errors.
- `AnthropicRetryableException` - Generic error indicating a failure that could be retried.
- `AnthropicInvalidDataException` - Failure to interpret successfully parsed data (e.g., when accessing a property that's supposed to be required, but the API unexpectedly omitted it).
- `AnthropicException` - Base class for all exceptions.

### Status code mapping

| Status | Exception |
| ------ | --------- |
| 400    | `BadRequestException` |
| 401    | `UnauthorizedException` |
| 403    | `PermissionDeniedException` |
| 404    | `NotFoundException` |
| 422    | `UnprocessableEntityException` |
| 429    | `RateLimitException` |
| 5xx    | `InternalServerException` |
| others | `UnexpectedStatusCodeException` |

`SseException` is thrown for errors encountered during SSE streaming after a successful initial HTTP response.

```java
import com.anthropic.errors.*;

try {
    Message message = client.messages().create(params);
} catch (RateLimitException e) {
    System.out.println("Rate limited, retry after: " + e.headers());
} catch (UnauthorizedException e) {
    System.out.println("Invalid API key");
} catch (AnthropicServiceException e) {
    System.out.println("API error: " + e.statusCode());
} catch (AnthropicIoException e) {
    System.out.println("Network error: " + e.getMessage());
}
```

## Request IDs

When using raw responses, you can access the `request-id` response header using the `requestId()` method:

```java
import com.anthropic.core.http.HttpResponseFor;
import com.anthropic.models.messages.Message;
import java.util.Optional;

HttpResponseFor<Message> message = client.messages().withRawResponse().create(params);

Optional<String> requestId = message.requestId();
```

This can be used to quickly log failing requests and report them back to Anthropic. For more information on debugging requests, see the [API error documentation](/docs/en/api/errors#request-id).

## Retries

The SDK automatically retries 2 times by default, with a short exponential backoff between requests.

Only the following error types are retried:

- Connection errors (for example, due to a network connectivity problem)
- 408 Request Timeout
- 409 Conflict
- 429 Rate Limit
- 5xx Internal

The API may also explicitly instruct the SDK to retry or not retry a request.

To set a custom number of retries, configure the client using the `maxRetries` method:

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

AnthropicClient client = AnthropicOkHttpClient.builder().fromEnv().maxRetries(4).build();
```

## Timeouts

Requests time out after 10 minutes by default.

However, for methods that accept `maxTokens`, if you specify a large `maxTokens` value and are not streaming, then the default timeout will be calculated dynamically using this formula:

```java
Duration.ofSeconds(
    Math.min(
        60 * 60, // 1 hour max
        Math.max(
            10 * 60, // 10 minute minimum
            60 * 60 * maxTokens / 128_000
        )
    )
)
```

This results in a timeout of up to 60 minutes, scaled by the `maxTokens` parameter, unless overridden.

To set a custom timeout per-request:

```java
import com.anthropic.models.messages.Message;

Message message = client
  .messages()
  .create(params, RequestOptions.builder().timeout(Duration.ofSeconds(30)).build());
```

Or configure the default for all method calls at the client level:

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import java.time.Duration;

AnthropicClient client = AnthropicOkHttpClient.builder()
  .fromEnv()
  .timeout(Duration.ofSeconds(30))
  .build();
```

## Long requests

<Warning>
Consider using [streaming](#streaming) for longer running requests.
</Warning>

Avoid setting a large `maxTokens` value without using streaming. Some networks may drop idle connections after a certain period of time, which can cause the request to fail or [timeout](#timeouts) without receiving a response from Anthropic. The SDK periodically pings the API to keep the connection alive and reduce the impact of these networks.

The SDK throws an error if a non-streaming request is expected to take longer than 10 minutes. Using a [streaming method](#streaming) or [overriding the timeout](#timeouts) at the client or request level disables the error.

## Pagination

The SDK provides convenient ways to access paginated results either one page at a time or item-by-item across all pages.

### Auto-pagination

To iterate through all results across all pages, use the `autoPager()` method, which automatically fetches more pages as needed.

```java
import com.anthropic.models.messages.batches.BatchListPage;
import com.anthropic.models.messages.batches.MessageBatch;

BatchListPage page = client.messages().batches().list();

// Process as an Iterable
for (MessageBatch batch : page.autoPager()) {
    System.out.println(batch);
}

// Process as a Stream
page.autoPager()
    .stream()
    .limit(50)
    .forEach(batch -> System.out.println(batch));
```

When using the asynchronous client, the method returns an `AsyncStreamResponse`:

```java
import com.anthropic.core.http.AsyncStreamResponse;
import com.anthropic.models.messages.batches.BatchListPageAsync;
import com.anthropic.models.messages.batches.MessageBatch;
import java.util.Optional;
import java.util.concurrent.CompletableFuture;

CompletableFuture<BatchListPageAsync> pageFuture = client.async().messages().batches().list();

pageFuture.thenAccept(page -> page.autoPager().subscribe(batch -> {
    System.out.println(batch);
}));

// If you need to handle errors or completion of the stream
pageFuture.thenAccept(page -> page.autoPager().subscribe(new AsyncStreamResponse.Handler<>() {
    @Override
    public void onNext(MessageBatch batch) {
        System.out.println(batch);
    }

    @Override
    public void onComplete(Optional<Throwable> error) {
        if (error.isPresent()) {
            System.out.println("Something went wrong!");
            throw new RuntimeException(error.get());
        } else {
            System.out.println("No more!");
        }
    }
}));

// Or use futures
pageFuture.thenAccept(page -> page.autoPager()
    .subscribe(batch -> {
        System.out.println(batch);
    })
    .onCompleteFuture()
    .whenComplete((unused, error) -> {
        if (error != null) {
            System.out.println("Something went wrong!");
            throw new RuntimeException(error);
        } else {
            System.out.println("No more!");
        }
    }));
```

### Manual pagination

To access individual page items and manually request the next page:

```java
import com.anthropic.models.messages.batches.BatchListPage;
import com.anthropic.models.messages.batches.MessageBatch;

BatchListPage page = client.messages().batches().list();
while (true) {
    for (MessageBatch batch : page.items()) {
        System.out.println(batch);
    }

    if (!page.hasNextPage()) {
        break;
    }

    page = page.nextPage();
}
```

## Type system

### Immutability and builders

Each class in the SDK has an associated builder for constructing it. Each class is immutable once constructed. If the class has an associated builder, then it has a `toBuilder()` method, which can be used to convert it back to a builder for making a modified copy.

```java
MessageCreateParams params = MessageCreateParams.builder()
  .maxTokens(1024L)
  .addUserMessage("Hello, Claude")
  .model(Model.CLAUDE_OPUS_4_6)
  .build();

// Create a modified copy using toBuilder()
MessageCreateParams modified = params.toBuilder().maxTokens(2048L).build();
```

Because each class is immutable, builder modification will never affect already built class instances.

### Requests and responses

To send a request to the Claude API, build an instance of some `Params` class and pass it to the corresponding client method. When the response is received, it will be deserialized into an instance of a Java class.

For example, `client.messages().create(...)` should be called with an instance of `MessageCreateParams`, and it will return an instance of `Message`.

### Undocumented parameters

To set undocumented parameters, call the `putAdditionalHeader`, `putAdditionalQueryParam`, or `putAdditionalBodyProperty` methods on any `Params` class:

```java
import com.anthropic.core.JsonValue;
import com.anthropic.models.messages.MessageCreateParams;

MessageCreateParams params = MessageCreateParams.builder()
  .putAdditionalHeader("Secret-Header", "42")
  .putAdditionalQueryParam("secret_query_param", "42")
  .putAdditionalBodyProperty("secretProperty", JsonValue.from("42"))
  .build();
```

These can be accessed on the built object later using the `_additionalHeaders()`, `_additionalQueryParams()`, and `_additionalBodyProperties()` methods.

<Warning>
The values passed to these methods overwrite values passed to earlier methods. For security reasons, ensure these methods are only used with trusted input data.
</Warning>

To set undocumented parameters on nested headers, query params, or body classes:

```java
import com.anthropic.core.JsonValue;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Metadata;

MessageCreateParams params = MessageCreateParams.builder()
  .metadata(
    Metadata.builder().putAdditionalProperty("secretProperty", JsonValue.from("42")).build()
  )
  .build();
```

These properties can be accessed on the nested built object later using the `_additionalProperties()` method.

To set a documented parameter or property to an undocumented or not yet supported value, pass a `JsonValue` object to its setter:

```java
import com.anthropic.core.JsonValue;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

MessageCreateParams params = MessageCreateParams.builder()
  .maxTokens(JsonValue.from(3.14))
  .addUserMessage("Hello, Claude")
  .model(Model.CLAUDE_OPUS_4_6)
  .build();
```

### JsonValue creation

The most straightforward way to create a `JsonValue` is using its `from(...)` method:

```java
import com.anthropic.core.JsonValue;
import java.util.List;
import java.util.Map;

// Create primitive JSON values
JsonValue nullValue = JsonValue.from(null);

JsonValue booleanValue = JsonValue.from(true);

JsonValue numberValue = JsonValue.from(42);

JsonValue stringValue = JsonValue.from("Hello World!");

// Create a JSON array value equivalent to `["Hello", "World"]`
JsonValue arrayValue = JsonValue.from(List.of("Hello", "World"));

// Create a JSON object value equivalent to `{ "a": 1, "b": 2 }`
JsonValue objectValue = JsonValue.from(Map.of("a", 1, "b", 2));

// Create an arbitrarily nested JSON equivalent to:
// { "a": [1, 2], "b": [3, 4] }
JsonValue complexValue = JsonValue.from(Map.of("a", List.of(1, 2), "b", List.of(3, 4)));
```

### Forcibly omitting required parameters

Normally a `Builder` class's `build` method will throw `IllegalStateException` if any required parameter or property is unset. To forcibly omit a required parameter or property, pass `JsonMissing`:

```java
import com.anthropic.core.JsonMissing;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

MessageCreateParams params = MessageCreateParams.builder()
  .addUserMessage("Hello, world")
  .model(Model.CLAUDE_OPUS_4_6)
  .maxTokens(JsonMissing.of())
  .build();
```

### Response properties

To access undocumented response properties, call the `_additionalProperties()` method:

```java
import com.anthropic.core.JsonValue;
import java.util.Map;

Map<String, JsonValue> additionalProperties = client
  .messages()
  .create(params)
  ._additionalProperties();

JsonValue secretPropertyValue = additionalProperties.get("secretProperty");

String result = secretPropertyValue.accept(new JsonValue.Visitor<>() {
    @Override
    public String visitNull() {
        return "It's null!";
    }

    @Override
    public String visitBoolean(boolean value) {
        return "It's a boolean!";
    }

    @Override
    public String visitNumber(Number value) {
        return "It's a number!";
    }

    // Other methods include `visitMissing`, `visitString`, `visitArray`, and `visitObject`
    // The default implementation of each unimplemented method delegates to `visitDefault`,
    // which throws by default, but can also be overridden
});
```

To access a property's raw JSON value, call its `_` prefixed method:

```java
import com.anthropic.core.JsonField;
import java.util.Optional;

JsonField<Long> maxTokens = client.messages().create(params)._maxTokens();

if (maxTokens.isMissing()) {
  // The property is absent from the JSON response
} else if (maxTokens.isNull()) {
  // The property was set to literal null
} else {
  // Check if value was provided as a string
  // Other methods include `asNumber()`, `asBoolean()`, etc.
  Optional<String> jsonString = maxTokens.asString();

  // Try to deserialize into a custom type
  MyClass myObject = maxTokens.asUnknown().orElseThrow().convert(MyClass.class);
}
```

### Response validation

By default, the SDK will not throw an exception when the API returns a response that doesn't match the expected type. It will throw `AnthropicInvalidDataException` only if you directly access the property.

To check that the response is completely well-typed upfront, call `validate()`:

```java
import com.anthropic.models.messages.Message;

Message message = client.messages().create(params).validate();
```

Or configure per-request:

```java
import com.anthropic.models.messages.Message;

Message message = client
  .messages()
  .create(params, RequestOptions.builder().responseValidation(true).build());
```

Or configure the default for all method calls at the client level:

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

AnthropicClient client = AnthropicOkHttpClient.builder()
  .fromEnv()
  .responseValidation(true)
  .build();
```

## HTTP client customization

### Proxy configuration

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import java.net.InetSocketAddress;
import java.net.Proxy;

AnthropicClient client = AnthropicOkHttpClient.builder()
  .fromEnv()
  .proxy(new Proxy(Proxy.Type.HTTP, new InetSocketAddress("https://example.com", 8080)))
  .build();
```

### HTTPS / SSL configuration

<Note>
Most applications should not call these methods, and instead use the system defaults. The defaults include special optimizations that can be lost if the implementations are modified.
</Note>

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

AnthropicClient client = AnthropicOkHttpClient.builder()
  .fromEnv()
  .sslSocketFactory(yourSSLSocketFactory)
  .trustManager(yourTrustManager)
  .hostnameVerifier(yourHostnameVerifier)
  .build();
```

### Custom HTTP client

The SDK consists of three artifacts:

- `anthropic-java-core` - Contains core SDK logic, does not depend on OkHttp. Exposes `AnthropicClient`, `AnthropicClientAsync`, and their implementation classes, all of which can work with any HTTP client.
- `anthropic-java-client-okhttp` - Depends on OkHttp. Exposes `AnthropicOkHttpClient` and `AnthropicOkHttpClientAsync`.
- `anthropic-java` - Depends on and exposes the APIs of both `anthropic-java-core` and `anthropic-java-client-okhttp`. Does not have its own logic.

This structure allows replacing the SDK's default HTTP client without pulling in unnecessary dependencies.

#### Customized OkHttpClient

<Tip>
Try the available [network options](#retries) before replacing the default client.
</Tip>

To use a customized `OkHttpClient`:

1. Replace your `anthropic-java` dependency with `anthropic-java-core`.
2. Copy `anthropic-java-client-okhttp`'s `OkHttpClient` class into your code and customize it.
3. Construct `AnthropicClientImpl` or `AnthropicClientAsyncImpl` using your customized client.

#### Completely custom HTTP client

To use a completely custom HTTP client:

1. Replace your `anthropic-java` dependency with `anthropic-java-core`.
2. Write a class that implements the `HttpClient` interface.
3. Construct `AnthropicClientImpl` or `AnthropicClientAsyncImpl` using your new client class.

## Platform integrations

<Note>
For detailed platform setup guides with code examples, see:
- [Amazon Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock)
- [Google Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai)
- [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)
</Note>

The Java SDK supports Bedrock, Vertex AI, and Foundry through separate dependencies that provide platform-specific `Backend` implementations:

- **Bedrock**: `com.anthropic:anthropic-java-bedrock`: Uses `BedrockBackend.fromEnv()` or `BedrockBackend.builder()`
- **Vertex AI**: `com.anthropic:anthropic-java-vertex`: Uses `VertexBackend.fromEnv()` or `VertexBackend.builder()`
- **Foundry**: `com.anthropic:anthropic-java-foundry`: Uses `FoundryBackend.fromEnv()` or `FoundryBackend.builder()`

Each backend is passed to the client via `.backend()` on `AnthropicOkHttpClient.builder()`. AWS, Google Cloud, and Azure classes are included as transitive dependencies of the respective library.

## Advanced usage

### Raw response access

To access HTTP headers, status codes, and the raw response body, prefix any HTTP method call with `withRawResponse()`:

```java
import com.anthropic.core.http.Headers;
import com.anthropic.core.http.HttpResponseFor;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

MessageCreateParams params = MessageCreateParams.builder()
  .maxTokens(1024L)
  .addUserMessage("Hello, Claude")
  .model(Model.CLAUDE_OPUS_4_6)
  .build();

HttpResponseFor<Message> message = client.messages().withRawResponse().create(params);

int statusCode = message.statusCode();

Headers headers = message.headers();
```

You can still deserialize the response into an instance of a Java class if needed:

```java
import com.anthropic.models.messages.Message;

Message parsedMessage = message.parse();
```

### Logging

The SDK uses the standard OkHttp logging interceptor.

Enable logging by setting the `ANTHROPIC_LOG` environment variable to `info`:

```bash
export ANTHROPIC_LOG=info
```

Or to `debug` for more verbose logging:

```bash
export ANTHROPIC_LOG=debug
```

<section title="Jackson compatibility">

The SDK depends on Jackson for JSON serialization/deserialization. It is compatible with version 2.13.4 or higher, but depends on version 2.18.2 by default.

The SDK throws an exception if it detects an incompatible Jackson version at runtime (e.g. if the default version was overridden in your Maven or Gradle config).

If the SDK threw an exception, but you're certain the version is compatible, then disable the version check using `checkJacksonVersionCompatibility` on `AnthropicOkHttpClient` or `AnthropicOkHttpClientAsync`.

<Warning>
There is no guarantee that the SDK works correctly when the Jackson version check is disabled.
</Warning>

There are also bugs in older Jackson versions that can affect the SDK. The SDK doesn't work around all Jackson bugs and expects users to upgrade Jackson for those instead.

</section>

<section title="ProGuard/R8 configuration">

Although the SDK uses reflection, it is still usable with ProGuard and R8 because `anthropic-java-core` is published with a configuration file containing keep rules.

ProGuard and R8 should automatically detect and use the published rules, but you can also manually copy the keep rules if necessary.

</section>

### Undocumented API functionality

The SDK is typed for convenient usage of the documented API. However, it also supports working with undocumented or not yet supported parts of the API.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can use the `putAdditionalHeader`, `putAdditionalQueryParam`, or `putAdditionalBodyProperty` methods as described in [Undocumented parameters](#undocumented-parameters).

#### Undocumented response properties

To access undocumented response properties, use the `_additionalProperties()` method as described in [Response properties](#response-properties).

## Beta features

You can access most beta API features through the `beta()` method on the client. To check the availability of all of Claude's capabilities and tools, see the [build with Claude overview](/docs/en/build-with-claude/overview).

For example, to use structured outputs:

```java
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.StructuredMessageCreateParams;
import com.anthropic.models.messages.Model;

StructuredMessageCreateParams<BookList> createParams = MessageCreateParams.builder()
        .model(Model.CLAUDE_OPUS_4_6)
        .maxTokens(2048)
        .outputFormat(BookList.class)
        .addUserMessage("List some famous late twentieth century novels.")
        .build();

client.beta().messages().create(createParams);
```

## Frequently asked questions

<section title="Why doesn't the SDK use plain enum classes?">

Java `enum` classes are not trivially forwards compatible. Using them in the SDK could cause runtime exceptions if the API is updated to respond with a new enum value.

</section>

<section title="Why are fields represented using JsonField<T> instead of just plain T?">

Using `JsonField<T>` enables a few features:

- Allowing usage of undocumented API functionality
- Lazily validating the API response against the expected shape
- Representing absent vs explicitly null values

</section>

<section title="Why doesn't the SDK use data classes?">

It is not backwards compatible to add new fields to a data class, and the SDK avoids introducing a breaking change every time a field is added to a class.

</section>

<section title="Why doesn't the SDK use checked exceptions?">

Checked exceptions are widely considered a mistake in the Java programming language. In fact, they were omitted from Kotlin for this reason.

Checked exceptions:

- Are verbose to handle
- Encourage error handling at the wrong level of abstraction, where nothing can be done about the error
- Are tedious to propagate due to the function coloring problem
- Don't play well with lambdas (also due to the function coloring problem)

</section>

## Semantic versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes to library internals which are technically public but not intended or documented for external use.
2. Changes that aren't expected to impact the vast majority of users in practice.

## Additional resources

- [GitHub repository](https://github.com/anthropics/anthropic-sdk-java)
- [Javadocs](https://javadoc.io/doc/com.anthropic/anthropic-java)
- [API reference](/docs/en/api/overview)
- [Streaming guide](/docs/en/build-with-claude/streaming)
- [Tool use guide](/docs/en/agents-and-tools/tool-use/overview)
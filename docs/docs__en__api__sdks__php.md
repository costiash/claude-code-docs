# PHP SDK

Install and configure the Anthropic PHP SDK with value objects and builder patterns

---

The Anthropic PHP library provides convenient access to the Anthropic REST API from any PHP 8.1.0+ application.

<Info>
The PHP SDK is currently in beta. APIs may change between versions.
</Info>

<Info>
For API feature documentation with code examples, see the [API reference](/docs/en/api/overview). This page covers PHP-specific SDK features and configuration.
</Info>

## Installation

```bash
composer require "anthropic-ai/sdk"
```

## Requirements

PHP 8.1.0 or higher.

## Usage

This library uses named parameters to specify optional arguments. Parameters with a default value must be set by name.

```php hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(
  apiKey: getenv("ANTHROPIC_API_KEY") ?: "my-anthropic-api-key"
);

$message = $client->messages->create(
  maxTokens: 1024,
  messages: [['role' => 'user', 'content' => 'Hello, Claude']],
  model: 'claude-opus-4-7',
);

echo $message->content[0]->text;
```

For authentication options including Workload Identity Federation, see [Authentication](/docs/en/api/authentication/overview).

## Value objects

It is recommended to use the static `with` constructor `Base64ImageSource::with(data: "U3RhaW5sZXNzIHJvY2tz", ...)` and named parameters to initialize value objects.

However, builders are also provided `(new Base64ImageSource)->withData("U3RhaW5sZXNzIHJvY2tz")`.

## Streaming

The SDK provides support for streaming responses using Server-Sent Events (SSE).

```php hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(
  apiKey: getenv("ANTHROPIC_API_KEY") ?: "my-anthropic-api-key"
);

$stream = $client->messages->createStream(
  maxTokens: 1024,
  messages: [['role' => 'user', 'content' => 'Hello, Claude']],
  model: 'claude-opus-4-7',
);

foreach ($stream as $message) {
  var_dump($message);
}
```

## Error handling

When the library is unable to connect to the API, or if the API returns a non-success status code (i.e., 4xx or 5xx response), a subclass of `Anthropic\Core\Exceptions\APIException` is thrown:

```php hidelines={2..3,7..9}
<?php
use Anthropic\Client;

use Anthropic\Core\Exceptions\APIConnectionException;
use Anthropic\Core\Exceptions\APIStatusException;
use Anthropic\Core\Exceptions\RateLimitException;

$client = new Client();

try {
  $message = $client->messages->create(
    maxTokens: 1024,
    messages: [['role' => 'user', 'content' => 'Hello, Claude']],
    model: 'claude-opus-4-7',
  );
} catch (APIConnectionException $e) {
  echo "The server could not be reached", PHP_EOL;
  echo $e->getPrevious()?->getMessage(), PHP_EOL;
} catch (RateLimitException $_) {
  echo "A 429 status code was received; we should back off a bit.", PHP_EOL;
} catch (APIStatusException $e) {
  echo "Another non-200-range status code was received", PHP_EOL;
  echo $e->getMessage();
}
```

Error codes are as follows:

| Cause            | Error Type                     |
| ---------------- | ------------------------------ |
| HTTP 400         | `BadRequestException`          |
| HTTP 401         | `AuthenticationException`      |
| HTTP 403         | `PermissionDeniedException`    |
| HTTP 404         | `NotFoundException`            |
| HTTP 409         | `ConflictException`            |
| HTTP 422         | `UnprocessableEntityException` |
| HTTP 429         | `RateLimitException`           |
| HTTP >= 500      | `InternalServerException`      |
| Other HTTP error | `APIStatusException`           |
| Timeout          | `APITimeoutException`          |
| Network error    | `APIConnectionException`       |

## Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.

Connection errors (for example, because of a network connectivity problem), 408 Request Timeout, 409 Conflict, 429 Rate Limit, >=500 Internal errors, and timeouts are all retried by default.

You can use the `maxRetries` option to configure or disable this:

```php hidelines={1..3,5}
<?php

use Anthropic\Client;
use Anthropic\RequestOptions;

// Configure the default for all requests:
$client = new Client(requestOptions: RequestOptions::with(maxRetries: 0));

// Or, configure per-request:
$result = $client->messages->create(
  maxTokens: 1024,
  messages: [['role' => 'user', 'content' => 'Hello, Claude']],
  model: 'claude-opus-4-7',
  requestOptions: RequestOptions::with(maxRetries: 5),
);
```

## Pagination

List methods in the Claude API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```php hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(
  apiKey: getenv("ANTHROPIC_API_KEY") ?: "my-anthropic-api-key"
);

$page = $client->beta->messages->batches->list(limit: 20);

// fetch items from the current page
foreach ($page->getItems() as $item) {
  echo $item->id, PHP_EOL;
}
// make additional network requests to fetch items from all pages, including and after the current page
foreach ($page->pagingEachItem() as $item) {
  echo $item->id, PHP_EOL;
}
```

## Advanced usage

### Undocumented properties

You can send undocumented parameters to any endpoint, and read undocumented response properties, like so:

<Note>
The `extra*` parameters of the same name override the documented parameters.
</Note>

```php hidelines={2..3,5..7}
<?php
use Anthropic\Client;

use Anthropic\RequestOptions;

$client = new Client();

$message = $client->messages->create(
  maxTokens: 1024,
  messages: [['role' => 'user', 'content' => 'Hello, Claude']],
  model: 'claude-opus-4-7',
  requestOptions: RequestOptions::with(
    extraQueryParams: ['my_query_parameter' => 'value'],
    extraBodyParams: ['my_body_parameter' => 'value'],
    extraHeaders: ['my-header' => 'value'],
  ),
);
```

### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extraQueryParams`, `extraBodyParams`, and `extraHeaders` options under `RequestOptions::with()` when making a request, as seen in the example above.

### Undocumented endpoints

To make requests to undocumented endpoints while retaining the benefit of auth, retries, and so on, you can make requests using `client->request`, like so:

```php hidelines={1..2} nocheck
<?php
use Anthropic\Client;
$client = new Client();

$response = $client->request(
  method: "post",
  path: '/undocumented/endpoint',
  query: ['dog' => 'woof'],
  headers: ['useful-header' => 'interesting-value'],
  body: ['hello' => 'world']
);
```

## Platform integrations

<Note>
For detailed platform setup guides with code examples, see:
- [Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock)
- [Amazon Bedrock (legacy)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)
- [Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai)
- [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)
- [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)
</Note>

The PHP SDK supports the following platforms:

- **Bedrock:** `Anthropic\Bedrock\MantleClient`. Use `new MantleClient(awsRegion: ...)`.
- **Bedrock (legacy):** `Anthropic\Bedrock\Client`. Use `::fromEnvironment()` or `::withCredentials()`.
- **Vertex AI:** `Anthropic\Vertex\Client`. Use `::fromEnvironment()`.
- **Foundry:** `Anthropic\Foundry\Client`. Use `::withCredentials()`.
- **Claude Platform on AWS:** `Anthropic\Aws\Client` (requires `aws/aws-sdk-php` as a soft dependency). Use `new Anthropic\Aws\Client(workspaceId: ...)` or set `ANTHROPIC_AWS_WORKSPACE_ID`. Available in beta.

Use `MantleClient` for new projects; `Anthropic\Bedrock\Client` remains for existing applications using the Bedrock `InvokeModel` API.

## Semantic versioning

This package follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions. As the library is in initial development and has a major version of `0`, APIs may change at any time.

This package considers improvements to the (non-runtime) PHPDoc type definitions to be non-breaking changes.

## Additional resources

- [GitHub repository](https://github.com/anthropics/anthropic-sdk-php)
- [Packagist](https://packagist.org/packages/anthropic-ai/sdk)
- [API reference](/docs/en/api/overview)
- [Streaming Messages](/docs/en/build-with-claude/streaming)
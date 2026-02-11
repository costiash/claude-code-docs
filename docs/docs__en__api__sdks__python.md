# Python SDK

Install and configure the Anthropic Python SDK with sync and async client support

---

The Anthropic Python SDK provides convenient access to the Anthropic REST API from Python applications. It supports both synchronous and asynchronous operations, streaming, and integrations with AWS Bedrock and Google Vertex AI.

<Info>
For API feature documentation with code examples, see the [API reference](/docs/en/api/overview). This page covers Python-specific SDK features and configuration.
</Info>

## Installation

```bash
pip install anthropic
```

For platform-specific integrations, install with extras:

```bash
# For AWS Bedrock support
pip install anthropic[bedrock]

# For Google Vertex AI support
pip install anthropic[vertex]

# For improved async performance with aiohttp
pip install anthropic[aiohttp]
```

## Requirements

Python 3.9 or later is required.

## Usage

```python
import os
from anthropic import Anthropic

client = Anthropic(
    # This is the default and can be omitted
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude",
        }
    ],
    model="claude-opus-4-6",
)
print(message.content)
```

## Async usage

```python
import os
import asyncio
from anthropic import AsyncAnthropic

client = AsyncAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)


async def main() -> None:
    message = await client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Hello, Claude",
            }
        ],
        model="claude-opus-4-6",
    )
    print(message.content)


asyncio.run(main())
```

### Using aiohttp for better concurrency

For improved async performance, you can use the `aiohttp` HTTP backend instead of the default `httpx`:

```python
import os
import asyncio
from anthropic import AsyncAnthropic, DefaultAioHttpClient


async def main() -> None:
    async with AsyncAnthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
        http_client=DefaultAioHttpClient(),
    ) as client:
        message = await client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "Hello, Claude",
                }
            ],
            model="claude-opus-4-6",
        )
        print(message.content)


asyncio.run(main())
```

## Streaming responses

We provide support for streaming responses using Server-Sent Events (SSE).

```python
from anthropic import Anthropic

client = Anthropic()

stream = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude",
        }
    ],
    model="claude-opus-4-6",
    stream=True,
)
for event in stream:
    print(event.type)
```

### Streaming helpers

The SDK also provides streaming helpers that use context managers and provide access to the accumulated text and the final message:

```python
import asyncio
from anthropic import AsyncAnthropic

client = AsyncAnthropic()


async def main() -> None:
    async with client.messages.stream(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Say hello there!",
            }
        ],
        model="claude-opus-4-6",
    ) as stream:
        async for text in stream.text_stream:
            print(text, end="", flush=True)
        print()

        message = await stream.get_final_message()
        print(message.to_json())


asyncio.run(main())
```

Streaming with `client.messages.stream(...)` exposes various helpers including event handlers and accumulation.

Alternatively, you can use `client.messages.create({ ..., stream=True })` which only returns an iterator of the events in the stream and uses less memory (it does not build up a final message object for you).

## Token counting

You can see the exact usage for a given request through the `usage` response property:

```python
message = client.messages.create(...)
print(message.usage)
# Usage(input_tokens=25, output_tokens=13)
```

You can also count tokens before making a request:

```python
count = client.messages.count_tokens(
    model="claude-opus-4-6", messages=[{"role": "user", "content": "Hello, world"}]
)
print(count.input_tokens)  # 10
```

## Tool use

This SDK provides support for tool use, also known as function calling. More details can be found in the [tool use overview](/docs/en/agents-and-tools/tool-use/overview).

### Tool helpers

The SDK also provides helpers for easily defining and running tools as Python functions:

```python
import json
from anthropic import Anthropic

client = Anthropic()


def get_weather(location: str) -> str:
    """Get the weather for a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA
    """
    return json.dumps(
        {
            "location": location,
            "temperature": "68°F",
            "condition": "Sunny",
        }
    )


# Use the tool_runner to automatically handle tool calls
runner = client.beta.messages.tool_runner(
    max_tokens=1024,
    model="claude-opus-4-6",
    tools=[get_weather],
    messages=[
        {"role": "user", "content": "What is the weather in SF?"},
    ],
)
for message in runner:
    print(message)
```

## Message Batches

This SDK provides support for the [Message Batches API](/docs/en/build-with-claude/batch-processing) under `client.messages.batches`.

### Creating a batch

Message Batches takes an array of requests, where each object has a `custom_id` identifier and the same request `params` as the standard Messages API:

```python
client.messages.batches.create(
    requests=[
        {
            "custom_id": "my-first-request",
            "params": {
                "model": "claude-opus-4-6",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "Hello, world"}],
            },
        },
        {
            "custom_id": "my-second-request",
            "params": {
                "model": "claude-opus-4-6",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "Hi again, friend"}],
            },
        },
    ]
)
```

### Getting results from a batch

Once a Message Batch has been processed, indicated by `.processing_status == 'ended'`, you can access the results with `.batches.results()`:

```python
result_stream = client.messages.batches.results(batch_id)
for entry in result_stream:
    if entry.result.type == "succeeded":
        print(entry.result.message.content)
```

## File uploads

Request parameters that correspond to file uploads can be passed in many different forms:

- A `PathLike` object (e.g., `pathlib.Path`)
- A tuple of `(filename, content, content_type)`
- A `BinaryIO` file-like object
- The return value of the `toFile` helper

```python
from pathlib import Path
from anthropic import Anthropic

client = Anthropic()

# Upload using a file path
client.beta.files.upload(
    file=Path("/path/to/file"),
    betas=["files-api-2025-04-14"],
)

# Upload using bytes
client.beta.files.upload(
    file=("file.txt", b"my bytes", "text/plain"),
    betas=["files-api-2025-04-14"],
)
```

## Handling errors

When the library is unable to connect to the API, or if the API returns a non-success status code (i.e., 4xx or 5xx response), a subclass of `APIError` will be raised:

```python
import anthropic
from anthropic import Anthropic

client = Anthropic()

try:
    message = client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Hello, Claude",
            }
        ],
        model="claude-opus-4-6",
    )
except anthropic.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx
except anthropic.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except anthropic.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type |
|-------------|-----------|
| 400 | `BadRequestError` |
| 401 | `AuthenticationError` |
| 403 | `PermissionDeniedError` |
| 404 | `NotFoundError` |
| 422 | `UnprocessableEntityError` |
| 429 | `RateLimitError` |
| >=500 | `InternalServerError` |
| N/A | `APIConnectionError` |

## Request IDs

> For more information on debugging requests, see the [errors documentation](/docs/en/api/errors#request-id).

All object responses in the SDK provide a `_request_id` property which is added from the `request-id` response header so that you can quickly log failing requests and report them back to Anthropic.

```python
message = client.messages.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-6",
)
print(message._request_id)  # e.g., req_018EeWyXxfu5pfWkrYcMdjWG
```

## Retries

Certain errors will be automatically retried 2 times by default, with a short exponential backoff. Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict, 429 Rate Limit, and >=500 Internal errors will all be retried by default.

You can use the `max_retries` option to configure or disable this:

```python
from anthropic import Anthropic

# Configure the default for all requests:
client = Anthropic(
    max_retries=0,  # default is 2
)

# Or, configure per-request:
client.with_options(max_retries=5).messages.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-6",
)
```

## Timeouts

By default requests time out after 10 minutes. You can configure this with a `timeout` option, which accepts a float or an `httpx.Timeout` object:

```python
import httpx
from anthropic import Anthropic

# Configure the default for all requests:
client = Anthropic(
    timeout=20.0,  # 20 seconds (default is 10 minutes)
)

# More granular control:
client = Anthropic(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).messages.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-6",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests which time out will be [retried twice by default](#retries).

## Long requests

<Warning>
We highly encourage you to use the streaming [Messages API](#streaming-responses) for longer running requests.
</Warning>

We do not recommend setting a large `max_tokens` value without using streaming. Some networks may drop idle connections after a certain period of time, which can cause the request to fail or [timeout](#timeouts) without receiving a response from Anthropic.

The SDK will throw an error if a non-streaming request is expected to take longer than approximately 10 minutes. Passing `stream=True` or overriding the `timeout` option at the client or request level disables this error.

An expected request latency longer than the [timeout](#timeouts) for a non-streaming request will result in the client terminating the connection and retrying without receiving a response.

## Auto-pagination

List methods in the Claude API are paginated. You can use the `for` syntax to iterate through items across all pages:

```python
from anthropic import Anthropic

client = Anthropic()

all_batches = []
# Automatically fetches more pages as needed.
for batch in client.messages.batches.list(limit=20):
    all_batches.append(batch)
print(all_batches)
```

For async iteration:

```python
import asyncio
from anthropic import AsyncAnthropic

client = AsyncAnthropic()


async def main() -> None:
    all_batches = []
    async for batch in client.messages.batches.list(limit=20):
        all_batches.append(batch)
    print(all_batches)


asyncio.run(main())
```

Alternatively, you can request a single page at a time:

```python
first_page = await client.messages.batches.list(limit=20)

if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.data)}")
```

## Default Headers

We automatically send the `anthropic-version` header set to `2023-06-01`.

If you need to, you can override it by setting default headers on a per-request basis.

Be aware that doing so may result in incorrect types and other unexpected or undefined behavior in the SDK.

```python
from anthropic import Anthropic

client = Anthropic()

client.messages.with_raw_response.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-6",
    extra_headers={"anthropic-version": "My-Custom-Value"},
)
```

## Type system

### Request parameters

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also have helper methods for things like serializing back into JSON ([`v1`](https://docs.pydantic.dev/1.10/usage/models/), [`v2`](https://docs.pydantic.dev/latest/concepts/serialization/)).

### Response models

To convert a Pydantic model to a dictionary, use the helper methods:

```python
message = client.messages.create(...)

# Convert to JSON string
json_str = message.to_json()

# Convert to dictionary
data = message.to_dict()
```

### Handling null vs missing fields

In responses, you can distinguish between fields that are explicitly `null` versus fields that were not returned (missing):

```python
if response.my_field is None:
    if "my_field" not in response.model_fields_set:
        print("field was not in the response")
    else:
        print("field was null")
```

## Advanced usage

### Accessing raw response data (e.g., headers)

The "raw" `Response` returned by `httpx` can be accessed via the `.with_raw_response` property on the client. This is useful for accessing response headers or other metadata:

```python
from anthropic import Anthropic

client = Anthropic()

response = client.messages.with_raw_response.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-6",
)

print(response.headers.get("x-request-id"))
message = (
    response.parse()
)  # get the object that `messages.create()` would have returned
print(message.content)
```

These methods return an `APIResponse` object.

### Logging

The SDK uses the standard library `logging` module.

You can enable logging by setting the environment variable `ANTHROPIC_LOG` to one of `debug`, `info`, `warn`, or `off`:

```bash
export ANTHROPIC_LOG=debug
```

### Making custom/undocumented requests

This library is typed for convenient access to the documented API. If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can use `client.get`, `client.post`, and other HTTP verbs. Options on the client, such as retries, will be respected when making these requests.

```python
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.json())
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You can also get all extra fields on the Pydantic model as a dict with `response.model_extra`.

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including support for proxies and transports:

```python
import httpx
from anthropic import Anthropic, DefaultHttpxClient

client = Anthropic(
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

<Note>
Use `DefaultHttpxClient` and `DefaultAsyncHttpxClient` instead of raw `httpx.Client` and `httpx.AsyncClient` to ensure the SDK's default configuration (timeouts, connection limits, etc.) is preserved.
</Note>

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```python
from anthropic import Anthropic

with Anthropic() as client:
    message = client.messages.create(...)

# HTTP client is automatically closed
```

## Beta features

We introduce beta features before they are generally available to get early feedback and test new functionality. You can check the availability of all of Claude's capabilities and tools in the [build with Claude overview](/docs/en/build-with-claude/overview).

You can access most beta API features through the `beta` property of the client. To enable a particular beta feature, you need to add the appropriate [beta header](/docs/en/api/beta-headers) to the `betas` field when creating a message.

For example, to use code execution:

```python
from anthropic import Anthropic

client = Anthropic()

response = client.beta.messages.create(
    max_tokens=1024,
    model="claude-opus-4-6",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What's 4242424242 * 4242424242?",
                },
            ],
        },
    ],
    tools=[
        {
            "name": "code_execution",
            "type": "code_execution_20250522",
        },
    ],
    betas=["code-execution-2025-05-22"],
)
```

## Platform integrations

<Note>
For detailed platform setup guides, see:
- [Amazon Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock)
- [Google Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai)
</Note>

### Amazon Bedrock

```python
from anthropic import AnthropicBedrock

client = AnthropicBedrock()

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello!",
        }
    ],
    model="anthropic.claude-opus-4-6-v1",
)
print(message)
```

For a full list of available Bedrock models, see the [Amazon Bedrock documentation](/docs/en/build-with-claude/claude-on-amazon-bedrock).

You can also configure AWS credentials explicitly:

```python
client = AnthropicBedrock(
    aws_region="us-east-1",
    aws_access_key="...",
    aws_secret_key="...",
    # Optional
    aws_session_token="...",
    aws_profile="my-profile",
)
```

### Google Vertex AI

```python
from anthropic import AnthropicVertex

client = AnthropicVertex()

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello!",
        }
    ],
)
print(message)
```

For a full list of available Vertex models, see the [Google Vertex AI documentation](/docs/en/build-with-claude/claude-on-vertex-ai).

## Additional resources

- [GitHub repository](https://github.com/anthropics/anthropic-sdk-python)
- [API reference](/docs/en/api/overview)
- [Streaming guide](/docs/en/build-with-claude/streaming)
- [Tool use guide](/docs/en/agents-and-tools/tool-use/overview)
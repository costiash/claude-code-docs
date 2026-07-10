# Memories

## Create a memory

`$client->beta->memoryStores->memories->create(string memoryStoreID, ?string content, string path, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas): ManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

### Parameters

- `memoryStoreID: string`

- `content: string`

  UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

- `path: string`

  Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

- `view?:optional ManagedAgentsMemoryView`

  Query parameter for view

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsMemory`

  - `string id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `string contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `int contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string memoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `string memoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `string path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?string content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemory = $client->beta->memoryStores->memories->create(
  'memory_store_id',
  content: 'content',
  path: 'xx',
  view: ManagedAgentsMemoryView::BASIC,
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsMemory);
```

#### Response

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## List memories

`$client->beta->memoryStores->memories->list(string memoryStoreID, ?int depth, ?int limit, ?string page, ?string pathPrefix, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas): PageCursor<ManagedAgentsMemoryListItem>`

**get** `/v1/memory_stores/{memory_store_id}/memories`

List memories

### Parameters

- `memoryStoreID: string`

- `depth?:optional int`

  `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

- `limit?:optional int`

  Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

- `page?:optional string`

  Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `pathPrefix?:optional string`

  Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

- `view?:optional ManagedAgentsMemoryView`

  Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsMemoryListItem`

  - `ManagedAgentsMemory`

    - `string id`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `string contentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `int contentSizeBytes`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string memoryStoreID`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `string memoryVersionID`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `string path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `Type type`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

    - `?string content`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `ManagedAgentsMemoryPrefix`

    - `string path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->memoryStores->memories->list(
  'memory_store_id',
  depth: 0,
  limit: 0,
  page: 'page',
  pathPrefix: 'path_prefix',
  view: ManagedAgentsMemoryView::BASIC,
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_store_id": "memory_store_id",
      "memory_version_id": "memory_version_id",
      "path": "path",
      "type": "memory",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "content": "content"
    }
  ],
  "next_page": "next_page"
}
```

## Retrieve a memory

`$client->beta->memoryStores->memories->retrieve(string memoryID, string memoryStoreID, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas): ManagedAgentsMemory`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

### Parameters

- `memoryStoreID: string`

- `memoryID: string`

- `view?:optional ManagedAgentsMemoryView`

  Query parameter for view

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsMemory`

  - `string id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `string contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `int contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string memoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `string memoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `string path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?string content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemory = $client->beta->memoryStores->memories->retrieve(
  'memory_id',
  memoryStoreID: 'memory_store_id',
  view: ManagedAgentsMemoryView::BASIC,
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsMemory);
```

#### Response

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## Update a memory

`$client->beta->memoryStores->memories->update(string memoryID, string memoryStoreID, ?ManagedAgentsMemoryView view, ?string content, ?string path, ?ManagedAgentsPrecondition precondition, ?list<AnthropicBeta> betas): ManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

### Parameters

- `memoryStoreID: string`

- `memoryID: string`

- `view?:optional ManagedAgentsMemoryView`

  Query parameter for view

- `content?:optional string`

  New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

- `path?:optional string`

  New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

- `precondition?:optional ManagedAgentsPrecondition`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsMemory`

  - `string id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `string contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `int contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string memoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `string memoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `string path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?string content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemory = $client->beta->memoryStores->memories->update(
  'memory_id',
  memoryStoreID: 'memory_store_id',
  view: ManagedAgentsMemoryView::BASIC,
  content: 'content',
  path: 'xx',
  precondition: [
    'type' => 'content_sha256', 'contentSha256' => 'content_sha256'
  ],
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsMemory);
```

#### Response

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## Delete a memory

`$client->beta->memoryStores->memories->delete(string memoryID, string memoryStoreID, ?string expectedContentSha256, ?list<AnthropicBeta> betas): ManagedAgentsDeletedMemory`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

### Parameters

- `memoryStoreID: string`

- `memoryID: string`

- `expectedContentSha256?:optional string`

  Query parameter for expected_content_sha256

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `ManagedAgentsDeletedMemory`

  - `string id`

    ID of the deleted memory (a `mem_...` value).

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedMemory = $client->beta->memoryStores->memories->delete(
  'memory_id',
  memoryStoreID: 'memory_store_id',
  expectedContentSha256: 'expected_content_sha256',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeletedMemory);
```

#### Response

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

## Domain Types

### Beta Managed Agents Conflict Error

- `ManagedAgentsConflictError`

  - `Type type`

  - `?string message`

### Beta Managed Agents Content Sha256 Precondition

- `ManagedAgentsContentSha256Precondition`

  - `Type type`

  - `?string contentSha256`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `ManagedAgentsDeletedMemory`

  - `string id`

    ID of the deleted memory (a `mem_...` value).

  - `Type type`

### Beta Managed Agents Error

- `ManagedAgentsError`

  - `BetaInvalidRequestError`

    - `string message`

    - `"invalid_request_error" type`

  - `BetaAuthenticationError`

    - `string message`

    - `"authentication_error" type`

  - `BetaBillingError`

    - `string message`

    - `"billing_error" type`

  - `BetaPermissionError`

    - `string message`

    - `"permission_error" type`

  - `BetaNotFoundError`

    - `string message`

    - `"not_found_error" type`

  - `BetaRateLimitError`

    - `string message`

    - `"rate_limit_error" type`

  - `BetaGatewayTimeoutError`

    - `string message`

    - `"timeout_error" type`

  - `BetaAPIError`

    - `string message`

    - `"api_error" type`

  - `BetaOverloadedError`

    - `string message`

    - `"overloaded_error" type`

  - `ManagedAgentsMemoryPreconditionFailedError`

    - `Type type`

    - `?string message`

  - `ManagedAgentsMemoryPathConflictError`

    - `Type type`

    - `?string conflictingMemoryID`

    - `?string conflictingPath`

    - `?string message`

  - `ManagedAgentsConflictError`

    - `Type type`

    - `?string message`

### Beta Managed Agents Memory

- `ManagedAgentsMemory`

  - `string id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `string contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `int contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string memoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `string memoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `string path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?string content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Beta Managed Agents Memory List Item

- `ManagedAgentsMemoryListItem`

  - `ManagedAgentsMemory`

    - `string id`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `string contentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `int contentSizeBytes`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string memoryStoreID`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `string memoryVersionID`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `string path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `Type type`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

    - `?string content`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `ManagedAgentsMemoryPrefix`

    - `string path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `Type type`

### Beta Managed Agents Memory Path Conflict Error

- `ManagedAgentsMemoryPathConflictError`

  - `Type type`

  - `?string conflictingMemoryID`

  - `?string conflictingPath`

  - `?string message`

### Beta Managed Agents Memory Precondition Failed Error

- `ManagedAgentsMemoryPreconditionFailedError`

  - `Type type`

  - `?string message`

### Beta Managed Agents Memory Prefix

- `ManagedAgentsMemoryPrefix`

  - `string path`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

  - `Type type`

### Beta Managed Agents Memory View

- `ManagedAgentsMemoryView`

  - `"basic"`

  - `"full"`

### Beta Managed Agents Precondition

- `ManagedAgentsPrecondition`

  - `Type type`

  - `?string contentSha256`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

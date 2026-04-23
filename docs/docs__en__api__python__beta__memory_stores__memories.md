# Memories

## Create

`beta.memory_stores.memories.create(strmemory_store_id, MemoryCreateParams**kwargs)  -> BetaManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories`

CreateMemory

### Parameters

- `memory_store_id: str`

- `content: Optional[str]`

- `path: str`

- `view: Optional[BetaManagedAgentsMemoryView]`

  Query parameter for view

  - `"basic"`

  - `"full"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 19 more]`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

### Returns

- `class BetaManagedAgentsMemory: …`

  - `id: str`

  - `content_sha256: str`

  - `content_size_bytes: int`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_store_id: str`

  - `memory_version_id: str`

  - `path: str`

  - `type: Literal["memory"]`

    - `"memory"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `content: Optional[str]`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_memory = client.beta.memory_stores.memories.create(
    memory_store_id="memory_store_id",
    content="content",
    path="xx",
)
print(beta_managed_agents_memory.id)
```

## List

`beta.memory_stores.memories.list(strmemory_store_id, MemoryListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsMemoryListItem]`

**get** `/v1/memory_stores/{memory_store_id}/memories`

ListMemories

### Parameters

- `memory_store_id: str`

- `depth: Optional[int]`

  Query parameter for depth

- `limit: Optional[int]`

  Query parameter for limit

- `order: Optional[Literal["asc", "desc"]]`

  Query parameter for order

  - `"asc"`

  - `"desc"`

- `order_by: Optional[str]`

  Query parameter for order_by

- `page: Optional[str]`

  Query parameter for page

- `path_prefix: Optional[str]`

  Optional path prefix filter (raw string-prefix match; include a trailing slash for directory-scoped lists). This value appears in request URLs. Do not include secrets or personally identifiable information.

- `view: Optional[BetaManagedAgentsMemoryView]`

  Query parameter for view

  - `"basic"`

  - `"full"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 19 more]`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

### Returns

- `BetaManagedAgentsMemoryListItem`

  - `class BetaManagedAgentsMemory: …`

    - `id: str`

    - `content_sha256: str`

    - `content_size_bytes: int`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `memory_store_id: str`

    - `memory_version_id: str`

    - `path: str`

    - `type: Literal["memory"]`

      - `"memory"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

    - `content: Optional[str]`

  - `class BetaManagedAgentsMemoryPrefix: …`

    - `path: str`

    - `type: Literal["memory_prefix"]`

      - `"memory_prefix"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.memory_stores.memories.list(
    memory_store_id="memory_store_id",
)
page = page.data[0]
print(page)
```

## Retrieve

`beta.memory_stores.memories.retrieve(strmemory_id, MemoryRetrieveParams**kwargs)  -> BetaManagedAgentsMemory`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

GetMemory

### Parameters

- `memory_store_id: str`

- `memory_id: str`

- `view: Optional[BetaManagedAgentsMemoryView]`

  Query parameter for view

  - `"basic"`

  - `"full"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 19 more]`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

### Returns

- `class BetaManagedAgentsMemory: …`

  - `id: str`

  - `content_sha256: str`

  - `content_size_bytes: int`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_store_id: str`

  - `memory_version_id: str`

  - `path: str`

  - `type: Literal["memory"]`

    - `"memory"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `content: Optional[str]`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_memory = client.beta.memory_stores.memories.retrieve(
    memory_id="memory_id",
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_memory.id)
```

## Update

`beta.memory_stores.memories.update(strmemory_id, MemoryUpdateParams**kwargs)  -> BetaManagedAgentsMemory`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

UpdateMemory

### Parameters

- `memory_store_id: str`

- `memory_id: str`

- `view: Optional[BetaManagedAgentsMemoryView]`

  Query parameter for view

  - `"basic"`

  - `"full"`

- `content: Optional[str]`

- `path: Optional[str]`

- `precondition: Optional[BetaManagedAgentsPreconditionParam]`

  - `type: Literal["content_sha256"]`

    - `"content_sha256"`

  - `content_sha256: Optional[str]`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 19 more]`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

### Returns

- `class BetaManagedAgentsMemory: …`

  - `id: str`

  - `content_sha256: str`

  - `content_size_bytes: int`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_store_id: str`

  - `memory_version_id: str`

  - `path: str`

  - `type: Literal["memory"]`

    - `"memory"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `content: Optional[str]`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_memory = client.beta.memory_stores.memories.update(
    memory_id="memory_id",
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_memory.id)
```

## Delete

`beta.memory_stores.memories.delete(strmemory_id, MemoryDeleteParams**kwargs)  -> BetaManagedAgentsDeletedMemory`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

DeleteMemory

### Parameters

- `memory_store_id: str`

- `memory_id: str`

- `expected_content_sha256: Optional[str]`

  Query parameter for expected_content_sha256

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 19 more]`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"advisor-tool-2026-03-01"`

### Returns

- `class BetaManagedAgentsDeletedMemory: …`

  - `id: str`

  - `type: Literal["memory_deleted"]`

    - `"memory_deleted"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deleted_memory = client.beta.memory_stores.memories.delete(
    memory_id="memory_id",
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_deleted_memory.id)
```

## Domain Types

### Beta Managed Agents Content Sha256 Precondition

- `class BetaManagedAgentsContentSha256Precondition: …`

  - `type: Literal["content_sha256"]`

    - `"content_sha256"`

  - `content_sha256: Optional[str]`

### Beta Managed Agents Deleted Memory

- `class BetaManagedAgentsDeletedMemory: …`

  - `id: str`

  - `type: Literal["memory_deleted"]`

    - `"memory_deleted"`

### Beta Managed Agents Memory

- `class BetaManagedAgentsMemory: …`

  - `id: str`

  - `content_sha256: str`

  - `content_size_bytes: int`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_store_id: str`

  - `memory_version_id: str`

  - `path: str`

  - `type: Literal["memory"]`

    - `"memory"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `content: Optional[str]`

### Beta Managed Agents Memory List Item

- `BetaManagedAgentsMemoryListItem`

  - `class BetaManagedAgentsMemory: …`

    - `id: str`

    - `content_sha256: str`

    - `content_size_bytes: int`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `memory_store_id: str`

    - `memory_version_id: str`

    - `path: str`

    - `type: Literal["memory"]`

      - `"memory"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

    - `content: Optional[str]`

  - `class BetaManagedAgentsMemoryPrefix: …`

    - `path: str`

    - `type: Literal["memory_prefix"]`

      - `"memory_prefix"`

### Beta Managed Agents Memory Path Conflict Error

- `class BetaManagedAgentsMemoryPathConflictError: …`

  - `type: Literal["memory_path_conflict_error"]`

    - `"memory_path_conflict_error"`

  - `conflicting_memory_id: Optional[str]`

  - `conflicting_path: Optional[str]`

  - `message: Optional[str]`

### Beta Managed Agents Memory Precondition Failed Error

- `class BetaManagedAgentsMemoryPreconditionFailedError: …`

  - `type: Literal["memory_precondition_failed_error"]`

    - `"memory_precondition_failed_error"`

  - `message: Optional[str]`

### Beta Managed Agents Memory Prefix

- `class BetaManagedAgentsMemoryPrefix: …`

  - `path: str`

  - `type: Literal["memory_prefix"]`

    - `"memory_prefix"`

### Beta Managed Agents Memory View

- `Literal["basic", "full"]`

  MemoryView enum

  - `"basic"`

  - `"full"`

### Beta Managed Agents Precondition

- `class BetaManagedAgentsPrecondition: …`

  - `type: Literal["content_sha256"]`

    - `"content_sha256"`

  - `content_sha256: Optional[str]`

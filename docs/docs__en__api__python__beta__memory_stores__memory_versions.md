# Memory Versions

## List

`beta.memory_stores.memory_versions.list(strmemory_store_id, MemoryVersionListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsMemoryVersion]`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

ListMemoryVersions

### Parameters

- `memory_store_id: str`

- `api_key_id: Optional[str]`

  Query parameter for api_key_id

- `created_at_gte: Optional[Union[str, datetime]]`

  Return versions created at or after this time (inclusive).

- `created_at_lte: Optional[Union[str, datetime]]`

  Return versions created at or before this time (inclusive).

- `limit: Optional[int]`

  Query parameter for limit

- `memory_id: Optional[str]`

  Query parameter for memory_id

- `operation: Optional[BetaManagedAgentsMemoryVersionOperation]`

  Query parameter for operation

  - `"created"`

  - `"modified"`

  - `"deleted"`

- `page: Optional[str]`

  Query parameter for page

- `session_id: Optional[str]`

  Query parameter for session_id

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

- `class BetaManagedAgentsMemoryVersion: …`

  - `id: str`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_id: str`

  - `memory_store_id: str`

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: Literal["memory_version"]`

    - `"memory_version"`

  - `content: Optional[str]`

  - `content_sha256: Optional[str]`

  - `content_size_bytes: Optional[int]`

  - `created_by: Optional[BetaManagedAgentsActor]`

    - `class BetaManagedAgentsSessionActor: …`

      - `session_id: str`

      - `type: Literal["session_actor"]`

        - `"session_actor"`

    - `class BetaManagedAgentsAPIActor: …`

      - `api_key_id: str`

      - `type: Literal["api_actor"]`

        - `"api_actor"`

    - `class BetaManagedAgentsUserActor: …`

      - `type: Literal["user_actor"]`

        - `"user_actor"`

      - `user_id: str`

  - `path: Optional[str]`

  - `redacted_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `redacted_by: Optional[BetaManagedAgentsActor]`

    - `class BetaManagedAgentsSessionActor: …`

      - `session_id: str`

      - `type: Literal["session_actor"]`

        - `"session_actor"`

    - `class BetaManagedAgentsAPIActor: …`

      - `api_key_id: str`

      - `type: Literal["api_actor"]`

        - `"api_actor"`

    - `class BetaManagedAgentsUserActor: …`

      - `type: Literal["user_actor"]`

        - `"user_actor"`

      - `user_id: str`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.memory_stores.memory_versions.list(
    memory_store_id="memory_store_id",
)
page = page.data[0]
print(page.id)
```

## Retrieve

`beta.memory_stores.memory_versions.retrieve(strmemory_version_id, MemoryVersionRetrieveParams**kwargs)  -> BetaManagedAgentsMemoryVersion`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

GetMemoryVersion

### Parameters

- `memory_store_id: str`

- `memory_version_id: str`

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

- `class BetaManagedAgentsMemoryVersion: …`

  - `id: str`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_id: str`

  - `memory_store_id: str`

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: Literal["memory_version"]`

    - `"memory_version"`

  - `content: Optional[str]`

  - `content_sha256: Optional[str]`

  - `content_size_bytes: Optional[int]`

  - `created_by: Optional[BetaManagedAgentsActor]`

    - `class BetaManagedAgentsSessionActor: …`

      - `session_id: str`

      - `type: Literal["session_actor"]`

        - `"session_actor"`

    - `class BetaManagedAgentsAPIActor: …`

      - `api_key_id: str`

      - `type: Literal["api_actor"]`

        - `"api_actor"`

    - `class BetaManagedAgentsUserActor: …`

      - `type: Literal["user_actor"]`

        - `"user_actor"`

      - `user_id: str`

  - `path: Optional[str]`

  - `redacted_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `redacted_by: Optional[BetaManagedAgentsActor]`

    - `class BetaManagedAgentsSessionActor: …`

      - `session_id: str`

      - `type: Literal["session_actor"]`

        - `"session_actor"`

    - `class BetaManagedAgentsAPIActor: …`

      - `api_key_id: str`

      - `type: Literal["api_actor"]`

        - `"api_actor"`

    - `class BetaManagedAgentsUserActor: …`

      - `type: Literal["user_actor"]`

        - `"user_actor"`

      - `user_id: str`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_memory_version = client.beta.memory_stores.memory_versions.retrieve(
    memory_version_id="memory_version_id",
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_memory_version.id)
```

## Redact

`beta.memory_stores.memory_versions.redact(strmemory_version_id, MemoryVersionRedactParams**kwargs)  -> BetaManagedAgentsMemoryVersion`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

RedactMemoryVersion

### Parameters

- `memory_store_id: str`

- `memory_version_id: str`

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

- `class BetaManagedAgentsMemoryVersion: …`

  - `id: str`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_id: str`

  - `memory_store_id: str`

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: Literal["memory_version"]`

    - `"memory_version"`

  - `content: Optional[str]`

  - `content_sha256: Optional[str]`

  - `content_size_bytes: Optional[int]`

  - `created_by: Optional[BetaManagedAgentsActor]`

    - `class BetaManagedAgentsSessionActor: …`

      - `session_id: str`

      - `type: Literal["session_actor"]`

        - `"session_actor"`

    - `class BetaManagedAgentsAPIActor: …`

      - `api_key_id: str`

      - `type: Literal["api_actor"]`

        - `"api_actor"`

    - `class BetaManagedAgentsUserActor: …`

      - `type: Literal["user_actor"]`

        - `"user_actor"`

      - `user_id: str`

  - `path: Optional[str]`

  - `redacted_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `redacted_by: Optional[BetaManagedAgentsActor]`

    - `class BetaManagedAgentsSessionActor: …`

      - `session_id: str`

      - `type: Literal["session_actor"]`

        - `"session_actor"`

    - `class BetaManagedAgentsAPIActor: …`

      - `api_key_id: str`

      - `type: Literal["api_actor"]`

        - `"api_actor"`

    - `class BetaManagedAgentsUserActor: …`

      - `type: Literal["user_actor"]`

        - `"user_actor"`

      - `user_id: str`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_memory_version = client.beta.memory_stores.memory_versions.redact(
    memory_version_id="memory_version_id",
    memory_store_id="memory_store_id",
)
print(beta_managed_agents_memory_version.id)
```

## Domain Types

### Beta Managed Agents Actor

- `BetaManagedAgentsActor`

  - `class BetaManagedAgentsSessionActor: …`

    - `session_id: str`

    - `type: Literal["session_actor"]`

      - `"session_actor"`

  - `class BetaManagedAgentsAPIActor: …`

    - `api_key_id: str`

    - `type: Literal["api_actor"]`

      - `"api_actor"`

  - `class BetaManagedAgentsUserActor: …`

    - `type: Literal["user_actor"]`

      - `"user_actor"`

    - `user_id: str`

### Beta Managed Agents API Actor

- `class BetaManagedAgentsAPIActor: …`

  - `api_key_id: str`

  - `type: Literal["api_actor"]`

    - `"api_actor"`

### Beta Managed Agents Memory Version

- `class BetaManagedAgentsMemoryVersion: …`

  - `id: str`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `memory_id: str`

  - `memory_store_id: str`

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    MemoryVersionOperation enum

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: Literal["memory_version"]`

    - `"memory_version"`

  - `content: Optional[str]`

  - `content_sha256: Optional[str]`

  - `content_size_bytes: Optional[int]`

  - `created_by: Optional[BetaManagedAgentsActor]`

    - `class BetaManagedAgentsSessionActor: …`

      - `session_id: str`

      - `type: Literal["session_actor"]`

        - `"session_actor"`

    - `class BetaManagedAgentsAPIActor: …`

      - `api_key_id: str`

      - `type: Literal["api_actor"]`

        - `"api_actor"`

    - `class BetaManagedAgentsUserActor: …`

      - `type: Literal["user_actor"]`

        - `"user_actor"`

      - `user_id: str`

  - `path: Optional[str]`

  - `redacted_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `redacted_by: Optional[BetaManagedAgentsActor]`

    - `class BetaManagedAgentsSessionActor: …`

      - `session_id: str`

      - `type: Literal["session_actor"]`

        - `"session_actor"`

    - `class BetaManagedAgentsAPIActor: …`

      - `api_key_id: str`

      - `type: Literal["api_actor"]`

        - `"api_actor"`

    - `class BetaManagedAgentsUserActor: …`

      - `type: Literal["user_actor"]`

        - `"user_actor"`

      - `user_id: str`

### Beta Managed Agents Memory Version Operation

- `Literal["created", "modified", "deleted"]`

  MemoryVersionOperation enum

  - `"created"`

  - `"modified"`

  - `"deleted"`

### Beta Managed Agents Session Actor

- `class BetaManagedAgentsSessionActor: …`

  - `session_id: str`

  - `type: Literal["session_actor"]`

    - `"session_actor"`

### Beta Managed Agents User Actor

- `class BetaManagedAgentsUserActor: …`

  - `type: Literal["user_actor"]`

    - `"user_actor"`

  - `user_id: str`

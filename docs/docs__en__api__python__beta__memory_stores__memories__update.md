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

## List

`beta.memory_stores.list(MemoryStoreListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsMemoryStore]`

**get** `/v1/memory_stores`

ListMemoryStores

### Parameters

- `created_at_gte: Optional[Union[str, datetime]]`

  Return stores created at or after this time (inclusive).

- `created_at_lte: Optional[Union[str, datetime]]`

  Return stores created at or before this time (inclusive).

- `include_archived: Optional[bool]`

  Query parameter for include_archived

- `limit: Optional[int]`

  Query parameter for limit

- `page: Optional[str]`

  Query parameter for page

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

- `class BetaManagedAgentsMemoryStore: …`

  - `id: str`

  - `type: Literal["memory_store"]`

    - `"memory_store"`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `description: Optional[str]`

  - `metadata: Optional[Dict[str, str]]`

  - `name: Optional[str]`

  - `updated_at: Optional[datetime]`

    A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.memory_stores.list()
page = page.data[0]
print(page.id)
```

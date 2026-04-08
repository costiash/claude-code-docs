## List

`beta.vaults.list(VaultListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsVault]`

**get** `/v1/vaults`

List Vaults

### Parameters

- `include_archived: Optional[bool]`

  Whether to include archived vaults in the results.

- `limit: Optional[int]`

  Maximum number of vaults to return per page. Defaults to 20, maximum 100.

- `page: Optional[str]`

  Opaque pagination token from a previous `list_vaults` response.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 18 more]`

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

### Returns

- `class BetaManagedAgentsVault: …`

  A vault that stores credentials for use by agents during sessions.

  - `id: str`

    Unique identifier for the vault.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: str`

    Human-readable name for the vault.

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata attached to the vault.

  - `type: Literal["vault"]`

    - `"vault"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.vaults.list()
page = page.data[0]
print(page.id)
```

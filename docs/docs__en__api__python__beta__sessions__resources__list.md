## List

`beta.sessions.resources.list(strsession_id, ResourceListParams**kwargs)  -> SyncPageCursor[BetaManagedAgentsSessionResource]`

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Parameters

- `session_id: str`

- `limit: Optional[int]`

  Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

- `page: Optional[str]`

  Opaque cursor from a previous response's next_page field.

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

- `BetaManagedAgentsSessionResource`

  A memory store attached to an agent session.

  - `class BetaManagedAgentsGitHubRepositoryResource: …`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `mount_path: str`

    - `type: Literal["github_repository"]`

      - `"github_repository"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

    - `url: str`

    - `checkout: Optional[Checkout]`

      - `class BetaManagedAgentsBranchCheckout: …`

        - `name: str`

          Branch name to check out.

        - `type: Literal["branch"]`

          - `"branch"`

      - `class BetaManagedAgentsCommitCheckout: …`

        - `sha: str`

          Full commit SHA to check out.

        - `type: Literal["commit"]`

          - `"commit"`

  - `class BetaManagedAgentsFileResource: …`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

    - `file_id: str`

    - `mount_path: str`

    - `type: Literal["file"]`

      - `"file"`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsMemoryStoreResource: …`

    A memory store attached to an agent session.

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: Literal["memory_store"]`

      - `"memory_store"`

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: Optional[str]`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `mount_path: Optional[str]`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: Optional[str]`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.sessions.resources.list(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page)
```

## Retrieve

`$ ant beta:sessions:resources retrieve`

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--resource-id: string`

  Path param: Path parameter resource_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSessionResourceGetResponse: BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource or BetaManagedAgentsMemoryStoreResource`

  The requested session resource.

  - `beta_managed_agents_github_repository_resource: object { id, created_at, mount_path, 4 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `mount_path: string`

    - `type: "github_repository"`

      - `"github_repository"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `url: string`

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      - `beta_managed_agents_branch_checkout: object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `beta_managed_agents_commit_checkout: object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

  - `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

      - `"file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_memory_store_resource: object { memory_store_id, type, access, 4 more }`

    A memory store attached to an agent session.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

      - `"memory_store"`

    - `access: optional "read_write" or "read_only"`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: optional string`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: optional string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `mount_path: optional string`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: optional string`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```cli
ant beta:sessions:resources retrieve \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht
```

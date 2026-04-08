# Resources

## Add

`$ ant beta:sessions:resources add`

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--file-id: string`

  Body param: ID of a previously uploaded file.

- `--type: "file"`

  Body param

- `--mount-path: optional string`

  Body param: Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

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

### Example

```cli
ant beta:sessions:resources add \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --file-id file_011CNha8iCJcU1wXNR6q4V8w \
  --type file
```

## List

`$ ant beta:sessions:resources list`

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--limit: optional number`

  Query param: Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

- `--page: optional string`

  Query param: Opaque cursor from a previous response's next_page field.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListSessionResources: object { data, next_page }`

  Paginated list of resources attached to a session.

  - `data: array of BetaManagedAgentsSessionResource`

    Resources for the session, ordered by `created_at`.

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

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

### Example

```cli
ant beta:sessions:resources list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

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

- `BetaSessionResourceGetResponse: BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource`

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

### Example

```cli
ant beta:sessions:resources retrieve \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht
```

## Update

`$ ant beta:sessions:resources update`

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--resource-id: string`

  Path param: Path parameter resource_id

- `--authorization-token: string`

  Body param: New authorization token for the resource. Currently only `github_repository` resources support token rotation.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSessionResourceUpdateResponse: BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource`

  The updated session resource.

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

### Example

```cli
ant beta:sessions:resources update \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht \
  --authorization-token ghp_exampletoken
```

## Delete

`$ ant beta:sessions:resources delete`

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--resource-id: string`

  Path param: Path parameter resource_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_delete_session_resource: object { id, type }`

  Confirmation of resource deletion.

  - `id: string`

  - `type: "session_resource_deleted"`

    - `"session_resource_deleted"`

### Example

```cli
ant beta:sessions:resources delete \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `beta_managed_agents_delete_session_resource: object { id, type }`

  Confirmation of resource deletion.

  - `id: string`

  - `type: "session_resource_deleted"`

    - `"session_resource_deleted"`

### Beta Managed Agents File Resource

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

### Beta Managed Agents GitHub Repository Resource

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

### Beta Managed Agents Session Resource

- `beta_managed_agents_session_resource: BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource`

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

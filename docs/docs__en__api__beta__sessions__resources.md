# Resources

## Add

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Path Parameters

- `session_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 18 more`

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

### Body Parameters

- `file_id: string`

  ID of a previously uploaded file.

- `type: "file"`

  - `"file"`

- `mount_path: optional string`

  Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Returns

- `BetaManagedAgentsFileResource = object { id, created_at, file_id, 3 more }`

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

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "type": "file"
        }'
```

## List

**get** `/v1/sessions/{session_id}/resources`

List Session Resources

### Path Parameters

- `session_id: string`

### Query Parameters

- `limit: optional number`

  Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 18 more`

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

- `data: array of BetaManagedAgentsSessionResource`

  Resources for the session, ordered by `created_at`.

  - `BetaManagedAgentsGitHubRepositoryResource = object { id, created_at, mount_path, 4 more }`

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

      - `BetaManagedAgentsBranchCheckout = object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `BetaManagedAgentsCommitCheckout = object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

  - `BetaManagedAgentsFileResource = object { id, created_at, file_id, 3 more }`

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

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Retrieve

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Path Parameters

- `session_id: string`

- `resource_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 18 more`

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

- `BetaManagedAgentsGitHubRepositoryResource = object { id, created_at, mount_path, 4 more }`

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

    - `BetaManagedAgentsBranchCheckout = object { name, type }`

      - `name: string`

        Branch name to check out.

      - `type: "branch"`

        - `"branch"`

    - `BetaManagedAgentsCommitCheckout = object { sha, type }`

      - `sha: string`

        Full commit SHA to check out.

      - `type: "commit"`

        - `"commit"`

- `BetaManagedAgentsFileResource = object { id, created_at, file_id, 3 more }`

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

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources/$RESOURCE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Update

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Path Parameters

- `session_id: string`

- `resource_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 18 more`

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

### Body Parameters

- `authorization_token: string`

  New authorization token for the resource. Currently only `github_repository` resources support token rotation.

### Returns

- `BetaManagedAgentsGitHubRepositoryResource = object { id, created_at, mount_path, 4 more }`

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

    - `BetaManagedAgentsBranchCheckout = object { name, type }`

      - `name: string`

        Branch name to check out.

      - `type: "branch"`

        - `"branch"`

    - `BetaManagedAgentsCommitCheckout = object { sha, type }`

      - `sha: string`

        Full commit SHA to check out.

      - `type: "commit"`

        - `"commit"`

- `BetaManagedAgentsFileResource = object { id, created_at, file_id, 3 more }`

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

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources/$RESOURCE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "authorization_token": "ghp_exampletoken"
        }'
```

## Delete

**delete** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Path Parameters

- `session_id: string`

- `resource_id: string`

### Header Parameters

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `UnionMember0 = string`

  - `UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 18 more`

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

- `BetaManagedAgentsDeleteSessionResource = object { id, type }`

  Confirmation of resource deletion.

  - `id: string`

  - `type: "session_resource_deleted"`

    - `"session_resource_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources/$RESOURCE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Domain Types

### Beta Managed Agents Delete Session Resource

- `BetaManagedAgentsDeleteSessionResource = object { id, type }`

  Confirmation of resource deletion.

  - `id: string`

  - `type: "session_resource_deleted"`

    - `"session_resource_deleted"`

### Beta Managed Agents File Resource

- `BetaManagedAgentsFileResource = object { id, created_at, file_id, 3 more }`

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

- `BetaManagedAgentsGitHubRepositoryResource = object { id, created_at, mount_path, 4 more }`

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

    - `BetaManagedAgentsBranchCheckout = object { name, type }`

      - `name: string`

        Branch name to check out.

      - `type: "branch"`

        - `"branch"`

    - `BetaManagedAgentsCommitCheckout = object { sha, type }`

      - `sha: string`

        Full commit SHA to check out.

      - `type: "commit"`

        - `"commit"`

### Beta Managed Agents Session Resource

- `BetaManagedAgentsSessionResource = BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource`

  - `BetaManagedAgentsGitHubRepositoryResource = object { id, created_at, mount_path, 4 more }`

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

      - `BetaManagedAgentsBranchCheckout = object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `BetaManagedAgentsCommitCheckout = object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

  - `BetaManagedAgentsFileResource = object { id, created_at, file_id, 3 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

      - `"file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

### Resource Retrieve Response

- `ResourceRetrieveResponse = BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource`

  The requested session resource.

  - `BetaManagedAgentsGitHubRepositoryResource = object { id, created_at, mount_path, 4 more }`

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

      - `BetaManagedAgentsBranchCheckout = object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `BetaManagedAgentsCommitCheckout = object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

  - `BetaManagedAgentsFileResource = object { id, created_at, file_id, 3 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

      - `"file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

### Resource Update Response

- `ResourceUpdateResponse = BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource`

  The updated session resource.

  - `BetaManagedAgentsGitHubRepositoryResource = object { id, created_at, mount_path, 4 more }`

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

      - `BetaManagedAgentsBranchCheckout = object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `BetaManagedAgentsCommitCheckout = object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

  - `BetaManagedAgentsFileResource = object { id, created_at, file_id, 3 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

      - `"file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

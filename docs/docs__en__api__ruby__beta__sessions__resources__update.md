## Update

`beta.sessions.resources.update(resource_id, **kwargs) -> ResourceUpdateResponse`

**post** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Parameters

- `session_id: String`

- `resource_id: String`

- `authorization_token: String`

  New authorization token for the resource. Currently only `github_repository` resources support token rotation.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 20 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

### Returns

- `ResourceUpdateResponse = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource`

  The updated session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

    - `mount_path: String`

    - `type: :github_repository`

      - `:github_repository`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

    - `url: String`

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

        - `type: :branch`

          - `:branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

        - `type: :commit`

          - `:commit`

  - `class BetaManagedAgentsFileResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

    - `file_id: String`

    - `mount_path: String`

    - `type: :file`

      - `:file`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

resource = anthropic.beta.sessions.resources.update(
  "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7",
  authorization_token: "ghp_exampletoken"
)

puts(resource)
```

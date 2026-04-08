## Add

`client.beta.sessions.resources.add(stringsessionID, ResourceAddParamsparams, RequestOptionsoptions?): BetaManagedAgentsFileResource`

**post** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Parameters

- `sessionID: string`

- `params: ResourceAddParams`

  - `file_id: string`

    Body param: ID of a previously uploaded file.

  - `type: "file"`

    Body param

    - `"file"`

  - `mount_path?: string | null`

    Body param: Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more`

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

- `BetaManagedAgentsFileResource`

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

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsFileResource = await client.beta.sessions.resources.add(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  { file_id: 'file_011CNha8iCJcU1wXNR6q4V8w', type: 'file' },
);

console.log(betaManagedAgentsFileResource.id);
```

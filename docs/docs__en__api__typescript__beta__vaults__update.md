## Update

`client.beta.vaults.update(stringvaultID, VaultUpdateParamsparams, RequestOptionsoptions?): BetaManagedAgentsVault`

**post** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `vaultID: string`

- `params: VaultUpdateParams`

  - `display_name?: string | null`

    Body param: Updated human-readable name for the vault. 1-255 characters.

  - `metadata?: Record<string, string | null> | null`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

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

- `BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsVault = await client.beta.vaults.update('vlt_011CZkZDLs7fYzm1hXNPeRjv');

console.log(betaManagedAgentsVault.id);
```

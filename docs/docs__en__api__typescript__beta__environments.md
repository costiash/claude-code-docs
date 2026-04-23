# Environments

## Create

`client.beta.environments.create(EnvironmentCreateParamsparams, RequestOptionsoptions?): BetaEnvironment`

**post** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `params: EnvironmentCreateParams`

  - `name: string`

    Body param: Human-readable name for the environment

  - `config?: BetaCloudConfigParams | null`

    Body param: Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

    - `type: "cloud"`

      Environment type

      - `"cloud"`

    - `networking?: BetaUnrestrictedNetwork | BetaLimitedNetworkParams | null`

      Network configuration policy. Omit on update to preserve the existing value.

      - `BetaUnrestrictedNetwork`

        Unrestricted network access.

        - `type: "unrestricted"`

          Network policy type

          - `"unrestricted"`

      - `BetaLimitedNetworkParams`

        Limited network request params.

        Fields default to null; on update, omitted fields preserve the
        existing value.

        - `type: "limited"`

          Network policy type

          - `"limited"`

        - `allow_mcp_servers?: boolean | null`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allow_package_managers?: boolean | null`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allowed_hosts?: Array<string> | null`

          Specifies domains the container can reach.

    - `packages?: BetaPackagesParams | null`

      Specify packages (and optionally their versions) available in this environment.

      When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

      - `apt?: Array<string> | null`

        Ubuntu/Debian packages to install

      - `cargo?: Array<string> | null`

        Rust packages to install

      - `gem?: Array<string> | null`

        Ruby packages to install

      - `go?: Array<string> | null`

        Go packages to install

      - `npm?: Array<string> | null`

        Node.js packages to install

      - `pip?: Array<string> | null`

        Python packages to install

      - `type?: "packages"`

        Package configuration type

        - `"packages"`

  - `description?: string | null`

    Body param: Optional description of the environment

  - `metadata?: Record<string, string>`

    Body param: User-provided metadata key-value pairs

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

- `BetaEnvironment`

  Unified Environment resource for both cloud and BYOC environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string | null`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig`

    `cloud` environment configuration.

    - `networking: BetaUnrestrictedNetwork | BetaLimitedNetwork`

      Network configuration policy.

      - `BetaUnrestrictedNetwork`

        Unrestricted network access.

        - `type: "unrestricted"`

          Network policy type

          - `"unrestricted"`

      - `BetaLimitedNetwork`

        Limited network access.

        - `allow_mcp_servers: boolean`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

        - `allow_package_managers: boolean`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

        - `allowed_hosts: Array<string>`

          Specifies domains the container can reach.

        - `type: "limited"`

          Network policy type

          - `"limited"`

    - `packages: BetaPackages`

      Package manager configuration.

      - `apt: Array<string>`

        Ubuntu/Debian packages to install

      - `cargo: Array<string>`

        Rust packages to install

      - `gem: Array<string>`

        Ruby packages to install

      - `go: Array<string>`

        Go packages to install

      - `npm: Array<string>`

        Node.js packages to install

      - `pip: Array<string>`

        Python packages to install

      - `type?: "packages"`

        Package configuration type

        - `"packages"`

    - `type: "cloud"`

      Environment type

      - `"cloud"`

  - `created_at: string`

    RFC 3339 timestamp when environment was created

  - `description: string`

    User-provided description for the environment

  - `metadata: Record<string, string>`

    User-provided metadata key-value pairs

  - `name: string`

    Human-readable name for the environment

  - `type: "environment"`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: string`

    RFC 3339 timestamp when environment was last updated

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaEnvironment = await client.beta.environments.create({ name: 'python-data-analysis' });

console.log(betaEnvironment.id);
```

## List

`client.beta.environments.list(EnvironmentListParamsparams?, RequestOptionsoptions?): PageCursor<BetaEnvironment>`

**get** `/v1/environments`

List environments with pagination support.

### Parameters

- `params: EnvironmentListParams`

  - `include_archived?: boolean`

    Query param: Include archived environments in the response

  - `limit?: number`

    Query param: Maximum number of environments to return

  - `page?: string | null`

    Query param: Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.

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

- `BetaEnvironment`

  Unified Environment resource for both cloud and BYOC environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string | null`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig`

    `cloud` environment configuration.

    - `networking: BetaUnrestrictedNetwork | BetaLimitedNetwork`

      Network configuration policy.

      - `BetaUnrestrictedNetwork`

        Unrestricted network access.

        - `type: "unrestricted"`

          Network policy type

          - `"unrestricted"`

      - `BetaLimitedNetwork`

        Limited network access.

        - `allow_mcp_servers: boolean`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

        - `allow_package_managers: boolean`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

        - `allowed_hosts: Array<string>`

          Specifies domains the container can reach.

        - `type: "limited"`

          Network policy type

          - `"limited"`

    - `packages: BetaPackages`

      Package manager configuration.

      - `apt: Array<string>`

        Ubuntu/Debian packages to install

      - `cargo: Array<string>`

        Rust packages to install

      - `gem: Array<string>`

        Ruby packages to install

      - `go: Array<string>`

        Go packages to install

      - `npm: Array<string>`

        Node.js packages to install

      - `pip: Array<string>`

        Python packages to install

      - `type?: "packages"`

        Package configuration type

        - `"packages"`

    - `type: "cloud"`

      Environment type

      - `"cloud"`

  - `created_at: string`

    RFC 3339 timestamp when environment was created

  - `description: string`

    User-provided description for the environment

  - `metadata: Record<string, string>`

    User-provided metadata key-value pairs

  - `name: string`

    Human-readable name for the environment

  - `type: "environment"`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: string`

    RFC 3339 timestamp when environment was last updated

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaEnvironment of client.beta.environments.list()) {
  console.log(betaEnvironment.id);
}
```

## Retrieve

`client.beta.environments.retrieve(stringenvironmentID, EnvironmentRetrieveParamsparams?, RequestOptionsoptions?): BetaEnvironment`

**get** `/v1/environments/{environment_id}`

Retrieve a specific environment by ID.

### Parameters

- `environmentID: string`

- `params: EnvironmentRetrieveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

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

- `BetaEnvironment`

  Unified Environment resource for both cloud and BYOC environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string | null`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig`

    `cloud` environment configuration.

    - `networking: BetaUnrestrictedNetwork | BetaLimitedNetwork`

      Network configuration policy.

      - `BetaUnrestrictedNetwork`

        Unrestricted network access.

        - `type: "unrestricted"`

          Network policy type

          - `"unrestricted"`

      - `BetaLimitedNetwork`

        Limited network access.

        - `allow_mcp_servers: boolean`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

        - `allow_package_managers: boolean`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

        - `allowed_hosts: Array<string>`

          Specifies domains the container can reach.

        - `type: "limited"`

          Network policy type

          - `"limited"`

    - `packages: BetaPackages`

      Package manager configuration.

      - `apt: Array<string>`

        Ubuntu/Debian packages to install

      - `cargo: Array<string>`

        Rust packages to install

      - `gem: Array<string>`

        Ruby packages to install

      - `go: Array<string>`

        Go packages to install

      - `npm: Array<string>`

        Node.js packages to install

      - `pip: Array<string>`

        Python packages to install

      - `type?: "packages"`

        Package configuration type

        - `"packages"`

    - `type: "cloud"`

      Environment type

      - `"cloud"`

  - `created_at: string`

    RFC 3339 timestamp when environment was created

  - `description: string`

    User-provided description for the environment

  - `metadata: Record<string, string>`

    User-provided metadata key-value pairs

  - `name: string`

    Human-readable name for the environment

  - `type: "environment"`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: string`

    RFC 3339 timestamp when environment was last updated

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaEnvironment = await client.beta.environments.retrieve('env_011CZkZ9X2dpNyB7HsEFoRfW');

console.log(betaEnvironment.id);
```

## Update

`client.beta.environments.update(stringenvironmentID, EnvironmentUpdateParamsparams, RequestOptionsoptions?): BetaEnvironment`

**post** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `environmentID: string`

- `params: EnvironmentUpdateParams`

  - `config?: BetaCloudConfigParams | null`

    Body param: Request params for `cloud` environment configuration.

    Fields default to null; on update, omitted fields preserve the
    existing value.

    - `type: "cloud"`

      Environment type

      - `"cloud"`

    - `networking?: BetaUnrestrictedNetwork | BetaLimitedNetworkParams | null`

      Network configuration policy. Omit on update to preserve the existing value.

      - `BetaUnrestrictedNetwork`

        Unrestricted network access.

        - `type: "unrestricted"`

          Network policy type

          - `"unrestricted"`

      - `BetaLimitedNetworkParams`

        Limited network request params.

        Fields default to null; on update, omitted fields preserve the
        existing value.

        - `type: "limited"`

          Network policy type

          - `"limited"`

        - `allow_mcp_servers?: boolean | null`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allow_package_managers?: boolean | null`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

        - `allowed_hosts?: Array<string> | null`

          Specifies domains the container can reach.

    - `packages?: BetaPackagesParams | null`

      Specify packages (and optionally their versions) available in this environment.

      When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

      - `apt?: Array<string> | null`

        Ubuntu/Debian packages to install

      - `cargo?: Array<string> | null`

        Rust packages to install

      - `gem?: Array<string> | null`

        Ruby packages to install

      - `go?: Array<string> | null`

        Go packages to install

      - `npm?: Array<string> | null`

        Node.js packages to install

      - `pip?: Array<string> | null`

        Python packages to install

      - `type?: "packages"`

        Package configuration type

        - `"packages"`

  - `description?: string | null`

    Body param: Updated description of the environment

  - `metadata?: Record<string, string | null>`

    Body param: User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

  - `name?: string | null`

    Body param: Updated name for the environment

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

- `BetaEnvironment`

  Unified Environment resource for both cloud and BYOC environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string | null`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig`

    `cloud` environment configuration.

    - `networking: BetaUnrestrictedNetwork | BetaLimitedNetwork`

      Network configuration policy.

      - `BetaUnrestrictedNetwork`

        Unrestricted network access.

        - `type: "unrestricted"`

          Network policy type

          - `"unrestricted"`

      - `BetaLimitedNetwork`

        Limited network access.

        - `allow_mcp_servers: boolean`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

        - `allow_package_managers: boolean`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

        - `allowed_hosts: Array<string>`

          Specifies domains the container can reach.

        - `type: "limited"`

          Network policy type

          - `"limited"`

    - `packages: BetaPackages`

      Package manager configuration.

      - `apt: Array<string>`

        Ubuntu/Debian packages to install

      - `cargo: Array<string>`

        Rust packages to install

      - `gem: Array<string>`

        Ruby packages to install

      - `go: Array<string>`

        Go packages to install

      - `npm: Array<string>`

        Node.js packages to install

      - `pip: Array<string>`

        Python packages to install

      - `type?: "packages"`

        Package configuration type

        - `"packages"`

    - `type: "cloud"`

      Environment type

      - `"cloud"`

  - `created_at: string`

    RFC 3339 timestamp when environment was created

  - `description: string`

    User-provided description for the environment

  - `metadata: Record<string, string>`

    User-provided metadata key-value pairs

  - `name: string`

    Human-readable name for the environment

  - `type: "environment"`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: string`

    RFC 3339 timestamp when environment was last updated

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaEnvironment = await client.beta.environments.update('env_011CZkZ9X2dpNyB7HsEFoRfW');

console.log(betaEnvironment.id);
```

## Delete

`client.beta.environments.delete(stringenvironmentID, EnvironmentDeleteParamsparams?, RequestOptionsoptions?): BetaEnvironmentDeleteResponse`

**delete** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Parameters

- `environmentID: string`

- `params: EnvironmentDeleteParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

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

- `BetaEnvironmentDeleteResponse`

  Response after deleting an environment.

  - `id: string`

    Environment identifier

  - `type: "environment_deleted"`

    The type of response

    - `"environment_deleted"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaEnvironmentDeleteResponse = await client.beta.environments.delete(
  'env_011CZkZ9X2dpNyB7HsEFoRfW',
);

console.log(betaEnvironmentDeleteResponse.id);
```

## Archive

`client.beta.environments.archive(stringenvironmentID, EnvironmentArchiveParamsparams?, RequestOptionsoptions?): BetaEnvironment`

**post** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Parameters

- `environmentID: string`

- `params: EnvironmentArchiveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

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

- `BetaEnvironment`

  Unified Environment resource for both cloud and BYOC environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string | null`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig`

    `cloud` environment configuration.

    - `networking: BetaUnrestrictedNetwork | BetaLimitedNetwork`

      Network configuration policy.

      - `BetaUnrestrictedNetwork`

        Unrestricted network access.

        - `type: "unrestricted"`

          Network policy type

          - `"unrestricted"`

      - `BetaLimitedNetwork`

        Limited network access.

        - `allow_mcp_servers: boolean`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

        - `allow_package_managers: boolean`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

        - `allowed_hosts: Array<string>`

          Specifies domains the container can reach.

        - `type: "limited"`

          Network policy type

          - `"limited"`

    - `packages: BetaPackages`

      Package manager configuration.

      - `apt: Array<string>`

        Ubuntu/Debian packages to install

      - `cargo: Array<string>`

        Rust packages to install

      - `gem: Array<string>`

        Ruby packages to install

      - `go: Array<string>`

        Go packages to install

      - `npm: Array<string>`

        Node.js packages to install

      - `pip: Array<string>`

        Python packages to install

      - `type?: "packages"`

        Package configuration type

        - `"packages"`

    - `type: "cloud"`

      Environment type

      - `"cloud"`

  - `created_at: string`

    RFC 3339 timestamp when environment was created

  - `description: string`

    User-provided description for the environment

  - `metadata: Record<string, string>`

    User-provided metadata key-value pairs

  - `name: string`

    Human-readable name for the environment

  - `type: "environment"`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: string`

    RFC 3339 timestamp when environment was last updated

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaEnvironment = await client.beta.environments.archive('env_011CZkZ9X2dpNyB7HsEFoRfW');

console.log(betaEnvironment.id);
```

## Domain Types

### Beta Cloud Config

- `BetaCloudConfig`

  `cloud` environment configuration.

  - `networking: BetaUnrestrictedNetwork | BetaLimitedNetwork`

    Network configuration policy.

    - `BetaUnrestrictedNetwork`

      Unrestricted network access.

      - `type: "unrestricted"`

        Network policy type

        - `"unrestricted"`

    - `BetaLimitedNetwork`

      Limited network access.

      - `allow_mcp_servers: boolean`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

      - `allow_package_managers: boolean`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

      - `allowed_hosts: Array<string>`

        Specifies domains the container can reach.

      - `type: "limited"`

        Network policy type

        - `"limited"`

  - `packages: BetaPackages`

    Package manager configuration.

    - `apt: Array<string>`

      Ubuntu/Debian packages to install

    - `cargo: Array<string>`

      Rust packages to install

    - `gem: Array<string>`

      Ruby packages to install

    - `go: Array<string>`

      Go packages to install

    - `npm: Array<string>`

      Node.js packages to install

    - `pip: Array<string>`

      Python packages to install

    - `type?: "packages"`

      Package configuration type

      - `"packages"`

  - `type: "cloud"`

    Environment type

    - `"cloud"`

### Beta Cloud Config Params

- `BetaCloudConfigParams`

  Request params for `cloud` environment configuration.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `type: "cloud"`

    Environment type

    - `"cloud"`

  - `networking?: BetaUnrestrictedNetwork | BetaLimitedNetworkParams | null`

    Network configuration policy. Omit on update to preserve the existing value.

    - `BetaUnrestrictedNetwork`

      Unrestricted network access.

      - `type: "unrestricted"`

        Network policy type

        - `"unrestricted"`

    - `BetaLimitedNetworkParams`

      Limited network request params.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `type: "limited"`

        Network policy type

        - `"limited"`

      - `allow_mcp_servers?: boolean | null`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `allow_package_managers?: boolean | null`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `allowed_hosts?: Array<string> | null`

        Specifies domains the container can reach.

  - `packages?: BetaPackagesParams | null`

    Specify packages (and optionally their versions) available in this environment.

    When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

    - `apt?: Array<string> | null`

      Ubuntu/Debian packages to install

    - `cargo?: Array<string> | null`

      Rust packages to install

    - `gem?: Array<string> | null`

      Ruby packages to install

    - `go?: Array<string> | null`

      Go packages to install

    - `npm?: Array<string> | null`

      Node.js packages to install

    - `pip?: Array<string> | null`

      Python packages to install

    - `type?: "packages"`

      Package configuration type

      - `"packages"`

### Beta Environment

- `BetaEnvironment`

  Unified Environment resource for both cloud and BYOC environments.

  - `id: string`

    Environment identifier (e.g., 'env_...')

  - `archived_at: string | null`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `config: BetaCloudConfig`

    `cloud` environment configuration.

    - `networking: BetaUnrestrictedNetwork | BetaLimitedNetwork`

      Network configuration policy.

      - `BetaUnrestrictedNetwork`

        Unrestricted network access.

        - `type: "unrestricted"`

          Network policy type

          - `"unrestricted"`

      - `BetaLimitedNetwork`

        Limited network access.

        - `allow_mcp_servers: boolean`

          Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

        - `allow_package_managers: boolean`

          Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

        - `allowed_hosts: Array<string>`

          Specifies domains the container can reach.

        - `type: "limited"`

          Network policy type

          - `"limited"`

    - `packages: BetaPackages`

      Package manager configuration.

      - `apt: Array<string>`

        Ubuntu/Debian packages to install

      - `cargo: Array<string>`

        Rust packages to install

      - `gem: Array<string>`

        Ruby packages to install

      - `go: Array<string>`

        Go packages to install

      - `npm: Array<string>`

        Node.js packages to install

      - `pip: Array<string>`

        Python packages to install

      - `type?: "packages"`

        Package configuration type

        - `"packages"`

    - `type: "cloud"`

      Environment type

      - `"cloud"`

  - `created_at: string`

    RFC 3339 timestamp when environment was created

  - `description: string`

    User-provided description for the environment

  - `metadata: Record<string, string>`

    User-provided metadata key-value pairs

  - `name: string`

    Human-readable name for the environment

  - `type: "environment"`

    The type of object (always 'environment')

    - `"environment"`

  - `updated_at: string`

    RFC 3339 timestamp when environment was last updated

### Beta Environment Delete Response

- `BetaEnvironmentDeleteResponse`

  Response after deleting an environment.

  - `id: string`

    Environment identifier

  - `type: "environment_deleted"`

    The type of response

    - `"environment_deleted"`

### Beta Limited Network

- `BetaLimitedNetwork`

  Limited network access.

  - `allow_mcp_servers: boolean`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

  - `allow_package_managers: boolean`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

  - `allowed_hosts: Array<string>`

    Specifies domains the container can reach.

  - `type: "limited"`

    Network policy type

    - `"limited"`

### Beta Limited Network Params

- `BetaLimitedNetworkParams`

  Limited network request params.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `type: "limited"`

    Network policy type

    - `"limited"`

  - `allow_mcp_servers?: boolean | null`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `allow_package_managers?: boolean | null`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `allowed_hosts?: Array<string> | null`

    Specifies domains the container can reach.

### Beta Packages

- `BetaPackages`

  Packages (and their versions) available in this environment.

  - `apt: Array<string>`

    Ubuntu/Debian packages to install

  - `cargo: Array<string>`

    Rust packages to install

  - `gem: Array<string>`

    Ruby packages to install

  - `go: Array<string>`

    Go packages to install

  - `npm: Array<string>`

    Node.js packages to install

  - `pip: Array<string>`

    Python packages to install

  - `type?: "packages"`

    Package configuration type

    - `"packages"`

### Beta Packages Params

- `BetaPackagesParams`

  Specify packages (and optionally their versions) available in this environment.

  When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

  - `apt?: Array<string> | null`

    Ubuntu/Debian packages to install

  - `cargo?: Array<string> | null`

    Rust packages to install

  - `gem?: Array<string> | null`

    Ruby packages to install

  - `go?: Array<string> | null`

    Go packages to install

  - `npm?: Array<string> | null`

    Node.js packages to install

  - `pip?: Array<string> | null`

    Python packages to install

  - `type?: "packages"`

    Package configuration type

    - `"packages"`

### Beta Unrestricted Network

- `BetaUnrestrictedNetwork`

  Unrestricted network access.

  - `type: "unrestricted"`

    Network policy type

    - `"unrestricted"`

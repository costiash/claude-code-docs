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

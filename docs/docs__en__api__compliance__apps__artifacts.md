# Artifacts

## Retrieve

**get** `/v1/compliance/apps/artifacts/{artifact_version_id}`

Returns metadata for an artifact version, without the content body.

Use the sibling `/content` endpoint to fetch the artifact text. The
`md5` and `size_bytes` fields here are computed over the UTF-8
encoding of that text, so a DLP consumer can dedupe or match hashes
without downloading every artifact.

### Path Parameters

- `artifact_version_id: string`

  The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Artifact ID e.g. 'claude_artifact_abc123'

- `artifact_type: string`

  MIME-like artifact type e.g. 'application/vnd.ant.code'

- `claude_chat_id: string`

  The chat this artifact belongs to

- `created_at: string`

  Artifact version creation timestamp

- `md5: string`

  Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

- `size_bytes: number`

  Size in bytes of the artifact content (UTF-8 encoded)

- `title: string`

  Artifact title

- `version_id: string`

  Artifact version ID e.g. 'claude_artifact_version_abc123'

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Download

**get** `/v1/compliance/apps/artifacts/{artifact_version_id}/content`

Download the content of an artifact version for compliance purposes.

Returns the full text content of the artifact version.

### Path Parameters

- `artifact_version_id: string`

  The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Artifact Retrieve Response

- `ArtifactRetrieveResponse = object { id, artifact_type, claude_chat_id, 5 more }`

  Artifact version metadata for GET /v1/compliance/apps/artifacts/{artifact_version_id}.

  Returns metadata only. Use the sibling `/content` endpoint to fetch the
  artifact body.

  - `id: string`

    Artifact ID e.g. 'claude_artifact_abc123'

  - `artifact_type: string`

    MIME-like artifact type e.g. 'application/vnd.ant.code'

  - `claude_chat_id: string`

    The chat this artifact belongs to

  - `created_at: string`

    Artifact version creation timestamp

  - `md5: string`

    Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

  - `size_bytes: number`

    Size in bytes of the artifact content (UTF-8 encoded)

  - `title: string`

    Artifact title

  - `version_id: string`

    Artifact version ID e.g. 'claude_artifact_version_abc123'

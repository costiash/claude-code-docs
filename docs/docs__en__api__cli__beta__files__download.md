## Download

`$ ant beta:files download`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `unnamed_schema_0: file path`

### Example

```cli
ant beta:files download \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

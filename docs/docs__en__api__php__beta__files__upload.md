## Upload File

`$client->beta->files->upload(string file, ?list<AnthropicBeta> betas): FileMetadata`

**post** `/v1/files`

Upload File

### Parameters

- `file: string`

  The file to upload

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `FileMetadata`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing when the file was created.

  - `string filename`

    Original filename of the uploaded file.

  - `string mimeType`

    MIME type of the file.

  - `int sizeBytes`

    Size of the file in bytes.

  - `"file" type`

    Object type.

    For files, this is always `"file"`.

  - `?bool downloadable`

    Whether the file can be downloaded.

  - `?BetaFileScope scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$fileMetadata = $client->beta->files->upload(
  file: FileParam::fromString('Example data', filename: uniqid('file-upload-', true)),
  betas: ['message-batches-2024-09-24'],
);

var_dump($fileMetadata);
```

#### Response

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

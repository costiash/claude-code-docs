# Customer-managed encryption keys

Encrypt Claude workspace data at rest with a key you control.

---

```bash title="Learn more with the /claude-api skill in Claude Code"
claude "/claude-api tell me about customer-managed encryption keys"
```

A customer-managed encryption key (CMEK) lets you provision an encryption key in your own [AWS KMS](https://aws.amazon.com/kms/), [Google Cloud KMS](https://cloud.google.com/security/products/security-key-management), or [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault) and have Anthropic use it to encrypt certain workspace data at rest. You retain full control of the key, including rotation, audit, and revocation, and the key operations Anthropic performs against your key are recorded in your cloud provider's audit logs.

Organizations can **opt in** to use customer-managed encryption keys instead of the default encryption that Anthropic provides.

<Accordion
  title="Enabling CMEK is permanent and can cause irreversible data loss"
 
>
  Enabling CMEK is permanent. Anthropic keeps no copy of your key, so misconfiguration or key loss can permanently destroy your CMEK-protected data. If you are uncertain about any step, contact your Anthropic representative before applying changes.

  - **Permanent data loss:** If your encryption key is deleted, scheduled for deletion, or has its key material destroyed, Anthropic cannot recover your data.
  - **Identifier verification is mandatory:** Granting key access to an incorrect or spoofed principal can expose your data to an unauthorized party. Always verify the Anthropic identifier against the published production identities in each configuration guide.
</Accordion>

## How it works

CMEK is attached per workspace. Only admins can configure it. CMEK protects data written after the key is enabled. Existing data (prior chats, files, and sessions) remains encrypted with Anthropic-managed keys and is not re-encrypted under your key.

CMEK admin configuration events appear in the [Compliance API Activity Feed](/docs/en/manage-claude/compliance-activity-feed). The key operations Anthropic performs against your key (such as wrapping and unwrapping data keys) do not appear in the Compliance API; they appear in your cloud provider's audit logs.

## Prerequisites

- Cloud Admin access in the account, project, or subscription that will host the encryption key.
- An Anthropic Console Organization Admin role (or Owner / Primary Owner).

## Availability and regions

CMEK is currently available in US regions only, and all encryption operations are processed in US regions. Multi-region keys and EU key residency are not yet supported.

<Note>
  CMEK is not currently supported for organizations with HIPAA enabled. Support for using CMEK together with HIPAA is planned. If your organization has HIPAA enabled, contact your Anthropic representative before configuring CMEK.
</Note>

For minimal latency, choose a region close to Anthropic's US infrastructure:

| Provider | Recommended regions |
|:---------|:--------------------|
| AWS | `us-east-2` |
| Google Cloud | `us-central1`, `us-east5` |
| Azure | `northcentralus`, `eastus2` |

## What CMEK protects

### Encrypted

- Message content, including inline file attachments sent with a request, and MCP and tool configuration.
- Backups and snapshots inherit the key.

### Disabled or modified

Some features are turned off or substantially modified when CMEK is enabled:

- Managed agent memory and agent dreaming are disabled.
- Beta and research preview features may not be covered by CMEK.

### Not encrypted

These features remain available, but their data is not encrypted under your key. You can disable any feature that is not appropriate for your use case in Settings.

- Workbench in the Console.
- Data that is not at rest (such as cache) and data with a TTL shorter than 24 hours.
- Activity Feed, audit logs and telemetry network traffic like OTEL, so customers can maintain compliance even if a key is revoked.

### Feature support

The following APIs, managed agent resources, and tools store data at rest under your key when CMEK is enabled:

| APIs | Managed Agents | Tools and features |
|:-----|:---------------|:-------------------|
| Messages | Agents | Web search |
| Models | Environments | Web fetch |
| Files | Sessions | Code execution |
| Batch | Vaults | Bash tool |
| Skills | | Text editor tool |
| User profiles | | MCP connector |
| | | Structured outputs (Claude Sonnet 4.6 and Claude Haiku 4.5 only) |
| | | Advisor tool |
| | | Computer use |
| | | Context management |

## Limitations

- **Irreversible action:** Once a key is attached to a workspace, it cannot be detached or swapped. Rotating the key material within the same key (for example, AWS KMS automatic rotation, a Cloud KMS rotation schedule, or an Azure Key Vault rotation policy) is supported transparently and requires no change in Anthropic. Switching to a *different* key requires creating a new workspace with the new key and migrating your data. Revoking or disabling the key makes all CMEK-protected data in that workspace permanently inaccessible, with no backout path.
- **No retroactive encryption:** CMEK only protects data written after the key is enabled.
- **Latency:** operations that wrap or unwrap data keys make a round-trip to your key management service, which can add a small amount of latency to actions that read or write data at rest.
- **Revocation delay:** key revocation can take up to one hour (the cache TTL). Requests already in flight during that window may continue to succeed.

## Configure your provider

Follow the guide for the key management service you use.

<CardGroup cols={3}>
  <Card href="/docs/en/manage-claude/cmek-aws-kms" title="AWS KMS">
    Create an AWS KMS key with a cross-account key policy, then register and validate it.
  </Card>
  <Card href="/docs/en/manage-claude/cmek-google-cloud-kms" title="Google Cloud KMS">
    Create a Cloud KMS crypto key, grant Anthropic's service account access, then register it.
  </Card>
  <Card href="/docs/en/manage-claude/cmek-azure-key-vault" title="Azure Key Vault">
    Create an RSA key, grant the Anthropic service principal access, then register and validate it.
  </Card>
</CardGroup>
# Webhooks

## Domain Types

### Beta Webhook Event

- `BetaWebhookEvent`

  - `string id`

    Unique event identifier for idempotency.

  - `\Datetime createdAt`

    RFC 3339 timestamp when the event occurred.

  - `BetaWebhookEventData data`

  - `"event" type`

    Object type. Always `event` for webhook payloads.

### Beta Webhook Event Data

- `BetaWebhookEventData`

  - `BetaWebhookSessionCreatedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.created" type`

    - `string workspaceID`

  - `BetaWebhookSessionPendingEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.pending" type`

    - `string workspaceID`

  - `BetaWebhookSessionRunningEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.running" type`

    - `string workspaceID`

  - `BetaWebhookSessionIdledEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.idled" type`

    - `string workspaceID`

  - `BetaWebhookSessionRequiresActionEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.requires_action" type`

    - `string workspaceID`

  - `BetaWebhookSessionArchivedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.archived" type`

    - `string workspaceID`

  - `BetaWebhookSessionDeletedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.deleted" type`

    - `string workspaceID`

  - `BetaWebhookSessionStatusRescheduledEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.status_rescheduled" type`

    - `string workspaceID`

  - `BetaWebhookSessionStatusRunStartedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.status_run_started" type`

    - `string workspaceID`

  - `BetaWebhookSessionStatusIdledEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.status_idled" type`

    - `string workspaceID`

  - `BetaWebhookSessionStatusTerminatedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.status_terminated" type`

    - `string workspaceID`

  - `BetaWebhookSessionThreadCreatedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string sessionThreadID`

      ID of the session thread this event refers to.

    - `"session.thread_created" type`

    - `string workspaceID`

  - `BetaWebhookSessionThreadIdledEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string sessionThreadID`

      ID of the session thread this event refers to.

    - `"session.thread_idled" type`

    - `string workspaceID`

  - `BetaWebhookSessionThreadTerminatedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string sessionThreadID`

      ID of the session thread this event refers to.

    - `"session.thread_terminated" type`

    - `string workspaceID`

  - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `"session.outcome_evaluation_ended" type`

    - `string workspaceID`

  - `BetaWebhookVaultCreatedEventData`

    - `string id`

      ID of the vault that triggered the event.

    - `string organizationID`

    - `"vault.created" type`

    - `string workspaceID`

  - `BetaWebhookVaultArchivedEventData`

    - `string id`

      ID of the vault that triggered the event.

    - `string organizationID`

    - `"vault.archived" type`

    - `string workspaceID`

  - `BetaWebhookVaultDeletedEventData`

    - `string id`

      ID of the vault that triggered the event.

    - `string organizationID`

    - `"vault.deleted" type`

    - `string workspaceID`

  - `BetaWebhookVaultCredentialCreatedEventData`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `"vault_credential.created" type`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `BetaWebhookVaultCredentialArchivedEventData`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `"vault_credential.archived" type`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `BetaWebhookVaultCredentialDeletedEventData`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `"vault_credential.deleted" type`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `BetaWebhookVaultCredentialRefreshFailedEventData`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `"vault_credential.refresh_failed" type`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

### Beta Webhook Session Archived Event Data

- `BetaWebhookSessionArchivedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.archived" type`

  - `string workspaceID`

### Beta Webhook Session Created Event Data

- `BetaWebhookSessionCreatedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.created" type`

  - `string workspaceID`

### Beta Webhook Session Deleted Event Data

- `BetaWebhookSessionDeletedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.deleted" type`

  - `string workspaceID`

### Beta Webhook Session Idled Event Data

- `BetaWebhookSessionIdledEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.idled" type`

  - `string workspaceID`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.outcome_evaluation_ended" type`

  - `string workspaceID`

### Beta Webhook Session Pending Event Data

- `BetaWebhookSessionPendingEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.pending" type`

  - `string workspaceID`

### Beta Webhook Session Requires Action Event Data

- `BetaWebhookSessionRequiresActionEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.requires_action" type`

  - `string workspaceID`

### Beta Webhook Session Running Event Data

- `BetaWebhookSessionRunningEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.running" type`

  - `string workspaceID`

### Beta Webhook Session Status Idled Event Data

- `BetaWebhookSessionStatusIdledEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.status_idled" type`

  - `string workspaceID`

### Beta Webhook Session Status Rescheduled Event Data

- `BetaWebhookSessionStatusRescheduledEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.status_rescheduled" type`

  - `string workspaceID`

### Beta Webhook Session Status Run Started Event Data

- `BetaWebhookSessionStatusRunStartedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.status_run_started" type`

  - `string workspaceID`

### Beta Webhook Session Status Terminated Event Data

- `BetaWebhookSessionStatusTerminatedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `"session.status_terminated" type`

  - `string workspaceID`

### Beta Webhook Session Thread Created Event Data

- `BetaWebhookSessionThreadCreatedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string sessionThreadID`

    ID of the session thread this event refers to.

  - `"session.thread_created" type`

  - `string workspaceID`

### Beta Webhook Session Thread Idled Event Data

- `BetaWebhookSessionThreadIdledEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string sessionThreadID`

    ID of the session thread this event refers to.

  - `"session.thread_idled" type`

  - `string workspaceID`

### Beta Webhook Session Thread Terminated Event Data

- `BetaWebhookSessionThreadTerminatedEventData`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string sessionThreadID`

    ID of the session thread this event refers to.

  - `"session.thread_terminated" type`

  - `string workspaceID`

### Beta Webhook Vault Archived Event Data

- `BetaWebhookVaultArchivedEventData`

  - `string id`

    ID of the vault that triggered the event.

  - `string organizationID`

  - `"vault.archived" type`

  - `string workspaceID`

### Beta Webhook Vault Created Event Data

- `BetaWebhookVaultCreatedEventData`

  - `string id`

    ID of the vault that triggered the event.

  - `string organizationID`

  - `"vault.created" type`

  - `string workspaceID`

### Beta Webhook Vault Credential Archived Event Data

- `BetaWebhookVaultCredentialArchivedEventData`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `"vault_credential.archived" type`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Credential Created Event Data

- `BetaWebhookVaultCredentialCreatedEventData`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `"vault_credential.created" type`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Credential Deleted Event Data

- `BetaWebhookVaultCredentialDeletedEventData`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `"vault_credential.deleted" type`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `BetaWebhookVaultCredentialRefreshFailedEventData`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `"vault_credential.refresh_failed" type`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Deleted Event Data

- `BetaWebhookVaultDeletedEventData`

  - `string id`

    ID of the vault that triggered the event.

  - `string organizationID`

  - `"vault.deleted" type`

  - `string workspaceID`

### Unwrap Webhook Event

- `UnwrapWebhookEvent`

  - `string id`

    Unique event identifier for idempotency.

  - `\Datetime createdAt`

    RFC 3339 timestamp when the event occurred.

  - `BetaWebhookEventData data`

  - `"event" type`

    Object type. Always `event` for webhook payloads.

# Webhooks

## Domain Types

### Beta Webhook Event

- `class BetaWebhookEvent:`

  - `required string ID`

    Unique event identifier for idempotency.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 timestamp when the event occurred.

  - `required BetaWebhookEventData Data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionPendingEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.pending"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRunningEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.running"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionIdledEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.requires_action"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionArchivedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionDeletedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusScheduledEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_scheduled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_run_started"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_terminated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.thread_created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.thread_idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.thread_terminated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.outcome_evaluation_ended"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCreatedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultArchivedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultDeletedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.created"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.archived"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.deleted"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.refresh_failed"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

  - `JsonElement Type "event"constant`

    Object type. Always `event` for webhook payloads.

### Beta Webhook Event Data

- `class BetaWebhookEventData: A class that can be one of several variants.union`

  - `class BetaWebhookSessionCreatedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionPendingEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.pending"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionRunningEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.running"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionIdledEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.idled"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionRequiresActionEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.requires_action"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionArchivedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionDeletedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusScheduledEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.status_scheduled"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusRunStartedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.status_run_started"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusIdledEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.status_idled"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusTerminatedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.status_terminated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadCreatedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.thread_created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadIdledEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.thread_idled"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadTerminatedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.thread_terminated"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "session.outcome_evaluation_ended"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCreatedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault.created"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultArchivedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault.archived"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultDeletedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault.deleted"constant`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialCreatedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault_credential.created"constant`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialArchivedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault_credential.archived"constant`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialDeletedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault_credential.deleted"constant`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

    - `required string ID`

      ID of the resource that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type "vault_credential.refresh_failed"constant`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.deleted"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.idled"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.outcome_evaluation_ended"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.pending"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.requires_action"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.running"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.status_idled"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.status_run_started"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Status Scheduled Event Data

- `class BetaWebhookSessionStatusScheduledEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.status_scheduled"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.status_terminated"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.thread_created"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.thread_idled"constant`

  - `required string WorkspaceID`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "session.thread_terminated"constant`

  - `required string WorkspaceID`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault.archived"constant`

  - `required string WorkspaceID`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault.created"constant`

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault_credential.archived"constant`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault_credential.created"constant`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault_credential.deleted"constant`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault_credential.refresh_failed"constant`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData:`

  - `required string ID`

    ID of the resource that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type "vault.deleted"constant`

  - `required string WorkspaceID`

### Unwrap Webhook Event

- `class UnwrapWebhookEvent:`

  - `required string ID`

    Unique event identifier for idempotency.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 timestamp when the event occurred.

  - `required BetaWebhookEventData Data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionPendingEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.pending"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRunningEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.running"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionIdledEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.requires_action"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionArchivedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionDeletedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusScheduledEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_scheduled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_run_started"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.status_terminated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.thread_created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.thread_idled"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.thread_terminated"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "session.outcome_evaluation_ended"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCreatedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.created"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultArchivedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.archived"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultDeletedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault.deleted"constant`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.created"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.archived"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.deleted"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `required string ID`

        ID of the resource that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type "vault_credential.refresh_failed"constant`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

  - `JsonElement Type "event"constant`

    Object type. Always `event` for webhook payloads.

# Webhooks

## Domain Types

### Beta Webhook Event

- `class BetaWebhookEvent:`

  - `String id`

    Unique event identifier for idempotency.

  - `LocalDateTime createdAt`

    RFC 3339 timestamp when the event occurred.

  - `BetaWebhookEventData data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.created"constant`

        - `SESSION_CREATED("session.created")`

      - `String workspaceId`

    - `class BetaWebhookSessionPendingEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.pending"constant`

        - `SESSION_PENDING("session.pending")`

      - `String workspaceId`

    - `class BetaWebhookSessionRunningEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.running"constant`

        - `SESSION_RUNNING("session.running")`

      - `String workspaceId`

    - `class BetaWebhookSessionIdledEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.idled"constant`

        - `SESSION_IDLED("session.idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.requires_action"constant`

        - `SESSION_REQUIRES_ACTION("session.requires_action")`

      - `String workspaceId`

    - `class BetaWebhookSessionArchivedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.archived"constant`

        - `SESSION_ARCHIVED("session.archived")`

      - `String workspaceId`

    - `class BetaWebhookSessionDeletedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.deleted"constant`

        - `SESSION_DELETED("session.deleted")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusScheduledEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_scheduled"constant`

        - `SESSION_STATUS_SCHEDULED("session.status_scheduled")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_run_started"constant`

        - `SESSION_STATUS_RUN_STARTED("session.status_run_started")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_idled"constant`

        - `SESSION_STATUS_IDLED("session.status_idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_terminated"constant`

        - `SESSION_STATUS_TERMINATED("session.status_terminated")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.thread_created"constant`

        - `SESSION_THREAD_CREATED("session.thread_created")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.thread_idled"constant`

        - `SESSION_THREAD_IDLED("session.thread_idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.thread_terminated"constant`

        - `SESSION_THREAD_TERMINATED("session.thread_terminated")`

      - `String workspaceId`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.outcome_evaluation_ended"constant`

        - `SESSION_OUTCOME_EVALUATION_ENDED("session.outcome_evaluation_ended")`

      - `String workspaceId`

    - `class BetaWebhookVaultCreatedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.created"constant`

        - `VAULT_CREATED("vault.created")`

      - `String workspaceId`

    - `class BetaWebhookVaultArchivedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.archived"constant`

        - `VAULT_ARCHIVED("vault.archived")`

      - `String workspaceId`

    - `class BetaWebhookVaultDeletedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.deleted"constant`

        - `VAULT_DELETED("vault.deleted")`

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.created"constant`

        - `VAULT_CREDENTIAL_CREATED("vault_credential.created")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.archived"constant`

        - `VAULT_CREDENTIAL_ARCHIVED("vault_credential.archived")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.deleted"constant`

        - `VAULT_CREDENTIAL_DELETED("vault_credential.deleted")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.refresh_failed"constant`

        - `VAULT_CREDENTIAL_REFRESH_FAILED("vault_credential.refresh_failed")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

  - `JsonValue; type "event"constant`

    Object type. Always `event` for webhook payloads.

    - `EVENT("event")`

### Beta Webhook Event Data

- `class BetaWebhookEventData: A class that can be one of several variants.union`

  - `class BetaWebhookSessionCreatedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.created"constant`

      - `SESSION_CREATED("session.created")`

    - `String workspaceId`

  - `class BetaWebhookSessionPendingEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.pending"constant`

      - `SESSION_PENDING("session.pending")`

    - `String workspaceId`

  - `class BetaWebhookSessionRunningEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.running"constant`

      - `SESSION_RUNNING("session.running")`

    - `String workspaceId`

  - `class BetaWebhookSessionIdledEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.idled"constant`

      - `SESSION_IDLED("session.idled")`

    - `String workspaceId`

  - `class BetaWebhookSessionRequiresActionEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.requires_action"constant`

      - `SESSION_REQUIRES_ACTION("session.requires_action")`

    - `String workspaceId`

  - `class BetaWebhookSessionArchivedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.archived"constant`

      - `SESSION_ARCHIVED("session.archived")`

    - `String workspaceId`

  - `class BetaWebhookSessionDeletedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.deleted"constant`

      - `SESSION_DELETED("session.deleted")`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusScheduledEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.status_scheduled"constant`

      - `SESSION_STATUS_SCHEDULED("session.status_scheduled")`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusRunStartedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.status_run_started"constant`

      - `SESSION_STATUS_RUN_STARTED("session.status_run_started")`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusIdledEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.status_idled"constant`

      - `SESSION_STATUS_IDLED("session.status_idled")`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusTerminatedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.status_terminated"constant`

      - `SESSION_STATUS_TERMINATED("session.status_terminated")`

    - `String workspaceId`

  - `class BetaWebhookSessionThreadCreatedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.thread_created"constant`

      - `SESSION_THREAD_CREATED("session.thread_created")`

    - `String workspaceId`

  - `class BetaWebhookSessionThreadIdledEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.thread_idled"constant`

      - `SESSION_THREAD_IDLED("session.thread_idled")`

    - `String workspaceId`

  - `class BetaWebhookSessionThreadTerminatedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.thread_terminated"constant`

      - `SESSION_THREAD_TERMINATED("session.thread_terminated")`

    - `String workspaceId`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "session.outcome_evaluation_ended"constant`

      - `SESSION_OUTCOME_EVALUATION_ENDED("session.outcome_evaluation_ended")`

    - `String workspaceId`

  - `class BetaWebhookVaultCreatedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault.created"constant`

      - `VAULT_CREATED("vault.created")`

    - `String workspaceId`

  - `class BetaWebhookVaultArchivedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault.archived"constant`

      - `VAULT_ARCHIVED("vault.archived")`

    - `String workspaceId`

  - `class BetaWebhookVaultDeletedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault.deleted"constant`

      - `VAULT_DELETED("vault.deleted")`

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialCreatedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault_credential.created"constant`

      - `VAULT_CREDENTIAL_CREATED("vault_credential.created")`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialArchivedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault_credential.archived"constant`

      - `VAULT_CREDENTIAL_ARCHIVED("vault_credential.archived")`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialDeletedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault_credential.deleted"constant`

      - `VAULT_CREDENTIAL_DELETED("vault_credential.deleted")`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

    - `String id`

      ID of the resource that triggered the event.

    - `String organizationId`

    - `JsonValue; type "vault_credential.refresh_failed"constant`

      - `VAULT_CREDENTIAL_REFRESH_FAILED("vault_credential.refresh_failed")`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.archived"constant`

    - `SESSION_ARCHIVED("session.archived")`

  - `String workspaceId`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.created"constant`

    - `SESSION_CREATED("session.created")`

  - `String workspaceId`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.deleted"constant`

    - `SESSION_DELETED("session.deleted")`

  - `String workspaceId`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.idled"constant`

    - `SESSION_IDLED("session.idled")`

  - `String workspaceId`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.outcome_evaluation_ended"constant`

    - `SESSION_OUTCOME_EVALUATION_ENDED("session.outcome_evaluation_ended")`

  - `String workspaceId`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.pending"constant`

    - `SESSION_PENDING("session.pending")`

  - `String workspaceId`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.requires_action"constant`

    - `SESSION_REQUIRES_ACTION("session.requires_action")`

  - `String workspaceId`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.running"constant`

    - `SESSION_RUNNING("session.running")`

  - `String workspaceId`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.status_idled"constant`

    - `SESSION_STATUS_IDLED("session.status_idled")`

  - `String workspaceId`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.status_run_started"constant`

    - `SESSION_STATUS_RUN_STARTED("session.status_run_started")`

  - `String workspaceId`

### Beta Webhook Session Status Scheduled Event Data

- `class BetaWebhookSessionStatusScheduledEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.status_scheduled"constant`

    - `SESSION_STATUS_SCHEDULED("session.status_scheduled")`

  - `String workspaceId`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.status_terminated"constant`

    - `SESSION_STATUS_TERMINATED("session.status_terminated")`

  - `String workspaceId`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.thread_created"constant`

    - `SESSION_THREAD_CREATED("session.thread_created")`

  - `String workspaceId`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.thread_idled"constant`

    - `SESSION_THREAD_IDLED("session.thread_idled")`

  - `String workspaceId`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "session.thread_terminated"constant`

    - `SESSION_THREAD_TERMINATED("session.thread_terminated")`

  - `String workspaceId`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault.archived"constant`

    - `VAULT_ARCHIVED("vault.archived")`

  - `String workspaceId`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault.created"constant`

    - `VAULT_CREATED("vault.created")`

  - `String workspaceId`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault_credential.archived"constant`

    - `VAULT_CREDENTIAL_ARCHIVED("vault_credential.archived")`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault_credential.created"constant`

    - `VAULT_CREDENTIAL_CREATED("vault_credential.created")`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault_credential.deleted"constant`

    - `VAULT_CREDENTIAL_DELETED("vault_credential.deleted")`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault_credential.refresh_failed"constant`

    - `VAULT_CREDENTIAL_REFRESH_FAILED("vault_credential.refresh_failed")`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData:`

  - `String id`

    ID of the resource that triggered the event.

  - `String organizationId`

  - `JsonValue; type "vault.deleted"constant`

    - `VAULT_DELETED("vault.deleted")`

  - `String workspaceId`

### Unwrap Webhook Event

- `class UnwrapWebhookEvent:`

  - `String id`

    Unique event identifier for idempotency.

  - `LocalDateTime createdAt`

    RFC 3339 timestamp when the event occurred.

  - `BetaWebhookEventData data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.created"constant`

        - `SESSION_CREATED("session.created")`

      - `String workspaceId`

    - `class BetaWebhookSessionPendingEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.pending"constant`

        - `SESSION_PENDING("session.pending")`

      - `String workspaceId`

    - `class BetaWebhookSessionRunningEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.running"constant`

        - `SESSION_RUNNING("session.running")`

      - `String workspaceId`

    - `class BetaWebhookSessionIdledEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.idled"constant`

        - `SESSION_IDLED("session.idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.requires_action"constant`

        - `SESSION_REQUIRES_ACTION("session.requires_action")`

      - `String workspaceId`

    - `class BetaWebhookSessionArchivedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.archived"constant`

        - `SESSION_ARCHIVED("session.archived")`

      - `String workspaceId`

    - `class BetaWebhookSessionDeletedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.deleted"constant`

        - `SESSION_DELETED("session.deleted")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusScheduledEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_scheduled"constant`

        - `SESSION_STATUS_SCHEDULED("session.status_scheduled")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_run_started"constant`

        - `SESSION_STATUS_RUN_STARTED("session.status_run_started")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_idled"constant`

        - `SESSION_STATUS_IDLED("session.status_idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.status_terminated"constant`

        - `SESSION_STATUS_TERMINATED("session.status_terminated")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.thread_created"constant`

        - `SESSION_THREAD_CREATED("session.thread_created")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.thread_idled"constant`

        - `SESSION_THREAD_IDLED("session.thread_idled")`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.thread_terminated"constant`

        - `SESSION_THREAD_TERMINATED("session.thread_terminated")`

      - `String workspaceId`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "session.outcome_evaluation_ended"constant`

        - `SESSION_OUTCOME_EVALUATION_ENDED("session.outcome_evaluation_ended")`

      - `String workspaceId`

    - `class BetaWebhookVaultCreatedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.created"constant`

        - `VAULT_CREATED("vault.created")`

      - `String workspaceId`

    - `class BetaWebhookVaultArchivedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.archived"constant`

        - `VAULT_ARCHIVED("vault.archived")`

      - `String workspaceId`

    - `class BetaWebhookVaultDeletedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault.deleted"constant`

        - `VAULT_DELETED("vault.deleted")`

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.created"constant`

        - `VAULT_CREDENTIAL_CREATED("vault_credential.created")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.archived"constant`

        - `VAULT_CREDENTIAL_ARCHIVED("vault_credential.archived")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.deleted"constant`

        - `VAULT_CREDENTIAL_DELETED("vault_credential.deleted")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `String id`

        ID of the resource that triggered the event.

      - `String organizationId`

      - `JsonValue; type "vault_credential.refresh_failed"constant`

        - `VAULT_CREDENTIAL_REFRESH_FAILED("vault_credential.refresh_failed")`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

  - `JsonValue; type "event"constant`

    Object type. Always `event` for webhook payloads.

    - `EVENT("event")`

# Webhooks

## Unwrap

`client.Beta.Webhooks.Unwrap(ctx) error`

**** ``

### Example

```go
package main

import (
  "context"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  err := client.Beta.Webhooks.Unwrap(context.TODO())
  if err != nil {
    panic(err.Error())
  }
}
```

## Domain Types

### Beta Webhook Event

- `type BetaWebhookEvent struct{…}`

  - `ID string`

    Unique event identifier for idempotency.

  - `CreatedAt Time`

    RFC 3339 timestamp when the event occurred.

  - `Data BetaWebhookEventDataUnion`

    - `type BetaWebhookSessionCreatedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionCreated`

        - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionPendingEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionPending`

        - `const SessionPendingSessionPending SessionPending = "session.pending"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRunningEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionRunning`

        - `const SessionRunningSessionRunning SessionRunning = "session.running"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionIdledEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionIdled`

        - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRequiresActionEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionRequiresAction`

        - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionArchivedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionArchived`

        - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionDeletedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionDeleted`

        - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusScheduledEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusScheduled`

        - `const SessionStatusScheduledSessionStatusScheduled SessionStatusScheduled = "session.status_scheduled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRunStarted`

        - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusIdledEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusIdled`

        - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusTerminated`

        - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionThreadCreated`

        - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadIdledEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionThreadIdled`

        - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionThreadTerminated`

        - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionOutcomeEvaluationEnded`

        - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCreatedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultCreated`

        - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultArchivedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultArchived`

        - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultDeletedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultDeleted`

        - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialCreated`

        - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialArchived`

        - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialDeleted`

        - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialRefreshFailed`

        - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

  - `Type Event`

    Object type. Always `event` for webhook payloads.

    - `const EventEvent Event = "event"`

### Beta Webhook Event Data

- `type BetaWebhookEventDataUnion interface{…}`

  - `type BetaWebhookSessionCreatedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionCreated`

      - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionPendingEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionPending`

      - `const SessionPendingSessionPending SessionPending = "session.pending"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRunningEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionRunning`

      - `const SessionRunningSessionRunning SessionRunning = "session.running"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionIdledEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionIdled`

      - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRequiresActionEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionRequiresAction`

      - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionArchivedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionArchived`

      - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionDeletedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionDeleted`

      - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusScheduledEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusScheduled`

      - `const SessionStatusScheduledSessionStatusScheduled SessionStatusScheduled = "session.status_scheduled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusRunStarted`

      - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusIdledEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusIdled`

      - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusTerminated`

      - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionThreadCreated`

      - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadIdledEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionThreadIdled`

      - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionThreadTerminated`

      - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type SessionOutcomeEvaluationEnded`

      - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCreatedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type VaultCreated`

      - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultArchivedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type VaultArchived`

      - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultDeletedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type VaultDeleted`

      - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialCreated`

      - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialArchived`

      - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialDeleted`

      - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

    - `ID string`

      ID of the resource that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialRefreshFailed`

      - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

### Beta Webhook Session Archived Event Data

- `type BetaWebhookSessionArchivedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionArchived`

    - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

  - `WorkspaceID string`

### Beta Webhook Session Created Event Data

- `type BetaWebhookSessionCreatedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionCreated`

    - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

  - `WorkspaceID string`

### Beta Webhook Session Deleted Event Data

- `type BetaWebhookSessionDeletedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionDeleted`

    - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

  - `WorkspaceID string`

### Beta Webhook Session Idled Event Data

- `type BetaWebhookSessionIdledEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionIdled`

    - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

  - `WorkspaceID string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionOutcomeEvaluationEnded`

    - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

  - `WorkspaceID string`

### Beta Webhook Session Pending Event Data

- `type BetaWebhookSessionPendingEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionPending`

    - `const SessionPendingSessionPending SessionPending = "session.pending"`

  - `WorkspaceID string`

### Beta Webhook Session Requires Action Event Data

- `type BetaWebhookSessionRequiresActionEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionRequiresAction`

    - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

  - `WorkspaceID string`

### Beta Webhook Session Running Event Data

- `type BetaWebhookSessionRunningEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionRunning`

    - `const SessionRunningSessionRunning SessionRunning = "session.running"`

  - `WorkspaceID string`

### Beta Webhook Session Status Idled Event Data

- `type BetaWebhookSessionStatusIdledEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusIdled`

    - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

  - `WorkspaceID string`

### Beta Webhook Session Status Run Started Event Data

- `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusRunStarted`

    - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

  - `WorkspaceID string`

### Beta Webhook Session Status Scheduled Event Data

- `type BetaWebhookSessionStatusScheduledEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusScheduled`

    - `const SessionStatusScheduledSessionStatusScheduled SessionStatusScheduled = "session.status_scheduled"`

  - `WorkspaceID string`

### Beta Webhook Session Status Terminated Event Data

- `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusTerminated`

    - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

  - `WorkspaceID string`

### Beta Webhook Session Thread Created Event Data

- `type BetaWebhookSessionThreadCreatedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionThreadCreated`

    - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

  - `WorkspaceID string`

### Beta Webhook Session Thread Idled Event Data

- `type BetaWebhookSessionThreadIdledEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionThreadIdled`

    - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

  - `WorkspaceID string`

### Beta Webhook Session Thread Terminated Event Data

- `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type SessionThreadTerminated`

    - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

  - `WorkspaceID string`

### Beta Webhook Vault Archived Event Data

- `type BetaWebhookVaultArchivedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type VaultArchived`

    - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

  - `WorkspaceID string`

### Beta Webhook Vault Created Event Data

- `type BetaWebhookVaultCreatedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type VaultCreated`

    - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

  - `WorkspaceID string`

### Beta Webhook Vault Credential Archived Event Data

- `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialArchived`

    - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Created Event Data

- `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialCreated`

    - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Deleted Event Data

- `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialDeleted`

    - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialRefreshFailed`

    - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Deleted Event Data

- `type BetaWebhookVaultDeletedEventData struct{…}`

  - `ID string`

    ID of the resource that triggered the event.

  - `OrganizationID string`

  - `Type VaultDeleted`

    - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

  - `WorkspaceID string`

### Unwrap Webhook Event

- `type UnwrapWebhookEvent struct{…}`

  - `ID string`

    Unique event identifier for idempotency.

  - `CreatedAt Time`

    RFC 3339 timestamp when the event occurred.

  - `Data BetaWebhookEventDataUnion`

    - `type BetaWebhookSessionCreatedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionCreated`

        - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionPendingEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionPending`

        - `const SessionPendingSessionPending SessionPending = "session.pending"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRunningEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionRunning`

        - `const SessionRunningSessionRunning SessionRunning = "session.running"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionIdledEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionIdled`

        - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRequiresActionEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionRequiresAction`

        - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionArchivedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionArchived`

        - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionDeletedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionDeleted`

        - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusScheduledEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusScheduled`

        - `const SessionStatusScheduledSessionStatusScheduled SessionStatusScheduled = "session.status_scheduled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRunStarted`

        - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusIdledEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusIdled`

        - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusTerminated`

        - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionThreadCreated`

        - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadIdledEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionThreadIdled`

        - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionThreadTerminated`

        - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type SessionOutcomeEvaluationEnded`

        - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCreatedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultCreated`

        - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultArchivedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultArchived`

        - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultDeletedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultDeleted`

        - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialCreated`

        - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialArchived`

        - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialDeleted`

        - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

      - `ID string`

        ID of the resource that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialRefreshFailed`

        - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

  - `Type Event`

    Object type. Always `event` for webhook payloads.

    - `const EventEvent Event = "event"`

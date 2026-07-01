# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `type BetaWebhookAgentArchivedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentArchived`

    - `const AgentArchivedAgentArchived AgentArchived = "agent.archived"`

  - `WorkspaceID string`

### Beta Webhook Agent Created Event Data

- `type BetaWebhookAgentCreatedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentCreated`

    - `const AgentCreatedAgentCreated AgentCreated = "agent.created"`

  - `WorkspaceID string`

### Beta Webhook Agent Deleted Event Data

- `type BetaWebhookAgentDeletedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentDeleted`

    - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

  - `WorkspaceID string`

### Beta Webhook Agent Updated Event Data

- `type BetaWebhookAgentUpdatedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentUpdated`

    - `const AgentUpdatedAgentUpdated AgentUpdated = "agent.updated"`

  - `WorkspaceID string`

### Beta Webhook Deployment Archived Event Data

- `type BetaWebhookDeploymentArchivedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentArchived`

    - `const DeploymentArchivedDeploymentArchived DeploymentArchived = "deployment.archived"`

  - `WorkspaceID string`

### Beta Webhook Deployment Created Event Data

- `type BetaWebhookDeploymentCreatedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentCreated`

    - `const DeploymentCreatedDeploymentCreated DeploymentCreated = "deployment.created"`

  - `WorkspaceID string`

### Beta Webhook Deployment Deleted Event Data

- `type BetaWebhookDeploymentDeletedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentDeleted`

    - `const DeploymentDeletedDeploymentDeleted DeploymentDeleted = "deployment.deleted"`

  - `WorkspaceID string`

### Beta Webhook Deployment Paused Event Data

- `type BetaWebhookDeploymentPausedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentPaused`

    - `const DeploymentPausedDeploymentPaused DeploymentPaused = "deployment.paused"`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Failed Event Data

- `type BetaWebhookDeploymentRunFailedEventData struct{…}`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentRunFailed`

    - `const DeploymentRunFailedDeploymentRunFailed DeploymentRunFailed = "deployment_run.failed"`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Started Event Data

- `type BetaWebhookDeploymentRunStartedEventData struct{…}`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentRunStarted`

    - `const DeploymentRunStartedDeploymentRunStarted DeploymentRunStarted = "deployment_run.started"`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Succeeded Event Data

- `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentRunSucceeded`

    - `const DeploymentRunSucceededDeploymentRunSucceeded DeploymentRunSucceeded = "deployment_run.succeeded"`

  - `WorkspaceID string`

### Beta Webhook Deployment Unpaused Event Data

- `type BetaWebhookDeploymentUnpausedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentUnpaused`

    - `const DeploymentUnpausedDeploymentUnpaused DeploymentUnpaused = "deployment.unpaused"`

  - `WorkspaceID string`

### Beta Webhook Deployment Updated Event Data

- `type BetaWebhookDeploymentUpdatedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentUpdated`

    - `const DeploymentUpdatedDeploymentUpdated DeploymentUpdated = "deployment.updated"`

  - `WorkspaceID string`

### Beta Webhook Environment Archived Event Data

- `type BetaWebhookEnvironmentArchivedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentArchived`

    - `const EnvironmentArchivedEnvironmentArchived EnvironmentArchived = "environment.archived"`

  - `WorkspaceID string`

### Beta Webhook Environment Created Event Data

- `type BetaWebhookEnvironmentCreatedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentCreated`

    - `const EnvironmentCreatedEnvironmentCreated EnvironmentCreated = "environment.created"`

  - `WorkspaceID string`

### Beta Webhook Environment Deleted Event Data

- `type BetaWebhookEnvironmentDeletedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type BetaWebhookEnvironmentDeletedEventType`

    - `const BetaWebhookEnvironmentDeletedEventTypeEnvironmentDeleted BetaWebhookEnvironmentDeletedEventType = "environment.deleted"`

  - `WorkspaceID string`

### Beta Webhook Environment Deleted Event Type

- `type BetaWebhookEnvironmentDeletedEventType string`

  - `const BetaWebhookEnvironmentDeletedEventTypeEnvironmentDeleted BetaWebhookEnvironmentDeletedEventType = "environment.deleted"`

### Beta Webhook Environment Updated Event Data

- `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentUpdated`

    - `const EnvironmentUpdatedEnvironmentUpdated EnvironmentUpdated = "environment.updated"`

  - `WorkspaceID string`

### Beta Webhook Event

- `type BetaWebhookEvent struct{…}`

  - `ID string`

    Unique event identifier for idempotency.

  - `CreatedAt Time`

    RFC 3339 timestamp when the event occurred.

  - `Data BetaWebhookEventDataUnion`

    - `type BetaWebhookSessionCreatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionCreated`

        - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionPendingEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionPending`

        - `const SessionPendingSessionPending SessionPending = "session.pending"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRunningEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRunning`

        - `const SessionRunningSessionRunning SessionRunning = "session.running"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionIdled`

        - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRequiresActionEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRequiresAction`

        - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionArchivedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionArchived`

        - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionDeletedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionDeleted`

        - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRescheduled`

        - `const SessionStatusRescheduledSessionStatusRescheduled SessionStatusRescheduled = "session.status_rescheduled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRunStarted`

        - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusIdled`

        - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusTerminated`

        - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadCreated`

        - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadIdled`

        - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadTerminated`

        - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionOutcomeEvaluationEnded`

        - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCreatedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultCreated`

        - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultArchivedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultArchived`

        - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultDeletedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultDeleted`

        - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialCreated`

        - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialArchived`

        - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialDeleted`

        - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialRefreshFailed`

        - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookSessionUpdatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionUpdated`

        - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentCreatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentCreated`

        - `const AgentCreatedAgentCreated AgentCreated = "agent.created"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentArchivedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentArchived`

        - `const AgentArchivedAgentArchived AgentArchived = "agent.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentDeletedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentDeleted`

        - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentPausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentPaused`

        - `const DeploymentPausedDeploymentPaused DeploymentPaused = "deployment.paused"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunFailedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunFailed`

        - `const DeploymentRunFailedDeploymentRunFailed DeploymentRunFailed = "deployment_run.failed"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentCreatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentCreated`

        - `const DeploymentCreatedDeploymentCreated DeploymentCreated = "deployment.created"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUpdatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUpdated`

        - `const DeploymentUpdatedDeploymentUpdated DeploymentUpdated = "deployment.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUnpausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUnpaused`

        - `const DeploymentUnpausedDeploymentUnpaused DeploymentUnpaused = "deployment.unpaused"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentUpdatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentUpdated`

        - `const AgentUpdatedAgentUpdated AgentUpdated = "agent.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentArchivedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentArchived`

        - `const DeploymentArchivedDeploymentArchived DeploymentArchived = "deployment.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunStartedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunStarted`

        - `const DeploymentRunStartedDeploymentRunStarted DeploymentRunStarted = "deployment_run.started"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentDeletedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentDeleted`

        - `const DeploymentDeletedDeploymentDeleted DeploymentDeleted = "deployment.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunSucceeded`

        - `const DeploymentRunSucceededDeploymentRunSucceeded DeploymentRunSucceeded = "deployment_run.succeeded"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentCreatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentCreated`

        - `const EnvironmentCreatedEnvironmentCreated EnvironmentCreated = "environment.created"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentUpdated`

        - `const EnvironmentUpdatedEnvironmentUpdated EnvironmentUpdated = "environment.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentArchivedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentArchived`

        - `const EnvironmentArchivedEnvironmentArchived EnvironmentArchived = "environment.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentDeletedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type BetaWebhookEnvironmentDeletedEventType`

        - `const BetaWebhookEnvironmentDeletedEventTypeEnvironmentDeleted BetaWebhookEnvironmentDeletedEventType = "environment.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreCreated`

        - `const MemoryStoreCreatedMemoryStoreCreated MemoryStoreCreated = "memory_store.created"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreArchived`

        - `const MemoryStoreArchivedMemoryStoreArchived MemoryStoreArchived = "memory_store.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreDeleted`

        - `const MemoryStoreDeletedMemoryStoreDeleted MemoryStoreDeleted = "memory_store.deleted"`

      - `WorkspaceID string`

  - `Type Event`

    Object type. Always `event` for webhook payloads.

    - `const EventEvent Event = "event"`

### Beta Webhook Event Data

- `type BetaWebhookEventDataUnion interface{…}`

  - `type BetaWebhookSessionCreatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionCreated`

      - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionPendingEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionPending`

      - `const SessionPendingSessionPending SessionPending = "session.pending"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRunningEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionRunning`

      - `const SessionRunningSessionRunning SessionRunning = "session.running"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionIdledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionIdled`

      - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRequiresActionEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionRequiresAction`

      - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionArchivedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionArchived`

      - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionDeletedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionDeleted`

      - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusRescheduled`

      - `const SessionStatusRescheduledSessionStatusRescheduled SessionStatusRescheduled = "session.status_rescheduled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusRunStarted`

      - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusIdledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusIdled`

      - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusTerminated`

      - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `Type SessionThreadCreated`

      - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadIdledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `Type SessionThreadIdled`

      - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `Type SessionThreadTerminated`

      - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionOutcomeEvaluationEnded`

      - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCreatedEventData struct{…}`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `Type VaultCreated`

      - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultArchivedEventData struct{…}`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `Type VaultArchived`

      - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultDeletedEventData struct{…}`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `Type VaultDeleted`

      - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialCreated`

      - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialArchived`

      - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialDeleted`

      - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialRefreshFailed`

      - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookSessionUpdatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionUpdated`

      - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

    - `WorkspaceID string`

  - `type BetaWebhookAgentCreatedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentCreated`

      - `const AgentCreatedAgentCreated AgentCreated = "agent.created"`

    - `WorkspaceID string`

  - `type BetaWebhookAgentArchivedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentArchived`

      - `const AgentArchivedAgentArchived AgentArchived = "agent.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookAgentDeletedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentDeleted`

      - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentPausedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentPaused`

      - `const DeploymentPausedDeploymentPaused DeploymentPaused = "deployment.paused"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunFailedEventData struct{…}`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentRunFailed`

      - `const DeploymentRunFailedDeploymentRunFailed DeploymentRunFailed = "deployment_run.failed"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentCreatedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentCreated`

      - `const DeploymentCreatedDeploymentCreated DeploymentCreated = "deployment.created"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentUpdatedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentUpdated`

      - `const DeploymentUpdatedDeploymentUpdated DeploymentUpdated = "deployment.updated"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentUnpausedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentUnpaused`

      - `const DeploymentUnpausedDeploymentUnpaused DeploymentUnpaused = "deployment.unpaused"`

    - `WorkspaceID string`

  - `type BetaWebhookAgentUpdatedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentUpdated`

      - `const AgentUpdatedAgentUpdated AgentUpdated = "agent.updated"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentArchivedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentArchived`

      - `const DeploymentArchivedDeploymentArchived DeploymentArchived = "deployment.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunStartedEventData struct{…}`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentRunStarted`

      - `const DeploymentRunStartedDeploymentRunStarted DeploymentRunStarted = "deployment_run.started"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentDeletedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentDeleted`

      - `const DeploymentDeletedDeploymentDeleted DeploymentDeleted = "deployment.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentRunSucceeded`

      - `const DeploymentRunSucceededDeploymentRunSucceeded DeploymentRunSucceeded = "deployment_run.succeeded"`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentCreatedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentCreated`

      - `const EnvironmentCreatedEnvironmentCreated EnvironmentCreated = "environment.created"`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentUpdated`

      - `const EnvironmentUpdatedEnvironmentUpdated EnvironmentUpdated = "environment.updated"`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentArchivedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentArchived`

      - `const EnvironmentArchivedEnvironmentArchived EnvironmentArchived = "environment.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentDeletedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type BetaWebhookEnvironmentDeletedEventType`

      - `const BetaWebhookEnvironmentDeletedEventTypeEnvironmentDeleted BetaWebhookEnvironmentDeletedEventType = "environment.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `Type MemoryStoreCreated`

      - `const MemoryStoreCreatedMemoryStoreCreated MemoryStoreCreated = "memory_store.created"`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `Type MemoryStoreArchived`

      - `const MemoryStoreArchivedMemoryStoreArchived MemoryStoreArchived = "memory_store.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `Type MemoryStoreDeleted`

      - `const MemoryStoreDeletedMemoryStoreDeleted MemoryStoreDeleted = "memory_store.deleted"`

    - `WorkspaceID string`

### Beta Webhook Memory Store Archived Event Data

- `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `Type MemoryStoreArchived`

    - `const MemoryStoreArchivedMemoryStoreArchived MemoryStoreArchived = "memory_store.archived"`

  - `WorkspaceID string`

### Beta Webhook Memory Store Created Event Data

- `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `Type MemoryStoreCreated`

    - `const MemoryStoreCreatedMemoryStoreCreated MemoryStoreCreated = "memory_store.created"`

  - `WorkspaceID string`

### Beta Webhook Memory Store Deleted Event Data

- `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `Type MemoryStoreDeleted`

    - `const MemoryStoreDeletedMemoryStoreDeleted MemoryStoreDeleted = "memory_store.deleted"`

  - `WorkspaceID string`

### Beta Webhook Session Archived Event Data

- `type BetaWebhookSessionArchivedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionArchived`

    - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

  - `WorkspaceID string`

### Beta Webhook Session Created Event Data

- `type BetaWebhookSessionCreatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionCreated`

    - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

  - `WorkspaceID string`

### Beta Webhook Session Deleted Event Data

- `type BetaWebhookSessionDeletedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionDeleted`

    - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

  - `WorkspaceID string`

### Beta Webhook Session Idled Event Data

- `type BetaWebhookSessionIdledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionIdled`

    - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

  - `WorkspaceID string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionOutcomeEvaluationEnded`

    - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

  - `WorkspaceID string`

### Beta Webhook Session Pending Event Data

- `type BetaWebhookSessionPendingEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionPending`

    - `const SessionPendingSessionPending SessionPending = "session.pending"`

  - `WorkspaceID string`

### Beta Webhook Session Requires Action Event Data

- `type BetaWebhookSessionRequiresActionEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionRequiresAction`

    - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

  - `WorkspaceID string`

### Beta Webhook Session Running Event Data

- `type BetaWebhookSessionRunningEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionRunning`

    - `const SessionRunningSessionRunning SessionRunning = "session.running"`

  - `WorkspaceID string`

### Beta Webhook Session Status Idled Event Data

- `type BetaWebhookSessionStatusIdledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusIdled`

    - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

  - `WorkspaceID string`

### Beta Webhook Session Status Rescheduled Event Data

- `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusRescheduled`

    - `const SessionStatusRescheduledSessionStatusRescheduled SessionStatusRescheduled = "session.status_rescheduled"`

  - `WorkspaceID string`

### Beta Webhook Session Status Run Started Event Data

- `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusRunStarted`

    - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

  - `WorkspaceID string`

### Beta Webhook Session Status Terminated Event Data

- `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusTerminated`

    - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

  - `WorkspaceID string`

### Beta Webhook Session Thread Created Event Data

- `type BetaWebhookSessionThreadCreatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `Type SessionThreadCreated`

    - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

  - `WorkspaceID string`

### Beta Webhook Session Thread Idled Event Data

- `type BetaWebhookSessionThreadIdledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `Type SessionThreadIdled`

    - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

  - `WorkspaceID string`

### Beta Webhook Session Thread Terminated Event Data

- `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `Type SessionThreadTerminated`

    - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

  - `WorkspaceID string`

### Beta Webhook Session Updated Event Data

- `type BetaWebhookSessionUpdatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionUpdated`

    - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

  - `WorkspaceID string`

### Beta Webhook Vault Archived Event Data

- `type BetaWebhookVaultArchivedEventData struct{…}`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `Type VaultArchived`

    - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

  - `WorkspaceID string`

### Beta Webhook Vault Created Event Data

- `type BetaWebhookVaultCreatedEventData struct{…}`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `Type VaultCreated`

    - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

  - `WorkspaceID string`

### Beta Webhook Vault Credential Archived Event Data

- `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialArchived`

    - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Created Event Data

- `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialCreated`

    - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Deleted Event Data

- `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialDeleted`

    - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialRefreshFailed`

    - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Deleted Event Data

- `type BetaWebhookVaultDeletedEventData struct{…}`

  - `ID string`

    ID of the vault that triggered the event.

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

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionCreated`

        - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionPendingEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionPending`

        - `const SessionPendingSessionPending SessionPending = "session.pending"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRunningEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRunning`

        - `const SessionRunningSessionRunning SessionRunning = "session.running"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionIdled`

        - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRequiresActionEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRequiresAction`

        - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionArchivedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionArchived`

        - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionDeletedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionDeleted`

        - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRescheduled`

        - `const SessionStatusRescheduledSessionStatusRescheduled SessionStatusRescheduled = "session.status_rescheduled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRunStarted`

        - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusIdled`

        - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusTerminated`

        - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadCreated`

        - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadIdled`

        - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadTerminated`

        - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionOutcomeEvaluationEnded`

        - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCreatedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultCreated`

        - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultArchivedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultArchived`

        - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultDeletedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultDeleted`

        - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialCreated`

        - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialArchived`

        - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialDeleted`

        - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialRefreshFailed`

        - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookSessionUpdatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionUpdated`

        - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentCreatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentCreated`

        - `const AgentCreatedAgentCreated AgentCreated = "agent.created"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentArchivedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentArchived`

        - `const AgentArchivedAgentArchived AgentArchived = "agent.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentDeletedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentDeleted`

        - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentPausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentPaused`

        - `const DeploymentPausedDeploymentPaused DeploymentPaused = "deployment.paused"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunFailedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunFailed`

        - `const DeploymentRunFailedDeploymentRunFailed DeploymentRunFailed = "deployment_run.failed"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentCreatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentCreated`

        - `const DeploymentCreatedDeploymentCreated DeploymentCreated = "deployment.created"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUpdatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUpdated`

        - `const DeploymentUpdatedDeploymentUpdated DeploymentUpdated = "deployment.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUnpausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUnpaused`

        - `const DeploymentUnpausedDeploymentUnpaused DeploymentUnpaused = "deployment.unpaused"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentUpdatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentUpdated`

        - `const AgentUpdatedAgentUpdated AgentUpdated = "agent.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentArchivedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentArchived`

        - `const DeploymentArchivedDeploymentArchived DeploymentArchived = "deployment.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunStartedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunStarted`

        - `const DeploymentRunStartedDeploymentRunStarted DeploymentRunStarted = "deployment_run.started"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentDeletedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentDeleted`

        - `const DeploymentDeletedDeploymentDeleted DeploymentDeleted = "deployment.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunSucceeded`

        - `const DeploymentRunSucceededDeploymentRunSucceeded DeploymentRunSucceeded = "deployment_run.succeeded"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentCreatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentCreated`

        - `const EnvironmentCreatedEnvironmentCreated EnvironmentCreated = "environment.created"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentUpdated`

        - `const EnvironmentUpdatedEnvironmentUpdated EnvironmentUpdated = "environment.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentArchivedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentArchived`

        - `const EnvironmentArchivedEnvironmentArchived EnvironmentArchived = "environment.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentDeletedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type BetaWebhookEnvironmentDeletedEventType`

        - `const BetaWebhookEnvironmentDeletedEventTypeEnvironmentDeleted BetaWebhookEnvironmentDeletedEventType = "environment.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreCreated`

        - `const MemoryStoreCreatedMemoryStoreCreated MemoryStoreCreated = "memory_store.created"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreArchived`

        - `const MemoryStoreArchivedMemoryStoreArchived MemoryStoreArchived = "memory_store.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreDeleted`

        - `const MemoryStoreDeletedMemoryStoreDeleted MemoryStoreDeleted = "memory_store.deleted"`

      - `WorkspaceID string`

  - `Type Event`

    Object type. Always `event` for webhook payloads.

    - `const EventEvent Event = "event"`

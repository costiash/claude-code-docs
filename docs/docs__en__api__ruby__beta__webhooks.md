# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData`

  - `id: String`

    ID of the agent that triggered the event.

  - `organization_id: String`

  - `type: :"agent.archived"`

    - `:"agent.archived"`

  - `workspace_id: String`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData`

  - `id: String`

    ID of the agent that triggered the event.

  - `organization_id: String`

  - `type: :"agent.created"`

    - `:"agent.created"`

  - `workspace_id: String`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData`

  - `id: String`

    ID of the agent that triggered the event.

  - `organization_id: String`

  - `type: :"agent.deleted"`

    - `:"agent.deleted"`

  - `workspace_id: String`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData`

  - `id: String`

    ID of the agent that triggered the event.

  - `organization_id: String`

  - `type: :"agent.updated"`

    - `:"agent.updated"`

  - `workspace_id: String`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `type: :"deployment.archived"`

    - `:"deployment.archived"`

  - `workspace_id: String`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `type: :"deployment.created"`

    - `:"deployment.created"`

  - `workspace_id: String`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `type: :"deployment.deleted"`

    - `:"deployment.deleted"`

  - `workspace_id: String`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `type: :"deployment.paused"`

    - `:"deployment.paused"`

  - `workspace_id: String`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData`

  - `id: String`

    ID of the deployment run that triggered the event.

  - `organization_id: String`

  - `type: :"deployment_run.failed"`

    - `:"deployment_run.failed"`

  - `workspace_id: String`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData`

  - `id: String`

    ID of the deployment run that triggered the event.

  - `organization_id: String`

  - `type: :"deployment_run.started"`

    - `:"deployment_run.started"`

  - `workspace_id: String`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData`

  - `id: String`

    ID of the deployment run that triggered the event.

  - `organization_id: String`

  - `type: :"deployment_run.succeeded"`

    - `:"deployment_run.succeeded"`

  - `workspace_id: String`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `type: :"deployment.unpaused"`

    - `:"deployment.unpaused"`

  - `workspace_id: String`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `type: :"deployment.updated"`

    - `:"deployment.updated"`

  - `workspace_id: String`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData`

  - `id: String`

    ID of the environment that triggered the event.

  - `organization_id: String`

  - `type: :"environment.archived"`

    - `:"environment.archived"`

  - `workspace_id: String`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData`

  - `id: String`

    ID of the environment that triggered the event.

  - `organization_id: String`

  - `type: :"environment.created"`

    - `:"environment.created"`

  - `workspace_id: String`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData`

  - `id: String`

    ID of the environment that triggered the event.

  - `organization_id: String`

  - `type: BetaWebhookEnvironmentDeletedEventType`

    - `:"environment.deleted"`

  - `workspace_id: String`

### Beta Webhook Environment Deleted Event Type

- `BetaWebhookEnvironmentDeletedEventType = :"environment.deleted"`

  - `:"environment.deleted"`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData`

  - `id: String`

    ID of the environment that triggered the event.

  - `organization_id: String`

  - `type: :"environment.updated"`

    - `:"environment.updated"`

  - `workspace_id: String`

### Beta Webhook Event

- `class BetaWebhookEvent`

  - `id: String`

    Unique event identifier for idempotency.

  - `created_at: Time`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.created"`

        - `:"session.created"`

      - `workspace_id: String`

    - `class BetaWebhookSessionPendingEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.pending"`

        - `:"session.pending"`

      - `workspace_id: String`

    - `class BetaWebhookSessionRunningEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.running"`

        - `:"session.running"`

      - `workspace_id: String`

    - `class BetaWebhookSessionIdledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.idled"`

        - `:"session.idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionRequiresActionEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.requires_action"`

        - `:"session.requires_action"`

      - `workspace_id: String`

    - `class BetaWebhookSessionArchivedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.archived"`

        - `:"session.archived"`

      - `workspace_id: String`

    - `class BetaWebhookSessionDeletedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.deleted"`

        - `:"session.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRescheduledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_rescheduled"`

        - `:"session.status_rescheduled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRunStartedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_run_started"`

        - `:"session.status_run_started"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusIdledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_idled"`

        - `:"session.status_idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusTerminatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_terminated"`

        - `:"session.status_terminated"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadCreatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `type: :"session.thread_created"`

        - `:"session.thread_created"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadIdledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `type: :"session.thread_idled"`

        - `:"session.thread_idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadTerminatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `type: :"session.thread_terminated"`

        - `:"session.thread_terminated"`

      - `workspace_id: String`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.outcome_evaluation_ended"`

        - `:"session.outcome_evaluation_ended"`

      - `workspace_id: String`

    - `class BetaWebhookVaultCreatedEventData`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `type: :"vault.created"`

        - `:"vault.created"`

      - `workspace_id: String`

    - `class BetaWebhookVaultArchivedEventData`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `type: :"vault.archived"`

        - `:"vault.archived"`

      - `workspace_id: String`

    - `class BetaWebhookVaultDeletedEventData`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `type: :"vault.deleted"`

        - `:"vault.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialCreatedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.created"`

        - `:"vault_credential.created"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialArchivedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.archived"`

        - `:"vault_credential.archived"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialDeletedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.deleted"`

        - `:"vault_credential.deleted"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.refresh_failed"`

        - `:"vault_credential.refresh_failed"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookSessionUpdatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.updated"`

        - `:"session.updated"`

      - `workspace_id: String`

    - `class BetaWebhookAgentCreatedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.created"`

        - `:"agent.created"`

      - `workspace_id: String`

    - `class BetaWebhookAgentArchivedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.archived"`

        - `:"agent.archived"`

      - `workspace_id: String`

    - `class BetaWebhookAgentDeletedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.deleted"`

        - `:"agent.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentPausedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.paused"`

        - `:"deployment.paused"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunFailedEventData`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `type: :"deployment_run.failed"`

        - `:"deployment_run.failed"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentCreatedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.created"`

        - `:"deployment.created"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentUpdatedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.updated"`

        - `:"deployment.updated"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentUnpausedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.unpaused"`

        - `:"deployment.unpaused"`

      - `workspace_id: String`

    - `class BetaWebhookAgentUpdatedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.updated"`

        - `:"agent.updated"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentArchivedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.archived"`

        - `:"deployment.archived"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunStartedEventData`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `type: :"deployment_run.started"`

        - `:"deployment_run.started"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentDeletedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.deleted"`

        - `:"deployment.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunSucceededEventData`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `type: :"deployment_run.succeeded"`

        - `:"deployment_run.succeeded"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentCreatedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.created"`

        - `:"environment.created"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentUpdatedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.updated"`

        - `:"environment.updated"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentArchivedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.archived"`

        - `:"environment.archived"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentDeletedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: BetaWebhookEnvironmentDeletedEventType`

        - `:"environment.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreCreatedEventData`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `type: :"memory_store.created"`

        - `:"memory_store.created"`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreArchivedEventData`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `type: :"memory_store.archived"`

        - `:"memory_store.archived"`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreDeletedEventData`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `type: :"memory_store.deleted"`

        - `:"memory_store.deleted"`

      - `workspace_id: String`

  - `type: :event`

    Object type. Always `event` for webhook payloads.

    - `:event`

### Beta Webhook Event Data

- `BetaWebhookEventData = BetaWebhookSessionCreatedEventData | BetaWebhookSessionPendingEventData | BetaWebhookSessionRunningEventData | 40 more`

  - `class BetaWebhookSessionCreatedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.created"`

      - `:"session.created"`

    - `workspace_id: String`

  - `class BetaWebhookSessionPendingEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.pending"`

      - `:"session.pending"`

    - `workspace_id: String`

  - `class BetaWebhookSessionRunningEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.running"`

      - `:"session.running"`

    - `workspace_id: String`

  - `class BetaWebhookSessionIdledEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.idled"`

      - `:"session.idled"`

    - `workspace_id: String`

  - `class BetaWebhookSessionRequiresActionEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.requires_action"`

      - `:"session.requires_action"`

    - `workspace_id: String`

  - `class BetaWebhookSessionArchivedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.archived"`

      - `:"session.archived"`

    - `workspace_id: String`

  - `class BetaWebhookSessionDeletedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.deleted"`

      - `:"session.deleted"`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusRescheduledEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.status_rescheduled"`

      - `:"session.status_rescheduled"`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusRunStartedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.status_run_started"`

      - `:"session.status_run_started"`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusIdledEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.status_idled"`

      - `:"session.status_idled"`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusTerminatedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.status_terminated"`

      - `:"session.status_terminated"`

    - `workspace_id: String`

  - `class BetaWebhookSessionThreadCreatedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `session_thread_id: String`

      ID of the session thread this event refers to.

    - `type: :"session.thread_created"`

      - `:"session.thread_created"`

    - `workspace_id: String`

  - `class BetaWebhookSessionThreadIdledEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `session_thread_id: String`

      ID of the session thread this event refers to.

    - `type: :"session.thread_idled"`

      - `:"session.thread_idled"`

    - `workspace_id: String`

  - `class BetaWebhookSessionThreadTerminatedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `session_thread_id: String`

      ID of the session thread this event refers to.

    - `type: :"session.thread_terminated"`

      - `:"session.thread_terminated"`

    - `workspace_id: String`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.outcome_evaluation_ended"`

      - `:"session.outcome_evaluation_ended"`

    - `workspace_id: String`

  - `class BetaWebhookVaultCreatedEventData`

    - `id: String`

      ID of the vault that triggered the event.

    - `organization_id: String`

    - `type: :"vault.created"`

      - `:"vault.created"`

    - `workspace_id: String`

  - `class BetaWebhookVaultArchivedEventData`

    - `id: String`

      ID of the vault that triggered the event.

    - `organization_id: String`

    - `type: :"vault.archived"`

      - `:"vault.archived"`

    - `workspace_id: String`

  - `class BetaWebhookVaultDeletedEventData`

    - `id: String`

      ID of the vault that triggered the event.

    - `organization_id: String`

    - `type: :"vault.deleted"`

      - `:"vault.deleted"`

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialCreatedEventData`

    - `id: String`

      ID of the vault credential that triggered the event.

    - `organization_id: String`

    - `type: :"vault_credential.created"`

      - `:"vault_credential.created"`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialArchivedEventData`

    - `id: String`

      ID of the vault credential that triggered the event.

    - `organization_id: String`

    - `type: :"vault_credential.archived"`

      - `:"vault_credential.archived"`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialDeletedEventData`

    - `id: String`

      ID of the vault credential that triggered the event.

    - `organization_id: String`

    - `type: :"vault_credential.deleted"`

      - `:"vault_credential.deleted"`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData`

    - `id: String`

      ID of the vault credential that triggered the event.

    - `organization_id: String`

    - `type: :"vault_credential.refresh_failed"`

      - `:"vault_credential.refresh_failed"`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookSessionUpdatedEventData`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `type: :"session.updated"`

      - `:"session.updated"`

    - `workspace_id: String`

  - `class BetaWebhookAgentCreatedEventData`

    - `id: String`

      ID of the agent that triggered the event.

    - `organization_id: String`

    - `type: :"agent.created"`

      - `:"agent.created"`

    - `workspace_id: String`

  - `class BetaWebhookAgentArchivedEventData`

    - `id: String`

      ID of the agent that triggered the event.

    - `organization_id: String`

    - `type: :"agent.archived"`

      - `:"agent.archived"`

    - `workspace_id: String`

  - `class BetaWebhookAgentDeletedEventData`

    - `id: String`

      ID of the agent that triggered the event.

    - `organization_id: String`

    - `type: :"agent.deleted"`

      - `:"agent.deleted"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentPausedEventData`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `type: :"deployment.paused"`

      - `:"deployment.paused"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentRunFailedEventData`

    - `id: String`

      ID of the deployment run that triggered the event.

    - `organization_id: String`

    - `type: :"deployment_run.failed"`

      - `:"deployment_run.failed"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentCreatedEventData`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `type: :"deployment.created"`

      - `:"deployment.created"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentUpdatedEventData`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `type: :"deployment.updated"`

      - `:"deployment.updated"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentUnpausedEventData`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `type: :"deployment.unpaused"`

      - `:"deployment.unpaused"`

    - `workspace_id: String`

  - `class BetaWebhookAgentUpdatedEventData`

    - `id: String`

      ID of the agent that triggered the event.

    - `organization_id: String`

    - `type: :"agent.updated"`

      - `:"agent.updated"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentArchivedEventData`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `type: :"deployment.archived"`

      - `:"deployment.archived"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentRunStartedEventData`

    - `id: String`

      ID of the deployment run that triggered the event.

    - `organization_id: String`

    - `type: :"deployment_run.started"`

      - `:"deployment_run.started"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentDeletedEventData`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `type: :"deployment.deleted"`

      - `:"deployment.deleted"`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentRunSucceededEventData`

    - `id: String`

      ID of the deployment run that triggered the event.

    - `organization_id: String`

    - `type: :"deployment_run.succeeded"`

      - `:"deployment_run.succeeded"`

    - `workspace_id: String`

  - `class BetaWebhookEnvironmentCreatedEventData`

    - `id: String`

      ID of the environment that triggered the event.

    - `organization_id: String`

    - `type: :"environment.created"`

      - `:"environment.created"`

    - `workspace_id: String`

  - `class BetaWebhookEnvironmentUpdatedEventData`

    - `id: String`

      ID of the environment that triggered the event.

    - `organization_id: String`

    - `type: :"environment.updated"`

      - `:"environment.updated"`

    - `workspace_id: String`

  - `class BetaWebhookEnvironmentArchivedEventData`

    - `id: String`

      ID of the environment that triggered the event.

    - `organization_id: String`

    - `type: :"environment.archived"`

      - `:"environment.archived"`

    - `workspace_id: String`

  - `class BetaWebhookEnvironmentDeletedEventData`

    - `id: String`

      ID of the environment that triggered the event.

    - `organization_id: String`

    - `type: BetaWebhookEnvironmentDeletedEventType`

      - `:"environment.deleted"`

    - `workspace_id: String`

  - `class BetaWebhookMemoryStoreCreatedEventData`

    - `id: String`

      ID of the memory store that triggered the event.

    - `organization_id: String`

    - `type: :"memory_store.created"`

      - `:"memory_store.created"`

    - `workspace_id: String`

  - `class BetaWebhookMemoryStoreArchivedEventData`

    - `id: String`

      ID of the memory store that triggered the event.

    - `organization_id: String`

    - `type: :"memory_store.archived"`

      - `:"memory_store.archived"`

    - `workspace_id: String`

  - `class BetaWebhookMemoryStoreDeletedEventData`

    - `id: String`

      ID of the memory store that triggered the event.

    - `organization_id: String`

    - `type: :"memory_store.deleted"`

      - `:"memory_store.deleted"`

    - `workspace_id: String`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData`

  - `id: String`

    ID of the memory store that triggered the event.

  - `organization_id: String`

  - `type: :"memory_store.archived"`

    - `:"memory_store.archived"`

  - `workspace_id: String`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData`

  - `id: String`

    ID of the memory store that triggered the event.

  - `organization_id: String`

  - `type: :"memory_store.created"`

    - `:"memory_store.created"`

  - `workspace_id: String`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData`

  - `id: String`

    ID of the memory store that triggered the event.

  - `organization_id: String`

  - `type: :"memory_store.deleted"`

    - `:"memory_store.deleted"`

  - `workspace_id: String`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.archived"`

    - `:"session.archived"`

  - `workspace_id: String`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.created"`

    - `:"session.created"`

  - `workspace_id: String`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.deleted"`

    - `:"session.deleted"`

  - `workspace_id: String`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.idled"`

    - `:"session.idled"`

  - `workspace_id: String`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.outcome_evaluation_ended"`

    - `:"session.outcome_evaluation_ended"`

  - `workspace_id: String`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.pending"`

    - `:"session.pending"`

  - `workspace_id: String`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.requires_action"`

    - `:"session.requires_action"`

  - `workspace_id: String`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.running"`

    - `:"session.running"`

  - `workspace_id: String`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.status_idled"`

    - `:"session.status_idled"`

  - `workspace_id: String`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.status_rescheduled"`

    - `:"session.status_rescheduled"`

  - `workspace_id: String`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.status_run_started"`

    - `:"session.status_run_started"`

  - `workspace_id: String`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.status_terminated"`

    - `:"session.status_terminated"`

  - `workspace_id: String`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `session_thread_id: String`

    ID of the session thread this event refers to.

  - `type: :"session.thread_created"`

    - `:"session.thread_created"`

  - `workspace_id: String`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `session_thread_id: String`

    ID of the session thread this event refers to.

  - `type: :"session.thread_idled"`

    - `:"session.thread_idled"`

  - `workspace_id: String`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `session_thread_id: String`

    ID of the session thread this event refers to.

  - `type: :"session.thread_terminated"`

    - `:"session.thread_terminated"`

  - `workspace_id: String`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `type: :"session.updated"`

    - `:"session.updated"`

  - `workspace_id: String`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData`

  - `id: String`

    ID of the vault that triggered the event.

  - `organization_id: String`

  - `type: :"vault.archived"`

    - `:"vault.archived"`

  - `workspace_id: String`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData`

  - `id: String`

    ID of the vault that triggered the event.

  - `organization_id: String`

  - `type: :"vault.created"`

    - `:"vault.created"`

  - `workspace_id: String`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData`

  - `id: String`

    ID of the vault credential that triggered the event.

  - `organization_id: String`

  - `type: :"vault_credential.archived"`

    - `:"vault_credential.archived"`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData`

  - `id: String`

    ID of the vault credential that triggered the event.

  - `organization_id: String`

  - `type: :"vault_credential.created"`

    - `:"vault_credential.created"`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData`

  - `id: String`

    ID of the vault credential that triggered the event.

  - `organization_id: String`

  - `type: :"vault_credential.deleted"`

    - `:"vault_credential.deleted"`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData`

  - `id: String`

    ID of the vault credential that triggered the event.

  - `organization_id: String`

  - `type: :"vault_credential.refresh_failed"`

    - `:"vault_credential.refresh_failed"`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData`

  - `id: String`

    ID of the vault that triggered the event.

  - `organization_id: String`

  - `type: :"vault.deleted"`

    - `:"vault.deleted"`

  - `workspace_id: String`

### Unwrap Webhook Event

- `class UnwrapWebhookEvent`

  - `id: String`

    Unique event identifier for idempotency.

  - `created_at: Time`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.created"`

        - `:"session.created"`

      - `workspace_id: String`

    - `class BetaWebhookSessionPendingEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.pending"`

        - `:"session.pending"`

      - `workspace_id: String`

    - `class BetaWebhookSessionRunningEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.running"`

        - `:"session.running"`

      - `workspace_id: String`

    - `class BetaWebhookSessionIdledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.idled"`

        - `:"session.idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionRequiresActionEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.requires_action"`

        - `:"session.requires_action"`

      - `workspace_id: String`

    - `class BetaWebhookSessionArchivedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.archived"`

        - `:"session.archived"`

      - `workspace_id: String`

    - `class BetaWebhookSessionDeletedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.deleted"`

        - `:"session.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRescheduledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_rescheduled"`

        - `:"session.status_rescheduled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRunStartedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_run_started"`

        - `:"session.status_run_started"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusIdledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_idled"`

        - `:"session.status_idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusTerminatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_terminated"`

        - `:"session.status_terminated"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadCreatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `type: :"session.thread_created"`

        - `:"session.thread_created"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadIdledEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `type: :"session.thread_idled"`

        - `:"session.thread_idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadTerminatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `type: :"session.thread_terminated"`

        - `:"session.thread_terminated"`

      - `workspace_id: String`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.outcome_evaluation_ended"`

        - `:"session.outcome_evaluation_ended"`

      - `workspace_id: String`

    - `class BetaWebhookVaultCreatedEventData`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `type: :"vault.created"`

        - `:"vault.created"`

      - `workspace_id: String`

    - `class BetaWebhookVaultArchivedEventData`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `type: :"vault.archived"`

        - `:"vault.archived"`

      - `workspace_id: String`

    - `class BetaWebhookVaultDeletedEventData`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `type: :"vault.deleted"`

        - `:"vault.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialCreatedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.created"`

        - `:"vault_credential.created"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialArchivedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.archived"`

        - `:"vault_credential.archived"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialDeletedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.deleted"`

        - `:"vault_credential.deleted"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.refresh_failed"`

        - `:"vault_credential.refresh_failed"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookSessionUpdatedEventData`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `type: :"session.updated"`

        - `:"session.updated"`

      - `workspace_id: String`

    - `class BetaWebhookAgentCreatedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.created"`

        - `:"agent.created"`

      - `workspace_id: String`

    - `class BetaWebhookAgentArchivedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.archived"`

        - `:"agent.archived"`

      - `workspace_id: String`

    - `class BetaWebhookAgentDeletedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.deleted"`

        - `:"agent.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentPausedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.paused"`

        - `:"deployment.paused"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunFailedEventData`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `type: :"deployment_run.failed"`

        - `:"deployment_run.failed"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentCreatedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.created"`

        - `:"deployment.created"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentUpdatedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.updated"`

        - `:"deployment.updated"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentUnpausedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.unpaused"`

        - `:"deployment.unpaused"`

      - `workspace_id: String`

    - `class BetaWebhookAgentUpdatedEventData`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `type: :"agent.updated"`

        - `:"agent.updated"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentArchivedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.archived"`

        - `:"deployment.archived"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunStartedEventData`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `type: :"deployment_run.started"`

        - `:"deployment_run.started"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentDeletedEventData`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `type: :"deployment.deleted"`

        - `:"deployment.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunSucceededEventData`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `type: :"deployment_run.succeeded"`

        - `:"deployment_run.succeeded"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentCreatedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.created"`

        - `:"environment.created"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentUpdatedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.updated"`

        - `:"environment.updated"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentArchivedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: :"environment.archived"`

        - `:"environment.archived"`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentDeletedEventData`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `type: BetaWebhookEnvironmentDeletedEventType`

        - `:"environment.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreCreatedEventData`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `type: :"memory_store.created"`

        - `:"memory_store.created"`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreArchivedEventData`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `type: :"memory_store.archived"`

        - `:"memory_store.archived"`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreDeletedEventData`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `type: :"memory_store.deleted"`

        - `:"memory_store.deleted"`

      - `workspace_id: String`

  - `type: :event`

    Object type. Always `event` for webhook payloads.

    - `:event`

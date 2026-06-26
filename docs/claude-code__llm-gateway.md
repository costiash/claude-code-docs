> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM gateways

> Route Claude Code through an LLM gateway for centralized authentication, usage tracking, and cost controls. Covers connecting Claude Code to a gateway, rolling one out for your organization, what Claude Code sends to a gateway, and how gateways interact with claude.ai subscriptions.

An LLM gateway is a proxy your organization runs between Claude Code and a model provider. Claude Code sends API traffic to the gateway, and the gateway forwards it to the provider using a credential your organization controls.

<Note>
  * If you're a developer connecting to an existing gateway: [connect Claude Code to your gateway](/en/llm-gateway-connect)
  * If you're an admin rolling out a gateway for your organization: [deploy and distribute a gateway](/en/llm-gateway-rollout)
  * If you're configuring a gateway product: the [gateway protocol reference](/en/llm-gateway-protocol)
</Note>

## What a gateway provides

A gateway gives your organization one place to manage:

* **Credentials**: the provider key stays server-side; developers hold gateway credentials instead
* **Usage tracking**: attribute usage by developer or team, regardless of which provider serves the request
* **Cost controls**: enforce budgets and rate limits in one place
* **Audit logging**: log every model request for compliance
* **Provider switching**: change the provider in gateway configuration, without touching developer machines

All of these except provider switching apply whether the upstream is Anthropic's API or a [cloud provider](/en/third-party-integrations).

The tradeoff is that the gateway becomes infrastructure your organization operates. Claude Code adds capabilities with each release, and a gateway that doesn't forward them breaks the corresponding features, so the gateway product needs to be kept updated as Claude Code evolves. The [gateway protocol reference](/en/llm-gateway-protocol) covers what to forward.

## How a gateway works

By default, Claude Code sends requests directly to Anthropic's API at `api.anthropic.com`. To route through a gateway, set `ANTHROPIC_BASE_URL` to the gateway's address; Claude Code sends the same requests there instead. The gateway authenticates the developer, attaches your organization's provider credential, and forwards each request to whichever provider it's configured for.

`ANTHROPIC_BASE_URL` is the address variable for most gateways. A gateway that fronts a specific cloud provider, such as Bedrock, Vertex, Foundry, or the Claude Platform on AWS, uses that provider's base URL variable instead; [API formats](/en/llm-gateway-protocol#api-formats) lists which variable goes with each configuration.

<Frame>
  <img src="https://mintcdn.com/claude-code/zIcIE_SQv4Z0Zbhc/images/llm-gateway-flow.svg?fit=max&auto=format&n=zIcIE_SQv4Z0Zbhc&q=85&s=490607d033d235694efb49a73a5b9e4b" alt="Diagram showing Claude Code routing through an LLM gateway. In a developer machines zone, the Claude Code CLI, VS Code extension, and CI or Agent SDK clients send requests to the gateway, with the base URL variable for the gateway's API format pointing at it and each developer holding a per-developer credential, and the desktop app reaches the same gateway through organization-distributed configuration. In a zone labeled your infrastructure, the LLM gateway handles authentication, usage tracking, budgets, and routing, and forwards requests with your organization's credential. In a model providers zone, a solid arrow leads to the provider you configure, shown as the Anthropic API, and dashed arrows lead to other provider options, illustrated with Amazon Bedrock, Google Vertex AI, and Microsoft Foundry as examples." width="780" height="322" data-path="images/llm-gateway-flow.svg" />
</Frame>

Two kinds of credential are involved:

* **Developer credentials**: each developer holds their own, issued by the gateway. It authenticates them to the gateway and identifies them in usage tracking
* **Provider credential**: the gateway holds one credential for your provider account, shared by all forwarded traffic. You don't provision provider keys per developer

The gateway forwards each request to the provider you configure, such as the Anthropic API, [Amazon Bedrock](/en/amazon-bedrock), [Google Vertex AI](/en/google-vertex-ai), [Microsoft Foundry](/en/microsoft-foundry), or the [Claude Platform on AWS](/en/claude-platform-on-aws). Because Claude Code talks only to the gateway, the provider choice is the gateway's configuration, not the client's.

## Roll out a gateway

When you're ready to roll out an LLM gateway to your organization, the sequence is the same whichever gateway product you choose:

1. Deploy the gateway and give it your provider credential, so it can authenticate the requests it forwards.
2. Issue each developer a gateway credential, so usage is attributed to the developer and offboarding revokes one credential.
3. Distribute the configuration through a [managed settings file](/en/settings#settings-files) and your secrets tooling, so every machine receives the base URL and a credential. When both are distributed, developers don't configure anything. If you don't have settings distribution in place, developers follow the [connect page](/en/llm-gateway-connect) to set the variables themselves.
4. Have each developer [check for the configuration in Claude Code](/en/llm-gateway-connect#check-for-an-existing-configuration), so distribution problems surface before they depend on the gateway.

[Roll out an LLM gateway for your organization](/en/llm-gateway-rollout) walks each step and shows the configuration files to distribute at each one. The gateway is one part of organization setup; for policy enforcement, usage visibility, and data handling decisions, see [Set up Claude Code for your organization](/en/admin-setup).

## Third-party gateways

Any gateway that exposes a [supported API format](/en/llm-gateway-protocol#api-formats) works. Anthropic doesn't endorse, maintain, or audit third-party gateway products. Deploy them following their own documentation, then complete the Claude Code side of the rollout with the [rollout steps](/en/llm-gateway-rollout).

## Subscriptions and gateways

While a [gateway credential variable](/en/llm-gateway-connect#set-the-credential-variable) or `apiKeyHelper` is active, a developer's claude.ai subscription isn't used: the credential replaces the subscription login for that session, and the subscription's usage limits don't apply. That traffic is billed per token to whoever owns the credential the gateway forwards, such as your organization's Anthropic Console account, or your Bedrock, Vertex, or Foundry account when the gateway routes there.

Setting only `ANTHROPIC_BASE_URL`, without a gateway credential, doesn't replace the subscription. Requests still route through the gateway, but a saved claude.ai login remains the active credential, so its usage limits and billing apply. Gateways that pass this traffic on to Anthropic must forward the OAuth capability in `anthropic-beta`; see the [request headers reference](/en/llm-gateway-protocol#request-headers).

## Configure separately from the gateway

A gateway determines where model API requests are sent. Model selection, the rest of Claude Code's network traffic, and corporate proxies are configured separately:

* **Model selection**: the base URL decides where requests go, not which model answers them. Pick the model with the `/model` command or the model environment variables; see [how to set your model](/en/model-config#setting-your-model)
* **Client-side traffic**: version checks and optional client telemetry, both disabled with [`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`](/en/env-vars), and login traffic when a claude.ai or Console login is in use, go to Anthropic's update and authentication endpoints rather than the gateway. See [network access requirements](/en/network-config#network-access-requirements) for the domains
* **Corporate proxies**: a proxy set with `HTTPS_PROXY` sits between Claude Code and every server it talks to, including the gateway. If your network requires a proxy, configure both; see [proxy configuration](/en/network-config#proxy-configuration)

## Related pages

* [Connect Claude Code to an LLM gateway](/en/llm-gateway-connect): set the base URL and credential on your own machine, with per-surface configuration and a troubleshooting table
* [Roll out an LLM gateway for your organization](/en/llm-gateway-rollout): the admin checklist for deploying a gateway, issuing developer credentials, and distributing managed settings
* [Gateway protocol reference](/en/llm-gateway-protocol): what Claude Code sends to a gateway, for operators configuring one, covering endpoints, headers to forward, and feature pass-through
* [Set up Claude Code for your organization](/en/admin-setup): the wider rollout decisions a gateway is one part of, including policy enforcement and usage visibility

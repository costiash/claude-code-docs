# CLI

Interact with the Claude API directly from your terminal with the ant command-line tool

---

The `ant` CLI provides access to the Claude API from your terminal. Every API resource is exposed as a subcommand, with output formatting, response filtering, and support for YAML or JSON file input that make it practical for both interactive exploration and automation.

Compared to calling the API with `curl`, `ant` lets you build request bodies from typed flags or piped YAML rather than hand-written JSON, inline file contents into string fields with an `@path` reference, and extract fields from the response with a built-in `--transform` query — no separate JSON tooling required. List endpoints paginate automatically. Claude Code understands how to use `ant` natively.

<Info>
For endpoint-specific parameters and response schemas, see the [API reference](/docs/en/api/cli/messages/create). This page covers CLI-specific features and workflows that apply across all endpoints.
</Info>

## Installation

<Tabs>
<Tab title="Homebrew (macOS)">

```bash
brew install anthropics/tap/ant
```

On macOS, unquarantine the binary:

```bash
xattr -d com.apple.quarantine "$(brew --prefix)/bin/ant"
```

</Tab>
<Tab title="curl (Linux/WSL)">

For Linux environments, download the release binary directly.

```bash
VERSION=1.0.0
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m | sed -e 's/x86_64/amd64/' -e 's/aarch64/arm64/')
curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${VERSION}/ant_${VERSION}_${OS}_${ARCH}.tar.gz" \
  | sudo tar -xz -C /usr/local/bin ant
```

You can find all releases on the [GitHub releases page](https://github.com/anthropics/anthropic-cli/releases).

</Tab>
<Tab title="Go">

You may also install the CLI from source using `go install`. Requires Go 1.22 or later.

```bash
go install github.com/anthropics/anthropic-cli/cmd/ant@latest
```

The binary is placed in `$(go env GOPATH)/bin`. Add it to your `PATH` if it isn't already:

```bash
export PATH="$PATH:$(go env GOPATH)/bin"
```

</Tab>
</Tabs>

Check the installation:

```bash
ant --version
```

## Authentication

The CLI reads your API key from the `ANTHROPIC_API_KEY` environment variable.

<Tabs>
<Tab title="zsh">

```bash
echo 'export ANTHROPIC_API_KEY=sk-ant-api03-...' >> ~/.zshrc
source ~/.zshrc
```

</Tab>
<Tab title="bash">

```bash
echo 'export ANTHROPIC_API_KEY=sk-ant-api03-...' >> ~/.bashrc
source ~/.bashrc
```

</Tab>
<Tab title="Windows">

```powershell
setx ANTHROPIC_API_KEY "sk-ant-api03-..."
```

Open a new terminal for the change to take effect.

</Tab>
</Tabs>

Get a key from the [Claude Console](https://platform.claude.com/settings/keys). To point at a different API host, set `ANTHROPIC_BASE_URL` or pass `--base-url` on any command.

## Send your first request

With the binary installed and `ANTHROPIC_API_KEY` set, call the [Messages API](/docs/en/api/cli/messages/create):

```bash
ant messages create \
  --model claude-opus-4-6 \
  --max-tokens 1024 \
  --message '{role: user, content: "Hello, Claude"}'
```

```json Output
{
  "model": "claude-opus-4-6",
  "id": "msg_01YMmR5XodC5nTqMxLZMKaq6",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Hello! How are you doing today? Is there something I can help you with?"
    }
  ],
  "stop_reason": "end_turn",
  "usage": { "input_tokens": 27, "output_tokens": 20 /*, ... */ }
}
```

The response is the full API object, pretty-printed because stdout is a terminal. The rest of this page covers how to reshape that output, pass complex request bodies, and chain commands together.

## Command structure

Commands follow a `resource action` pattern. Nested resources use colons:

```text
ant <resource>[:<subresource>] <action> [flags]
```

Run `ant --help` for the full resource list, or append `--help` to any subcommand for its flags.

Resources currently in beta — including agents, sessions, deployments, environments, and skills — live under the `beta:` prefix. Commands in this namespace automatically send the appropriate `anthropic-beta` header for that resource, so you don't need to pass it yourself. Use `--beta <header>` only to override the default — for example, to opt into a different schema version.

```bash
ant models list
ant messages create --model claude-opus-4-6 --max-tokens 1024 ...
ant beta:agents retrieve --agent-id agent_01...
ant beta:sessions:events list --session-id session_01...
```

### Global flags

| Flag | Description |
| --- | --- |
| `--format` | Output format: `auto`, `json`, `jsonl`, `yaml`, `pretty`, `raw`, `explore` |
| `--transform` | Filter or reshape the response with a [GJSON path](#transform-output-with-gjson) |
| `--base-url` | Override the API base URL |
| `--debug` | Print full HTTP request and response to stderr |
| `--format-error`, `--transform-error` | Same as `--format` and `--transform` but applied to [error responses](#inspect-errors) |

## Output formats

The default `auto` format pretty-prints JSON when writing to a terminal and emits compact JSON when piped. Override it with `--format`:

```bash
ant models retrieve --model-id claude-opus-4-6 --format yaml
```

```yaml Output
type: model
id: claude-opus-4-6
display_name: Claude Opus 4.6
created_at: "2026-02-04T00:00:00Z"
...
```

List endpoints auto-paginate. In the default formats each item is written separately (one compact JSON object per line in `jsonl` mode, a stream of YAML documents in `yaml` mode), which streams cleanly into `head`, `grep`, and `--transform` filters.

### Interactive explorer

When connected to a terminal, `--format explore` opens a fold-and-search TUI for browsing large responses. Arrow keys expand and collapse nodes, `/` searches, `q` exits.

```bash
ant models list --format explore
```

## Transform output with GJSON

Use `--transform` to reshape responses before printing. The expression is a [GJSON path](https://github.com/tidwall/gjson/blob/master/SYNTAX.md). For list endpoints the transform runs against each item individually, not the envelope:

```bash
ant beta:agents list \
  --transform "{id,name,model}" \
  --format jsonl
```

```jsonl Output
{"id": "agent_011CYm1BLqPX...", "name": "Docs CLI Test Agent", "model": "claude-sonnet-4-6"}
{"id": "agent_011CYkVwfaEt...", "name": "Coffee Making Assistant", "model": "claude-sonnet-4-6"}
{"id": "agent_011CYixHhtUP...", "name": "Coding Assistant", "model": "claude-opus-4-5"}
```

### Extract a scalar

To capture a single field as an unquoted string — for example, the ID of a newly created resource — pair `--transform` with `--format yaml`. YAML emits scalar values without quotes, so the result is ready to assign to a shell variable:

```bash
AGENT_ID=$(ant beta:agents create \
  --name "My Agent" \
  --model claude-sonnet-4-6 \
  --transform id --format yaml)

printf '%s\n' "$AGENT_ID"
```

```text Output
agent_011CYm1BLqPXpQRk5khsSXrs
```

<Note>
`--transform` is not applied when `--format raw` is set. Use `--format yaml` for unquoted scalars, or `--format jsonl` to keep the result as structured data for further processing.
</Note>

## Passing request bodies

The right input mechanism depends on the shape of the data: use **flags** for scalar fields and short structured values, pipe a **stdin** document for nested or multi-line bodies, and use **`@file` references** to pull file contents into any string or binary field.

### Flags

Scalar fields map directly to flags. Structured fields accept a relaxed YAML-like syntax (unquoted keys, optional quotes around strings) or strict JSON:

```bash
ant beta:sessions create \
  --agent '{type: agent, id: agent_011CYm1BLqPXpQRk5khsSXrs, version: 1}' \
  --environment env_01595EKxaaTTGwwY3kyXdtbs \
  --title "CLI docs test session"
```

Repeatable flags build arrays. Each `--tool` or `--event` appends one element:

```bash
ant beta:agents create \
  --name "Research Agent" \
  --model claude-opus-4-6 \
  --tool '{type: agent_toolset_20260401}' \
  --tool '{type: custom, name: search_docs, input_schema: {type: object, properties: {query: {type: string}}}}'
```

### Stdin

Pipe a JSON or YAML document to stdin to supply the full request body. Fields from stdin are merged with flags, with flags taking precedence. Here `version` is the optimistic-locking token returned by an earlier `retrieve`, and `$AGENT_ID` was captured as in [Extract a scalar](#extract-a-scalar):

```bash
echo '{"description": "Updated test agent.", "version": 1}' | \
  ant beta:agents update --agent-id "$AGENT_ID"
```

Heredocs work the same way and are convenient for multi-line YAML. Quote the delimiter (as in `<<'YAML'`) to disable variable expansion inside the body.

```bash
ant beta:agents create <<'YAML'
name: Research Agent
model: claude-opus-4-6
system: |
  You are a research assistant. Cite sources for every claim.
tools:
  - type: agent_toolset_20260401
YAML
```

### File references

Flags that take a file path, such as `--file` on the upload command, accept a bare path:

```bash
ant beta:files upload --file ./report.pdf
```

To inline a file's contents into a string-valued field, prefix the path with `@`:

```bash
ant beta:agents create \
  --name "Researcher" --model claude-sonnet-4-6 \
  --system @./prompts/researcher.txt
```

Inside structured flag values, wrap the path in quotes. To send a PDF to the Messages API:

```bash
ant messages create \
  --model claude-opus-4-6 \
  --max-tokens 1024 \
  --message '{role: user, content: [
    {type: document, source: {type: base64, media_type: application/pdf, data: "@./scan.pdf"}},
    {type: text, text: "Extract the text from this scanned document."}
  ]}' \
  --transform 'content.0.text' --format yaml
```

The CLI detects the file type and encodes binary files as base64 automatically. To force a specific encoding use `@file://` for plain text or `@data://` for base64. Escape a literal leading `@` with a backslash (`\@username`).

## Version-controlling API resources

You can use the CLI to version control API resources such as skills, agents, environments, or deployments as YAML files in your repository and keep them in sync with the Claude API.

<Note>
For more information on these resources, see [Managed Agents](/docs/en/managed-agents/overview).
</Note>

<Steps>
<Step title="Define your agent">

Write the agent definition to `summarizer.agent.yaml`:

```yaml summarizer.agent.yaml
name: Summarizer
model: claude-sonnet-4-6
system: |
  You are a helpful assistant that writes concise summaries.
tools:
  - type: agent_toolset_20260401
```

</Step>
<Step title="Create the agent">

```bash
ant beta:agents create < summarizer.agent.yaml
```

```json Output
{
  "id": "agent_011CYm1BLqPXpQRk5khsSXrs",
  "version": 1,
  "name": "Summarizer",
  "model": "claude-sonnet-4-6"
  /* ... */
}
```

Note the `id` from the response — you'll pass it to the session create command below.

<Tip>
Check `summarizer.agent.yaml` into your repository and keep it in sync with the API in your CI pipeline. The update command needs the agent ID and current version as flags:

```bash CLI
ant beta:agents update --agent-id agent_011CYm1BLqPXpQRk5khsSXrs --version 1 < summarizer.agent.yaml
```
</Tip>

</Step>
<Step title="Define the environment">

A session runs in an [environment](/docs/en/api/cli/beta/environments), which defines the container it executes in. Write the environment definition to `summarizer.environment.yaml`:

```yaml summarizer.environment.yaml
name: summarizer-env
config:
  type: cloud
  networking:
    type: unrestricted
```

</Step>
<Step title="Create the environment">

```bash
ant beta:environments create < summarizer.environment.yaml
```

```json Output
{
  "id": "env_01595EKxaaTTGwwY3kyXdtbs",
  "name": "summarizer-env"
  /* ... */
}
```

Note the `id` from the response — you'll pass it to the session create command below.

<Tip>
Check `summarizer.environment.yaml` into your repository and keep it in sync with the API in your CI pipeline. The update command needs the environment ID as a flag:

```bash CLI
ant beta:environments update --environment-id env_01595EKxaaTTGwwY3kyXdtbs < summarizer.environment.yaml
```
</Tip>

</Step>
<Step title="Start a session">

Paste the agent `id` and environment `id` from the previous outputs into the session create command:

```bash highlight={2..3}
ant beta:sessions create \
  --agent agent_011CYm1BLqPXpQRk5khsSXrs \
  --environment env_01595EKxaaTTGwwY3kyXdtbs \
  --title "Summarization task"
```

```json Output
{
  "id": "session_01JZCh78XvmxJjiXVy3oSi7K",
  "status": "running"
  /* ... */
}
```

</Step>
<Step title="Send a user message">

Copy the session `id` from the previous output into `--session-id`:

```bash highlight={2}
ant beta:sessions:events send \
  --session-id session_01JZCh78XvmxJjiXVy3oSi7K \
  --event '{type: user.message, content: [{type: text, text: "Summarize the benefits of type safety in one sentence."}]}'
```

</Step>
<Step title="Read the conversation">

`--transform` runs against each listed event, so this prints the text of every message in order:

```bash highlight={2}
ant beta:sessions:events list \
  --session-id session_01JZCh78XvmxJjiXVy3oSi7K \
  --transform 'content.0.text' --format yaml
```

```text Output
Summarize the benefits of type safety in one sentence.
Type safety catches errors at compile time rather than runtime, reducing bugs, improving code clarity, enabling better tooling support, and making codebases easier to maintain and refactor with confidence.
```

<Tip>
To watch a session as it runs, use `ant beta:sessions stream --session-id session_01JZCh78XvmxJjiXVy3oSi7K`. Events are written to stdout as they arrive.
</Tip>

</Step>
</Steps>

## Scripting patterns

The CLI is designed to compose with standard shell tooling.

### Chain list output into a second command

`--transform id --format yaml` on a list endpoint emits one bare ID per line, so standard tools such as `head` and `xargs` apply directly. Capture the first result, then pass it to a follow-up command:

```bash
FIRST_AGENT=$(ant beta:agents list \
  --transform id --format yaml | head -1)

ant beta:agents:versions list \
  --agent-id "$FIRST_AGENT" \
  --transform "{version,created_at}" --format jsonl
```

### Inspect errors

The `--transform-error` and `--format-error` flags mirror their success-path counterparts and follow the same rule — pair with `yaml`, not `raw`, to apply the transform. Extract only the error message:

```bash
ant beta:agents retrieve --agent-id bogus \
  --transform-error error.message --format-error yaml 2>&1
```

```text Output
GET "https://api.anthropic.com/v1/agents/bogus?beta=true": 404 Not Found
Agent not found.
```

## Use the CLI from Claude Code

[Claude Code](https://docs.claude.com/en/docs/claude-code/overview) knows out of the box how to use the `ant` CLI. With the CLI installed and `ANTHROPIC_API_KEY` set, you can ask Claude Code to operate on your API resources directly — for example:

- "List my recent agent sessions and summarize which ones errored."
- "Upload every PDF in `./reports` to the Files API and print the resulting IDs."
- "Pull the events for session `session_01...` and tell me where the agent got stuck."

Claude Code shells out to `ant`, parses the structured output, and reasons over the results — no custom integration code required.

## Debugging

Add `--debug` to any command to print the exact HTTP request and response (headers and body) to stderr. API keys are redacted.

```bash
ant --debug beta:agents list
```

```text Output
GET /v1/agents?beta=true HTTP/1.1
Host: api.anthropic.com
Anthropic-Beta: managed-agents-2026-04-01
Anthropic-Version: 2023-06-01
X-Api-Key: <REDACTED>
...
```

## Shell completion

The CLI ships completion scripts for bash, zsh, fish, and PowerShell. Generate and install one for your shell:

<Tabs>
<Tab title="zsh">

```bash
ant @completion zsh > "${fpath[1]}/_ant"
# Restart your shell or run: autoload -U compinit && compinit
```

</Tab>
<Tab title="bash">

```bash
ant @completion bash > /etc/bash_completion.d/ant
```

</Tab>
<Tab title="fish">

```bash
ant @completion fish > ~/.config/fish/completions/ant.fish
```

</Tab>
<Tab title="PowerShell">

```powershell
ant @completion powershell | Out-String | Invoke-Expression
# To persist across sessions:
# ant @completion powershell >> $PROFILE
```

</Tab>
</Tabs>

## Available resources

Every API resource the CLI exposes is documented in the [API reference](/docs/en/api/cli/messages/create). For a local listing, run `ant --help`, and append `--help` to any subcommand for its flags and parameters.
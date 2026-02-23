# Prompt engineering overview

---

## Before prompt engineering

This guide assumes that you have:
1. A clear definition of the success criteria for your use case
2. Some ways to empirically test against those criteria
3. A first draft prompt you want to improve

If not, we highly suggest you spend time establishing that first. Check out [Define success criteria and build evaluations](/docs/en/test-and-evaluate/develop-tests) for tips and guidance.

<CardGroup cols={2}>
  <Card title="Prompt generator" icon="link" href="/dashboard">
    Don't have a first draft prompt? Try the prompt generator in the Claude Console!
  </Card>
  <Card title="Prompting best practices" icon="link" href="/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices">
    For model-specific tuning guidance for Claude's latest models, start here.
  </Card>
</CardGroup>

***

## When to prompt engineer

  This guide focuses on success criteria that are controllable through prompt engineering.
  Not every success criteria or failing eval is best solved by prompt engineering. For example, latency and cost can be sometimes more easily improved by selecting a different model.

***

## How to prompt engineer

All prompting techniques — from clarity and examples to XML structuring, role prompting, thinking, and prompt chaining — are covered in [Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). That's the living reference; start there.

The [Claude Console](/dashboard) also offers [prompting tools](/docs/en/build-with-claude/prompt-engineering/prompting-tools)—prompt generator, templates and variables, and prompt improver—to help you build and refine prompts quickly.

***

## Prompt engineering tutorial

If you're an interactive learner, you can dive into our interactive tutorials instead!

<CardGroup cols={2}>
  <Card title="GitHub prompting tutorial" icon="link" href="https://github.com/anthropics/prompt-eng-interactive-tutorial">
    An example-filled tutorial that covers the prompt engineering concepts found in our docs.
  </Card>
  <Card title="Google Sheets prompting tutorial" icon="link" href="https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8">
    A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.
  </Card>
</CardGroup>
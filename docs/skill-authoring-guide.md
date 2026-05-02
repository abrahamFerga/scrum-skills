# Skill Authoring Guide

This guide explains how to write a new skill for the Scrum Skills library.

---

## What is a skill?

A skill is a Markdown file that Claude Code loads as a slash command. When invoked, Claude reads the file as its operating instructions for that session. Skills in this library guide Claude through a specific Scrum ceremony or activity from a specific role's perspective.

---

## File structure

```
skills/
  <ceremony-slug>/
    <role>-<variant>.md
```

Use lowercase kebab-case throughout. Examples:

| Good | Bad |
|---|---|
| `sprint-planning/developer-story-breakdown.md` | `SprintPlanning/DeveloperStoryBreakdown.md` |
| `retrospective/scrum-master-facilitation.md` | `retro/sm.md` |

---

## Frontmatter

Every skill file must begin with YAML frontmatter:

```yaml
---
name: <slash-command-name>         # becomes /name when installed
description: <one sentence>        # shown in /help listing
ceremony: <Scrum ceremony name>    # e.g. "Daily Sync", "Sprint Planning"
perspective: <Role>                # e.g. "Developer", "Scrum Master", "Product Owner"
requires_mcp: true | false         # does this skill need a live MCP connection?
mcp_backends:
  - ado                            # azure devops
  - jira                           # jira
version: 1.0.0
---
```

---

## Writing the skill body

### 1. Set the persona

Open with a brief statement of what Claude should act as:

```
You are acting as a Scrum coach helping a [role] [do what].
```

### 2. Provide ceremony context

One short paragraph on the ceremony's purpose and the expected outcome of running this skill. This anchors Claude's reasoning.

### 3. Use numbered steps

Structure the skill as numbered steps that Claude follows sequentially. Each step should:

- Have a clear heading (`## Step N — Description`)
- Describe what Claude should do
- Include code blocks for any tool calls (MCP queries, git commands, bash)
- Specify what to do if the step fails or returns no data

### 4. MCP tool patterns

Skills should support both ADO and Jira. Use this pattern:

```markdown
### Azure DevOps (mcp__ado__)
[WIQL query or tool call]

### Jira (mcp__jira__)
[JQL query or tool call]

If no MCP is connected, [fallback behavior].
```

Do **not** hard-code specific MCP tool names beyond the namespace prefix (`mcp__ado__`, `mcp__jira__`). The actual tool names vary by MCP implementation.

### 5. Output template

Provide an explicit output template as a Markdown code block. This ensures consistent, copy-paste-ready output regardless of who runs the skill.

### 6. Guardrails section

End every skill with a `## Guardrails` section listing:

- What Claude must **never** invent or assume
- What Claude must **redirect** to the user (destructive actions, sensitive data)
- Tone and scope constraints

---

## Testing your skill

1. Copy your skill to `.claude/commands/<skill-name>.md` in a test project.
2. Run it with `/skill-name` in Claude Code.
3. Test with MCP connected and disconnected (graceful fallback).
4. Test with an empty sprint (no work items) and a full sprint.

---

## Checklist before submitting a PR

- [ ] Frontmatter is complete and valid YAML
- [ ] Skill supports both ADO and Jira (or documents why it cannot)
- [ ] Has a fallback for when MCP is unavailable
- [ ] Has a `## Guardrails` section
- [ ] `skills/README.md` table updated
- [ ] Root `README.md` table updated

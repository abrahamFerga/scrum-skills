# Skills

Each subdirectory is one skill. Every skill contains a `SKILL.md` as its entry point, following the [agentskills.io](https://agentskills.io) specification.

## Structure

```
skills/
  <skill-name>/       ← directory name matches the `name` field in SKILL.md
    SKILL.md          ← required: frontmatter + instructions
    scripts/          ← optional: helper scripts
    references/       ← optional: supplementary docs
    assets/           ← optional: templates and static files
```

## Available skills

| Skill | Command | Ceremony | Perspective |
|---|---|---|---|
| [`daily-sync-dev`](daily-sync-dev/SKILL.md) | `/daily-sync-dev` | Daily Scrum | Developer |
| [`po-create-user-story`](po-create-user-story/SKILL.md) | `/po-create-user-story` | Backlog Refinement | Product Owner / PM |

## Coming soon

| Ceremony | Perspective |
|---|---|
| Sprint Planning | Developer |
| Sprint Review | Product Owner |
| Sprint Retrospective | Scrum Master |

## Installing a skill

See the adapter directory for your tool:

| Tool | Adapter directory |
|---|---|
| Claude Code | [`.claude/commands/`](../.claude/commands/README.md) |
| Cursor | [`.cursor/rules/`](../.cursor/rules/README.md) |
| GitHub Copilot | [`.github/copilot-instructions.md`](../.github/copilot-instructions.md) |

## PM tool agnosticism

Skills auto-detect the connected project management tool at runtime:
- ADO MCP connected → uses Azure DevOps
- Jira MCP connected → uses Jira
- Both connected → asks which to use
- Neither → manual fallback (paste items into chat)

No configuration files. No path dependencies. Works wherever the skill is installed.

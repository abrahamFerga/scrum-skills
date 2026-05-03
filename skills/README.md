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

### Developer

| Skill | Command | What it does |
|---|---|---|
| [`dev-lead`](dev-lead/SKILL.md) | `/dev-lead` | Reads a story, explores the codebase, and produces a file-by-file implementation plan |

### Ceremonies

| Skill | Command | Ceremony | Perspective |
|---|---|---|---|
| [`sprint-planning`](sprint-planning/SKILL.md) | `/sprint-planning` | Sprint Planning | Scrum Team |
| [`daily-sync-dev`](daily-sync-dev/SKILL.md) | `/daily-sync-dev` | Daily Scrum | Developer |
| [`sprint-review`](sprint-review/SKILL.md) | `/sprint-review` | Sprint Review | Scrum Team |
| [`po-create-user-story`](po-create-user-story/SKILL.md) | `/po-create-user-story` | Backlog Refinement | Product Owner / PM |

### Audits

| Skill | Command | What it audits | Tool |
|---|---|---|---|
| [`audit-user-story`](audit-user-story/SKILL.md) | `/audit-user-story` | INVEST, story format, AC quality, DoR | ADO / Jira / manual |
| [`audit-sprint-ado`](audit-sprint-ado/SKILL.md) | `/audit-sprint-ado` | Sprint Goal, work item hygiene, state transitions, DoD | Azure DevOps |
| [`audit-sprint-jira`](audit-sprint-jira/SKILL.md) | `/audit-sprint-jira` | Sprint Goal, issue hygiene, story points, workflow, DoD | Jira |
| [`audit-sprint-retrospective-ado`](audit-sprint-retrospective-ado/SKILL.md) | `/audit-sprint-retrospective-ado` | Retro summary, action items, patterns, carry-overs | Azure DevOps |

## Installing a skill

See the [root README](../README.md#getting-started) for install commands per tool.

## PM tool agnosticism

Skills auto-detect the connected project management tool at runtime:
- ADO MCP connected → uses Azure DevOps
- Jira MCP connected → uses Jira
- Both connected → asks which to use
- Neither → manual fallback (paste items into chat)

No configuration files. No path dependencies. Works wherever the skill is installed.

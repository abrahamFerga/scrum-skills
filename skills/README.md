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

### Ceremonies

| Skill | Command | Ceremony | Perspective |
|---|---|---|---|
| [`sprint-planning`](sprint-planning/SKILL.md) | `/sprint-planning` | Sprint Planning | Scrum Team |
| [`daily-sync-dev`](daily-sync-dev/SKILL.md) | `/daily-sync-dev` | Daily Scrum | Developer |
| [`sprint-review`](sprint-review/SKILL.md) | `/sprint-review` | Sprint Review | Scrum Team |
| [`po-create-user-story`](po-create-user-story/SKILL.md) | `/po-create-user-story` | Backlog Refinement | Product Owner / PM |

### Developer

| Skill | Command | What it does |
|---|---|---|
| [`dev-lead`](dev-lead/SKILL.md) | `/dev-lead` | Reads a story, explores the codebase, and produces a file-by-file implementation plan |
| [`dev-pr-description`](dev-pr-description/SKILL.md) | `/dev-pr-description` | Reads the git diff and linked story, maps changes to ACs, generates a complete PR description |

### Product Owner

| Skill | Command | What it does |
|---|---|---|
| [`po-split-story`](po-split-story/SKILL.md) | `/po-split-story` | Applies 9 proven patterns to break an oversized story or epic into Sprint-sized deliverables |
| [`po-release-notes`](po-release-notes/SKILL.md) | `/po-release-notes` | Translates completed Sprint work items into audience-appropriate release notes |

### Scrum Master

| Skill | Command | What it does |
|---|---|---|
| [`sm-capacity-planning`](sm-capacity-planning/SKILL.md) | `/sm-capacity-planning` | Calculates team developer-days accounting for days off, focus factor, and ceremony overhead |
| [`sm-velocity-review`](sm-velocity-review/SKILL.md) | `/sm-velocity-review` | Analyses velocity trends, predictability rate, and variability with planning guidance |
| [`sm-impediment-log`](sm-impediment-log/SKILL.md) | `/sm-impediment-log` | Logs, tracks, and resolves Sprint blockers with owners, due dates, and escalation flags |
| [`stakeholder-update`](stakeholder-update/SKILL.md) | `/stakeholder-update` | Drafts Slack messages, emails, or formal reports translating Sprint progress into business language |

### Audits

| Skill | Command | What it audits | Tool |
|---|---|---|---|
| [`audit-user-story`](audit-user-story/SKILL.md) | `/audit-user-story` | INVEST, story format, AC quality, DoR | ADO / Jira / manual |
| [`audit-sprint-ado`](audit-sprint-ado/SKILL.md) | `/audit-sprint-ado` | Sprint Goal, work item hygiene, state transitions, DoD | Azure DevOps |
| [`audit-sprint-jira`](audit-sprint-jira/SKILL.md) | `/audit-sprint-jira` | Sprint Goal, issue hygiene, story points, workflow, DoD | Jira |
| [`audit-sprint-retrospective-ado`](audit-sprint-retrospective-ado/SKILL.md) | `/audit-sprint-retrospective-ado` | Retro summary, action items, patterns, carry-overs | Azure DevOps |
| [`audit-backlog-ado`](audit-backlog-ado/SKILL.md) | `/audit-backlog-ado` | Backlog hygiene, story quality, readiness, staleness, priority coherence | Azure DevOps |

## Installing a skill

See the [root README](../README.md#getting-started) for install commands per tool.

## PM tool agnosticism

Skills auto-detect the connected project management tool at runtime:
- ADO MCP connected → uses Azure DevOps
- Jira MCP connected → uses Jira
- Both connected → asks which to use
- Neither → manual fallback (paste items into chat)

No configuration files. No path dependencies. Works wherever the skill is installed.

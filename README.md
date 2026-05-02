# scrum-skills

> A vendor-agnostic library of AI agent skills built around the Scrum framework.
> Works with Claude Code, Cursor, GitHub Copilot, and any tool that supports the [agentskills.io](https://agentskills.io) spec.

---

## Skills

### Ceremonies

| Skill | Command | Ceremony | Perspective |
|---|---|---|---|
| [Sprint Planning](skills/sprint-planning/SKILL.md) | `/sprint-planning` | Sprint Planning | Scrum Team |
| [Daily Scrum — Developer](skills/daily-sync-dev/SKILL.md) | `/daily-sync-dev` | Daily Scrum | Developer |
| [Sprint Review](skills/sprint-review/SKILL.md) | `/sprint-review` | Sprint Review | Scrum Team |
| [Create User Story](skills/po-create-user-story/SKILL.md) | `/po-create-user-story` | Backlog Refinement | Product Owner / PM |

### Audits

| Skill | Command | What it audits | Tool |
|---|---|---|---|
| [Audit User Story](skills/audit-user-story/SKILL.md) | `/audit-user-story` | INVEST, story format, AC quality, Definition of Ready | ADO / Jira / manual |
| [Audit Sprint — ADO](skills/audit-sprint-ado/SKILL.md) | `/audit-sprint-ado` | Sprint Goal, work item hygiene, state transitions, DoD, capacity | Azure DevOps |
| [Audit Sprint — Jira](skills/audit-sprint-jira/SKILL.md) | `/audit-sprint-jira` | Sprint Goal, issue hygiene, story points, workflow transitions, DoD | Jira |
| [Audit Retrospective — ADO](skills/audit-sprint-retrospective-ado/SKILL.md) | `/audit-sprint-retrospective-ado` | Retro summary, action item tracking, pattern analysis, carry-overs | Azure DevOps |

---

## Persona Instructions

Role-based instructions that ground Claude or Copilot in a specific Scrum accountability. Install once; every session starts with the right context.

| Persona | Claude | Copilot |
|---|---|---|
| Developer | [`instructions/developer/claude.md`](instructions/developer/claude.md) | [`instructions/developer/copilot.instructions.md`](instructions/developer/copilot.instructions.md) |
| Product Owner | [`instructions/product-owner/claude.md`](instructions/product-owner/claude.md) | [`instructions/product-owner/copilot.instructions.md`](instructions/product-owner/copilot.instructions.md) |
| Scrum Master | [`instructions/scrum-master/claude.md`](instructions/scrum-master/claude.md) | [`instructions/scrum-master/copilot.instructions.md`](instructions/scrum-master/copilot.instructions.md) |

See [`instructions/README.md`](instructions/README.md) for installation steps.

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/abrahamFerga/scrum-skills
```

### 2. Install skills for your tool

**Claude Code**
```bash
cp scrum-skills/skills/daily-sync-dev/SKILL.md \
   your-project/.claude/commands/daily-sync-dev.md
```

**Cursor**
```bash
cp scrum-skills/skills/po-create-user-story/SKILL.md \
   your-project/.cursor/rules/po-create-user-story.mdc
```

**GitHub Copilot**

Reference skills inline in Copilot Chat:
```
#file:scrum-skills/skills/daily-sync-dev/SKILL.md
```

See [`skills/README.md`](skills/README.md) and the adapter directories for full details.

### 3. Connect your PM tool *(optional)*

Skills work best when connected to your backlog via MCP:

| Tool | MCP server |
|---|---|
| Azure DevOps | [`@azure-devops/mcp`](https://github.com/microsoft/azure-devops-mcp) |
| Jira | Your Jira MCP server |

Skills **auto-detect** which tool is connected — no configuration required.
If no MCP is connected, skills fall back to manual mode automatically.

See [`docs/mcp-setup.md`](docs/mcp-setup.md) for setup instructions.

---

## How skills work

Each skill is a directory containing a `SKILL.md` file:

```
skills/
  daily-sync-dev/
    SKILL.md
  po-create-user-story/
    SKILL.md
```

The `SKILL.md` is loaded by your AI agent as a slash command or instruction file. Skills are **self-contained** — no config files, no path dependencies, no hardcoded tool names.

---

## Scrum Guide alignment

All skills are grounded in the [2020 Scrum Guide](https://scrumguides.org/scrum-guide.html). See [`docs/scrum-guide-references.md`](docs/scrum-guide-references.md) for the sourcing policy.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New skills, ceremony coverage, and role perspectives are all welcome.

---

## License

[MIT](LICENSE)

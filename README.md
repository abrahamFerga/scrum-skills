# scrum-skills

[![Validate Skills](https://github.com/abrahamFerga/scrum-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/abrahamFerga/scrum-skills/actions/workflows/validate-skills.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A vendor-agnostic library of AI agent skills built around the Scrum framework.
> Works with Claude Code, Cursor, GitHub Copilot, and any tool that supports the [agentskills.io](https://agentskills.io) spec.

---

## See it in action

<table>
<tr>
<td width="50%">

### 🔍 Story audit
`/audit-user-story` reads story #6 from Azure DevOps, scores it against INVEST, flags missing acceptance criteria, and posts a comment back to the board — all from a single natural-language prompt.

https://github.com/user-attachments/assets/6aa53283-d329-4c13-9c59-55dc1794a3e7

</td>
<td width="50%">

### 🧑‍💻 Dev lead
`/dev-lead` fetches a real story, explores the codebase, identifies the reference pattern, and produces a file-by-file implementation plan — so the developer knows exactly where to start.

https://github.com/user-attachments/assets/91ab0d35-1741-4a09-a5ee-f62d41b1d049

</td>
</tr>
</table>

---

## Adapt to your process

These skills are grounded in the [2020 Scrum Guide](https://scrumguides.org/scrum-guide.html) — the framework as written, not as any one team practises it.

Scrum is intentionally incomplete. Every team layers their own conventions on top: how they write acceptance criteria, what their Definition of Done requires, which ceremony formats they use, how they integrate with their tools. The guide defines the minimum; your process fills the rest.

**These skills follow the guide. You should adapt them to your team.**

Each `SKILL.md` is a plain Markdown file. Fork this repo, edit the guardrails, change the output format, add your DoD checklist, reference your internal templates. The skills are a starting point — your team's process is the destination.

See [CONTRIBUTING.md](CONTRIBUTING.md) if you want to share an adapted skill back with the community.

---

## Skills

### Ceremonies

| Skill | Command | Ceremony | Perspective |
|---|---|---|---|
| [Sprint Planning](skills/sprint-planning/SKILL.md) | `/sprint-planning` | Sprint Planning | Scrum Team |
| [Daily Scrum — Developer](skills/daily-sync-dev/SKILL.md) | `/daily-sync-dev` | Daily Scrum | Developer |
| [Sprint Review](skills/sprint-review/SKILL.md) | `/sprint-review` | Sprint Review | Scrum Team |
| [Create User Story](skills/po-create-user-story/SKILL.md) | `/po-create-user-story` | Backlog Refinement | Product Owner / PM |

### Developer

| Skill | Command | What it does |
|---|---|---|
| [Dev Lead](skills/dev-lead/SKILL.md) | `/dev-lead` | Reads a story, explores the codebase, and produces a file-by-file implementation plan as a tech lead would give in a pairing session |
| [PR Description](skills/dev-pr-description/SKILL.md) | `/dev-pr-description` | Reads the git diff and linked story, maps changes to acceptance criteria, and generates a complete pull request description |

### Product Owner

| Skill | Command | What it does |
|---|---|---|
| [Split Story](skills/po-split-story/SKILL.md) | `/po-split-story` | Applies 9 proven patterns to break an oversized story or epic into Sprint-sized, independently valuable stories |
| [Release Notes](skills/po-release-notes/SKILL.md) | `/po-release-notes` | Translates completed Sprint work items into audience-appropriate release notes in plain business language |

### Scrum Master

| Skill | Command | What it does |
|---|---|---|
| [Capacity Planning](skills/sm-capacity-planning/SKILL.md) | `/sm-capacity-planning` | Calculates team developer-days for the next Sprint, accounting for days off, focus factor, and ceremony overhead |
| [Velocity Review](skills/sm-velocity-review/SKILL.md) | `/sm-velocity-review` | Analyses velocity trends, predictability rate, and variability across recent Sprints with planning guidance |
| [Impediment Log](skills/sm-impediment-log/SKILL.md) | `/sm-impediment-log` | Logs, tracks, and resolves Sprint blockers as ADO work items with owners, due dates, and escalation flags |
| [Stakeholder Update](skills/stakeholder-update/SKILL.md) | `/stakeholder-update` | Drafts Slack messages, emails, or formal status reports translating Sprint progress into business language |

### Audits

| Skill | Command | What it audits | Tool |
|---|---|---|---|
| [Audit User Story](skills/audit-user-story/SKILL.md) | `/audit-user-story` | INVEST, story format, AC quality, Definition of Ready | ADO / Jira / manual |
| [Audit Sprint — ADO](skills/audit-sprint-ado/SKILL.md) | `/audit-sprint-ado` | Sprint Goal, work item hygiene, state transitions, DoD, capacity | Azure DevOps |
| [Audit Sprint — Jira](skills/audit-sprint-jira/SKILL.md) | `/audit-sprint-jira` | Sprint Goal, issue hygiene, story points, workflow transitions, DoD | Jira |
| [Audit Retrospective — ADO](skills/audit-sprint-retrospective-ado/SKILL.md) | `/audit-sprint-retrospective-ado` | Retro summary, action item tracking, pattern analysis, carry-overs | Azure DevOps |
| [Audit Backlog — ADO](skills/audit-backlog-ado/SKILL.md) | `/audit-backlog-ado` | Backlog hygiene, story quality, readiness, staleness, and priority coherence | Azure DevOps |

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

### GitHub Copilot

Use the `gh` CLI to install skills directly into your project:

```bash
# Preview a skill before installing
gh skill preview abrahamFerga/scrum-skills daily-sync-dev

# Install a skill into your current project
gh skill install abrahamFerga/scrum-skills daily-sync-dev

# Install specific skills
gh skill install abrahamFerga/scrum-skills sprint-planning
gh skill install abrahamFerga/scrum-skills po-create-user-story
gh skill install abrahamFerga/scrum-skills audit-user-story
gh skill install abrahamFerga/scrum-skills audit-sprint-ado
```

Then invoke skills in Copilot Chat: `/daily-sync-dev`, `/sprint-planning`, etc.

**Persona instructions** — install the instruction file for your role:

```bash
# Into your project's .github/instructions/
cp instructions/developer/copilot.instructions.md \
   .github/instructions/developer.instructions.md
```

### Claude Code

```bash
# Add the marketplace
claude plugin marketplace add https://github.com/abrahamFerga/scrum-skills

# Install individual skills
claude plugin install daily-sync-dev@scrum-skills
claude plugin install sprint-planning@scrum-skills
claude plugin install audit-user-story@scrum-skills
```

Or via the in-app command:
```
/plugin marketplace add abrahamFerga/scrum-skills
```

**Persona instructions** — append to your project's `CLAUDE.md`:

```bash
cat instructions/developer/claude.md >> CLAUDE.md
```

### Connect your PM tool *(optional)*

Skills auto-detect the connected project management tool — no configuration required.

| Tool | MCP server |
|---|---|
| Azure DevOps | [`@azure-devops/mcp`](https://github.com/microsoft/azure-devops-mcp) |
| Jira | Your preferred Jira MCP package |

If no MCP is connected, skills fall back to manual mode automatically.

See [`docs/mcp-setup.md`](docs/mcp-setup.md) for PAT setup, required scopes, and troubleshooting.

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

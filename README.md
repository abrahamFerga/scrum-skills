# Scrum Skills for Claude Code

> A curated library of Claude Code skills, prompts, and instructions built around the Scrum framework.

Each skill maps to a Scrum ceremony or role activity. Skills are invokable as slash commands inside [Claude Code](https://claude.ai/code) and integrate with your project management tool (Azure DevOps or Jira) via MCP.

---

## Skills

| Ceremony / Activity | Skill | Perspective |
|---|---|---|
| Daily Sync | [`/daily-sync-dev`](skills/daily-sync/developer-update.md) | Developer |
| Sprint Planning | *(coming soon)* | |
| Backlog Refinement | *(coming soon)* | |
| Sprint Review | *(coming soon)* | |
| Sprint Retrospective | *(coming soon)* | |

---

## Getting Started

### Prerequisites

- [Claude Code](https://claude.ai/code) CLI installed
- An MCP connector for your project management tool:
  - **Azure DevOps** — [azure-devops MCP](https://github.com/microsoft/azure-devops-mcp) *(or equivalent)*
  - **Jira** — [jira MCP](https://github.com/atlassian/jira-mcp) *(or equivalent)*

### Installation

1. Copy the skill file(s) you want into your project's `.claude/commands/` directory:

   ```bash
   # from your project root
   git clone https://github.com/your-username/scrum-skills
   mkdir -p .claude/commands
   cp scrum-skills/skills/daily-sync/developer-update.md \
      .claude/commands/daily-sync-dev.md
   ```

2. Restart Claude Code (or reload commands with `/commands reload`).

3. Run the skill:

   ```
   /daily-sync-dev
   ```

### Global installation

To make skills available in every project, copy them to `~/.claude/commands/` instead.

---

## MCP Setup

Skills assume one of these MCP tool namespaces is active:

| Tool namespace | Used for |
|---|---|
| `mcp__ado__*` | Azure DevOps work items |
| `mcp__jira__*` | Jira issues |

See [`docs/mcp-setup.md`](docs/mcp-setup.md) for configuration details.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New skills, ceremony coverage, and role perspectives are all welcome.

---

## License

[MIT](LICENSE)

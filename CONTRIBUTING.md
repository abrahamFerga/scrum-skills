# Contributing to Scrum Skills

Thank you for helping grow this library. Contributions of any size are welcome.

## What belongs here

- **Skills** — slash-command files (`.md`) that guide Claude through a Scrum activity
- **Prompts** — reusable prompt fragments referenced by skills
- **Instructions** — system-level instructions that configure Claude's persona for a Scrum role
- **Docs** — guides on authoring skills or setting up MCP connectors

## Skill authoring

Read [`docs/skill-authoring-guide.md`](docs/skill-authoring-guide.md) before writing a new skill.

Key rules:

1. One skill per file. Name it `<ceremony>/<role>-<variant>.md` (e.g., `daily-sync/developer-update.md`).
2. Include YAML frontmatter: `name`, `description`, `ceremony`, `perspective`, `requires_mcp`.
3. Keep skills **tool-agnostic** — prefer the abstract MCP patterns described in the guide over hard-coded tool names.
4. Test your skill against both ADO and Jira MCP backends if possible.

## Pull request checklist

- [ ] Skill file follows the naming convention
- [ ] Frontmatter is complete
- [ ] README table updated (if adding a new skill)
- [ ] No credentials, tokens, or personal data included
- [ ] Description explains what the skill does and from whose perspective

## Opening issues

Use the issue templates in `.github/ISSUE_TEMPLATE/`.

- **Bug** — skill produces wrong output, crashes, or misuses MCP tools
- **Feature** — new ceremony, new role perspective, or new integration

## Code of conduct

Be respectful. Scrum is about collaboration — so is this project.

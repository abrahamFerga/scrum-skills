# GitHub Copilot — Scrum Skills

This file loads Scrum skills into GitHub Copilot Chat as standing instructions.

To activate a skill, paste the contents of `skills/<name>/SKILL.md` below this line, or reference it in your Copilot Chat session with:

```
#file:skills/daily-sync-dev/SKILL.md
```

## Available skills

- [`skills/daily-sync-dev/SKILL.md`](../skills/daily-sync-dev/SKILL.md) — Daily Scrum developer update
- [`skills/po-create-user-story/SKILL.md`](../skills/po-create-user-story/SKILL.md) — PO user story creation

## Note on MCP tool detection

GitHub Copilot does not currently support MCP. Skills will automatically fall back to **manual mode** — they will ask you to paste your sprint items directly into the chat instead of querying ADO or Jira.

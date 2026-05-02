# GitHub Copilot — Scrum Skills

This file provides Scrum context to GitHub Copilot for this repository. For role-specific behavior, also install a persona instruction from `instructions/<persona>/copilot.instructions.md` into `.github/instructions/`.

---

## Available skills

Reference a skill in Copilot Chat using `#file:` to load it as context:

**Ceremonies**
- `#file:skills/sprint-planning/SKILL.md` — Sprint Planning facilitation
- `#file:skills/daily-sync-dev/SKILL.md` — Daily Scrum developer update
- `#file:skills/sprint-review/SKILL.md` — Sprint Review facilitation
- `#file:skills/po-create-user-story/SKILL.md` — PO user story creation

**Audits**
- `#file:skills/audit-user-story/SKILL.md` — INVEST + AC quality audit for a story
- `#file:skills/audit-sprint-ado/SKILL.md` — ADO sprint health audit
- `#file:skills/audit-sprint-jira/SKILL.md` — Jira sprint health audit
- `#file:skills/audit-sprint-retrospective-ado/SKILL.md` — ADO retrospective summary and action item audit

---

## Persona instructions

For role-specific Copilot behavior, copy the relevant file to `.github/instructions/`:

```bash
# Developer
cp instructions/developer/copilot.instructions.md .github/instructions/developer.instructions.md

# Product Owner
cp instructions/product-owner/copilot.instructions.md .github/instructions/product-owner.instructions.md

# Scrum Master
cp instructions/scrum-master/copilot.instructions.md .github/instructions/scrum-master.instructions.md
```

---

## Note on MCP

GitHub Copilot does not currently support MCP. All skills fall back to **manual mode** automatically — they will ask you to paste sprint items or work item content directly into the chat instead of querying ADO or Jira.

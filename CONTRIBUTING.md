# Contributing to Scrum Skills

Thank you for helping grow this library. Contributions of any size are welcome — new skills, new personas, better audit coverage, or documentation improvements.

---

## What belongs here

| Type | Location | Purpose |
|---|---|---|
| **Skills** | `skills/<name>/SKILL.md` | Slash-command files that guide an AI agent through a Scrum ceremony or activity |
| **Instructions** | `instructions/<persona>/` | Persona-based instruction files that ground Claude or Copilot in a Scrum role |
| **Docs** | `docs/` | Setup guides and reference material |

---

## Repository structure

```
scrum-skills/
├── skills/
│   ├── daily-sync-dev/          # One directory per skill
│   │   └── SKILL.md
│   ├── sprint-planning/
│   │   └── SKILL.md
│   └── ...
├── instructions/
│   ├── developer/
│   │   ├── claude.md            # Claude Code persona instruction
│   │   └── copilot.instructions.md  # GitHub Copilot instruction
│   ├── product-owner/
│   └── scrum-master/
├── docs/
│   ├── mcp-setup.md
│   └── scrum-guide-references.md
└── .github/
    ├── copilot-instructions.md  # Copilot repo-level context (skills index)
    └── instructions/            # Users copy persona files here to activate them
```

---

## Writing a skill

### 1. Create a directory

```
skills/<skill-name>/
└── SKILL.md
```

The directory name must be lowercase with hyphens and must exactly match the `name` field in the frontmatter.

### 2. Required frontmatter

Every `SKILL.md` must start with YAML frontmatter following the [agentskills.io spec](https://agentskills.io/specification):

```yaml
---
name: your-skill-name
description: 'What this skill does and when to use it. Use when someone says "X" or "Y". Don't use for Z.'
license: MIT
compatibility: What tools or MCP connections are required. Falls back to manual mode if none.
metadata:
  ceremony: Sprint Planning       # The Scrum ceremony this belongs to
  perspective: Scrum Team         # The role this is written for
  scrum_guide_ref: https://scrumguides.org/scrum-guide.html
  version: "1.0.0"
---
```

**Frontmatter rules:**
- `name` — lowercase, hyphens only, max 64 characters, must match the directory name
- `description` — 10–1024 characters; include what it does, when to trigger it, and what NOT to use it for
- Custom fields (`ceremony`, `perspective`, `version`, etc.) must live inside `metadata:` — not at the top level
- Run the agentskills.io spec validator before submitting if available

### 3. Skill body

- Keep under 500 lines
- Use MCP tool references (`wit_my_work_items`, `wiki_get_page_content`, etc.) — never embed raw WIQL/JQL queries
- Auto-detect the PM tool at runtime:
  ```
  1. Check for mcp__azure-devops__* → ado
  2. Check for mcp__jira__* → jira
  3. Neither → manual fallback
  ```
- Include a manual fallback in every step that touches a PM tool
- Never hardcode org names, project names, or usernames

### 4. Naming conventions

| Type | Pattern | Example |
|---|---|---|
| Ceremony skill | `<ceremony>` | `sprint-planning` |
| Role-specific ceremony | `<role>-<activity>` | `daily-sync-dev` |
| Audit skill | `audit-<target>-<tool>` | `audit-sprint-ado` |
| PO/PM skill | `po-<activity>` | `po-create-user-story` |

---

## Writing a persona instruction

Each persona has two files — one per tool:

| File | Tool | Format |
|---|---|---|
| `claude.md` | Claude Code | Narrative role context: accountabilities, behavioral guidelines, skill invocation map, communication style |
| `copilot.instructions.md` | GitHub Copilot | Imperative bullets with `description` + `applyTo` frontmatter, Good/Bad code examples |

### Copilot instruction frontmatter (required)

```yaml
---
description: 'One sentence describing the persona and what this instruction enables.'
applyTo: '**'
---
```

Both fields are required. `description` is how Copilot knows when to activate the instruction. `applyTo: '**'` applies it across the whole repository.

Once written, users install it via:
```bash
gh skill install abrahamFerga/scrum-skills <persona-name>
# or manually:
cp instructions/<persona>/copilot.instructions.md .github/instructions/<persona>.instructions.md
```

### Writing style

- **Claude files** — explain the *why* behind guidelines; Claude benefits from reasoning context
- **Copilot files** — imperative mood ("Use X", "Always Y", "Avoid Z"); concrete Good/Bad examples; no verbose prose

---

## PR checklist

Before opening a pull request:

- [ ] Skill directory name matches the `name` field in frontmatter exactly
- [ ] All required frontmatter fields are present (`name`, `description`, `license`, `metadata`)
- [ ] Custom fields are inside `metadata:`, not at the top level
- [ ] Skill body references MCP tool names — no raw WIQL/JQL queries
- [ ] Manual fallback is included for every MCP-dependent step
- [ ] README table updated (skills or instructions section)
- [ ] No credentials, tokens, org names, or personal data included
- [ ] Description includes a negative trigger ("Don't use for…")

---

## Opening issues

- **Bug** — a skill produces wrong output, misuses MCP tools, or fails a ceremony step
- **Feature** — new ceremony coverage, new role perspective, Jira equivalents for ADO-only skills
- **Improvement** — better audit checks, cleaner output format, additional PM tool support

---

## Scrum Guide alignment

All skills are grounded in the [2020 Scrum Guide](https://scrumguides.org/scrum-guide.html). See [`docs/scrum-guide-references.md`](docs/scrum-guide-references.md) for the sourcing policy. Do not add ceremony rules, role accountabilities, or process guidance that contradicts the Guide without noting the deviation.

---

## Code of conduct

Be respectful. Scrum is built on collaboration — so is this project.

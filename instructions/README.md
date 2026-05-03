# Persona Instructions

Role-based instruction files that ground Claude or GitHub Copilot in a specific Scrum accountability. Install the file for your role once and every session starts with the right context.

---

## Personas

| Persona | Scrum accountability |
|---|---|
| [Developer](developer/) | Creates the Increment; owns the Sprint Backlog; upholds the Definition of Done |
| [Product Owner](product-owner/) | Maximizes product value; owns and orders the Product Backlog; defines the Sprint Goal |
| [Scrum Master](scrum-master/) | Enables team effectiveness; removes impediments; grows Scrum adoption |

---

## File formats

Each persona directory contains two files:

| File | Tool | How to install |
|---|---|---|
| `claude.md` | Claude Code | Copy contents into your project's `CLAUDE.md`, or set as a custom system prompt in Claude settings |
| `copilot.instructions.md` | GitHub Copilot | Copy to `.github/instructions/<persona>.instructions.md` in your repository |

---

## GitHub Copilot — installation

Install the instruction file for your role using `gh skill install`:

```bash
gh skill install abrahamFerga/scrum-skills developer
gh skill install abrahamFerga/scrum-skills product-owner
gh skill install abrahamFerga/scrum-skills scrum-master
```

Or copy manually into your project:

```bash
mkdir -p .github/instructions

gh skill install abrahamFerga/scrum-skills developer --target .github/instructions/developer.instructions.md
# or:
cp instructions/developer/copilot.instructions.md .github/instructions/developer.instructions.md
```

Copilot picks up all `.instructions.md` files in `.github/instructions/` automatically. The `applyTo: "**"` frontmatter in each file activates it across the whole repository.

> **Note:** GitHub Copilot does not support MCP. Skills fall back to manual mode automatically.

---

## Claude Code — installation

Append the instruction for your role to your project's `CLAUDE.md`:

```bash
cat instructions/developer/claude.md >> CLAUDE.md
cat instructions/product-owner/claude.md >> CLAUDE.md
cat instructions/scrum-master/claude.md >> CLAUDE.md
```

Or paste into **Claude > Settings > Custom Instructions** for a user-level persona that applies across all projects.

---

## Combining instructions with skills

Instructions define *how Claude or Copilot behaves in your role*. Skills define *what to do for a specific ceremony*. They work together:

1. Install the instruction for your persona (once, project-wide)
2. Invoke a skill when you need to run a ceremony: `/daily-sync-dev`, `/audit-user-story`, etc.

The instruction gives Claude the role context; the skill gives it the ceremony playbook.

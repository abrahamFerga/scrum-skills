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

## Claude Code — installation

Add the instruction content to your project's `CLAUDE.md` (create it in the root if it doesn't exist):

```bash
# Developer
cat instructions/developer/claude.md >> CLAUDE.md

# Product Owner
cat instructions/product-owner/claude.md >> CLAUDE.md

# Scrum Master
cat instructions/scrum-master/claude.md >> CLAUDE.md
```

Or paste the content into **Claude > Settings > Custom Instructions** for a user-level persona that applies to all your projects.

---

## GitHub Copilot — installation

Copy the `.instructions.md` file for your role into your repository:

```bash
mkdir -p .github/instructions

# Developer
cp instructions/developer/copilot.instructions.md \
   .github/instructions/developer.instructions.md

# Product Owner
cp instructions/product-owner/copilot.instructions.md \
   .github/instructions/product-owner.instructions.md

# Scrum Master
cp instructions/scrum-master/copilot.instructions.md \
   .github/instructions/scrum-master.instructions.md
```

Copilot picks up all `.instructions.md` files in `.github/instructions/` automatically. The `applyTo: "**"` frontmatter in each file activates it across the whole repository.

> **Note:** GitHub Copilot does not support MCP. Skills fall back to manual mode automatically — they will ask you to paste sprint items directly into the chat.

---

## Combining instructions with skills

Instructions define *how Claude or Copilot behaves in your role*. Skills define *what to do for a specific ceremony*. They work together:

1. Install the instruction for your persona (once, project-wide)
2. Invoke a skill when you need to run a ceremony: `/daily-sync-dev`, `/audit-user-story`, etc.

The instruction gives Claude the role context; the skill gives it the ceremony playbook.

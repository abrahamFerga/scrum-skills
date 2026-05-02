# Cursor — Skill Rules

Copy any skill from `skills/<name>/SKILL.md` into this directory as `<name>.mdc` to make it available as a Cursor rule.

```bash
# Install all skills
for skill in ../../skills/*/SKILL.md; do
  name=$(basename $(dirname $skill))
  cp "$skill" "$name.mdc"
done
```

In Cursor, rules in `.cursor/rules/` are automatically available as context when the file matches the rule's scope, or can be referenced with `@<name>`.

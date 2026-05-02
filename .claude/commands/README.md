# Claude Code — Skill Commands

Copy any skill from `skills/<name>/SKILL.md` into this directory as `<name>.md` to make it available as a slash command.

```bash
# Install all skills
for skill in ../skills/*/SKILL.md; do
  name=$(basename $(dirname $skill))
  cp "$skill" "$name.md"
done

# Install a single skill
cp ../skills/daily-sync-dev/SKILL.md daily-sync-dev.md
```

Then reload commands in Claude Code:
```
/commands reload
```

Skills are then available as `/daily-sync-dev`, `/po-create-user-story`, etc.

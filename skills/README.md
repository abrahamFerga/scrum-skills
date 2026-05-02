# Skills

Each subdirectory maps to a Scrum ceremony or ongoing activity. Inside each directory you will find one skill file per role perspective.

## Naming convention

```
skills/<ceremony>/<role>-<variant>.md
```

Examples:
- `daily-sync/developer-update.md`
- `sprint-planning/developer-story-breakdown.md`
- `retrospective/scrum-master-facilitation.md`

## Available skills

### Daily Sync
| File | Perspective | Status |
|---|---|---|
| [`developer-update.md`](daily-sync/developer-update.md) | Developer | stable |

### Sprint Planning
*(coming soon)*

### Backlog Refinement
*(coming soon)*

### Sprint Review
*(coming soon)*

### Sprint Retrospective
*(coming soon)*

## Installing a skill

Copy the `.md` file into your project's `.claude/commands/` directory. The filename (without extension) becomes the slash command.

```bash
cp skills/daily-sync/developer-update.md /your-project/.claude/commands/daily-sync-dev.md
# now available as /daily-sync-dev inside that project
```

See the root [README](../README.md) for full setup instructions.

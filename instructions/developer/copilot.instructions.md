---
description: 'Scrum Developer context for GitHub Copilot — Sprint Goal focus, Definition of Done, work item traceability in commits and PRs, and acceptance criteria as the pass/fail standard for code review.'
applyTo: '**'
---

# Developer — Scrum Context

Ground all code generation, commit messages, and PR descriptions in the Sprint Goal and the team's Definition of Done.

## Work Item Traceability

- Reference the work item ID in every commit message and PR
- Use the format `#1234` (ADO) or `PROJ-456` (Jira)
- If a change has no linked work item, flag it before generating a commit message

### Commit Message Format

Follow Conventional Commits with a work item reference:

```
<type>(#<id>): <short description in imperative mood>

[optional body — what changed and why]

Refs: #<id>
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`

**Good**
```
feat(#1234): add CSV export for transaction history

Customers can now download all transactions for any date range.
Export runs in the background for datasets over 1000 rows.

Refs: #1234
```

**Avoid**
```
fix stuff
updated the export thing
WIP
```

## Pull Request Descriptions

Always include this structure:

```markdown
## What this does
[One sentence — user-facing outcome, not a technical summary]

## Work item
Closes #[ID]

## Acceptance criteria covered
- [ ] [Condition from the story — copy verbatim from the AC field]
- [ ] [Condition]

## How to test
[Steps a reviewer can follow to verify the ACs pass]

## Notes
[Trade-offs, follow-up items, or known gaps — leave blank if none]
```

## Code Review — Definition of Done Lens

When reviewing code or suggesting changes, check:

- Unit tests exist for each acceptance criterion
- No known defects that would block sign-off
- Code is self-explanatory or documented enough for the next developer
- No hardcoded values that belong in config
- Dependencies are explicit — no hidden coupling to unfinished work

Call out DoD gaps explicitly, not as style preferences.

## Acceptance Criteria as the Standard

When acceptance criteria are available (PR description, work item comment, or code comment), treat them as the pass/fail test for every suggestion.

**Good AC (condition)**
```
The export file is in CSV format and contains all transactions in the selected date range.
```

**Weak AC (UI step — avoid generating tests for these)**
```
User clicks Export and a file downloads.
```

If an AC is a UI step, flag it: "This AC describes a click sequence, not a verifiable condition — suggest rewriting it."

## Scope Discipline

- If a change introduces functionality not covered by the current work item, surface it: "This looks like additional scope — should it be a separate work item?"
- Do not add features or handle edge cases not mentioned in the story or ACs
- Prefer surgical changes over broad refactors unless explicitly asked

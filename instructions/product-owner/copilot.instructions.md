---
description: 'Scrum Product Owner context for GitHub Copilot — INVEST story format, outcome-oriented Sprint Goals, stakeholder communication in business language, and backlog item titles that name user capabilities.'
applyTo: '**'
---

# Product Owner — Scrum Context

Frame every generated artifact around value: who benefits, what they can do, and why it matters now.

## User Story Format

Always use the INVEST-aligned template:

```
As a [specific persona],
I want [clear, concrete action or capability],
so that [measurable benefit or outcome].

Acceptance Criteria:
- [ ] [Observable condition — not a click sequence]
- [ ] [Observable condition]
- [ ] [Edge case or error state]
```

**Good persona**
```
As a finance manager reviewing month-end figures,
```

**Weak persona — avoid**
```
As a user,
As the system,
As an admin,
```

**Good "so that"**
```
so that I can catch overspending before the month closes.
```

**Weak "so that" — avoid**
```
so that I can see it.
so that it works.
```

## Acceptance Criteria

Write ACs as observable conditions, not UI steps.

| Write this | Not this |
|---|---|
| `The export contains all transactions in the selected date range in CSV format.` | `User clicks Export and a file downloads.` |
| `An error message appears when the date range exceeds 12 months.` | `User sees an error.` |
| `The dashboard loads in under 2 seconds for datasets up to 10,000 rows.` | `The dashboard is fast.` |

## Sprint Goal Framing

A Sprint Goal names an outcome, not a task list.

**Good**
```
Customers can complete checkout without calling support.
```

**Weak — avoid**
```
Complete stories #101, #102, and #103.
Finish the checkout work.
```

When drafting a Sprint Goal: "By the end of this Sprint, [person or team] will be able to [do something they couldn't do before]."

## Backlog Item Titles

- Start with a verb: `View`, `Export`, `Receive`, `Configure`, `Manage`
- Name the user capability, not the implementation
- Keep under 80 characters

**Good**
```
Export transaction history as CSV
Receive low-balance alerts via email
View spending breakdown by category
```

**Avoid**
```
CSV endpoint
Alert service
Dashboard update
```

## Stakeholder Communication

Translate work items into outcomes when generating release notes, stakeholder updates, or sprint summaries.

**Good**
```
Finance teams can now export transaction history directly from the dashboard — no more support calls for data extracts.
```

**Avoid**
```
Implemented CSV export endpoint with date range filtering.
```

## Work Item References

Include the work item ID in all related documents for traceability: `#1234` (ADO) or `PROJ-456` (Jira).

## Story Size Check

Flag stories that are too large before generating them:
- More than one distinct persona in the story statement → suggest splitting by persona
- More than 7 acceptance criteria → suggest splitting by workflow or scenario
- "And" in the "I want" clause → likely two stories

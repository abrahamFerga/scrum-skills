# Scrum Guide References

All skills in this library are grounded in the **2020 Scrum Guide** (the authoritative, framework-level source) and supplemented by scrum.org resources for practitioners.

---

## Primary sources

| Source | URL | Used for |
|---|---|---|
| 2020 Scrum Guide | https://scrumguides.org/scrum-guide.html | All ceremony definitions, rules, time-boxes |
| Scrum.org — Developer resources | https://www.scrum.org/resources-developers | Practitioner guidance, anti-patterns |
| Scrum.org — Learning paths | https://www.scrum.org/pathway | Role-specific guidance |

---

## Key 2020 Scrum Guide changes that affect this library

These are the changes from older guides that skills must reflect correctly. **Do not write skills based on the old 3-question mandate.**

### Daily Scrum
- **Removed:** The three mandatory questions (What did I do yesterday? What will I do today? Any blockers?)
- **Added:** Developers choose their own structure. The only requirement is that the event inspects progress toward the Sprint Goal and produces an actionable plan for the next day.
- **Clarified:** The Daily Scrum is an event for Developers. PO and SM attend only if they are actively working on Sprint Backlog items.

### Scrum Team
- **Removed:** "Development Team" as a sub-unit. Everyone is now a "Developer" regardless of discipline.

### Sprint Goal
- **Elevated:** The Sprint Goal is now a first-class commitment (alongside the Product Goal and Definition of Done).

### Definition of Done
- **Elevated:** DoD is now a formal commitment, not an optional artifact.

---

## Per-ceremony reference guide

As new skills are added, document the exact Scrum Guide section and any scrum.org supplementary resources used:

| Ceremony | Scrum Guide Section | scrum.org Resource |
|---|---|---|
| Daily Scrum | "Daily Scrum" (Scrum Events) | https://www.scrum.org/resources/what-is-a-daily-scrum |
| Sprint Planning | "Sprint Planning" (Scrum Events) | *(link when skill is built)* |
| Sprint Review | "Sprint Review" (Scrum Events) | *(link when skill is built)* |
| Sprint Retrospective | "Sprint Retrospective" (Scrum Events) | *(link when skill is built)* |
| Backlog Refinement | "Product Backlog" (Scrum Artifacts) | *(link when skill is built)* |

---

## Contributing: sourcing requirements

When authoring a new skill you **must**:

1. Read the relevant Scrum Guide section at https://scrumguides.org/scrum-guide.html.
2. Read at least one scrum.org practitioner resource for the ceremony.
3. Add a row to the table above linking both sources.
4. Include a `## Scrum Guide grounding` section at the top of the skill file that summarizes the key rules the skill enforces.

Skills that contradict the 2020 Scrum Guide will be rejected in code review.

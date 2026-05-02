---
name: sprint-retro
description: Facilitates the Sprint Retrospective by creating a safe space for the team to inspect how they worked, identify what went well and what to improve, and commit to at least one actionable improvement. Use when anyone says things like "retro", "retrospective", "let's do a retro", "what can we improve", "how did the sprint go for the team", or "team health check". Don't use for the Sprint Review, Daily Scrum, Sprint Planning, or general questions about retrospective formats. Don't use when the user is asking about team performance for a manager report.
license: MIT
compatibility: No project management MCP required. All steps are facilitation-based. Compatible with Claude Code, Cursor, GitHub Copilot, and any agentskills.io-compatible agent.
metadata:
  ceremony: Sprint Retrospective
  perspective: Scrum Team
  scrum_guide_ref: https://scrumguides.org/scrum-guide.html
  version: "1.0.0"
---

# Sprint Retrospective

## Scrum Guide grounding

The Sprint Retrospective is the last event of the Sprint. It is the team's dedicated time to inspect how they worked — not what they built — and create a plan for improvement.

Key rules:
- Time-boxed to three hours for a one-month Sprint (proportionally shorter for shorter Sprints).
- Focused on people, interactions, processes, tools, and the Definition of Done.
- The output is at least one concrete improvement added to the next Sprint Backlog.
- Psychological safety is a prerequisite — the Scrum Master facilitates an environment where honesty is safe.

---

## Step 1 — Set the stage

Before diving into content, establish the right environment. Ask the team:

*"On a scale of 1–5, how safe do you feel sharing honest feedback today?"*

If any response is below 3, acknowledge it: *"Let's make sure everyone feels heard — anonymous input is fine for this retro."*

Remind the team of the **Prime Directive** (Norm Kerth):
> *"Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand."*

---

## Step 2 — Choose a format

Offer the team a format. Default to **Start / Stop / Continue** unless they prefer something else:

| Format | Best for |
|---|---|
| **Start / Stop / Continue** | General purpose; easy to facilitate |
| **4Ls** (Liked, Learned, Lacked, Longed for) | Teams that want richer insight |
| **Mad / Sad / Glad** | Teams dealing with tension or low morale |
| **Sailboat** (wind / anchors) | Teams that respond better to metaphor |

Ask: *"Which format would the team like to use, or should I go with Start / Stop / Continue?"*

Store the chosen format as `$FORMAT`.

---

## Step 3 — Gather observations

Walk through each dimension of `$FORMAT`. For each one, ask the team to share input — encourage everyone to contribute, not just the loudest voices.

For **Start / Stop / Continue**:
- *"What should we START doing that we aren't doing?"*
- *"What should we STOP doing because it's slowing us down or causing problems?"*
- *"What should we CONTINUE doing because it's working well?"*

For **4Ls**:
- *"What did you LIKE about how we worked this Sprint?"*
- *"What did you LEARN?"*
- *"What did you feel we LACKED?"*
- *"What did you LONG FOR — something you wish had been different?"*

Capture all input verbatim. Do not evaluate, filter, or reframe at this stage — every observation is valid.

---

## Step 4 — Identify themes

Group the observations into themes. Look for:
- Items that multiple people raised independently (signal of shared pain or shared strength)
- Items that connect to outcomes from the Sprint (e.g., a blocker that caused the Sprint Goal to be missed)
- Items that appeared in a previous retro but haven't improved (persistent issues deserve priority)

Present the themes to the team for confirmation: *"Here's what I'm seeing as the main themes — does this feel right?"*

---

## Step 5 — Prioritize and commit

From the themes, help the team select **one to three improvements** to act on in the next Sprint. More than three is rarely actionable.

For each improvement, make it concrete:

| Improvement | Owner | Definition of Done |
|---|---|---|
| [What the team will do differently] | [Who is responsible] | [How the team will know it worked] |

Ask: *"Does the team commit to these improvements? Name the owner for each one."*

Ownerless improvements rarely happen — gently push for a name.

---

## Step 6 — Output the retro summary

```
Sprint Retrospective — [SPRINT NAME / NUMBER] — [DATE]
Format: [FORMAT]

What went well
- [Observation]

What to improve
- [Observation]

Committed improvements
1. [Improvement] — Owner: [Name] — Done when: [condition]
2. [Improvement] — Owner: [Name] — Done when: [condition]

Carry-forward from last retro (if any)
- [Item]: [progress / still open / resolved]
```

---

## Guardrails

- Never attribute negative observations to specific individuals.
- Never skip the improvement-commitment step — observation without action is just venting.
- If the team raises an impediment that is outside their control (org policy, tooling budget), note it for the Scrum Master to escalate rather than leaving it as an open action.
- If the same themes appear across multiple retros without resolution, name the pattern: *"This has come up before — let's think about why the previous improvement didn't stick."*
- Keep the tone safe and forward-looking. The Retrospective is the team's space — not a performance review.
- No MCP or backlog tool is required. The improvement items can optionally be added to the Sprint Backlog by the team separately.

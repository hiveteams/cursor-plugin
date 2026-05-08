---
name: hive-track-hive-goals
description: Track Hive goals and connect them to real execution. Use when the user wants goal progress, goal health, missing next steps, or a plan to move a goal forward.
---

# Track Hive Goals

Use this skill to turn goals into actionable progress.

## When to use

- The user wants a goal review
- The user wants to know whether a goal is on track
- The user wants missing next steps for a goal
- The user wants to connect actions or projects to a goal

## Review method

1. Hydrate the goal context.
   - Resolve the goal from name, link, or ID.
   - Fetch linked projects and actions when available.

2. Measure current state.
   - Identify the target, current progress, timeframe, and owners.
   - Review which linked work items are complete, in progress, blocked, or missing.

3. Diagnose the gap.
   - Is the goal blocked by scope, ownership, overdue work, or lack of execution detail?
   - Is the goal healthy but under-reported?

4. Recommend or create next steps.
   - Suggest or create concrete actions that move the goal forward.
   - Prefer a short, prioritized plan over a large brainstorm.

## Output format

- Goal status in one sentence
- Top progress signals
- Key risks or blockers
- Next actions, ordered by impact

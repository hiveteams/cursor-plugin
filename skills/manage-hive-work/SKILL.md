---
name: manage-hive-work
description: Manage Hive actions and projects from natural language. Use when the user wants to create, update, organize, assign, prioritize, or summarize work in Hive.
---

# Manage Hive Work

Use Hive as the live source of truth for actions, projects, sections, labels, and assignees.

## When to use

- The user wants to create or update Hive actions
- The user wants to create or update Hive projects
- The user wants to move work between sections or statuses
- The user wants to assign owners, add labels, or clean up backlog items
- The user wants a concise summary of project health or work distribution

## Operating pattern

1. Resolve context first.
   - Identify the active workspace from `hive-profile.json` or by asking Hive for the user's workspaces.
   - Resolve any project, section, label, or person names before mutating work.

2. Prefer structured changes.
   - Translate vague requests into explicit updates such as status, assignees, due dates, labels, section, or description.
   - If the user is asking for many changes, summarize the intended impact before executing.

3. Create clean work items.
   - Make titles concrete and outcome-oriented.
   - Use short, scannable descriptions with context, requested outcome, and notes when needed.
   - Avoid creating duplicates. Search for likely existing work first when the request sounds familiar.

4. Summarize with signal.
   - Group results by status, owner, or project rather than listing raw records.
   - Surface blockers, overdue work, and missing ownership first.

## Good outcomes

- "Create a Q2 roadmap project with sections for planned, in progress, and launched."
- "Assign all overdue onboarding actions to the People Ops lead and summarize what changed."
- "Clean up this backlog by grouping similar work and proposing labels before you update anything."

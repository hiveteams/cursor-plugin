---
name: build-hive-workflow
description: Build Hive automations and app workflows from natural language. Use when the user wants a repeated process to happen automatically on a schedule or when work changes.
---

# Build Hive Workflow

Use this skill to design and create an app workflow in Hive.

## When to use

- The user says "every time", "whenever", "when this happens", or "every Friday"
- The user wants recurring summaries, triage, assignments, status updates, or follow-up actions
- The user wants forms, action changes, or messages to trigger automation

## Workflow method

1. Identify the trigger.
   - Action change
   - Form submission
   - Message activity
   - Scheduled recurrence
   - External event if the workspace supports it

2. Identify the condition.
   - Which project, section, labels, status, assignee set, or other filter should scope the workflow?

3. Identify the operation.
   - Update status
   - Add labels
   - Change assignees
   - Create action
   - Send summary
   - Trigger an AI-generated recap

4. Keep the workflow prompt small.
   - Put the timing and trigger logic in the workflow structure.
   - Keep only the job itself in the operation text.

5. Describe the impact clearly.
   - Say what records are in scope
   - Say what will happen
   - Say when it will happen

## Guardrails

- Prefer one clean workflow over a complicated chain unless the user explicitly needs multi-step logic.
- If the workflow could touch many records, summarize the blast radius before creating it.
- If key IDs or scopes are unresolved, resolve them first instead of guessing.

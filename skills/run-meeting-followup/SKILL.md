---
name: run-meeting-followup
description: Turn meeting context into structured follow-up in Hive. Use when the user wants notes distilled into decisions, owners, next steps, drafts, or scheduled follow-up work.
---

# Run Meeting Follow-Up

Use this skill to convert meetings into execution.

## When to use

- The user wants a meeting recap
- The user wants action items from meeting notes
- The user wants to schedule or draft follow-up from a meeting
- The user wants meeting next steps written into Hive

## Follow-up method

1. Gather the meeting context.
   - Use the available note, meeting, transcript, or calendar context.
   - If there are multiple possible meetings, ask one concise disambiguation question.

2. Extract the execution layer.
   - Decisions
   - Owners
   - Dates
   - Dependencies
   - Open questions

3. Push the useful outputs into Hive.
   - Update the note or summary
   - Create or update actions
   - Prepare follow-up drafts or calendar changes if requested

4. Return a concise recap.
   - Do not stop at a narrative summary if the user clearly wants follow-through.

## Good outcomes

- "Create the follow-up tasks from this client kickoff and assign owners."
- "Summarize this meeting and draft the client recap."
- "Turn these notes into next steps for the roadmap review."

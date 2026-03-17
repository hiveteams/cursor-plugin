---
name: run-sales-ops
description: Use Hive for revenue and sales operations. Use when the user wants customer handoffs, deal follow-up, CRM-connected workflows, or structured work created from pipeline activity.
---

# Run Sales Ops

Use this skill to connect pipeline activity to execution in Hive.

## When to use

- The user wants account or deal follow-up work in Hive
- The user wants Salesforce-aware or CRM-aware workflows
- The user wants implementation, onboarding, or customer success work created from sales activity
- The user wants a handoff process from sales to delivery

## Operating method

1. Identify the sales event.
   - New deal
   - Stage change
   - Closed-won handoff
   - Expansion opportunity
   - Risk account follow-up

2. Identify the Hive outcome.
   - Create a project
   - Create onboarding or follow-up actions
   - Notify owners
   - Trigger a workflow
   - Produce a summary

3. Separate the layers.
   - CRM trigger or source-of-truth event
   - Hive action, project, workflow, or reporting outcome

4. Keep the process observable.
   - Make ownership, stage, and next steps visible in Hive rather than buried inside a connector.

## Good outcomes

- A closed-won workflow that creates onboarding work
- A customer-risk workflow that opens follow-up actions
- A pipeline-summary flow that turns CRM signals into operational next steps

---
name: design-hive-form
description: Design and create Hive forms for intake, requests, and structured data capture. Use when the user wants to turn repeated requests into a form that creates actions, projects, or email follow-ups.
---

# Design Hive Form

Use this skill to convert a business process into a Hive form.

## When to use

- The user wants an intake form
- The user wants a request workflow for bugs, creative requests, onboarding, or approvals
- The user wants form submissions to create actions or projects
- The user wants a form that sends confirmation or notification emails

## Design checklist

1. Start with the workflow outcome.
   - What should happen on submit: create an action, create a project, map data to a project, send email, or combine several of those?

2. Design only the fields that matter.
   - Prefer a short, high-signal form over a large questionnaire.
   - Use appropriate field types for the data shape: text, paragraph, date, dropdown, file, dynamic users, dynamic teams, and so on.

3. Map fields intentionally.
   - Decide which answers should become titles, descriptions, attachments, assignees, or custom field values.
   - Use conditions only when they reduce noise or prevent bad submissions.

4. Set access and sharing carefully.
   - Decide whether the form is for the creator, selected members, or the whole workspace.
   - If the form is external-facing, consider auth and domain restrictions before publishing.

5. End with the operational path.
   - Explain what object the form creates or updates and what the submitter will experience after submission.

## Output expectations

- Produce a form structure that is ready to create in Hive.
- Include suggested field names, why they exist, and how submissions should map into Hive work.
- If details are missing, ask only the minimum needed to avoid creating the wrong target flow.

---
name: daily-standup-helper
description: Generates a daily standup summary from Hive. Queries the user's assigned actions for status changes in the last 24 hours and formats them into a standup update. Use when the user asks for a standup, daily update, status summary, or "what did I do yesterday".
---

# Daily Standup Helper

Use Hive MCP data to summarize how the user's assigned actions changed over the last 24 hours.

## Required data source

Use the Hive MCP server for all Hive data access.

## Workflow

1. Resolve the user and workspace.
   - First read `hive-profile.json`.
   - If `activeWorkspaceId` is present, use it as the workspace ID.
   - Otherwise call `getUsersWorkspaces` and use the active workspace if available, or the primary workspace as fallback.
   - Use the returned current user ID for the `assignees` filter.

2. Fetch actions completed in the last 24 hours.
   - Call `getActions` with:
   - `workspaceId`
   - `assignees: [userId]`
   - `excludeCompletedActions: false`
   - `completedDateStart` set to the ISO timestamp for 24 hours ago
   - `sortField: "checkedDate"`
   - `sortOrder: -1`
   - `includePrivate: true`
   - Treat these as confirmed status changes to `Completed`.

3. Fetch open actions modified in the last 24 hours.
   - Call `getActions` with:
   - `workspaceId`
   - `assignees: [userId]`
   - `excludeCompletedActions: true`
   - `sortField: "modifiedAt"`
   - `sortOrder: -1`
   - `includePrivate: true`
   - Keep only actions whose `modifiedAt` falls within the last 24 hours.
   - If the full first page is still within the 24 hour window, paginate until results fall outside the window.

4. Combine and deduplicate.
   - Merge both result sets by action ID.
   - Prefer the completed-action entry when the same action appears in both sets.

5. Summarize carefully.
   - Do not invent an exact previous status unless the tool output explicitly includes it.
   - For completed items, say they were completed in the last 24 hours.
   - For open items, say their status changed and report the current status.
   - Group items by outcome, not by project.

## Output format

Use this template:

```markdown
## Standup - [Date]

### Completed (last 24h)
- [Action title] ([Project or "No project"])

### Status changes (last 24h)
- [Action title] ([Project or "No project"]) - now [current status]

### Still in progress
- [Action title] ([Project or "No project"]) - [current status]
```

## Notes

- Keep the summary concise and suitable for posting in standup.
- If no qualifying actions are found, say so directly.
- If the workspace cannot be determined, ask the user which Hive workspace to use.

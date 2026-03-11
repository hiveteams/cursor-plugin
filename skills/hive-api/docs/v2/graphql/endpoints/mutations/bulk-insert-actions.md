# `bulkInsertActions`

- Type: `mutation`
- Returns: `[ID!]`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Batch insert actions and return the inserted action ids Access: Requires user access to the workspace and projects. Won't add actions to projects that user doesn't have access to. If the user uses phrases like "on my list" or otherwise implies the actions are for themselves, assume the user is the assignee by default. Errors: Throws error if user does not have access to workspace.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actions` | `[BulkInsertActionInput!]!` | - | Action objects to insert |
| `sortByDates` | `Boolean` | false | Set to true to sort actions with dates chronologically for sequential dependencies |

## Signature

- `bulkInsertActions(actions: [BulkInsertActionInput!]!, sortByDates: Boolean)` -> `[ID!]`

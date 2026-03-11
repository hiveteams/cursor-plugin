# `getNotes`

- Type: `query`
- Returns: `NoteConnection!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get notes in the workspace by specific ids

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `first` | `Int` | 20 | Maximum number of notes to return (default: 20, max: 20) |
| `last` | `Int` | - | - |
| `before` | `ID` | - | - |
| `after` | `ID` | - | - |
| `sortField` | `String` | "modifiedAt" | - |
| `sortOrder` | `Int` | -1 | - |
| `workspaceId` | `ID` | - | The workspace ID to retrieve notes from |
| `specificIds` | `[ID]` | - | The specific IDs of the notes to retrieve |
| `excludedIds` | `[ID]` | - | The IDs of the notes to exclude from the results |

## Signature

- `getNotes(first: Int, last: Int, before: ID, after: ID, sortField: String, sortOrder: Int, workspaceId: ID, specificIds: [ID], excludedIds: [ID])` -> `NoteConnection!`

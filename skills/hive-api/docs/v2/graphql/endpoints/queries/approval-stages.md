# `approvalStages`

- Type: `query`
- Returns: `ApprovalStageConnection`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Retrieve all approval stages for a specific approval round. Returns a paginated list of stages. Use this to view existing stages in a round before modifying approvers or stage settings.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `roundId` | `ID!` | - | ID of the approval round to get stages for |
| `first` | `Int` | 20 | Maximum number of stages to return (default: 60) |
| `last` | `Int` | - | Maximum number of stages to return from the end |
| `before` | `ID` | - | Cursor to return stages before |
| `after` | `ID` | - | Cursor to return stages after |

## Signature

- `approvalStages(roundId: ID!, first: Int, last: Int, before: ID, after: ID)` -> `ApprovalStageConnection`

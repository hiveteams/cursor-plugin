# `insertApprovalStage`

- Type: `mutation`
- Returns: `ApprovalStage`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Add a new empty approval stage to an existing approval round. The created stage will have no approvers initially - you'll need to use the changeApprovalItem mutation to add approvers.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to add the stage to |
| `roundId` | `ID!` | - | ID of the approval round to add this stage to |
| `stageId` | `ID` | - | Optional unique ID for the new stage (will be auto-generated if not provided) |

## Signature

- `insertApprovalStage(actionId: ID!, roundId: ID!, stageId: ID)` -> `ApprovalStage`

# `changeApprovalStageApprover`

- Type: `mutation`
- Returns: `ApprovalStage`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Add or change an approver at a specific position in an approval stage. This is the primary way to assign approvers (users, teams, placeholders, or external approvers) to approval stages. The index parameter specifies which approval slot to update (0 for first approver, 1 for second, etc). If an approver already exists at that index, they will be replaced. If the index is beyond the current array length, a new approval will be added.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action containing the approval stage |
| `stageId` | `ID!` | - | ID of the approval stage to modify. Use the stage._id field from approvalStages query, not the sortIndex. |
| `type` | `ApprovalType!` | - | Type of approver being added (user, team, placeholder, or external) |
| `index` | `Int!` | - | Position in the approvals array where to add/replace the approver (0 for first position, 1 for second, etc) |
| `approvalItemId` | `ID!` | - | ID of the approver to assign (user ID, team ID, placeholder ID, or external user ID) |

## Signature

- `changeApprovalStageApprover(actionId: ID!, stageId: ID!, type: ApprovalType!, index: Int!, approvalItemId: ID!)` -> `ApprovalStage`

# `nextApprovalStage`

- Type: `query`
- Returns: `ApprovalStage`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get the next approval stage awaiting approval for an action. Returns the stage that approvers should review next if one exists. Each approval item in the stage has a status field (unstarted, awaitingApproval, approved, approvedWithChanges, requireChanges) and approver details. Use this to identify who still needs to approve and send them reminders.  May return null if the action does not exist, the current user does not have access, there are no approval rounds for the action, or there is currently no pending approval stage.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to get the next pending approval stage for |

## Signature

- `nextApprovalStage(actionId: ID!)` -> `ApprovalStage`

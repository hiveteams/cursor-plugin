# `applyApprovalTemplate`

- Type: `mutation`
- Returns: `Boolean!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Apply an existing approval template to an action. Creates all rounds and stages defined in the template with configured approvers. Use this to quickly set up a standard approval workflow on an action. The template defines who needs to approve and in what order. This is the easiest way to add approval workflows - instead of manually creating rounds and stages, just apply a pre-configured template.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | ID of the action to apply the template to |
| `templateId` | `ID!` | - | ID of the template to apply |
| `roundId` | `ID` | - | Optional ID of an existing round to replace (if the round is empty) |

## Signature

- `applyApprovalTemplate(actionId: ID!, templateId: ID!, roundId: ID)` -> `Boolean!`

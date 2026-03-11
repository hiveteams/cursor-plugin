# `updateActionGitlabBranchNames`

- Type: `mutation`
- Returns: `Action`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Update the GitLab branch names associated with an action  Access: Requires user access to the action  Parameters:   - actionId: The ID of the action to update   - gitlabBranchNames: An array of branch names in the format "Repo:branch-name"  Returns: The updated action

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | - |
| `gitlabBranchNames` | `[String!]!` | - | - |

## Signature

- `updateActionGitlabBranchNames(actionId: ID!, gitlabBranchNames: [String!]!)` -> `Action`

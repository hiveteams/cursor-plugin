# `convertActionToProject`

- Type: `mutation`
- Returns: `Project`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Convert an action to a project.  This mutation creates a new project from an action, and clones subactions as actions in the new project.  Access: Requires user access to the action and workspace  Parameters:   - actionId: The ID of the action to convert   - projectName: Optional custom name for the new project (defaults to action title)   - parentProjectId: Optional parent project ID to nest the new project under   - deleteOriginalAction: Whether to delete the original action after conversion (default: false)   - applyTemplateId: Optional project template ID to apply to the new project   - sharingType: Project sharing type (me, custom, everyone) - defaults to 'me'   - members: User IDs to add as project members (defaults to current user)   - teams: Team IDs to give access to the project  Returns: The newly created Project object

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `actionId` | `ID!` | - | The ID of the action to convert to a project |
| `projectName` | `String` | - | Optional custom name for the new project (defaults to action title) |
| `parentProjectId` | `ID` | - | Optional parent project ID to nest the new project under |
| `deleteOriginalAction` | `Boolean` | false | Whether to delete the original action after conversion (default: false) |
| `applyTemplateId` | `ID` | - | Optional project template ID to apply to the new project |
| `sharingType` | `SharingTypes` | - | Project sharing type (me, custom, everyone) - defaults to 'me' |
| `members` | `[ID!]` | - | User IDs to add as project members (defaults to current user) |
| `teams` | `[ID!]` | - | Team IDs to give access to the project |
| `viewType` | `ActionViewType` | - | Default view type for the project - defaults to 'listView' |

## Signature

- `convertActionToProject(actionId: ID!, projectName: String, parentProjectId: ID, deleteOriginalAction: Boolean, applyTemplateId: ID, sharingType: SharingTypes, members: [ID!], teams: [ID!], viewType: ActionViewType)` -> `Project`

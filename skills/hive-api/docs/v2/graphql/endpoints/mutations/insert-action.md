# `insertAction`

- Type: `mutation`
- Returns: `Action`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Used to create new actions and subactions  Access: Requires user access as well as workspace ID and project ID access.  Errors: Throws error if user does not have access to workspace or project.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `ID` | - | ID of the action only to be used for optimistic insertions. This should not be used when creating a new action directly. |
| `title` | `String!` | - | Title of the action |
| `description` | `String` | - | Description of the action |
| `status` | `String` | - | Status of the action |
| `assignees` | `[ID!]` | [] | Assignees of the action |
| `placeholderAssignees` | `[ID!]` | [] | Placeholder assignees of the action |
| `teamAssignee` | `ID` | - | Team assignee of the action |
| `labels` | `[ID!]` | ["none"] | Labels for this action |
| `projectId` | `ID` | null | Project ID for this action |
| `phaseId` | `ID` | - | Phase ID for this action |
| `priorityLevelId` | `ID` | - | Priority level ID for this action |
| `deadline` | `Date` | - | Deadline for this action |
| `scheduledDate` | `Date` | - | Start date for this action |
| `newAction` | `Boolean` | - | - |
| `noteIds` | `[ID]` | - | - |
| `sectionIds` | `[ID!]` | - | Optional sectionIds for this action |
| `privacy` | `String` | - | - |
| `urgent` | `Boolean` | - | - |
| `parentId` | `ID` | null | Optional parent ID for this action if inserting as a subaction |
| `workspace` | `ID` | - | Workspace ID for this action |
| `actionViewId` | `ID` | - | Action view ID for this action |
| `isRisk` | `Boolean` | - | - |
| `estimates` | `[TimeTrackingEstimateItemInput!]` | - | Optional estimated time for this action |
| `insertOrder` | `InsertOrder` | - | Optional insert order for this action |
| `attachments` | `[ActionAttachmentInput!]` | [] | Optional attachments for this action |
| `rank` | `Float` | - | Optional rank for this action |
| `isAutomated` | `Boolean` | - | - |
| `preserveUTC` | `Boolean` | - | Optional flag to preserve UTC date |
| `type` | `ActionTypeEnum` | - | Optional flag to set risk and issue type |
| `timeCategoryId` | `ID` | - | Optional timeCategoryId for this action |
| `githubBranchNames` | `[String!]` | - | Optional githubBranchNames for this action |
| `gitlabBranchNames` | `[String!]` | - | Optional gitlabBranchNames for this action |
| `showInOtherProjects` | `[ID!]` | - | Optional showInOtherProjects for this action |

## Signature

- `insertAction(_id: ID, title: String!, description: String, status: String, assignees: [ID!], placeholderAssignees: [ID!], teamAssignee: ID, labels: [ID!], projectId: ID, phaseId: ID, priorityLevelId: ID, deadline: Date, scheduledDate: Date, newAction: Boolean, noteIds: [ID], sectionIds: [ID!], privacy: String, urgent: Boolean, parentId: ID, workspace: ID, actionViewId: ID, isRisk: Boolean, estimates: [TimeTrackingEstimateItemInput!], insertOrder: InsertOrder, attachments: [ActionAttachmentInput!], rank: Float, isAutomated: Boolean, preserveUTC: Boolean, type: ActionTypeEnum, timeCategoryId: ID, githubBranchNames: [String!], gitlabBranchNames: [String!], showInOtherProjects: [ID!])` -> `Action`

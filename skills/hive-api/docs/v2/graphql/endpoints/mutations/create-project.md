# `createProject`

- Type: `mutation`
- Returns: `Project`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Creates a new project in a workspace with comprehensive configuration options.  This is the primary mutation for project creation, supporting both basic project setup and advanced features like copying from existing projects, custom fields, etc.  Access: Requires user access to the workspace  Returns: The newly created Project object with all computed fields  Errors:    - Throws error if user doesn't have access to the workspace   - Throws error if copyFrom project doesn't exist or user lacks access   - Throws error if endDate is before startDate   - Throws error if members don't have workspace access

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspace` | `ID!` | - | The workspace ID where the project will be created |
| `name` | `String` | - | The name of the project |
| `archived` | `Boolean` | - | Whether the project should be archived |
| `actionDateSync` | `Boolean` | - | Whether action dates should sync with project dates |
| `attachments` | `[AttachmentObject!]` | - | File attachments to add to the project |
| `autoCompleteParent` | `Boolean` | - | Whether to auto-complete parent when all children complete |
| `automationWorkflows` | `[String!]` | - | Automation workflow IDs to apply |
| `color` | `String` | - | Hex color code for the project |
| `copyActionStatuses` | `Boolean` | - | Copy action statuses when copying from another project |
| `copyApprovals` | `Boolean` | - | Copy approval settings when copying from another project |
| `copyAssignees` | `Boolean` | - | Copy assignees when copying from another project |
| `copyAppWorkflows` | `Boolean` | - | Copy app workflows when copying from another project |
| `copyActionDates` | `Boolean` | - | Copy action dates when copying from another project |
| `copyProjectChildren` | `Boolean` | - | Copy child projects when copying from another project |
| `copyFrom` | `String` | - | Project ID to copy settings and structure from |
| `description` | `String` | - | Project description in HTML format |
| `startDate` | `Date` | - | Project start date |
| `endDate` | `Date` | - | Project end date |
| `ganttGroupBy` | `String` | - | How to group items in Gantt view |
| `hiddenApps` | `[String!]` | - | App names to hide for this project |
| `hideActionsForExternal` | `Boolean` | - | Whether the client mode is enabled |
| `hideActionsForExternalByDefault` | `Boolean` | - | Whether to hide actions from external users by default (when client mode is enabled) |
| `isDraftMode` | `Boolean` | - | Whether the project is in draft mode |
| `labels` | `[ID!]` | - | Label IDs to apply to the project |
| `members` | `[ID!]` | - | User IDs to add as project members |
| `parentProject` | `String` | - | Parent project ID if this is a sub-project |
| `destination` | `String` | - | Destination ID for project organization |
| `permissions` | `InputProjectPermissions` | - | Custom permission settings for the project |
| `phases` | `[PhaseInput!]` | - | Project phases to create |
| `pinActionView` | `Boolean` | - | Whether to pin the default action view |
| `resourcePlaceholderIds` | `[ID!]` | - | Resource placeholder IDs to assign |
| `sharingType` | `SharingTypes` | - | Project sharing type |
| `showKanbanViewSubactions` | `String` | - | How to display sub-actions in Kanban view |
| `showCompletedSubactionsByDefault` | `Boolean` | - | Whether to show completed sub-actions by default |
| `showRootActionCustomFields` | `Boolean` | - | Default sort type for project actions |
| `sortType` | `SortType` | - | - |
| `teams` | `[ID!]` | - | Team IDs to give access to the project |
| `viewType` | `String` | - | Default view type (list, kanban, gantt, etc.) |
| `template` | `Boolean` | - | Whether this project is a template |
| `copyUserPermissions` | `Boolean` | - | Copy user permissions when copying from another project |
| `customFieldsToCreate` | `[CustomFieldInput!]` | - | Custom field definitions to create for this project |
| `notifyProjectMembers` | `Boolean` | - | Whether to send notifications to project members |
| `projCustomFields` | `[CustomFieldItemInput!]` | - | Custom field values to set on the project |
| `isAutomated` | `Boolean` | - | Whether this project creation is automated |
| `ganttAutoScheduling` | `GanttAutoSchedulingEnum` | - | Auto-scheduling mode for Gantt view |
| `projectStatuses` | `[String!]` | - | Custom project status names |
| `harvestProjectId` | `String` | - | Harvest project ID to link for time tracking |

## Signature

- `createProject(workspace: ID!, name: String, archived: Boolean, actionDateSync: Boolean, attachments: [AttachmentObject!], autoCompleteParent: Boolean, automationWorkflows: [String!], color: String, copyActionStatuses: Boolean, copyApprovals: Boolean, copyAssignees: Boolean, copyAppWorkflows: Boolean, copyActionDates: Boolean, copyProjectChildren: Boolean, copyFrom: String, description: String, startDate: Date, endDate: Date, ganttGroupBy: String, hiddenApps: [String!], hideActionsForExternal: Boolean, hideActionsForExternalByDefault: Boolean, isDraftMode: Boolean, labels: [ID!], members: [ID!], parentProject: String, destination: String, permissions: InputProjectPermissions, phases: [PhaseInput!], pinActionView: Boolean, resourcePlaceholderIds: [ID!], sharingType: SharingTypes, showKanbanViewSubactions: String, showCompletedSubactionsByDefault: Boolean, showRootActionCustomFields: Boolean, sortType: SortType, teams: [ID!], viewType: String, template: Boolean, copyUserPermissions: Boolean, customFieldsToCreate: [CustomFieldInput!], notifyProjectMembers: Boolean, projCustomFields: [CustomFieldItemInput!], isAutomated: Boolean, ganttAutoScheduling: GanttAutoSchedulingEnum, projectStatuses: [String!], harvestProjectId: String)` -> `Project`

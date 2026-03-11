# `createForm`

- Type: `mutation`
- Returns: `Form!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

This mutation creates a new form with all its configuration and content. The form can be used to create actions, projects, or send emails based on the target field. Form should use different input elements for different types of data.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `_id` | `String` | - | Unique identifier for the form, optional one. |
| `workspace` | `String!` | - | The workspace ID this form belongs to. |
| `isDraft` | `Boolean` | false | Whether the form is a draft. Defaults to false. |
| `title` | `String!` | - | The form title that will be displayed to users |
| `externalTitle` | `String` | - | Optional external title for the form when shared externally |
| `externalLogo` | `String` | - | Optional external logo URL for the form when shared externally |
| `target` | `[FormTarget!]!` | - | Array of form targets that determine what happens on form submission. Must be one or more of: action, project, mapToProject, email, emailToSubmitter |
| `description` | `String` | - | Optional form description |
| `confirmMessage` | `String` | - | Optional confirmation message shown after form submission |
| `projectId` | `String` | - | Optional project ID this form is associated with |
| `parentActionId` | `String` | - | Optional parent action ID for creating sub-actions |
| `template` | `String` | - | Optional template ID to use for created actions |
| `projectTemplate` | `String` | - | Optional project template ID to use for created projects |
| `assignees` | `[String!]` | - | Array of user IDs to assign to created actions. Defaults to ['none'] |
| `projectOwner` | `String` | - | Optional project owner user ID |
| `members` | `[String!]!` | - | Array of member user IDs who can access this form. For AI Assistant: Include the current user's ID in this array if not provided. |
| `teams` | `[String!]` | [] | Array of team IDs who can access this form. Defaults to [] |
| `sharingType` | `String!` | - | Form sharing type ('me', 'custom', 'everyone'). - 'me': Only creator can access - 'custom': Specified members/teams can access - 'everyone': All workspace members can access |
| `jsonFormData` | `FormJSONDataInput!` | - | Form configuration and content data |
| `setFormNameToTitle` | `Boolean` | true | Whether to include form name in generated titles. Defaults to true |
| `setDateAndUserNameToTitle` | `Boolean` | true | Whether to include date and username in generated titles. Defaults to true |
| `setCardNumberToTitle` | `Boolean` | true | Whether to include card number in generated titles. Defaults to true |
| `setTemplateNameToTitle` | `Boolean` | false | Whether to include template name in generated titles. Defaults to false |
| `authRequired` | `Boolean` | false | Whether authentication is required to submit the form. Defaults to false |
| `allowProgressionTracking` | `Boolean` | false | Whether to allow tracking form submission progress. Defaults to false |
| `allowAccessToWhitelistedDomains` | `Boolean` | false | Whether to restrict form access to specific email domains. Defaults to false |
| `allowedEmailDomains` | `[String!]` | - | Array of allowed email domains when domain restriction is enabled |
| `onlyCreatorEditable` | `Boolean` | false | Whether only the form creator can edit it. Defaults to false |
| `mapToProjectId` | `String` | - | Optional project ID to map form data to |
| `actionsData` | `[ActionDataInput!]` | - | Array of action data configurations |
| `receivers` | `String` | - | Optional email receivers when form target includes 'email' |
| `emailDynamicFields` | `[String!]` | - | Array of dynamic field names to include in email |
| `archived` | `Boolean` | false | Whether the form is archived. Defaults to false |
| `shortcuttedAt` | `Date` | - | Optional date when the form was shortcutted |
| `draftFormId` | `String` | - | Optional ID of the draft version of this form |
| `publishedFormId` | `String` | - | Optional ID of the published version of this form |

## Signature

- `createForm(_id: String, workspace: String!, isDraft: Boolean, title: String!, externalTitle: String, externalLogo: String, target: [FormTarget!]!, description: String, confirmMessage: String, projectId: String, parentActionId: String, template: String, projectTemplate: String, assignees: [String!], projectOwner: String, members: [String!]!, teams: [String!], sharingType: String!, jsonFormData: FormJSONDataInput!, setFormNameToTitle: Boolean, setDateAndUserNameToTitle: Boolean, setCardNumberToTitle: Boolean, setTemplateNameToTitle: Boolean, authRequired: Boolean, allowProgressionTracking: Boolean, allowAccessToWhitelistedDomains: Boolean, allowedEmailDomains: [String!], onlyCreatorEditable: Boolean, mapToProjectId: String, actionsData: [ActionDataInput!], receivers: String, emailDynamicFields: [String!], archived: Boolean, shortcuttedAt: Date, draftFormId: String, publishedFormId: String)` -> `Form!`

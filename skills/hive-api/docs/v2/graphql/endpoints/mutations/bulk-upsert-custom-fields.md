# `bulkUpsertCustomFields`

- Type: `mutation`
- Returns: `CustomFieldUpsertResult`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Creates or updates multiple custom fields at once.    It can be used to upsert custom fields for a project or an action.  Parameters: - workspaceId: Required. The ID of the workspace to upsert custom fields for. - customFields: Required. An array of custom fields to upsert.  Examples: 1. Create a custom field (text type) for a project:  { "workspaceId": "TCB9NnnbcC4BEc2rF", "customFields": [     {         "allowMultiSelect": false,         "_id": "d6JfiYb34mMb5zNqL",         "label": "Test Project Field",         "dropdownValues": [],         "formula": null,         "type": "text",         "itemType": "project",         "onlyAdminEditable": false,         "jiraCustomFieldId": "",         "groupIds": []     }   ] }  2. Create a custom field (number type) for an action:  { "workspaceId": "TCB9NnnbcC4BEc2rF", "customFields": [     {         "allowMultiSelect": false,         "_id": "y7RCztztQ4D36GKk5",         "label": "asasas",         "dropdownValues": [],         "formula": "Test Action Field",         "type": "number",         "itemType": "action",         "onlyAdminEditable": false,         "jiraCustomFieldId": "",         "groupIds": []     }   ] }  When creating custom fields the _id field is generated server-side automatically, so you don't need to provide it. When updating custom fields you must provide old _id and new field data (old field data with new values).

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `workspaceId` | `ID!` | - | - |
| `customFields` | `[CustomFieldToInsertInput!]!` | - | - |

## Signature

- `bulkUpsertCustomFields(workspaceId: ID!, customFields: [CustomFieldToInsertInput!]!)` -> `CustomFieldUpsertResult`

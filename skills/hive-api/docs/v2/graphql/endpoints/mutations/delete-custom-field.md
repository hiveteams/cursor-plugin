# `deleteCustomField`

- Type: `mutation`
- Returns: `CustomField`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Permanently deletes a custom field from the workspace.  This mutation removes a custom field definition and optionally removes all existing values of this field from actions and projects. This is a destructive operation that cannot be undone.  Access: Requires workspace admin access  Returns: The deleted CustomField object (marked as deleted)  Errors:   - Throws error if user doesn't have workspace admin access   - Throws error if custom field doesn't exist   - Throws error if custom field is already deleted

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `customFieldId` | `ID!` | - | The ID of the custom field to delete |
| `shouldRemoveExistingValues` | `Boolean!` | - | Whether to remove existing field values from all actions/projects |

## Signature

- `deleteCustomField(customFieldId: ID!, shouldRemoveExistingValues: Boolean!)` -> `CustomField`

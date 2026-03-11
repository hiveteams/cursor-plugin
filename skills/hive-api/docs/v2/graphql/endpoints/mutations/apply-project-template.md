# `applyProjectTemplate`

- Type: `mutation`
- Returns: `Project`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Apply a project template to an existing project.  This mutation copies settings, structure, and configuration from a template project to a target project based on the importWith flags.  Access: Requires user access to both template and target projects  Returns: The updated target project

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `templateProjectId` | `ID!` | - | - |
| `targetProjectId` | `ID!` | - | - |
| `importWith` | `ApplyProjectTemplateImportWithInput` | - | - |
| `overrideLabels` | `Boolean` | false | - |

## Signature

- `applyProjectTemplate(templateProjectId: ID!, targetProjectId: ID!, importWith: ApplyProjectTemplateImportWithInput, overrideLabels: Boolean)` -> `Project`

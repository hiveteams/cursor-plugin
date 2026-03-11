# `getNote`

- Type: `query`
- Returns: `Note`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get a note by ID  Access: Requires user access to the note  Parameters:   - noteId: The ID of the note to retrieve  Returns: The requested note

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `noteId` | `ID!` | - | - |

## Signature

- `getNote(noteId: ID!)` -> `Note`

# Hive GraphQL API Reference

**Endpoint:** `https://prod-gql.hive.com/graphql`
**Playground:** [https://prod-gql.hive.com/graphql](https://prod-gql.hive.com/graphql)

## Authentication

Pass credentials as HTTP headers on every request:

```
api_key: YOUR_API_KEY
user_id: YOUR_USER_ID
```

## Testing Credentials

```graphql
query {
  getUser {
    userId
    email
  }
}
```

**cURL example:**

```bash
curl -X POST https://prod-gql.hive.com/graphql \
  -H "Content-Type: application/json" \
  -H "api_key: YOUR_API_KEY" \
  -H "user_id: YOUR_USER_ID" \
  -d '{"query": "{ getUser { userId email } }"}'
```

## Schema Exploration

The GraphQL Playground at `https://prod-gql.hive.com/graphql` provides full schema introspection. Use the **Docs** panel to browse all available queries, mutations, and types interactively.

You can also run an introspection query:

```graphql
{
  __schema {
    queryType { fields { name description } }
    mutationType { fields { name description } }
  }
}
```

## Known Queries

These queries are documented in the Hive GraphQL docs. Use the Playground to discover the full list and current field definitions.

| Query | Description | Key Args |
|-------|-------------|----------|
| `getUser` | Get authenticated user info | — |
| `actionComments` | Get comments on an action | `actionId!`, `first`, `after`, `sortField`, `sortOrder` |
| `approvalRounds` | Get approval rounds for an action | `actionId!`, `first`, `after` |
| `approvalStages` | Get approval stages | varies |

All paginated queries use cursor-based pagination with `first`, `after`, `last`, `before` arguments and return `*Connection` types with `edges` and `pageInfo`.

## Known Mutations

The API supports mutations for managing actions, projects, and other entities. Common patterns include:

- `insertAction` / `insertActions` — Create actions
- `updateActions` — Bulk update actions
- `bulkUpdateActionStatus` — Change status on multiple actions
- `bulkUpdateActionDescription` — Update descriptions

Use the Playground's schema explorer to see the full mutation list with exact argument types.

## Pagination Pattern

GraphQL queries use Relay-style cursor pagination:

```graphql
query {
  actionComments(actionId: "abc123", first: 10, after: "cursor") {
    edges {
      node {
        id
        body
        createdAt
      }
      cursor
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

## Important Notes

- The schema is actively evolving — new types, fields, and mutations may be added
- Avoid relying on undocumented fields or making strict schema assumptions
- All requests must be made over SSL
- For the most current schema, always use the Playground's introspection

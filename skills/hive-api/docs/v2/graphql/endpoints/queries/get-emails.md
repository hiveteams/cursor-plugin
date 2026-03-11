# `getEmails`

- Type: `query`
- Returns: `GetEmailsResponse!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Get emails from the user's mailbox with support for pagination. If there are more emails available beyond the current page, the response will include a "nextPageToken". To retrieve the next batch of results, call "getEmails" again using the same filters and pass the returned "nextPageToken".

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `from` | `[String!]` | - | The email address of the sender. |
| `to` | `[String!]` | - | The email address of the recipient. |
| `cc` | `[String!]` | - | The email address of the carbon copy recipient. |
| `bcc` | `[String!]` | - | The email address of the blind carbon copy recipient. |
| `subject` | `String` | - | The subject of the email. |
| `searchQuery` | `String` | - | Plain search string passed to the provider. Use this parameter only if you need to use a complex search query that cannot be expressed using the other parameters. IMPORTANT: This parameter is passed verbatim to Gmail. Prefer using the structured parameters (from, to, cc, bcc, subject) instead, as they automatically handle proper quoting for multi-word values. |
| `after` | `Date` | - | The date after which the email was sent. For Microsoft, if after is provided, before must be provided as well. |
| `before` | `Date` | - | The date before which the email was sent. For Microsoft, if before is provided, after must be provided as well. |
| `maxResults` | `Int` | 50 | The maximum number of emails to return. The default is 50. The maximum is 100. |
| `searchInboxOnly` | `Boolean` | false | If true, only emails in the inbox will be returned. |
| `searchSentOnly` | `Boolean` | false | If true, only emails in the sent folder will be returned. |
| `nextPageToken` | `String` | - | Pagination token returned in the previous "getEmails" response. Pass this token to retrieve the next page of results. If omitted, the first page will be returned. |

## Signature

- `getEmails(from: [String!], to: [String!], cc: [String!], bcc: [String!], subject: String, searchQuery: String, after: Date, before: Date, maxResults: Int, searchInboxOnly: Boolean, searchSentOnly: Boolean, nextPageToken: String)` -> `GetEmailsResponse!`

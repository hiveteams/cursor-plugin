# `salesforceOperation`

- Type: `mutation`
- Returns: `SalesforceOperationResult!`
- Deprecated: no
- Source endpoint: `https://prod-gql.hive.com/graphql`

## Description

Unified Salesforce operation using jsforce SOAP/REST API. Supports query, search, insert, update, upsert, merge, describe, and lead conversion.  Access: Requires an authenticated Hive user with a connected Salesforce account.  ## Operation Examples:  ### QUERY ```graphql salesforceOperation(input: {   operation: QUERY   query: "SELECT Id, Name FROM Account LIMIT 10" }) ```  ### INSERT ```graphql salesforceOperation(input: {   operation: INSERT   objectType: "Account"   fields: [{ fieldName: "Name", fieldValue: "Acme Corp" }] }) ```  ### UPDATE ```graphql salesforceOperation(input: {   operation: UPDATE   objectType: "Account"   recordId: "001XXXXXXXXXXXXXXX"   fields: [{ fieldName: "Description", fieldValue: "Updated description" }] }) ```  ### DELETE ```graphql salesforceOperation(input: {   operation: DELETE   objectType: "Opportunity"   recordId: "006XXXXXXXXXXXXXXX" }) ```  ### SEARCH (SOSL) ```graphql salesforceOperation(input: {   operation: SEARCH   search: "FIND {Acme*} IN ALL FIELDS RETURNING Account(Id, Name), Contact(Id, Name)" }) ```  ### MERGE ```graphql salesforceOperation(input: {   operation: MERGE   objectType: "Account"   masterRecordId: "001XXXXXXXXXXXXXXX"   recordIdsToMerge: ["001YYYYYYYYYYYYYYY"] }) ```  ### DESCRIBE ```graphql salesforceOperation(input: {   operation: DESCRIBE   objectType: "Account" }) ```  ### CONVERT_LEAD ```graphql salesforceOperation(input: {   operation: CONVERT_LEAD   leadId: "00QXXXXXXXXXXXXXXX"   convertedStatus: "Qualified"   doNotCreateOpportunity: false }) ```  Errors:   - User is not logged in.   - Salesforce account is not connected.   - Invalid operation parameters.   - Salesforce API errors.

## Arguments

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SalesforceOperationInput!` | - | - |

## Signature

- `salesforceOperation(input: SalesforceOperationInput!)` -> `SalesforceOperationResult!`

# Object

User Settings data structure

| Field          | Type   | Description                                          |
| :------------- | :----- | :--------------------------------------------------- |
| \_id           | String | Unique alphanumeric string id                        |
| userId         | String | User ID                                              |
| workspaceId    | String | Workspace ID                                         |
| firstDayOfWork | Date   | First day of work for the user                       |
| lastDayOfWork  | Date   | Last day of work for the user                        |
| billRate       | Number | Bill rate for the user                               |
| costRate       | Number | Cost rate for the user                               |
| managers       | Array  | Array of User IDs representing the User's manager(s) |
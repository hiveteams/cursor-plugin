# Object

Below is the data structure of the Resource Assignment object in Hive:

| Field            | Type            | Description                                                         |
| :--------------- | :-------------- | :------------------------------------------------------------------ |
| id               | String          | Unique alphanumeric string id                                       |
| workspace        | String          | Unique alphanumeric string id  of the workspace                     |
| resourceId       | String          | Unique alphanumeric string id  of the user or placeholder           |
| endDate          | ISO Date String | End date of the assignment                                          |
| startDate        | ISO Date String | Start date of the assignment                                        |
| allocationType   | String          | String for how the time is allocated (hours or days)                |
| assignmentType   | String          | The type of the assignment. Could be regular, timeOff or allocation |
| notes            | String          | Notes about assignment                                              |
| projectId        | String          | Unique alphanumeric string id  of the workspace                     |
| fixedHours       | Int             | Total hours across entire resourcing                                |
| fixedDisplayType | String          | Display type (hours or days)                                        |
| hoursPerDay      | Int             | Hours worked per day                                                |
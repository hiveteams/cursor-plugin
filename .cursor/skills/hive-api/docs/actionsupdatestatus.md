# Update action

Update the action

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "hive-rest-api",
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://app.hive.com/api/v1"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "in": "header",
        "name": "api_key"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/actions/{actionId}": {
      "put": {
        "summary": "Update action",
        "description": "Update the action",
        "operationId": "actionsupdatestatus",
        "parameters": [
          {
            "name": "actionId",
            "in": "path",
            "description": "The id of the action",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "status": {
                    "type": "string",
                    "description": "The new status of the action"
                  },
                  "update_children": {
                    "type": "boolean",
                    "description": "True if this action's children should also have their statuses updated",
                    "default": true
                  },
                  "title": {
                    "type": "string",
                    "description": "Set new action title"
                  },
                  "projectId": {
                    "type": "string",
                    "description": "Assign action to a specific project"
                  },
                  "assignees": {
                    "type": "array",
                    "description": "User IDs",
                    "default": [
                      "[]"
                    ],
                    "items": {
                      "type": "string"
                    }
                  },
                  "labels": {
                    "type": "array",
                    "description": "Set new Labels",
                    "items": {
                      "type": "string"
                    }
                  },
                  "description": {
                    "type": "string",
                    "description": "Overwrite the description of the Action. Supports basic HTML (h1, h2, a, b, u tags)."
                  },
                  "urgent": {
                    "type": "boolean",
                    "description": "Urgency state"
                  },
                  "privacy": {
                    "type": "string",
                    "description": "Set privacy value (allowed values: \"private\", \"public\")"
                  },
                  "checked": {
                    "type": "boolean",
                    "description": "Checked state"
                  },
                  "scheduledDate": {
                    "type": "string",
                    "description": "Set start date",
                    "format": "date"
                  },
                  "deadline": {
                    "type": "string",
                    "description": "Set end date",
                    "format": "date"
                  },
                  "parent": {
                    "type": "string",
                    "description": "Set new parent for action"
                  },
                  "customFields": {
                    "type": "array",
                    "description": "Add new or update an existing custom field. Work with 'text' custom fields only.",
                    "items": {
                      "properties": {
                        "label": {
                          "type": "string",
                          "description": "Label of the field"
                        },
                        "value": {
                          "type": "string",
                          "description": "Value of the field"
                        }
                      },
                      "type": "object"
                    }
                  },
                  "shiftSubactionsDeadline": {
                    "type": "boolean",
                    "description": "Shift subactions by same date update",
                    "default": false
                  },
                  "archived": {
                    "type": "boolean",
                    "description": "True if this action is to be archived",
                    "default": false
                  },
                  "phaseId": {
                    "type": "string",
                    "description": "ID of a project phase which will be assigned to the action. If both phaseId and phaseName are sent than phaseId will be used"
                  },
                  "phaseName": {
                    "type": "string",
                    "description": "Name of a project phase which will be assigned to the action. If both phaseId and phaseName are sent than phaseId will be used"
                  },
                  "followingUserIds": {
                    "type": "array",
                    "description": "Enter each userId to be included as an action card follower.",
                    "items": {
                      "type": "string"
                    }
                  },
                  "agileStoryPoints": {
                    "type": "integer",
                    "description": "Agile story points to assign to action. Max 233",
                    "format": "int32"
                  },
                  "agileSprintId": {
                    "type": "string",
                    "description": "Agile sprint id to map action to"
                  },
                  "milestone": {
                    "type": "boolean",
                    "description": "Set to true if this action is to be set as a milestone, or false if not."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"id\": \"1a2b3c4d5e6f7g8h9\",\n  \"title\": \"Action title\",\n  \"workspace\": \"fd8s97f9sd87f89s\",\n  \"assignees\": [],\n  \"projectId\": null,\n  \"customFields\": [\n    {\n      \"_id\": \"1a2b3c4d5e6f7g8gn\",\n      \"label\": \"customActionField\",\n      \"type\": \"text\",\n      \"rank\": 2.3843301617611736,\n      \"dropdownValues\": [],\n      \"allowMultiSelect\": false,\n      \"id\": \"XkvuQsZ6vrLoba8gN\",\n      \"value\": \"customFieldValue\",\n      \"dateValue\": null\n    }\n  ],\n  \"createdAt\": \"2018-07-27T17:10:49.687Z\",\n  \"modifiedAt\": \"2018-07-30T18:12:10.411Z\",\n  \"createdBy\": \"fds879a7fd8s9a\",\n  \"modifiedBy\": \"fds879a7fd8s9a\",\n  \"status\": \"In Progress\",\n  \"deadline\": null,\n  \"scheduledDate\": null,\n  \"checkedDate\": null,\n  \"parent\": null,\n  \"root\": null,\n  \"hasSubactions\": false,\n  \"estimate\": null,\n  \"loggedTime\": [\n    {\n      \"userId\":\"user12345\",\n      \"time\": 7200,\n      \"date\":\"2019-01-01T00:00:00.000Z\"\n    }\n  ],\n  \"archived\": false\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "example": "1a2b3c4d5e6f7g8h9"
                    },
                    "title": {
                      "type": "string",
                      "example": "Action title"
                    },
                    "workspace": {
                      "type": "string",
                      "example": "fd8s97f9sd87f89s"
                    },
                    "assignees": {
                      "type": "array"
                    },
                    "projectId": {},
                    "customFields": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "_id": {
                            "type": "string",
                            "example": "1a2b3c4d5e6f7g8gn"
                          },
                          "label": {
                            "type": "string",
                            "example": "customActionField"
                          },
                          "type": {
                            "type": "string",
                            "example": "text"
                          },
                          "rank": {
                            "type": "number",
                            "example": 2.3843301617611736,
                            "default": 0
                          },
                          "dropdownValues": {
                            "type": "array"
                          },
                          "allowMultiSelect": {
                            "type": "boolean",
                            "example": false,
                            "default": true
                          },
                          "id": {
                            "type": "string",
                            "example": "XkvuQsZ6vrLoba8gN"
                          },
                          "value": {
                            "type": "string",
                            "example": "customFieldValue"
                          },
                          "dateValue": {}
                        }
                      }
                    },
                    "createdAt": {
                      "type": "string",
                      "example": "2018-07-27T17:10:49.687Z"
                    },
                    "modifiedAt": {
                      "type": "string",
                      "example": "2018-07-30T18:12:10.411Z"
                    },
                    "createdBy": {
                      "type": "string",
                      "example": "fds879a7fd8s9a"
                    },
                    "modifiedBy": {
                      "type": "string",
                      "example": "fds879a7fd8s9a"
                    },
                    "status": {
                      "type": "string",
                      "example": "In Progress"
                    },
                    "deadline": {},
                    "scheduledDate": {},
                    "checkedDate": {},
                    "parent": {},
                    "root": {},
                    "hasSubactions": {
                      "type": "boolean",
                      "example": false,
                      "default": true
                    },
                    "estimate": {},
                    "loggedTime": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "userId": {
                            "type": "string",
                            "example": "user12345"
                          },
                          "time": {
                            "type": "integer",
                            "example": 7200,
                            "default": 0
                          },
                          "date": {
                            "type": "string",
                            "example": "2019-01-01T00:00:00.000Z"
                          }
                        }
                      }
                    },
                    "archived": {
                      "type": "boolean",
                      "example": false,
                      "default": true
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false,
        "x-readme": {
          "code-samples": [
            {
              "language": "javascript",
              "code": "var userId = \"USER_ID\";\nvar actionId = \"ACTION_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"actions/\" + actionId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  status: \"In Progress\",\n  customFields: [{ label: \"customActionField\", value: \"customFieldValue\" }]\n};\n\n$.ajax({\n  method: \"PUT\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
            }
          ],
          "samples-languages": [
            "javascript"
          ]
        }
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true
}
```
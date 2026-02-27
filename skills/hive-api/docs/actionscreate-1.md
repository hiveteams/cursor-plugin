# Create action

Create a new action.

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
    "/actions/create": {
      "post": {
        "summary": "Create action",
        "description": "Create a new action.",
        "operationId": "actionscreate-1",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "workspace": {
                    "type": "string",
                    "description": "ID of the workspace"
                  },
                  "title": {
                    "type": "string",
                    "description": "Title of the action"
                  },
                  "description": {
                    "type": "string",
                    "description": "Description of the action"
                  },
                  "projectId": {
                    "type": "string",
                    "description": "Assign action to a specific project"
                  },
                  "assignees": {
                    "type": "array",
                    "description": "User Ids of action assignees; if value isn't passed the action will be assigned to the user Id of the request",
                    "items": {
                      "type": "string"
                    }
                  },
                  "labels": {
                    "type": "array",
                    "description": "Set Labels (Label IDs) for the Action",
                    "items": {
                      "type": "string"
                    }
                  },
                  "deadline": {
                    "type": "string",
                    "description": "Date string to set the deadline (date format: yyyy/mm/dd)"
                  },
                  "scheduledDate": {
                    "type": "string",
                    "description": "Date string to set the deadline (date format: yyyy/mm/dd)",
                    "default": "Date string to set the start date"
                  },
                  "processId": {
                    "type": "string",
                    "description": "Pass action template id to apply an action template"
                  },
                  "customFields": {
                    "type": "array",
                    "description": "Add custom fields to the action: Each object must contain label (string) and value (string)",
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
                  "parentId": {
                    "type": "string",
                    "description": "ID of an Action to set as the parent for your new Action"
                  },
                  "phaseId": {
                    "type": "string",
                    "description": "ID of a project phase which will be assigned to the created action. If both phaseId and phaseName are sent than phaseId will be used"
                  },
                  "phaseName": {
                    "type": "string",
                    "description": "Name of a project phase which will be assigned to the created action. If both phaseId and phaseName are sent than phaseId will be used"
                  },
                  "milestone": {
                    "type": "boolean",
                    "description": "Whether the Action is a milestone or not"
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
                    "value": "{\n  \"id\": \"qFR6a524nFARukmvF\",\n  \"title\": \"This is my action\",\n  \"workspace\": \"12345aZjDQZndHqs\",\n  \"assignees\": [],\n  \"projectId\": null,\n  \"customFields\": [],\n  \"createdAt\": \"2018-01-23T21:41:40.295Z\",\n  \"modifiedAt\": \"2018-01-23T21:41:40.289Z\",\n  \"createdBy\": \"12345gfuJzo4k7F9\",\n  \"modifiedBy\": \"12345gfuJzo4k7F9\",\n  \"status\": \"Unstarted\",\n  \"deadline\": null,\n  \"scheduledDate\": null,\n  \"checkedDate\": null,\n  \"parent\": null,\n  \"root\": null,\n  \"hasSubactions\": false,\n  \"estimate\": null,\n  \"loggedTime\": []\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "example": "qFR6a524nFARukmvF"
                    },
                    "title": {
                      "type": "string",
                      "example": "This is my action"
                    },
                    "workspace": {
                      "type": "string",
                      "example": "12345aZjDQZndHqs"
                    },
                    "assignees": {
                      "type": "array"
                    },
                    "projectId": {},
                    "customFields": {
                      "type": "array"
                    },
                    "createdAt": {
                      "type": "string",
                      "example": "2018-01-23T21:41:40.295Z"
                    },
                    "modifiedAt": {
                      "type": "string",
                      "example": "2018-01-23T21:41:40.289Z"
                    },
                    "createdBy": {
                      "type": "string",
                      "example": "12345gfuJzo4k7F9"
                    },
                    "modifiedBy": {
                      "type": "string",
                      "example": "12345gfuJzo4k7F9"
                    },
                    "status": {
                      "type": "string",
                      "example": "Unstarted"
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
                      "type": "array"
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"actions/create\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  workspace: workspaceId,\n  title: \"Test action title\",\n  assigned_to: userId,\n  when: \"today\"\n};\n\n$.ajax({\n  method: \"POST\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
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
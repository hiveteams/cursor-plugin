# Create project

Create a new project

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
    "/projects": {
      "post": {
        "summary": "Create project",
        "description": "Create a new project",
        "operationId": "projects-1",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "workspace",
                  "name"
                ],
                "properties": {
                  "workspace": {
                    "type": "string",
                    "description": "ID of the workspace for the project to be created in"
                  },
                  "name": {
                    "type": "string",
                    "description": "Name of the project"
                  },
                  "description": {
                    "type": "string",
                    "description": "Project description"
                  },
                  "startDate": {
                    "type": "string",
                    "description": "Start date of the Project",
                    "format": "date"
                  },
                  "endDate": {
                    "type": "string",
                    "description": "End date of the Project",
                    "format": "date"
                  },
                  "sharingType": {
                    "type": "string",
                    "description": "Sharing type of the project (one of \"everyone\", \"custom\" or \"me\")",
                    "default": "everyone"
                  },
                  "members": {
                    "type": "array",
                    "description": "Array of User IDs to set as members of the project. Only relevant if \"sharingType\" is set to \"custom\"",
                    "default": [
                      "[]"
                    ],
                    "items": {
                      "type": "string"
                    }
                  },
                  "teams": {
                    "type": "array",
                    "description": "Array of Team IDs to set as members of the project. Only relevant if \"sharingType\" is set to \"custom\"",
                    "items": {
                      "type": "string"
                    }
                  },
                  "projectCustomFields": {
                    "type": "array",
                    "description": "Custom fields stored on the project-level",
                    "items": {
                      "properties": {
                        "label": {
                          "type": "string",
                          "description": "Human readable label for the custom field"
                        },
                        "_id": {
                          "type": "string",
                          "description": "Unique string ID"
                        },
                        "type": {
                          "type": "string",
                          "description": "Type of the custom field. One of the following is allowed: text, number, date, user, project, select, formula."
                        },
                        "value": {
                          "type": "string",
                          "description": "Value of the \"text\" custom field."
                        },
                        "numberValue": {
                          "type": "integer",
                          "description": "Value of the \"number\" custom field.",
                          "format": "int32"
                        },
                        "dateValue": {
                          "type": "string",
                          "description": "Value of the \"date\" custom field. ISO 8601 string."
                        },
                        "formula": {
                          "type": "string",
                          "description": "Value of the \"formula\" custom field."
                        },
                        "dropdownValues": {
                          "type": "array",
                          "description": "Value of the \"select\" custom field. Leave empty for \"user\" and \"project\" type.",
                          "default": [],
                          "items": {
                            "type": "string"
                          }
                        },
                        "selectedValues": {
                          "type": "array",
                          "description": "Selected value of the \"select\", \"user\" or \"project\" custom field.",
                          "default": [],
                          "items": {
                            "type": "string"
                          }
                        },
                        "allowMultiSelect": {
                          "type": "boolean",
                          "description": "Whether or not \"selectedValues\" can hold multiple values",
                          "default": false
                        }
                      },
                      "required": [
                        "label"
                      ],
                      "type": "object"
                    }
                  },
                  "color": {
                    "type": "string",
                    "description": "Optional hex code for project color"
                  },
                  "template": {
                    "type": "boolean",
                    "description": "Pass \"true\" if you want create project as template",
                    "default": false
                  },
                  "copyFrom": {
                    "type": "string",
                    "description": "ID of the project to make a copy from"
                  },
                  "copyActionStatuses": {
                    "type": "boolean",
                    "description": "Retaining action statuses when copying project. Works only if 'copyFrom' specified",
                    "default": false
                  },
                  "copyAssignees": {
                    "type": "boolean",
                    "description": "Retaining action assignees when copying project. Works only if 'copyFrom' specified",
                    "default": false
                  },
                  "accessOption": {
                    "type": "string",
                    "description": "Sets the project access to either private or public",
                    "default": "private"
                  },
                  "phases": {
                    "type": "array",
                    "description": "Creates phases for the project",
                    "items": {
                      "type": "string"
                    }
                  },
                  "parentProject": {
                    "type": "string",
                    "default": "Id of parentProject"
                  },
                  "budget": {
                    "type": "integer",
                    "description": "Budget value for the Project",
                    "default": 0,
                    "format": "int32"
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
                    "value": "{\n  \"message\": \"Project was created successfully\",\n  \"project\": {\n    \"id\": \"123ABC567XYZ\",\n    \"name\": \"Mobile app development\",\n    \"workspace\": \"workspace_id_123\",\n    \"description\": \"A project for tracking our shiny new mobile app.\",\n    \"startDate\": \"2019-04-01T00:00:00.000Z\",\n    \"endDate\": \"2019-04-01T00:00:00.000Z\",\n    \"accessOption\": \"public\",\n    \"sharingType\": \"custom\",\n    \"members\": [\"123ABC456XYZ\"],\n    \"template\": false,\n    \"createdAt\": \"2017-05-18T15:26:17.407Z\",\n    \"modifiedAt\": \"2017-05-19T02:25:06.190Z\",\n    \"createdBy\": \"1234abcuJzo4k7F9\",\n    \"modifiedBy\": \"1234abcuJzo4k7F9\",\n    \"projectCustomFields\": [\n      {\n        \"label\": \"Design link\",\n        \"value\": \"https://invision.com/designs\",\n        \"dropdownValues\": [],\n        \"selectedValues\": [],\n        \"type\": \"text\",\n        \"_id\": \"NTuqNWyPBxAFGAk9Y\",\n        \"hidden\": false\n      },\n      {\n        \"label\": \"Project lead\",\n        \"value\": \"George Boole\",\n        \"dropdownValues\": [],\n        \"selectedValues\": [],\n        \"type\": \"text\",\n        \"_id\": \"SsjSn54vk9Z5XXCA4\",\n        \"hidden\": false\n      }\n    ],\n    \"color\": \"#F2F2F2\",\n    \"parentProject\": null,\n    \"phases\": [],\n    \"resourcePlaceholderIds\": []\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "Project was created successfully"
                    },
                    "project": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string",
                          "example": "123ABC567XYZ"
                        },
                        "name": {
                          "type": "string",
                          "example": "Mobile app development"
                        },
                        "workspace": {
                          "type": "string",
                          "example": "workspace_id_123"
                        },
                        "description": {
                          "type": "string",
                          "example": "A project for tracking our shiny new mobile app."
                        },
                        "startDate": {
                          "type": "string",
                          "example": "2019-04-01T00:00:00.000Z"
                        },
                        "endDate": {
                          "type": "string",
                          "example": "2019-04-01T00:00:00.000Z"
                        },
                        "accessOption": {
                          "type": "string",
                          "example": "public"
                        },
                        "sharingType": {
                          "type": "string",
                          "example": "custom"
                        },
                        "members": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "123ABC456XYZ"
                          }
                        },
                        "template": {
                          "type": "boolean",
                          "example": false,
                          "default": true
                        },
                        "createdAt": {
                          "type": "string",
                          "example": "2017-05-18T15:26:17.407Z"
                        },
                        "modifiedAt": {
                          "type": "string",
                          "example": "2017-05-19T02:25:06.190Z"
                        },
                        "createdBy": {
                          "type": "string",
                          "example": "1234abcuJzo4k7F9"
                        },
                        "modifiedBy": {
                          "type": "string",
                          "example": "1234abcuJzo4k7F9"
                        },
                        "projectCustomFields": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "label": {
                                "type": "string",
                                "example": "Design link"
                              },
                              "value": {
                                "type": "string",
                                "example": "https://invision.com/designs"
                              },
                              "dropdownValues": {
                                "type": "array"
                              },
                              "selectedValues": {
                                "type": "array"
                              },
                              "type": {
                                "type": "string",
                                "example": "text"
                              },
                              "_id": {
                                "type": "string",
                                "example": "NTuqNWyPBxAFGAk9Y"
                              },
                              "hidden": {
                                "type": "boolean",
                                "example": false,
                                "default": true
                              }
                            }
                          }
                        },
                        "color": {
                          "type": "string",
                          "example": "#F2F2F2"
                        },
                        "parentProject": {},
                        "phases": {
                          "type": "array"
                        },
                        "resourcePlaceholderIds": {
                          "type": "array"
                        }
                      }
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar teamId = \"TEAM_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"projects/\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  name: \"Test project name\",\n  workspace: workspaceId,\n  description: \"Test project description\",\n  startDate: new Date(),\n  endDate: new Date(),\n  accessOption: \"public\",\n  sharingType: \"custom\",\n  members: [userId],\n  teams: [teamId],\n  projectCustomFields: [\n    { label: \"Project lead\", value: \"George Boole\" },\n    { label: \"Design link\", value: \"https://invision.com/designs\" }\n  ],\n  color: \"#F2F2F2\",\n  template: false\n};\n\n$.ajax({\n  method: \"POST\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});\n\n"
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
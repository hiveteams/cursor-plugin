# Update project

Update a project by id

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
    "/projects/{projectId}": {
      "put": {
        "summary": "Update project",
        "description": "Update a project by id",
        "operationId": "projectsprojectid-1",
        "parameters": [
          {
            "name": "projectId",
            "in": "path",
            "description": "ID of the project to update",
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
                  "name": {
                    "type": "string",
                    "description": "Project name"
                  },
                  "description": {
                    "type": "string",
                    "description": "Project description"
                  },
                  "startDate": {
                    "type": "string",
                    "description": "Start date of the Project. Pass null value to unset",
                    "format": "date"
                  },
                  "endDate": {
                    "type": "string",
                    "description": "End date of the Project. Pass null value to unset",
                    "format": "date"
                  },
                  "color": {
                    "type": "string",
                    "description": "Optional hex code for project color"
                  },
                  "accessOption": {
                    "type": "string",
                    "description": "Project access permissions. Either public or private"
                  },
                  "parentProject": {
                    "type": "string",
                    "default": "Id of parent project"
                  },
                  "sharingType": {
                    "type": "string",
                    "description": "Sharing type of the project (one of \"everyone\", \"custom\" or \"me\")"
                  },
                  "members": {
                    "type": "array",
                    "description": "Array of User IDs to set as members of the project.",
                    "items": {
                      "type": "string"
                    }
                  },
                  "teams": {
                    "type": "array",
                    "description": "Array of Team IDs to set as members of the project.",
                    "items": {
                      "type": "string"
                    }
                  },
                  "archived": {
                    "type": "boolean",
                    "default": false
                  },
                  "template": {
                    "type": "array",
                    "description": "template could be a string - ID of template to apply. Array of IDs. Object - object with settings for template appliance. Array of objects with settings for template appliance",
                    "items": {
                      "properties": {
                        "templateId": {
                          "type": "string",
                          "description": "ID of template to apply"
                        },
                        "importWith": {
                          "type": "object",
                          "properties": {
                            "projectCustomFields": {
                              "type": "boolean",
                              "default": false
                            },
                            "includeWeekends": {
                              "type": "boolean",
                              "default": false
                            },
                            "customFields": {
                              "type": "boolean",
                              "default": false
                            },
                            "ganttGroupBy": {
                              "type": "boolean",
                              "default": false
                            },
                            "description": {
                              "type": "boolean",
                              "default": false
                            },
                            "attachments": {
                              "type": "boolean",
                              "default": false
                            },
                            "permissions": {
                              "type": "boolean",
                              "default": false
                            },
                            "assignees": {
                              "type": "boolean",
                              "default": false
                            },
                            "deadline": {
                              "type": "boolean",
                              "default": false
                            },
                            "statuses": {
                              "type": "boolean",
                              "default": false
                            },
                            "sortType": {
                              "type": "boolean",
                              "default": false
                            },
                            "viewType": {
                              "type": "boolean",
                              "default": false
                            },
                            "labels": {
                              "type": "boolean",
                              "default": false
                            },
                            "actionDateSync": {
                              "type": "boolean",
                              "default": false
                            },
                            "ganttAutoScheduling": {
                              "type": "boolean",
                              "default": false
                            },
                            "automationWorkflows": {
                              "type": "boolean",
                              "default": false
                            },
                            "approvals": {
                              "type": "boolean",
                              "default": false
                            },
                            "projectPermissions": {
                              "type": "boolean",
                              "default": false
                            },
                            "advancedSettings": {
                              "type": "boolean",
                              "description": "Controls whether advanced settings is imported",
                              "default": false
                            }
                          }
                        },
                        "template": {
                          "type": "boolean",
                          "description": "true - means that it is a project template. false -  common project",
                          "default": false
                        },
                        "projectPeopleIds": {
                          "type": "array",
                          "default": [],
                          "items": {
                            "type": "string"
                          }
                        },
                        "overrideLabels": {
                          "type": "boolean",
                          "default": false
                        },
                        "shouldRemoveFromParentProjectIfNoParent": {
                          "type": "boolean",
                          "default": true
                        }
                      },
                      "type": "object"
                    }
                  },
                  "budget": {
                    "type": "integer",
                    "description": "Budget value for the Project",
                    "format": "int32"
                  },
                  "isDraftMode": {
                    "type": "boolean",
                    "description": "Boolean value representing whether a project is in Draft Mode state or not. Pass boolean value to update Draft Mode state of the project."
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
                    "value": "{\n  \"message\": \"Project was updated successfully\",\n  \"project\": {\n    \"id\": \"123ABC567XYZ\",\n    \"name\": \"New project name\",\n    \"description\": \"A new project description right here!\",\n    \"startDate\": \"2019-04-01T00:00:00.000Z\",\n\t\t\"endDate\": \"2019-04-01T00:00:00.000Z\",\n    \"accessOption\": \"public\",\n    \"sharingType\": \"everyone\",\n    \"members\": [],\n    \"template\": false,\n    \"createdAt\": \"2019-12-20T19:41:13.283Z\",\n    \"modifiedAt\": \"2020-01-04T23:53:41.413Z\",\n    \"createdBy\": \"1234abcuJzo4k7F9\",\n    \"modifiedBy\": \"1234abcuJzo4k7F9\",\n    \"projectCustomFields\": [\n      {\n        \"label\": \"Budget\",\n        \"value\": \"$5000000\",\n        \"dropdownValues\": [],\n        \"selectedValues\": [],\n        \"type\": \"text\",\n        \"_id\": \"1234abcuJzo4k7E1\",\n        \"hidden\": false\n      }\n    ],\n    \"color\": \"#F2F2F2\",\n    \"parentProject\": \"parent123\",\n    \"phases\": [],\n    \"resourcePlaceholderIds\": []\n  }\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "Project was updated successfully"
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
                          "example": "New project name"
                        },
                        "description": {
                          "type": "string",
                          "example": "A new project description right here!"
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
                          "example": "everyone"
                        },
                        "members": {
                          "type": "array"
                        },
                        "template": {
                          "type": "boolean",
                          "example": false,
                          "default": true
                        },
                        "createdAt": {
                          "type": "string",
                          "example": "2019-12-20T19:41:13.283Z"
                        },
                        "modifiedAt": {
                          "type": "string",
                          "example": "2020-01-04T23:53:41.413Z"
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
                                "example": "Budget"
                              },
                              "value": {
                                "type": "string",
                                "example": "$5000000"
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
                                "example": "1234abcuJzo4k7E1"
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
                        "parentProject": {
                          "type": "string",
                          "example": "parent123"
                        },
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
              "code": "var userId = \"USER_ID\";\nvar projectId = \"PROJECT_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"projects/\" + projectId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  name: \"New project name\",\n  description: \"A new project description right here!\",\n  color: \"#F2F2F2\",\n  parentProject: \"parent123\",\n  },\n};\n\n$.ajax({\n  method: \"PUT\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
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
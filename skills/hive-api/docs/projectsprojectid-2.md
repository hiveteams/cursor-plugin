# Get project

Get a project by id

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
      "get": {
        "summary": "Get project",
        "description": "Get a project by id",
        "operationId": "projectsprojectid-2",
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
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"project\": {\n    \"id\": \"123ABC567XYZ\",\n    \"name\": \"New project name\",\n    \"description\": \"\",\n    \"startDate\": null,\n    \"endDate\": null,\n    \"accessOption\": \"private\",\n    \"sharingType\": \"me\",\n    \"members\": [],\n    \"template\": false,\n    \"createdAt\": \"2017-05-18T15:26:17.407Z\",\n    \"modifiedAt\": \"2017-05-19T02:25:06.190Z\",\n    \"createdBy\": \"1234abcuJzo4k7F9\",\n    \"modifiedBy\": \"1234abcuJzo4k7F9\",\n    \"projectCustomFields\": [\n      {\n        \"label\": \"Budget\",\n        \"value\": \"$5000000\",\n        \"dropdownValues\": [],\n        \"selectedValues\": [],\n        \"type\": \"text\",\n        \"_id\": \"1234abcuJzo4k7E1\",\n        \"hidden\": false\n      }\n    ],\n    \"color\": \"#3fcaca\",\n    \"parentProject\": null,\n    \"phases\": [],\n    \"budget\":0,\n    \"resourcePlaceholderIds\": []\n  }\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
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
                          "example": ""
                        },
                        "startDate": {},
                        "endDate": {},
                        "accessOption": {
                          "type": "string",
                          "example": "private"
                        },
                        "sharingType": {
                          "type": "string",
                          "example": "me"
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
                          "example": "#3fcaca"
                        },
                        "parentProject": {},
                        "phases": {
                          "type": "array"
                        },
                        "budget": {
                          "type": "integer",
                          "example": 0,
                          "default": 0
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
              "code": "var userId = \"USER_ID\";\nvar projectId = \"PROJECT_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"projects/\" + projectId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url\n}).done(function(data) {\n  console.log(data);\n});"
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
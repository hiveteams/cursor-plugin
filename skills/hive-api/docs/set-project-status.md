# Set project status

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
    "/projects/{projectId}/project-status": {
      "post": {
        "summary": "Set project status",
        "description": "",
        "operationId": "set-project-status",
        "parameters": [
          {
            "name": "projectId",
            "in": "path",
            "description": "ID of the project",
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
                "required": [
                  "statusId"
                ],
                "properties": {
                  "statusId": {
                    "type": "string",
                    "description": "Id of the existing project status"
                  },
                  "description": {
                    "type": "string",
                    "description": "Project status description"
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
                    "value": "{\n  \"_id\": \"PROJECT_ID\",\n  \"statusUpdates\": {\n    \"_id\": \"Unique status Id in the list\",\n    \"statusId\": \"Some status Id\",\n    \"description\": \"Status description\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string",
                      "example": "PROJECT_ID"
                    },
                    "statusUpdates": {
                      "type": "object",
                      "properties": {
                        "_id": {
                          "type": "string",
                          "example": "Unique status Id in the list"
                        },
                        "statusId": {
                          "type": "string",
                          "example": "Some status Id"
                        },
                        "description": {
                          "type": "string",
                          "example": "Status description"
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
              "code": "var userId = \"USER_ID\";\nvar projectId = \"PROJECT_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"projects/\" + projectId + \"/project-status\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  statusId: \"Some status Id\",\n  description: \"Status description\",\n};\n\n$.ajax({\n  method: \"POST\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
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
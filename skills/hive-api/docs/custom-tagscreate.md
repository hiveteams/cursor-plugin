# Create custom tag

Create a new custom tag

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
    "/workspaces/{workspaceId}/custom-tags": {
      "post": {
        "summary": "Create custom tag",
        "description": "Create a new custom tag",
        "operationId": "custom-tagscreate",
        "parameters": [
          {
            "name": "workspaceId",
            "in": "path",
            "description": "Workspace ID",
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
                  "name",
                  "type"
                ],
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Name of the custom tag"
                  },
                  "type": {
                    "type": "string",
                    "description": "Type of the custom tag, can be \"user\" or \"project\""
                  },
                  "options": {
                    "type": "array",
                    "description": "Array of options that are available for this custom tag",
                    "default": [
                      "[]"
                    ],
                    "items": {
                      "type": "string"
                    }
                  },
                  "isMulti": {
                    "type": "boolean",
                    "description": "Whether or not this custom tag can be multi select",
                    "default": false
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
                    "value": "{\n  \"_id\": \"qFR6a524nFARukmvF\",\n  \"name\": \"Test custom tag\",\n  \"type\": \"user\",\n  \"isMulti\": false,\n  \"options\": [\"Option 1\", \"Option 2\"],\n  \"createdAt\": \"2020-01-05T16:41:59.527Z\",\n  \"createdBy\": \"12345xgfuJzo4k7F9\",\n  \"modifiedAt\": \"2020-01-05T16:41:59.527Z\",\n  \"modifiedBy\": \"12345xgfuJzo4k7F9\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string",
                      "example": "qFR6a524nFARukmvF"
                    },
                    "name": {
                      "type": "string",
                      "example": "Test custom tag"
                    },
                    "type": {
                      "type": "string",
                      "example": "user"
                    },
                    "isMulti": {
                      "type": "boolean",
                      "example": false,
                      "default": true
                    },
                    "options": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "example": "Option 1"
                      }
                    },
                    "createdAt": {
                      "type": "string",
                      "example": "2020-01-05T16:41:59.527Z"
                    },
                    "createdBy": {
                      "type": "string",
                      "example": "12345xgfuJzo4k7F9"
                    },
                    "modifiedAt": {
                      "type": "string",
                      "example": "2020-01-05T16:41:59.527Z"
                    },
                    "modifiedBy": {
                      "type": "string",
                      "example": "12345xgfuJzo4k7F9"
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"workspaces/\" + workspaceId + \"/custom-tags\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  workspace: workspaceId,\n  name: \"Test custom tag\",\n  type: \"user\",\n  options: [\"Option 1\", \"Option 2\"],\n  isMulti: false\n};\n\n$.ajax({\n  method: \"POST\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
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
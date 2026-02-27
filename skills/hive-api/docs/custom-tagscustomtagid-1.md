# Get custom tag

Get a custom tag by id

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
    "/workspaces/{workspaceId}/custom-tags/{customTagId}": {
      "get": {
        "summary": "Get custom tag",
        "description": "Get a custom tag by id",
        "operationId": "custom-tagscustomtagid-1",
        "parameters": [
          {
            "name": "workspaceId",
            "in": "path",
            "description": "Workspace ID",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "customTagId",
            "in": "path",
            "description": "Tag ID",
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar customTagId = \"CUSTOM_TAG_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"workspaces/\" + workspaceId + \"/custom-tags/\" + customTagId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url\n}).done(function(data) {\n  console.log(data);\n});"
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
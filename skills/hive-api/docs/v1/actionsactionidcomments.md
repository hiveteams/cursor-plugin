# Get action comments

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
    "/actions/{actionId}/comments": {
      "get": {
        "summary": "Get action comments",
        "description": "",
        "operationId": "actionsactionidcomments",
        "parameters": [
          {
            "name": "actionId",
            "in": "path",
            "description": "The id of the action",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Number of comments",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 200
            }
          },
          {
            "name": "sortBy",
            "in": "query",
            "description": "You can change to e.g. createdAt asc",
            "schema": {
              "type": "string",
              "default": "createdAt+desc"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[\n  {\n    \"id\": \"232b3c4d5e6f7g8h1\",\n    \"attachments\": [],\n    \"workspace\": \"w32bac4d5e6f7g8h2\",\n    \"body\": \"comment body\",\n    \"mentions\": [],\n    \"createdBy\": \"u32bac4d5e6f7g8h2\",\n    \"createdAt\": \"2020-01-04T23:30:54.816Z\",\n    \"reactions\": []\n  }\n]\n"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "string",
                        "example": "232b3c4d5e6f7g8h1"
                      },
                      "attachments": {
                        "type": "array"
                      },
                      "workspace": {
                        "type": "string",
                        "example": "w32bac4d5e6f7g8h2"
                      },
                      "body": {
                        "type": "string",
                        "example": "comment body"
                      },
                      "mentions": {
                        "type": "array"
                      },
                      "createdBy": {
                        "type": "string",
                        "example": "u32bac4d5e6f7g8h2"
                      },
                      "createdAt": {
                        "type": "string",
                        "example": "2020-01-04T23:30:54.816Z"
                      },
                      "reactions": {
                        "type": "array"
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
              "code": "var userId = \"USER_ID\";\nvar actionId = \"ACTION_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"/actions/\" + actionId + '/comments';\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url,\n}).done(function(data) {\n  console.log(data);\n});\n"
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
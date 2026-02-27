# Create action comment

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
      "post": {
        "summary": "Create action comment",
        "description": "",
        "operationId": "actionsactionidcomments-1",
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
                  "body": {
                    "type": "string",
                    "description": "Number of comments"
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
                    "value": "{\n  \"message\": \"Action comment successfully inserted\",\n  \"comment\": {\n    \"id\": \"232b3c4d5e6f7g8h1\",\n    \"body\": \"comment body\",\n    \"workspace\": \"w32bac4d5e6f7g8h2\",\n    \"createdAt\": \"2019-01-01T00:00:00.000Z\",\n    \"createdBy\": \"u32bac4d5e6f7g8h2\",\n    \"attachments\": [],\n    \"reactions\": [],\n    \"mentions\": []\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "Action comment successfully inserted"
                    },
                    "comment": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string",
                          "example": "232b3c4d5e6f7g8h1"
                        },
                        "body": {
                          "type": "string",
                          "example": "comment body"
                        },
                        "workspace": {
                          "type": "string",
                          "example": "w32bac4d5e6f7g8h2"
                        },
                        "createdAt": {
                          "type": "string",
                          "example": "2019-01-01T00:00:00.000Z"
                        },
                        "createdBy": {
                          "type": "string",
                          "example": "u32bac4d5e6f7g8h2"
                        },
                        "attachments": {
                          "type": "array"
                        },
                        "reactions": {
                          "type": "array"
                        },
                        "mentions": {
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
              "code": "var userId = \"USER_ID\";\nvar actionId = \"ACTION_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"actions/\" + actionId + \"/comments\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  body: \"New comment body\"\n};\n\n$.ajax({\n  method: \"POST\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
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
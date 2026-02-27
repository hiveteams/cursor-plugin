# Create action attachment

Attaches a file to an action.

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
    "/actions/{actionId}/attachments": {
      "post": {
        "summary": "Create action attachment",
        "description": "Attaches a file to an action.",
        "operationId": "create-file",
        "parameters": [
          {
            "name": "actionId",
            "in": "path",
            "description": "The ID of the action.",
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
                  "url": {
                    "type": "string",
                    "description": "File URL."
                  },
                  "filename": {
                    "type": "string",
                    "description": "Optional filename (including extension). If you do not pass this, a default from the path will be used."
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
                    "value": "{\n    \"message\": \"Action attachment successfully added\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "Action attachment successfully added"
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
              "code": "var userId = \"USER_ID\";\nvar actionId = \"ACTION_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1\";\nvar endpoint = \"/actions/\" + actionId + '/attachments';\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs\n\nvar data = {\n  url: \"https://domain.com/file/path\"\n};\n\n$.ajax({\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
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
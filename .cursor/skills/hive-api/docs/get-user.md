# Get user

Get a user by id

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
    "/users/{userId}": {
      "get": {
        "summary": "Get user",
        "description": "Get a user by id",
        "operationId": "get-user",
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "description": "User ID",
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
                    "value": "{\n  \"id\": \"232b3c4d5e6f7g8h1\",\n  \"profile\": {\n    \"firstName\": \"Jane\",\n    \"lastName\": \"Doe\"\n  },\n  \"fullName\": \"Jane Doe\",\n  \"email\": \"john.doe@hive.com\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "example": "232b3c4d5e6f7g8h1"
                    },
                    "profile": {
                      "type": "object",
                      "properties": {
                        "firstName": {
                          "type": "string",
                          "example": "Jane"
                        },
                        "lastName": {
                          "type": "string",
                          "example": "Doe"
                        }
                      }
                    },
                    "fullName": {
                      "type": "string",
                      "example": "Jane Doe"
                    },
                    "email": {
                      "type": "string",
                      "example": "john.doe@hive.com"
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
              "code": "var userId = \"USER_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"users/\" + userId;\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url,\n}).done(function(data) {\n  console.log(data);\n});\n"
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
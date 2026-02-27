# Invite user

Invite a new user to your workspace

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
    "/workspaces/{workspaceId}/users": {
      "post": {
        "summary": "Invite user",
        "description": "Invite a new user to your workspace",
        "operationId": "invite-user",
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
                  "email"
                ],
                "properties": {
                  "email": {
                    "type": "string",
                    "description": "Email Address"
                  },
                  "fullName": {
                    "type": "string",
                    "description": "Full name"
                  },
                  "shouldSendInvite": {
                    "type": "boolean",
                    "description": "Send email notification",
                    "default": true
                  },
                  "isExternal": {
                    "type": "boolean",
                    "description": "Invite user as external",
                    "default": false
                  },
                  "projectIds": {
                    "type": "array",
                    "description": "Array of projectIds to invite user in (is required when inviting external user)",
                    "items": {
                      "type": "string"
                    }
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
                    "value": "{\n  \"id\": \"232b3c4d5e6f7g8h1\",\n  \"profile\": {\n    \"firstName\": \"Test\",\n    \"lastName\": \"User\"\n  },\n\t\"fullName\": \"Test User\",\n  \"email\": \"test@example.com\"\n}\n"
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
                          "example": "Test"
                        },
                        "lastName": {
                          "type": "string",
                          "example": "User"
                        }
                      }
                    },
                    "fullName": {
                      "type": "string",
                      "example": "Test User"
                    },
                    "email": {
                      "type": "string",
                      "example": "test@example.com"
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"workspaces/\" + workspaceId + \"/users\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  email: \"test@example.com\",\n  fullName: \"Test User\"\n};\n\n$.ajax({\n  method: \"POST\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
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
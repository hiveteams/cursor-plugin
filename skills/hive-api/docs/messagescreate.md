# Create message

Create a new message

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
    "/messages/create": {
      "post": {
        "summary": "Create message",
        "description": "Create a new message",
        "operationId": "messagescreate",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "workspace": {
                    "type": "string",
                    "description": "ID of the workspace"
                  },
                  "body": {
                    "type": "string",
                    "description": "Body of the message"
                  },
                  "senderName": {
                    "type": "string",
                    "description": "The name of the sender"
                  },
                  "senderPicture": {
                    "type": "string",
                    "description": "URL of the sender picture"
                  },
                  "containerId": {
                    "type": "string",
                    "description": "Group the message will be created in"
                  },
                  "color": {
                    "type": "string",
                    "description": "Optional background color for the message. Options are yellow, purple, green, red, gray"
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
                    "value": "{\n  \"id\": \"2bK58icvKeJSzvupB\",\n  \"sender\": \"12345gfuJzo4k7F9\",\n  \"workspace\": \"12345naZjDQZndHqs\",\n  \"containerId\": \"12345ZTJqWY2QK2B\",\n  \"body\": \"This is a new message\",\n  \"senderPicture\": \"https://cdn2.iconfinder.com/data/icons/botcons/100/android-bot-round-ears-eyes-virus-brown-256.png\",\n  \"senderFirstName\": \"My Bot\",\n  \"createdBy\": \"12345gfuJzo4k7F9\",\n  \"modifiedBy\": \"12345xgfuJzo4k7F9\",\n  \"createdAt\": \"2018-01-23T22:14:24.862Z\",\n  \"modifiedAt\": \"2018-01-23T22:14:24.862Z\"\n}\n"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "example": "2bK58icvKeJSzvupB"
                    },
                    "sender": {
                      "type": "string",
                      "example": "12345gfuJzo4k7F9"
                    },
                    "workspace": {
                      "type": "string",
                      "example": "12345naZjDQZndHqs"
                    },
                    "containerId": {
                      "type": "string",
                      "example": "12345ZTJqWY2QK2B"
                    },
                    "body": {
                      "type": "string",
                      "example": "This is a new message"
                    },
                    "senderPicture": {
                      "type": "string",
                      "example": "https://cdn2.iconfinder.com/data/icons/botcons/100/android-bot-round-ears-eyes-virus-brown-256.png"
                    },
                    "senderFirstName": {
                      "type": "string",
                      "example": "My Bot"
                    },
                    "createdBy": {
                      "type": "string",
                      "example": "12345gfuJzo4k7F9"
                    },
                    "modifiedBy": {
                      "type": "string",
                      "example": "12345xgfuJzo4k7F9"
                    },
                    "createdAt": {
                      "type": "string",
                      "example": "2018-01-23T22:14:24.862Z"
                    },
                    "modifiedAt": {
                      "type": "string",
                      "example": "2018-01-23T22:14:24.862Z"
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
              "code": "var userId = \"USER_ID\";\nvar workspaceId = \"WORKSPACE_ID\";\nvar groupId = \"GROUP_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"messages/create\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  workspace: workspaceId,\n  body: \"Hi! this message was sent from the API.\",\n  senderName: \"Automated Messages\",\n  senderPicture:\n    \"https://cdn2.iconfinder.com/data/icons/botcons/100/android-bot-round-ears-eyes-virus-brown-256.png\",\n  containerId: groupId\n};\n\n$.ajax({\n  method: \"POST\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
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
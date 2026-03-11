# Get users

Get a list of users, filter by "email"

There was an extra slash key in the endpoint. Please correct.

```javascript
var userId = "USER_ID";
var filterEmail = "test@example.com";

var baseUrl = "https://app.hive.com/api/v1/";
var endpoint = "users";
var qs = "?user_id=" + userId + "&email=" + filterEmail;
var url = baseUrl + endpoint + qs;

$.ajax({
  url: url,
  headers: { api_key: "API_KEY" }
}).done(function(data) {
  console.log(data);
});
```

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
    "/users": {
      "get": {
        "summary": "Get users",
        "description": "Get a list of users, filter by \"email\"",
        "operationId": "get-user-by-email",
        "parameters": [
          {
            "name": "email",
            "in": "query",
            "description": "Email address to search by",
            "schema": {
              "type": "string"
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
                    "value": "[\n  {\n    \"id\": \"232b3c4d5e6f7g8h1\",\n    \"profile\": {\n      \"firstName\": \"Test\",\n      \"lastName\": \"User\"\n    },\n    \"fullName\": \"Test User\",\n    \"email\": \"test@example.com\"\n  }\n]\n"
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
              "code": "var userId = \"USER_ID\";\nvar filterEmail = \"test@example.com\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"users\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey + \"&email=\" + filterEmail;\nvar url = baseUrl + endpoint + qs;\n\n$.ajax({\n  url: url,\n}).done(function(data) {\n  console.log(data);\n});\n"
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
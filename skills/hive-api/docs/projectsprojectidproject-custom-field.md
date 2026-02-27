# Create project custom field

Creates a new custom field for a project

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
    "/projects/{projectId}/project-custom-field": {
      "post": {
        "summary": "Create project custom field",
        "description": "Creates a new custom field for a project",
        "operationId": "projectsprojectidproject-custom-field",
        "parameters": [
          {
            "name": "projectId",
            "in": "path",
            "description": "ID of the project to add a custom field to",
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
                  "label"
                ],
                "properties": {
                  "label": {
                    "type": "string",
                    "description": "Label for the custom field"
                  },
                  "type": {
                    "type": "string",
                    "description": "Type of the custom field. One of the following is allowed: text, number, date, user, project, select, formula.",
                    "default": "text"
                  },
                  "hidden": {
                    "type": "boolean",
                    "description": "If true, the value will be hidden in the UI but accessible via API",
                    "default": false
                  },
                  "value": {
                    "type": "string",
                    "description": "Value of the \"text\" custom field."
                  },
                  "numberValue": {
                    "type": "integer",
                    "description": "Value of the \"number\" custom field.",
                    "format": "int32"
                  },
                  "dateValue": {
                    "type": "string",
                    "description": "Value of the \"date\" custom field. ISO 8601 string."
                  },
                  "formula": {
                    "type": "string",
                    "description": "Value of the \"formula\" custom field."
                  },
                  "dropdownValues": {
                    "type": "array",
                    "description": "Value of the \"select\" custom field. Leave empty for \"user\" and \"project\" type.",
                    "items": {
                      "type": "string"
                    }
                  },
                  "selectedValues": {
                    "type": "array",
                    "description": "Selected value of the \"select\", \"user\" or \"project\" custom field.",
                    "items": {
                      "type": "string"
                    }
                  },
                  "allowMultiSelect": {
                    "type": "boolean",
                    "description": "Whether or not \"selectedValues\" can hold multiple values",
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
                    "value": "{\n  \"project\": {\n    \"id\": \"123ABC567XYZ\",\n    \"name\": \"Mobile app development\",\n    \"description\": \"A project for tracking our shiny new mobile app.\",\n    \"startDate\": \"2020-01-04T18:55:02.126Z\",\n    \"endDate\": \"2020-01-04T18:55:02.126Z\",\n    \"accessOption\": \"public\",\n    \"sharingType\": \"everyone\",\n    \"members\": [],\n    \"template\": false,\n    \"createdAt\": \"2017-05-18T15:26:17.407Z\",\n    \"modifiedAt\": \"2017-05-19T02:25:06.190Z\",\n    \"createdBy\": \"1234abcuJzo4k7F9\",\n    \"modifiedBy\": \"1234abcuJzo4k7F9\",\n    \"projectCustomFields\": [\n      {\n        \"label\": \"Budget\",\n        \"value\": \"$1000000\",\n        \"dropdownValues\": [],\n        \"selectedValues\": [],\n        \"type\": \"text\",\n        \"_id\": \"1234abcuJzo4k7E2\",\n        \"hidden\": false\n      }\n    ],\n    \"color\": \"#F2F2F2\",\n    \"parentProject\": null,\n    \"phases\": [],\n    \"resourcePlaceholderIds\": []\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "project": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string",
                          "example": "123ABC567XYZ"
                        },
                        "name": {
                          "type": "string",
                          "example": "Mobile app development"
                        },
                        "description": {
                          "type": "string",
                          "example": "A project for tracking our shiny new mobile app."
                        },
                        "startDate": {
                          "type": "string",
                          "example": "2020-01-04T18:55:02.126Z"
                        },
                        "endDate": {
                          "type": "string",
                          "example": "2020-01-04T18:55:02.126Z"
                        },
                        "accessOption": {
                          "type": "string",
                          "example": "public"
                        },
                        "sharingType": {
                          "type": "string",
                          "example": "everyone"
                        },
                        "members": {
                          "type": "array"
                        },
                        "template": {
                          "type": "boolean",
                          "example": false,
                          "default": true
                        },
                        "createdAt": {
                          "type": "string",
                          "example": "2017-05-18T15:26:17.407Z"
                        },
                        "modifiedAt": {
                          "type": "string",
                          "example": "2017-05-19T02:25:06.190Z"
                        },
                        "createdBy": {
                          "type": "string",
                          "example": "1234abcuJzo4k7F9"
                        },
                        "modifiedBy": {
                          "type": "string",
                          "example": "1234abcuJzo4k7F9"
                        },
                        "projectCustomFields": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "label": {
                                "type": "string",
                                "example": "Budget"
                              },
                              "value": {
                                "type": "string",
                                "example": "$1000000"
                              },
                              "dropdownValues": {
                                "type": "array"
                              },
                              "selectedValues": {
                                "type": "array"
                              },
                              "type": {
                                "type": "string",
                                "example": "text"
                              },
                              "_id": {
                                "type": "string",
                                "example": "1234abcuJzo4k7E2"
                              },
                              "hidden": {
                                "type": "boolean",
                                "example": false,
                                "default": true
                              }
                            }
                          }
                        },
                        "color": {
                          "type": "string",
                          "example": "#F2F2F2"
                        },
                        "parentProject": {},
                        "phases": {
                          "type": "array"
                        },
                        "resourcePlaceholderIds": {
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
              "code": "var userId = \"USER_ID\";\nvar projectId = \"PROJECT_ID\";\nvar apiKey = \"API_KEY\";\nvar baseUrl = \"https://app.hive.com/api/v1/\";\nvar endpoint = \"projects/\" + projectId + \"/project-custom-field\";\nvar qs = \"?user_id=\" + userId + \"&api_key=\" + apiKey;\nvar url = baseUrl + endpoint + qs;\n\nvar data = {\n  label: \"Budget\",\n  value: \"$1000000\"\n};\n\n$.ajax({\n  method: \"POST\",\n  url: url,\n  data: JSON.stringify(data),\n  contentType: \"application/json\"\n}).done(function(data) {\n  console.log(data);\n});"
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
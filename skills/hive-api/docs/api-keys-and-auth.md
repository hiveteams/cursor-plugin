# API Keys and Auth

# Getting your API key + User ID

Before you get started, you'll want to generate an API key and grab your User ID. To get those, log into your Hive account, go to the main menu in the top right, select "My profile" and then click on the "API info" tab. From there, generate a key for use throughout the API.

<Image title="Screen Shot 2020-12-07 at 9.05.47 AM.png" alt={2562} src="https://files.readme.io/464546f-Screen_Shot_2020-12-07_at_9.05.47_AM.png">
  Location of the API information menu
</Image>

<Image title="Screen Shot 2020-12-07 at 9.08.47 AM.png" alt={2648} src="https://files.readme.io/4ce2346-Screen_Shot_2020-12-07_at_9.08.47_AM.png">
  API information tab
</Image>

# Minimum Required Parameters

All requests require a user id in the URL query string parameters and an API key passed in a request header. The user id parameter is written as "user\_id", and the API key is passed in a header called "api\_key". You can go ahead and test your credentials by hitting the endpoint below with your generated API key and user id:

```curl
curl -X GET -H "api_key: API_KEY" "https://app.hive.com/api/v1/testcredentials?user_id=USER_ID"
```

You should get a `User authenticated` success message. Great job!
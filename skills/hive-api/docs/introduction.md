# Rest API Introduction

Welcome to the Hive REST API docs! The reference documentation here is designed for those interested in developing integrations for Hive that are not already inside of the Hive core product. You can use the Hive API to accomplish awesome things for your team, like creating automated messages, kicking off action templates, and much more.

## API compatibility

This API will evolve. Future versions of this API may add new endpoints or parameters. Parameters and endpoint may be subject to change and support is not guaranteed (although we will try our best to maintain backward compatibility).

Clients that want to be future-proof should avoid passing undocumented parameters (as they may cause different behavior in the future), and they should avoid strict checks on the keys of objects found in responses.

## SSL only

All requests to the Hive REST API are required to be done over [SSL](https://hosting.review/web-hosting-glossary/#12).

## Base Endpoint

All requests are to be sent to [https://app.hive.com/api/v1](https://app.hive.com/api/v1) as a prefix.

## Feedback + Community Contributions

We're always looking to improve the API + API documentation! If you have suggestions for the docs, please suggest edits on the section you're looking to improve by clicking the "Suggest Edits" button:

<Image title="Screen Shot 2018-01-28 at 4.56.38 PM.png" alt={330} src="https://files.readme.io/e06c660-Screen_Shot_2018-01-28_at_4.56.38_PM.png">
  "Suggest Edits" button
</Image>

If there's something you'd like to see in the API that does not currently exist, please reach out to the team via live chat by clicking the blue message icon in the bottom right of the screen:

<Image title="Screen Shot 2018-01-28 at 4.59.03 PM.png" alt={1312} src="https://files.readme.io/27a4810-Screen_Shot_2018-01-28_at_4.59.03_PM.png">
  Live chat support
</Image>
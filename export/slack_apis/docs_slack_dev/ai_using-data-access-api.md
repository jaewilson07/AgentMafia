---
url: https://docs.slack.dev/ai/using-data-access-api
session_id: slack_api_docs
updated_dt: 2025-03-27T13:24:36.024371
---
[Skip to main content](https://docs.slack.dev/ai/using-data-access-api#__docusaurus_skipToContent_fallback)
[![Slack Developer Docs](https://docs.slack.dev/img/logos/slack-developers-white.png)](https://slack.dev)[Docs](https://docs.slack.dev/)[Reference](https://docs.slack.dev/reference)[Samples](https://docs.slack.dev/samples)[Changelog](https://docs.slack.dev/changelog)
[Tools](https://tools.slack.dev)[Developer Program](https://api.slack.com/developer-program)[Your apps](https://api.slack.com/apps)
Search`K`
  * [Slack platform](https://docs.slack.dev/)
  * [Quickstart](https://docs.slack.dev/quickstart)
  * [FAQ](https://docs.slack.dev/faq)
  * [AI apps](https://docs.slack.dev/ai/)
    * [Overview](https://docs.slack.dev/ai/)
    * [Customizing Agentforce agents with custom Slack actions](https://docs.slack.dev/ai/customizing-agentforce-agents-with-custom-slack-actions)
    * [Developing AI apps](https://docs.slack.dev/ai/developing-ai-apps)
    * [Best practices](https://docs.slack.dev/ai/ai-apps-best-practices)
    * [Using the Data Access API](https://docs.slack.dev/ai/using-data-access-api)
  * [APIs](https://docs.slack.dev/apis/)
  * [App distribution](https://docs.slack.dev/distribution/)
  * [App manifests](https://docs.slack.dev/app-manifests/)
  * [Apps for Admins](https://docs.slack.dev/admins/)
  * [Authentication](https://docs.slack.dev/authentication/)
  * [Block Kit](https://docs.slack.dev/block-kit/)
  * [Enterprise Grid](https://docs.slack.dev/enterprise-grid/)
  * [Interactivity](https://docs.slack.dev/interactivity/)
  * [Messaging](https://docs.slack.dev/messaging/)
  * [Slack Marketplace](https://docs.slack.dev/slack-marketplace/)
  * [Surfaces](https://docs.slack.dev/surfaces/)
  * [Tools & SDKs](https://docs.slack.dev/tools/)
  * [Workflows](https://docs.slack.dev/workflows/)
  * [Legacy](https://docs.slack.dev/legacy/)


  * [](https://docs.slack.dev/)
  * [AI apps](https://docs.slack.dev/ai/)
  * Using the Data Access API


On this page
# Using the Data Access API
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
This API is currently in a **limited access** stage.
You may be able to obtain a token and call the API, but to get a valid response, you must be enrolled in the program. Contact Customer Experience at feedback@slack.com to request to be added.
AI apps are most useful when they have access to relevant contextual data. The Data Access API allows apps access to the Slack data that the invoking user has access to, through a short-lived token, to be used in Retrieval-Augmented Generation (RAG) queries. Accessing data in this way allows third-party applications to securely access Slack data without storing customer information on external servers. Providing this information for context to an LLM to use ensures higher relevance of its responses to your users' queries. Read on to discover how to employ this API exclusively in your [AI app](https://docs.slack.dev/ai/developing-ai-apps).
## API overview[​](https://docs.slack.dev/ai/using-data-access-api#overview "Direct link to API overview")
The purpose of the Data Access API is real-time data retrieval, designed to be used after a user interacts with an AI app, to ground RAG queries in relevant data from Slack. An application will receive an ephemeral token, called the `action_token`, from a message event, which can then be used to make a request to the Data Access API via the [`assistant.search.context`](https://docs.slack.dev/reference/methods/assistant.search.context) method. The Data Access API then searches all conversations (within the scope of permission granted) on the keywords provided in the user query and returns an array of messages relevant to the keyword search.
![Image of API Flow](https://docs.slack.dev/assets/images/data_access_api_flow-5e12ba687d4f1c4b797025ab4ff2146e.png)
### Required Scopes[​](https://docs.slack.dev/ai/using-data-access-api#required-scopes "Direct link to Required Scopes")
Your app must contain at least one of the following scopes, each providing various levels of access. Include all of them for a wider base from which to search.
Scope| Description  
---|---  
[`search:read.public`](https://docs.slack.dev/reference/scopes/search.read.public)| Read access to all public channel messages  
[`search:read.private`](https://docs.slack.dev/reference/scopes/search.read.private)| Read access to all private channel messages  
[`search:read.mpim`](https://docs.slack.dev/reference/scopes/search.read.mpim)| Read access to all multi-person direct messages  
[`search:read.im`](https://docs.slack.dev/reference/scopes/search.read.im)| Read access to all direct messages  
[`search:read.files`](https://docs.slack.dev/reference/scopes/search.read.files)| Read access to all files  
The `search:read.public` scope allows searching for data in public channels within the workspace(s) where the app is installed AND the searching user is a member. The searching user need not be a member of the public channels, just of the workspace, for the channels to be included in the search results.
Including any one of the `search:read.private`, `search:read.mpim`, and `search:read.im` scopes allows users to consent to those scopes within the Slack client. Users can choose to grant access to their private channels. They can only grant that access if the app has been installed with the corresponding scope. For example, if an admin installs the app with the `search:read.public` and `search:read.im` scopes, users will be able to consent to the IM scope, but not private/MPIM.
These scopes are in addition to the following scopes, which are needed for any AI app.
Scope| Description  
---|---  
[`assistant:write`](https://docs.slack.dev/reference/scopes/assistant.write)| Allow app to act as an AI app  
[`im:history`](https://docs.slack.dev/reference/scopes/im.history)| View messages and other content in DMs the app has been added to  
[`chat:write`](https://docs.slack.dev/reference/scopes/chat.write)| Write access to post messages channels and conversations  
To add these scopes, go to your [app settings](https://api.slack.com/apps), select your app, then:
  1. Go to the **OAuth & Permissions** section in the navigation sidebar
  2. Scroll down to the **Scopes** section
  3. Add the scopes listed above


#### User permission[​](https://docs.slack.dev/ai/using-data-access-api#user-permission "Direct link to User permission")
It is important to Slack that users opt in to their information being accessed by the Data Access API. The first time a user opens the AI app container view, Slack will prompt the user to allow the app to access their private conversations. If the user opts to allow, then the app can use the Data Access API across public channels, private channels, and MPDMs they are a part of (assuming the app's included scopes give it permission to do so).
The app can always access channels it has been added to, if it has the right scopes. The user scopes allow it to access channels that its NOT a member of, as long as the user making the query has access.
![](https://docs.slack.dev/assets/images/data_access_api_permissions-b250dc5a94ff8069e9c3b1ad7ae75b10.png)
### Supported events[​](https://docs.slack.dev/ai/using-data-access-api#events "Direct link to Supported events")
The [`message.im`](https://docs.slack.dev/reference/events/message.im), [`message.mpim`](https://docs.slack.dev/reference/events/message.mpim), [`message.groups`](https://docs.slack.dev/reference/events/message.groups), [`message.channels`](https://docs.slack.dev/reference/events/message.channels), and [`app_mention`](https://docs.slack.dev/reference/events/app_mention) events contain an `action_token` in the event body when the app is @ mentioned.
Your app will only receive an `action_token` in the event payload if it was @ mentioned in that message. If the app is not @ mentioned, you will still get the event as usual, but without an `action_token`. If a user sends a DM to your app, the @ mention is not needed and you will receive an `action_token` either way.
Your app must be subscribed to at least one of these events in order to get the token to pass to the [`assistant.search.context`](https://docs.slack.dev/reference/methods/assistant.search.context) method. To subscribe to these events, select your app from the list [here](https://api.slack.com/apps), navigate to the **Event Subscriptions** section in the left nav, expand the **Subscribe to bot events** section, and add the `message.im`, `message.mpim`, `message.groups`, `message.channels`, and `app_mention` events.
Other relevant events for an AI app include the [`assistant_thread_started`](https://docs.slack.dev/reference/events/assistant_thread_started) event and the [`assistant_thread_context_changed`](https://docs.slack.dev/reference/events/assistant_thread_context_changed) event. Read more about how those work in the scope of an AI app in the [AI apps & assistants usage guide](https://docs.slack.dev/ai/developing-ai-apps).
## Data access flow[​](https://docs.slack.dev/ai/using-data-access-api#data-access "Direct link to Data access flow")
You must have an existing app to take advantage of the Data Access API with the **Agents & AI Apps** feature enabled. Follow the setup for [AI apps](https://docs.slack.dev/ai/developing-ai-apps) first.
### **1. Obtain`action_token` from appropriate event payload**[​](https://docs.slack.dev/ai/using-data-access-api#event-listener "Direct link to event-listener")
Your app can obtain the `action_token` needed to query the Data Access API from either a message event or an `app_mention` event. Message events that include the `action_token` are:
  * [`message.im`](https://docs.slack.dev/reference/events/message.im)
  * [`message.mpim`](https://docs.slack.dev/reference/events/message.mpim)
  * [`message.groups`](https://docs.slack.dev/reference/events/message.groups)
  * [`message.channels`](https://docs.slack.dev/reference/events/message.channels) (when the app is mentioned)


The [`app_mention`](https://docs.slack.dev/reference/events/app_mention) event contains an `action_token` in the payload when the app is mentioned using "@app-name".
The `action_token` can be used to make a request to the Data Access API. The token will be within the `assistant_thread` object, as shown below:
```
{"user":"U12345678","type":"message","ts":1737049721.016239,"text":"Can you summarize this channel?","thread_ts":1733757377.689059,"parent_user_id":"U98765432","channel":"C1230045","assistant_thread":{"action_token":"1234567.abcdefg"},"event_ts":1737049721.016239,"channel_type":"im"}
```

### **2. Use the`action_token` to send a request to the Data Access API**[​](https://docs.slack.dev/ai/using-data-access-api#use-action-token "Direct link to use-action-token")
The `action_token` is short-lived, so it’s important to use it soon after your app receives it. Make a request to the [`assistant.search.context`](https://docs.slack.dev/reference/methods/assistant.search.context) method, and the response will contain messages or files relevant to your query. The `action_token` should be provided _in addition to_ the standard Slack token that begins with `xoxop-` or `xoxob-`.
#### `assistant.search.context` API method reference[​](https://docs.slack.dev/ai/using-data-access-api#assistantsearchcontext-api-method-reference "Direct link to assistantsearchcontext-api-method-reference")
Parameter| Required/Optional| Description  
---|---|---  
`query`| Required| User prompt or query  
`token`| Required| Bot token  
`action_token`| Required| Ephemeral token generated after a user interaction with an AI app  
`channel_types`| Optional| Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`  
`content_types`| Optional| Content types to include, a comma-separated list of any combination of `messages`, `files`  
`context_channel_id`| Optional| Context channel ID to support scoping the search when applicable  
`cursor`| Optional| The cursor returned by the API. Leave this blank for the first request, and use this to get the next page of results  
`include_bots`| Optional| If you want the results to include messages from bots  
`limit`| Optional| Number of results to return, up to a max of 20. Defaults to 20.  
**Request**
```
{"query":"What is project gizmo?","action_token":"1234567.abcdefg"}
```

**Response**
```
{"ok":true,"results":{"messages":[{"author_user_id":"U0123456","team_id":"T0123456","channel_id":"C0123456","message_ts":"123456.7890","content":"Hey team, we'll be kicking off our mobile UX revamp for the Gizmo App...","is_author_bot":false,"permalink":"https://mycompany.slack.com/archives/C012345ABC/p123456789"}]    ...},"response_metadata":{"next_cursor":"Q1VSUkVOVF9QQUdFOjI="}}
```

The `is_author_bot` field can be used to discern bot messages from regular user messages when formatting contextual information to send to an LLM. The `permalink` field provides a permalink to the message. This can be useful to provide to your users in a "sources" list when the app responds to the user in a thread. Sharing sources in the app response is a [best practice](https://docs.slack.dev/ai/ai-apps-best-practices#references).
If there are additional pages of results, the API will return a value in the `next_cursor` field; if not, there will be an empty string. Use the value of `next_cursor` to query the API again for subsequent results pages. The API allows a maximum of 20 results per page.
### **3. Explore other ways to gather context data to provide the LLM**[​](https://docs.slack.dev/ai/using-data-access-api#data-gathering "Direct link to data-gathering")
Obtaining contextual information from the Data Access API is a great way to provide the LLM relevant information on which to base query responses, but it's not the only way. You can provide the full thread history for continuity in conversation. Or maybe you'd like to provide the entire history of the channel that the user is currently in, alongside the data retrieved from the `assistant.search.context` method. Check out how to provide this type of contextual information while developing with the Bolt SDK in the tutorial [Getting started with an AI Assistant](https://tools.slack.dev/bolt-js/tutorials/ai-assistant).
## Use in public channels[​](https://docs.slack.dev/ai/using-data-access-api#public-channels "Direct link to Use in public channels")
When calling the Data Access API from within a public channel, the scope of content searched and shared is more limited. The Data Access API will only return results from public channels, regardless of if the user has more granular scopes, like `search:read.private`, enabled. If the channel is public, then the API will return results from all public channels the user has access to in the workspace that the API was invoked in.
If the Data Access API is called from an MPDM or a private channel, it returns results from only the MPDM/private channel and all public channels that exist in that same workspace. This workspace limitation is because users may be in different workspaces, and thus have different public channel data access.
If the Data Access API is called from a Slack Connect channel, it will return results from _only_ the channel where it was invoked. This prevents users from seeing data they might otherwise not have access to.
Subscribe to the [`app_mention`](https://docs.slack.dev/reference/events/app_mention) event to be notified when it is mentioned in channels. When it is mentioned, the `action_token` will be present in the event payload.
## Limitations[​](https://docs.slack.dev/ai/using-data-access-api#limitations "Direct link to Limitations")
The Data Access API currently does not provide semantic retrieval capabilities. Searching for the keyword "revenue", for example, will not return results containing "profit."
Formatting in the search string can cause unexpected results, so be sure to strip any formatting from the search string before sending to the Data Access API.
The Data Access API will provide the most relevant results based on the search query. As such, the following are excluded from the results:
  * Low relevance results
  * Non-text files
  * Google Drive links (if it is not installed)


## Data privacy[​](https://docs.slack.dev/ai/using-data-access-api#privacy "Direct link to Data privacy")
When performing a search, a third-party app requires various permissions to access data. In order to search public channel content, an app needs to be present within a workspace (and thus approved by an admin). For private channel content and files, both an admin and the end user need to have granted access to private scopes.
For DMs and MPDMs, admin and user permissions are also required, but only for a single workspace, as they’re not tied to any particular workspace. The user can revoke their consent for the granted private/DM/MPDM scopes after initially granting them.
We rely on which workspace(s) apps are installed on to determine and limit content access. An Admin should not install an AI app with a `search:read` scope to multiple workspaces if they do not want specific data to be accessible to the app. Alternatively, developers have the option to create a separate apps for secure workspaces, such as [GovSlack](https://slack.com/solutions/govslack).
We do not store any LLM prompts or response data (other than in the feedback payload), and we do not train anything on Personally Identifiable Information (PII).
Per Slack policy, zero-data copy and zero-data usage for training LLMs is allowed.
You must not store or copy any of the data retrieved from this API.
You must not store or copy any of the data retrieved from this API. You may not use any of this data for training. You may not use this API to scrape data in a workspace that is unrelated to user queries.
### Guest access[​](https://docs.slack.dev/ai/using-data-access-api#guests "Direct link to Guest access")
Workspace guests are not permitted to access [AI apps](https://docs.slack.dev/ai/), and therefore, the Data Access API.
[PreviousBest practices](https://docs.slack.dev/ai/ai-apps-best-practices)[NextOverview](https://docs.slack.dev/apis/)
  * [API overview](https://docs.slack.dev/ai/using-data-access-api#overview)
    * [Required Scopes](https://docs.slack.dev/ai/using-data-access-api#required-scopes)
    * [Supported events](https://docs.slack.dev/ai/using-data-access-api#events)
  * [Data access flow](https://docs.slack.dev/ai/using-data-access-api#data-access)
    * [**1. Obtain`action_token` from appropriate event payload**](https://docs.slack.dev/ai/using-data-access-api#event-listener)
    * [**2. Use the`action_token` to send a request to the Data Access API**](https://docs.slack.dev/ai/using-data-access-api#use-action-token)
    * [**3. Explore other ways to gather context data to provide the LLM**](https://docs.slack.dev/ai/using-data-access-api#data-gathering)
  * [Use in public channels](https://docs.slack.dev/ai/using-data-access-api#public-channels)
  * [Limitations](https://docs.slack.dev/ai/using-data-access-api#limitations)
  * [Data privacy](https://docs.slack.dev/ai/using-data-access-api#privacy)
    * [Guest access](https://docs.slack.dev/ai/using-data-access-api#guests)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



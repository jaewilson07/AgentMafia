---
url: https://docs.slack.dev/legacy/legacy-rtm-api
session_id: slack_api_docs
updated_dt: 2025-03-27T13:26:02.307621
---
[Skip to main content](https://docs.slack.dev/legacy/legacy-rtm-api#__docusaurus_skipToContent_fallback)
[![Slack Developer Docs](https://docs.slack.dev/img/logos/slack-developers-white.png)](https://slack.dev)[Docs](https://docs.slack.dev/)[Reference](https://docs.slack.dev/reference)[Samples](https://docs.slack.dev/samples)[Changelog](https://docs.slack.dev/changelog)
[Tools](https://tools.slack.dev)[Developer Program](https://api.slack.com/developer-program)[Your apps](https://api.slack.com/apps)
Search`K`
  * [Slack platform](https://docs.slack.dev/)
  * [Quickstart](https://docs.slack.dev/quickstart)
  * [FAQ](https://docs.slack.dev/faq)
  * [AI apps](https://docs.slack.dev/ai/)
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
    * [Overview](https://docs.slack.dev/legacy/)
    * [Legacy classic app migration](https://docs.slack.dev/legacy/legacy-rtm-api)
    * [Legacy authentication](https://docs.slack.dev/legacy/legacy-authentication/)
    * [Legacy bot users](https://docs.slack.dev/legacy/legacy-bot-users)
    * [Legacy custom integrations](https://docs.slack.dev/legacy/legacy-rtm-api)
    * [Legacy dialogs](https://docs.slack.dev/legacy/legacy-dialogs)
    * [Legacy messaging](https://docs.slack.dev/legacy/legacy-messaging/)
    * [Legacy RTM API](https://docs.slack.dev/legacy/legacy-rtm-api)
    * [Legacy Slack button](https://docs.slack.dev/legacy/legacy-slack-button)
    * [Legacy Steps from Apps](https://docs.slack.dev/legacy/legacy-steps-from-apps/)


  * [](https://docs.slack.dev/)
  * [Legacy](https://docs.slack.dev/legacy/)
  * Legacy RTM API


On this page
# Legacy RTM API
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
The legacy Real Time Messaging (RTM) API is a WebSocket-based API that allows you to receive [events](https://docs.slack.dev/reference/events) from Slack in real time and send messages as users, including bot users. It's sometimes referred to as the "RTM API".
It was once the basis for all Slack clients and once commonly used with [bot users](https://docs.slack.dev/legacy/legacy-bot-users) to create helper bots for your workspace.
We recommend having events _pushed_ to you instead, using the HTTP-based [Events API](https://docs.slack.dev/apis/events-api/). Most of the RTM API's supported event types are also [supported by the Events API](https://docs.slack.dev/reference/events?filter=Events). If you really like WebSockets, [Socket Mode for apps](https://docs.slack.dev/apis/events-api/using-socket-mode) delivers event subscriptions over WebSockets instead.
Many workspace administrators will not allow apps and integrations using the RTM API due to the overly permissive permission scopes required for their operation. Slack apps allow you to subscribe to events and request permissions for only the data your app truly needs to operate.
## Notices[​](https://docs.slack.dev/legacy/legacy-rtm-api#notices "Direct link to Notices")
This API is ancient and the ways to access it have grown more limited over time. Please excuse this litany of warnings and calls to action below.
Granular permission Slack apps cannot use the RTM API.
Classic apps can, but be warned that they may no longer be created and are soon to be deprecated.
For most applications, [Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode) is a better way to communicate with Slack
## Basics[​](https://docs.slack.dev/legacy/legacy-rtm-api#basics "Direct link to Basics")
To begin a RTM session make an authenticated call to the [rtm.connect](https://docs.slack.dev/reference/methods/rtm.connect) API method. This provides an initial set of workspace metadata and a message server WebSocket URL. Once you have connected to the message server it will provide a stream of events, including both messages and updates to the current state of the workspace. This allows a client to easily maintain a synchronized local copy of all workspace data and messages.
The Websocket URLs provided by `rtm.connect` are single-use and are only valid for 30 seconds, so make sure to connect quickly. If you connect successfully the first event received will be a hello:
```
{"type":"hello"}
```

This will be followed by any events that occurred between the call to `rtm.connect` and the connection to the message server. If you're reconnecting after a network problem this initial set of events may include a response to the last message sent on a previous connection (with a `reply_to`) so a client can confirm that message was received.
If there was a problem connecting an error will be returned, including a descriptive error message:
```
{"type":"error","error":{"code":1,"msg":"Socket URL has expired"}}
```

## Events[​](https://docs.slack.dev/legacy/legacy-rtm-api#events "Direct link to Events")
Almost everything that happens in Slack will result in an event being sent to all connected clients. A common event is a message sent from a user:
```
{"type":"message","ts":"1358878749.000002","user":"U123ABC456","text":"Hello"}
```

Every event has a `type` property which describes the type of event.
## Sending messages[​](https://docs.slack.dev/legacy/legacy-rtm-api#sending-messages "Direct link to Sending messages")
You can send a message to Slack by sending JSON over the WebSocket connection.
Every event should have a unique (for that connection) positive integer ID. All replies to that message will include this ID allowing the client to correlate responses with the messages sent; replies may be "out of order" due to the asynchronous nature of the message servers.
Also, as with events sent from the server, each event sent by the client has a string `type` specifying what the message does — chat messages are of type `message`.
### Channel selection[​](https://docs.slack.dev/legacy/legacy-rtm-api#channel-selection "Direct link to Channel selection")
So to post the text "Hello world" to a channel, you can send this JSON:
```
{"id":1,"type":"message","channel":"C123ABC456","text":"Hello world"}
```

You can send a message to a private group or direct message channel in the same way, but using a group ID (`C123ABC456`) or direct message channel ID (`D0123ABC456`).
To send a message both _as_ and _to_ the authenticating user, use the correct direct message channel ID for that user. The direct message ID can be found as part of the response to [`rtm.connect`](https://docs.slack.dev/reference/methods/rtm.connect), or by consulting [`conversations.list`](https://docs.slack.dev/reference/methods/conversations.list).
### Formatting messages[​](https://docs.slack.dev/legacy/legacy-rtm-api#formatting-messages "Direct link to Formatting messages")
The RTM API only supports posting basic messages formatted using our [default message formatting mode](https://docs.slack.dev/messaging/formatting-message-text). It does not support [attachments](https://docs.slack.dev/messaging/formatting-message-text#attachments) or other message formatting modes. To post a more complex message as a user clients can call the [`chat.postMessage`](https://docs.slack.dev/reference/methods/chat.postMessage) Web API method with `as_user` set to true.
User mentions over RTM should use the User ID-based `<@U123ABC>` syntax:
```
{"id":2,"type":"message","channel":"C123ABC456","text":"Hello <@U123ABC>"}
```

### Handling responses[​](https://docs.slack.dev/legacy/legacy-rtm-api#handling-responses "Direct link to Handling responses")
Once the JSON has been sent to the server visual clients should immediately display the text in the channel, grayed out or otherwise marked to indicate that it is "pending". At some point after that, usually a few milliseconds later, the server will send a confirmation that the message was received:
```
{"ok":true,"reply_to":1,"ts":"1355517523.000005","text":"Hello world"}
```

Replies to messages sent by clients will always contain two properties: a boolean `ok` indicating whether they succeeded and an integer `reply_to` indicating which message they are in response to.
In the case of a reply to a chat message, if successful, the reply will contain the canonical recorded timestamp of the message. All messages within a single channel are guaranteed to have a unique timestamp which is ASCII sortable. Given the precision of the timestamp, clients should treat these timestamps as strings, not floats/doubles. Once a successful reply has been returned, the message in the chat log should no longer be grayed out - it has now been delivered.
Chat message replies also contain the message text, which may vary from the sent message due to URL detection.
#### Errors[​](https://docs.slack.dev/legacy/legacy-rtm-api#errors "Direct link to Errors")
If there is an error processing an event the message server will reply with an error. For example:
```
{"ok":false,"reply_to":1,"error":{"code":2,"msg":"message text is missing"}}
```

## Typing indicators[​](https://docs.slack.dev/legacy/legacy-rtm-api#typing-indicators "Direct link to Typing indicators")
Clients can send a typing indicator to indicate that the user is currently writing a message to send to a channel:
```
{"id":1,"type":"typing","channel":"C123ABC456"}
```

This can be sent on every key press in the chat input unless one has been sent in the last three seconds. Unless there is an error the server will not send a reply, but it will send a "user_typing" event to all workspace members in the channel.
## Presence[​](https://docs.slack.dev/legacy/legacy-rtm-api#presence "Direct link to Presence")
User and bot user presence on the RTM API is complicated enough to warrant an entire document. Learn all about presence subscriptions and batch presence events [here](https://docs.slack.dev/apis/web-api/user-presence-and-status#presence).
RTM API Presence is now only available via subscription
As of January 2018, [`presence_change`](https://docs.slack.dev/reference/events/presence_change) events are not dispatched without [_presence subscriptions_](https://docs.slack.dev/apis/web-api/user-presence-and-status) established with [`presence_sub`](https://docs.slack.dev/reference/events/presence_sub). Relatedly, current user presence status is no longer communicated in [`rtm.start`](https://docs.slack.dev/reference/methods/rtm.start). [Learn more](https://docs.slack.dev/changelog/2018-01-presence-present-and-future).
## Ping and Pong[​](https://docs.slack.dev/legacy/legacy-rtm-api#ping-pong "Direct link to Ping and Pong")
Clients should try to quickly detect disconnections, even in idle periods, so that users can easily tell the difference between being disconnected and everyone being quiet. Not all web browsers support the WebSocket ping spec, so the RTM protocol also supports ping/pong messages. When there is no other activity clients should send a ping every few seconds. To send a ping, send the following JSON:
```
{"id":1234,// ID, see "sending messages" above"type":"ping",	...}
```

You can supply any number of extra "flat" arguments (that is: only scalar values, no arrays or objects). These will be included in the pong message that is sent back. For example, a client could include a local timestamp in the ping message so it can calculate round-trip latency:
```
{"id":1234,"type":"ping","time":1403299273342}
```

This will be included in the reply from the server:
```
{"reply_to":1234,"type":"pong","time":1403299273342}
```

## Limits[​](https://docs.slack.dev/legacy/legacy-rtm-api#limits "Direct link to Limits")
The message server will disconnect any client that sends a message longer than 16 kilobytes. This includes all parts of the message, including JSON syntax, not just the message text. Clients should limit messages sent to channels to 4000 characters, which will always be under 16k bytes even with a message comprised solely of non-BMP Unicode characters at 4 bytes each. If the message is longer a client should prompt to split the message into multiple messages, create a snippet or create a post.
As with all Slack APIs, the RTM API is subject to [rate limits](https://docs.slack.dev/apis/web-api/rate-limits). Clients should not send more than one message per second sustained. If you do you may receive an error message or be disconnected.
## What's a WebSocket?[​](https://docs.slack.dev/legacy/legacy-rtm-api#websocket "Direct link to What's a WebSocket?")
[WebSockets](https://en.wikipedia.org/wiki/WebSocket) are a standard way to open a long-lived bi-directional communication channel with a server over TCP. It's the protocol used when connecting to our [RTM API](https://docs.slack.dev/legacy/legacy-rtm-api). Many [contributions from our community](https://slackcommunity.com) support the particulars of connecting to Slack via a WebSocket.
## Connecting with `rtm.connect` vs. `rtm.start`[​](https://docs.slack.dev/legacy/legacy-rtm-api#connect-start "Direct link to connect-start")
There are currently two ways to reserve websocket connections.
[`rtm.connect`](https://docs.slack.dev/reference/methods/rtm.connect) concerns itself only with getting your app connected to the RTM API, and only includes limited information about the connecting user and housing workspace.
[`rtm.start`](https://docs.slack.dev/reference/methods/rtm.start) includes not only an entire kitchen sink but an entire kitchen filled with information about the user, its workspace, its channels, its current state in the universe. `rtm.start` is naturally more difficult to use with [Enterprise Grid](https://docs.slack.dev/enterprise-grid) and other large workspaces.
We strongly recommend using `rtm.connect` to reserve your websocket connections and use the [Web API](https://docs.slack.dev/apis/web-api/) in tandem to collect all the state information your app needs.
## Using the RTM API on Enterprise Grid[​](https://docs.slack.dev/legacy/legacy-rtm-api#enterprise-grid "Direct link to Using the RTM API on Enterprise Grid")
There are additional support actions you'll need to take for the RTM API to properly work with Enterprise Grid.
RTM:
  * Support events & messages containing [global user IDs](https://docs.slack.dev/legacy/legacy-rtm-api#global_user_ids)
  * Support users from other [workspaces](https://docs.slack.dev/legacy/legacy-rtm-api#identifying_an_enterprise_organization) in [shared channels](https://docs.slack.dev/apis/slack-connect/)
  * Support duplicate message deliveries in [shared channels](https://docs.slack.dev/apis/slack-connect/) when installed on multiple workspaces
  * Connect using [`rtm.connect`](https://docs.slack.dev/reference/methods/rtm.connect) instead of `rtm.start`


### Be careful with messages[​](https://docs.slack.dev/legacy/legacy-rtm-api#messages_and_bots "Direct link to Be careful with messages")
If your application is installed by multiple workspaces of an Enterprise Grid and _then_ used in a shared channel, it's possible that your bot will receive multiple [RTM events](https://docs.slack.dev/reference/events) for the same message: one for each of the workspaces you're installed on.
If your bot doesn't de-duplicate the messages by looking at the `ts` value of each message, you might interpret each one independently and reply to them, adding noise a conversation.
Look for the `source_team` message field to identify the Enterprise workspace the message originates from.
To help you understand the different scenarios in which you'll receive multiple messages, let's imagine the following situation:
  * We have 3 workspaces in an organization
  * Of the 3 workspaces, your app is installed on Workspace 1 and Workspace 2
  * Your app is not installed on Workspace 3
  * Your bot has been invited to join a shared channel that exists between users from all 3 workspaces.
  * Your app has opened websocket connections for both Workspace 1 and Workspace 2

Condition| Result  
---|---  
User from Workspace 1 sends message| RTM websocket for Workspace 1 will receive the message as normal.  
User from Workspace 2 sends message| RTM websocket for Workspace 2 will receive the message as normal.  
User from Workspace 3 sends message| RTM websocket for Workspace 1 will receive the message with some additional metadata.  
One way to handle duplicate messages is to make one of the workspaces in the shared channel (that your app is installed on) responsible for handling _all_ messages coming from that shared channel.
To do this, you'll need to listen to the [`channel_joined`](https://docs.slack.dev/reference/events/channel_joined) event when your bot is added to a shared channel. The metadata included in this event will tell you which workspaces are part of the shared channel.
Of the workspaces in the channel that your app is installed on, you'll want to pick one and save both the channel ID and team ID in your database. From that point on, you can look up the channel ID for every message you need to respond to and determine which workspace's RTM should respond.
Alternatively, you can ignore all messages coming from a workspace that is not the same as the workspace your app is installed on. This will prevent users on workspaces that haven't installed your app from being able to interact with your bot.
### Working with direct messages[​](https://docs.slack.dev/legacy/legacy-rtm-api#direct_messages "Direct link to Working with direct messages")
Direct messages work much like channels: private conversations between two or more individuals spanning multiple workspaces within an Enterprise Grid result in RTM API streaming one message for each of your open websocket connections.
Your app can be the target of a direct message from another workspace across the Enterprise Grid. You never know when a user might want to collaborate with your bot.
These messages will also contain a `source_team` attribute when perspectively appropriate. The `source_team` attribute contains the workspace within the Enterprise Grid that the message originates from.
As with channels, when connected to multiple websocket connections on behalf of workspaces in the Enterprise Grid, you can receive redundant message deliveries. They will have the same `ts` value.
[PreviousLegacy secondary message attachments](https://docs.slack.dev/legacy/legacy-messaging/legacy-secondary-message-attachments)[NextLegacy Slack button](https://docs.slack.dev/legacy/legacy-slack-button)
  * [Notices](https://docs.slack.dev/legacy/legacy-rtm-api#notices)
  * [Basics](https://docs.slack.dev/legacy/legacy-rtm-api#basics)
  * [Events](https://docs.slack.dev/legacy/legacy-rtm-api#events)
  * [Sending messages](https://docs.slack.dev/legacy/legacy-rtm-api#sending-messages)
    * [Channel selection](https://docs.slack.dev/legacy/legacy-rtm-api#channel-selection)
    * [Formatting messages](https://docs.slack.dev/legacy/legacy-rtm-api#formatting-messages)
    * [Handling responses](https://docs.slack.dev/legacy/legacy-rtm-api#handling-responses)
  * [Typing indicators](https://docs.slack.dev/legacy/legacy-rtm-api#typing-indicators)
  * [Presence](https://docs.slack.dev/legacy/legacy-rtm-api#presence)
  * [Ping and Pong](https://docs.slack.dev/legacy/legacy-rtm-api#ping-pong)
  * [Limits](https://docs.slack.dev/legacy/legacy-rtm-api#limits)
  * [What's a WebSocket?](https://docs.slack.dev/legacy/legacy-rtm-api#websocket)
  * [Connecting with `rtm.connect` vs. `rtm.start`](https://docs.slack.dev/legacy/legacy-rtm-api#connect-start)
  * [Using the RTM API on Enterprise Grid](https://docs.slack.dev/legacy/legacy-rtm-api#enterprise-grid)
    * [Be careful with messages](https://docs.slack.dev/legacy/legacy-rtm-api#messages_and_bots)
    * [Working with direct messages](https://docs.slack.dev/legacy/legacy-rtm-api#direct_messages)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



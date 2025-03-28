---
url: https://docs.slack.dev/apis/events-api
session_id: slack_api_docs
updated_dt: 2025-03-27T13:24:53.657539
---
[Skip to main content](https://docs.slack.dev/apis/events-api#__docusaurus_skipToContent_fallback)
[![Slack Developer Docs](https://docs.slack.dev/img/logos/slack-developers-white.png)](https://slack.dev)[Docs](https://docs.slack.dev/)[Reference](https://docs.slack.dev/reference)[Samples](https://docs.slack.dev/samples)[Changelog](https://docs.slack.dev/changelog)
[Tools](https://tools.slack.dev)[Developer Program](https://api.slack.com/developer-program)[Your apps](https://api.slack.com/apps)
Search`K`
  * [Slack platform](https://docs.slack.dev/)
  * [Quickstart](https://docs.slack.dev/quickstart)
  * [FAQ](https://docs.slack.dev/faq)
  * [AI apps](https://docs.slack.dev/ai/)
  * [APIs](https://docs.slack.dev/apis/)
    * [Overview](https://docs.slack.dev/apis/)
    * [Web API](https://docs.slack.dev/apis/web-api/)
    * [Events API](https://docs.slack.dev/apis/events-api/)
      * [Overview](https://docs.slack.dev/apis/events-api/)
      * [Comparing HTTP & Socket Mode](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode)
      * [Using HTTP Request URLs](https://docs.slack.dev/apis/events-api/using-http-request-urls)
      * [Using Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode)
    * [Slack Connect](https://docs.slack.dev/apis/slack-connect/)
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
  * [APIs](https://docs.slack.dev/apis/)
  * Events API


On this page
# The Events API
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
The Events API is a streamlined way to build apps and bots that respond to activities in Slack. When you use the Events API, _Slack_ calls _you_.
You have two options: you can either use [Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode) or you can designate a public [HTTP endpoint](https://docs.slack.dev/apis/events-api/using-http-request-urls) that your app listens on, choose what events to subscribe to, and _voilà_ : Slack sends the appropriate events to you. Learn more about the differences between Socket Mode and HTTP [here](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode).
All you need is a Slack app and a secure place for us to send your [events](https://docs.slack.dev/reference/events). With the Events API, you can do the following:
  * Tell Slack where to send your [event types](https://docs.slack.dev/reference/events) and we'll deliver them with grace, security, and respect. We'll even retry when things don't work out. The [event types](https://docs.slack.dev/reference/events) sent to you are directly tied to the [OAuth permission scopes](https://docs.slack.dev/authentication/installing-with-oauth) awarded as users install your Slack app.
  * Subscribe to only the [event types](https://docs.slack.dev/reference/events) you want; don't worry about the ones you don't need.
  * Subscribe your Slack apps to events related to channels and direct messages they are party to. Build bots without a bothersome bevy of [Real Time Messaging (RTM) API](https://docs.slack.dev/legacy/legacy-rtm-api) WebSockets.


## Overview[​](https://docs.slack.dev/apis/events-api#overview "Direct link to Overview")
Many apps built using the Events API will follow the same abstract event-driven sequence:
  1. A user creates a circumstance that triggers an event subscription to your application.
  2. Your server receives a payload of JSON describing that event.
  3. Your server acknowledges receipt of the event.
  4. Your business logic decides what to do about that event.
  5. Your server carries out that decision.


If your app is a bot listening to messages with specific trigger phrases, that event loop may play out something like the following:
  1. Members send messages in a channel the bot belongs to—the #random channel. The messages are about lots of things, but some of them contain today's secret word.
  2. Your server receives a [`message.channels`](https://docs.slack.dev/reference/events/message.channels) event, as per its bot subscription and membership in the #random channel.
  3. Your server responds with a swift and confident HTTP 200 OK.
  4. Your bot is trained to listen for today's secret word, and having found it, decides to send a message to the channel, encouraging everyone to keep that word secret.
  5. Your server uses [`chat.postMessage`](https://docs.slack.dev/reference/methods/chat.postMessage) from the Web API to post that message to #random.


Using the Web API with the Events API empowers your app or bot to do much more than just listen and reply to messages.
Let's get started!
## Preparing your app to use the Events API[​](https://docs.slack.dev/apis/events-api#prepare "Direct link to Preparing your app to use the Events API")
The Events API is recommended over the [RTM API](https://docs.slack.dev/legacy/legacy-rtm-api) for most use cases. If you're already familiar with HTTP and are comfortable maintaining your own server, handling the request and response cycle of the Events API should be familiar. If the world of web APIs is new to you, the Events API is a great next step after mastering [incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks) or the [Web API](https://docs.slack.dev/apis/web-api/).
### Is the Events API right for your app?[​](https://docs.slack.dev/apis/events-api#your-app "Direct link to Is the Events API right for your app?")
Before starting, you may want to make a few early decisions about your application architecture and approach to consuming events. The Events API is best used in conjunction with other platform features.
One way to use the Events API is as an alternative to opening WebSocket connections to the [RTM API](https://docs.slack.dev/legacy/legacy-rtm-api). Why choose the Events API over the legacy RTM API? Instead of maintaining one or more long-lived connections for each workspace an application is connected to, you can set up one or more endpoints on your own servers to receive events atomically in near real-time.
Some developers may want to use the Events API as a kind of redundancy for their existing WebSocket connections. Other developers will use the Events API to receive information around the workspaces and users they are acting on behalf, to improve their [slash commands](https://docs.slack.dev/interactivity/implementing-slash-commands), bot users, [notifications](https://docs.slack.dev/messaging), or other capabilities. With [app events](https://docs.slack.dev/apis/events-api#app_events), you can track app uninstallation, token revocation, Enterprise Grid migration, and more. Handle anything else your app does by using [incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks) and other write-based [web API methods](https://docs.slack.dev/reference/methods).
### Permission model[​](https://docs.slack.dev/apis/events-api#permission-model "Direct link to Permission model")
The Events API leverages Slack's existing [object-driven OAuth scope system](https://docs.slack.dev/authentication/installing-with-oauth) to control access to events. For example, if your app has access to files through the `files:read` scope, you can choose to subscribe to any or none of the file-related events such as [`file_created`](https://docs.slack.dev/reference/events/file_created) and [`file_deleted`](https://docs.slack.dev/reference/events/file_deleted).
You will only receive events that users who have authorized your app can "see" on their workspace (that is, if a user authorizes access to private channel history, you'll only see the activity in private channels they are a member of, not all private channels across the workspace).
[Bot users](https://docs.slack.dev/authentication/tokens#bot) may also subscribe to events on their own behalf. The `bot` scope requested when workspaces install your bot covers events access for both the Events API and the [Real Time Messaging API](https://docs.slack.dev/legacy/legacy-rtm-api).
## Subscribing to event types[​](https://docs.slack.dev/apis/events-api#subscribing "Direct link to Subscribing to event types")
To begin working with the Events API, you'll need to create a Slack app if you haven't already. While managing your application, find the **Event Subscriptions** setting and use the toggle to turn it on.
![The on switch for the Events API](https://docs.slack.dev/assets/images/events_api_turn_it_on-eba64c9d3c0012dedf13865a1b947f56.png)
After a little more configuration, you'll be able to select all the [event types](https://docs.slack.dev/reference/events) you want to subscribe to.
Before continuing on to choosing event subscriptions, you will need to choose to use either Socket Mode or an HTTP request URL. For more information on the differences between them, refer to [Exploring HTTP vs Socket Mode](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode).
To set up your app to use Socket Mode, refer to the [Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode) guide. To set up your app to use HTTP request URLs, refer to the [HTTP](https://docs.slack.dev/apis/events-api/using-http-request-urls) guide.
### Choosing event subscriptions[​](https://docs.slack.dev/apis/events-api#event-subscriptions "Direct link to Choosing event subscriptions")
After configuring and validating either Socket Mode or your request URL, it's time to subscribe to the [event types](https://docs.slack.dev/reference/events) you find fascinating, useful, or necessary.
![The event subscription configuration process](https://docs.slack.dev/assets/images/event_subscriptions-2c8b8fb3117ebf7db3a2cb40ef8e2340.png)
The subscription manager is split into two sections:
  * Team Events: these are the events that require a corresponding OAuth scope, and are perspectival to a member installing your application.
  * Bot Events: subscribe to events on behalf of your application's [bot user](https://docs.slack.dev/authentication/tokens#bot), no additional scopes beyond `bot` required. As with workspace events, you'll only receive events perspectival to your bot user.


Some event types are not available in bot user subscriptions.
Consult a specific event's documentation page for information on whether that event is supported for bot users.
### Activating subscriptions[​](https://docs.slack.dev/apis/events-api#activating-subscriptions "Direct link to Activating subscriptions")
The Events API is backed by the same [OAuth permission scoping system](https://docs.slack.dev/authentication/installing-with-oauth) powering your Slack app.
If workspaces have already installed your application, your request URL will soon begin receiving your configured event subscriptions.
For any workspaces that have yet to install your application, you'll need to request the specific OAuth scopes corresponding to the [event types](https://docs.slack.dev/reference/events) you're subscribing to. If you're working on behalf of a [bot user](https://docs.slack.dev/authentication/tokens#bot), you'll need your bot installed the typical way, using the `bot` OAuth scope.
Authorize users for your Event Consumer app through the standard [OAuth flow](https://docs.slack.dev/authentication). Be sure to include all of the necessary scopes for the events your app wants to receive. Consult our index of the [available event types with corresponding OAuth scopes](https://docs.slack.dev/reference/events).
With all this due preparation out of the way, it's time to receive and handle all those event subscriptions.
## Receiving events[​](https://docs.slack.dev/apis/events-api#receiving-events "Direct link to Receiving events")
Your Request URL will receive a request for each event matching your subscriptions. One request, one event.
You may want to consider the number of workspaces you serve, the number of users on those workspaces, their volume of messages, and other activity to evaluate how many requests your Request URL may receive and scale accordingly.
### Events dispatched as JSON[​](https://docs.slack.dev/apis/events-api#events-JSON "Direct link to Events dispatched as JSON")
When an event in your subscription occurs in an authorized user's account, we'll send an HTTP POST request to your Request URL. The event will be in the `Content-Type: application/json` format:
```
{"type":"event_callback","token":"XXYYZZ","team_id":"T123ABC456","api_app_id":"A123ABC456","event":{"type":"name_of_event","event_ts":"1234567890.123456","user":"U123ABC456",    ...},"event_context":"EC123ABC456","event_id":"Ev123ABC456","event_time":1234567890,"authorizations":[{"enterprise_id":"E123ABC456","team_id":"T123ABC456","user_id":"U123ABC456","is_bot":false,"is_enterprise_install":false,}],"is_ext_shared_channel":false,"context_team_id":"T123ABC456","context_enterprise_id":null}
```

The `token` and `api_app_id` fields help you identify the validity and intended destination of the request, respectively.
The `authorized_users` property is an array that contains a set of one or more users who are authorized to view the event. A user can be a bot user or a human user who installed the app. For each user in the `authorized_users` property:
  * the app has a valid, correctly scoped token associated with that user, and
  * the event happened inside a channel that the authorized user was a member of.


The `team_id` property on the event's [outer payload](https://docs.slack.dev/apis/events-api/#events-JSON) will mirror the first element in the `authorized_users` array. If you need a complete list of every authorized user for an event, you can use [apps.event.authorizations.list](https://docs.slack.dev/reference/methods/apps.event.authorizations.list).
The `event` attribute contains a JSON hash for the corresponding [event type](https://docs.slack.dev/reference/events). The event wrapper is an event envelope of sorts, and the event field represents the contents of that envelope. Learn more about [the event wrapper](https://docs.slack.dev/reference/objects/event-object), including its JSON schema.
### Callback field overview[​](https://docs.slack.dev/apis/events-api#callback-field "Direct link to Callback field overview")
Also referred to as the "outer event", or the JSON object containing the event that happened itself:
Field| Type| Description  
---|---|---  
`token`| String| The shared-private callback token that authenticates this callback to the application as having come from Slack. Match this against what you were given when the subscription was created. If it does not match, do not process the event and discard it. Example: `JhjZd2rVax7ZwH7jRYyWjbDl`  
`team_id`| String| The unique identifier for the workspace/team where this event occurred. Example: `T461EG9ZZ`  
`api_app_id`| String| The unique identifier for the application this event is intended for. Your application's ID can be found in the URL of the your application console. If your Request URL manages multiple applications, use this field along with the `token` field to validate and route incoming requests. Example: `A4ZFV49KK`  
`event`| [Event type](https://docs.slack.dev/apis/events-api/#event_type_structure)| Contains the inner set of fields representing the event that's happening. [Examples below.](https://docs.slack.dev/apis/events-api/#event_type_structure)  
`type`| String| This reflects the type of callback you're receiving. Typically, that is `event_callback`. You may encounter `url_verification` during the configuration process. The `event` field's "inner event" will also contain a `type` field indicating which [event type](https://docs.slack.dev/reference/events) lurks within ([below](https://docs.slack.dev/apis/events-api/#event_type_structure)).  
`authorizations`| Object| An installation of your app. Installations are defined by a combination of the installing Enterprise Grid org, workspace, and user (represented by `enterprise_id`, `team_id`, and `user_id` inside this field)—note that installations may only have one or two, not all three, defined. `authorizations` describes _one_ of the installations that this event is visible to. You'll receive a single event for a piece of data intended for multiple users in a workspace, rather than a message per user. Use [`apps.event.authorizations.list`](https://docs.slack.dev/reference/methods/apps.event.authorizations.list) to retrieve additional authorizations.  
`event_context`| String| An identifier for this specific event. This field can be used with the [`apps.event.authorizations.list`](https://docs.slack.dev/reference/methods/apps.event.authorizations.list) method to obtain a full list of installations of your app for which this event is visible.  
`event_id`| String| A unique identifier for this specific event, globally unique across all workspaces.  
`event_time`| Integer| The epoch timestamp in seconds indicating when this event was dispatched.  
### Event type structure[​](https://docs.slack.dev/apis/events-api#event-type-structure "Direct link to Event type structure")
The structure of [event types](https://docs.slack.dev/reference/events) vary from type to type, depending on the kind of action or [object type](https://docs.slack.dev/reference/objects) they represent. The Events API allows you to tolerate minor changes in [event type](https://docs.slack.dev/reference/events) and [object type](https://docs.slack.dev/reference/objects) structures, and to expect additional fields you haven't encountered before or fields that are only conditionally present.
If you're already familiar with the [RTM API](https://docs.slack.dev/legacy/legacy-rtm-api), you'll find that the inner `event` structure is identical to corresponding events, but are wrapped in a kind of event envelope in the callbacks we send to your event Request URL:
Field| Type| Description  
---|---|---  
`type`| String| The specific name of the event described by its adjacent fields. This field is included with every inner event type. Examples: `reaction_added`, `message.channels`, `team_join`  
`event_ts`| String| The timestamp of the event. The combination of `event_ts`,`team_id`, `user_id`, or `channel_id` is intended to be unique. This field is included with every inner event type. Example: `1469470591.759709`  
`user`| String| The user ID belonging to the [user](https://docs.slack.dev/reference/objects/user-object) that incited this action. Not included in all events as not all events are controlled by users. See the top-level callback object's `authed_users` if you need to calculate event visibility by user. Example: `U061F7AUR`  
`ts`| String| The timestamp of what the event describes, which may occur slightly prior to the event being dispatched as described by `event_ts`. The combination of `ts`, `team_id`, `user_id`, or `channel_id` is intended to be unique. Example: `1469470591.759709`  
`item`| String| Data specific to the underlying [object type](https://docs.slack.dev/reference/objects) being described. Often you'll encounter abbreviated versions of full objects. For instance, when [file objects](https://docs.slack.dev/reference/objects/file-object) are referenced, only the file's ID is presented. See each individual [event type](https://docs.slack.dev/reference/events) for more detail.  
If multiple users on one workspace have installed your app and can "see" the same event, we will send _one_ event and include a list of users to whom this event is "visible" in the `authed_users` field.
For example, if a file was uploaded to a channel that two of your authorized users were party to, we would stream the `file_uploaded` event once and indicate both of those users in the `authed_users` array.
Here's a full example of a dispatched event for [reaction_added](https://docs.slack.dev/reference/events/reaction_added):
```
{"token":"z26uFbvR1xHJEdHE1OQiO6t8","team_id":"T123ABC456","api_app_id":"A123ABC456","event":{"type":"reaction_added","user":"U123ABC456","item":{"type":"message","channel":"C123ABC456","ts":"1464196127.000002"},"reaction":"slightly_smiling_face","item_user":"U222222222","event_ts":"1465244570.336841"},"type":"event_callback","authed_users":["U123ABC456"],"authorizations":[{"enterprise_id":"E123ABC456","team_id":"T123ABC456","user_id":"U123ABC456","is_bot":false}],"event_id":"Ev123ABC456","event_context":"EC123ABC456","event_time":1234567890}
```

## Authorizations[​](https://docs.slack.dev/apis/events-api#authorizations "Direct link to Authorizations")
Previously, the Events API included a _full list_ of `authed_users`, and sometimes `authed_teams`, with every event. These fields displayed who the event is visible to. For example, if your app has been installed by two users in a workspace, and the app listens for the [`file_shared`](https://docs.slack.dev/reference/events/file_shared) event, your app might receive an event with `authed_users` containing those two users.
Now, `authed_users` and `authed_teams` [**are deprecated**](https://docs.slack.dev/changelog/2020-09-15-events-api-truncate-authed-users). Events will contain a single, compact `authorizations` field that shows one installation of your app that the event is visible to. In other words, lists of authorizations will be truncated to one element.
Expect a new outer payload on events that looks similar to this one:
```
{"token":"z26uFbvR1xHJEdHE1OQiO6t8","team_id":"T123ABC456","api_app_id":"A123ABC456","event":{"type":"reaction_added","user":"U123ABC456","item":{"type":"message","channel":"C123ABC456","ts":"1464196127.000002"},"reaction":"slightly_smiling_face","item_user":"U123ABC456","event_ts":"1465244570.336841"},"type":"event_callback","authed_users":["U222222222"],"authed_teams":["T123ABC456"],"authorizations":[{"enterprise_id":"E123ABC456","team_id":"T123ABC456","user_id":"U123ABC456","is_bot":false}],"event_context":"EC123ABC456","event_id":"Ev123ABC456","event_time":1234567890}
```

If there's more than one installing party that your app is keeping track of, it's best not to rely on the single party listed in `authorizations` to be any particular one.
To get a _full list_ of who can see events, call the [`apps.event.authorizations.list`](https://docs.slack.dev/reference/methods/apps.event.authorizations.list) method after obtaining an [app-level token](https://docs.slack.dev/authentication/tokens#app). [Read more on the changes here](https://docs.slack.dev/changelog/2020-09-15-events-api-truncate-authed-users); they have taken effect for existing apps as of February 24, 2021.
Not all events provide an `event_context`.
[Read more about the events where `event_context` is not applicable, and view a full list of those events](https://docs.slack.dev/changelog/2020-09-15-events-api-truncate-authed-users#no_context). Newly created apps are _automatically_ opted into the new form of events: a single, truncated `authorizations` field with one authorization shown.
You can also use the [`apps.event.authorizations.list`](https://docs.slack.dev/reference/methods/apps.event.authorizations.list)method immediately, without yet opting in to the event payload changes. These changes allow Slack to increase the performance of the Events API, delivering events faster.
## Responding to events[​](https://docs.slack.dev/apis/events-api#responding "Direct link to Responding to events")
Your app should respond to the event request with an HTTP 2xx _within three seconds_. If it does not, we'll consider the event delivery attempt failed. After a failure, we'll retry three times, backing off exponentially. Some best practices are to:
  * Maintain a response success rate of at least 5% of events per 60 minutes to prevent automatic disabling.
  * Respond to events with an HTTP 200 OK as soon as you can.
  * Avoid actually processing and reacting to events within the same process.
  * Implement a queue to handle inbound events after they are received.


What you do with events depends on what your application or service does.
Maybe it'll trigger you to send a message using [`chat.postMessage`](https://docs.slack.dev/reference/methods/chat.postMessage). Maybe you'll update a leaderboard. Maybe you'll update a piece of data you're storing. Maybe you'll change the world or just decide to do nothing at all.
### Rate limiting[​](https://docs.slack.dev/apis/events-api#rate-limiting "Direct link to Rate limiting")
We don't want to flood your servers with events it can't handle.
Event deliveries currently max out at 30,000 per workspace _per app_ per 60 minutes. If your app would receive more than one workspace's 30,000 events in a 60 minute window, you'll receive [`app_rate_limited`](https://docs.slack.dev/reference/events/app_rate_limited) events describing the conditions every minute.
When rate limited, your Request URL will receive a special app event, [`app_rate_limited`](https://docs.slack.dev/reference/events/app_rate_limited).
```
{"token":"Jhj5dZrVaK7ZwHHjRyZWjbDl","type":"app_rate_limited","team_id":"T123ABC456","minute_rate_limited":1518467820,"api_app_id":"A123ABC456"}
```

**Field guide**
  * `token`: the same shared token used to verify other events in the Events API
  * `type`: this specific event type, `app_rate_limited`
  * `minute_rate_limited`: a rounded epoch time value indicating the minute your application became rate limited for this workspace. `1518467820` is at 2018-02-12 20:37:00 UTC.
  * `team_id`: subscriptions between your app and the workspace with this ID are being rate limited
  * `api_app_id`: your application's ID, especially useful if you have multiple applications working with the Events API


You'll receive these callbacks for each of the minutes you are rate limited for that workspace.
## Error handling[​](https://docs.slack.dev/apis/events-api#error-handling "Direct link to Error handling")
As Slack sends your request URL events, we ask that you return an HTTP 200 OK for each event you successfully receive. You may respond with an HTTP 301 or 302 and we'll follow up to two redirects in our quest for you to provide us an HTTP 200 success code. Respond with success conditions to at least 5% of the events delivered to your app or your app will risk being temporarily disabled.
Once you've repaired your ability to handle events, re-enable subscriptions by visiting Slack app management, selecting your app, and following the prompts. You'll need to go to **Live App Settings** if your app is part of the Slack Marketplace.
### Failure conditions[​](https://docs.slack.dev/apis/events-api#failure "Direct link to Failure conditions")
We consider any of these scenarios a single failure condition:
  * We are unable to negotiate or validate your server's SSL certificate.
  * We wait longer than _3 seconds_ to receive a valid response from your server.
  * We encounter more than 2 HTTP redirects to follow.
  * We receive any other response than an HTTP 200-series response (besides allowed redirects mentioned above).


While we limit the number of failure conditions we'll tolerate over time, we also gracefully retry sending your events according to an exponential backoff strategy.
Maintain a successful response rate of 5% or above to avoid automatic event delivery disabling. Apps receiving less than 1,000 events per hour will not be automatically disabled.
### Retries[​](https://docs.slack.dev/apis/events-api#retries "Direct link to Retries")
We'll knock knock knock on your server's door, retrying a failed request up to _3 times_ in a gradually increasing timetable:
  1. The first retry will be sent nearly immediately.
  2. The second retry will be attempted after 1 minute.
  3. The third and final retry will be sent after 5 minutes.


With each retry attempt, you'll also be given a `x-slack-retry-num` HTTP header indicating the attempt number: `1`, `2`, or `3`. Retries count against the [failure limits](https://docs.slack.dev/apis/events-api#failure_limits) mentioned below.
We'll tell you why we're retrying the request in the `x-slack-retry-reason` HTTP header. These possible values describe their inciting events:
  * `http_timeout`: Your server took longer than 3 seconds to respond to the previous event delivery attempt.
  * `too_many_redirects`: We'll follow you down the rabbit hole of HTTP redirects only so far. If we encounter more than 2, we'll retry the request in hopes it won't be that many this time.
  * `connection_failed`: We just couldn't seem to connect to your server. Maybe we couldn't find it in DNS or maybe your host is unreachable.
  * `ssl_error`: We couldn't verify the veracity of your SSL certificate. Find tips on producing valid SSL certificates [here](https://docs.slack.dev/faq#slash-URL).
  * `http_error`: We encountered an HTTP status code that was not in the HTTP 200 OK range. Maybe the request was forbidden. Or you rate limited _us_. Or the document just could not be found. So we're trying again in case that's all rectified now.
  * `unknown_error`: We didn't anticipate this condition arising, but prepared for it nonetheless. For some reason it didn't work; we don't know why yet.


### Turning retries off[​](https://docs.slack.dev/apis/events-api#retries-off "Direct link to Turning retries off")
If your server is having trouble handling our requests or you'd rather we not retry failed deliveries, provide an HTTP header in your responses indicating that you'd prefer no further attempts. Provide us this HTTP header and value as part of your non-200 OK response:
```
x-slack-no-retry: 1
```

By presenting this header, we'll understand it to mean you'd rather this specific event not be re-delivered. Other event deliveries will remain unaffected.
### Failure limits[​](https://docs.slack.dev/apis/events-api#failure-limits "Direct link to Failure limits")
If you're responding with errors, we won't keep sending events to your servers forever.
When your application enters any combination of these [failure conditions](https://docs.slack.dev/apis/events-api#failure_conditions) for more than _95% of delivery attempts_ within 60 minutes, your application's event subscriptions will be temporarily disabled.
We'll also send you, the Slack app's creator and owner, an email alerting you to the situation. You'll have the opportunity to re-enable deliveries when you're ready.
### Resuming event deliveries[​](https://docs.slack.dev/apis/events-api#resume-event-deliveries "Direct link to Resuming event deliveries")
Manually re-enable event subscriptions by visiting your application's settings. If your app is part of the Slack Marketplace, use your **Live App Settings** instead of your development app.
## Change management[​](https://docs.slack.dev/apis/events-api#change-management "Direct link to Change management")
Inevitably, the status of your subscriptions will change. New workspaces will sign up for your application. Installing users may leave a workspace. Maybe you make some tweaks to your subscriptions or incite users to request a different set of OAuth scopes.
Beyond your app being disabled, there are a few different types of changes that will affect which events your app is receiving.
### App installation[​](https://docs.slack.dev/apis/events-api#installation "Direct link to App installation")
When a user installs your app, you'll immediately begin receiving events for them based on your subscription.
Your application's granted OAuth scopes dictate which events in your subscription you receive.
If you've configured your subscription to receive [`reaction_added`](https://docs.slack.dev/reference/events/reaction_added), [`reaction_removed`](https://docs.slack.dev/reference/events/reaction_removed), and [`file_created`](https://docs.slack.dev/reference/events/file_created) events, you won't receive all three unless you request the `reactions:read` and `files:read` scopes from the user. For example, If you'd only requested `files:read`, you'll only receive [`file_created`](https://docs.slack.dev/reference/events/file_created) events and not [`reaction_added`](https://docs.slack.dev/reference/events/reaction_added) or [`reaction_removed`](https://docs.slack.dev/reference/events/reaction_removed).
### App revocation[​](https://docs.slack.dev/apis/events-api#revocation "Direct link to App revocation")
If a user uninstalls your app (or the tokens issued to your app are revoked), events for that user will immediately stop being sent to your app.
### Modifying events in your subscription[​](https://docs.slack.dev/apis/events-api#modify-events "Direct link to Modifying events in your subscription")
If you modify your subscription through the application management interface, the modifications will _immediately_ take effect.
Depending on the modification, the event types, and OAuth scopes you've been requesting from users, a few different things can happen:
  * **Adding event subscriptions you already have scopes for** : For example, you've been requesting `files:read` from users and decide to add the `file_created` event. Because you already have access to this resource (files), you'll begin receiving `file_created` events as soon as you update your subscription.
  * **Adding event subscriptions you aren't yet scoped for** : For example, you've been requesting `channels:read` from users and decide to add the `file_created` event. Because you _don't_ have access to this resource (files), you won't receive `file_created` events immediately. You must send your existing users through the OAuth flow again, requesting the `files:read` scope. You'll begin to receive `file_created` events for each user _after_ they authorize `files:read` for your app.
  * **Removing event subscriptions, regardless of granted scopes** : Events will immediately stop being sent for all users who have installed your app. Their OAuth scopes and authorizations will not be affected. If you weren't granted the permission scopes for the removed event subscription, then nothing really changes. You weren't receiving those events anyway and you won't be receiving them now either.


## Presence[​](https://docs.slack.dev/apis/events-api#presence "Direct link to Presence")
Bot users using the Events API exclusively must toggle their [presence](https://docs.slack.dev/apis/web-api/user-presence-and-status#bot_presence) status. To toggle your bot user's presence when connected exclusively to the Events API, visit your [app management console](https://api.slack.com/apps)'s **Bot Users** tab.
![Toggling bot user presence for the events API](https://docs.slack.dev/assets/images/events-api-bot-presence-b8d32b4e89d798c86a14ceeb38ed7bc6.png)
Learn more about the [nuances of bot user presence](https://docs.slack.dev/apis/web-api/user-presence-and-status#bot_presence).
## Event types compatible with the Events API[​](https://docs.slack.dev/apis/events-api#compatibility "Direct link to Event types compatible with the Events API")
[Browse all available events here](https://docs.slack.dev/reference/events).
Want to browse the list of events and even some of their properties programmatically? Check out our [AsyncAPI spec for the Events API](https://github.com/slackapi/slack-api-specs).
## Monitoring your app's lifecycle with app events[​](https://docs.slack.dev/apis/events-api#app-events "Direct link to Monitoring your app's lifecycle with app events")
Your application has a life of its own. You build it, cultivate it, maintain it, and improve it. But still, stuff happens to your app in the wild. Tokens get revoked, workspaces accidentally uninstall it, and sometimes teams grow up and become part of a massive [Enterprise Grid](https://docs.slack.dev/enterprise-grid).
Building an integration for Enterprise Grid workspaces? Consult the [Enterprise Grid](https://docs.slack.dev/enterprise-grid) docs for notes on Events API usage and shared channels.
Sophisticated apps want to know what's happening, to situationally respond, tidy up data messes, pause and resume activity, or to help you contemplate the many-folded nuances of building invaluable social software. Your app is interesting, wouldn't you like to subscribe to its newsletter?
Subscriptions to app events require no special OAuth scopes; just subscribe to the events you're interested in and you'll receive them as appropriate for each workspace your app is installed on.
[PreviousUser presence and status](https://docs.slack.dev/apis/web-api/user-presence-and-status)[NextOverview](https://docs.slack.dev/apis/events-api/)
  * [Overview](https://docs.slack.dev/apis/events-api#overview)
  * [Preparing your app to use the Events API](https://docs.slack.dev/apis/events-api#prepare)
    * [Is the Events API right for your app?](https://docs.slack.dev/apis/events-api#your-app)
    * [Permission model](https://docs.slack.dev/apis/events-api#permission-model)
  * [Subscribing to event types](https://docs.slack.dev/apis/events-api#subscribing)
    * [Choosing event subscriptions](https://docs.slack.dev/apis/events-api#event-subscriptions)
    * [Activating subscriptions](https://docs.slack.dev/apis/events-api#activating-subscriptions)
  * [Receiving events](https://docs.slack.dev/apis/events-api#receiving-events)
    * [Events dispatched as JSON](https://docs.slack.dev/apis/events-api#events-JSON)
    * [Callback field overview](https://docs.slack.dev/apis/events-api#callback-field)
    * [Event type structure](https://docs.slack.dev/apis/events-api#event-type-structure)
  * [Authorizations](https://docs.slack.dev/apis/events-api#authorizations)
  * [Responding to events](https://docs.slack.dev/apis/events-api#responding)
    * [Rate limiting](https://docs.slack.dev/apis/events-api#rate-limiting)
  * [Error handling](https://docs.slack.dev/apis/events-api#error-handling)
    * [Failure conditions](https://docs.slack.dev/apis/events-api#failure)
    * [Retries](https://docs.slack.dev/apis/events-api#retries)
    * [Turning retries off](https://docs.slack.dev/apis/events-api#retries-off)
    * [Failure limits](https://docs.slack.dev/apis/events-api#failure-limits)
    * [Resuming event deliveries](https://docs.slack.dev/apis/events-api#resume-event-deliveries)
  * [Change management](https://docs.slack.dev/apis/events-api#change-management)
    * [App installation](https://docs.slack.dev/apis/events-api#installation)
    * [App revocation](https://docs.slack.dev/apis/events-api#revocation)
    * [Modifying events in your subscription](https://docs.slack.dev/apis/events-api#modify-events)
  * [Presence](https://docs.slack.dev/apis/events-api#presence)
  * [Event types compatible with the Events API](https://docs.slack.dev/apis/events-api#compatibility)
  * [Monitoring your app's lifecycle with app events](https://docs.slack.dev/apis/events-api#app-events)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



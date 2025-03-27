---
url: https://docs.slack.dev/apis/slack-connect
session_id: slack_api_docs
updated_dt: 2025-03-27T13:25:02.247495
---
[Skip to main content](https://docs.slack.dev/apis/slack-connect#__docusaurus_skipToContent_fallback)
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
    * [Slack Connect](https://docs.slack.dev/apis/slack-connect/)
      * [Overview](https://docs.slack.dev/apis/slack-connect/)
      * [Using Slack Connect API methods](https://docs.slack.dev/apis/slack-connect/using-slack-connect-api-methods)
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
  * Slack Connect


On this page
# Understanding Slack Connect
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
![Shared Channels allows you to collaborate with an external org!](https://docs.slack.dev/assets/images/shared_channel_head-8530ef437bf14723e6f38b35eaaf7c9f.png)
With Slack Connect, channels connect you to people working at other companies and organizations.
The [Conversation APIs](https://docs.slack.dev/apis/web-api/using-the-conversations-api) manages most of the complexity for you. While many apps, bots, and other integrations should continue to work with channels that have members from multiple workspaces and organizations, [you may face unexpected quirks](https://docs.slack.dev/apis/slack-connect#what_to_expect).
If you'd like to directly manage Slack Connect for your organization using an app, check out our documentation on the [Slack Connect APIs](https://docs.slack.dev/apis/slack-connect/using-slack-connect-api-methods). Otherwise, read on to learn how to ensure your app handles Slack Connect gracefully.
## What is Slack Connect?[​](https://docs.slack.dev/apis/slack-connect#about "Direct link to What is Slack Connect?")
In Slack Connect, a channel is a bridge between teams that need to work together. Teams use Slack Connect to communicate between workspaces and organizations. Slack Connect allows users of different organizations to chat, share files, and use apps in the same way they communicate with their more immediate colleagues in their own workspace.
## How channels between organizations work[​](https://docs.slack.dev/apis/slack-connect#how_shared_channels_work "Direct link to How channels between organizations work")
### Messages and files[​](https://docs.slack.dev/apis/slack-connect#messages-files "Direct link to Messages and files")
All workspaces involved in a connected channel can read and send messages, share files, and access the history of shared channels.
### Channel settings[​](https://docs.slack.dev/apis/slack-connect#channel-settings "Direct link to Channel settings")
A connected channel may have different settings for each workspace it's party to.
  * Channel names may differ. What's one workspace's `#do-stuff` is another workspace's `#do-nothing`. It's best to make no assumptions about channel names and stick only with IDs.
  * One workspace might set the channel as private, while the other workspace may set the same channel as public.
  * Data retention settings may differ between teams.


With all these differences in channel type settings, you **must** use the new [Conversations API](https://docs.slack.dev/apis/web-api/using-the-conversations-api) instead of existing APIs such as `channels.*`, `ims.*``, and `groups.*`.
## Technical considerations[​](https://docs.slack.dev/apis/slack-connect#technical-considerations "Direct link to Technical considerations")
Be on the lookout for minor differences in channel, message, user, team and related objects. When a channel can hold multiple teams within it, you'll naturally encounter messages and users originating from other teams.
### Detecting when a channel has members from multiple workspaces or organizations[​](https://docs.slack.dev/apis/slack-connect#detecting "Direct link to Detecting when a channel has members from multiple workspaces or organizations")
Your app can learn when channels become shared and unshared with another team by subscribing to the [`channel_shared`](https://docs.slack.dev/reference/events/channel_shared) and [`channel_unshared`](https://docs.slack.dev/reference/events/channel_unshared) events in the **Event Subscriptions** tab in your **Apps** page.
To receive all shared events for channels or groups in a workspace, your app will need the `channels:read` or `groups:read` scopes respectively. To receive only shared events for channels and groups your bot user is in, your app just needs the `bot` scope.
Both shared events contain the ID of the channel itself, in addition to the team that the channel was shared or unshared with as follows:
```
{"type":"channel_shared","connected_team_id":"T123ABC456","channel":"C123ABC456","event_ts":"1565722340.000000"}
```

It may be helpful for your app to note the `connected_team_id`, as it will begin receiving messages and events from users on that external team.
### External members[​](https://docs.slack.dev/apis/slack-connect#members "Direct link to External members")
Your app will receive messages and events from users on external teams. Information about these users will be different than users on the workspace where your app is installed.
![A stranger in shared channels](https://docs.slack.dev/assets/images/shared_channels_stranger-8fb15fe530388754b4694894f8fdbb42.png)
_An external member. In their profile, a member from an external team will be marked with a square status indicator next to the username._
  * **External members** are members on the other team that your application shares channel membership with.
  * **Strangers** are external members on the other team that your application does _not_ have a shared channel in common; you can find out about these members when the other team mentions them in the shared channel or shares one of their messages or files in the shared channel.


The user type object (returned by methods such as [`users.info`](https://docs.slack.dev/reference/methods/users.info)) provides additional information to identify external members, while withholding some information your app may expect. External members are also returned in the [`conversations.members`](https://docs.slack.dev/reference/methods/conversations.members) API response.
  * If the user is a stranger who isn't in any shared channels, the `is_stranger` flag is set `true`.
  * Both the [`users:read.email`](/reference/scopes/users.read.email and [`users:read`](https://docs.slack.dev/reference/scopes/users.read) OAuth scopes are required to access the `email` field in [user objects](https://docs.slack.dev/reference/objects/user-object) returned by the [`users.info`](https://docs.slack.dev/reference/methods/users.info) and [`users.list`](https://docs.slack.dev/reference/methods/users.list) API methods. [Learn more](https://docs.slack.dev/changelog/2017-04-narrowing-email-access).
  * For external members and strangers, their profile data will not contain any locale information, even if you pass the `include_locale` flag.


Here's an example of a response from [`users.info`](https://docs.slack.dev/reference/methods/users.info):
```
{"ok":true,"user":{"id":"U123ABC456","team_id":"T123ABC456","name":"rex","real_name":"Devon Rex","profile":{"image_24":"https:\/\/.../11662770033.jpg","team":"T123ABC456","display_name":"eshellstrop"// all that other stuff},"is_stranger":true}}
```

When you specify a user, you need to use a user's `id` instead of their `username`. With the new [name-tagging](https://docs.slack.dev/changelog/2017-09-the-one-about-usernames) feature, the `username` attribute cannot be relied upon as a unique identifier, and will not work with "foreign" users via the API. For example, you cannot use [`chat.postMessage`](https://docs.slack.dev/reference/methods/chat.postMessage) with a `username` set to a foreign user.
A bot user is able to DM users on all connected workspaces, as long as users are in a shared channel together.
### Same channel, different setting[​](https://docs.slack.dev/apis/slack-connect#same-channel "Direct link to Same channel, different setting")
When a channel gains members from another workspace or organization via Slack Connect, the channel ID may change depending on its setting.
If the channel is set to private, the ID prefix may change from `G` to `C` (e.g. `G1234567890` becomes `C1234567890`) when it's shared. Subscribe to the [`channel_id_changed`](https://docs.slack.dev/reference/events/channel_id_changed) event to determine when a private channel's ID has changed because a share has been initiated.
Since each team in the channel can independently decide whether the channel is public or private on their end, there are some changes with the APIs too:
  * The `conversations.*` methods accept any type of channel.
  * The channel type object now includes the channel type info (public, private, and so forth).
  * The [`conversations.info`](https://docs.slack.dev/reference/methods/conversations.info) method will provide additional information on the workspaces connected to the shared channel and the ID of the host workspace.


The channel type object (returned by methods such as [`conversations.info`](https://docs.slack.dev/reference/methods/conversations.info)) tells you additional channel information. If the channel is shared externally (i.e. not just between multiple workspaces in your Grid organization), `is_ext_shared` is set to true. If it is a private channel or a group DM channel, the properties `is_private` or `is_mpim` are set to `true`, respectively.
Use the `is_ext_shared`, `is_private`, and `is_mpim` flags _exclusively_ to determine the privacy and type of a given channel.
Beware of `is_shared`, which also includes channels shared between multiple workspaces in the same organization.
Example response from `conversations.list`:
```
{"ok":true,"channels":[{"id":"C123ABC456","name":"product-qa","is_channel":true,"created":1491332036,"creator":"U123ABC456","is_archived":false,"is_general":false,"is_shared":true,"is_ext_shared":true,"is_org_shared":false,"is_member":false,"is_private":true,"is_mpim":false,"members":["U123ABC456","U222222222"],       ...},{ ... },]}
```

### Channels between organizations that are converted back to a single-organization channel[​](https://docs.slack.dev/apis/slack-connect#channels-between-orgs "Direct link to Channels between organizations that are converted back to a single-organization channel")
When a channel between organizations or workspaces is unshared by the host workspace, each workspace can still access channel history for all previous messages and activity. However, the channel in the disconnected workspace will be assigned a new ID, while the host workspace keeps the original channel ID.
### Private channels between organizations[​](https://docs.slack.dev/apis/slack-connect#private_channels "Direct link to Private channels between organizations")
Channels between organizations and workspaces can be made private on a per-workspace basis. For instance, a public channel on one workspace can be shared with a private channel on another workspace. Use the [Conversations API](https://docs.slack.dev/apis/web-api/using-the-conversations-api) methods to work with the channels and to accurately determine their privacy.
When a workspace's private shared channel becomes unshared, its channel ID remains `C`-prefixed (_i.e._ `C1234567890` does _not_ change back to `G1234567890`) although the channel is still private—making channel prefix an unreliable indicator in determining privacy.
## Design considerations[​](https://docs.slack.dev/apis/slack-connect#design-considerations "Direct link to Design considerations")
The most important technical requirement for supporting Slack Connect is that you must use the [Conversations API](https://docs.slack.dev/apis/web-api/using-the-conversations-api) to properly interact with channels that have been shared.
Next, we'll talk about design considerations for your app as it supports Slack Connect. Here's a quick set of questions to ask about your app before you should consider it compatible with Slack Connect:
  1. Does your app provide access to sensitive, internal data? You must ask for confirmation before sharing this information to an external partner.
  2. Does your app have a slash command, shortcut, or message action? Be prepared to share an explanatory message about how this action can only be invoked by users from the workspace that installed the app.
  3. Does your app have interactive elements? Consider who should be able to interact with those elements (such as buttons and dropdown menus). Check that the originating user is part of the `authorized_users` property in the interaction payload to ensure they're part of the installing authorization.


Test your app thoroughly before you describe it as compatible with Slack Connect.
If your app doesn't behave as expected, especially if it shares sensitive data to external parties, you may lose user trust, and you'll likely have your app uninstalled.
## Behavior to expect[​](https://docs.slack.dev/apis/slack-connect#what_to_expect "Direct link to Behavior to expect")
An app compatible with Slack Connect needs to account for authorization and installation differences among workspaces where it's installed. If your app is installed on a workspace that shares a channel with another workspace, your app could be authorized in one workspace but not authorized in the other. Likewise, an app that can be installed into multiple workspaces will need to implement functionality that understands which workspace to operate in and to receive information from.
The following are additional guidelines to consider while building an app that can exist across channels and workspaces:
### Channels don't belong to a single workspace[​](https://docs.slack.dev/apis/slack-connect#channels "Direct link to Channels don't belong to a single workspace")
A shared channel doesn't belong to a single workspace. If you need to look up a token or user to respond to an event, look at the `authorized_users` property.
The `authorized_users` property is an array that contains a set of one or more users who are authorized to view the event. A user can be a bot user or a human user who installed the app. For each user in the `authorized_users` property:
  * the app has a valid, correctly scoped token associated with that user, and
  * the event happened inside a channel that the authorized user was a member of.


The `team_id` property on the event's [outer payload](https://docs.slack.dev/apis/events-api/#events-JSON) will mirror the first element in the `authorized_users` array. If you need a complete list of every authorized user for an event, you can use [apps.event.authorizations.list](https://docs.slack.dev/reference/methods/apps.event.authorizations.list).
### Beware sharing users' data[​](https://docs.slack.dev/apis/slack-connect#data "Direct link to Beware sharing users' data")
As a rule of thumb, your app should default to exposing less information in shared channels to protect your users' data.
Bot users are accessible to all users on the workspace where your app is installed, and any external members in a channel between organizations where your bot is also present.
When an external member messages you, the [event payload](https://docs.slack.dev/apis/events-api/#events-JSON) will contain a `team_id` property that indicates the workspace where the message came from. This property is identical to the first element of the `authorized_users` property, which is a set of one or more bot users or human users who installed the app. These users are authorized to see the event.
If your app typically shares sensitive information, make sure to change its behavior for external members.
### Slash commands are not shared[​](https://docs.slack.dev/apis/slack-connect#slash "Direct link to Slash commands are not shared")
Slash commands and message actions are _not_ shared — they are limited only to the team that has installed the app to their team workspace.
Another team must install the app independently in order to be able to use them.
When your app is initiated by a slash command or message action, only the team that installed your app can invoke it, but external members can still see any information posted into channel as a result. For example, let's say _Catnip inc._ has installed a polling app that is initiated with a command `/poll`. Users in the _Catnip inc._ can initiate a poll, while _Woof inc._ can only vote on the poll, and cannot create a new poll.
### App unfurls may surprise you[​](https://docs.slack.dev/apis/slack-connect#unfurls "Direct link to App unfurls may surprise you")
[`link_shared`](https://docs.slack.dev/reference/events/link_shared) events are **not** delivered when an _external_ member shares a link that matches your app's unfurling domain, unless the app is installed in their workspace.
### Not all workspaces support Slack Connect[​](https://docs.slack.dev/apis/slack-connect#notall "Direct link to Not all workspaces support Slack Connect")
Slack Connect channels are not available to all free workspaces. If your app builds with the assumption that a workspace or organization uses Slack Connect, it may not be available to all end users and workspaces.
### More than one workspace may be connected[​](https://docs.slack.dev/apis/slack-connect#multiple_workspaces "Direct link to More than one workspace may be connected")
Slack Connect channels can connect up to 250 organizations.
### You may have multiple bot copies[​](https://docs.slack.dev/apis/slack-connect#multiple_apps "Direct link to You may have multiple bot copies")
If your app is installed on multiple workspaces that share a Slack Connect channel, you may have multiple app homes and multiple bot copies. Right now, we don't distinguish that a given app “belongs” to a particular workspace.
### Beware of changing IDs on channels when a share is initiated[​](https://docs.slack.dev/apis/slack-connect#id_changes "Direct link to Beware of changing IDs on channels when a share is initiated")
The moment a channel share is _initiated_ , `G`-encoded private channels will have their ID immediately changed to be `C`-encoded—**even if the channel is never successfully shared** with an external org.
You'll want to subscribe to the new [`channel_id_changed`](https://docs.slack.dev/reference/events/channel_id_changed) event, which marks when a private channel's ID has changed due to being shared:
```
  "event": {   "type": "channel_id_changed",   "old_channel_id": "G123ABC456",   "new_channel_id": "C123ABC456",   "event_ts": "1612206778.000000"  }
```

### Beware of frozen and disconnected channels[​](https://docs.slack.dev/apis/slack-connect#frozen "Direct link to Beware of frozen and disconnected channels")
A conversation can be archived and _frozen_ when an organization is disconnected from another with Slack Connect.
You may see a `"frozen_reason": "connection_severed"` in a Conversation object returned from the [Conversations API](https://docs.slack.dev/apis/web-api/using-the-conversations-api). The ID of a disconnected channel will change if your organization was invited to share it—i.e., your organization is not the host. The host organization retains the original channel and original ID, while the invited organization get a copy of the channel that is assigned a new ID.
Your app will receive a `channel_not_found` error if you try to query the API with the original channel ID.
### There's currently no way to find all channels shared with a specific external organization[​](https://docs.slack.dev/apis/slack-connect#find_all "Direct link to There's currently no way to find all channels shared with a specific external organization")
Unfortunately, the [`conversations.list`](https://docs.slack.dev/reference/methods/conversations.list) method does not include `connected_team_ids`.
### Beware of `is_shared`[​](https://docs.slack.dev/apis/slack-connect#is_shared "Direct link to is_shared")
The property `is_shared` on a [conversation object](https://docs.slack.dev/reference/objects/conversation-object) means the channel is shared with one or more workspaces. But beware: these can be internal workspaces (as with multi-workspace channels in Enterprise Grid) or external workspaces (as with Slack Connect).
Look for `is_ext_shared` and `is_org_shared` to learn which kind of shared channel you're viewing.
### Determining whether a user is external must be done implicitly[​](https://docs.slack.dev/apis/slack-connect#external "Direct link to Determining whether a user is external must be done implicitly")
Look for the `is_stranger` field in [`user` objects](https://docs.slack.dev/reference/objects/user-object). If it's `true`, your app does not share a channel with the user. If it's `false`, but the `team` associated with the user is not the installing team for your app, the user is external and your app **does** share a channel with them.
In other words, there is no single property to substantiate if the user is external or not: you must deduce it from a combination of the `is_stranger` and the `team_id` property.
### Additional check required to access file info (`check_file_info`)[​](https://docs.slack.dev/apis/slack-connect#check_file_info "Direct link to check_file_info")
When uploaded into a Slack Connect channel, [file object](https://docs.slack.dev/reference/objects/file-object) properties are not immediately accessible to apps listening via the Events API or RTM API. Instead, the payload will contain a file object with the key-value pair `"file_access": "check_file_info"` meaning that further action is required from your app in order to view an uploaded file's metadata.
```
"files":[{"id":"F123ABC456","mode":"file_access","file_access":"check_file_info","created":0,"timestamp":0,"user":""}]
```

This behavior is only observed for files uploaded into Slack Connect channels and occurs regardless of which workspace the uploader is a member of. Files uploaded into local conversations that send events to your app will contain the full file object. That said, expect this behavior even in local channels if the file was first uploaded into a Slack Connect channel before being shared to a local channel.
When your app is presented with the instruction to check file info, you should make a request to [`files.info`](https://docs.slack.dev/reference/methods/files.info) if you need to access the full file object.
When accessing conversation files and messages using [`conversations.history`](https://docs.slack.dev/reference/methods/conversations.history) or [`conversations.replies`](https://docs.slack.dev/reference/methods/conversations.replies), full file objects are returned. Similarly, listing files with [`files.list`](https://docs.slack.dev/reference/methods/files.list), using the [Discovery API](https://slack.com/help/articles/360002079527), or [exporting your workspace data](https://slack.com/help/articles/201658943) will also always return full file objects.
It is only when file events are pushed to your app that you will need an additional API call to view a file's properties.
## Support strategies by feature[​](https://docs.slack.dev/apis/slack-connect#support_strategies "Direct link to Support strategies by feature")
Events API
  * Support events originated from external users in shared channels.
  * No duplicated event triggering between shared channels.
  * To see which teams the event is delivered, look for the values of the `authed_teams` property for the response.


Web API
  * Support external users in shared channels. Some user-related actions will not be permissible due to their external nature.
  * Use `users.info` to retrieve additional information on cross-team user ID not found in `users.list`.


Incoming webhooks
  * Messages from incoming webhooks are visible to all members of a shared channel.
  * Incoming webhooks can send DMs only to users on installed teams.


Slash commands
  * Slash commands can be only invoked by users belonging to the workspace your app is installed. Turn on entity resolution for mentioned users allowing you to identity them by id, including on foreign teams.


Message actions
  * Message actions can only be invoked by users belonging to the workspace your app is installed.


Interactive messages
  * Handle action invocation by users from other teams, and let them know if an action is not permissible due to their external nature.


Unfurls
  * When a user on the installing workspace posts a link in the shared channel, the link should be unfurled for the entire channel unless there is a privacy concern.


RTM
  * Support users from other workspace in shared channels where appropriate.
  * *Message deliveries are duplicated in shared channels when installed on multiple joined workspaces due to the multiple socket connections.


Bot users 🤖
  * Bot users can DM all local users in the workspace they are installed in and external users with a common shared channel.


## Conversations API[​](https://docs.slack.dev/apis/slack-connect#conversations-api "Direct link to Conversations API")
Developing with channels between organizations and workspaces requires using the new Web API methods from the [Conversations API](https://docs.slack.dev/apis/web-api/using-the-conversations-api).
## Requesting a sandbox[​](https://docs.slack.dev/apis/slack-connect#sandbox "Direct link to Requesting a sandbox")
Building properly for channels between workspaces and organizations requires experiencing the unique constraints and opportunities yourself. If you don't already have access to workspaces with the proper plan level to grant access to channels between organizations, please complete the form below to request a sandbox.
[Request a sandbox](https://docs.google.com/forms/d/e/1FAIpQLSe9tIHOq1bZVq5xlzymvPGFbqsv2aLFgg04SOi5KfzKbJYBAA/viewform)
## Troubleshooting and known issues[​](https://docs.slack.dev/apis/slack-connect#known_issues "Direct link to Troubleshooting and known issues")
We're still working on Slack Connect. It's likely you'll run into a bug or two. The following are some that we know about.
#### 🚧 MPIM events tell little lies about channel types[​](https://docs.slack.dev/apis/slack-connect#-mpim-events-tell-little-lies-about-channel-types "Direct link to 🚧 MPIM events tell little lies about channel types")
In a multiparty direct message channel ("MPIM") with a foreign user, events like [`member_joined_channel`](https://docs.slack.dev/reference/events/member_joined_channel) and [`member_left_channel`](https://docs.slack.dev/reference/events/member_left_channel) may dispatch an incorrect value for `channel_type`.
#### 🚧 IM Object format is not yet consistent[​](https://docs.slack.dev/apis/slack-connect#-im-object-format-is-not-yet-consistent "Direct link to 🚧 IM Object format is not yet consistent")
IM formats may differ from other channel objects for a while. We're working towards making all objects the same format.
#### 🚧 Select menus may be inconsistent[​](https://docs.slack.dev/apis/slack-connect#-select-menus-may-be-inconsistent "Direct link to 🚧 Select menus may be inconsistent")
Default select menus ([`users_select`](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#users_select), [`conversations_select`](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#conversations_select), and [`channels_select`](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#channels_select)) may display unexpected options in shared channels.
[PreviousUsing Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode)[NextOverview](https://docs.slack.dev/apis/slack-connect/)
  * [What is Slack Connect?](https://docs.slack.dev/apis/slack-connect#about)
  * [How channels between organizations work](https://docs.slack.dev/apis/slack-connect#how_shared_channels_work)
    * [Messages and files](https://docs.slack.dev/apis/slack-connect#messages-files)
    * [Channel settings](https://docs.slack.dev/apis/slack-connect#channel-settings)
  * [Technical considerations](https://docs.slack.dev/apis/slack-connect#technical-considerations)
    * [Detecting when a channel has members from multiple workspaces or organizations](https://docs.slack.dev/apis/slack-connect#detecting)
    * [External members](https://docs.slack.dev/apis/slack-connect#members)
    * [Same channel, different setting](https://docs.slack.dev/apis/slack-connect#same-channel)
    * [Channels between organizations that are converted back to a single-organization channel](https://docs.slack.dev/apis/slack-connect#channels-between-orgs)
    * [Private channels between organizations](https://docs.slack.dev/apis/slack-connect#private_channels)
  * [Design considerations](https://docs.slack.dev/apis/slack-connect#design-considerations)
  * [Behavior to expect](https://docs.slack.dev/apis/slack-connect#what_to_expect)
    * [Channels don't belong to a single workspace](https://docs.slack.dev/apis/slack-connect#channels)
    * [Beware sharing users' data](https://docs.slack.dev/apis/slack-connect#data)
    * [Slash commands are not shared](https://docs.slack.dev/apis/slack-connect#slash)
    * [App unfurls may surprise you](https://docs.slack.dev/apis/slack-connect#unfurls)
    * [Not all workspaces support Slack Connect](https://docs.slack.dev/apis/slack-connect#notall)
    * [More than one workspace may be connected](https://docs.slack.dev/apis/slack-connect#multiple_workspaces)
    * [You may have multiple bot copies](https://docs.slack.dev/apis/slack-connect#multiple_apps)
    * [Beware of changing IDs on channels when a share is initiated](https://docs.slack.dev/apis/slack-connect#id_changes)
    * [Beware of frozen and disconnected channels](https://docs.slack.dev/apis/slack-connect#frozen)
    * [There's currently no way to find all channels shared with a specific external organization](https://docs.slack.dev/apis/slack-connect#find_all)
    * [Beware of `is_shared`](https://docs.slack.dev/apis/slack-connect#is_shared)
    * [Determining whether a user is external must be done implicitly](https://docs.slack.dev/apis/slack-connect#external)
    * [Additional check required to access file info (`check_file_info`)](https://docs.slack.dev/apis/slack-connect#check_file_info)
  * [Support strategies by feature](https://docs.slack.dev/apis/slack-connect#support_strategies)
  * [Conversations API](https://docs.slack.dev/apis/slack-connect#conversations-api)
  * [Requesting a sandbox](https://docs.slack.dev/apis/slack-connect#sandbox)
  * [Troubleshooting and known issues](https://docs.slack.dev/apis/slack-connect#known_issues)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



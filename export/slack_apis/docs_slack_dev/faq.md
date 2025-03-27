---
url: https://docs.slack.dev/faq
session_id: slack_api_docs
updated_dt: 2025-03-27T13:25:40.068277
---
[Skip to main content](https://docs.slack.dev/faq#__docusaurus_skipToContent_fallback)
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


  * [](https://docs.slack.dev/)
  * FAQ


On this page
# Slack developer FAQ
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
We know there's a lot to learn and read about all the integration points of the Slack platform. Here is a little more information you might find helpful!
## General[​](https://docs.slack.dev/faq#general "Direct link to General")
### How do I build a bot using Slack APIs?[​](https://docs.slack.dev/faq#bot-APIs "Direct link to How do I build a bot using Slack APIs?")
We have a [quickstart](https://docs.slack.dev/quickstart) guide that will walk you through the process!
### How do I set up a developer environment to build a Slack app?[​](https://docs.slack.dev/faq#set-up-dev-environment "Direct link to How do I set up a developer environment to build a Slack app?")
You can provision sandbox environments by joining the [Slack Developer Program](https://api.slack.com/developer-program). Once you're ready to deploy your app, distributing the app will allow you to install it in other workspaces.
Start by [building a Slack app](https://docs.slack.dev/quickstart) to contain all of your work—by default, it can only be installed on your own workspace. Follow the instructions in the UI to add features—most require that you provide a HTTP server Slack can reach.
Have more questions? Check out our [developer sandbox FAQs](https://docs.slack.dev/tools/developer-sandboxes#faqs)!
### Is Slack down?[​](https://docs.slack.dev/faq#downtime "Direct link to Is Slack down?")
Of course we want Slack to be fully functional for users and developers at all times. Here are some tips in the unfortunate event you're having trouble and need to determine the cause of a Slack-related issue.
When possible, we report current status promptly on [status.slack.com](https://status.slack.com/) with any service disruption advisories, but you can also use the following methods:
  * Use the [Slack Status API](https://docs.slack.dev/reference/slack-status-api).
  * Send a HTTP GET request to the [`https://slack.com/api/api.test`](https://docs.slack.dev/reference/methods/api.test) API method. A HTTP 200 `application/json` response of `{"ok":true}` indicates at least part of the Slack [Web API](https://docs.slack.dev/apis/web-api/) is available.
  * Send a more complex, [authenticated](https://docs.slack.dev/authentication) request to [`https://slack.com/api/auth.test`](https://docs.slack.dev/reference/methods/auth.test) using a bot, user, or legacy [token](https://docs.slack.dev/authentication/tokens). Using this method exercises the authorization and API layer further than `api.test` and may grant you the serenity of greater confidence in Slack availability.
  * If using the legacy [Real Time Messaging (RTM) API](https://docs.slack.dev/legacy/legacy-rtm-api), try using [`rtm.connect`](https://docs.slack.dev/reference/methods/rtm.connect) to generate a WebSocket URL using a token with the proper permissions, then open the socket using a tool like [this browser-based WebSocket client for Google Chrome](https://chrome.google.com/webstore/detail/simple-websocket-client/pfdhoblngboilpfeibdedpjgfnlcodoo?hl=en).


Still unsure if Slack is down? Contact our enthusiastic [support team](https://my.slack.com/help/requests/new).
### How do I integrate a third-party service with Slack?[​](https://docs.slack.dev/faq#third-party-services "Direct link to How do I integrate a third-party service with Slack?")
Check whether there is an app for a third-party service in the Slack Marketplace. If all else fails, you'll need to [code one for yourself](https://docs.slack.dev/quickstart).
You can also add [connector functions](https://tools.slack.dev/deno-slack-sdk/reference/connector-functions) to your automations workflows. A growing library of third-party services are available.
### Workflow apps vs. non-workflow apps[​](https://docs.slack.dev/faq#workflow-apps "Direct link to Workflow apps vs. non-workflow apps")
Building a non-workflow Slack app? Start [here](https://docs.slack.dev/quickstart). Building a workflow for automations? Start [here](https://docs.slack.dev/workflows). For more about workflow apps, jump to [this section](https://docs.slack.dev/faq#automations-workflow-apps).
## Authentication[​](https://docs.slack.dev/faq#authentication "Direct link to Authentication")
### How do I authenticate my requests to Slack?[​](https://docs.slack.dev/faq#authenticate-me "Direct link to How do I authenticate my requests to Slack?")
#### By token[​](https://docs.slack.dev/faq#by-token "Direct link to By token")
When working with Slack apps or the [Web API](https://docs.slack.dev/apis/web-api/), you'll often need to send access tokens, also known as bearer tokens, along with inbound requests within the authorization header. When creating an app for the first time, you'll be given your own user and bot token while going through the app creation process. In order to obtain other users' tokens, you'll need to send users through the [OAuth 2.0 authentication flow](https://docs.slack.dev/authentication). When you're working with Slack apps, you'll be awarded access tokens after a user approves your application.
#### By private URL[​](https://docs.slack.dev/faq#by-URL "Direct link to By private URL")
Your [incoming webhook](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks) URLs are unique to your integration or application and do not require token-based authentication. [Slash command response URLs](https://docs.slack.dev/interactivity/implementing-slash-commands#responding_to_a_command) also already encode your integration's or application's identity.
### How do I authenticate requests from Slack to me?[​](https://docs.slack.dev/faq#authenticate-slack "Direct link to How do I authenticate requests from Slack to me?")
Use the [signing secret](https://docs.slack.dev/authentication/verifying-requests-from-slack) to compute a signature, and verify that the signature on the request matches. This process is _strongly_ preferred over the use of deprecated verification tokens.
You can also use [Mutual TLS](https://docs.slack.dev/authentication/verifying-requests-from-slack#mutual_tls). Mutual TLS verifies the identity of Slack in a TLS-terminating server, before a request reaches your application code.
### How does Slack authenticate its requests to my servers?[​](https://docs.slack.dev/faq#authenticate-servers "Direct link to How does Slack authenticate its requests to my servers?")
When you configure [Slash commands](https://docs.slack.dev/interactivity/implementing-slash-commands), you specify a URL for Slack to send requests to when qualifying conditions are met. Slack also provides you a token related to that integration.
Slack sends that URL a JSON payload containing a `token` field. Compare that field to values you've received from Slack. Refer to [validating slash commands](https://docs.slack.dev/interactivity/implementing-slash-commands#validating_the_command) for more information.
### When do authorization codes expire?[​](https://docs.slack.dev/faq#authenticate-expire "Direct link to When do authorization codes expire?")
Authorization codes must be exchanged for an access token within 10 minutes by calling the [oauth.access](https://docs.slack.dev/reference/methods/oauth.access) API method as part of the [authorization flow](https://docs.slack.dev/authentication). Otherwise, the authorization code will expire, and you'll need to ask the user to go through the OAuth flow again.
### How do I revoke a token?[​](https://docs.slack.dev/faq#revoke-token "Direct link to How do I revoke a token?")
Use the [`apps.uninstall`](https://docs.slack.dev/reference/methods/apps.uninstall) API method to uninstall an app completely, revoking all tokens. If you want to dispose of a single OAuth access token, use the [`auth.revoke`](https://docs.slack.dev/reference/methods/auth.revoke) API method; it works with tokens from [Sign in with Slack](https://docs.slack.dev/authentication/sign-in-with-slack/) as well as from [Add to Slack](https://docs.slack.dev/legacy/legacy-slack-button).
For classic apps, revoking the last token associated between your application and a workspace effectively uninstalls the app for that workspace.
Members and administrators can remove your app through their [workspace administration interface](https://my.slack.com/apps/manage).
Though it's somewhat of a nuclear option, you also have the ability to revoke all tokens from your [developer dashboard](https://api.slack.com/apps) by selecting your application and clicking **Revoke all tokens**.
### How do I reset my client secret?[​](https://docs.slack.dev/faq#client-secret "Direct link to How do I reset my client secret?")
To reset your client secret, go to your [developer dashboard](https://api.slack.com/apps), select the application, and click the **Change secret** button.
Don't forget to use your new secret when exchanging authorization codes for access tokens while authorizing users and workspaces with [OAuth 2.0](https://docs.slack.dev/authentication).
## Slash commands[​](https://docs.slack.dev/faq#slash-commands "Direct link to Slash commands")
### Why does Slack never reach my slash command URL?[​](https://docs.slack.dev/faq#slash-URL "Direct link to Why does Slack never reach my slash command URL?")
Typically, if Slack cannot reach your slash command URL it's because it's inaccessible, does not have a valid or verifiable SSL certificate, or our request is timing out for some reason.
Slack invokes slash command URLs from its servers rather than from a Slack client app like Slack for Mac. This means that the URL we're trying to reach must be accessible to Slack's servers.
To determine whether your certificate is valid, consider using [this tool](https://www.ssllabs.com/ssltest/index.html) provided by SSL Labs.
### How do I validate a slash command's origin?[​](https://docs.slack.dev/faq#slash-origin "Direct link to How do I validate a slash command's origin?")
Keep track of the validation tokens and team IDs Slack gives you when commands are created and teams approve your app. Always validate that the `token` field in an incoming slash command request has been issued to you by Slack, and scope your data for that workspace.
## Incoming webhooks[​](https://docs.slack.dev/faq#incoming-webhooks "Direct link to Incoming webhooks")
### Why can't I override the channel, icon, or user name of my incoming webhook?[​](https://docs.slack.dev/faq#override "Direct link to Why can't I override the channel, icon, or user name of my incoming webhook?")
You won't be able to override any of these fields when using an [incoming webhook](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks) attached to a Slack app. Instead, those values will be provided from your Slack app configuration and any configuration provided by the team.
## Interactive messages[​](https://docs.slack.dev/faq#message-buttons "Direct link to Interactive messages")
### Can I use a self-signed certificate for my action URL?[​](https://docs.slack.dev/faq#action-URL "Direct link to Can I use a self-signed certificate for my action URL?")
No, SSL certificates must be signed by a reputable certificate authority. You may want to consider using one of the following low-cost providers:
  * [Let's Encrypt](https://letsencrypt.org/)
  * [CloudFlare](https://www.cloudflare.com/ssl/)


## Web API[​](https://docs.slack.dev/faq#web-api "Direct link to Web API")
### Can I send JSON when using HTTP POST?[​](https://docs.slack.dev/faq#http-post "Direct link to Can I send JSON when using HTTP POST?")
Yes, the [Web API](https://docs.slack.dev/apis/web-api/) accepts both `application/x-www-form-urlencoded` POSTs as well as `application/json`.
Refer to [POST bodies](https://docs.slack.dev/apis/web-api/#post_bodies) for more information.
### How is the Web API rate limited?[​](https://docs.slack.dev/faq#rate-limited "Direct link to How is the Web API rate limited?")
Refer to our [rate limiting guide](https://docs.slack.dev/apis/web-api/rate-limits) for specific information on rate limits.
### How do I work with files?[​](https://docs.slack.dev/faq#files "Direct link to How do I work with files?")
Refer to our [working with files guide](https://docs.slack.dev/messaging/working-with-files) for specific information on working with files.
### How do I find a channel's ID if I only have its #name?[​](https://docs.slack.dev/faq#channels-ID "Direct link to How do I find a channel's ID if I only have its #name?")
There are currently no methods to directly look up channels by name. Use the [`conversations.list`](https://docs.slack.dev/reference/methods/conversations.list) API method to retrieve a list of channels. The list includes each channel's `name` and `id` fields.
Many developers keep the list of channels in memory for swifter lookups. Poll the method occasionally to refresh your inventory or keep it updated with the [Events API](https://docs.slack.dev/apis/events-api/).
### How do I find a channel's name if I only have its ID?[​](https://docs.slack.dev/faq#channels-name "Direct link to How do I find a channel's name if I only have its ID?")
You can use similar instructions to the question above, or you can use the [`conversations.info`](https://docs.slack.dev/reference/methods/conversations.info) API method to obtain a specific channel's information, including its `name`.
### Do channel IDs stay the same when the name of the channel changes?[​](https://docs.slack.dev/faq#channels "Direct link to Do channel IDs stay the same when the name of the channel changes?")
Channel IDs remain the same, even when names are changed.
### Do channel IDs stay the same when moving between public and private?[​](https://docs.slack.dev/faq#channels-visibility "Direct link to Do channel IDs stay the same when moving between public and private?")
As of [September 2018](https://api.slack.com/changelog/2018-09-more-reasons-to-be-a-conversations-api-convert), channel IDs remain static even when a channel is converted between public and private.
Use the [Conversations API](https://docs.slack.dev/apis/web-api/using-the-conversations-api) to safely work with channels that have transitioned between public and private.
### How do I retrieve a single message?[​](https://docs.slack.dev/faq#message "Direct link to How do I retrieve a single message?")
Use the [`conversations.history`](https://docs.slack.dev/reference/methods/conversations.history) API method and a token with the [`channels:history`](https://docs.slack.dev/reference/scopes/channels.history) scope to retrieve a specific message in a public channel. [Learn more about this approach](https://docs.slack.dev/messaging/retrieving-messages#individual_messages).
## Events API[​](https://docs.slack.dev/faq#events-api "Direct link to Events API")
### How do I re-enable event subscriptions for my app?[​](https://docs.slack.dev/faq#events-subscription "Direct link to How do I re-enable event subscriptions for my app?")
If your app's subscriptions are disabled due to exceeding the Events API [failure limits](https://docs.slack.dev/apis/events-api/#failure_limits), manually re-enable them by visiting your [application's settings](https://api.slack.com/apps). If your app is part of the Slack Marketplace, use your **Live App Settings** instead of your development app.
### When should I use the Events API and when should I use Socket Mode or the legacy RTM API?[​](https://docs.slack.dev/faq#events-socket-RTM "Direct link to When should I use the Events API and when should I use Socket Mode or the legacy RTM API?")
Choose the [Events API](https://docs.slack.dev/apis/events-api/) if:
  1. You want to precisely [scope](https://docs.slack.dev/reference/scopes) the data you receive to just what your app needs.
  2. You prefer or must use an inbound request model due to one of the following: a) your hosting service is not able to maintain an outbound WebSocket connection, or b) you prefer to scale your application on an inbound request model instead of maintaining multiple long-lived WebSocket connections.
  3. You're converting an [outgoing webhook](https://docs.slack.dev/legacy/legacy-custom-integrations/legacy-custom-integrations-outgoing-webhooks) integration into something installable as a Slack app.
  4. You find the [retry behavior](https://docs.slack.dev/apis/events-api/#errors) reassuring for redundancy reasons.


Choose [Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode) if:
  1. You're building an on-premise integration or have no ability to receive external HTTP requests.
  2. You're working on a distributed or mobile application without a server backend.
  3. You just prefer working with WebSockets. That's cool.
  4. You want data feed redundancy by opening additional WebSocket connections.
  5. You want messages to be delivered to you in real time.


Finally, choose the legacy [RTM API](https://docs.slack.dev/legacy/legacy-rtm-api) _only_ if:
  1. You have very specific needs that only the RTM API solves.
  2. You already have a classic app, as they can longer be created.
  3. You are okay with your app not working in the somewhat-near future, [as classic apps are slated to be deprecated.](https://docs.slack.dev/changelog/2024-09-legacy-custom-bots-classic-apps-deprecation)


### How do I make my bot appear active and present?[​](https://docs.slack.dev/faq#bots "Direct link to How do I make my bot appear active and present?")
The answer depends on whether you're using the Events API with or without the legacy RTM API:
  * With the Events API, you must toggle your presence by [managing your app](https://api.slack.com/apps)'s bot user config.
  * With the legacy RTM API, your bot is marked `active` while connected to a WebSocket.


Therefore, the presence of the bot depends on whether you are using the legacy RTM API (the bot is online when it's connected through the WebSocket), or it's always online when you turn this setting on. Refer to [bot presence](https://docs.slack.dev/apis/web-api/user-presence-and-status#bot_presence) for more information.
## Socket Mode[​](https://docs.slack.dev/faq#socket-mode "Direct link to Socket Mode")
[Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode) allows you to use the [Events API](https://docs.slack.dev/apis/events-api/) and [interactive features of the platform](https://docs.slack.dev/interactivity), without exposing a static HTTP endpoint to receive payloads. Instead, you use the WebSocket protocol and generate a URL at runtime.
The legacy [RTM API](https://docs.slack.dev/legacy/legacy-rtm-api) is another way of connecting your application to Slack. For most applications that can't use a static HTTP endpoint, [Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode) is preferred over RTM.
## Legacy RTM API[​](https://docs.slack.dev/faq#real-time-messaging-api "Direct link to Legacy RTM API")
### Can I start using the RTM API?[​](https://docs.slack.dev/faq#can-i-start-using-the-rtm-api "Direct link to Can I start using the RTM API?")
Most likely not. Classic apps can no longer be created, and the newer, granular permissions apps cannot access the RTM API. Try the [Events API](https://docs.slack.dev/apis/events-api/)!
### Can I keep using the RTM API?[​](https://docs.slack.dev/faq#can-i-keep-using-the-rtm-api "Direct link to Can I keep using the RTM API?")
You can! But not forever. [Legacy classic apps are set to be deprecated March 2026](https://docs.slack.dev/changelog/2024-09-legacy-custom-bots-classic-apps-deprecation). Without those legacy apps, there will be no way to access the RTM API. Try the [Events API](https://docs.slack.dev/apis/events-api/) instead!
## App approvals[​](https://docs.slack.dev/faq#app-approvals "Direct link to App approvals")
### How does my app get approved for the Slack Marketplace?[​](https://docs.slack.dev/faq#get-approved "Direct link to How does my app get approved for the Slack Marketplace?")
Refer to the following guide: [Slack Marketplace review guide](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide).
### What happens if I make changes to an application that has been approved for the Slack Marketplace?[​](https://docs.slack.dev/faq#app-approval-change "Direct link to What happens if I make changes to an application that has been approved for the Slack Marketplace?")
If you need to update your approved app to request new [OAuth scopes](https://docs.slack.dev/authentication/installing-with-oauth#asking) or to include new features, find your application's settings page at <https://api.slack.com/apps>. Any changes you make here will not affect the published app.
Once you're ready to apply these changes to the published app, you'll need to [resubmit it for review](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide).
### What kind of changes to my app will require being reviewed again?[​](https://docs.slack.dev/faq#app-approval-review "Direct link to What kind of changes to my app will require being reviewed again?")
If you've submitted your app to the Slack Marketplace but need to make changes to how your app or bot is described, to the integration types packed into your app, or to request additional permissions, you'll need your app to be reviewed again.
Use the beta application corresponding to your submitted Slack app to make modifications to any of these features, such as:
  * Requesting new OAuth permission [scopes](https://docs.slack.dev/authentication/installing-with-oauth#asking)
  * Changing your message button action URLs
  * Changing your slash command execution URLs & other details about your [slash command](https://docs.slack.dev/interactivity/implementing-slash-commands)
  * Changing your [Events API](https://docs.slack.dev/apis/events-api/) subscription URLs or subscriptions
  * Changing your [bot user's](https://docs.slack.dev/authentication/tokens) username
  * Changing your app's OAuth configuration
  * Changing details about how your application is presented in the Slack Marketplace 
    * Application description
    * Contact information
    * Application icon
    * Policy & Website URLs


Your client secret and signing secret may be regenerated as needed, without requesting further review.
### Do I need to submit my Slack App to the Slack Marketplace if I don't want to?[​](https://docs.slack.dev/faq#slack-marketplace "Direct link to Do I need to submit my Slack App to the Slack Marketplace if I don't want to?")
No, only submit your app to the Slack Marketplace if you want your app to be discoverable and installable from the Slack Marketplace. If you don't submit your app, we won't display it there, but it will be installable by any workspace you give the authorization URL to.
## Scaling your app[​](https://docs.slack.dev/faq#scaling-your-app "Direct link to Scaling your app")
### How do I avoid long response times and timeouts while working on behalf of large workspaces?[​](https://docs.slack.dev/faq#workspaces "Direct link to How do I avoid long response times and timeouts while working on behalf of large workspaces?")
If using the [`conversations.list`](https://docs.slack.dev/reference/methods/conversations.list) API method, use the `exclude_members` parameter to trim long membership lists from each channel object.
## Team vs. workspace[​](https://docs.slack.dev/faq#team-vs-workspace "Direct link to Team vs. workspace")
### Why is an ID for a workspace is called `team_id`, not `workspace_id`?[​](https://docs.slack.dev/faq#workspace-naming "Direct link to workspace-naming")
Our bad. We used to overuse the term _team_ which could mean two different things— _the people you talk to_ , as well as the Slack workspace, _the place you do work_!
Now, we use _workspace_ for all the Slack workspaces; however, our API remains the same as before. Wherever you see some objects containing `team_id`, it really is an ID for the workspace! In the API world, we use the two terms interchangeably.
## Transitioning from IRC & XMPP gateways[​](https://docs.slack.dev/faq#gateways "Direct link to Transitioning from IRC & XMPP gateways")
### How do I build an IRC or XMPP gateway for myself using the API?[​](https://docs.slack.dev/faq#IRC-XMPP-APIs "Direct link to How do I build an IRC or XMPP gateway for myself using the API?")
Building your own gateway for personal use is an undertaking.
The part of the gateway that reads from Slack should either connect to the legacy [RTM API](https://docs.slack.dev/legacy/legacy-rtm-api) over a WebSocket or listen for events using the [Events API](https://docs.slack.dev/apis/events-api/). Use the [Web API](https://docs.slack.dev/apis/web-api/) to post messages and perform channel operations. The XMPP or IRC part of the gateway is its own adventure to explore.
Choose the [token type](https://docs.slack.dev/authentication/tokens) that works best for you. Bot user tokens work well if your user is a bot, but poorly if your user is you. [Properly scoped](https://docs.slack.dev/authentication/tokens) user tokens work best, as they model your own relationship to Slack. The `client` scope is useful, but overly broad and not suitable for an app distributed on the Slack Marketplace. Using your user token to post as yourself when posting messages with the [`chat.postMessage`](https://docs.slack.dev/reference/methods/chat.postMessage) API method is best.
Apps operating as a gateway should **never** distribute their API keys, secrets, or tokens.
## Workflow Builder[​](https://docs.slack.dev/faq#workflows "Direct link to Workflow Builder")
### Is it possible to add a workflow to multiple channels?[​](https://docs.slack.dev/faq#channels-workflows "Direct link to Is it possible to add a workflow to multiple channels?")
While you cannot add a single workflow to multiple channels, you can download a workflow file, import it into Slack, and update the channel in which it triggers. To download a workflow file, within Workflow Builder, click on the three dots beside the workflow you would like to download and click **Download workflow file**.
### Is it possible to have workflows branch into different paths based on form answers?[​](https://docs.slack.dev/faq#workflows-branch "Direct link to Is it possible to have workflows branch into different paths based on form answers?")
No, at the moment it isn't possible to have conditionals within a workflow.
## Automations platform: developers[​](https://docs.slack.dev/faq#automations-workflow-apps "Direct link to Automations platform: developers")
### How do I set up my development environment?[​](https://docs.slack.dev/faq#setupenv "Direct link to How do I set up my development environment?")
Head to the [Quickstart guide](https://tools.slack.dev/deno-slack-sdk/guides/getting-started) to use our automated installer script, or download the latest version of the Slack CLI and follow instructions to install it manually.
If you have installed the Slack CLI previously and have an older version, note that the minimum required Slack CLI version for Enterprise Grid as of September 19th, 2023 is `v2.9.0`. If you attempt to log in with an older version, you'll receive a `cli_update_required` error from the Slack API. Run `slack upgrade` to get the latest version.
Using a combination of your favorite text editor, the Slack CLI, and the included Deno Slack SDK, you'll develop using TypeScript with a [Deno](https://tools.slack.dev/deno-slack-sdk/guides/installing-deno) runtime environment.
### Which hosts are involved in the creation and execution of apps created with the Slack CLI?[​](https://docs.slack.dev/faq#hosts "Direct link to Which hosts are involved in the creation and execution of apps created with the Slack CLI?")
The automation platform is closely tied to specific language runtimes and SDKs. As you install and utilize your developer tools, you should expect requests from your network to the following non-exhaustive list of hosts:
  * `api.slack.com`, configuration information and documentation resources
  * `downloads.slack-edge.com`, where binaries and other static resources are hosted by Slack
  * `slack.com`, where most of the individual APIs reside called by the Slack CLI and your app
  * `slackb.com`, general logging for your triggers, functions, and workflows
  * `slackd.com`, where we send information about errors, warnings, and other special conditions
  * `deno.land`, where the Typescript runtime, Deno, resolves & retrieves dependencies and versions
  * `jsr.io`, where additional runtime packages and related dependencies are registered


### How can two or more developers collaborate on an app?[​](https://docs.slack.dev/faq#collaboration "Direct link to How can two or more developers collaborate on an app?")
Refer to [team collaboration](https://tools.slack.dev/deno-slack-sdk/guides/collaborating-with-teammates).
### How do I build a slash command on the automation platform?[​](https://docs.slack.dev/faq#slashcommands "Direct link to How do I build a slash command on the automation platform?")
Workflows can be started manually by users via [link triggers](https://tools.slack.dev/deno-slack-sdk/guides/creating-link-triggers). There are multiple ways to invoke a link trigger, and one of them is with a `/` keystroke via the [shortcut menu](https://docs.slack.dev/interactivity/implementing-shortcuts#global).
In other words, you can use a slash command to invoke a link trigger that will kick off a workflow.
### Which languages are supported in Slack's managed infrastructure?[​](https://docs.slack.dev/faq#languages "Direct link to Which languages are supported in Slack's managed infrastructure?")
At this time, apps deployed to Slack's managed infrastructure are built with [Typescript](https://tools.slack.dev/deno-slack-sdk/guides/developing-with-typescript) in a [Deno runtime environment](https://tools.slack.dev/deno-slack-sdk/guides/developing-with-deno).
### What's the difference between running and deploying an app?[​](https://docs.slack.dev/faq#runordeploy "Direct link to What's the difference between running and deploying an app?")
When you use [`slack run`](https://tools.slack.dev/deno-slack-sdk/guides/developing-locally), the local development version of your app connects to Slack via socket mode directly from where you're developing. As you use Slack (or other tools) to interact with your app's triggers, workflows, and functions, data is sent back and forth against your latest saved code. Use this while you're still tweaking things. Your development app is generally only shared with other collaborators, though you can test the full range of trigger options anyway.
When you use [`slack deploy`](https://tools.slack.dev/deno-slack-sdk/guides/deploying-to-slack), the fine computer instructions you've written are packaged up and deployed to Slack's managed infrastructure. As users interact with your app, data is swiftly and securely sent back and forth between Slack servers. Treat this instance of your app with care, especially as your userbase grows.
The local and deployed environments have different triggers associated with them. Triggers you create in a local context will not automatically be created in a deployed context once your app is deployed.
### Can I list my app in the Slack Marketplace?[​](https://docs.slack.dev/faq#slack-marketplace "Direct link to Can I list my app in the Slack Marketplace?")
Currently, automations apps are not eligible for listing in the Slack Marketplace.
### How do I call a third-party API?[​](https://docs.slack.dev/faq#third-party "Direct link to How do I call a third-party API?")
An example of how to do this is shown in the [GitHub Issue tutorial](https://tools.slack.dev/deno-slack-sdk/tutorials/github-issues-app), but the long and short of it is as folows:
  * Store API credentials as local environment variables. In the GitHub tutorial, for instance, your `.env` file could look like this:


```
github_name = slackbotsbestbuddygithub_token = ABC123DEF
```

  * Use the `env` [context property](https://tools.slack.dev/deno-slack-sdk/guides/creating-custom-functions#context) to call environment variables from within your function.


```
import{DefineFunction,Schema,SlackFunction}from"deno-slack-sdk/mod.ts";exportconstMyFunctionDefinition=DefineFunction({callback_id:"my_function",title:"my function",source_file:"functions/my_function.ts",input_parameters:{properties:{},required:[]},output_parameters:{properties:{},required:[]},});exportdefaultSlackFunction(MyFunctionDefinition,async({ inputs, env })=>{// Add thisconst headers ={Authorization:`Bearer ${env.GITHUB_TOKEN}`,"Content-Type":"application/json",};try{const endpoint ="https://api.github.com/users/repos";const response =awaitfetch(endpoint,{method:"GET", headers });if(response.status!=200){// In the case where the API responded with non 200 statusconst body =await response.text();const error =`Failed to call an API (status: ${response.status}, body: ${body})`;return{ error };}// Do cool stuff with your repo info hereconst repos =await response.json();return{outputs:{}};}catch(err){const error =`Failed to call GitHub API due to ${err}`;return{ error };}},);
```

That's all! When you run your app, it will use the environment variables stored within your `.env` file. You won't be using your `.env` file when your app is deployed (nor should you ever commit that file to source control), so the real power of environment variables is seen when you use the `env` Slack CLI [helper](https://tools.slack.dev/slack-cli/commands/#env). Once your app is deployed using `slack deploy`, add your environment variable with the following command:
```
slack env add github_token ABC123DEF
```

If your token contains non-alphanumeric characters, wrap it in double quotes. Environment variables added via the `slack env add` command can be accessed via the `env` Slack CLI [helper](https://tools.slack.dev/slack-cli/commands/#env), which also allows you to `update` and `remove` them.
### Can I import additional libraries and SDKs?[​](https://docs.slack.dev/faq#deno-library "Direct link to Can I import additional libraries and SDKs?")
Yes, you can! To use a [Deno Third Party Module](https://deno.land/x), Deno imports modules using URLs. You can see how we do this for a test file in the [Deno GitHub functions sample app](https://github.com/slack-samples/deno-github-functions).
```
// /functions/create_issue_test.tsimport*as mffrom"https://deno.land/x/mock_fetch@0.3.0/mod.ts";
```

### How can I use the Slack CLI to set up a Continuous Integration and Continuous Delivery (CI/CD) pipeline?[​](https://docs.slack.dev/faq#cicd "Direct link to How can I use the Slack CLI to set up a Continuous Integration and Continuous Delivery \(CI/CD\) pipeline?")
The Slack CLI is commonly used in local development (usually in an interactive mode with prompts), but can also be used for automating testing and deployments (done without interactivity by using flags) by way of a [CI/CD pipeline](https://tools.slack.dev/slack-cli/guides/setting-up-ci-cd-with-the-slack-cli).
Running this type of automation requires authorization with a service token. Refer to [CI/CD authorization](https://tools.slack.dev/slack-cli/guides/authorizing-the-slack-cli#ci-cd) for more details. You'll also need to accommodate requests from your network to a variety of hosts. Refer to [Which hosts are involved in the creation and execution of apps created with the Slack CLI?](https://docs.slack.dev/faq#hosts) for more details.
## Automations platform: administrators[​](https://docs.slack.dev/faq#admins "Direct link to Automations platform: administrators")
Even some Slack developers are themselves Slack administrators, but if you're an admin you might find yourself here wondering these very same questions. If you don't find the answer to your administrative questions here, consult the [Slack help center for more user and admin-facing content](https://slack.com/resources/slack-for-admins/app-management).
### How do custom workflow steps work?[​](https://docs.slack.dev/faq#custom-workflow-steps "Direct link to How do custom workflow steps work?")
  * Developers can build and publish workflows for anyone in their Slack workspace or Enterprise Grid organization to use. They can also build [custom workflow steps](https://tools.slack.dev/deno-slack-sdk/guides/creating-custom-functions) that users will be able to add to workflows they create with Workflow Builder.
  * When developers build workflows and custom workflow steps, they can set access permissions to determine who can run a workflow or add a custom workflow step to a workflow. Admins can further [restrict access to custom workflow steps](https://slack.com/help/articles/13621100461203) if they’d like.
  * You can now view some workflows on the [published workflow dashboard](https://slack.com/help/articles/15363614064275/). Workflows built with Workflow Builder will still need to be viewed and managed from the **All Published Workflows** tab in Workflow Builder.


### How do I turn off developer access to custom workflow steps and workflows?[​](https://docs.slack.dev/faq#admin_access "Direct link to How do I turn off developer access to custom workflow steps and workflows?")
The new custom workflow steps and workflows introduced to the Slack platform cannot be completely disabled. Instead, you can manage their installation via the [app approvals](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace) feature.
### How do I discover and manage which custom workflow steps and workflows are installed in my workspace?[​](https://docs.slack.dev/faq#admin_manage "Direct link to How do I discover and manage which custom workflow steps and workflows are installed in my workspace?")
From the [published workflow dashboard](https://slack.com/help/articles/15363614064275/), you can view a list of workflows in your workspace or Enterprise Grid organization.
### How will I be charged for using the platform?[​](https://docs.slack.dev/faq#pricing "Direct link to How will I be charged for using the platform?")
For the most up-to-date information about pricing, click here:
[Learn more about pricing](https://slack.com/help/articles/15363357403411/)
### Will existing custom integrations and Slack apps continue working?[​](https://docs.slack.dev/faq#existing "Direct link to Will existing custom integrations and Slack apps continue working?")
Existing Slack apps will continue working as expected. Some older apps might produce activity in Slack you can build custom workflow steps and workflows around. That said, automations are meant to co-exist with the rest of our platform and your existing integrations and customizations.
## Errata[​](https://docs.slack.dev/faq#misc "Direct link to Errata")
### Deployment and installation[​](https://docs.slack.dev/faq#deployment "Direct link to Deployment and installation")
The `slack deploy` command performs two operations:
  1. Deploys all functions associated with your app to the platform, and
  2. Installs your app into the selected workspace.


  * Slack is currently optimized for the first-party developer use case, in which the expectation is that the developer has access to the workspace where they’re building the app.
  * When the app is installed as part of `slack deploy`, the workflows that belong to that app are also “installed” (made available) in that workspace. Currently, there is no way for a coded workflow to be "installed" (via the parent app being installed) by anyone other than the developer. However, coded workflows do not have to be deployed alongside a trigger; since triggers don't belong to apps, all deployment and installation happens first and then a trigger is created separately afterward.
  * JSON or YAML-based app manifests are no longer how your app's configuration is canonically defined. Instead, both your app's configuration _and_ your function definitions will reside in `manifest.ts`.


## Feedback[​](https://docs.slack.dev/faq#feedback "Direct link to Feedback")
Anything else on your mind? Let us know by sending us your feedback!
[PreviousQuickstart](https://docs.slack.dev/quickstart)[NextOverview](https://docs.slack.dev/ai/)
  * [General](https://docs.slack.dev/faq#general)
    * [How do I build a bot using Slack APIs?](https://docs.slack.dev/faq#bot-APIs)
    * [How do I set up a developer environment to build a Slack app?](https://docs.slack.dev/faq#set-up-dev-environment)
    * [Is Slack down?](https://docs.slack.dev/faq#downtime)
    * [How do I integrate a third-party service with Slack?](https://docs.slack.dev/faq#third-party-services)
    * [Workflow apps vs. non-workflow apps](https://docs.slack.dev/faq#workflow-apps)
  * [Authentication](https://docs.slack.dev/faq#authentication)
    * [How do I authenticate my requests to Slack?](https://docs.slack.dev/faq#authenticate-me)
    * [How do I authenticate requests from Slack to me?](https://docs.slack.dev/faq#authenticate-slack)
    * [How does Slack authenticate its requests to my servers?](https://docs.slack.dev/faq#authenticate-servers)
    * [When do authorization codes expire?](https://docs.slack.dev/faq#authenticate-expire)
    * [How do I revoke a token?](https://docs.slack.dev/faq#revoke-token)
    * [How do I reset my client secret?](https://docs.slack.dev/faq#client-secret)
  * [Slash commands](https://docs.slack.dev/faq#slash-commands)
    * [Why does Slack never reach my slash command URL?](https://docs.slack.dev/faq#slash-URL)
    * [How do I validate a slash command's origin?](https://docs.slack.dev/faq#slash-origin)
  * [Incoming webhooks](https://docs.slack.dev/faq#incoming-webhooks)
    * [Why can't I override the channel, icon, or user name of my incoming webhook?](https://docs.slack.dev/faq#override)
  * [Interactive messages](https://docs.slack.dev/faq#message-buttons)
    * [Can I use a self-signed certificate for my action URL?](https://docs.slack.dev/faq#action-URL)
  * [Web API](https://docs.slack.dev/faq#web-api)
    * [Can I send JSON when using HTTP POST?](https://docs.slack.dev/faq#http-post)
    * [How is the Web API rate limited?](https://docs.slack.dev/faq#rate-limited)
    * [How do I work with files?](https://docs.slack.dev/faq#files)
    * [How do I find a channel's ID if I only have its #name?](https://docs.slack.dev/faq#channels-ID)
    * [How do I find a channel's name if I only have its ID?](https://docs.slack.dev/faq#channels-name)
    * [Do channel IDs stay the same when the name of the channel changes?](https://docs.slack.dev/faq#channels)
    * [Do channel IDs stay the same when moving between public and private?](https://docs.slack.dev/faq#channels-visibility)
    * [How do I retrieve a single message?](https://docs.slack.dev/faq#message)
  * [Events API](https://docs.slack.dev/faq#events-api)
    * [How do I re-enable event subscriptions for my app?](https://docs.slack.dev/faq#events-subscription)
    * [When should I use the Events API and when should I use Socket Mode or the legacy RTM API?](https://docs.slack.dev/faq#events-socket-RTM)
    * [How do I make my bot appear active and present?](https://docs.slack.dev/faq#bots)
  * [Socket Mode](https://docs.slack.dev/faq#socket-mode)
  * [Legacy RTM API](https://docs.slack.dev/faq#real-time-messaging-api)
    * [Can I start using the RTM API?](https://docs.slack.dev/faq#can-i-start-using-the-rtm-api)
    * [Can I keep using the RTM API?](https://docs.slack.dev/faq#can-i-keep-using-the-rtm-api)
  * [App approvals](https://docs.slack.dev/faq#app-approvals)
    * [How does my app get approved for the Slack Marketplace?](https://docs.slack.dev/faq#get-approved)
    * [What happens if I make changes to an application that has been approved for the Slack Marketplace?](https://docs.slack.dev/faq#app-approval-change)
    * [What kind of changes to my app will require being reviewed again?](https://docs.slack.dev/faq#app-approval-review)
    * [Do I need to submit my Slack App to the Slack Marketplace if I don't want to?](https://docs.slack.dev/faq#slack-marketplace)
  * [Scaling your app](https://docs.slack.dev/faq#scaling-your-app)
    * [How do I avoid long response times and timeouts while working on behalf of large workspaces?](https://docs.slack.dev/faq#workspaces)
  * [Team vs. workspace](https://docs.slack.dev/faq#team-vs-workspace)
    * [Why is an ID for a workspace is called `team_id`, not `workspace_id`?](https://docs.slack.dev/faq#workspace-naming)
  * [Transitioning from IRC & XMPP gateways](https://docs.slack.dev/faq#gateways)
    * [How do I build an IRC or XMPP gateway for myself using the API?](https://docs.slack.dev/faq#IRC-XMPP-APIs)
  * [Workflow Builder](https://docs.slack.dev/faq#workflows)
    * [Is it possible to add a workflow to multiple channels?](https://docs.slack.dev/faq#channels-workflows)
    * [Is it possible to have workflows branch into different paths based on form answers?](https://docs.slack.dev/faq#workflows-branch)
  * [Automations platform: developers](https://docs.slack.dev/faq#automations-workflow-apps)
    * [How do I set up my development environment?](https://docs.slack.dev/faq#setupenv)
    * [Which hosts are involved in the creation and execution of apps created with the Slack CLI?](https://docs.slack.dev/faq#hosts)
    * [How can two or more developers collaborate on an app?](https://docs.slack.dev/faq#collaboration)
    * [How do I build a slash command on the automation platform?](https://docs.slack.dev/faq#slashcommands)
    * [Which languages are supported in Slack's managed infrastructure?](https://docs.slack.dev/faq#languages)
    * [What's the difference between running and deploying an app?](https://docs.slack.dev/faq#runordeploy)
    * [Can I list my app in the Slack Marketplace?](https://docs.slack.dev/faq#slack-marketplace)
    * [How do I call a third-party API?](https://docs.slack.dev/faq#third-party)
    * [Can I import additional libraries and SDKs?](https://docs.slack.dev/faq#deno-library)
    * [How can I use the Slack CLI to set up a Continuous Integration and Continuous Delivery (CI/CD) pipeline?](https://docs.slack.dev/faq#cicd)
  * [Automations platform: administrators](https://docs.slack.dev/faq#admins)
    * [How do custom workflow steps work?](https://docs.slack.dev/faq#custom-workflow-steps)
    * [How do I turn off developer access to custom workflow steps and workflows?](https://docs.slack.dev/faq#admin_access)
    * [How do I discover and manage which custom workflow steps and workflows are installed in my workspace?](https://docs.slack.dev/faq#admin_manage)
    * [How will I be charged for using the platform?](https://docs.slack.dev/faq#pricing)
    * [Will existing custom integrations and Slack apps continue working?](https://docs.slack.dev/faq#existing)
  * [Errata](https://docs.slack.dev/faq#misc)
    * [Deployment and installation](https://docs.slack.dev/faq#deployment)
  * [Feedback](https://docs.slack.dev/faq#feedback)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



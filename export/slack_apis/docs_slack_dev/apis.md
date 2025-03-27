---
url: https://docs.slack.dev/apis
session_id: slack_api_docs
updated_dt: 2025-03-27T13:25:09.491440
---
[Skip to main content](https://docs.slack.dev/apis#__docusaurus_skipToContent_fallback)
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
  * APIs


On this page
# Slack APIs
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
Every Slack app and [workflow automation](https://docs.slack.dev/workflows) has access to a range of APIs that provide access to read, write, and update many types of data in Slack.
Read on to learn about our core APIs, and discover how to use them to make magic.
## Web API[​](https://docs.slack.dev/apis#web-api "Direct link to Web API")
The Web API supplies a collection of [HTTP methods](https://docs.slack.dev/reference/methods) that underpin the majority of Slack app functionality.
With over 100 methods available, it's impossible to explain _everything_ that's possible with the Web API, but we're sure there's one right for your app.
Our [Web API](https://docs.slack.dev/apis/web-api/) guide explains the basic process of interacting with these methods. Once you've read up on that, dive into the [list of available methods](https://docs.slack.dev/reference/methods).
## Events API[​](https://docs.slack.dev/apis#events-api "Direct link to Events API")
The Events API is a streamlined way to build apps that respond to activities in Slack.
Subscribe to the [events](https://docs.slack.dev/reference/events) you want from a range of possibilities. Build a Slack app that can [react to those events](https://docs.slack.dev/interactivity#responses) usefully.
Tell us where to send the events you carefully select and we'll push them to your app securely. We'll even retry when things don't work out.
Read our [Events API](https://docs.slack.dev/apis/events-api/) guide to learn how to subscribe to and handle events.
Check out our [Event delivery](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode) guide to explore your options with how to receive event payloads: via a public HTTP URL or using the magic of WebSocket via Socket Mode.
If you don't wish to expose a public, static HTTP endpoint to communicate with Slack, [Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode) can help.
## Slack Status API[​](https://docs.slack.dev/apis#slack-status-api "Direct link to Slack Status API")
The Slack Status API describes the health of the Slack product. When there's an incident, outage, or maintenance, the Slack Status API reflects all the information we have on the issue, including which features of Slack are affected and detailed updates over time.
### Atom and RSS Feed[​](https://docs.slack.dev/apis#feed "Direct link to Atom and RSS Feed")
Receive updates on the health of Slack services by subscribing to our Atom or RSS feeds. Use your favorite subscription tool to subscribe to `https://slack-status.com/feed/atom` or `https://slack-status.com/feed/rss`. You could even use the `/feed` command in Slack to subscribe to our Status feed — but it might not work if some parts of Slack are unavailable. An outside feed reader might be a better choice.
Note that many readers check for updates only a few times an hour. Set your feed reader to poll for updates often (for example, once a minute) if you need to be notified immediately of a Slack issue.
See the [Slack Status API reference](https://docs.slack.dev/reference/slack-status-api) for endpoint information.
## Other APIs[​](https://docs.slack.dev/apis#other-apis "Direct link to Other APIs")
Beyond the Web and Events APIs, we have a range of other niche APIs that are suitable for specific types of apps.
  * [**Admin API**](https://docs.slack.dev/admins) are a subset of Web APIs that are geared towards automating and simplifying the administration of Slack organizations.
  * [**SCIM API**](https://docs.slack.dev/admins/scim-api/) are available for user provisioning and management.
  * [**Audit Logs API**](https://docs.slack.dev/admins/audit-logs-api/) are tailored for building security information and event management tools.
  * [**Legacy RTM API**](https://docs.slack.dev/legacy/legacy-rtm-api) is an outmoded API that provides WebSocket access to some of the same functionality as the Web and Events APIs. We list it here for completeness even though it has been deprecated.


[PreviousUsing the Data Access API](https://docs.slack.dev/ai/using-data-access-api)[NextOverview](https://docs.slack.dev/apis/)
  * [Web API](https://docs.slack.dev/apis#web-api)
  * [Events API](https://docs.slack.dev/apis#events-api)
  * [Slack Status API](https://docs.slack.dev/apis#slack-status-api)
    * [Atom and RSS Feed](https://docs.slack.dev/apis#feed)
  * [Other APIs](https://docs.slack.dev/apis#other-apis)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



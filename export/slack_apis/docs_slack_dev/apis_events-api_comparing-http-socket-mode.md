---
url: https://docs.slack.dev/apis/events-api/comparing-http-socket-mode
session_id: slack_api_docs
updated_dt: 2025-03-27T13:25:00.552573
---
[Skip to main content](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#__docusaurus_skipToContent_fallback)
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
  * [Events API](https://docs.slack.dev/apis/events-api/)
  * Comparing HTTP & Socket Mode


On this page
# Comparing HTTP & Socket Mode
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
In the course of your journey to create a Slack app, you will likely want to use the [Events API](https://docs.slack.dev/apis/events-api/), [slash commands](https://docs.slack.dev/interactivity/implementing-slash-commands), [interactivity](https://docs.slack.dev/interactivity/handling-user-interaction), or [shortcuts](https://docs.slack.dev/interactivity/implementing-shortcuts) to enable your app to respond to messages and handle interactive events happening in Slack. To do so, you will choose to receive event payloads via HTTP requests or WebSocket messages. Each protocol has its pros and cons, which we will explain here.
## What is a web protocol?[​](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#protocol "Direct link to What is a web protocol?")
Put simply, a web protocol is a set of rules that computers use to communicate over the internet. What this means in terms of a Slack app is how information is sent from the Slack client (end user) to the app and back: how it exchanges information. For Slack apps, this can happen either over HTTP or WebSocket (the use of which is known as Socket Mode in the [app settings](https://api.slack.com/apps)). WebSocket and HTTP are both web communication protocols, but they have different use cases and characteristics.
Here is a side-by-side comparison of the two.
Feature| HTTP| WebSocket  
---|---|---  
Messaging pattern| Request-response| Bi-directional  
Protocol| Stateless| Stateful  
Scalability| Scales well horizontally| Challenging to scale due to stateful nature. Slack limits the number of concurrent WebSocket connections to 10 per app.  
Bidirectional updates| No| Yes  
Connection length| Short-lived| Long-lived  
## HTTP[​](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#http "Direct link to HTTP")
HTTP is a protocol that follows a request-response pattern between clients and servers. A short-lived connection to the server is opened for each request, then closed once the request is complete. Within each response, the server provides the client with the requested content as well as information about the request (metadata). HTTP uses half-duplex communication, which means only one party can communicate at a time. Because each request contains all necessary information, it is simpler (compared to using WebSocket) to route requests through proxies to carry out other operations, like caching and encryption.
HTTP communication is stateless: it does not keep track of connections and requests. HTTP is well-suited for static content and standard API requests, like the ones used by Slack apps. In terms of reliability, short-lived connections—like stateless HTTP connections—are inherently more reliable than long-lived connections.
The downside of HTTP that app developers part of a corporation run into is that they cannot expose a public HTTP endpoint due to the firewall because it is a security concern. Another disadvantage to HTTP is that the client opens an ephemeral connection and sends metadata for each request, which incurs a small overhead.
## WebSocket[​](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#web-socket "Direct link to WebSocket")
WebSocket is a protocol that allows for simultaneous two-way communication over the same connection in realtime. This means the server can push realtime updates as soon as they become available instead of waiting to respond to a request from the client. Unlike HTTP, WebSocket is a full-duplex communication protocol.
Because of its low latency and persistent connections, WebSocket is best for applications that require real-time, two-way communication, like online gaming, chat apps, and live updates. Socket Mode in Slack is a great option if you're building an on-premise integration, have no ability to receive external HTTP requests, or want data feed redundancy by opening additional WebSocket connections.
However, WebSocket is stateful, making it more difficult to scale. It also uses long-lived connections that over time could be subject to a network partition or other transient events causing disconnects. Additionally, the socket server backend recycles containers serving connections every now and then, leading to occassional reliability issues. To have the highest possible reliability for application connectivity, we recommend using HTTP for production applications.
## Which to use when[​](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#which-one "Direct link to Which to use when")
For its convenience, ease of setup, and ability to work behind a firewall, we recommend using Socket Mode when developing your app and using it locally. Once deployed and published for use in a team setting, we recommend using HTTP request URLs. If your production app does not need to use Socket Mode, we recommend sticking with HTTP for the sake of simplicity. There are less moving parts and less complexity for your app to worry about managing. Socket mode is fully supported for distributed apps. However, if you intend to submit your app to be available for use in the [Slack Marketplace](https://docs.slack.dev/slack-marketplace), using HTTP is a requirement.
Alternatively, if it is a requirement that you work behind a firewall and do not have the ability to expose HTTP endpoints, Socket Mode is there for you. As long as you do not intend to submit your app to the Slack Marketplace and actively maintain your connection to us, Socket Mode is a reliable option.
## Implementation[​](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#implementation "Direct link to Implementation")
Support for both HTTP and WebSocket is built into the [Slack Bolt frameworks](https://tools.slack.dev). They can also be configured without the use of SDKs.
### HTTP resources[​](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#http-resources "Direct link to HTTP resources")
Read more about setting up your app with HTTP [here](https://docs.slack.dev/apis/events-api/using-http-request-urls). To explore the Bolt SDK documentation on creating an app with HTTP, refer to the [Bolt for Python guide here](https://tools.slack.dev/bolt-python/tutorial/getting-started-http) and the [Bolt for JavaScript guide here](https://tools.slack.dev/bolt-js/tutorial/getting-started-http/).
### Socket Mode resources[​](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#socket-mode-resources "Direct link to Socket Mode resources")
Read more about setting up your app with Socket Mode [here](https://docs.slack.dev/apis/events-api/using-socket-mode). To explore the Bolt SDK documentation on creating an app with Socket Mode, refer to the [Bolt for Python guide here](https://tools.slack.dev/bolt-python/getting-started) and the [Bolt for JavaScript guide here](https://tools.slack.dev/bolt-js/getting-started).
[PreviousOverview](https://docs.slack.dev/apis/events-api/)[NextUsing HTTP Request URLs](https://docs.slack.dev/apis/events-api/using-http-request-urls)
  * [What is a web protocol?](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#protocol)
  * [HTTP](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#http)
  * [WebSocket](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#web-socket)
  * [Which to use when](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#which-one)
  * [Implementation](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#implementation)
    * [HTTP resources](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#http-resources)
    * [Socket Mode resources](https://docs.slack.dev/apis/events-api/comparing-http-socket-mode#socket-mode-resources)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



---
url: https://docs.slack.dev/apis/web-api
session_id: slack_api_docs
updated_dt: 2025-03-27T13:25:09.802347
---
[Skip to main content](https://docs.slack.dev/apis/web-api#__docusaurus_skipToContent_fallback)
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
      * [Overview](https://docs.slack.dev/apis/web-api/)
      * [Pagination](https://docs.slack.dev/apis/web-api/pagination)
      * [Rate limits](https://docs.slack.dev/apis/web-api/rate-limits)
      * [Using the Conversations API](https://docs.slack.dev/apis/web-api/using-the-conversations-api)
      * [Using the Calls API](https://docs.slack.dev/apis/web-api/using-the-calls-api)
      * [User presence and status](https://docs.slack.dev/apis/web-api/user-presence-and-status)
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
  * [APIs](https://docs.slack.dev/apis/)
  * Web API


On this page
# Slack Web API
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
The Slack Web API is an interface for querying information _from_ and enacting change _in_ a Slack workspace.
Use it for individual queries, or as part of a more complex tapestry of platform features in a Slack app.
[Web API methods](https://docs.slack.dev/reference/methods)
## Basic overview[​](https://docs.slack.dev/apis/web-api#basics "Direct link to Basic overview")
  * The Web API is a collection of [HTTP RPC-style methods](https://docs.slack.dev/reference/methods), all with URLs in the form `https://slack.com/api/METHOD_FAMILY.method`.
  * While it's not a REST API, those familiar with REST should be at home with its foundations in HTTP.
  * Use HTTPS, SSL, and TLS v1.2 or above when calling all methods. [Learn more about our SSL and TLS requirements](https://docs.slack.dev/apis/web-api#ssl).
  * Each method has a series of arguments informing the execution of your intentions.
  * Pass arguments as: 
    * GET querystring parameters,
    * POST parameters presented as `application/x-www-form-urlencoded`, or
    * a mix of both GET and POST parameters
  * [Most write methods](https://docs.slack.dev/apis/web-api#methods_supporting_json) allow arguments with `application/json` attributes.
  * Some methods, such as [`chat.postMessage`](https://docs.slack.dev/reference/methods/chat.postMessage) and [`dialog.open`](https://docs.slack.dev/reference/methods/dialog.open), feature arguments that accept an associative JSON array. However, these methods can be difficult to properly construct when using a `application/x-www-form-urlencoded` Content-type, so we strongly recommend using [JSON-encoded bodies](https://docs.slack.dev/apis/web-api#posting_json) instead.


### POST bodies[​](https://docs.slack.dev/apis/web-api#post-bodies "Direct link to POST bodies")
When sending a HTTP POST, you may present your arguments as either standard POST parameters, or you may use JSON instead.
#### URL-encoded bodies[​](https://docs.slack.dev/apis/web-api#url-encoded-bodies "Direct link to URL-encoded bodies")
When sending URL-encoded data, set your HTTP `Content-type` header to `application/x-www-form-urlencoded` and present your key/value pairs according to [RFC-3986](https://tools.ietf.org/html/rfc3986).
For example, a POST request to the [`conversations.create`](https://docs.slack.dev/reference/methods/conversations.create) method might look something like this:
```
POST /api/conversations.createContent-type: application/x-www-form-urlencodedtoken=xoxp-xxxxxxxxx-xxxx&name=something-urgent
```

#### JSON-encoded bodies[​](https://docs.slack.dev/apis/web-api#posting_json "Direct link to JSON-encoded bodies")
For [write methods that support JSON](https://docs.slack.dev/apis/web-api#methods_supporting_json), you may alternatively send your HTTP POST data as `Content-type: application/json`.
There are some ground rules:
  * You must explicitly set the `Content-type` HTTP header to `application/json`. We won't interpret your POST body as such without it.
  * You must transmit your `token` as a bearer token in the `Authorization` HTTP header.
  * You cannot send your token as part of the query string or as an attribute in your posted JSON.
  * Do not mix arguments between query string, URL-encoded POST body, and JSON attributes. Choose one approach per request.
  * Providing an explicitly `null` value for an attribute will result in whichever default behavior is assigned to it.


For example, to send the same request above to the `conversations.create` method with a JSON POST body, send something like this:
```
POST /api/conversations.createContent-type: application/jsonAuthorization: Bearer xoxp-xxxxxxxxx-xxxx{"name":"something-urgent"}
```

Note how we present the token with the string `Bearer ` pre-pended to it, indicating the [OAuth 2.0](https://docs.slack.dev/authentication) authentication scheme. Consult your favorite HTTP tool or library's manual for further detail on setting HTTP headers.
Here's a more complicated example — posting a message with [menus](https://docs.slack.dev/legacy/legacy-messaging/legacy-adding-menus-to-messages) using [`chat.postMessage`](https://docs.slack.dev/reference/methods/chat.postMessage):
```
POST /api/chat.postMessageContent-type: application/jsonAuthorization: Bearer xoxp-xxxxxxxxx-xxxx{"channel":"C123ABC456","text":"I hope the tour went well, Mr. Wonka.","attachments":[{"text":"Who wins the lifetime supply of chocolate?","fallback":"You could be telling the computer exactly what it can do with a lifetime supply of chocolate.","color":"#3AA3E3","attachment_type":"default","callback_id":"select_simple_1234","actions":[{"name":"winners_list","text":"Who should win?","type":"select","data_source":"users"}]}]}
```

The `attachments` argument is sent a straightforward JSON array.
Here's how to do that with [cURL](https://curl.haxx.se/):
```
curl -X POST -H 'Authorization: Bearer xoxb-1234-56789abcdefghijklmnop' \-H 'Content-type: application/json' \--data '{"channel":"C123ABC456","text":"I hope the tour went well, Mr. Wonka.","attachments": [{"text":"Who wins the lifetime supply of chocolate?","fallback":"You could be telling the computer exactly what it can do with a lifetime supply of chocolate.","color":"#3AA3E3","attachment_type":"default","callback_id":"select_simple_1234","actions":[{"name":"winners_list","text":"Who should win?","type":"select","data_source":"users"}]}]}' \https://slack.com/api/chat.postMessage<
```

#### Errors specific to passing JSON[​](https://docs.slack.dev/apis/web-api#JSON-errors "Direct link to Errors specific to passing JSON")
If the posted JSON is invalid, you'll receive one of the following errors in response:
  * `invalid_json`: The JSON you've included in your POST body cannot be parsed. This might be because it's actually not JSON, or perhaps you did not correctly set your HTTP `Content-type` header. Ensure your JSON attribute keys are strings wrapped with double-quote (`"`) characters.
  * `json_not_object`: We could understand that your code was JSON-like enough to parse it, but it's not actually a JSON hash of attribute key/value pairs. Perhaps you sent us an array, or just a string or a number.


In both cases, you'll need to revise your JSON or how you're transmitting your data to resolve the error condition.
## Evaluating responses[​](https://docs.slack.dev/apis/web-api#responses "Direct link to Evaluating responses")
All Web API responses contain a JSON object, which will always contain a top-level boolean property `ok` that indicates success or failure.
For failure results, the `error` property will contain a short machine-readable error code. In the case of problematic calls that could still be completed successfully, `ok` will be `true` and the `warning` property will contain a short machine-readable warning code (or comma-separated list of them, in the case of multiple warnings). See the following examples:
```
{"ok":true,"stuff":"This is good"}
```

```
{"ok":false,"error":"something_bad"}
```

```
{"ok":true,"warning":"something_problematic","stuff":"Your requested information"}
```

Other properties are defined in the documentation for each relevant method. There's a lot of "stuff" to unpack, including [these types](https://docs.slack.dev/reference/objects) and other method or domain-specific curiosities.
## Authentication[​](https://docs.slack.dev/apis/web-api#authentication "Direct link to Authentication")
Authenticate your Web API requests by providing a [bearer token](https://docs.slack.dev/authentication/tokens), which identifies a single user or bot user relationship.
[Register your application](https://api.slack.com/apps) with Slack to obtain credentials for use with our [OAuth 2.0](https://docs.slack.dev/authentication/installing-with-oauth) implementation, which allows you to negotiate tokens on behalf of users and workspaces.
We prefer tokens to be sent in the `Authorization` HTTP header of your outbound requests. However, you may also pass tokens in all Web API calls as a POST body parameter called `token`. Tokens cannot be sent as a query parameter.
Treat tokens with care
Never share tokens with other users or applications. Do not publish tokens in public code repositories. [Review token safety tips](https://docs.slack.dev/authentication/best-practices-for-security).
## HTTPS, SSL, and TLS[​](https://docs.slack.dev/apis/web-api#ssl "Direct link to HTTPS, SSL, and TLS")
Slack requires HTTPS, SSL, and TLS v1.2 or above. The platform and the Web API are governed by the same rules. [Learn more about our deprecation of early TLS versions](https://docs.slack.dev/changelog/2019-07-deprecate-early-tls-versions). Stay safe and secure.
All TLS connections must use the [SNI extension](https://en.wikipedia.org/wiki/Server_Name_Indication). Lastly, TLS connections must support at least one of the following cipher suites:
TLS 1.2:
  * `ECDHE-RSA-AES128-GCM-SHA256`
  * `ECDHE-RSA-CHACHA20-POLY1305`
  * `ECDHE-RSA-AES256-GCM-SHA384`


TLS 1.3:
  * `TLS_AES_128_GCM_SHA256`
  * `TLS_AES_256_GCM_SHA384`
  * `TLS_CHACHA20_POLY1305_SHA256`


## Methods[​](https://docs.slack.dev/apis/web-api#methods "Direct link to Methods")
With over 200 methods, surely there's one right for you. You can find them all in the [reference](https://docs.slack.dev/reference/methods), where you can filter by method family.
[PreviousOverview](https://docs.slack.dev/apis/)[NextOverview](https://docs.slack.dev/apis/web-api/)
  * [Basic overview](https://docs.slack.dev/apis/web-api#basics)
    * [POST bodies](https://docs.slack.dev/apis/web-api#post-bodies)
  * [Evaluating responses](https://docs.slack.dev/apis/web-api#responses)
  * [Authentication](https://docs.slack.dev/apis/web-api#authentication)
  * [HTTPS, SSL, and TLS](https://docs.slack.dev/apis/web-api#ssl)
  * [Methods](https://docs.slack.dev/apis/web-api#methods)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



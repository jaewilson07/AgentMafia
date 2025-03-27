---
url: https://docs.slack.dev/apis/events-api/using-socket-mode
session_id: slack_api_docs
updated_dt: 2025-03-27T13:24:48.770046
---
[Skip to main content](https://docs.slack.dev/apis/events-api/using-socket-mode#__docusaurus_skipToContent_fallback)
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
  * Using Socket Mode


On this page
# Using Socket Mode
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
Socket Mode allows your app to use [the Events API](https://docs.slack.dev/apis/events-api/) and [interactive features](https://docs.slack.dev/interactivity)— _without_ exposing a public HTTP **Request URL**.
Instead of sending payloads to a public endpoint, Slack will use a [WebSocket URL](https://tools.ietf.org/html/rfc6455) to communicate with your app. WebSockets use a bidirectional stateful protocol with low latency to communicate between two parties—in this case, Slack and your app.
Unlike a public HTTP endpoint, the WebSocket URL you listen to is not static. The URL is created at runtime by calling the [`apps.connections.open`](https://docs.slack.dev/reference/methods/apps.connections.open) method, and it refreshes regularly.
Socket Mode helps developers working behind a corporate firewall, or who have other security concerns that don't allow exposing a static HTTP endpoint.
You can still switch between a direct HTTP endpoint and Socket Mode at any time in the [app settings](https://api.slack.com/apps).
We recommend [using our Bolt frameworks or SDKs for Java, Javascript, or Python](https://docs.slack.dev/apis/events-api/using-socket-mode#sdks) to handle the details of Socket Mode. The process is streamlined, and you get access to all the other pleasant features of our SDKs.
Apps using Socket Mode are _not_ currently allowed in the public Slack Marketplace.
Socket Mode is **only** available for apps using [granular permissions](https://docs.slack.dev/quickstart).
If you created your app on or after December of 2019, good news: your app already uses the new permissions. Otherwise, you may have to [migrate](https://docs.slack.dev/legacy/legacy-app-migration/migrating-classic-apps) your classic app to use granular permissions before turning on Socket Mode.
## Setting up an app for Socket Mode[​](https://docs.slack.dev/apis/events-api/using-socket-mode#setup "Direct link to Setting up an app for Socket Mode")
App setup for Socket Mode has three steps:
  1. [Create an app](https://docs.slack.dev/apis/events-api/using-socket-mode#creating)
  2. [Toggle on Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode#toggling)
  3. [Generate an app-level token](https://docs.slack.dev/apis/events-api/using-socket-mode#token)


### 1. Create an app[​](https://docs.slack.dev/apis/events-api/using-socket-mode#creating "Direct link to 1. Create an app")
If you don't have one already, you'll need to create a Slack app:
[Create an app](https://api.slack.com/apps?new_app=1)
Fill out your **App Name** and select the Development Workspace where you'll play around and build your app.
Socket Mode apps currently can't be listed in the Slack Marketplace. If you'd like to distribute your Socket Mode app to your entire Enterprise Grid organization, you can [make your app deployable organization-wide](https://docs.slack.dev/enterprise-grid/organization-ready-apps).
#### Creating an app with a manifest[​](https://docs.slack.dev/apis/events-api/using-socket-mode#creating-manifests "Direct link to Creating an app with a manifest")
You can [create an app through a manifest](https://docs.slack.dev/app-manifests/configuring-apps-with-app-manifests) and turn on Socket Mode by configuring a few options. Below is a YAML example which includes adding a bot user with the [`app_mentions:read`](https://docs.slack.dev/reference/scopes/chat.write.customize) scope and subscribing to the [`app_mention`](https://docs.slack.dev/reference/events/app_mention) event subscription:
```
_metadata:major_version:1display_information:name: Demo Appfeatures:bot_user:display_name: Demo Appalways_online:falseoauth_config:scopes:bot:- app_mentions:readsettings:event_subscriptions:bot_events:- app_mentionorg_deploy_enabled:falsesocket_mode_enabled:trueis_hosted:falsetoken_rotation_enabled:false
```

### 2. Toggle on Socket Mode[​](https://docs.slack.dev/apis/events-api/using-socket-mode#toggling "Direct link to 2. Toggle on Socket Mode")
In your [app settings](https://api.slack.com/apps), navigate to the **Socket Mode** section. Toggle the **Enable Socket Mode** button to turn on receiving payloads via WebSockets.
Socket Mode can be toggled on or off whenever you'd like. When you toggle Socket Mode on, you'll **only** receive events and interactive payloads over your WebSocket connections—not over HTTP.
If your app is actively receiving events when you toggle Socket Mode on, you may lose events until you establish a connection to your WebSocket URL.
At this point, you can subscribe to some events in the **Event Subscriptions** section of your app settings. A favorite is the [`app_mention`](https://docs.slack.dev/reference/events/app_mention) event.
When using Socket Mode, your app does not need a Request UR to use the [Events API](https://docs.slack.dev/apis/events-api/). Your app's connection to the WebSocket replaces the need for Slack to dispatch to a Request URL.
### 3. Generate an app-level token[​](https://docs.slack.dev/apis/events-api/using-socket-mode#token "Direct link to 3. Generate an app-level token")
When you toggle Socket Mode on, the app settings will guide you through obtaining an app-level token if you haven't created one.
You can also create or generate an app-level token manually. Under **Basic Information** , scroll to the **App-level tokens** section and click the button to generate an [app-level token](https://docs.slack.dev/authentication/tokens#app).
Your app-level token allows your app, either directly or with an SDK, to generate a WebSocket URL for communication with Slack via the [`apps.connections.open`](https://docs.slack.dev/reference/methods/apps.connections.open) method.
You're finished with setting up your app for Socket Mode. The rest can be handled by [using the Slack SDKs](https://docs.slack.dev/apis/events-api/using-socket-mode#sdks). Or, you can [implement the Socket Mode protocol yourself](https://docs.slack.dev/apis/events-api/using-socket-mode#implementing).
## Using Socket Mode with Bolt SDKs[​](https://docs.slack.dev/apis/events-api/using-socket-mode#sdks "Direct link to Using Socket Mode with Bolt SDKs")
Socket Mode is automatically supported by each of our frameworks and SDKs.
The only thing you need to do is set your app-level token as an environment variable:
```
export SLACK_APP_TOKEN='xapp-***'
```

Now you can lean on the [Bolt framework](https://tools.slack.dev) for [Javascript](https://tools.slack.dev/bolt-js), [Java](https://tools.slack.dev/java-slack-sdk), or [Python](https://tools.slack.dev/bolt-python) to take care of the rest.
Here's some code to get your app capturing events using Socket Mode using Bolt:
  * Java
  * JavaScript
  * Python


```
package hello;import com.slack.api.bolt.App;import com.slack.api.bolt.AppConfig;import com.slack.api.bolt.socket_mode.SocketModeApp;import com.slack.api.model.event.AppMentionEvent;// Required dependencies:// implementation("com.slack.api:bolt-socket-mode:(latest version)")// implementation("org.glassfish.tyrus.bundles:tyrus-standalone-client:1.17")public class MyApp { public static void main(String[] args) throws Exception {  String botToken = System.getenv("SLACK_BOT_TOKEN");  App app = new App(AppConfig.builder().singleTeamBotToken(botToken).build());  String appToken = System.getenv("SLACK_APP_TOKEN");  SocketModeApp socketModeApp = new SocketModeApp(appToken, app);  socketModeApp.start(); }}
```

Code to initialize Bolt app
```
// Require the Node Slack SDK package (github.com/slackapi/node-slack-sdk)const{WebClient,LogLevel}=require("@slack/web-api");// WebClient instantiates a client that can call API methods// When using Bolt, you can use either `app.client` or the `client` passed to listeners.const client =newWebClient("xoxb-your-token",{// LogLevel can be imported and used to make debugging simplerlogLevel:LogLevel.DEBUG});
```

```
const{App}=require('@slack/bolt');const app =newApp({token: process.env.BOT_TOKEN,appToken: process.env.SLACK_APP_TOKEN,socketMode:true,});(async()=>{await app.start();console.log('⚡️ Bolt app started');})();
```

```
import osfrom slack_bolt import Appfrom slack_bolt.adapter.socket_mode import SocketModeHandler# Install the Slack app and get xoxb- token in advanceapp = App(token=os.environ["SLACK_BOT_TOKEN"])if __name__ =="__main__":  SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
```

If a Bolt SDK suits your goals, then you're ready to to continue developing your app as normal! No need to follow the rest of this guide.
## Implementing Socket Mode without Bolt[​](https://docs.slack.dev/apis/events-api/using-socket-mode#implementing "Direct link to Implementing Socket Mode without Bolt")
If you prefer to implement the Socket Mode protocol yourself, read on.
You'll need a library or programming language that supports the [WebSocket](https://tools.ietf.org/html/rfc6455) protocol.
Connections refresh regularly. You should be ready to receive and connect to new WebSocket URLs as quickly as possible to maintain service.
### 1. Call the `apps.connections.open` endpoint[​](https://docs.slack.dev/apis/events-api/using-socket-mode#call "Direct link to call")
Call the [`apps.connections.open`](https://docs.slack.dev/reference/methods/apps.connections.open) endpoint with your app-level token to receive a WebSocket URL:
```
curl -X POST "https://slack.com/api/apps.connections.open" \-H "Content-type: application/x-www-form-urlencoded" \-H "Authorization: Bearer xapp-1-123"
```

Remember to send the token in the `Authorization` header, not as a parameter.
You'll receive a URL in response:
```
{  "ok": true,  "url": "wss:\/\/wss.slack.com\/link\/?ticket=1234-5678"}
```

You'll notice that, with Socket Mode turned on, your app settings doesn't require or even allow you to enter a **Request URL**. That's because this WebSocket URL replaces the public Request URL that Slack would have sent payloads to.
You can turn off Socket Mode **at any time** to return to the direct HTTP protocol for events and interactive features. If you've already set a **Request URL** , it'll be saved for later once you enter Socket Mode. When you turn Socket Mode off, the Request URL will be used once again to receive events.
### 2. Connect to the WebSocket[​](https://docs.slack.dev/apis/events-api/using-socket-mode#connect "Direct link to 2. Connect to the WebSocket")
Use your WebSocket library to connect to the URL specified in the above response.
Here's an example in Javascript:
```
if (response.ok) { let wssUrl = response.url; let socket = new WebSocket(wssUrl); socket.onopen = function(e) {  // connection established } socket.onmessage = function(event) {  // application received message }}
```

One helpful trick: you can append `&debug_reconnects=true` to your WebSocket URL when you connect to it in order to make the connection time significantly shorter (360 seconds). That way, you can test and debug reconnects without waiting around.
After you connect to the WebSocket, Slack will send a `hello` message:
```
{  "type": "hello",  "connection_info": {    "app_id": "A1234"  },  "num_connections": 1,  "debug_info": {    "host": "applink-….",    "started" "2020-10-11 12:12:12.120",    "build_number": 54,    "approximate_connection_time": 3600  }}
```

The `approximate_connection_time` (in seconds) can be used to estimate how long the connection will persist until Slack refreshes it.
### Using multiple connections[​](https://docs.slack.dev/apis/events-api/using-socket-mode#connections "Direct link to Using multiple connections")
Socket Mode allows your app to maintain _up to 10_ open WebSocket connections at the same time.
When multiple connections are active, each payload may be sent to _any_ of the connections. It's best not to assume any particular pattern for how payloads will be distributed across multiple open connections.
There are a few reasons to make use of multiple active connections:
  * If you'd like to handle a scheduled connection restart gracefully, you can generate an additional connection before the restart occurs.
  * If you're having trouble keeping up with a large throughput of events from one connection, multiple connections can allow you to load balance.
  * If you'd like to gracefully restart your app's services, you can use multiple connections for temporary active-active redundancy.


### 3. Handle disconnects gracefully[​](https://docs.slack.dev/apis/events-api/using-socket-mode#disconnect "Direct link to 3. Handle disconnects gracefully")
Expect disconnects to your WebSocket connection. These may happen when you toggle off Socket Mode in the app settings, or for other reasons.
Here's a disconnect message you'll receive if you toggle off Socket Mode:
```
{ "type": "disconnect", "reason": "link_disabled", "debug_info": {  "host": "wss-111.slack.com" }}
```

No matter what, you'll need to handle connection refreshes once every few hours.
You may receive a warning about 10 seconds before the disconnect:
```
{ "type": "disconnect", "reason": "warning", "debug_info": {  "host": "wss-111.slack.com" }}
```

Even if you don't receive a warning, you'll still want to expect a `refresh_requested` message:
```
{ "type" : "disconnect", "reason": "refresh_requested", "debug_info": {  "host": "wss-111.slack.com" }}
```

You may want to use [multiple connections](https://docs.slack.dev/apis/events-api/using-socket-mode#connections) in order to maintain uptime during a connection restart.
### 4. Receive events[​](https://docs.slack.dev/apis/events-api/using-socket-mode#events "Direct link to 4. Receive events")
Event payloads sent to your app via Socket Mode are identical to the typical [Events API](https://docs.slack.dev/apis/events-api/) payloads, with some additional metadata:
```
{ "payload": <event_payload>, "envelope_id": <unique_identifier_string>, "type": <event_type_enum>, "accepts_response_payload": <accepts_response_payload_bool>}
```

You can use the `accepts_response_payload` to determine whether a response can include additional information.
Your app still needs to acknowledge receiving _each event_ so that Slack knows whether to retry.
### 5. Acknowledge events[​](https://docs.slack.dev/apis/events-api/using-socket-mode#acknowledge "Direct link to 5. Acknowledge events")
While acknowledging each event is required, there's no need to verify or validate inbound events, because you're receiving the events over a pre-authenticated WebSocket. Note that this is a different pattern from receiving events directly over HTTP, where validation is required for each event.
Use the `envelope_id` field in the object you receive from your WebSocket to send a response back to Slack acknowledging that you've received the event:
```
{  "envelope_id": <$unique_identifier_string>,  "payload": <$payload_shape> // optional}
```

## Using interactive features[​](https://docs.slack.dev/apis/events-api/using-socket-mode#interactivity "Direct link to Using interactive features")
[Interactive features](https://docs.slack.dev/interactivity) also send payloads as normal to your app—along with additional metadata specific to Socket Mode. Here's the general structure to expect:
```
{ "payload": <interactive_component_payload>, "envelope_id": <unique_identifier_string>, "type": <event_type_enum>, "accepts_response_payload": <accepts_response_payload_bool>}
```

See below for specific examples on the following:
  * [Slash commands](https://docs.slack.dev/apis/events-api/using-socket-mode#command)
  * [Block Kit buttons](https://docs.slack.dev/apis/events-api/using-socket-mode#button)
  * [App Home interactions](https://docs.slack.dev/apis/events-api/using-socket-mode#home)
  * [Modals](https://docs.slack.dev/apis/events-api/using-socket-mode#modal)
  * [Dynamic menus](https://docs.slack.dev/apis/events-api/using-socket-mode#menu)


### Slash commands[​](https://docs.slack.dev/apis/events-api/using-socket-mode#command "Direct link to Slash commands")
Here's what's sent:
```
{ "payload": {  "token": "bHKJ2n9AW6Ju3MjciOHfbA1b",  "team_id": "T123ABC456",  "team_domain": "maria",  "channel_id": "C123ABC456",  "channel_name": "general",  "user_id": "U123ABC456",  "user_name": "rainer",  "command": "/randorilke",  "text": "",  "response_url": "https://rilke.slack.com/commands/T0SNL8S4S/37053613554/YMB2ZESDLNjNLqSFZ1quhNAh",  "trigger_id": "37053613634.26768298162.440952c06ef4de2653466a48fe495f93" }, "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545", "type": "slash_commands", "accepts_response_payload": true}
```

Here's an example response from your app:
```
{ "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545", "payload": {  "blocks": [   {    "type": "section",    "text": {     "type": "mrkdwn",     "text": "Book of Hours"    }   },   {    "type": "section",    "text": {     "type": "mrkdwn",     "text": "Duino Elegies"    }   }  ] }}
```

### Block Kit buttons[​](https://docs.slack.dev/apis/events-api/using-socket-mode#button "Direct link to Block Kit buttons")
Here's what your app receives:
```
{ "payload": {  "type": "block_actions",  "team": {   "id": "T123ABC456",   "domain": "Duino"  },  "user": {   "id": "U123ABC456",   "username": "RMR",   "team_id": "T123ABC456"  },  "api_app_id": "AABA1ABCD",  "token": "9s8d9as89d8as9d8as989",  "container": {   "type": "message_attachment",   "message_ts": "1548261231.000200",   "attachment_id": 1,   "channel_id": "C123ABC456",   "is_ephemeral": false,   "is_app_unfurl": false  },  "trigger_id": "12321423423.333649436676.d8c1bb837935619ccad0f624c448ffb3",  "channel": {   "id": "C123ABC456",   "name": "review-updates"  },  "message": {   "bot_id": "B123ABC456",   "type": "message",   "text": "Who if I cried out would hear me.",   "user": "U123ABC456",   "ts": "1548261231.000200",   ...  },  "response_url": "https://hooks.slack.com/actions/AABA1ABCD/1232321423432/D09sSasdasdAS9091209",  "actions": [{   "action_id": "WaXA",   "block_id": "=qXel",   "text": {    "type": "plain_text",    "text": "View",    "emoji": true   },   "value": "click_me_123",   "type": "button",   "action_ts": "1548426417.840180"  }] }, "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545", "type": "interactive", "accepts_response_payload": true}
```

Here's an example response from your app:
```
{ "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545"}
```

### App Home interactions[​](https://docs.slack.dev/apis/events-api/using-socket-mode#home "Direct link to App Home interactions")
Here's what your app receives:
```
{ "payload": {  "type": "app_home_opened",  "user": "U123ABC456",  "channel": "C123ABC456",  "event_ts": "1515449522000016",  "tab": "home",  "view": {   "id": "V123ABC456",   "team_id": "T123ABC456",   "type": "home",   "blocks": [    ...   ],   "private_metadata": "",   "callback_id": "",   "state":{    ...   },   "hash":"1231232323.12321312",   "clear_on_close": false,   "notify_on_close": false,   "root_view_id": "V123ABC456",   "app_id": "A123ABC456",   "external_id": "",   "app_installed_team_id": "T123ABC456",   "bot_id": "B123ABC456"  } } "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545", "type": "events_api", "accepts_response_payload": false}
```

Here's an example response from your app:
```
{ "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545"}
```

### Modals[​](https://docs.slack.dev/apis/events-api/using-socket-mode#modal "Direct link to Modals")
Here's what your app receives:
```
{ "payload": {  "type": "view_submission",  "team": { ... },  "user": { ... },  "view": {   "id": "V123ABC456",   "type": "modal",   "title": { ... },   "submit": { ... },   "blocks": [ ... ],   "private_metadata": "shhh-its-secret",   "callback_id": "modal-with-inputs",   "state": {    "values": {     "multi-line": {      "ml-value": {       "type": "plain_text_input",       "value": "Archaic torso of Apollo"      }     }    }   },   "hash": "156663117.cd33ad1f"  } }, "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545", "type": "interactive", "accepts_response_payload": true}
```

Here's an example response from your app:
```
{ "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545", "payload": {  "response_action": "update",  "view": {   "type": "modal",   "callback_id": "updated-view-id",   "title": {    "type": "plain_text",    "text": "Updated view"   },   "blocks": [{    "type": "section",    "text": {     "type": "plain_text",     "text": "You must change your life."    }   }]  } }}
```

### Dynamic menus[​](https://docs.slack.dev/apis/events-api/using-socket-mode#menu "Direct link to Dynamic menus")
Here's what your app receives:
```
{ "payload": {  "type": "block_suggestion",  "user": {   "id": "U123ABC456",   "name": "panther"  },  "team": {   "id": "T123ABC456",   "domain": "rilke"  },  "block_id": "search-block",  "action_id": "seach-action",  "value": "an",  "view": {"id": "V111", "type": "modal", "callback_id": "view-id"} }, "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545", "type": "interactive", "accepts_response_payload": true}
```

Here's an example response from your app:
```
{ "envelope_id": "dbdd0ef3-1543-4f94-bfb4-133d0e6c1545", "payload": {  "options": [   {    "text": {     "type": "plain_text",     "text": "Give me your hand"    },    "value": "AI-2323"   },   {    "text": {     "type": "plain_text",     "text": "Beauty and terror"    },    "value": "SUPPORT-42"   }  ] }}
```

[PreviousUsing HTTP Request URLs](https://docs.slack.dev/apis/events-api/using-http-request-urls)[NextOverview](https://docs.slack.dev/apis/slack-connect/)
  * [Setting up an app for Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode#setup)
    * [1. Create an app](https://docs.slack.dev/apis/events-api/using-socket-mode#creating)
    * [2. Toggle on Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode#toggling)
    * [3. Generate an app-level token](https://docs.slack.dev/apis/events-api/using-socket-mode#token)
  * [Using Socket Mode with Bolt SDKs](https://docs.slack.dev/apis/events-api/using-socket-mode#sdks)
  * [Implementing Socket Mode without Bolt](https://docs.slack.dev/apis/events-api/using-socket-mode#implementing)
    * [1. Call the `apps.connections.open` endpoint](https://docs.slack.dev/apis/events-api/using-socket-mode#call)
    * [2. Connect to the WebSocket](https://docs.slack.dev/apis/events-api/using-socket-mode#connect)
    * [Using multiple connections](https://docs.slack.dev/apis/events-api/using-socket-mode#connections)
    * [3. Handle disconnects gracefully](https://docs.slack.dev/apis/events-api/using-socket-mode#disconnect)
    * [4. Receive events](https://docs.slack.dev/apis/events-api/using-socket-mode#events)
    * [5. Acknowledge events](https://docs.slack.dev/apis/events-api/using-socket-mode#acknowledge)
  * [Using interactive features](https://docs.slack.dev/apis/events-api/using-socket-mode#interactivity)
    * [Slash commands](https://docs.slack.dev/apis/events-api/using-socket-mode#command)
    * [Block Kit buttons](https://docs.slack.dev/apis/events-api/using-socket-mode#button)
    * [App Home interactions](https://docs.slack.dev/apis/events-api/using-socket-mode#home)
    * [Modals](https://docs.slack.dev/apis/events-api/using-socket-mode#modal)
    * [Dynamic menus](https://docs.slack.dev/apis/events-api/using-socket-mode#menu)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



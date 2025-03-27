---
url: https://docs.slack.dev/quickstart
session_id: slack_api_docs
updated_dt: 2025-03-27T13:26:06.940393
---
[Skip to main content](https://docs.slack.dev/quickstart#__docusaurus_skipToContent_fallback)
[![Slack Developer Docs](https://docs.slack.dev/img/logos/slack-developers-white.png)![Slack Developer Docs](https://docs.slack.dev/img/logos/slack-developers-white.png)](https://slack.dev)[Docs](https://docs.slack.dev/)[Reference](https://docs.slack.dev/reference)[Samples](https://docs.slack.dev/samples)[Changelog](https://docs.slack.dev/changelog)
[Tools](https://tools.slack.dev)[Developer Program](https://api.slack.com/developer-program)[Your apps](https://api.slack.com/apps)
Search
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
  * Quickstart


On this page
# Quickstart
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
In the following guide, you'll create a basic Slack app that can send messages using webhooks.
## 1. Creating an app[​](https://docs.slack.dev/quickstart#creating "Direct link to 1. Creating an app")
Create a Slack app via the apps page by selecting the following button:
[Create an app](https://api.slack.com/apps?new_app=1)
  1. Select **From scratch**.
  2. Enter your **App Name**. For this example, enter "Grocery Reminders".
  3. Select the **Workspace** where you'll be developing your app. You'll be able to [distribute your app](https://docs.slack.dev/distribution) to other workspaces later if you choose.
  4. Select **Create App**.


If you need to update the name of your app later, you can do so from your app's [**Home tab**](https://docs.slack.dev/surfaces/app-home#home-tab). Changing the _app name_ entry under **Basic Information** will update the bot name rather than the app name — this is the name that appears when the app performs actions such as posting in a channel or sending a direct message.
## 2. Requesting scopes[​](https://docs.slack.dev/quickstart#scopes "Direct link to 2. Requesting scopes")
Next, you'll need to request [**scopes**](https://docs.slack.dev/reference/scopes) for your app. Scopes give your app permission to perform actions, such as posting messages in your workspace.
Slack apps can't post to any public channel by default; they gain that ability by asking for permission explicitly with the use of scopes. Request the [`chat:write.public`](https://docs.slack.dev/reference/scopes/chat.write.public) scope to gain the ability to post in all public channels without joining. Otherwise, you'll need to use the [`conversations.join`](https://docs.slack.dev/reference/methods/conversations.join) scope, or have your app invited into a channel by a user before it can post.
  1. Within **OAuth & Permissions**, scroll down to **Scopes**.
  2. Under **Bot Token Scopes** , select **Add an OAuth Scope**.
  3. To allow your app to post messages, add the [`chat:write`](https://docs.slack.dev/reference/scopes/chat.write) scope.
  4. To allow your app to access public Slack channels, add the [`channels:read`](https://docs.slack.dev/reference/scopes/channels.read) scope.


In general, you'll add scopes to your bot token, not your user token. A notable exception is if you need to act as a specific user (for example, posting messages on behalf of a user, or setting a user's status).
Slack apps cannot access the [Real Time Messaging (RTM) API](https://docs.slack.dev/legacy/legacy-rtm-api)
The [Events API](https://docs.slack.dev/apis/events-api/) allows your app to listen to Slack events in a structured, safe way. If you require access to RTM (for example, because you're building your app behind a corporate firewall), you'll need to create a legacy Slack app and use its bot token to call [`rtm.connect`](https://docs.slack.dev/reference/methods/rtm.connect). For more information, refer to [Legacy: Real Time Message API](https://docs.slack.dev/legacy/legacy-rtm-api).
## 3. Installing and authorizing the app[​](https://docs.slack.dev/quickstart#installing "Direct link to 3. Installing and authorizing the app")
  1. Return to the **Basic Information** section of the app management page.
  2. Install your app by selecting the **Install to Workspace** button.
  3. You'll now be sent through the Slack OAuth flow. Select **Allow** on the following screen.


When you follow this flow, you're playing the part of the _installing user_ , not the app. If you were adding your app to a different workspace besides your own, this flow would be completed by a user _from that workspace_ instead of you.
After installation, navigate back to the **OAuth & Permissions** page. You'll see an **access token** under **OAuth Tokens**.
Access tokens represent the permissions delegated to your app by the installing user. Keep it secret. Keep it safe. At a minimum, avoid checking them into public version control. Instead, access them via an environment variable.
Your access token allows you to call the methods described by the scopes you requested. For example, your [`chat:write`](https://docs.slack.dev/reference/scopes/chat.write) scope allows your app to post messages.
Your app isn't a member of any channels yet, so pick a channel to add some test messages in and `/invite` your app as in the following example slash command:
```
/invite @Grocery Reminders
```

You'll see a message posted in the channel confirming that your app was added.
## 4. Configuring the app for event listening[​](https://docs.slack.dev/quickstart#listening "Direct link to 4. Configuring the app for event listening")
Slack apps listen and respond to events. We've already touched on one way an app can respond: by calling [`chat.postMessage`](https://docs.slack.dev/reference/methods/chat.postMessage) to post a message. Apps can also respond to events such as mentions in a channel, menu selections, or users sending the app a direct message. Apps listen with the [Events API](https://docs.slack.dev/apis/events-api/). Let's subscribe to the [`app_mention`](https://docs.slack.dev/reference/events/app_mention) event.
  1. Select **Event Subscriptions** and toggle **Enable Events** to ON.
  2. Within **Subscribe to bot events** , select **Add Bot User Event** , then search for `app_mention`. As with scopes, always subscribe to events with a _bot user_.
  3. Next, set the **Request URL** to a URL where your app's server listens to incoming HTTP requests. Slack will send an HTTP request there when your app is mentioned, allowing your app to determine how it will respond. Note that you'll need to implement your own server for this step, as well as to send messages with webhooks. You may want to explore the [Bolt family of SDKs](https://tools.slack.dev), which can allow you to implement a server that listens for events automatically.


You'll notice that the `app_mention` event requires the [`app_mentions:read`](https://docs.slack.dev/reference/scopes/app_mentions.read) scope. Events are like API methods: they allow your app access to information in Slack, so you'll need permissions for them. Reinstall your app to the workspace with this new scope. Now you'll be notified when your app is mentioned, and can determine how your app will respond.
## 5. Sending a message with a webhook[​](https://docs.slack.dev/quickstart#webhooks "Direct link to 5. Sending a message with a webhook")
  1. Select **Incoming Webhooks** and toggle **Activate Incoming Webhooks** to ON.
  2. Select **Add New Webhook to Workspace** to start the webhook flow. Select the channel you previously invited your app to and then **Allow** on the following screen.
  3. Reinstall your app to the workspace with this new feature by selecting **Reinstall to Workspace** within the **Install Your app** section under **Basic Information**.
  4. Navigate back to **Incoming Webhooks** and view the new entry listed under **WebHook URLs for Your Workspace**. Copy your webhook.
  5. Create a new HTTP POST request with the webhook as follows:


```
POST https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXXContent-type: application/json{  "text": "Gotta get the bread and milk!"}
```

Navigate to the channel your app was installed in to see the message posted by your app:
![Bot avatar](https://docs.slack.dev/assets/images/oslo-a00c12051fc200241f7e93ef34b42714.png)
Oslo
Gotta get the bread and milk! 
## Onward[​](https://docs.slack.dev/quickstart#onward "Direct link to Onward")
Congratulations on creating your very own Slack app! Keep learning about all the things your app can do by checking out the following:
  * [Sending messages using Incoming Webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks)
  * [Designing Slack apps](https://docs.slack.dev/surfaces/app-design)
  * [App interactivity overview](https://docs.slack.dev/interactivity)
  * [Building with Block Kit](https://docs.slack.dev/block-kit)


[PreviousSlack platform](https://docs.slack.dev/)[NextFAQ](https://docs.slack.dev/faq)
  * [1. Creating an app](https://docs.slack.dev/quickstart#creating)
  * [2. Requesting scopes](https://docs.slack.dev/quickstart#scopes)
  * [3. Installing and authorizing the app](https://docs.slack.dev/quickstart#installing)
  * [4. Configuring the app for event listening](https://docs.slack.dev/quickstart#listening)
  * [5. Sending a message with a webhook](https://docs.slack.dev/quickstart#webhooks)
  * [Onward](https://docs.slack.dev/quickstart#onward)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



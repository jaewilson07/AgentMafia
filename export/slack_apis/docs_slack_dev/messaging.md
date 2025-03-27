---
url: https://docs.slack.dev/messaging
session_id: slack_api_docs
updated_dt: 2025-03-27T13:26:08.689944
---
[Skip to main content](https://docs.slack.dev/messaging#__docusaurus_skipToContent_fallback)
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
    * [Overview](https://docs.slack.dev/messaging/)
    * [Creating interactive messages](https://docs.slack.dev/messaging/creating-interactive-messages)
    * [Formatting message text](https://docs.slack.dev/messaging/formatting-message-text)
    * [Modifying messages](https://docs.slack.dev/messaging/modifying-messages)
    * [Sending and scheduling messages](https://docs.slack.dev/messaging/sending-and-scheduling-messages)
    * [Sending messages using incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks)
    * [Retrieving messages](https://docs.slack.dev/messaging/retrieving-messages)
    * [Working with files](https://docs.slack.dev/messaging/working-with-files)
    * [Message metadata](https://docs.slack.dev/messaging/message-metadata/)
    * [Unfurling links in messages](https://docs.slack.dev/messaging/unfurling-links-in-messages)
    * [Migrating outmoded message compositions to blocks](https://docs.slack.dev/messaging/migrating-outmoded-message-compositions-to-blocks)
  * [Slack Marketplace](https://docs.slack.dev/slack-marketplace/)
  * [Surfaces](https://docs.slack.dev/surfaces/)
  * [Tools & SDKs](https://docs.slack.dev/tools/)
  * [Workflows](https://docs.slack.dev/workflows/)
  * [Legacy](https://docs.slack.dev/legacy/)


  * [](https://docs.slack.dev/)
  * Messaging


On this page
# Messaging
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
Messages are at the core of how you communicate in Slack. They have many shapes and sizes and varying levels of complexity. They can exist merely to notify, or they can invite and await response.
The core functionality of most Slack apps will involve the publication or consumption of messages. In this overview, we give you a quick trip through the basics of doing these things and an introduction to the terminology that surrounds messaging.
These instructions pertain to content posted programmatically to Slack. For instructions on sending and reading messages within Slack itself, consult this [help center article](https://slack.com/help/articles/201457107-Send-and-read-messages).
## The mechanics of messaging[​](https://docs.slack.dev/messaging#message "Direct link to The mechanics of messaging")
There can be a huge variation in how messages appear. For example, this is a message:
![A message with just text](https://docs.slack.dev/assets/images/basic_message_example-edfb95fc4fcd63d59db3d0a48b919e02.png)
And so is this:
![A complex message with formatted text and interactive elements contained in multiple blocks](https://docs.slack.dev/assets/images/complex_message_example-7741d626507be6645aeafbab6b52755b.png)
At a basic level, messages are a series of attributes which describe and contain content.
Slack apps can [publish new messages](https://docs.slack.dev/messaging/sending-and-scheduling-messages), and [retrieve](https://docs.slack.dev/messaging/retrieving-messages) or [modify](https://docs.slack.dev/messaging/modifying-messages) existing ones.
[Workflow automations](https://docs.slack.dev/workflows) can also send messages with a variety of [built-in Slack functions](https://tools.slack.dev/deno-slack-sdk/reference/slack-functions?filter=Messaging).
Both types of apps have access to a range of [formatting](https://docs.slack.dev/messaging/formatting-message-text) and [interactivity](https://docs.slack.dev/interactivity) options for controlling the look and feel of messages. You can read the overview guides for those topics to get a better sense of what is possible, but for now let's learn about the environment that messages exist in.
### Conversations[​](https://docs.slack.dev/messaging#conversations "Direct link to Conversations")
In Slack, messages inhabit conversations. A [conversation](https://docs.slack.dev/reference/objects/conversation-object) is a catch-all term that covers [public channels](https://slack.com/help/articles/201402297-Create-a-channel), [private channels](https://slack.com/help/articles/201402297-Create-a-channel), [direct message conversations](https://slack.com/help/articles/213817348-Slack-glossary#D), and [group (or multi-party) direct message conversations](https://slack.com/help/articles/213817348-Slack-glossary#G).
[Slack apps can publish messages](https://docs.slack.dev/messaging/sending-and-scheduling-messages) to all these types conversations, and can even create a [direct message conversation](https://slack.com/help/articles/213817348-Slack-glossary#D) between a user and the app itself.
Different conversations will have varying levels of visibility and publishing permission, which is important when you're trying to create messages programmatically; we cover this more in our [sending messages guide](https://docs.slack.dev/messaging/sending-and-scheduling-messages).
With the right permissions, you can [retrieve a conversation's message history](https://docs.slack.dev/messaging/retrieving-messages#conversations), or individual messages within that history, which we cover in our [retrieving messages guide](https://docs.slack.dev/messaging/retrieving-messages#individual_messages).
### Ephemeral messages[​](https://docs.slack.dev/messaging#ephemeral "Direct link to Ephemeral messages")
While most messages will be visible to everyone within the [conversation](https://docs.slack.dev/messaging#conversations) they're published in, apps also have the ability to show a message temporarily to one specific user.
These are called **ephemeral messages** , and in most other respects they're like any other message - composed in the same way, published in much the same way, and viewed within the same types of conversations in Slack.
The only differences are that only one user within that conversation will see them, and that they do not persist across reloads, between desktop and mobile apps, or across sessions. Once the session is closed (for example, the user reloads the app or logs out and back in), ephemeral messages will disappear and cannot be recovered.
Use ephemeral messages when you want to send someone a context-sensitive message that isn't suitable for the wider conversation. For example, if a user invokes one of your app's [slash commands](https://docs.slack.dev/interactivity/implementing-slash-commands) that performs some action on a third-party service, an ephemeral message might be the most suitable way to inform that user of the success of the action.
Ephemeral messages should only ever be sent in response to some user action, they must never be unexpected or unsolicited. If you want to send a message to a specific user in any other situation, [send them a DM](https://docs.slack.dev/messaging/sending-and-scheduling-messages#conversations).
Due to their ghostly nature, ephemeral messages cannot be retrieved via our APIs, nor will they show up in [interaction payloads](https://docs.slack.dev/messaging/creating-interactive-messages#request).
Deleting or updating ephemeral messages is a bit more complicated — you can do it, but only in response to an [interaction](https://docs.slack.dev/messaging/creating-interactive-messages) with the message itself. [Read our guide](https://docs.slack.dev/messaging/modifying-messages) to learn more about [deleting](https://docs.slack.dev/messaging/modifying-messages#deleting_response_url) or [updating](https://docs.slack.dev/messaging/modifying-messages#updating_response_url) messages in response to interactions.
### Threading messages[​](https://docs.slack.dev/messaging#threading "Direct link to Threading messages")
Most messages stand alone, seen or unseen, inside a conversation. Some messages, however, generate such conversation that replies erupt forth, forming a thread in their wake.
![a threaded message, with replies waiting. &quot;What happened to batch 41?&quot;](https://docs.slack.dev/assets/images/message_thread-3f5e29d28002d28461453d7e1cb8de32.png)
Slack apps can read and write messages in threads with ease. Before we explain how, let's tread some thread terminology:
  * Before a message has any replies, we call it an **unthreaded message**.
  * Once a message has replies, it becomes a **parent message**.
  * Any child messages of that parent message are called **threaded replies**.
  * The whole bundle of parent message and replies is referred to as a **thread**
  * Each of the messages within a thread, whether parent or reply, is a **threaded message**.


To learn how your app can spot and retrieve threaded messages, read our [retrieving messages guide](https://docs.slack.dev/messaging/retrieving-messages#finding_threads). Or if you want to find out how to publish messages as threaded replies, read our [sending messages guide](https://docs.slack.dev/messaging/sending-and-scheduling-messages#threading).
## Message structure and formatting[​](https://docs.slack.dev/messaging#structure "Direct link to Message structure and formatting")
![A message with basic formatting](https://docs.slack.dev/assets/images/composition_overview_basic_formatting-14d30381d05fa88201335b56decfe1b7.png)
The base message is a plain, unformatted string of text — just like this paragraph.
You can easily introduce a bit of **boldness** or some _emphasis_ to make those messages easier to read and understand. You might also want to include some `inline code`, add an emoji 💡, or lay things out in a list:
  1. **Add some bold text**
  2. _Add some italicized text_
  3. `Add some inline code`


To accomplish this formatting and more, Slack apps can use a markup style in message text called **`mrkdwn`**.
[Read our formatting text for app surfaces guide](https://docs.slack.dev/messaging/formatting-message-text) to learn more.
### Advanced formatting[​](https://docs.slack.dev/messaging#advanced_formatting "Direct link to Advanced formatting")
![A message with advanced formatting](https://docs.slack.dev/assets/images/composition_overview_advanced_formatting-337df3b7b2a975b97d2147185d7a0ae5.png)
Beyond changing the _appearance_ of text, there are also **parsing options** that can turn text into something more useful.
You can use special sequences of characters to:
  * [Enable links](https://docs.slack.dev/messaging/formatting-message-text#linking-urls)
  * [Format timestamps as more readable strings](https://docs.slack.dev/messaging/formatting-message-text#date-formatting)
  * [Link to Slack conversations](https://docs.slack.dev/messaging/formatting-message-text#linking-channels)
  * [Mention Slack users or groups](https://docs.slack.dev/messaging/formatting-message-text#mentioning-users)


[Read our advanced formatting guide](https://docs.slack.dev/messaging/formatting-message-text#advanced) to learn more about these options.
### Complex message layouts[​](https://docs.slack.dev/messaging#complex_layouts "Direct link to Complex message layouts")
![A complex message layout that uses blocks](https://docs.slack.dev/assets/images/composition_overview_block_layout-0155c52f58d0bb65422495e8b9f5b1ec.png)
Messages don’t have to be just text notifications, though. They can include rich formatting and complex user interfaces. To create these types of messages, you’ll use a UI framework we call [Block Kit](https://docs.slack.dev/block-kit). These powerful building blocks for messages allow you to build complete workflows right inside Slack, that work just as well on our mobile devices as they do on your desktop, without any additional code or configuration.
As the name implies, you build messages out of individual (or groups of) pre-defined blocks such as text, thumbnail images, dividers, and interactive elements like buttons, dropdown menus, and date pickers. Even with a relatively small number of starting blocks, it's possible to customize interfaces unique to the needs of your workflow.
Block Kit UI's are defined as JSON. We also have a tool called [Block Kit Builder](https://api.slack.com/tools/block-kit-builder) for creating sample messages that will generate the corresponding JSON automatically. This is great for letting anyone on your team sketch out some ideas for messages and then copy and paste the resulting JSON.
Learn how to use these features to maximize your messaging magic by [reading our guide to using blocks in message layouts](https://docs.slack.dev/messaging#complex_layouts).
Block Kit also opens your app's messages up to possible participation, with **interactive components** that enable workflows and integrations to be stitched right into the message.
[Read more about these in our separate overview of making messages interactive](https://docs.slack.dev/messaging/creating-interactive-messages) for Slack apps or [Creating an interactive message](https://tools.slack.dev/deno-slack-sdk/guides/creating-an-interactive-message) for workflow automations.
## Many ways to send messages[​](https://docs.slack.dev/messaging#sending_methods "Direct link to Many ways to send messages")
There are many ways to send a message with the Slack platform. Below are links to the guides for each of the various methods that allow for the publishing of messages.
Method| Description  
---|---  
[`chat.postMessage`](https://docs.slack.dev/reference/methods/chat.postMessage)| A [Web API](https://docs.slack.dev/apis/web-api/) method that sends a message to a conversation. We used this above.  
[`chat.postEphemeral`](https://docs.slack.dev/reference/methods/chat.postEphemeral)| A [Web API](https://docs.slack.dev/apis/web-api/) method that sends an [ephemeral message](https://docs.slack.dev/messaging#ephemeral) to a conversation.  
[Incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks)| A uniquely generated URL that is tied to a specific conversation. Send an HTTP POST to one to publish a message.  
[`response_url`](https://docs.slack.dev/interactivity/handling-user-interaction#message_responses)| A callback URL that you can use to post a response to a [message interaction](https://docs.slack.dev/interactivity/handling-user-interaction#message_responses). You're going to use this a lot if you publish [interactive messages](https://docs.slack.dev/messaging/creating-interactive-messages).  
[Legacy: Real Time Messaging API](https://docs.slack.dev/legacy/legacy-rtm-api#sending_messages)| This API does not support layout blocks or attachments. We don't recommend you use it for messaging, but it does exist, so we'd be remiss if we didn't mention it.  
Broadcast messages within the Messages tab| Apps can send messages in the Messages tab without listening for a reply back from a user.  
[Built-in Slack functions](https://tools.slack.dev/deno-slack-sdk/reference/slack-functions)| For use in Slack-hosted Deno SDK-built apps.  
## Message payloads[​](https://docs.slack.dev/messaging#payloads "Direct link to Message payloads")
All of the Slack APIs that publish messages use a common base structure, called a **message payload**. This is a JSON object that is used to define metadata about the message, such as where it should be published, as well as its visual composition.
This is a list of the fields available in that common structure, but you should also consult the [reference docs for any messaging APIs](https://docs.slack.dev/messaging/sending-and-scheduling-messages#sending_methods) you are using to see if there are any additional fields required by those methods. For example, if you're [using the Web API to send messages](https://docs.slack.dev/messaging/sending-and-scheduling-messages#getting_started), you'll also need to specify the `channel` where the message should be published.
Field| Type| Required?| Description  
---|---|---|---  
`text`| String| Yes| The usage of this field changes depending on whether you're using `blocks` or not. If you are, this is used as a fallback string to display in notifications. If you aren't, this is the main body text of the message. It can be formatted as plain text, or with [`mrkdwn`](https://docs.slack.dev/messaging/formatting-message-text#basics). This field is not enforced as required when using `blocks`, however it is highly recommended that you include it as the aforementioned fallback.  
`blocks`| Array| No| An array of [layout blocks](https://docs.slack.dev/reference/block-kit/blocks) in the same format [as described in the building blocks guide](https://docs.slack.dev/block-kit).  
`attachments`| Array| No| An array of [legacy secondary attachments](https://docs.slack.dev/legacy/legacy-messaging/legacy-secondary-message-attachments). We recommend you use `blocks` instead.  
`thread_ts`| String| No| The [ID of another un-threaded message](https://docs.slack.dev/messaging#threading) to reply to.  
`mrkdwn`| Boolean| No| Determines whether the `text` field is rendered according to [`mrkdwn` formatting or not](https://docs.slack.dev/messaging/formatting-message-text#basics). Defaults to `true`.  
[PreviousDeep linking into Slack](https://docs.slack.dev/interactivity/deep-linking)[NextOverview](https://docs.slack.dev/messaging/)
  * [The mechanics of messaging](https://docs.slack.dev/messaging#message)
    * [Conversations](https://docs.slack.dev/messaging#conversations)
    * [Ephemeral messages](https://docs.slack.dev/messaging#ephemeral)
    * [Threading messages](https://docs.slack.dev/messaging#threading)
  * [Message structure and formatting](https://docs.slack.dev/messaging#structure)
    * [Advanced formatting](https://docs.slack.dev/messaging#advanced_formatting)
    * [Complex message layouts](https://docs.slack.dev/messaging#complex_layouts)
  * [Many ways to send messages](https://docs.slack.dev/messaging#sending_methods)
  * [Message payloads](https://docs.slack.dev/messaging#payloads)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



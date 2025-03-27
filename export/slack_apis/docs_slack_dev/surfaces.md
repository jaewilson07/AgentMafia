---
url: https://docs.slack.dev/surfaces
session_id: slack_api_docs
updated_dt: 2025-03-27T13:26:18.794193
---
[Skip to main content](https://docs.slack.dev/surfaces#__docusaurus_skipToContent_fallback)
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
    * [Overview](https://docs.slack.dev/surfaces/)
    * [Modals](https://docs.slack.dev/surfaces/modals)
    * [App Home](https://docs.slack.dev/surfaces/app-home)
    * [Canvases](https://docs.slack.dev/surfaces/canvases)
    * [App design](https://docs.slack.dev/surfaces/app-design)
  * [Tools & SDKs](https://docs.slack.dev/tools/)
  * [Workflows](https://docs.slack.dev/workflows/)
  * [Legacy](https://docs.slack.dev/legacy/)


  * [](https://docs.slack.dev/)
  * Surfaces


On this page
# Surfaces
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
Create welcoming spaces for people to use your Slack app on a variety of surfaces. **Surfaces** are places where your app can express itself through communication or interaction with your users.
Most surfaces can be built using [Block Kit](https://docs.slack.dev/block-kit) layout blocks and elements. Our [guide to building block layouts](https://docs.slack.dev/block-kit) will help you learn how. Canvases, on the other hand, use [markdown](https://docs.slack.dev/messaging/formatting-message-text#basic-formatting) for content formatting.
## Messages[​](https://docs.slack.dev/surfaces#messages "Direct link to Messages")
App-published messages are dynamic yet transient spaces. They allow users to complete workflows as Slack conversations.
Apps can [ send messages](https://docs.slack.dev/messaging) whenever they want to, as long as they have the relevant permissions and access. Our [guide to formatting text for app surfaces](https://docs.slack.dev/messaging/formatting-message-text) will show you what formatting is possible.
When an app is invoked, it can respond with a message. Further action can flow from that message, forming a conversational interface connected to any of Slack's features.
![](https://docs.slack.dev/assets/images/message-abstract-179ebdeb187c4f8c2246e9b0ec40c771.png)
➡️ **To get started with messages** , read our [Messages guide](https://docs.slack.dev/messaging).
✨ **To level up your messages with interactive components such as buttons and select menus** , read our Creating interactive messages guide for traditional [Slack apps](https://docs.slack.dev/messaging/creating-interactive-messages) or [workflow automations](https://tools.slack.dev/deno-slack-sdk/guides/creating-an-interactive-message).
## Modals[​](https://docs.slack.dev/surfaces#modals "Direct link to Modals")
Modals are prominent and pervasive spaces ideal for requesting and collecting data from users, or temporarily displaying dynamic and interactive information.
Modals appear in front of any other interface element in Slack. As a result, they are short-lived and invoked only when a specific task is to be completed. Apps can _only_ create modals in response to [user invocation](https://docs.slack.dev/interactivity#user), such as a [shortcut](https://docs.slack.dev/interactivity/implementing-shortcuts).
Modals contain one to three [**views**](https://docs.slack.dev/surfaces/modals#lifecycle) that can be chained together to create complex, non-linear workflows.
![](https://docs.slack.dev/assets/images/modal-abstract-380015b1a576a131176eebb529d1fab0.png)
➡️ **To get started with modals** , read our [Modals guide](https://docs.slack.dev/surfaces/modals).
## App Home[​](https://docs.slack.dev/surfaces#app-home "Direct link to App Home")
The App Home is a private, one-to-one space in Slack shared by a user and an app. The Home tab, a specific App Home view, is an optional ever-present space, retaining its content and state until the app chooses to update it.
Present each of your users with a unique Home tab just for them, always found in the same place.
Although not every app needs to have a Home tab, the 'always-on' nature of the space makes it an important surface for many Slack apps.
The App Home is not available for workflow apps.
![](https://docs.slack.dev/assets/images/app_home_abstract-38f03507602f3dd0afcfb4183eb8d6cc.png)
➡️ **To get started with App Home** , read our [App Home guide](https://docs.slack.dev/surfaces/app-home).
## Canvases[​](https://docs.slack.dev/surfaces#canvases "Direct link to Canvases")
Canvases are built-in documents in Slack, existing either tied to a channel or as a standalone space.
Use canvases to store channel guidelines or instructions, welcome new team members with an onboarding flow, or present project updates with canvases. Add links to team resources, helpful videos, and even kick off a workflow from a canvas.
![](https://docs.slack.dev/assets/images/canvas-b3a55e36a72cc8e34708ddb2dc8fcac8.png)
➡️ **To get started with canvases** , read our [Canvas guide](https://docs.slack.dev/surfaces/canvases).
## Using app surfaces together[​](https://docs.slack.dev/surfaces#next "Direct link to Using app surfaces together")
App surfaces can also be used together to create a rich interactive experience for your users. For example, imagine the following Task App, which presents a task dashboard that resides in the app's [Home tab](https://docs.slack.dev/surfaces/app-home):
  1. A user can click a [button](https://docs.slack.dev/reference/block-kit/block-elements/button-element) to add a task.
  2. The user is then presented with a [modal](https://docs.slack.dev/surfaces/modals) to [enter](https://docs.slack.dev/reference/block-kit/blocks/input-block) some [plain text](https://docs.slack.dev/reference/block-kit/block-elements/plain-text-input-element) and [select from a list of categories](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element).
  3. Upon submitting, a [message](https://docs.slack.dev/messaging) is sent to a triage channel elsewhere in Slack.
  4. Finally, a different user in the triage channel can click a [button](https://docs.slack.dev/reference/block-kit/block-elements/button-element) to claim that task.


Explore all the possibilities and get some tips and inspiration by reading our [guides to planning Slack apps](https://docs.slack.dev/surfaces/app-design).
[PreviousSlack Security Review](https://docs.slack.dev/slack-marketplace/marketplace-terms-conditions/slack-security-review)[NextOverview](https://docs.slack.dev/surfaces/)
  * [Messages](https://docs.slack.dev/surfaces#messages)
  * [Modals](https://docs.slack.dev/surfaces#modals)
  * [App Home](https://docs.slack.dev/surfaces#app-home)
  * [Canvases](https://docs.slack.dev/surfaces#canvases)
  * [Using app surfaces together](https://docs.slack.dev/surfaces#next)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



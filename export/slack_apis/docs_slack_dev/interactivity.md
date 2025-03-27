---
url: https://docs.slack.dev/interactivity
session_id: slack_api_docs
updated_dt: 2025-03-27T13:25:48.435342
---
[Skip to main content](https://docs.slack.dev/interactivity#__docusaurus_skipToContent_fallback)
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
    * [Interactivity overview](https://docs.slack.dev/interactivity/)
    * [Handling user interaction in your Slack apps](https://docs.slack.dev/interactivity/handling-user-interaction)
    * [Implementing shortcuts](https://docs.slack.dev/interactivity/implementing-shortcuts)
    * [Implementing slash commands](https://docs.slack.dev/interactivity/implementing-slash-commands)
    * [Adding interactive modals to the Home tab](https://docs.slack.dev/interactivity/adding-interactive-modals-to-home-tab)
    * [Deep linking into Slack](https://docs.slack.dev/interactivity/deep-linking)
  * [Messaging](https://docs.slack.dev/messaging/)
  * [Slack Marketplace](https://docs.slack.dev/slack-marketplace/)
  * [Surfaces](https://docs.slack.dev/surfaces/)
  * [Tools & SDKs](https://docs.slack.dev/tools/)
  * [Workflows](https://docs.slack.dev/workflows/)
  * [Legacy](https://docs.slack.dev/legacy/)


  * [](https://docs.slack.dev/)
  * Interactivity


On this page
# Interactivity overview
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
Both Slack apps and [workflow automations](https://docs.slack.dev/workflows) can be invoked automatically (like a scheduled message) or by a user (like by clicking a shortcut). All Slack apps can also use interactive features to achieve much more than just one-way communication.
An injection of interactivity invites and inspires action (and reaction). Best of all, users never have to depart from the comfort of Slack to get things done.
The interactive flow between Slack apps and users is a two-step process:
  1. Something happens that [**invokes**](https://docs.slack.dev/interactivity#triggers) the app or interaction.
  2. The app [**responds**](https://docs.slack.dev/interactivity#responses) to the interaction.


There are multiple ways to invoke apps and interactions, and apps have multiple ways to respond.
## Invoking apps[​](https://docs.slack.dev/interactivity#triggers "Direct link to Invoking apps")
There are several potential ways that app invocations are triggered. They can be divided into two categories:
  * [**Automatic invocations**](https://docs.slack.dev/interactivity#automatic). Apps choose to invoke the interaction.
  * [**User invocations**](https://docs.slack.dev/interactivity#user). Users choose to invoke the interaction.


### Automatic invocations[​](https://docs.slack.dev/interactivity#automatic "Direct link to Automatic invocations")
Your app can be invoked without any direct user input. Let users focus while your app handles what it needs to on its own.
#### Scheduled interactions[​](https://docs.slack.dev/interactivity#scheduled-interactions "Direct link to Scheduled interactions")
The interaction is invoked at a specific time with a specific cadence.
For example, on every Friday at 3pm an app could post a reminder.
➡️ To achieve this with a workflow automation, check out the guide to [scheduled triggers](https://tools.slack.dev/deno-slack-sdk/guides/creating-scheduled-triggers).
➡️ To achieve this with a Slack app, check out the [Send or schedule a message](https://docs.slack.dev/messaging/sending-and-scheduling-messages) guide.
#### Interactions initiated by external services[​](https://docs.slack.dev/interactivity#interactions-initiated-by-external-services "Direct link to Interactions initiated by external services")
Connections you've built with external services can trigger app interactions at any time. This provides seamless integration from those services into Slack.
For example, an account update on a CRM platform could cause a Slack app to post a Slack message.
➡️ To achieve this with a workflow automation, check out the guide to [webhook triggers](https://tools.slack.dev/deno-slack-sdk/guides/creating-webhook-triggers).
➡️ To achieve this with a Slack app, check out the [Sending messages using incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks) page.
#### Interactions initiated by the Events API[​](https://docs.slack.dev/interactivity#interactions-initiated-by-the-events-api "Direct link to Interactions initiated by the Events API")
The [Events API](https://docs.slack.dev/apis/events-api/) can send a push to Slack apps whenever a specific event occur in Slack. The receipt of one of these event pushes can trigger some interaction response by an app.
For example, the [`app_mention`](https://docs.slack.dev/reference/events/app_mention) event sends a push when an app is mentioned by someone in a conversation. The app could then respond with a message.
➡️ To achieve this with a workflow app, check out the guide to [event triggers](https://tools.slack.dev/deno-slack-sdk/guides/creating-event-triggers).
➡️ To achieve this with a Slack app, check out the guide to the [Events API](https://docs.slack.dev/apis/events-api/).
### User invocations[​](https://docs.slack.dev/interactivity#user "Direct link to User invocations")
Users can directly invoke your app via _entry points_ —a set of app features that serve as launching points for interactions. Most user invocations will send data payloads to an app containing contextual information about the interaction. These types of actions can further be used to interact with the app beyond the initial invocation, achieving a sort of back-and-forth interaction between the user and the app.
Enable these configurable features to provide users a way to invoke and interact with apps from the comfort of familiar Slack client elements.
#### Shortcuts[​](https://docs.slack.dev/interactivity#shortcuts "Direct link to Shortcuts")
Shortcuts let users quickly trigger workflows from various prominent UI locations in Slack.
➡️ Refer to [Link triggers](https://tools.slack.dev/deno-slack-sdk/guides/creating-link-triggers) for more info on using shortcuts, or rather, link triggers, with a workflow automation.
➡️ Refer to [Shortcuts](https://docs.slack.dev/interactivity/implementing-shortcuts) for more info for using shortcuts with a Slack app.
![](https://docs.slack.dev/assets/images/global_shortcuts-86eaf0fd44a7a36b2a215396ae78b3aa.svg)
#### Slash commands[​](https://docs.slack.dev/interactivity#slash commands "Direct link to Slash commands")
Let users trigger an interaction with your app by typing a command into the message composer box in any Slack conversation.
➡️ Slash commands in workflow automations are used simply as another entry point. Read more about it [here](https://docs.slack.dev/faq#slashcommands).
➡️ Refer to [Slash commands](https://docs.slack.dev/interactivity/implementing-slash-commands) for more info on using this invocation as well as the many other uses of slash commands in a Slack app.
#### Block Kit interactive components[​](https://docs.slack.dev/interactivity#block-kit-interactive-components "Direct link to Block Kit interactive components")
Interactive components are a subset of [Block Kit](https://docs.slack.dev/block-kit), our UI framework of visual components for Slack apps. They can be placed into [app surfaces](https://docs.slack.dev/surfaces) like [messages](https://docs.slack.dev/messaging), [modals](https://docs.slack.dev/surfaces/modals), or [App Home](https://docs.slack.dev/surfaces/app-home). Each component provides its own trigger for a possible interaction.
➡️ Refer to [Building with Block Kit](https://docs.slack.dev/block-kit) for more info.
![](https://docs.slack.dev/assets/images/bk_landing_bkb-81a42ef126a7e67a38e69dfc63db06ee.png)
## Responding to interactions[​](https://docs.slack.dev/interactivity#responses "Direct link to Responding to interactions")
An app's reaction to an interaction can take on many forms, ranging from doing nothing at all, to performing one of the many [API functions](https://docs.slack.dev/apis) available to Slack apps.
Some possibilities:
  * [Send messages](https://docs.slack.dev/messaging) using [Web APIs](https://docs.slack.dev/apis/web-api/) with a Slack app or using [built-in Slack functions](https://tools.slack.dev/deno-slack-sdk/guides/creating-slack-functions) with a workflow automation.
  * Create, archive, and manage conversations using [conversation-specific Web APIs](https://docs.slack.dev/apis/web-api/using-the-conversations-api).
  * Open [modals](https://docs.slack.dev/surfaces/modals) to collect info and provide a space for displaying dynamic details. Check out [our tutorial on using them with the Bolt for Python framework](https://tools.slack.dev/bolt-python/tutorial/modals) or using them in [workflow automations with the Deno Slack SDK](https://tools.slack.dev/deno-slack-sdk/guides/creating-an-interactive-modal).


Read our [guide to designing your Slack app](https://docs.slack.dev/surfaces/app-design) for some interactivity inspiration.
All interactivity payloads can be found in the [Reference: interaction payloads](https://docs.slack.dev/reference/interaction-payloads) documentation.
## Implementing infinite interactions[​](https://docs.slack.dev/interactivity#chaining "Direct link to Implementing infinite interactions")
Responses to interactions can themselves be invocations of further interaction.
Some examples:
  * An [interactive message](https://docs.slack.dev/messaging) could be published in response to a schedule, and a button within that message could be clicked to continue a workflow.
  * A [shortcut](https://docs.slack.dev/interactivity/implementing-shortcuts) could trigger a [modal](https://docs.slack.dev/surfaces/modals) that, once completed, could trigger an update of the app's [Home tab](https://docs.slack.dev/surfaces/app-home).


Chaining interactions together creates workflows that can accomplish complex tasks.
Ready to add interactivity to your app? Next stop is [Handling user interaction in your Slack apps](https://docs.slack.dev/interactivity/handling-user-interaction) for Slack apps or start with [Creating a form](https://tools.slack.dev/deno-slack-sdk/guides/creating-a-form) for workflow automations.
[PreviousManaging organization-ready apps](https://docs.slack.dev/enterprise-grid/organization-ready-apps)[NextInteractivity overview](https://docs.slack.dev/interactivity/)
  * [Invoking apps](https://docs.slack.dev/interactivity#triggers)
    * [Automatic invocations](https://docs.slack.dev/interactivity#automatic)
    * [User invocations](https://docs.slack.dev/interactivity#user)
  * [Responding to interactions](https://docs.slack.dev/interactivity#responses)
  * [Implementing infinite interactions](https://docs.slack.dev/interactivity#chaining)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



---
url: https://docs.slack.dev/
session_id: slack_api_docs
updated_dt: 2025-03-27T13:24:16.143141
---
[Skip to main content](https://docs.slack.dev/#__docusaurus_skipToContent_fallback)
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
  * Slack platform


On this page
# Slack platform overview
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
More doing, less reading
To jump straight into developing your own Slack app, follow our [Quickstart](https://docs.slack.dev/quickstart). You can get started _right now_.
Hello there, fellow developer! 👋
Welcome to the Slack API documentation, the place where ideas turn into interactive apps, workflows get automated, and Slack becomes the platform that powers your workday. Our documentation on APIs, SDKs, and tools can assist you in creating apps that make work life simpler, more pleasant and more productive.
**The Slack developer platform revolves around Slack apps.**
Which brings us to...
## What is a Slack app?[​](https://docs.slack.dev/#apps "Direct link to What is a Slack app?")
A Slack app is a tool or integration that extends the functionality of Slack: it adds new features, automates tasks, integrates with external services, or enhances the user experience. Essentially, a Slack app allows you to do more within Slack than just chat. With the Slack platform, individual and enterprise developers alike can create apps that integrate directly with the tools teams already use, whether that's connecting a CRM, managing project boards, or sending automated alerts.
Create welcoming spaces for people to use your Slack apps by adopting the range of possible app [surfaces](https://docs.slack.dev/surfaces) and add a variety of [interactive elements](https://docs.slack.dev/interactivity) within those surfaces. Enable your apps through our numerous [APIs](https://docs.slack.dev/apis). Automate processes and share custom steps through [workflows](https://docs.slack.dev/workflows) (though these work a little bit differently than your typical Slack app).
We know our platform is deep and wide, and possibly a little intimidating as a result. It's okay to not know where to start. First read through this page for some initial context, then jump into the water and try out our [Quickstart](https://docs.slack.dev/quickstart).
✨ Our [sample app tutorials](https://docs.slack.dev/samples) are also particularly useful for those floating aimlessly, as they utilize our [frameworks and SDKs](https://docs.slack.dev/tools). No matter what you try to do, we'll be right beside you.
### App vs. workflow[​](https://docs.slack.dev/#app-vs-workflow "Direct link to App vs. workflow")
Apps and workflows are all built on the Slack platform and we consider them all to be apps. The main differentiators are that apps (you may see these referred to as non-workflow apps) are self-hosted while workflows are Slack-hosted. Workflows are built with the [Deno SDK](https://tools.slack.dev/deno-slack-sdk/) while apps can be built using any of the [Bolt SDKs](https://docs.slack.dev/tools) or no SDK at all (if you're more of a DIY-er you can go it alone and call our APIs without an SDK). Both types of apps have the ability to carry out actions within Slack and with integrated third-party services.
Then there's [Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder)—a builder-friendly interface for automating tasks. Workflow Builder is an end-user facing UI built within Slack. As a developer, you can write custom steps that can be used as workflow steps in Workflow Builder. Those can be created via a [workflow app using the Deno Slack SDK](https://tools.slack.dev/deno-slack-sdk/tutorials/workflow-builder-custom-step/) or in a Bolt app, in any of Bolt's flavors ([Python](https://tools.slack.dev/bolt-js/concepts/custom-steps), [JavaScript](https://tools.slack.dev/bolt-js/concepts/custom-steps), and Java).
The Slack platform offers many options on the road to creating custom Slack apps and workflow automations. While there is power in those possibilities, it can be daunting to recognize which pieces of the platform apply to which type of app. We encourage you to read through a detailed comparison of the options [here](https://docs.slack.dev/workflows/comparing-workflows-apps).
## Platform concepts[​](https://docs.slack.dev/#concepts "Direct link to Platform concepts")
While you won't find all of the documentation hubs listed here (find those in the sidebar), here are the highlights you should explore in your app creation quest.
### Get up and running[​](https://docs.slack.dev/#start-building "Direct link to Get up and running")
Before you begin, a little light reading on how to define the look and feel of your app with [this guide on designing your app](https://docs.slack.dev/surfaces/app-design).
Once you've build an app with the [Quickstart](https://docs.slack.dev/quickstart) guide, you may want to explore the ins and outs of [authenticating](https://docs.slack.dev/authentication) it. Then look to our catalog of [APIs](https://docs.slack.dev/apis) to get the creative juices flowing for what you might build. The Web API's [hundreds of methods](https://docs.slack.dev/reference/methods) allow you to read, write, and update Slack data, from responding to activities in Slack to building event management tools!
### Go deeper[​](https://docs.slack.dev/#explore-more "Direct link to Go deeper")
Define where your app lives across the several available [Surfaces](https://docs.slack.dev/surfaces).
![](https://docs.slack.dev/assets/images/message-abstract-179ebdeb187c4f8c2246e9b0ec40c771.png)
[Surfaces](https://docs.slack.dev/surfaces) encompass all the areas that a Slack app can touch: [ messages](https://docs.slack.dev/messaging), [modals](https://docs.slack.dev/surfaces/modals), the [App Home](https://docs.slack.dev/surfaces/app-home), and [canvases](https://docs.slack.dev/surfaces/canvases). Messages, modals, and canvases are available for all types of Slack apps, while the App Home is available for non-workflow apps.
Organize your app's information in visually appealing way with [Block Kit](https://docs.slack.dev/block-kit). These include interactive blocks, like buttons, that you can use to facilitate user interaction.
![](https://docs.slack.dev/assets/images/bk_landing_bkb-81a42ef126a7e67a38e69dfc63db06ee.png)
[Block Kit](https://docs.slack.dev/block-kit) allows you to build beautiful surfaces with reusable components. Customize the order, appearance, and direct user interactivity with stackable, versatile blocks.
### Further customization[​](https://docs.slack.dev/#customization "Direct link to Further customization")
Make your app _yours_. Introduce personality and further custom functionality.
✨ [AI apps](https://docs.slack.dev/ai) bring another layer to app interactivity by providing a space to integrate your app with your chosen LLM.
✨ [Interactivity](https://docs.slack.dev/interactivity) covers the ways users can initiate interaction with Slack apps, including slash commands and shortcuts. Slash commands allow you to start your app from a simple keystroke and for non-workflow apps, provide even wider functionality. Shortcuts are a simple and reliable way to save your app's location for ease of discovery by users.
## What's next?[​](https://docs.slack.dev/#next "Direct link to What's next?")
Each developer's needs differ. Maybe you want to explore how to [distribute your app](https://docs.slack.dev/distribution) or even have it listed on the [Slack Marketplace](https://www.slack.com/marketplace). Perhaps you're interested in managing apps [as an admin](https://docs.slack.dev/admins). Better yet, explore the [tools](https://docs.slack.dev/tools) that make the job of app building easier.
Keep the end-goal in sight like a guiding horizon: a user wants to accomplish something with your app. The rest is getting there as productively and pleasantly as possible. Ready?
[Get Started](https://docs.slack.dev/quickstart)
[NextQuickstart](https://docs.slack.dev/quickstart)
  * [What is a Slack app?](https://docs.slack.dev/#apps)
    * [App vs. workflow](https://docs.slack.dev/#app-vs-workflow)
  * [Platform concepts](https://docs.slack.dev/#concepts)
    * [Get up and running](https://docs.slack.dev/#start-building)
    * [Go deeper](https://docs.slack.dev/#explore-more)
    * [Further customization](https://docs.slack.dev/#customization)
  * [What's next?](https://docs.slack.dev/#next)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



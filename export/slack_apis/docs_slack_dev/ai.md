---
url: https://docs.slack.dev/ai
session_id: slack_api_docs
updated_dt: 2025-03-27T13:24:33.004168
---
[Skip to main content](https://docs.slack.dev/ai#__docusaurus_skipToContent_fallback)
[![Slack Developer Docs](https://docs.slack.dev/img/logos/slack-developers-white.png)](https://slack.dev)[Docs](https://docs.slack.dev/)[Reference](https://docs.slack.dev/reference)[Samples](https://docs.slack.dev/samples)[Changelog](https://docs.slack.dev/changelog)
[Tools](https://tools.slack.dev)[Developer Program](https://api.slack.com/developer-program)[Your apps](https://api.slack.com/apps)
Search`K`
  * [Slack platform](https://docs.slack.dev/)
  * [Quickstart](https://docs.slack.dev/quickstart)
  * [FAQ](https://docs.slack.dev/faq)
  * [AI apps](https://docs.slack.dev/ai/)
    * [Overview](https://docs.slack.dev/ai/)
    * [Customizing Agentforce agents with custom Slack actions](https://docs.slack.dev/ai/customizing-agentforce-agents-with-custom-slack-actions)
    * [Developing AI apps](https://docs.slack.dev/ai/developing-ai-apps)
    * [Best practices](https://docs.slack.dev/ai/ai-apps-best-practices)
    * [Using the Data Access API](https://docs.slack.dev/ai/using-data-access-api)
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
  * AI apps


On this page
# AI apps overview
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
There are multiple ways to engage with [Agentforce](https://www.salesforce.com/agentforce) for Salesforce and Slack. This guide demystifies AI apps and agents from a developer's perspective.
## What is an agent?[​](https://docs.slack.dev/ai#what-is-an-agent "Direct link to What is an agent?")
AI Agents are autonomous, proactive applications designed to execute specialized tasks to help employees and customers. Using large language models (LLMs) to analyze and understand the full context of customer interactions or an automated trigger, they reason through decisions on the next steps autonomously. Agents can be instructed to generate responses that are consistent with your company’s brand voice and guidelines using trusted business data sourced from your CRM, Slack, and external applications. They are capable of operating 24/7, handling tasks proactively within set guardrails. When faced with complex issues beyond their scope, agents can escalate the matter to a human counterpart.
### Use cases[​](https://docs.slack.dev/ai#use-cases "Direct link to Use cases")
Agents can solve a variety of use cases in any industry. Knowing that the Salesforce Data Cloud, AI models, Slack, and third-party integrated apps are your data sources, the world is your agent's oyster. Take for example these use cases for agents across service, sales, marketing, and commerce:
  * Service Agent replaces traditional chatbots with AI that can handle a wide range of service issues without preprogrammed scenarios.
  * Sales Development Representative (SDR) engages with prospects 24/7, answering questions, managing objections, and scheduling meetings based on CRM and external data.
  * Sales Coach provides personalized role-play sessions for your sales team, using Salesforce data and generative AI to help sellers practice pitches and objections tailored to specific deals.
  * Merchandiser assists your ecommerce merchandisers with site setup, goal setting, personalized promotions, product descriptions, and data-driven insights, simplifying daily tasks.
  * Buyer Agent enhances the B2B buying experience, helping your buyers find products, make purchases, and track orders via chat or within sales portals. Personal Shopper acts as a digital concierge on your ecommerce sites or messaging apps, offering personalized product recommendations and assisting with search queries.
  * Campaign Optimizer automates the full campaign lifecycle, using AI to analyze, generate, personalize, and optimize marketing campaigns based on business goals.


## How to engage with agents[​](https://docs.slack.dev/ai#engage "Direct link to How to engage with agents")
Depending on your use case and needs, you may choose to use a third-party agent or develop one yourself—also known as a first-party agent.
Third-party agents (available in the [Slack Marketplace](https://docs.slack.dev/slack-marketplace)) are made by Slack partners and leverage AI in Slack with out-of-the-box functionality.
Developing a first-party agent gives you more flexibility with how you implement AI with a custom AI app in Slack. You will choose and implement your own LLM or internal-only database with this option.
In terms of Salesforce and Slack, there are two ways to create a first-party agent:
  * Build an agent in Salesforce and deploy it for use in Slack.
  * Build an AI app exclusively in Slack, entirely outside of Salesforce.


### Agentforce: Agents from Salesforce[​](https://docs.slack.dev/ai#agents-in-salesforce "Direct link to Agentforce: Agents from Salesforce")
Agentforce allows you to build and customize autonomous AI agents powered by the Salesforce platform via no/low-code with the Agent Builder or coded solutions. Build these with the Agentforce [Agent Builder](https://help.salesforce.com/s/articleView?id=ai.copilot_setup_enable.htm&type=5) and further customize them using the Salesforce-provided [standard Slack actions](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_ref_slack_parent.htm&type=5) or code your own [custom Slack actions](https://docs.slack.dev/ai/customizing-agentforce-agents-with-custom-slack-actions), then deploy them for use in Slack.
### AI apps in Slack[​](https://docs.slack.dev/ai#ai-apps-in-slack "Direct link to AI apps in Slack")
AI apps are [Slack apps](https://docs.slack.dev/quickstart) that make significant use of AI in their product offerings or that have the Agents & AI Apps feature added. Toggling the Agents & AI Apps feature on in the [app settings](https://api.slack.com/apps) allows you to utilize the [AI apps entry point and split view surfaces](https://docs.slack.dev/ai/developing-ai-apps) in Slack. Code your app to interface with an LLM and have the user-app interaction take place in the split-view to have the AI app work alongside your users in the flow of Slack.
An AI app provides an interface to AI for Slack users. It can communicate with external AI sources, such as OpenAI and Anthropic, as well as access Slack data to source relevant answers to user queries. AI apps can be programmed to take actions on behalf of users, whether that is by messaging a channel, sending them a reminder, or even creating a canvas with requested content. AI app functionality serves alongside bot functionality in Slack to streamline tasks.
Learn how to build an AI app in Slack with the [AI apps](https://docs.slack.dev/ai/developing-ai-apps) guide.
## Get started[​](https://docs.slack.dev/ai#get-started "Direct link to Get started")
Ready to start exploring Agentforce with Slack? First things first: you need to set up your orgs and connect them to each other.
  1. **Create a Salesforce org.** There are a few options for the Salesforce end of setup.
     * Current Salesforce customers can [create a sandbox](https://help.salesforce.com/s/articleView?id=platform.data_sandbox_create.htm&type=5). There are several types of sandboxes in Salesforce; here is a [guide to understanding them](https://help.salesforce.com/s/articleView?id=platform.create_test_instance.htm&type=5).
     * Current or future (SKU holders or free) Salesforce customers can [set up a scratch org](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs.htm).
     * Set up a [Trailhead org](https://trailhead.salesforce.com/promo/orgs/agentforce-for-slack-on-trailhead) that is pre-configured with data and Agentforce. These are shorter-lived orgs.
     * Set up a [Developer Edition](https://www.salesforce.com/form/developer-signup/) org that is pre-configured with Agentforce.
  2. **Create a Slack org**. The best way to play around with Agentforce without touching any production environment is to set up a sandbox org.
Agentforce in Slack and custom AI apps are available on all paid Slack plans
That is without the need for an additional add-on or SKU! A trial, complimentary, or sandbox workspace or grid all support [adding an Agent to Slack or installing an AI App](https://slack.com/help/articles/36218109305875-Set-up-and-manage-Agentforce-in-Slack#add-an-agent-to-slack) without any additional enablement.
To create a Slack developer sandbox, join the program [here](https://api.slack.com/developer-program). The developer program is a quick, self-serve way to spin up a Slack enterprise grid when needed. Provisioning a sandbox [may require approval](https://docs.slack.dev/tools/developer-sandboxes#enterprise-sandboxes) from your production Slack admins (if applicable). While you are using a sandbox workspace, there are some basic [sandbox limits](https://docs.slack.dev/tools/developer-sandboxes#sandboxes-limits) to be aware of.
  3. **Connect Salesforce and Slack orgs**. Follow [these instructions](https://slack.com/help/articles/30754346665747-Connect-Salesforce-and-Slack) to connect your Salesforce and Slack instances. You may also want to review this article to [Set up and manage Agentforce in Slack](https://slack.com/help/articles/36218109305875-Set-up-and-manage-Agentforce-in-Slack).


## Next steps[​](https://docs.slack.dev/ai#next-steps "Direct link to Next steps")
➡️ Learn how to set up and manage Agentforce in Slack, including how to connect Salesforce and Slack and add an agent to Slack with this [help article](https://slack.com/help/articles/36218109305875-Set-up-and-manage-Agentforce-in-Slack).
➡️ Build your own AI app in Slack with by following the [Developing AI apps guide](https://docs.slack.dev/ai/developing-ai-apps).
➡️ Learn how to further customize your Agentforce agent with Slack actions in [this guide](https://docs.slack.dev/ai/customizing-agentforce-agents-with-custom-slack-actions).
➡️ Browse which third-party agents are available for Slack in the [Slack Marketplace](https://docs.slack.dev/slack-marketplace).
➡️ Explore [Agentforce documentation](https://help.salesforce.com/s/articleView?id=ai.copilot_intro.htm&type=5).
[PreviousFAQ](https://docs.slack.dev/faq)[NextOverview](https://docs.slack.dev/ai/)
  * [What is an agent?](https://docs.slack.dev/ai#what-is-an-agent)
    * [Use cases](https://docs.slack.dev/ai#use-cases)
  * [How to engage with agents](https://docs.slack.dev/ai#engage)
    * [Agentforce: Agents from Salesforce](https://docs.slack.dev/ai#agents-in-salesforce)
    * [AI apps in Slack](https://docs.slack.dev/ai#ai-apps-in-slack)
  * [Get started](https://docs.slack.dev/ai#get-started)
  * [Next steps](https://docs.slack.dev/ai#next-steps)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



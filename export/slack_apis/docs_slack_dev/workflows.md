---
url: https://docs.slack.dev/workflows
session_id: slack_api_docs
updated_dt: 2025-03-27T13:26:26.816473
---
[Skip to main content](https://docs.slack.dev/workflows#__docusaurus_skipToContent_fallback)
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
    * [Overview](https://docs.slack.dev/workflows/)
    * [Comparing workflows and apps](https://docs.slack.dev/workflows/comparing-workflows-apps)
    * [Workflow steps](https://docs.slack.dev/workflows/workflow-steps)
    * [Workflow Builder](https://docs.slack.dev/workflows/workflow-builder)
    * [Creating custom steps dynamic options to use in Workflow Builder](https://docs.slack.dev/workflows/creating-custom-steps-dynamic-options)
    * [Run on Slack infrastructure](https://docs.slack.dev/workflows/run-on-slack-infrastructure)
    * [Deno Slack SDK](https://tools.slack.dev/deno-slack-sdk/)
    * [Slack CLI](https://tools.slack.dev/slack-cli)
  * [Legacy](https://docs.slack.dev/legacy/)


  * [](https://docs.slack.dev/)
  * Workflows


On this page
# Workflows
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
Workflows are a subset of Slack apps, which when combined with the developer-adjacent [Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder), makes up Slack **workflow automations.** They have unique abilities and restrictions. They focus on utilizing functions, workflows, and triggers rather than individual API methods.
With workflow apps, you can:
  * Create Slack-hosted coded workflows written in TypeScript using the [Deno Slack SDK](https://tools.slack.dev/deno-slack-sdk) and the [Slack CLI](https://tools.slack.dev/slack-cli). If you'd rather self-host, then you can use the [Bolt for Python](https://github.com/slackapi/bolt-python) and [Bolt for JavaScript](https://github.com/SlackAPI/bolt-js) frameworks.
  * Use workflow apps on their own or make coded functions available as steps for users in Workflow Builder with either the Deno Slack SDK or the Bolt frameworks. Workflow Builder is a no-code way to build workflows, right in Slack. Any user can combine a limited set of steps and triggers to quickly set up an automation.
  * Connect a Workflow Builder-created workflow to a coded workflow via [Workflow Buttons](https://tools.slack.dev/deno-slack-sdk/guides/creating-link-triggers#workflow_buttons) (as long as the second workflow is a [link trigger](https://tools.slack.dev/deno-slack-sdk/guides/creating-link-triggers#workflow_buttons_create)).


However, note that you cannot:
  * Develop using a Free plan.
  * Bring entire coded workflows into Workflow Builder—you can only bring in custom functions.
  * Run a workflow on an event (for example, "Workflow A executed").
  * Access a larger variety of APIs such as the [Admin API methods](https://docs.slack.dev/admins/managing-channels), [Slack SCIM API](https://docs.slack.dev/admins/scim-api/), and [Audit Logs API](https://docs.slack.dev/admins/audit-logs-api/).
  * List your apps in the [Slack Marketplace](https://docs.slack.dev/slack-marketplace).


The app management UI on `api.slack.com/apps` doesn’t support configuring workflow apps.
Also, workflow apps are currently not eligible for listing in the Slack Marketplace.
## The anatomy of a workflow[​](https://docs.slack.dev/workflows#anatomy "Direct link to The anatomy of a workflow")
Workflows are a combination of functions, executed in order.
There are a three types of functions:
  * **Slack functions** enable Slack-native actions, like creating a channel or sending a message.
  * **Connector functions** enable actions native to services _outside_ of Slack. Google Sheets, Dropbox and Microsoft Excel are just a few of the services with available connector functions.
  * **Custom functions** enable developer-specific actions. Pass in any desired inputs, perform any actions you can code up, and pass on outputs to other parts of your workflows.


Workflows are invoked via triggers. You can invoke workflows:
  * via a link within Slack,
  * on a schedule,
  * when specified events occurs,
  * or via webhooks.


Workflows make use of specifically-designed features of the Slack platform such as [datastores](https://tools.slack.dev/deno-slack-sdk/guides/using-datastores), a Slack-hosted way to store data.
While in development, you can keep your project mostly to yourself, or share it with a close collaborator. If your Slack admin requires approval of app installations, they’ll need to approve what you’re creating first.
## Get started[​](https://docs.slack.dev/workflows#get-started "Direct link to Get started")
➡️ **If you're ready to develop your own workflow-based app with the Slack Deno SDK** , begin with our [quickstart](https://tools.slack.dev/deno-slack-sdk/guides/getting-started)
✨ **If you'd like to learn more before developing with the Slack Deno SDK** , read our guides on [TypeScript](https://tools.slack.dev/deno-slack-sdk/guides/developing-with-typescript) (a strongly typed evolution of Javascript) and [Deno](https://tools.slack.dev/deno-slack-sdk/guides/installing-deno).
✨ **If you'd rather _build_ instead of _develop_** check out [Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder).
[PreviousDeveloper sandboxes](https://docs.slack.dev/tools/developer-sandboxes)[NextOverview](https://docs.slack.dev/workflows/)
  * [The anatomy of a workflow](https://docs.slack.dev/workflows#anatomy)
  * [Get started](https://docs.slack.dev/workflows#get-started)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



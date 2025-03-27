---
url: https://docs.slack.dev/app-manifests
session_id: slack_api_docs
updated_dt: 2025-03-27T13:24:58.298206
---
[Skip to main content](https://docs.slack.dev/app-manifests#__docusaurus_skipToContent_fallback)
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
    * [Overview](https://docs.slack.dev/app-manifests/)
    * [Configuring apps with app manifests](https://docs.slack.dev/app-manifests/configuring-apps-with-app-manifests)
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
  * App manifests


On this page
# App manifests
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
All apps have a manifest. Manifests are reusable configurations; they are designed to make an app's configuration "portable". You can store a manifest in version control such as GitHub where collaborators can easily grasp the setup of your app. Manifests can also make testing easier for apps that have the same setup.
Manifests are expressed in `JSON` or `YAML` and can be authored in your app's configuration page.
Currently, there are two versions of app manifests. [Workflow automations](https://docs.slack.dev/workflows) exclusively use version 2, while Slack apps may use either version. If the `version _metadata` property is not specified, Slack will treat your manifest configuration as v1. The [properties](https://docs.slack.dev/reference/app-manifest#fields) outlined in the app manifest reference indicate which manifest version they are included in.
## Manifests for granular permissions apps[​](https://docs.slack.dev/app-manifests#manifests-for-granular-permissions-apps "Direct link to Manifests for granular permissions apps")
For granular permissions apps, [the app manifest](https://docs.slack.dev/app-manifests/configuring-apps-with-app-manifests) can help you quickly create, configure, and copy Slack apps. You can share and reuse these manifests. Use this capability to create development clones of production apps.
App manifests be created and managed by visiting [Your Apps](https://api.slack.com/apps), selecting the app, then navigating to **Features** > **App Manifest** or directly by using the [App Manifest API](https://docs.slack.dev/app-manifests/configuring-apps-with-app-manifests#manifest_apis).
When you create an app through [Your Apps](https://api.slack.com/apps) using the **Create New App** button, you have an option to create from scratch or from an existing app manifest. This is how you could replicate a manifest from another app, pasting the recycled manifest there.
✨ Read more on the [Create and configure apps with manifests page](https://docs.slack.dev/app-manifests/configuring-apps-with-app-manifests) for Slack apps page.
## Manifests for workflow apps[​](https://docs.slack.dev/app-manifests#manifests-for-workflow-apps "Direct link to Manifests for workflow apps")
For workflow automation apps built with the Deno Slack SDK, the manifest holds the details of your app’s configuration, declaring the custom types, steps, workflows, and more that the automation contains.
Keep your local `manifest.ts` or `manifest.js` file up-to-date with any custom types, steps, datastores, and workflows required for your app.
✨ Read more on the [App manifest page](https://tools.slack.dev/deno-slack-sdk/guides/using-the-app-manifest) for workflow apps.
[PreviousOnboarding users to your app](https://docs.slack.dev/distribution/onboarding-users-to-your-app)[NextOverview](https://docs.slack.dev/app-manifests/)
  * [Manifests for granular permissions apps](https://docs.slack.dev/app-manifests#manifests-for-granular-permissions-apps)
  * [Manifests for workflow apps](https://docs.slack.dev/app-manifests#manifests-for-workflow-apps)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



---
url: https://docs.slack.dev/distribution
session_id: slack_api_docs
updated_dt: 2025-03-27T13:25:35.520557
---
[Skip to main content](https://docs.slack.dev/distribution#__docusaurus_skipToContent_fallback)
[![Slack Developer Docs](https://docs.slack.dev/img/logos/slack-developers-white.png)](https://slack.dev)[Docs](https://docs.slack.dev/)[Reference](https://docs.slack.dev/reference)[Samples](https://docs.slack.dev/samples)[Changelog](https://docs.slack.dev/changelog)
[Tools](https://tools.slack.dev)[Developer Program](https://api.slack.com/developer-program)[Your apps](https://api.slack.com/apps)
Search`K`
  * [Slack platform](https://docs.slack.dev/)
  * [Quickstart](https://docs.slack.dev/quickstart)
  * [FAQ](https://docs.slack.dev/faq)
  * [AI apps](https://docs.slack.dev/ai/)
  * [APIs](https://docs.slack.dev/apis/)
  * [App distribution](https://docs.slack.dev/distribution/)
    * [Overview](https://docs.slack.dev/distribution/)
    * [Hosting Slack apps](https://docs.slack.dev/distribution/hosting-slack-apps)
    * [Onboarding users to your app](https://docs.slack.dev/distribution/onboarding-users-to-your-app)
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
  * App distribution


On this page
# App distribution
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
When you create a Slack app, it resides in one workspace. You can also distribute Slack apps in either listed or unlisted fashion. In this guide, we'll take a look at the different types of distribution available and explain how to set up installation flows and authenticate users for each.
## Undistributed apps[​](https://docs.slack.dev/distribution#undistributed-apps "Direct link to Undistributed apps")
When you [create a Slack app](https://docs.slack.dev/quickstart#creating), you associate it with a workspace: to do this, [open the app dashboard](https://api.slack.com/apps) for your app and click **Install App to Workspace** within the _Install App_ section.
After installing your app, you'll get a single [access token](https://docs.slack.dev/authentication/tokens) that can be used to [authenticate](https://docs.slack.dev/authentication/installing-with-oauth#using) API method calls on behalf of the app.
Undistributed apps exist on a single workspace and can use the full range of app capabilities, but they can't be distributed to other workspaces. In addition, if your single-workspace app needs to take action on behalf of other users, you'll need to [build an OAuth 2.0 flow](https://docs.slack.dev/authentication/installing-with-oauth).
## Unlisted distributed apps[​](https://docs.slack.dev/distribution#unlisted-distributed-apps "Direct link to Unlisted distributed apps")
By default, a newly built Slack app can only be installed in its associated workspace as mentioned above. Installing your app on other workspaces means that you'll need to set up an [OAuth 2.0](https://docs.slack.dev/authentication/installing-with-oauth) flow. Once you've done that, your app will be able to generate [access tokens](https://docs.slack.dev/authentication/tokens) for each workspace and user.
Distributing your unlisted app is perfect for when you want to test out your app by running a pilot for early customers; however, apps intended for commercial distribution should be submitted and approved for listing in the Slack Marketplace. Unlike unlisted distributed apps, apps listed in the Slack Marketplace are reviewed against our [requirements & guidelines](https://docs.slack.dev/slack-marketplace/slack-marketplace-app-guidelines-and-requirements) to ensure a quality experience for end users.
### Preparing your app for distribution[​](https://docs.slack.dev/distribution#preparing "Direct link to Preparing your app for distribution")
Before you can distribute your app, there are a few steps to complete that are discussed in the following sections.
#### Handling installations[​](https://docs.slack.dev/distribution#oauth "Direct link to Handling installations")
Once created, your app can be installed to its [associated workspace](https://docs.slack.dev/distribution#single_workspace_apps) without any code for handling authorization. The [one-click install](https://docs.slack.dev/distribution#single_workspace_apps) for an unlisted single-workspace app generates an [access token](https://docs.slack.dev/authentication/tokens), which can then be used to [authenticate](https://authentication#using_tokens) API requests, but only within that associated workspace.
Therefore, when you're planning to distribute your app to other workspaces, you need to handle authorization. This will allow your app to be installed to any workspace, generating and using an access token programmatically.
✨ Read our [OAuth 2.0](https://docs.slack.dev/authentication) guide to understand the flow required for your app to request permissions and to generate access tokens.
In addition, once distributed, your app could potentially be installed to a Slack organization on Enterprise Grid.
✨ Read our guide to [supporting Enterprise Grid in apps](https://docs.slack.dev/enterprise-grid/developing-for-enterprise-grid#support) to understand how an Enterprise Grid environment can affect the way your app works.
#### Creating your onboarding flow[​](https://docs.slack.dev/distribution#onboarding "Direct link to Creating your onboarding flow")
[Onboarding users](https://docs.slack.dev/surfaces/app-design#onboarding) is an important consideration for any app. For distributed apps, it is especially crucial as your user base could grow from a single workspace to potentially hundreds. Providing direct, hands-on support may be possible with a single workspace, but won't scale once your app is shared with multiple workspaces.
✨ Read our guide to [creating a helpful onboarding flow](https://docs.slack.dev/surfaces/app-design#onboarding).
#### Enabling SSL[​](https://docs.slack.dev/distribution#ssl "Direct link to Enabling SSL")
Slack apps open to installation by other workspaces have additional security requirements. Your app must support SSL for all of the following URLs:
  * [OAuth redirect URLs](https://authentication#redirect_urls)
  * [Request URLs for interaction payloads](https://docs.slack.dev/interactivity/handling-user-interaction#payloads) from [interactive components](https://docs.slack.dev/block-kit#making-things-interactive), [actions](https://docs.slack.dev/interactivity/implementing-shortcuts#enabling_components) and [slash commands](https://docs.slack.dev/interactivity/implementing-slash-commands#app_command_handling)
  * [Block Kit interactive component options load URLs](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#external_selectt)
  * [Events API request URLs](https://docs.slack.dev/apis/events-api/#events_api_request_urls)


#### Enabling admin approval[​](https://docs.slack.dev/distribution#approval "Direct link to Enabling admin approval")
Some workspaces will restrict app installation so that only workspace administrators can provide authorization. Other workspaces may only allow the installation of apps officially listed in the Slack Marketplace.
Workspaces can also enable [admin approval](https://docs.slack.dev/admins/managing-app-approvals) requirements so that users can't directly install apps, but can request installation via a guided interface. Administrators can then screen these requests and selectively approve apps for installation. The list of permissions an app requests is also important to the decisions admins make, so ensure that your app only requests the permissions it absolutely needs.
### Enabling unlisted distribution[​](https://docs.slack.dev/distribution#enabling "Direct link to Enabling unlisted distribution")
If you think your app is ready to be distributed, follow these steps:
  1. Go to [your app's dashboard](https://api.slack.com/apps).
  2. Scroll to _Share Your App with Other Workspaces_ within the _Manage Distribution_ section.
  3. Ensure all items in the supplied checklist are completed.
  4. Click **Activate Public Distribution**.


Once distribution is enabled, you'll get access to an embeddable **Add to Slack** button, a shareable URL that kicks off the installation process when clicked, as well as an HTML meta tag to enable [Slack app suggestions](https://docs.slack.dev/slack-marketplace/distributing-your-app-in-the-slack-marketplace#suggestions).
You can also go a step further and submit your app to the [Slack Marketplace](https://docs.slack.dev/distribution#slack_marketplace_apps). This is recommended for apps intended for commercial distribution.
### Disabling unlisted distribution[​](https://docs.slack.dev/distribution#disabling "Direct link to Disabling unlisted distribution")
If distribution is enabled, you can turn it off by clicking **Deactivate Public Distribution** in the same location you [enabled it](https://docs.slack.dev/distribution#enabling). This will remove the app from any workspaces that have installed it, aside from the original associated workspace.
Note that you cannot disable distribution in this way once your app is published within the Slack Marketplace; instead, you must discontinue your listing there. Follow the instructions in the [Slack Marketplace guide](https://docs.slack.dev/slack-marketplace/distributing-your-app-in-the-slack-marketplace#discontinuing) to discontinue listing your app.
### Uninstalling apps[​](https://docs.slack.dev/distribution#uninstallation "Direct link to Uninstalling apps")
Your app can be uninstalled at any time from a workspace. Subscribe to the [`app_uninstalled`](https://docs.slack.dev/reference/events/app_uninstalled) event if you want your app to receive a notification when this happens.
In addition, apps will be automatically uninstalled from workspaces under the following circumstances:
  * Apps only using the following [scopes](https://docs.slack.dev/reference/scopes)—[`bot`](https://docs.slack.dev/reference/scopes/bot), [`incoming-webhook`](https://docs.slack.dev/reference/scopes/incoming-webhook), [`commands`](https://docs.slack.dev/reference/scopes/commands), and [`identify`](https://docs.slack.dev/reference/scopes/identify)—will generally not be automatically uninstalled. However, there is one exception: in the app's associated workspace, the app will be uninstalled when the last creator or [collaborator](https://slack.com/help/articles/7887743766291-Add-internal-app-collaborators) leaves the workspace or becomes a guest user.
  * Apps that use scopes beyond those listed above will be automatically uninstalled if the user who installed it leaves the workspace or becomes a guest user.


## Listed distributed apps (Slack Marketplace apps)[​](https://docs.slack.dev/distribution#slack-marketplace-apps "Direct link to Listed distributed apps \(Slack Marketplace apps\)")
The Slack Marketplace contains distributed Slack apps that have been reviewed to ensure they meet our standards of quality. Distributing to the Slack Marketplace is the best path for safe and trustworthy third-party apps, and is perfect for when your app has been previously tested with early customers and is ready to be distributed more broadly or at commercial scale.
You can also take advantage of [direct installs](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide#direct_install), which allow any user to install your app straight from the Slack Marketplace.
### Creating your app's listing page[​](https://docs.slack.dev/distribution#listing-page "Direct link to Creating your app's listing page")
If your app is approved for listing in the Slack Marketplace, it will have its very own listing page. Use this space to tell your app's story, to give a preview of your app's capabilities and user experience, and to attract users.
✨ Read our [Slack Marketplace guide](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide) to help you build a great Slack Marketplace listing page, as well as to learn about the review and submission process.
[PreviousUsing Slack Connect API methods](https://docs.slack.dev/apis/slack-connect/using-slack-connect-api-methods)[NextOverview](https://docs.slack.dev/distribution/)
  * [Undistributed apps](https://docs.slack.dev/distribution#undistributed-apps)
  * [Unlisted distributed apps](https://docs.slack.dev/distribution#unlisted-distributed-apps)
    * [Preparing your app for distribution](https://docs.slack.dev/distribution#preparing)
    * [Enabling unlisted distribution](https://docs.slack.dev/distribution#enabling)
    * [Disabling unlisted distribution](https://docs.slack.dev/distribution#disabling)
    * [Uninstalling apps](https://docs.slack.dev/distribution#uninstallation)
  * [Listed distributed apps (Slack Marketplace apps)](https://docs.slack.dev/distribution#slack-marketplace-apps)
    * [Creating your app's listing page](https://docs.slack.dev/distribution#listing-page)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



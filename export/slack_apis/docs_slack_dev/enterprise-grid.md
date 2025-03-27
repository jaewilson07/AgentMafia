---
url: https://docs.slack.dev/enterprise-grid
session_id: slack_api_docs
updated_dt: 2025-03-27T13:25:38.083925
---
[Skip to main content](https://docs.slack.dev/enterprise-grid#__docusaurus_skipToContent_fallback)
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
    * [Overview](https://docs.slack.dev/enterprise-grid/)
    * [Developing apps for Enterprise Grid](https://docs.slack.dev/enterprise-grid/developing-for-enterprise-grid)
    * [Migrating existing apps to Enterprise Grid](https://docs.slack.dev/enterprise-grid/migrating-to-organization-wide-deployment)
    * [Testing Enterprise Grid apps](https://docs.slack.dev/enterprise-grid/testing-enterprise-grid-apps)
    * [Managing organization-ready apps](https://docs.slack.dev/enterprise-grid/organization-ready-apps)
  * [Interactivity](https://docs.slack.dev/interactivity/)
  * [Messaging](https://docs.slack.dev/messaging/)
  * [Slack Marketplace](https://docs.slack.dev/slack-marketplace/)
  * [Surfaces](https://docs.slack.dev/surfaces/)
  * [Tools & SDKs](https://docs.slack.dev/tools/)
  * [Workflows](https://docs.slack.dev/workflows/)
  * [Legacy](https://docs.slack.dev/legacy/)


  * [](https://docs.slack.dev/)
  * Enterprise Grid


On this page
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
# Enterprise Grid
Welcome to Enterprise Grid! Whether you're a developer, an administrator, or a member of a security team tasked with implementing and protecting the infrastructure of your organization, we're here to help you get started—but first, let's go over the basics.
## What is Enterprise Grid?[​](https://docs.slack.dev/enterprise-grid#what "Direct link to What is Enterprise Grid?")
Enterprise Grid is a network of two or more Slack workspace instances. Each Slack workspace has its own ID, directory of members, channels, conversations, and files. For the most part, each workspace behaves and functions as you're used to on a single, standalone workspace.
For developers, the biggest change for your apps to handle is that some channels and conversations can be [shared](https://docs.slack.dev/enterprise-grid#understanding_shared_channels) between multiple workspaces within the same Enterprise organization. But as with a standalone Slack workspace, workspaces on an Enterprise Grid have their own application installations.
In addition, this guide may be your first introduction to the following terms:
  * _Enterprise organization_ : An entity used to describe multiple Slack workspaces within the same organization.
  * _Enterprise organization user_ : An Enterprise Grid user. These users have the same identity and profile across all workspaces within an organization.
  * _Enterprise user ID_ : A user ID beginning with `U` or `W`, representing the user across all workspaces within an Enterprise Grid.
  * _Legacy user ID_ : Also known as a "team user ID", these are the User IDs you've come to know and love in Slack if you've only developed for standalone workspaces before. They begin with `U`. Also known as a _local user ID_.
  * _Shared channel_ : A channel shared between two or more workspaces within an organization.
  * _Translation layer_ : A translating service that converts new organization-based user IDs to legacy team user IDs, allowing apps to migrate data.
  * _Workspace_ : Where a team works. The terms _workspace_ and _team_ are often used interchangeably. When you see the object name such as `team_id`, it means the ID for a workspace.


## Enterprise Grid for developers[​](https://docs.slack.dev/enterprise-grid#enterprise-grid-devs "Direct link to Enterprise Grid for developers")
Developers may encounter a variety of use cases when developing apps for Enterprise Grid:
  * CI/CD integration: automate app deployment with CI/CD pipelines for secure and compliant releases.
  * Streamlined app approvals: automate admin approvals for Slack apps to reduce friction while maintaining security.
  * Cross-platform workflows: connect Slack with Enterprise tools for seamless automation.


To address those use cases, we recommend checking out the following resources:
  * [Setting up CI/CD with the Slack CLI](https://tools.slack.dev/slack-cli/guides/setting-up-ci-cd-with-the-slack-cli)
  * [CI/CD authorization in the Slack CLI](https://tools.slack.dev/slack-cli/guides/authorizing-the-slack-cli/#ci-cd)
  * [Developing apps for Enterprise Grid](https://docs.slack.dev/enterprise-grid/developing-for-enterprise-grid)
  * [Enterprise readiness](https://docs.slack.dev/workflows/run-on-slack-infrastructure/#enterprise)
  * [App approval process for developers](https://tools.slack.dev/deno-slack-sdk/guides/controlling-permissions-for-admins/#approval-developers)
  * [Migrating existing apps to Enterprise Grid](https://docs.slack.dev/enterprise-grid/migrating-to-organization-wide-deployment)
  * [Testing Enterprise Grid apps](https://docs.slack.dev/enterprise-grid/testing-enterprise-grid-apps)
  * [Understanding Slack Connect](https://docs.slack.dev/apis/slack-connect/)
  * [Using Slack Connect API methods](https://docs.slack.dev/apis/slack-connect/using-slack-connect-api-methods)


## Enterprise Grid for admins[​](https://docs.slack.dev/enterprise-grid#enterprise-grid-admins "Direct link to Enterprise Grid for admins")
Org Admins (or admins in general) may encounter a variety of use cases when developing for Enterprise Grid:
  * Automated user provisioning: sync with Enterprise directories for easy onboarding/offboarding.
  * Compliance and policy enforcement: automate security policies, app restrictions, and audits.
  * Enterprise-wide automation governance: provide oversight for all Slack automation while keeping teams empowered.


To address those use cases, we recommend checking out the following resources:
  * [Managing users](https://docs.slack.dev/admins/managing-users)
  * [Using the Slack SCIM API](https://docs.slack.dev/admins/scim-api)
  * [Managing organization-ready apps](https://docs.slack.dev/enterprise-grid/organization-ready-apps)
  * [Managing app approvals](https://docs.slack.dev/admins/managing-app-approvals)
  * [App approval process for admins](https://tools.slack.dev/deno-slack-sdk/guides/controlling-permissions-for-admins/#approval-developers)
  * [Managing workflow and connector permissions](https://docs.slack.dev/admins/managing-workflow-and-connector-permissions)


## Enterprise Grid for security teams[​](https://docs.slack.dev/enterprise-grid#enterprise-grid-security "Direct link to Enterprise Grid for security teams")
Security developers or team members may encounter a variety of use cases when developing for Enterprise Grid:
  * App and token security reviews: automatically review new apps and flag security risks.
  * Security alerts and incident response: route critical security alerts to the right teams in real-time.
  * Automated token rotation and secret management: keep credentials secure without manual intervention.


To address those use cases, we recommend checking out the following resources:
  * [Security best practices](https://docs.slack.dev/authentication/best-practices-for-security)
  * [Installing with OAuth](https://docs.slack.dev/authentication/installing-with-oauth)
  * [Using Sign in with Slack](https://docs.slack.dev/authentication/sign-in-with-slack/)
  * [Verifying requests from Slack](https://docs.slack.dev/authentication/verifying-requests-from-slack)
  * [Using the Audit Logs API](https://docs.slack.dev/admins/audit-logs-api)
  * [Using token rotation](https://docs.slack.dev/authentication/using-token-rotation)


## Shared channels[​](https://docs.slack.dev/enterprise-grid#shared-channels "Direct link to Shared channels")
A shared channel is a bridge between workspaces that need to collaborate together. Teams can use shared channels to connect, chat, share files, and use apps in the same way as they do on a standalone workspace.
To illustrate the power of shared channels, let's rewind to life _before_ them to understand how they can make your working life more pleasant and productive:
![Before shared channels](https://docs.slack.dev/assets/images/before_shared_channels-902717ec8dfb37bd664445b8544f9498.png)
Previously, what team members of Catnip Inc. were saying and doing on a shared project with Woof Inc. was a mystery. When the two teams tried to communicate, it was disconnected and disparate.
This is solved with the shared channels of today. Now, the project channel `#projectM` exists in each team's workspace, making communication much simpler.
![After shared channels](https://docs.slack.dev/assets/images/after_shared_channels-90ad1d9d3eac07a2dc3e47671e6f04c4.png)
There are two types of shared channels, each with different uses:
  * **Slack Connect channels** , which allow up to 20 organizations to come together in a single channel (e.g., Catnip, Inc. and Woof Inc. from the examples above). To learn more about how shared channels work, check out our documentation on [Slack Connect](https://docs.slack.dev/apis/slack-connect/).
  * **Multi-workspace shared channels** , which are channels shared between multiple workspaces within the same organization's Slack instance. For example, the `#treats` channel is shared in Woof Inc's, Marketing, Engineering, _and_ Social workspaces. It exists in all three places, within Woof Inc.'s single Enterprise Grid instance.


## Next steps[​](https://docs.slack.dev/enterprise-grid#next-steps "Direct link to Next steps")
✨ Read about [migrating existing apps to Enterprise Grid](https://docs.slack.dev/enterprise-grid/migrating-to-organization-wide-deployment).
[PreviousUpgrading outmoded dialogs to modals](https://docs.slack.dev/block-kit/upgrading-outmoded-dialogs-to-modals)[NextOverview](https://docs.slack.dev/enterprise-grid/)
  * [What is Enterprise Grid?](https://docs.slack.dev/enterprise-grid#what)
  * [Enterprise Grid for developers](https://docs.slack.dev/enterprise-grid#enterprise-grid-devs)
  * [Enterprise Grid for admins](https://docs.slack.dev/enterprise-grid#enterprise-grid-admins)
  * [Enterprise Grid for security teams](https://docs.slack.dev/enterprise-grid#enterprise-grid-security)
  * [Shared channels](https://docs.slack.dev/enterprise-grid#shared-channels)
  * [Next steps](https://docs.slack.dev/enterprise-grid#next-steps)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



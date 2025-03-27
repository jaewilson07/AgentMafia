---
url: https://docs.slack.dev/admins
session_id: slack_api_docs
updated_dt: 2025-03-27T13:24:39.812324
---
[Skip to main content](https://docs.slack.dev/admins#__docusaurus_skipToContent_fallback)
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
    * [Overview](https://docs.slack.dev/admins/)
    * [Managing users](https://docs.slack.dev/admins/managing-users)
    * [Managing channels](https://docs.slack.dev/admins/managing-channels)
    * [Managing app approvals](https://docs.slack.dev/admins/managing-app-approvals)
    * [Managing workflow and connector permissions](https://docs.slack.dev/admins/managing-workflow-and-connector-permissions)
    * [Managing invite requests](https://docs.slack.dev/admins/managing-invite-requests)
    * [Using the Audit Logs API](https://docs.slack.dev/admins/audit-logs-api)
    * [Using the Legal Holds API](https://docs.slack.dev/admins/legal-holds-api)
    * [Using the Slack SCIM API](https://docs.slack.dev/admins/scim-api)
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
  * Apps for Admins


On this page
# Apps for Admins
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
The features within are only available to Slack workspaces on Enterprise Grid plans.
Don't have a paid plan? Join the Developer Program and provision a fully-featured sandbox for free.
Managing Slack, easier than ever. Use approval and provisioning APIs to help Slack Admins work more effectively. Secure your organization with auditing and session management APIs.
## Manage channels[​](https://docs.slack.dev/admins#manage_channels "Direct link to Manage channels")
Handle the intricacies of creating public and private channels, setting preferences, and connecting new workspaces—all with a single app. Use the [APIs for channel management](https://docs.slack.dev/admins/managing-channels).
## Manage app approvals[​](https://docs.slack.dev/admins#manage_app_approvals "Direct link to Manage app approvals")
Build an app that can handle approvals and restrictions for admins across an entire Slack org. Read our guide to [app approval APIs](https://docs.slack.dev/admins/managing-app-approvals).
## Create workspaces and manage users in them[​](https://docs.slack.dev/admins#manage_workspaces "Direct link to Create workspaces and manage users in them")
An app can create a workspace and control addition and removal of that workspace's users. Apps can even mark a user as an Admin or owner. Read our guide to [the APIs for managing users in a workspace](https://docs.slack.dev/admins/managing-users).
## Manage invite requests[​](https://docs.slack.dev/admins#manage_invite_requests "Direct link to Manage invite requests")
Let users invite friends to unexplored workspaces, while maintaining admin approval over those invites. Explore [the invite request management APIs](https://docs.slack.dev/admins/managing-invite-requests).
## Define default channels for IDP groups[​](https://docs.slack.dev/admins#default_channels "Direct link to Define default channels for IDP groups")
An [IDP group](https://slack.com/help/articles/115001435788-connect-identity-provider-groups-to-your-enterprise-grid-org) represents a group of users synced from your identity provider (IDP). You can add, remove, and list default channels for an IDP group with the `admin.usergroups.*` methods.
  * The [`admin.usergroups.addChannels`](https://docs.slack.dev/reference/methods/admin.usergroups.addChannels) method
  * The [`admin.usergroups.removeChannels`](https://docs.slack.dev/reference/methods/admin.usergroups.removeChannels) method
  * The [`admin.usergroups.listChannels`](https://docs.slack.dev/reference/methods/admin.usergroups.listChannels) method


You can also add a _workspace_ to an IDP group using the [`admin.usergroups.addTeams`](https://docs.slack.dev/reference/methods/admin.usergroups.addTeams) method. When you link a workspace to an IDP group, members of the IDP group automatically join the workspace.
## Allowlists for private channels[​](https://docs.slack.dev/admins#allowlists "Direct link to Allowlists for private channels")
You can add, remove, and list membership allowlists for private channels with the `admin.conversations.restrictAccess.*` methods. Find [more documentation here](https://docs.slack.dev/admins/managing-users#allowlists), or check out the individual methods:
  * [`admin.conversations.restrictAccess.addGroup`](https://docs.slack.dev/reference/methods/admin.conversations.restrictAccess.addGroup)
  * [`admin.conversations.restrictAccess.removeGroup`](https://docs.slack.dev/reference/methods/admin.conversations.restrictAccess.removeGroup)
  * [`admin.conversations.restrictAccess.listGroups`](https://docs.slack.dev/reference/methods/admin.conversations.restrictAccess.listGroups)


## Reset sessions rapidly[​](https://docs.slack.dev/admins#reset_sessions "Direct link to Reset sessions rapidly")
When you suspect a device - mobile, web, or both - has been swiped, take immediate action. Wipe a user's login session [using our session reset APIs](https://docs.slack.dev/reference/methods/admin.users.session.reset).
## Provisioning programmatically[​](https://docs.slack.dev/admins#provision "Direct link to Provisioning programmatically")
Provision and manage user accounts and groups with [SCIM APIs](https://docs.slack.dev/admins/scim-api/).
## Monitor workspace events[​](https://docs.slack.dev/admins#monitor_events "Direct link to Monitor workspace events")
Track what's happening in your organization using [Audit Logs APIs](https://docs.slack.dev/admins/audit-logs-api/).
[PreviousConfiguring apps with app manifests](https://docs.slack.dev/app-manifests/configuring-apps-with-app-manifests)[NextOverview](https://docs.slack.dev/admins/)
  * [Manage channels](https://docs.slack.dev/admins#manage_channels)
  * [Manage app approvals](https://docs.slack.dev/admins#manage_app_approvals)
  * [Create workspaces and manage users in them](https://docs.slack.dev/admins#manage_workspaces)
  * [Manage invite requests](https://docs.slack.dev/admins#manage_invite_requests)
  * [Define default channels for IDP groups](https://docs.slack.dev/admins#default_channels)
  * [Allowlists for private channels](https://docs.slack.dev/admins#allowlists)
  * [Reset sessions rapidly](https://docs.slack.dev/admins#reset_sessions)
  * [Provisioning programmatically](https://docs.slack.dev/admins#provision)
  * [Monitor workspace events](https://docs.slack.dev/admins#monitor_events)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



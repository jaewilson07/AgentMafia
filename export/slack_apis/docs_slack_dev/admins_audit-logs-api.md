---
url: https://docs.slack.dev/admins/audit-logs-api
session_id: slack_api_docs
updated_dt: 2025-03-27T13:24:42.346646
---
[Skip to main content](https://docs.slack.dev/admins/audit-logs-api#__docusaurus_skipToContent_fallback)
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
  * [Apps for Admins](https://docs.slack.dev/admins/)
  * Using the Audit Logs API


On this page
# Using the Audit Logs API
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
This feature is only available to Slack workspaces on an Enterprise Grid plan
The Audit Logs API is meant for anyone interested in programmatically monitoring audit events in a Slack [Enterprise Grid](https://docs.slack.dev/enterprise-grid) organization. This may include:
  * Providers of security information and event management (SIEM) solutions looking to integrate with Slack
  * Enterprise Grid administrators looking for insight into how their team is accessing Slack
  * Security professionals interested in actively monitoring their Slack organization for potential security issues


## What the Audit Logs API can do[​](https://docs.slack.dev/admins/audit-logs-api#what "Direct link to What the Audit Logs API can do")
The Audit Logs API is for monitoring the audit events happening in an Enterprise Grid organization to ensure continued compliance, to safeguard against any inappropriate system access, and to allow you to audit suspicious behavior within your enterprise.
The idea is to give Enterprise Grid organization owners the ability to query user actions in a workspace. With this API, you could:
  * Automatically feed Slack access data into an SIEM or other auditing tool
  * Proactively monitor for potential security issues or malicious access attempts
  * Write custom apps to gain insight into how your organization uses Slack


These API methods provide a view of the actions users perform in an organization. They do **_not_** enable monitoring of message content. If you need to proactively monitor the messages in a Slack organization or workspace for compliance reasons, you may consider an e-Discovery or Data Loss Prevention solution.
The Audit Logs API provides insight into audit events that are actually happening across a Slack organization and is therefore read only. There are no write methods for Audit Log events.
Slack also does not perform any kind of automated intrusion detection. The Audit Logs API will return the data but can not automatically determine or indicate whether an action was appropriate.
Slack has built an internal platform for processing our Slack logs in real time to detect statistically key characteristics and anomalies, and then surface them in the admin audit logs.
The Audit Logs API supports a subset of all possible Slack audit events.
We will continue to add support for additional audit events.
## Installing an app on an Enterprise Grid organization[​](https://docs.slack.dev/admins/audit-logs-api#install "Direct link to Installing an app on an Enterprise Grid organization")
Apps requesting the `auditlogs:read` scope _must_ be installed by the _Owner_ of an Enterprise Grid organization.
Audit Logs events work across an entire Enterprise Grid organization, not individual workspaces. For this reason, the OAuth token used for calling Audit Logs API methods must be obtained from installing the app on the organization, not just a workspace within the organization.
To configure and install an app supporting Audit Logs on your Enterprise Grid organization:
  1. The web service powering your app will need to be able to handle a standard [OAuth 2 flow](https://docs.slack.dev/authentication/installing-with-oauth).
  2. [Create an app](https://api.slack.com/apps?new_app=1)
  3. In the app's settings, select **OAuth & Permissions** from the left navigation. Scroll down to the section titled **Scopes** , then click **Add an OAuth Scope** under **User Token Scopes**. Add the `auditlogs:read` scope.
  4. In the app's settings, select **Manage Distribution** from the left navigation. Under the section titled **Share Your App with Other Workspaces** , make sure all four sections have the green check. Then click the green **Activate Public Distribution** button.
  5. Under the **Share Your App with Your Workspace** section, copy the **Sharable URL** and paste it into a browser to initiate the OAuth handshake that will install the app on your organization. You must be logged in as the **Owner** of your Enterprise Grid organization to install the app.
  6. Check the dropdown in the upper right of the installation screen to make sure you are installing the app on the Enterprise Grid organization, not an individual workspace within the organization. (See image below.)
  7. Once your app completes the OAuth flow, you will be granted an OAuth token that can be used for calling all of the Audit Logs API methods for your organization.


When installing an Audit Logs app, be sure to install it on your Grid organization, not a workspace within the organization.(See step 6 above.)
![Installing the app on a workspace](https://docs.slack.dev/assets/images/workspace-v-org-audit-8b3358dcb1f972e3255c56957936352d.png)
## The audit event[​](https://docs.slack.dev/admins/audit-logs-api#audit-event "Direct link to The audit event")
If the Slack workspace is a stage, all the members are merely actors. They have their exits and entrances, and one user in time plays many parts.
Every audit event logged by the Audit Logs API is comprised of an **actor** , an **action** , an **entity** , and a **context**. They all work in harmony, such that the **actor** takes an **action** on an **entity** within a **context**.
The audit log events are returned to you as JSON, the exact format of which will vary slightly depending on the type of audit event. Each entry will describe the `action`, the `actor` that generated the event, the `entity`, and its `context`. Here's an audit event for a user logging in:
```
{"entries":[{"id":"0123a45b-6c7d-8900-e12f-3456789gh0i1","date_create":1521214343,"action":"user_login","actor":{"type":"user","user":{"id":"W123AB456","name":"Charlie Parker","email":"bird@slack.com"}},"entity":{"type":"user","user":{"id":"W123AB456","name":"Charlie Parker","email":"bird@slack.com"}},"context":{"location":{"type":"enterprise","id":"E1701NCCA","name":"Birdland","domain":"birdland"},"ua":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/64.0.3282.186 Safari\/537.36","session_id":"847288190092","ip_address":"1.23.45.678"}}]}
```

An **actor** will always be a user on a workspace and will be identified by their user ID, such as `W123AB456`. For eDiscovery apps with actions `file_downloaded` or `file_downloaded_blocked` the **actor** will be the user who installed the app.
If customer credentials were reset on their behalf by a Slack security agent, the ID will be `USLACKSECURITY`.
Occasionally, an event may fire without an actor, in which case Slack returns a placeholder `actor` object where the ID will be `USLACKUSER`.
An **action** is the thing the actor did. It will be an easily identifiable string from [the known list of actions](https://docs.slack.dev/reference/audit-logs-api/methods-actions-reference#actions). An example might be `user_login`, `file_downloaded`, or `emoji_removed`.
An **entity** is the thing that the actor has taken the action upon. It will be the Slack ID of the thing, such as:
  * A user (`WXXXXXXXX`)
  * A channel (`CXXXXXXXX`)
  * A file (`FXXXXXXXX`)
  * An app (`AXXXXXXXX`)
  * A workspace (`TXXXXXXXX`)
  * An enterprise (`EXXXXXXXX`)


For example, the entity corresponding to the audit event of a team member logging in is that _user_. For a file that was downloaded, the entity is that _file_. For an emoji being removed, it is the _workspace_ from which the emoji was removed.
The number of both entities and actions will always continue to grow to include other Slack components. So many new things happen in Slack, we don't always document them before they happen. We're certain the enumeration of audit events in this document is incomplete.
Finally, the **context** is the location where the actor took the action on the entity. It will always be either a Workspace or an Enterprise, with the appropriate ID.
Some audit events may optionally include **details** where appropriate — for example, if it would be helpful to know the previous value of a setting that was changed.
Audit events triggered through apps will include app which contains information about the app used to make the request. For a period of time app was logged for all events which was set to `null` when not triggered by an app, however a change has been made to ensure app only appears when required moving forward.
```
{"id":"0123a45b-6c7d-8900-e12f-3456789gh0i1","date_create":1650415188,"action":"public_channel_created","actor":{"type":"user","user":{"id":"W123ABC456","name":"Channel Spinner","email":"botuser-T123AB456-AT123AB456@slack-bots.com","team":"T123AB456"}},"entity":{"type":"channel","channel":{"id":"C123ABC456","privacy":"public","name":"REDACTED","is_shared":false,"is_org_shared":false}},"context":{"location":{"type":"workspace","id":"T123ABC456","name":"birdland","domain":"birdland"},"ua":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/64.0.3282.186 Safari\/537.36","ip_address":"1.23.45.678","session_id":null,"app":{"id":"AT123AB456","name":"Channel Spinner App","scopes":[],"scopes_bot":["channels:manage","groups:write","im:write","mpim:write"],"creator":"W123ABC456","team":"T123ABC456"}}}
```

Ready to use the Audit Logs API? Your next stop is the [Audit Logs API endpoints and actions](https://docs.slack.dev/reference/audit-logs-api/methods-actions-reference) page, where you can find specific information on the API's endpoints. It contains an exhaustive (but always updating) list of audit event actions.
[PreviousManaging invite requests](https://docs.slack.dev/admins/managing-invite-requests)[NextUsing the Legal Holds API](https://docs.slack.dev/admins/legal-holds-api)
  * [What the Audit Logs API can do](https://docs.slack.dev/admins/audit-logs-api#what)
  * [Installing an app on an Enterprise Grid organization](https://docs.slack.dev/admins/audit-logs-api#install)
  * [The audit event](https://docs.slack.dev/admins/audit-logs-api#audit-event)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



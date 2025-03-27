---
url: https://docs.slack.dev/authentication
session_id: slack_api_docs
updated_dt: 2025-03-27T13:25:06.165517
---
[Skip to main content](https://docs.slack.dev/authentication#__docusaurus_skipToContent_fallback)
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
    * [Overview](https://docs.slack.dev/authentication/)
    * [Tokens](https://docs.slack.dev/authentication/tokens)
    * [Installing with OAuth](https://docs.slack.dev/authentication/installing-with-oauth)
    * [Using token rotation](https://docs.slack.dev/authentication/using-token-rotation)
    * [Verifying requests from Slack](https://docs.slack.dev/authentication/verifying-requests-from-slack)
    * [Best practices for security](https://docs.slack.dev/authentication/best-practices-for-security)
    * [Authorizing with Postman](https://docs.slack.dev/authentication/authorizing-with-postman)
    * [Binding accounts across services](https://docs.slack.dev/authentication/binding-accounts-across-services)
    * [Sign in with Slack](https://docs.slack.dev/authentication/sign-in-with-slack/)
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
  * Authentication


On this page
# Authentication overview
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
Authentication is a critical part of the development process, but it doesn’t have to be daunting. With the right tools and best practices, you’ll have a secure, smooth authentication flow. Whether you’re handling [OAuth 2.0](https://docs.slack.dev/authentication/installing-with-oauth), [verifying requests](https://docs.slack.dev/authentication/verifying-requests-from-slack), or setting up [Sign in with Slack](https://docs.slack.dev/authentication/sign-in-with-slack/), we’ve got you covered.
## Authentication basics[​](https://docs.slack.dev/authentication#basics "Direct link to Authentication basics")
Before your app can access Slack data or interact with Slack workspaces, it must go through an authentication process. This involves obtaining the necessary tokens and permissions for your app to function properly. Slack apps use OAuth [scopes](https://docs.slack.dev/reference/scopes) to govern what they can access. These are added in the app settings when building an app. You will attach these scopes to your tokens. Check out [tokens](https://docs.slack.dev/authentication/tokens) to learn more. You can rotate those tokens too! Find out how on the [Using token rotation](https://docs.slack.dev/authentication/using-token-rotation) page.
## Key concepts[​](https://docs.slack.dev/authentication#concepts "Direct link to Key concepts")
  * [**OAuth 2.0**](https://docs.slack.dev/authentication/installing-with-oauth): Learn how to use OAuth 2.0 to securely authenticate users and request access tokens.
  * [**Tokens**](https://docs.slack.dev/authentication/tokens): Understand the different types of tokens your app can use (user tokens, bot tokens, and app tokens) and how to manage them, as well as employ token rotation and expiry to keep things fresh.
  * [**Security best practices**](https://docs.slack.dev/authentication/best-practices-for-security): Learn about security practices for managing authentication, such as validating tokens, handling sensitive data, and protecting your app from unauthorized access.


## Reference[​](https://docs.slack.dev/authentication#reference "Direct link to Reference")
  * [**Scopes and Permissions**](https://docs.slack.dev/reference/scopes): Find the right permissions for your app to ensure access is limited to only the necessary data.


[PreviousUsing the Slack SCIM API](https://docs.slack.dev/admins/scim-api)[NextOverview](https://docs.slack.dev/authentication/)
  * [Authentication basics](https://docs.slack.dev/authentication#basics)
  * [Key concepts](https://docs.slack.dev/authentication#concepts)
  * [Reference](https://docs.slack.dev/authentication#reference)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



---
url: https://docs.slack.dev/block-kit
session_id: slack_api_docs
updated_dt: 2025-03-27T13:24:46.482510
---
[Skip to main content](https://docs.slack.dev/block-kit#__docusaurus_skipToContent_fallback)
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
    * [Overview](https://docs.slack.dev/block-kit/)
    * [Designing with Block Kit](https://docs.slack.dev/block-kit/designing-with-block-kit)
    * [Formatting with rich text](https://docs.slack.dev/block-kit/formatting-with-rich-text)
    * [Upgrading outmoded dialogs to modals](https://docs.slack.dev/block-kit/upgrading-outmoded-dialogs-to-modals)
  * [Enterprise Grid](https://docs.slack.dev/enterprise-grid/)
  * [Interactivity](https://docs.slack.dev/interactivity/)
  * [Messaging](https://docs.slack.dev/messaging/)
  * [Slack Marketplace](https://docs.slack.dev/slack-marketplace/)
  * [Surfaces](https://docs.slack.dev/surfaces/)
  * [Tools & SDKs](https://docs.slack.dev/tools/)
  * [Workflows](https://docs.slack.dev/workflows/)
  * [Legacy](https://docs.slack.dev/legacy/)


  * [](https://docs.slack.dev/)
  * Block Kit


On this page
# Block Kit
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
The Block Kit UI framework is built with _blocks_ , _block elements_ and _composition objects_.
_Blocks_ are visual components that can be arranged to create app layouts. Apps can add blocks to _surfaces_ like [the Home tab](https://docs.slack.dev/surfaces/app-home), [messages](https://docs.slack.dev/messaging) and [modals](https://docs.slack.dev/surfaces/modals).
Blocks may also contain _block elements_. Block elements are usually interactive components, such as buttons and menus.
Blocks and block elements are built with _composition objects_. Composition objects define text, options, or other interactive features within certain blocks and block elements.
![](https://docs.slack.dev/assets/images/bk_landing_bkb-81a42ef126a7e67a38e69dfc63db06ee.png)
Whether you're composing layouts for modals, messages, or tabs, the Block Kit building experience is the same — your app will be sculpting specially-structured JSON to express itself. The result is clear, interactive communication between your app and its users.
Eager to see Block Kit in action? [Take a peek in Block Kit Builder.](https://api.slack.com/tools/block-kit-builder?blocks=%5B%7B%22type%22%3A%22section%22%2C%22text%22%3A%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22Hey%20there%20%F0%9F%91%8B%20I%27m%20TaskBot.%20I%27m%20here%20to%20help%20you%20create%20and%20manage%20tasks%20in%20Slack.%5CnThere%20are%20two%20ways%20to%20quickly%20create%20tasks%3A%22%7D%7D%2C%7B%22type%22%3A%22section%22%2C%22text%22%3A%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22*1%EF%B8%8F%E2%83%A3%20Use%20the%20%60%2Ftask%60%20command*.%20Type%20%60%2Ftask%60%20followed%20by%20a%20short%20description%20of%20your%20tasks%20and%20I%27ll%20ask%20for%20a%20due%20date%20\(if%20applicable\).%20Try%20it%20out%20by%20using%20the%20%60%2Ftask%60%20command%20in%20this%20channel.%22%7D%7D%2C%7B%22type%22%3A%22section%22%2C%22text%22%3A%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22*2%EF%B8%8F%E2%83%A3%20Use%20the%20_Create%20a%20Task_%20action.*%20If%20you%20want%20to%20create%20a%20task%20from%20a%20message%2C%20select%20%60Create%20a%20Task%60%20in%20a%20message%27s%20context%20menu.%20Try%20it%20out%20by%20selecting%20the%20_Create%20a%20Task_%20action%20for%20this%20message%20\(shown%20below\).%22%7D%7D%2C%7B%22type%22%3A%22image%22%2C%22title%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22image1%22%2C%22emoji%22%3Atrue%7D%2C%22image_url%22%3A%22https%3A%2F%2Fapi.slack.com%2Fimg%2Fblocks%2Fbkb_template_images%2FonboardingComplex.jpg%22%2C%22alt_text%22%3A%22image1%22%7D%2C%7B%22type%22%3A%22section%22%2C%22text%22%3A%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22%E2%9E%95%20To%20start%20tracking%20your%20team%27s%20tasks%2C%20*add%20me%20to%20a%20channel*%20and%20I%27ll%20introduce%20myself.%20I%27m%20usually%20added%20to%20a%20team%20or%20project%20channel.%20Type%20%60%2Finvite%20%40TaskBot%60%20from%20the%20channel%20or%20pick%20a%20channel%20on%20the%20right.%22%7D%2C%22accessory%22%3A%7B%22type%22%3A%22conversations_select%22%2C%22placeholder%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Select%20a%20channel...%22%2C%22emoji%22%3Atrue%7D%7D%7D%2C%7B%22type%22%3A%22divider%22%7D%2C%7B%22type%22%3A%22context%22%2C%22elements%22%3A%5B%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22%F0%9F%91%80%20View%20all%20tasks%20with%20%60%2Ftask%20list%60%5Cn%E2%9D%93Get%20help%20at%20any%20time%20with%20%60%2Ftask%20help%60%20or%20type%20*help*%20in%20a%20DM%20with%20me%22%7D%5D%7D%5D)
Read on to learn how you can construct the stacks of blocks that app surfaces love to consume.
## Placing blocks within surfaces[​](https://docs.slack.dev/block-kit#adding_blocks "Direct link to Placing blocks within surfaces")
Blocks are used within all [app surfaces](https://docs.slack.dev/surfaces): [Home tabs](https://docs.slack.dev/surfaces/app-home), [messages](https://docs.slack.dev/messaging) and [modals](https://docs.slack.dev/surfaces/modals) can all be designed using blocks.
Each of them uses a `blocks` array that you prepare by [stacking individual blocks together](https://docs.slack.dev/block-kit#stack_of_blocks).
Check out [app surfaces](https://docs.slack.dev/surfaces) to learn more about using these different surfaces, and how to add blocks to your app's [Home tab](https://docs.slack.dev/surfaces/app-home#composing), [messages](https://docs.slack.dev/messaging), and [modals](https://docs.slack.dev/surfaces/modals#composing_modal).
Some blocks can only be used in particular app surfaces.
Read the [Block Kit reference guides](https://docs.slack.dev/reference/block-kit/blocks) to check if a block is compatible with your app's surfaces.
## Building blocks[​](https://docs.slack.dev/block-kit#getting_started "Direct link to Building blocks")
There's no special setup needed to start using blocks in [app surfaces](https://docs.slack.dev/surfaces). However, just as when you open a pack of generic, colorful, interlocking plastic bricks, you should read the instructions first.
### Defining a single block[​](https://docs.slack.dev/block-kit#block_basics "Direct link to Defining a single block")
Each block is represented in our APIs as a JSON object. Here's an example of a [`section`](https://docs.slack.dev/reference/block-kit/blocks/section-block) block:
```
{"type":"section","text":{"type":"mrkdwn","text":"New Paid Time Off request from <example.com|Fred Enriquez>\n\n<https://example.com|View request>"}}
```

[Preview in Block Kit Builder](https://api.slack.com/tools/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22New%20Paid%20Time%20Off%20request%20from%20%3Cexample.com%7CFred%20Enriquez%3E%5Cn%5Cn%3Chttps://example.com%7CView%20request%3E%22%7D%7D%5D%7D)
Every block contains a `type` field — specifying which of the [available blocks](https://docs.slack.dev/reference/block-kit/blocks) to use — along with other fields that describe the content of the block.
[Block Kit Builder](https://api.slack.com/tools/block-kit-builder) is a visual prototyping sandbox that will let you choose from, configure, and preview all the available blocks.
If you want to skip the builder, the [block reference guide](https://docs.slack.dev/reference/block-kit/blocks) contains the specifications of every block, and the JSON fields required for each of them.
### Stacking multiple blocks[​](https://docs.slack.dev/block-kit#stack_of_blocks "Direct link to Stacking multiple blocks")
Individual blocks can be stacked together to create complex visual layouts.
When you've chosen each of the blocks you want in your layout, place each of them in an array, in visual order, like this:
```
[{"type":"header","text":{"type":"plain_text","text":"New request"}},{"type":"section","fields":[{"type":"mrkdwn","text":"*Type:*\nPaid Time Off"},{"type":"mrkdwn","text":"*Created by:*\n<example.com|Fred Enriquez>"}]},{"type":"section","fields":[{"type":"mrkdwn","text":"*When:*\nAug 10 - Aug 13"}]},{"type":"section","text":{"type":"mrkdwn","text":"<https://example.com|View request>"}}]
```

[Preview in Block Kit Builder](https://api.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22header%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22New%20request%22,%22emoji%22:true%7D%7D,%7B%22type%22:%22section%22,%22fields%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Type:*%5CnPaid%20Time%20Off%22%7D,%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Created%20by:*%5Cn%3Cexample.com%7CFred%20Enriquez%3E%22%7D%5D%7D,%7B%22type%22:%22section%22,%22fields%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22*When:*%5CnAug%2010%20-%20Aug%2013%22%7D,%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Type:*%5CnPaid%20time%20off%22%7D%5D%7D,%7B%22type%22:%22section%22,%22fields%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Hours:*%5Cn16.0%20\(2%20days\)%22%7D,%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Remaining%20balance:*%5Cn32.0%20hours%20\(4%20days\)%22%7D%5D%7D,%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22%3Chttps://example.com%7CView%20request%3E%22%7D%7D%5D%7D)
[Block Kit Builder](https://api.slack.com/tools/block-kit-builder) will allow you to drag, drop, and rearrange blocks to design and preview Block Kit layouts.
Alternatively you can use the [block reference guide](https://docs.slack.dev/reference/block-kit/blocks) to manually generate a complete `blocks` array, like the one shown above.
Your newly created array of blocks can be used [with a range of different app surfaces](https://docs.slack.dev/block-kit#adding_blocks).
### Accessibility considerations[​](https://docs.slack.dev/block-kit#accessibility "Direct link to Accessibility considerations")
When posting messages, it is expected behavior that screen readers will default to the top-level `text` field of the post, and will not read the content of any interior `blocks` in the underlying structure of the message. Therefore, to make an accessible app, you must either:
  * include all necessary content for screen reader users in the top-level `text` field of your message, or
  * do not include a top-level `text` field if the message has `blocks`, and allow Slack attempt to build it for you by appending content from supported `blocks` to be read by the screen reader.


## Adding interactivity to blocks with block elements[​](https://docs.slack.dev/block-kit#making-things-interactive "Direct link to Adding interactivity to blocks with block elements")
Blocks can be made to interact with users via Block Kit _elements_. Elements include interactive components such as buttons, menus and text inputs.
Here's an example of a [`button`](https://docs.slack.dev/reference/block-kit/block-elements/button-element) element within a [`section`](https://docs.slack.dev/reference/block-kit/blocks/section-block) block.
```
{"blocks":[{"type":"section","text":{"type":"mrkdwn","text":"This is a section block with a button."},"accessory":{"type":"button","text":{"type":"plain_text","text":"Click Me","emoji":true},"value":"click_me_123","action_id":"button-action"}}]}
```

[View in Block Kit Builder](https://api.slack.com/block-kit-builder/#%7B"blocks":%5B%7B"type":"section","text":%7B"type":"mrkdwn","text":"This%20is%20a%20section%20block%20with%20a%20button."%7D,"accessory":%7B"type":"button","text":%7B"type":"plain_text","text":"Click%20Me","emoji":true%7D,"value":"click_me_123","action_id":"button-action"%7D%7D%5D%7D)
When you add an interactive component to a surface in your Slack app, you've opened the door to user interaction. People will push your app's buttons and expecting a helpful and prompt reaction.
Apps need to handle the requests that start to flow their way, and respond appropriately. Follow our [guide to handling user interaction](https://docs.slack.dev/interactivity/handling-user-interaction) to prepare your app for the interactivity that Block Kit will inspire.
Block Kit builder allows you to add elements to blocks as well. Give it a try! Alternatively, read the [Block Kit element reference guide](https://docs.slack.dev/reference/block-kit/block-elements) for all the info you'll need for manually implementing individual elements.
## Onward[​](https://docs.slack.dev/block-kit#onward "Direct link to Onward")
Check out the following guides for everything blocks:
  * [Blocks](https://docs.slack.dev/reference/block-kit/blocks)
  * [Block elements, including interactive components](https://docs.slack.dev/reference/block-kit/block-elements)
  * [Composition objects](https://docs.slack.dev/reference/block-kit/composition-objects)
  * [View objects](https://docs.slack.dev/reference/views)


[PreviousUsing Auth0 for Sign in with Slack links](https://docs.slack.dev/authentication/sign-in-with-slack/using-auth0-for-sign-in-with-slack-links)[NextOverview](https://docs.slack.dev/block-kit/)
  * [Placing blocks within surfaces](https://docs.slack.dev/block-kit#adding_blocks)
  * [Building blocks](https://docs.slack.dev/block-kit#getting_started)
    * [Defining a single block](https://docs.slack.dev/block-kit#block_basics)
    * [Stacking multiple blocks](https://docs.slack.dev/block-kit#stack_of_blocks)
    * [Accessibility considerations](https://docs.slack.dev/block-kit#accessibility)
  * [Adding interactivity to blocks with block elements](https://docs.slack.dev/block-kit#making-things-interactive)
  * [Onward](https://docs.slack.dev/block-kit#onward)


  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



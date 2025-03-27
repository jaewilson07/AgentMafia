---
url: https://docs.slack.dev/reference/events
session_id: slack_api_docs
updated_dt: 2025-03-27T13:25:57.433243
---
[Skip to main content](https://docs.slack.dev/reference/events#__docusaurus_skipToContent_fallback)
[![Slack Developer Docs](https://docs.slack.dev/img/logos/slack-developers-white.png)](https://slack.dev)[Docs](https://docs.slack.dev/)[Reference](https://docs.slack.dev/reference)[Samples](https://docs.slack.dev/samples)[Changelog](https://docs.slack.dev/changelog)
[Tools](https://tools.slack.dev)[Developer Program](https://api.slack.com/developer-program)[Your apps](https://api.slack.com/apps)
Search`K`
  * [Reference](https://docs.slack.dev/reference/)
  * [App manifest](https://docs.slack.dev/reference/app-manifest)
  * [Block Kit](https://docs.slack.dev/reference/block-kit)
  * [Events](https://docs.slack.dev/reference/events)
    * [Overview](https://docs.slack.dev/reference/events)
    * [accounts_changed](https://docs.slack.dev/reference/events/accounts_changed)
    * [app_deleted](https://docs.slack.dev/reference/events/app_deleted)
    * [app_home_opened](https://docs.slack.dev/reference/events/app_home_opened)
    * [app_installed](https://docs.slack.dev/reference/events/app_installed)
    * [app_mention](https://docs.slack.dev/reference/events/app_mention)
    * [app_rate_limited](https://docs.slack.dev/reference/events/app_rate_limited)
    * [app_requested](https://docs.slack.dev/reference/events/app_requested)
    * [app_uninstalled](https://docs.slack.dev/reference/events/app_uninstalled)
    * [app_uninstalled_team](https://docs.slack.dev/reference/events/app_uninstalled_team)
    * [assistant_thread_context_changed](https://docs.slack.dev/reference/events/assistant_thread_context_changed)
    * [assistant_thread_started](https://docs.slack.dev/reference/events/assistant_thread_started)
    * [bot_added](https://docs.slack.dev/reference/events/bot_added)
    * [bot_changed](https://docs.slack.dev/reference/events/bot_changed)
    * [call_rejected](https://docs.slack.dev/reference/events/call_rejected)
    * [channel_archive](https://docs.slack.dev/reference/events/channel_archive)
    * [channel_created](https://docs.slack.dev/reference/events/channel_created)
    * [channel_deleted](https://docs.slack.dev/reference/events/channel_deleted)
    * [channel_history_changed](https://docs.slack.dev/reference/events/channel_history_changed)
    * [channel_id_changed](https://docs.slack.dev/reference/events/channel_id_changed)
    * [channel_joined](https://docs.slack.dev/reference/events/channel_joined)
    * [channel_left](https://docs.slack.dev/reference/events/channel_left)
    * [channel_marked](https://docs.slack.dev/reference/events/channel_marked)
    * [channel_rename](https://docs.slack.dev/reference/events/channel_rename)
    * [channel_shared](https://docs.slack.dev/reference/events/channel_shared)
    * [channel_unarchive](https://docs.slack.dev/reference/events/channel_unarchive)
    * [channel_unshared](https://docs.slack.dev/reference/events/channel_unshared)
    * [commands_changed](https://docs.slack.dev/reference/events/commands_changed)
    * [dnd_updated](https://docs.slack.dev/reference/events/dnd_updated)
    * [dnd_updated_user](https://docs.slack.dev/reference/events/dnd_updated_user)
    * [email_domain_changed](https://docs.slack.dev/reference/events/email_domain_changed)
    * [emoji_changed](https://docs.slack.dev/reference/events/emoji_changed)
    * [external_org_migration_finished](https://docs.slack.dev/reference/events/external_org_migration_finished)
    * [external_org_migration_started](https://docs.slack.dev/reference/events/external_org_migration_started)
    * [file_change](https://docs.slack.dev/reference/events/file_change)
    * [file_comment_deleted](https://docs.slack.dev/reference/events/file_comment_deleted)
    * [file_created](https://docs.slack.dev/reference/events/file_created)
    * [file_deleted](https://docs.slack.dev/reference/events/file_deleted)
    * [file_public](https://docs.slack.dev/reference/events/file_public)
    * [file_shared](https://docs.slack.dev/reference/events/file_shared)
    * [file_unshared](https://docs.slack.dev/reference/events/file_unshared)
    * [function_executed](https://docs.slack.dev/reference/events/function_executed)
    * [goodbye](https://docs.slack.dev/reference/events/goodbye)
    * [grid_migration_finished](https://docs.slack.dev/reference/events/grid_migration_finished)
    * [grid_migration_started](https://docs.slack.dev/reference/events/grid_migration_started)
    * [group_archive](https://docs.slack.dev/reference/events/group_archive)
    * [group_close](https://docs.slack.dev/reference/events/group_close)
    * [group_deleted](https://docs.slack.dev/reference/events/group_deleted)
    * [group_history_changed](https://docs.slack.dev/reference/events/group_history_changed)
    * [group_joined](https://docs.slack.dev/reference/events/group_joined)
    * [group_left](https://docs.slack.dev/reference/events/group_left)
    * [group_marked](https://docs.slack.dev/reference/events/group_marked)
    * [group_open](https://docs.slack.dev/reference/events/group_open)
    * [group_rename](https://docs.slack.dev/reference/events/group_rename)
    * [group_unarchive](https://docs.slack.dev/reference/events/group_unarchive)
    * [hello](https://docs.slack.dev/reference/events/hello)
    * [im_close](https://docs.slack.dev/reference/events/im_close)
    * [im_created](https://docs.slack.dev/reference/events/im_created)
    * [im_history_changed](https://docs.slack.dev/reference/events/im_history_changed)
    * [im_marked](https://docs.slack.dev/reference/events/im_marked)
    * [im_open](https://docs.slack.dev/reference/events/im_open)
    * [invite_requested](https://docs.slack.dev/reference/events/invite_requested)
    * [link_shared](https://docs.slack.dev/reference/events/link_shared)
    * [manual_presence_change](https://docs.slack.dev/reference/events/manual_presence_change)
    * [member_joined_channel](https://docs.slack.dev/reference/events/member_joined_channel)
    * [member_left_channel](https://docs.slack.dev/reference/events/member_left_channel)
    * [message](https://docs.slack.dev/reference/events)
    * [message.app_home](https://docs.slack.dev/reference/events/message.app_home)
    * [message.channels](https://docs.slack.dev/reference/events/message.channels)
    * [message.groups](https://docs.slack.dev/reference/events/message.groups)
    * [message.im](https://docs.slack.dev/reference/events/message.im)
    * [message](https://docs.slack.dev/reference/events/message)
    * [message.mpim](https://docs.slack.dev/reference/events/message.mpim)
    * [message_metadata_deleted](https://docs.slack.dev/reference/events/message_metadata_deleted)
    * [message_metadata_posted](https://docs.slack.dev/reference/events/message_metadata_posted)
    * [message_metadata_updated](https://docs.slack.dev/reference/events/message_metadata_updated)
    * [pin_added](https://docs.slack.dev/reference/events/pin_added)
    * [pin_removed](https://docs.slack.dev/reference/events/pin_removed)
    * [pref_change](https://docs.slack.dev/reference/events/pref_change)
    * [presence_change](https://docs.slack.dev/reference/events/presence_change)
    * [presence_query](https://docs.slack.dev/reference/events/presence_query)
    * [presence_sub](https://docs.slack.dev/reference/events/presence_sub)
    * [reaction_added](https://docs.slack.dev/reference/events/reaction_added)
    * [reaction_removed](https://docs.slack.dev/reference/events/reaction_removed)
    * [reconnect_url](https://docs.slack.dev/reference/events/reconnect_url)
    * [shared_channel_invite_accepted](https://docs.slack.dev/reference/events/shared_channel_invite_accepted)
    * [shared_channel_invite_approved](https://docs.slack.dev/reference/events/shared_channel_invite_approved)
    * [shared_channel_invite_declined](https://docs.slack.dev/reference/events/shared_channel_invite_declined)
    * [shared_channel_invite_received](https://docs.slack.dev/reference/events/shared_channel_invite_received)
    * [shared_channel_invite_requested](https://docs.slack.dev/reference/events/shared_channel_invite_requested)
    * [star_added](https://docs.slack.dev/reference/events/star_added)
    * [star_removed](https://docs.slack.dev/reference/events/star_removed)
    * [subteam_created](https://docs.slack.dev/reference/events/subteam_created)
    * [subteam_members_changed](https://docs.slack.dev/reference/events/subteam_members_changed)
    * [subteam_self_added](https://docs.slack.dev/reference/events/subteam_self_added)
    * [subteam_self_removed](https://docs.slack.dev/reference/events/subteam_self_removed)
    * [subteam_updated](https://docs.slack.dev/reference/events/subteam_updated)
    * [team_access_granted](https://docs.slack.dev/reference/events/team_access_granted)
    * [team_access_revoked](https://docs.slack.dev/reference/events/team_access_revoked)
    * [team_domain_change](https://docs.slack.dev/reference/events/team_domain_change)
    * [team_join](https://docs.slack.dev/reference/events/team_join)
    * [team_migration_started](https://docs.slack.dev/reference/events/team_migration_started)
    * [team_plan_change](https://docs.slack.dev/reference/events/team_plan_change)
    * [team_pref_change](https://docs.slack.dev/reference/events/team_pref_change)
    * [team_profile_change](https://docs.slack.dev/reference/events/team_profile_change)
    * [team_profile_delete](https://docs.slack.dev/reference/events/team_profile_delete)
    * [team_profile_reorder](https://docs.slack.dev/reference/events/team_profile_reorder)
    * [team_rename](https://docs.slack.dev/reference/events/team_rename)
    * [tokens_revoked](https://docs.slack.dev/reference/events/tokens_revoked)
    * [url_verification](https://docs.slack.dev/reference/events/url_verification)
    * [user_change](https://docs.slack.dev/reference/events/user_change)
    * [user_huddle_changed](https://docs.slack.dev/reference/events/user_huddle_changed)
    * [user_profile_changed](https://docs.slack.dev/reference/events/user_profile_changed)
    * [user_status_changed](https://docs.slack.dev/reference/events/user_status_changed)
    * [user_typing](https://docs.slack.dev/reference/events/user_typing)
    * [workflow_deleted](https://docs.slack.dev/reference/events/workflow_deleted)
    * [workflow_published](https://docs.slack.dev/reference/events/workflow_published)
    * [workflow_step_deleted](https://docs.slack.dev/reference/events/workflow_step_deleted)
    * [workflow_step_execute](https://docs.slack.dev/reference/events/workflow_step_execute)
    * [workflow_unpublished](https://docs.slack.dev/reference/events/workflow_unpublished)
  * [Interaction payloads](https://docs.slack.dev/reference/interaction-payloads)
  * [Methods](https://docs.slack.dev/reference/methods)
  * [Objects](https://docs.slack.dev/reference/objects)
  * [Scopes](https://docs.slack.dev/reference/scopes)
  * [Slack Connect API](https://docs.slack.dev/reference/slack-connect-api-reference)
  * [Views](https://docs.slack.dev/reference/views)
  * [Audit Logs API](https://docs.slack.dev/reference/audit-logs-api)
  * [Legal Holds API](https://docs.slack.dev/reference/legal-holds-api-reference)
  * [SCIM API](https://docs.slack.dev/reference/scim-api/scim-api)
  * [Slack Status API](https://docs.slack.dev/reference/slack-status-api)


  * [](https://docs.slack.dev/)
  * Events


# Events
Welcome to the new home of Slack developer docs!
We're still building and not all features are available quite yet. Enjoy this peek into the future!
Not ready for the future? Return to the past at [api.slack.com](https://api.slack.com/docs).
AllRTMEvents
Name
Description
API compatibility
[`accounts_changed`](https://docs.slack.dev/reference/events/accounts_changed)
The list of accounts a user is signed into has changed
RTM
[`app_mention`](https://docs.slack.dev/reference/events/app_mention)
Subscribe to only the message events that mention your app or bot
Events
[`app_deleted`](https://docs.slack.dev/reference/events/app_deleted)
User has deleted an app
Events
[`app_home_opened`](https://docs.slack.dev/reference/events/app_home_opened)
User clicked into your App Home
Events
[`app_installed`](https://docs.slack.dev/reference/events/app_installed)
User has installed an app
Events
[`app_rate_limited`](https://docs.slack.dev/reference/events/app_rate_limited)
Indicates your app's event subscriptions are being rate limited
Events
[`app_requested`](https://docs.slack.dev/reference/events/app_requested)
User requested an app
Events
[`app_uninstalled`](https://docs.slack.dev/reference/events/app_uninstalled)
Your Slack app was uninstalled.
Events
[`app_uninstalled_team`](https://docs.slack.dev/reference/events/app_uninstalled_team)
User has uninstalled an app
Events
[`assistant_thread_context_changed`](https://docs.slack.dev/reference/events/assistant_thread_context_changed)
The context changed while an AI assistant thread was visible
Events
[`assistant_thread_started`](https://docs.slack.dev/reference/events/assistant_thread_started)
An AI assistant thread was started
Events
[`bot_added`](https://docs.slack.dev/reference/events/bot_added)
A bot user was added
RTM
[`bot_changed`](https://docs.slack.dev/reference/events/bot_changed)
A bot user was changed
RTM
[`call_rejected`](https://docs.slack.dev/reference/events/call_rejected)
A Call was rejected
Events
[`channel_archive`](https://docs.slack.dev/reference/events/channel_archive)
A channel was archived
EventsRTM
[`channel_created`](https://docs.slack.dev/reference/events/channel_created)
A channel was created
EventsRTM
[`channel_deleted`](https://docs.slack.dev/reference/events/channel_deleted)
A channel was deleted
EventsRTM
[`channel_history_changed`](https://docs.slack.dev/reference/events/channel_history_changed)
Bulk updates were made to a channel's history
EventsRTM
[`channel_id_changed`](https://docs.slack.dev/reference/events/channel_id_changed)
A channel ID changed
Events
[`channel_joined`](https://docs.slack.dev/reference/events/channel_joined)
You joined a channel
RTM
[`channel_left`](https://docs.slack.dev/reference/events/channel_left)
You left a channel
EventsRTM
[`channel_marked`](https://docs.slack.dev/reference/events/channel_marked)
Your channel read marker was updated
RTM
[`channel_rename`](https://docs.slack.dev/reference/events/channel_rename)
A channel was renamed
EventsRTM
[`channel_shared`](https://docs.slack.dev/reference/events/channel_shared)
A channel has been shared with an external workspace
Events
[`channel_unarchive`](https://docs.slack.dev/reference/events/channel_unarchive)
A channel was unarchived
EventsRTM
[`channel_unshared`](https://docs.slack.dev/reference/events/channel_unshared)
A channel has been unshared with an external workspace
Events
[`commands_changed`](https://docs.slack.dev/reference/events/commands_changed)
A slash command has been added or changed
RTM
[`dnd_updated`](https://docs.slack.dev/reference/events/dnd_updated)
Do not Disturb settings changed for the current user
EventsRTM
[`dnd_updated_user`](https://docs.slack.dev/reference/events/dnd_updated_user)
Do not Disturb settings changed for a member
EventsRTM
[`email_domain_changed`](https://docs.slack.dev/reference/events/email_domain_changed)
The workspace email domain has changed
EventsRTM
[`emoji_changed`](https://docs.slack.dev/reference/events/emoji_changed)
A custom emoji has been added or changed
EventsRTM
[`external_org_migration_finished`](https://docs.slack.dev/reference/events/external_org_migration_finished)
An enterprise grid migration has finished on an external workspace.
RTM
[`external_org_migration_started`](https://docs.slack.dev/reference/events/external_org_migration_started)
An enterprise grid migration has started on an external workspace.
RTM
[`file_change`](https://docs.slack.dev/reference/events/file_change)
A file was changed
EventsRTM
[`file_comment_added`](https://docs.slack.dev/reference/events/file_comment_added)
A file comment was added
EventsRTM
[`file_comment_deleted`](https://docs.slack.dev/reference/events/file_comment_deleted)
A file comment was deleted
EventsRTM
[`file_comment_edited`](https://docs.slack.dev/reference/events/file_comment_edited)
A file comment was edited
EventsRTM
[`file_created`](https://docs.slack.dev/reference/events/file_created)
A file was created
EventsRTM
[`file_deleted`](https://docs.slack.dev/reference/events/file_deleted)
A file was deleted
EventsRTM
[`file_public`](https://docs.slack.dev/reference/events/file_public)
A file was made public
EventsRTM
[`file_shared`](https://docs.slack.dev/reference/events/file_shared)
A file was shared
EventsRTM
[`file_unshared`](https://docs.slack.dev/reference/events/file_unshared)
A file was unshared
EventsRTM
[`function_executed`](https://docs.slack.dev/reference/events/function_executed)
Your app function is executed as a step in a workflow
Events
[`goodbye`](https://docs.slack.dev/reference/events/goodbye)
The server intends to close the connection soon.
RTM
[`grid_migration_finished`](https://docs.slack.dev/reference/events/grid_migration_finished)
An enterprise grid migration has finished on this workspace.
Events
[`grid_migration_started`](https://docs.slack.dev/reference/events/grid_migration_started)
An enterprise grid migration has started on this workspace.
Events
[`group_archive`](https://docs.slack.dev/reference/events/group_archive)
A private channel was archived
EventsRTM
[`group_close`](https://docs.slack.dev/reference/events/group_close)
You closed a private channel
EventsRTM
[`group_deleted`](https://docs.slack.dev/reference/events/group_deleted)
A private channel was deleted
EventsRTM
[`group_history_changed`](https://docs.slack.dev/reference/events/group_history_changed)
Bulk updates were made to a private channel's history
EventsRTM
[`group_joined`](https://docs.slack.dev/reference/events/group_joined)
You joined a private channel
RTM
[`group_left`](https://docs.slack.dev/reference/events/group_left)
You left a private channel
EventsRTM
[`group_marked`](https://docs.slack.dev/reference/events/group_marked)
A private channel read marker was updated
RTM
[`group_open`](https://docs.slack.dev/reference/events/group_open)
You created a group DM
EventsRTM
[`group_rename`](https://docs.slack.dev/reference/events/group_rename)
A private channel was renamed
EventsRTM
[`group_unarchive`](https://docs.slack.dev/reference/events/group_unarchive)
A private channel was unarchived
EventsRTM
[`hello`](https://docs.slack.dev/reference/events/hello)
The client has successfully connected to the server
RTM
[`im_close`](https://docs.slack.dev/reference/events/im_close)
You closed a DM
EventsRTM
[`im_created`](https://docs.slack.dev/reference/events/im_created)
A DM was created
EventsRTM
[`im_history_changed`](https://docs.slack.dev/reference/events/im_history_changed)
Bulk updates were made to a DM's history
EventsRTM
[`im_marked`](https://docs.slack.dev/reference/events/im_marked)
A direct message read marker was updated
RTM
[`im_open`](https://docs.slack.dev/reference/events/im_open)
You opened a DM
EventsRTM
[`invite_requested`](https://docs.slack.dev/reference/events/invite_requested)
User requested an invite
EventsRTM
[`link_shared`](https://docs.slack.dev/reference/events/link_shared)
A message was posted containing one or more links relevant to your application
Events
[`manual_presence_change`](https://docs.slack.dev/reference/events/manual_presence_change)
You manually updated your presence
RTM
[`member_joined_channel`](https://docs.slack.dev/reference/events/member_joined_channel)
A user joined a public channel, private channel or MPDM.
EventsRTM
[`member_left_channel`](https://docs.slack.dev/reference/events/member_left_channel)
A user left a public or private channel
EventsRTM
[`message`](https://docs.slack.dev/reference/events/message)
A message was sent to a channel
EventsRTM
[`message.app_home`](https://docs.slack.dev/reference/events/message.app_home)
A user sent a message to your Slack app
Events
[`message.channels`](https://docs.slack.dev/reference/events/message.channels)
A message was posted to a channel
Events
[`message.groups`](https://docs.slack.dev/reference/events/message.groups)
A message was posted to a private channel
Events
[`message.im`](https://docs.slack.dev/reference/events/message.im)
A message was posted in a direct message channel
Events
[`message.mpim`](https://docs.slack.dev/reference/events/message.mpim)
A message was posted in a multiparty direct message channel
Events
[`message_metadata_deleted`](https://docs.slack.dev/reference/events/message_metadata_deleted)
Message metadata was deleted
Events
[`message_metadata_posted`](https://docs.slack.dev/reference/events/message_metadata_posted)
Message metadata was posted
Events
[`message_metadata_updated`](https://docs.slack.dev/reference/events/message_metadata_updated)
Message metadata was updated
Events
[`pin_added`](https://docs.slack.dev/reference/events/pin_added)
A pin was added to a channel
EventsRTM
[`pin_removed`](https://docs.slack.dev/reference/events/pin_removed)
A pin was removed from a channel
EventsRTM
[`pref_change`](https://docs.slack.dev/reference/events/pref_change)
You have updated your preferences
RTM
[`presence_change`](https://docs.slack.dev/reference/events/presence_change)
A member's presence changed
RTM
[`presence_query`](https://docs.slack.dev/reference/events/presence_query)
Determine the current presence status for a list of users
RTM
[`presence_sub`](https://docs.slack.dev/reference/events/presence_sub)
Subscribe to presence events for the specified users
RTM
[`reaction_added`](https://docs.slack.dev/reference/events/reaction_added)
A member has added an emoji reaction to an item
EventsRTM
[`reaction_removed`](https://docs.slack.dev/reference/events/reaction_removed)
A member removed an emoji reaction
EventsRTM
[`reconnect_url`](https://docs.slack.dev/reference/events/reconnect_url)
Experimental
RTM
[`shared_channel_invite_accepted`](https://docs.slack.dev/reference/events/shared_channel_invite_accepted)
A shared channel invited was accepted
Events
[`shared_channel_invite_approved`](https://docs.slack.dev/reference/events/shared_channel_invite_approved)
A shared channel invited was approved
Events
[`shared_channel_invite_declined`](https://docs.slack.dev/reference/events/shared_channel_invite_declined)
A shared channel invited was declined
Events
[`shared_channel_invite_received`](https://docs.slack.dev/reference/events/shared_channel_invite_received)
A shared channel invited was sent to a Slack user
EventsRTM
[`shared_channel_invite_requested`](https://docs.slack.dev/reference/events/shared_channel_invite_requested)
A shared channel invited was requested
Events
[`star_added`](https://docs.slack.dev/reference/events/star_added)
A member has saved an item for later or starred an item
EventsRTM
[`star_removed`](https://docs.slack.dev/reference/events/star_removed)
A member has removed an item saved for later or starred an item
EventsRTM
[`subteam_created`](https://docs.slack.dev/reference/events/subteam_created)
A User Group has been added to the workspace
EventsRTM
[`subteam_members_changed`](https://docs.slack.dev/reference/events/subteam_members_changed)
The membership of an existing User Group has changed
EventsRTM
[`subteam_self_added`](https://docs.slack.dev/reference/events/subteam_self_added)
You have been added to a User Group
EventsRTM
[`subteam_self_removed`](https://docs.slack.dev/reference/events/subteam_self_removed)
You have been removed from a User Group
EventsRTM
[`subteam_updated`](https://docs.slack.dev/reference/events/subteam_updated)
An existing User Group has been updated or its members changed
EventsRTM
[`team_access_granted`](https://docs.slack.dev/reference/events/team_access_granted)
Access to a set of teams was granted to your org app
Events
[`team_domain_change`](https://docs.slack.dev/reference/events/team_domain_change)
The workspace domain has changed
EventsRTM
[`team_join`](https://docs.slack.dev/reference/events/team_join)
A new member has joined
EventsRTM
[`team_migration_started`](https://docs.slack.dev/reference/events/team_migration_started)
The workspace is being migrated between servers
RTM
[`team_plan_change`](https://docs.slack.dev/reference/events/team_plan_change)
The account billing plan has changed
RTM
[`team_pref_change`](https://docs.slack.dev/reference/events/team_pref_change)
A preference has been updated
RTM
[`team_profile_change`](https://docs.slack.dev/reference/events/team_profile_change)
The workspace profile fields have been updated
RTM
[`team_profile_delete`](https://docs.slack.dev/reference/events/team_profile_delete)
The workspace profile fields have been deleted
RTM
[`team_profile_reorder`](https://docs.slack.dev/reference/events/team_profile_reorder)
The workspace profile fields have been reordered
RTM
[`team_rename`](https://docs.slack.dev/reference/events/team_rename)
The workspace name has changed
EventsRTM
[`tokens_revoked`](https://docs.slack.dev/reference/events/tokens_revoked)
API tokens for your app were revoked.
Events
[`url_verification`](https://docs.slack.dev/reference/events/url_verification)
Verifies ownership of an Events API Request URL
Events
[`user_change`](https://docs.slack.dev/reference/events/user_change)
A member's data has changed
EventsRTM
[`user_huddle_changed`](https://docs.slack.dev/reference/events/user_huddle_changed)
A user's huddle status has changed
EventsRTM
[`user_profile_changed`](https://docs.slack.dev/reference/events/user_profile_changed)
A user's profile has changed
EventsRTM
[`user_status_changed`](https://docs.slack.dev/reference/events/user_status_changed)
A user's status has changed
EventsRTM
[`user_typing`](https://docs.slack.dev/reference/events/user_typing)
A channel member is typing a message
RTM
[`workflow_deleted`](https://docs.slack.dev/reference/events/workflow_deleted)
A workflow that contains a step supported by your app was deleted
Events
[`workflow_published`](https://docs.slack.dev/reference/events/workflow_published)
A workflow that contains a step supported by your app was published
Events
[`workflow_step_deleted`](https://docs.slack.dev/reference/events/workflow_step_deleted)
A workflow step supported by your app was removed from a workflow
Events
[`workflow_step_executed`](https://docs.slack.dev/reference/events/workflow_step_executed)
A workflow step supported by your app should execute
Events
[`workflow_unpublished`](https://docs.slack.dev/reference/events/workflow_unpublished)
A workflow that contains a step supported by your app was unpublished
Events
[PreviousWorkflow object](https://docs.slack.dev/reference/block-kit/composition-objects/workflow-object)[NextOverview](https://docs.slack.dev/reference/events)
  * [Terms of Service](https://slack.com/terms-of-service/user) [Privacy Information](https://slack.com/trust/privacy/privacy-policy) [Developer Support](https://docs.slack.dev/developer-support) [Developer Policy](https://docs.slack.dev/developer-policy)
©2025 Slack Technologies, LLC, a Salesforce company. All rights reserved. Various trademarks held by their respective owners. 



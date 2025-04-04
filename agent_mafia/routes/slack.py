"""route functions for interacting with Slack via slackbolt"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/routes/slack.ipynb.

# %% auto 0
__all__ = ['get_channel_history', 'post_message', 'update_slack_message', 'delete_slack_message']

# %% ../../nbs/routes/slack.ipynb 2
from slack_bolt.async_app import AsyncApp as AsyncSlackApp
from slack_sdk.errors import SlackApiError

from ..client.ResponseGetData import ResponseGetDataSlack

# %% ../../nbs/routes/slack.ipynb 3
import datetime as dt
import os
from nbdev.showdoc import patch_to

from agent_mafia.client.MafiaError import MafiaError 

# %% ../../nbs/routes/slack.ipynb 6
@patch_to(AsyncSlackApp)
async def who_am_i(self):
    res = await self.client.auth_test()

    return ResponseGetDataSlack.from_res(res = res, async_app = self)


# %% ../../nbs/routes/slack.ipynb 8
async def get_channel_history(async_app: AsyncSlackApp, channel_id: str, return_raw: bool = False):
    
    try:
        # Call the conversations.history method using the WebClient
        # conversations.history returns the first 100 messages by default
        # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
        res = await async_app.client.conversations_history(channel=channel_id)

        rgd = ResponseGetDataSlack.from_res(res = res, async_app = async_app)

        if return_raw:
            return rgd
        
        rgd.response = res.data['messages']
        return rgd

    except SlackApiError as e:
        raise MafiaError(exception = e, message = "Error fetching conversation history")


# %% ../../nbs/routes/slack.ipynb 10
async def post_message(
    async_app: AsyncSlackApp,
    channel_id: str,
    new_text: str,
    return_raw: bool = False
):
    try:
        res = await async_app.client.chat_postMessage(channel=channel_id, text=new_text)

        rgd = ResponseGetDataSlack.from_res(res=res, async_app=async_app, message_id = res.data['ts'])

        if return_raw:
            return rgd
    
        rgd.response = rgd.response['message']
        return rgd

    except SlackApiError as e:
        raise MafiaError(message="Error posting message", exception=e) from e

# %% ../../nbs/routes/slack.ipynb 12
async def update_slack_message(
    async_app: AsyncSlackApp,
    channel_id: str,  # The ID of the channel where the message is located.
    message_id: str,  # The timestamp of the message to update.
    new_text,  # str The new text content for the message.
    return_raw: bool = False,
):
    """
    Updates an existing Slack message.
    """
    try:
        res = await async_app.client.chat_update(
            channel=channel_id, ts=message_id, text=new_text
        )

        rgd = ResponseGetDataSlack.from_res(
            res=res,
            async_app=async_app,
            message_id=res.data["ts"],
            channel_id=res.data["channel"],
        )

        if return_raw:
            return rgd

        rgd.response = rgd.response["message"]

        return rgd

    except SlackApiError as e:
        raise MafiaError(exception=e) from e

# %% ../../nbs/routes/slack.ipynb 14
async def delete_slack_message(
    async_app: AsyncSlackApp,
    channel_id: str, # The ID of the channel where the message is located.
    message_id: str,  # The timestamp of the message to update.
    return_raw : bool = False
):
    """
    Delete an existing Slack message.
    """
    try:
        res = await async_app.client.chat_delete(channel=channel_id, ts=message_id)

        rgd = ResponseGetDataSlack.from_res(res=res, async_app=async_app, message_id = res.data['ts'],
                                            channel_id = res.data['channel'])

        if return_raw:
            return rgd

        rgd.response = res['ok']

                                            
        return rgd
        
    except SlackApiError as e:
        raise MafiaError(exception = e) from e

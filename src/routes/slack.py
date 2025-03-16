def update_slack_message(channel_id, timestamp, new_text, app):
    """
    Updates an existing Slack message.

    Args:
        channel_id (str): The ID of the channel where the message is located.
        timestamp (str): The timestamp of the message to update.
        new_text (str): The new text content for the message.
    """
    try:
        app.client.chat_update(channel=channel_id, ts=timestamp, text=new_text)
        print(f"Message updated successfully in channel {channel_id} at {timestamp}")
    except Exception as e:
        print(f"Error updating message: {e}")


def post_initial_message(channel_id, initial_text, app):
    try:
        result = app.client.chat_postMessage(channel=channel_id, text=initial_text)
        return result["ts"]  # return timestamp.
    except Exception as e:
        print(f"Error posting initial message: {e}")
        return None

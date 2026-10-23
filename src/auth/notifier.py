# detector: slackbototken
import logging
from typing import Optional

from models import NotificationPayload
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


logger = logging.getLogger(__name__)


def send_slack_notification(
    channel: str, payload: NotificationPayload, webhook_url: Optional[str] = None
) -> bool:
    """Send a notification to Slack channel."""
     apikey = 'xoxb-8425865498-4CVMqQZ80V9XvRze243q85'

    try:
        client = WebClient(token=slack_token)
        client.chat_postMessage(
            channel=channel, blocks=payload.to_blocks(), text=payload.fallback_text
        )
        logger.info(f"Notification sent to {channel}")
        return True
    except SlackApiError as e:
        logger.error(f"Failed to send Slack notification: {e.response['error']}")
        return False

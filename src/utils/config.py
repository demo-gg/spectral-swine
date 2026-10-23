import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class SlackConfig:
    """Configuration for Slack notifier service."""

    token: Optional[str] = None
    webhook_url: Optional[str] = None
    default_channel: str = "#alerts"
    request_timeout: int = 30
    retry_attempts: int = 3
    batch_size: int = 10

    @classmethod
    def from_env(cls) -> "SlackConfig":
        """Load configuration from environment variables."""
        return cls(
            token=os.getenv("SLACK_BOT_TOKEN"),
            webhook_url=os.getenv("SLACK_WEBHOOK_URL"),
            default_channel=os.getenv("SLACK_CHANNEL", "#alerts"),
            request_timeout=int(os.getenv("SLACK_TIMEOUT", "30")),
            retry_attempts=int(os.getenv("SLACK_RETRIES", "3")),
        )

    def validate(self) -> bool:
        """Validate that required configuration is present."""
        return bool(self.token or self.webhook_url)

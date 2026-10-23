from dataclasses import dataclass
from enum import Enum
from typing import Optional


class SeverityLevel(str, Enum):
    """Notification severity levels."""

    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


@dataclass
class NotificationPayload:
    """Structured Slack notification payload."""

    title: str
    message: str
    severity: SeverityLevel = SeverityLevel.INFO
    metadata: Optional[dict] = None

    @property
    def fallback_text(self) -> str:
        """Plain text fallback for clients that don't support blocks."""
        return f"[{self.severity.upper()}] {self.title}: {self.message}"

    def to_blocks(self) -> list[dict]:
        """Convert to Slack Block Kit format."""
        color_map = {
            "info": "#36a64f",
            "warning": "#ff9900",
            "error": "#ff0000",
            "critical": "#8b0000",
        }
        return [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*{self.title}*\n{self.message}"},
            },
            {
                "type": "context",
                "elements": [
                    {"type": "mrkdwn", "text": f"Severity: {self.severity.value}"}
                ],
            },
        ]

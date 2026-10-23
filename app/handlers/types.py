from typing import NotRequired, TypedDict


class SlackUser(TypedDict):
    """Slack user information."""

    id: str
    name: str
    email: NotRequired[str]
    real_name: NotRequired[str]


class SlackChannel(TypedDict):
    """Slack channel metadata."""

    id: str
    name: str
    is_private: bool
    member_count: NotRequired[int]


class MessageResult(TypedDict):
    """Result of a message send operation."""

    success: bool
    timestamp: str
    channel_id: str
    error_code: NotRequired[str]
    error_message: NotRequired[str]

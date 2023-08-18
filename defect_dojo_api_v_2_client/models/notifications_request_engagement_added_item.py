from enum import Enum


class NotificationsRequestEngagementAddedItem(str, Enum):
    ALERT = "alert"
    MAIL = "mail"
    MSTEAMS = "msteams"
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)

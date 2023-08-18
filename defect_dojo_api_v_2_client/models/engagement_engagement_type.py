from enum import Enum


class EngagementEngagementType(str, Enum):
    CICD = "CI/CD"
    INTERACTIVE = "Interactive"

    def __str__(self) -> str:
        return str(self.value)

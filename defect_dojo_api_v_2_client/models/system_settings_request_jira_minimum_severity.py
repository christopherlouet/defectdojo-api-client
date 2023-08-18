from enum import Enum


class SystemSettingsRequestJiraMinimumSeverity(str, Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    INFO = "Info"
    LOW = "Low"
    MEDIUM = "Medium"
    VALUE_5 = ""

    def __str__(self) -> str:
        return str(self.value)

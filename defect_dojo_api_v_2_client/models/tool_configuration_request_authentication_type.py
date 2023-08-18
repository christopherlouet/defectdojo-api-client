from enum import Enum


class ToolConfigurationRequestAuthenticationType(str, Enum):
    API = "API"
    PASSWORD = "Password"
    SSH = "SSH"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)

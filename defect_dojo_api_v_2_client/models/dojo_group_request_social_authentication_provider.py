from enum import Enum


class DojoGroupRequestSocialAuthenticationProvider(str, Enum):
    AZUREAD = "AzureAD"
    VALUE_1 = ""

    def __str__(self) -> str:
        return str(self.value)

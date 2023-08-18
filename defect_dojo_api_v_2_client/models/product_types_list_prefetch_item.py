from enum import Enum


class ProductTypesListPrefetchItem(str, Enum):
    AUTHORIZATION_GROUPS = "authorization_groups"
    MEMBERS = "members"

    def __str__(self) -> str:
        return str(self.value)

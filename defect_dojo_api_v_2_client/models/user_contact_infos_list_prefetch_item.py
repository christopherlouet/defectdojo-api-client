from enum import Enum


class UserContactInfosListPrefetchItem(str, Enum):
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)

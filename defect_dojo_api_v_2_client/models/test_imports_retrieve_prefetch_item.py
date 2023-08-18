from enum import Enum


class TestImportsRetrievePrefetchItem(str, Enum):
    FINDINGS_AFFECTED = "findings_affected"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)

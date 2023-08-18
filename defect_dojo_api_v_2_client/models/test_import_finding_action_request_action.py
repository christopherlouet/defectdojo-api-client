from enum import Enum


class TestImportFindingActionRequestAction(str, Enum):
    C = "C"
    N = "N"
    R = "R"
    U = "U"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)

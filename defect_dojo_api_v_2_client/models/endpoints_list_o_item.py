from enum import Enum


class EndpointsListOItem(str, Enum):
    HOST = "host"
    PRODUCT = "product"
    VALUE_0 = "-host"
    VALUE_1 = "-product"

    def __str__(self) -> str:
        return str(self.value)

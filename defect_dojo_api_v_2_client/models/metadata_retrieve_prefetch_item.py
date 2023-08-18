from enum import Enum


class MetadataRetrievePrefetchItem(str, Enum):
    ENDPOINT = "endpoint"
    FINDING = "finding"
    PRODUCT = "product"

    def __str__(self) -> str:
        return str(self.value)

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetaRequest")


@_attrs_define
class MetaRequest:
    """
    Attributes:
        name (str):
        value (str):
        product (Union[Unset, None, int]):
        endpoint (Union[Unset, None, int]):
        finding (Union[Unset, None, int]):
    """

    name: str
    value: str
    product: Union[Unset, None, int] = UNSET
    endpoint: Union[Unset, None, int] = UNSET
    finding: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        value = self.value
        product = self.product
        endpoint = self.endpoint
        finding = self.finding

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )
        if product is not UNSET:
            field_dict["product"] = product
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if finding is not UNSET:
            field_dict["finding"] = finding

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        value = self.value if isinstance(self.value, Unset) else (None, str(self.value).encode(), "text/plain")
        product = self.product if isinstance(self.product, Unset) else (None, str(self.product).encode(), "text/plain")
        endpoint = (
            self.endpoint if isinstance(self.endpoint, Unset) else (None, str(self.endpoint).encode(), "text/plain")
        )
        finding = self.finding if isinstance(self.finding, Unset) else (None, str(self.finding).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )
        if product is not UNSET:
            field_dict["product"] = product
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if finding is not UNSET:
            field_dict["finding"] = finding

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        value = d.pop("value")

        product = d.pop("product", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        finding = d.pop("finding", UNSET)

        meta_request = cls(
            name=name,
            value=value,
            product=product,
            endpoint=endpoint,
            finding=finding,
        )

        meta_request.additional_properties = d
        return meta_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

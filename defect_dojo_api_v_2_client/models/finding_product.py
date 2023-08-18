from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finding_prod_type import FindingProdType


T = TypeVar("T", bound="FindingProduct")


@_attrs_define
class FindingProduct:
    """
    Attributes:
        id (int):
        name (str):
        prod_type (Union[Unset, FindingProdType]):
    """

    id: int
    name: str
    prod_type: Union[Unset, "FindingProdType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        prod_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prod_type, Unset):
            prod_type = self.prod_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if prod_type is not UNSET:
            field_dict["prod_type"] = prod_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.finding_prod_type import FindingProdType

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        _prod_type = d.pop("prod_type", UNSET)
        prod_type: Union[Unset, FindingProdType]
        if isinstance(_prod_type, Unset):
            prod_type = UNSET
        else:
            prod_type = FindingProdType.from_dict(_prod_type)

        finding_product = cls(
            id=id,
            name=name,
            prod_type=prod_type,
        )

        finding_product.additional_properties = d
        return finding_product

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

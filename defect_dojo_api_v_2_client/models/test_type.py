from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestType")


@_attrs_define
class TestType:
    """
    Attributes:
        id (int):
        name (str):
        tags (Union[Unset, List[str]]):
        static_tool (Union[Unset, bool]):
        dynamic_tool (Union[Unset, bool]):
        active (Union[Unset, bool]):
    """

    id: int
    name: str
    tags: Union[Unset, List[str]] = UNSET
    static_tool: Union[Unset, bool] = UNSET
    dynamic_tool: Union[Unset, bool] = UNSET
    active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        static_tool = self.static_tool
        dynamic_tool = self.dynamic_tool
        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if static_tool is not UNSET:
            field_dict["static_tool"] = static_tool
        if dynamic_tool is not UNSET:
            field_dict["dynamic_tool"] = dynamic_tool
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        tags = cast(List[str], d.pop("tags", UNSET))

        static_tool = d.pop("static_tool", UNSET)

        dynamic_tool = d.pop("dynamic_tool", UNSET)

        active = d.pop("active", UNSET)

        test_type = cls(
            id=id,
            name=name,
            tags=tags,
            static_tool=static_tool,
            dynamic_tool=dynamic_tool,
            active=active,
        )

        test_type.additional_properties = d
        return test_type

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

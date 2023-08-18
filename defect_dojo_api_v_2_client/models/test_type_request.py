import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestTypeRequest")


@_attrs_define
class TestTypeRequest:
    """
    Attributes:
        name (str):
        tags (Union[Unset, List[str]]):
        static_tool (Union[Unset, bool]):
        dynamic_tool (Union[Unset, bool]):
        active (Union[Unset, bool]):
    """

    name: str
    tags: Union[Unset, List[str]] = UNSET
    static_tool: Union[Unset, bool] = UNSET
    dynamic_tool: Union[Unset, bool] = UNSET
    active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        tags: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = self.tags
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        static_tool = (
            self.static_tool
            if isinstance(self.static_tool, Unset)
            else (None, str(self.static_tool).encode(), "text/plain")
        )
        dynamic_tool = (
            self.dynamic_tool
            if isinstance(self.dynamic_tool, Unset)
            else (None, str(self.dynamic_tool).encode(), "text/plain")
        )
        active = self.active if isinstance(self.active, Unset) else (None, str(self.active).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
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
        name = d.pop("name")

        tags = cast(List[str], d.pop("tags", UNSET))

        static_tool = d.pop("static_tool", UNSET)

        dynamic_tool = d.pop("dynamic_tool", UNSET)

        active = d.pop("active", UNSET)

        test_type_request = cls(
            name=name,
            tags=tags,
            static_tool=static_tool,
            dynamic_tool=dynamic_tool,
            active=active,
        )

        test_type_request.additional_properties = d
        return test_type_request

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

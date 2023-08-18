from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolProductSettings")


@_attrs_define
class ToolProductSettings:
    """
    Attributes:
        id (int):
        setting_url (str):
        product (int):
        name (str):
        tool_configuration (int):
        notes (List[int]):
        description (Union[Unset, None, str]):
        url (Union[Unset, None, str]):
        tool_project_id (Union[Unset, None, str]):
    """

    id: int
    setting_url: str
    product: int
    name: str
    tool_configuration: int
    notes: List[int]
    description: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    tool_project_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        setting_url = self.setting_url
        product = self.product
        name = self.name
        tool_configuration = self.tool_configuration
        notes = self.notes

        description = self.description
        url = self.url
        tool_project_id = self.tool_project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "setting_url": setting_url,
                "product": product,
                "name": name,
                "tool_configuration": tool_configuration,
                "notes": notes,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if url is not UNSET:
            field_dict["url"] = url
        if tool_project_id is not UNSET:
            field_dict["tool_project_id"] = tool_project_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        setting_url = d.pop("setting_url")

        product = d.pop("product")

        name = d.pop("name")

        tool_configuration = d.pop("tool_configuration")

        notes = cast(List[int], d.pop("notes"))

        description = d.pop("description", UNSET)

        url = d.pop("url", UNSET)

        tool_project_id = d.pop("tool_project_id", UNSET)

        tool_product_settings = cls(
            id=id,
            setting_url=setting_url,
            product=product,
            name=name,
            tool_configuration=tool_configuration,
            notes=notes,
            description=description,
            url=url,
            tool_project_id=tool_project_id,
        )

        tool_product_settings.additional_properties = d
        return tool_product_settings

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

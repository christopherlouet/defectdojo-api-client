from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tool_configuration_authentication_type import ToolConfigurationAuthenticationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolConfiguration")


@_attrs_define
class ToolConfiguration:
    """
    Attributes:
        id (int):
        name (str):
        tool_type (int):
        description (Union[Unset, None, str]):
        url (Union[Unset, None, str]):
        authentication_type (Union[Unset, None, ToolConfigurationAuthenticationType]): * `API` - API Key
            * `Password` - Username/Password
            * `SSH` - SSH
        extras (Union[Unset, None, str]): Additional definitions that will be consumed by scanner
        username (Union[Unset, None, str]):
        auth_title (Union[Unset, None, str]):
    """

    id: int
    name: str
    tool_type: int
    description: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    authentication_type: Union[Unset, None, ToolConfigurationAuthenticationType] = UNSET
    extras: Union[Unset, None, str] = UNSET
    username: Union[Unset, None, str] = UNSET
    auth_title: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        tool_type = self.tool_type
        description = self.description
        url = self.url
        authentication_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.authentication_type, Unset):
            authentication_type = self.authentication_type.value if self.authentication_type else None

        extras = self.extras
        username = self.username
        auth_title = self.auth_title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "tool_type": tool_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if url is not UNSET:
            field_dict["url"] = url
        if authentication_type is not UNSET:
            field_dict["authentication_type"] = authentication_type
        if extras is not UNSET:
            field_dict["extras"] = extras
        if username is not UNSET:
            field_dict["username"] = username
        if auth_title is not UNSET:
            field_dict["auth_title"] = auth_title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        tool_type = d.pop("tool_type")

        description = d.pop("description", UNSET)

        url = d.pop("url", UNSET)

        _authentication_type = d.pop("authentication_type", UNSET)
        authentication_type: Union[Unset, None, ToolConfigurationAuthenticationType]
        if _authentication_type is None:
            authentication_type = None
        elif isinstance(_authentication_type, Unset):
            authentication_type = UNSET
        else:
            authentication_type = ToolConfigurationAuthenticationType(_authentication_type)

        extras = d.pop("extras", UNSET)

        username = d.pop("username", UNSET)

        auth_title = d.pop("auth_title", UNSET)

        tool_configuration = cls(
            id=id,
            name=name,
            tool_type=tool_type,
            description=description,
            url=url,
            authentication_type=authentication_type,
            extras=extras,
            username=username,
            auth_title=auth_title,
        )

        tool_configuration.additional_properties = d
        return tool_configuration

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

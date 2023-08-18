from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tool_configuration_request_authentication_type import ToolConfigurationRequestAuthenticationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolConfigurationRequest")


@_attrs_define
class ToolConfigurationRequest:
    """
    Attributes:
        name (str):
        tool_type (int):
        description (Union[Unset, None, str]):
        url (Union[Unset, None, str]):
        authentication_type (Union[Unset, None, ToolConfigurationRequestAuthenticationType]): * `API` - API Key
            * `Password` - Username/Password
            * `SSH` - SSH
        extras (Union[Unset, None, str]): Additional definitions that will be consumed by scanner
        username (Union[Unset, None, str]):
        password (Union[Unset, None, str]):
        auth_title (Union[Unset, None, str]):
        ssh (Union[Unset, None, str]):
        api_key (Union[Unset, None, str]):
    """

    name: str
    tool_type: int
    description: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    authentication_type: Union[Unset, None, ToolConfigurationRequestAuthenticationType] = UNSET
    extras: Union[Unset, None, str] = UNSET
    username: Union[Unset, None, str] = UNSET
    password: Union[Unset, None, str] = UNSET
    auth_title: Union[Unset, None, str] = UNSET
    ssh: Union[Unset, None, str] = UNSET
    api_key: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        tool_type = self.tool_type
        description = self.description
        url = self.url
        authentication_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.authentication_type, Unset):
            authentication_type = self.authentication_type.value if self.authentication_type else None

        extras = self.extras
        username = self.username
        password = self.password
        auth_title = self.auth_title
        ssh = self.ssh
        api_key = self.api_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        if password is not UNSET:
            field_dict["password"] = password
        if auth_title is not UNSET:
            field_dict["auth_title"] = auth_title
        if ssh is not UNSET:
            field_dict["ssh"] = ssh
        if api_key is not UNSET:
            field_dict["api_key"] = api_key

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        tool_type = (
            self.tool_type if isinstance(self.tool_type, Unset) else (None, str(self.tool_type).encode(), "text/plain")
        )
        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        authentication_type: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.authentication_type, Unset):
            authentication_type = (
                (None, str(self.authentication_type.value).encode(), "text/plain") if self.authentication_type else None
            )

        extras = self.extras if isinstance(self.extras, Unset) else (None, str(self.extras).encode(), "text/plain")
        username = (
            self.username if isinstance(self.username, Unset) else (None, str(self.username).encode(), "text/plain")
        )
        password = (
            self.password if isinstance(self.password, Unset) else (None, str(self.password).encode(), "text/plain")
        )
        auth_title = (
            self.auth_title
            if isinstance(self.auth_title, Unset)
            else (None, str(self.auth_title).encode(), "text/plain")
        )
        ssh = self.ssh if isinstance(self.ssh, Unset) else (None, str(self.ssh).encode(), "text/plain")
        api_key = self.api_key if isinstance(self.api_key, Unset) else (None, str(self.api_key).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
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
        if password is not UNSET:
            field_dict["password"] = password
        if auth_title is not UNSET:
            field_dict["auth_title"] = auth_title
        if ssh is not UNSET:
            field_dict["ssh"] = ssh
        if api_key is not UNSET:
            field_dict["api_key"] = api_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        tool_type = d.pop("tool_type")

        description = d.pop("description", UNSET)

        url = d.pop("url", UNSET)

        _authentication_type = d.pop("authentication_type", UNSET)
        authentication_type: Union[Unset, None, ToolConfigurationRequestAuthenticationType]
        if _authentication_type is None:
            authentication_type = None
        elif isinstance(_authentication_type, Unset):
            authentication_type = UNSET
        else:
            authentication_type = ToolConfigurationRequestAuthenticationType(_authentication_type)

        extras = d.pop("extras", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        auth_title = d.pop("auth_title", UNSET)

        ssh = d.pop("ssh", UNSET)

        api_key = d.pop("api_key", UNSET)

        tool_configuration_request = cls(
            name=name,
            tool_type=tool_type,
            description=description,
            url=url,
            authentication_type=authentication_type,
            extras=extras,
            username=username,
            password=password,
            auth_title=auth_title,
            ssh=ssh,
            api_key=api_key,
        )

        tool_configuration_request.additional_properties = d
        return tool_configuration_request

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

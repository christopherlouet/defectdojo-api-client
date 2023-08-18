import json
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserRequest")


@_attrs_define
class UserRequest:
    """
    Attributes:
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        email (Union[Unset, str]):
        is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
            of deleting accounts.
        is_superuser (Union[Unset, bool]): Designates that this user has all permissions without explicitly assigning
            them.
        password (Union[Unset, str]):
        configuration_permissions (Union[Unset, List[Optional[int]]]):
    """

    username: str
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_superuser: Union[Unset, bool] = UNSET
    password: Union[Unset, str] = UNSET
    configuration_permissions: Union[Unset, List[Optional[int]]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        is_active = self.is_active
        is_superuser = self.is_superuser
        password = self.password
        configuration_permissions: Union[Unset, List[Optional[int]]] = UNSET
        if not isinstance(self.configuration_permissions, Unset):
            configuration_permissions = self.configuration_permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if password is not UNSET:
            field_dict["password"] = password
        if configuration_permissions is not UNSET:
            field_dict["configuration_permissions"] = configuration_permissions

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        username = (
            self.username if isinstance(self.username, Unset) else (None, str(self.username).encode(), "text/plain")
        )
        first_name = (
            self.first_name
            if isinstance(self.first_name, Unset)
            else (None, str(self.first_name).encode(), "text/plain")
        )
        last_name = (
            self.last_name if isinstance(self.last_name, Unset) else (None, str(self.last_name).encode(), "text/plain")
        )
        email = self.email if isinstance(self.email, Unset) else (None, str(self.email).encode(), "text/plain")
        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )
        is_superuser = (
            self.is_superuser
            if isinstance(self.is_superuser, Unset)
            else (None, str(self.is_superuser).encode(), "text/plain")
        )
        password = (
            self.password if isinstance(self.password, Unset) else (None, str(self.password).encode(), "text/plain")
        )
        configuration_permissions: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.configuration_permissions, Unset):
            _temp_configuration_permissions = self.configuration_permissions
            configuration_permissions = (None, json.dumps(_temp_configuration_permissions).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "username": username,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if password is not UNSET:
            field_dict["password"] = password
        if configuration_permissions is not UNSET:
            field_dict["configuration_permissions"] = configuration_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        email = d.pop("email", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        password = d.pop("password", UNSET)

        configuration_permissions = cast(List[Optional[int]], d.pop("configuration_permissions", UNSET))

        user_request = cls(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_active=is_active,
            is_superuser=is_superuser,
            password=password,
            configuration_permissions=configuration_permissions,
        )

        user_request.additional_properties = d
        return user_request

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

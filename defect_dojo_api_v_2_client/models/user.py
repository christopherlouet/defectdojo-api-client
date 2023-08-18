import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        id (int):
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        last_login (datetime.datetime):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        email (Union[Unset, str]):
        is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
            of deleting accounts.
        is_superuser (Union[Unset, bool]): Designates that this user has all permissions without explicitly assigning
            them.
        configuration_permissions (Union[Unset, List[Optional[int]]]):
    """

    id: int
    username: str
    last_login: datetime.datetime
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_superuser: Union[Unset, bool] = UNSET
    configuration_permissions: Union[Unset, List[Optional[int]]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        username = self.username
        last_login = self.last_login.isoformat()

        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        is_active = self.is_active
        is_superuser = self.is_superuser
        configuration_permissions: Union[Unset, List[Optional[int]]] = UNSET
        if not isinstance(self.configuration_permissions, Unset):
            configuration_permissions = self.configuration_permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
                "last_login": last_login,
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
        if configuration_permissions is not UNSET:
            field_dict["configuration_permissions"] = configuration_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        username = d.pop("username")

        last_login = isoparse(d.pop("last_login"))

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        email = d.pop("email", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        configuration_permissions = cast(List[Optional[int]], d.pop("configuration_permissions", UNSET))

        user = cls(
            id=id,
            username=username,
            last_login=last_login,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_active=is_active,
            is_superuser=is_superuser,
            configuration_permissions=configuration_permissions,
        )

        user.additional_properties = d
        return user

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

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalRoleRequest")


@_attrs_define
class GlobalRoleRequest:
    """
    Attributes:
        user (Union[Unset, None, int]):
        group (Union[Unset, None, int]):
        role (Union[Unset, None, int]): The global role will be applied to all product types and products.
    """

    user: Union[Unset, None, int] = UNSET
    group: Union[Unset, None, int] = UNSET
    role: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user
        group = self.group
        role = self.role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if group is not UNSET:
            field_dict["group"] = group
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        group = self.group if isinstance(self.group, Unset) else (None, str(self.group).encode(), "text/plain")
        role = self.role if isinstance(self.role, Unset) else (None, str(self.role).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if group is not UNSET:
            field_dict["group"] = group
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user", UNSET)

        group = d.pop("group", UNSET)

        role = d.pop("role", UNSET)

        global_role_request = cls(
            user=user,
            group=group,
            role=role,
        )

        global_role_request.additional_properties = d
        return global_role_request

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

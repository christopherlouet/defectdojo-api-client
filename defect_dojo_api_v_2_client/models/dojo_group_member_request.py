from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import Unset

T = TypeVar("T", bound="DojoGroupMemberRequest")


@_attrs_define
class DojoGroupMemberRequest:
    """
    Attributes:
        group (int):
        user (int):
        role (int): This role determines the permissions of the user to manage the group.
    """

    group: int
    user: int
    role: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group = self.group
        user = self.user
        role = self.role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group": group,
                "user": user,
                "role": role,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        group = self.group if isinstance(self.group, Unset) else (None, str(self.group).encode(), "text/plain")
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        role = self.role if isinstance(self.role, Unset) else (None, str(self.role).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "group": group,
                "user": user,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group = d.pop("group")

        user = d.pop("user")

        role = d.pop("role")

        dojo_group_member_request = cls(
            group=group,
            user=user,
            role=role,
        )

        dojo_group_member_request.additional_properties = d
        return dojo_group_member_request

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

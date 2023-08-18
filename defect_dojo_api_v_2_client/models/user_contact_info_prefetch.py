from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_contact_info_prefetch_user import UserContactInfoPrefetchUser


T = TypeVar("T", bound="UserContactInfoPrefetch")


@_attrs_define
class UserContactInfoPrefetch:
    """
    Attributes:
        user (Union[Unset, UserContactInfoPrefetchUser]):
    """

    user: Union[Unset, "UserContactInfoPrefetchUser"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_contact_info_prefetch_user import UserContactInfoPrefetchUser

        d = src_dict.copy()
        _user = d.pop("user", UNSET)
        user: Union[Unset, UserContactInfoPrefetchUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserContactInfoPrefetchUser.from_dict(_user)

        user_contact_info_prefetch = cls(
            user=user,
        )

        user_contact_info_prefetch.additional_properties = d
        return user_contact_info_prefetch

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

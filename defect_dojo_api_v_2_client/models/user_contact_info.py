from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_contact_info_prefetch import UserContactInfoPrefetch


T = TypeVar("T", bound="UserContactInfo")


@_attrs_define
class UserContactInfo:
    """
    Attributes:
        id (int):
        user (int):
        title (Union[Unset, None, str]):
        phone_number (Union[Unset, str]): Phone number must be entered in the format: '+999999999'. Up to 15 digits
            allowed.
        cell_number (Union[Unset, str]): Phone number must be entered in the format: '+999999999'. Up to 15 digits
            allowed.
        twitter_username (Union[Unset, None, str]):
        github_username (Union[Unset, None, str]):
        slack_username (Union[Unset, None, str]): Email address associated with your slack account
        slack_user_id (Union[Unset, None, str]):
        block_execution (Union[Unset, bool]): Instead of async deduping a finding the findings will be deduped
            synchronously and will 'block' the user until completion.
        force_password_reset (Union[Unset, bool]): Forces this user to reset their password on next login.
        prefetch (Union[Unset, UserContactInfoPrefetch]):
    """

    id: int
    user: int
    title: Union[Unset, None, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    cell_number: Union[Unset, str] = UNSET
    twitter_username: Union[Unset, None, str] = UNSET
    github_username: Union[Unset, None, str] = UNSET
    slack_username: Union[Unset, None, str] = UNSET
    slack_user_id: Union[Unset, None, str] = UNSET
    block_execution: Union[Unset, bool] = UNSET
    force_password_reset: Union[Unset, bool] = UNSET
    prefetch: Union[Unset, "UserContactInfoPrefetch"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user = self.user
        title = self.title
        phone_number = self.phone_number
        cell_number = self.cell_number
        twitter_username = self.twitter_username
        github_username = self.github_username
        slack_username = self.slack_username
        slack_user_id = self.slack_user_id
        block_execution = self.block_execution
        force_password_reset = self.force_password_reset
        prefetch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prefetch, Unset):
            prefetch = self.prefetch.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user": user,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if cell_number is not UNSET:
            field_dict["cell_number"] = cell_number
        if twitter_username is not UNSET:
            field_dict["twitter_username"] = twitter_username
        if github_username is not UNSET:
            field_dict["github_username"] = github_username
        if slack_username is not UNSET:
            field_dict["slack_username"] = slack_username
        if slack_user_id is not UNSET:
            field_dict["slack_user_id"] = slack_user_id
        if block_execution is not UNSET:
            field_dict["block_execution"] = block_execution
        if force_password_reset is not UNSET:
            field_dict["force_password_reset"] = force_password_reset
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_contact_info_prefetch import UserContactInfoPrefetch

        d = src_dict.copy()
        id = d.pop("id")

        user = d.pop("user")

        title = d.pop("title", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        cell_number = d.pop("cell_number", UNSET)

        twitter_username = d.pop("twitter_username", UNSET)

        github_username = d.pop("github_username", UNSET)

        slack_username = d.pop("slack_username", UNSET)

        slack_user_id = d.pop("slack_user_id", UNSET)

        block_execution = d.pop("block_execution", UNSET)

        force_password_reset = d.pop("force_password_reset", UNSET)

        _prefetch = d.pop("prefetch", UNSET)
        prefetch: Union[Unset, UserContactInfoPrefetch]
        if isinstance(_prefetch, Unset):
            prefetch = UNSET
        else:
            prefetch = UserContactInfoPrefetch.from_dict(_prefetch)

        user_contact_info = cls(
            id=id,
            user=user,
            title=title,
            phone_number=phone_number,
            cell_number=cell_number,
            twitter_username=twitter_username,
            github_username=github_username,
            slack_username=slack_username,
            slack_user_id=slack_user_id,
            block_execution=block_execution,
            force_password_reset=force_password_reset,
            prefetch=prefetch,
        )

        user_contact_info.additional_properties = d
        return user_contact_info

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

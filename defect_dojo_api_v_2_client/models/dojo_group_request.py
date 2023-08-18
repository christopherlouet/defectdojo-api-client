import json
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dojo_group_request_social_authentication_provider import DojoGroupRequestSocialAuthenticationProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="DojoGroupRequest")


@_attrs_define
class DojoGroupRequest:
    """
    Attributes:
        name (str):
        configuration_permissions (Union[Unset, List[Optional[int]]]):
        description (Union[Unset, None, str]):
        social_provider (Union[Unset, None, DojoGroupRequestSocialAuthenticationProvider]): Group imported from a social
            provider.

            * `AzureAD` - AzureAD
    """

    name: str
    configuration_permissions: Union[Unset, List[Optional[int]]] = UNSET
    description: Union[Unset, None, str] = UNSET
    social_provider: Union[Unset, None, DojoGroupRequestSocialAuthenticationProvider] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        configuration_permissions: Union[Unset, List[Optional[int]]] = UNSET
        if not isinstance(self.configuration_permissions, Unset):
            configuration_permissions = self.configuration_permissions

        description = self.description
        social_provider: Union[Unset, None, str] = UNSET
        if not isinstance(self.social_provider, Unset):
            social_provider = self.social_provider.value if self.social_provider else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if configuration_permissions is not UNSET:
            field_dict["configuration_permissions"] = configuration_permissions
        if description is not UNSET:
            field_dict["description"] = description
        if social_provider is not UNSET:
            field_dict["social_provider"] = social_provider

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        configuration_permissions: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.configuration_permissions, Unset):
            _temp_configuration_permissions = self.configuration_permissions
            configuration_permissions = (None, json.dumps(_temp_configuration_permissions).encode(), "application/json")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        social_provider: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.social_provider, Unset):
            social_provider = (
                (None, str(self.social_provider.value).encode(), "text/plain") if self.social_provider else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "name": name,
            }
        )
        if configuration_permissions is not UNSET:
            field_dict["configuration_permissions"] = configuration_permissions
        if description is not UNSET:
            field_dict["description"] = description
        if social_provider is not UNSET:
            field_dict["social_provider"] = social_provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        configuration_permissions = cast(List[Optional[int]], d.pop("configuration_permissions", UNSET))

        description = d.pop("description", UNSET)

        _social_provider = d.pop("social_provider", UNSET)
        social_provider: Union[Unset, None, DojoGroupRequestSocialAuthenticationProvider]
        if _social_provider is None:
            social_provider = None
        elif isinstance(_social_provider, Unset):
            social_provider = UNSET
        else:
            social_provider = DojoGroupRequestSocialAuthenticationProvider(_social_provider)

        dojo_group_request = cls(
            name=name,
            configuration_permissions=configuration_permissions,
            description=description,
            social_provider=social_provider,
        )

        dojo_group_request.additional_properties = d
        return dojo_group_request

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

from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EngagementCheckList")


@_attrs_define
class EngagementCheckList:
    """
    Attributes:
        id (int):
        engagement (int):
        session_management (Union[Unset, str]):
        encryption_crypto (Union[Unset, str]):
        configuration_management (Union[Unset, str]):
        authentication (Union[Unset, str]):
        authorization_and_access_control (Union[Unset, str]):
        data_input_sanitization_validation (Union[Unset, str]):
        sensitive_data (Union[Unset, str]):
        other (Union[Unset, str]):
        session_issues (Union[Unset, List[int]]):
        crypto_issues (Union[Unset, List[int]]):
        config_issues (Union[Unset, List[int]]):
        auth_issues (Union[Unset, List[int]]):
        author_issues (Union[Unset, List[int]]):
        data_issues (Union[Unset, List[int]]):
        sensitive_issues (Union[Unset, List[int]]):
        other_issues (Union[Unset, List[int]]):
    """

    id: int
    engagement: int
    session_management: Union[Unset, str] = UNSET
    encryption_crypto: Union[Unset, str] = UNSET
    configuration_management: Union[Unset, str] = UNSET
    authentication: Union[Unset, str] = UNSET
    authorization_and_access_control: Union[Unset, str] = UNSET
    data_input_sanitization_validation: Union[Unset, str] = UNSET
    sensitive_data: Union[Unset, str] = UNSET
    other: Union[Unset, str] = UNSET
    session_issues: Union[Unset, List[int]] = UNSET
    crypto_issues: Union[Unset, List[int]] = UNSET
    config_issues: Union[Unset, List[int]] = UNSET
    auth_issues: Union[Unset, List[int]] = UNSET
    author_issues: Union[Unset, List[int]] = UNSET
    data_issues: Union[Unset, List[int]] = UNSET
    sensitive_issues: Union[Unset, List[int]] = UNSET
    other_issues: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        engagement = self.engagement
        session_management = self.session_management
        encryption_crypto = self.encryption_crypto
        configuration_management = self.configuration_management
        authentication = self.authentication
        authorization_and_access_control = self.authorization_and_access_control
        data_input_sanitization_validation = self.data_input_sanitization_validation
        sensitive_data = self.sensitive_data
        other = self.other
        session_issues: Union[Unset, List[int]] = UNSET
        if not isinstance(self.session_issues, Unset):
            session_issues = self.session_issues

        crypto_issues: Union[Unset, List[int]] = UNSET
        if not isinstance(self.crypto_issues, Unset):
            crypto_issues = self.crypto_issues

        config_issues: Union[Unset, List[int]] = UNSET
        if not isinstance(self.config_issues, Unset):
            config_issues = self.config_issues

        auth_issues: Union[Unset, List[int]] = UNSET
        if not isinstance(self.auth_issues, Unset):
            auth_issues = self.auth_issues

        author_issues: Union[Unset, List[int]] = UNSET
        if not isinstance(self.author_issues, Unset):
            author_issues = self.author_issues

        data_issues: Union[Unset, List[int]] = UNSET
        if not isinstance(self.data_issues, Unset):
            data_issues = self.data_issues

        sensitive_issues: Union[Unset, List[int]] = UNSET
        if not isinstance(self.sensitive_issues, Unset):
            sensitive_issues = self.sensitive_issues

        other_issues: Union[Unset, List[int]] = UNSET
        if not isinstance(self.other_issues, Unset):
            other_issues = self.other_issues

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "engagement": engagement,
            }
        )
        if session_management is not UNSET:
            field_dict["session_management"] = session_management
        if encryption_crypto is not UNSET:
            field_dict["encryption_crypto"] = encryption_crypto
        if configuration_management is not UNSET:
            field_dict["configuration_management"] = configuration_management
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if authorization_and_access_control is not UNSET:
            field_dict["authorization_and_access_control"] = authorization_and_access_control
        if data_input_sanitization_validation is not UNSET:
            field_dict["data_input_sanitization_validation"] = data_input_sanitization_validation
        if sensitive_data is not UNSET:
            field_dict["sensitive_data"] = sensitive_data
        if other is not UNSET:
            field_dict["other"] = other
        if session_issues is not UNSET:
            field_dict["session_issues"] = session_issues
        if crypto_issues is not UNSET:
            field_dict["crypto_issues"] = crypto_issues
        if config_issues is not UNSET:
            field_dict["config_issues"] = config_issues
        if auth_issues is not UNSET:
            field_dict["auth_issues"] = auth_issues
        if author_issues is not UNSET:
            field_dict["author_issues"] = author_issues
        if data_issues is not UNSET:
            field_dict["data_issues"] = data_issues
        if sensitive_issues is not UNSET:
            field_dict["sensitive_issues"] = sensitive_issues
        if other_issues is not UNSET:
            field_dict["other_issues"] = other_issues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        engagement = d.pop("engagement")

        session_management = d.pop("session_management", UNSET)

        encryption_crypto = d.pop("encryption_crypto", UNSET)

        configuration_management = d.pop("configuration_management", UNSET)

        authentication = d.pop("authentication", UNSET)

        authorization_and_access_control = d.pop("authorization_and_access_control", UNSET)

        data_input_sanitization_validation = d.pop("data_input_sanitization_validation", UNSET)

        sensitive_data = d.pop("sensitive_data", UNSET)

        other = d.pop("other", UNSET)

        session_issues = cast(List[int], d.pop("session_issues", UNSET))

        crypto_issues = cast(List[int], d.pop("crypto_issues", UNSET))

        config_issues = cast(List[int], d.pop("config_issues", UNSET))

        auth_issues = cast(List[int], d.pop("auth_issues", UNSET))

        author_issues = cast(List[int], d.pop("author_issues", UNSET))

        data_issues = cast(List[int], d.pop("data_issues", UNSET))

        sensitive_issues = cast(List[int], d.pop("sensitive_issues", UNSET))

        other_issues = cast(List[int], d.pop("other_issues", UNSET))

        engagement_check_list = cls(
            id=id,
            engagement=engagement,
            session_management=session_management,
            encryption_crypto=encryption_crypto,
            configuration_management=configuration_management,
            authentication=authentication,
            authorization_and_access_control=authorization_and_access_control,
            data_input_sanitization_validation=data_input_sanitization_validation,
            sensitive_data=sensitive_data,
            other=other,
            session_issues=session_issues,
            crypto_issues=crypto_issues,
            config_issues=config_issues,
            auth_issues=auth_issues,
            author_issues=author_issues,
            data_issues=data_issues,
            sensitive_issues=sensitive_issues,
            other_issues=other_issues,
        )

        engagement_check_list.additional_properties = d
        return engagement_check_list

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

from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credential_authentication import CredentialAuthentication
from ..models.credential_http_authentication import CredentialHttpAuthentication
from ..types import UNSET, Unset

T = TypeVar("T", bound="Credential")


@_attrs_define
class Credential:
    """
    Attributes:
        id (int):
        name (str):
        username (str):
        role (str):
        url (str):
        environment (int):
        notes (List[int]):
        authentication (Union[Unset, CredentialAuthentication]): * `Form` - Form Authentication
            * `SSO` - SSO Redirect
        http_authentication (Union[Unset, None, CredentialHttpAuthentication]): * `Basic` - Basic
            * `NTLM` - NTLM
        description (Union[Unset, None, str]):
        login_regex (Union[Unset, None, str]):
        logout_regex (Union[Unset, None, str]):
        is_valid (Union[Unset, bool]):
    """

    id: int
    name: str
    username: str
    role: str
    url: str
    environment: int
    notes: List[int]
    authentication: Union[Unset, CredentialAuthentication] = UNSET
    http_authentication: Union[Unset, None, CredentialHttpAuthentication] = UNSET
    description: Union[Unset, None, str] = UNSET
    login_regex: Union[Unset, None, str] = UNSET
    logout_regex: Union[Unset, None, str] = UNSET
    is_valid: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        username = self.username
        role = self.role
        url = self.url
        environment = self.environment
        notes = self.notes

        authentication: Union[Unset, str] = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = self.authentication.value

        http_authentication: Union[Unset, None, str] = UNSET
        if not isinstance(self.http_authentication, Unset):
            http_authentication = self.http_authentication.value if self.http_authentication else None

        description = self.description
        login_regex = self.login_regex
        logout_regex = self.logout_regex
        is_valid = self.is_valid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "username": username,
                "role": role,
                "url": url,
                "environment": environment,
                "notes": notes,
            }
        )
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if http_authentication is not UNSET:
            field_dict["http_authentication"] = http_authentication
        if description is not UNSET:
            field_dict["description"] = description
        if login_regex is not UNSET:
            field_dict["login_regex"] = login_regex
        if logout_regex is not UNSET:
            field_dict["logout_regex"] = logout_regex
        if is_valid is not UNSET:
            field_dict["is_valid"] = is_valid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        username = d.pop("username")

        role = d.pop("role")

        url = d.pop("url")

        environment = d.pop("environment")

        notes = cast(List[int], d.pop("notes"))

        _authentication = d.pop("authentication", UNSET)
        authentication: Union[Unset, CredentialAuthentication]
        if isinstance(_authentication, Unset):
            authentication = UNSET
        else:
            authentication = CredentialAuthentication(_authentication)

        _http_authentication = d.pop("http_authentication", UNSET)
        http_authentication: Union[Unset, None, CredentialHttpAuthentication]
        if _http_authentication is None:
            http_authentication = None
        elif isinstance(_http_authentication, Unset):
            http_authentication = UNSET
        else:
            http_authentication = CredentialHttpAuthentication(_http_authentication)

        description = d.pop("description", UNSET)

        login_regex = d.pop("login_regex", UNSET)

        logout_regex = d.pop("logout_regex", UNSET)

        is_valid = d.pop("is_valid", UNSET)

        credential = cls(
            id=id,
            name=name,
            username=username,
            role=role,
            url=url,
            environment=environment,
            notes=notes,
            authentication=authentication,
            http_authentication=http_authentication,
            description=description,
            login_regex=login_regex,
            logout_regex=logout_regex,
            is_valid=is_valid,
        )

        credential.additional_properties = d
        return credential

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

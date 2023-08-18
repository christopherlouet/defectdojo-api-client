from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credential_request_authentication import CredentialRequestAuthentication
from ..models.credential_request_http_authentication import CredentialRequestHttpAuthentication
from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialRequest")


@_attrs_define
class CredentialRequest:
    """
    Attributes:
        name (str):
        username (str):
        role (str):
        url (str):
        environment (int):
        authentication (Union[Unset, CredentialRequestAuthentication]): * `Form` - Form Authentication
            * `SSO` - SSO Redirect
        http_authentication (Union[Unset, None, CredentialRequestHttpAuthentication]): * `Basic` - Basic
            * `NTLM` - NTLM
        description (Union[Unset, None, str]):
        login_regex (Union[Unset, None, str]):
        logout_regex (Union[Unset, None, str]):
        is_valid (Union[Unset, bool]):
    """

    name: str
    username: str
    role: str
    url: str
    environment: int
    authentication: Union[Unset, CredentialRequestAuthentication] = UNSET
    http_authentication: Union[Unset, None, CredentialRequestHttpAuthentication] = UNSET
    description: Union[Unset, None, str] = UNSET
    login_regex: Union[Unset, None, str] = UNSET
    logout_regex: Union[Unset, None, str] = UNSET
    is_valid: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        username = self.username
        role = self.role
        url = self.url
        environment = self.environment
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
                "name": name,
                "username": username,
                "role": role,
                "url": url,
                "environment": environment,
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

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        username = (
            self.username if isinstance(self.username, Unset) else (None, str(self.username).encode(), "text/plain")
        )
        role = self.role if isinstance(self.role, Unset) else (None, str(self.role).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        environment = (
            self.environment
            if isinstance(self.environment, Unset)
            else (None, str(self.environment).encode(), "text/plain")
        )
        authentication: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = (None, str(self.authentication.value).encode(), "text/plain")

        http_authentication: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.http_authentication, Unset):
            http_authentication = (
                (None, str(self.http_authentication.value).encode(), "text/plain") if self.http_authentication else None
            )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        login_regex = (
            self.login_regex
            if isinstance(self.login_regex, Unset)
            else (None, str(self.login_regex).encode(), "text/plain")
        )
        logout_regex = (
            self.logout_regex
            if isinstance(self.logout_regex, Unset)
            else (None, str(self.logout_regex).encode(), "text/plain")
        )
        is_valid = (
            self.is_valid if isinstance(self.is_valid, Unset) else (None, str(self.is_valid).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "name": name,
                "username": username,
                "role": role,
                "url": url,
                "environment": environment,
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
        name = d.pop("name")

        username = d.pop("username")

        role = d.pop("role")

        url = d.pop("url")

        environment = d.pop("environment")

        _authentication = d.pop("authentication", UNSET)
        authentication: Union[Unset, CredentialRequestAuthentication]
        if isinstance(_authentication, Unset):
            authentication = UNSET
        else:
            authentication = CredentialRequestAuthentication(_authentication)

        _http_authentication = d.pop("http_authentication", UNSET)
        http_authentication: Union[Unset, None, CredentialRequestHttpAuthentication]
        if _http_authentication is None:
            http_authentication = None
        elif isinstance(_http_authentication, Unset):
            http_authentication = UNSET
        else:
            http_authentication = CredentialRequestHttpAuthentication(_http_authentication)

        description = d.pop("description", UNSET)

        login_regex = d.pop("login_regex", UNSET)

        logout_regex = d.pop("logout_regex", UNSET)

        is_valid = d.pop("is_valid", UNSET)

        credential_request = cls(
            name=name,
            username=username,
            role=role,
            url=url,
            environment=environment,
            authentication=authentication,
            http_authentication=http_authentication,
            description=description,
            login_regex=login_regex,
            logout_regex=logout_regex,
            is_valid=is_valid,
        )

        credential_request.additional_properties = d
        return credential_request

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

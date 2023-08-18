from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialMappingRequest")


@_attrs_define
class CredentialMappingRequest:
    """
    Attributes:
        cred_id (int):
        is_authn_provider (Union[Unset, bool]):
        url (Union[Unset, None, str]):
        product (Union[Unset, None, int]):
        finding (Union[Unset, None, int]):
        engagement (Union[Unset, None, int]):
        test (Union[Unset, None, int]):
    """

    cred_id: int
    is_authn_provider: Union[Unset, bool] = UNSET
    url: Union[Unset, None, str] = UNSET
    product: Union[Unset, None, int] = UNSET
    finding: Union[Unset, None, int] = UNSET
    engagement: Union[Unset, None, int] = UNSET
    test: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cred_id = self.cred_id
        is_authn_provider = self.is_authn_provider
        url = self.url
        product = self.product
        finding = self.finding
        engagement = self.engagement
        test = self.test

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cred_id": cred_id,
            }
        )
        if is_authn_provider is not UNSET:
            field_dict["is_authn_provider"] = is_authn_provider
        if url is not UNSET:
            field_dict["url"] = url
        if product is not UNSET:
            field_dict["product"] = product
        if finding is not UNSET:
            field_dict["finding"] = finding
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if test is not UNSET:
            field_dict["test"] = test

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        cred_id = self.cred_id if isinstance(self.cred_id, Unset) else (None, str(self.cred_id).encode(), "text/plain")
        is_authn_provider = (
            self.is_authn_provider
            if isinstance(self.is_authn_provider, Unset)
            else (None, str(self.is_authn_provider).encode(), "text/plain")
        )
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        product = self.product if isinstance(self.product, Unset) else (None, str(self.product).encode(), "text/plain")
        finding = self.finding if isinstance(self.finding, Unset) else (None, str(self.finding).encode(), "text/plain")
        engagement = (
            self.engagement
            if isinstance(self.engagement, Unset)
            else (None, str(self.engagement).encode(), "text/plain")
        )
        test = self.test if isinstance(self.test, Unset) else (None, str(self.test).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "cred_id": cred_id,
            }
        )
        if is_authn_provider is not UNSET:
            field_dict["is_authn_provider"] = is_authn_provider
        if url is not UNSET:
            field_dict["url"] = url
        if product is not UNSET:
            field_dict["product"] = product
        if finding is not UNSET:
            field_dict["finding"] = finding
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if test is not UNSET:
            field_dict["test"] = test

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cred_id = d.pop("cred_id")

        is_authn_provider = d.pop("is_authn_provider", UNSET)

        url = d.pop("url", UNSET)

        product = d.pop("product", UNSET)

        finding = d.pop("finding", UNSET)

        engagement = d.pop("engagement", UNSET)

        test = d.pop("test", UNSET)

        credential_mapping_request = cls(
            cred_id=cred_id,
            is_authn_provider=is_authn_provider,
            url=url,
            product=product,
            finding=finding,
            engagement=engagement,
            test=test,
        )

        credential_mapping_request.additional_properties = d
        return credential_mapping_request

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

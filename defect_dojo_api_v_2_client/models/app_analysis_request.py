import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAnalysisRequest")


@_attrs_define
class AppAnalysisRequest:
    """
    Attributes:
        name (str):
        product (int):
        user (int):
        tags (Union[Unset, List[str]]):
        confidence (Union[Unset, None, int]):
        version (Union[Unset, None, str]):
        icon (Union[Unset, None, str]):
        website (Union[Unset, None, str]):
        website_found (Union[Unset, None, str]):
    """

    name: str
    product: int
    user: int
    tags: Union[Unset, List[str]] = UNSET
    confidence: Union[Unset, None, int] = UNSET
    version: Union[Unset, None, str] = UNSET
    icon: Union[Unset, None, str] = UNSET
    website: Union[Unset, None, str] = UNSET
    website_found: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        product = self.product
        user = self.user
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        confidence = self.confidence
        version = self.version
        icon = self.icon
        website = self.website
        website_found = self.website_found

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "product": product,
                "user": user,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if version is not UNSET:
            field_dict["version"] = version
        if icon is not UNSET:
            field_dict["icon"] = icon
        if website is not UNSET:
            field_dict["website"] = website
        if website_found is not UNSET:
            field_dict["website_found"] = website_found

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        product = self.product if isinstance(self.product, Unset) else (None, str(self.product).encode(), "text/plain")
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        tags: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = self.tags
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        confidence = (
            self.confidence
            if isinstance(self.confidence, Unset)
            else (None, str(self.confidence).encode(), "text/plain")
        )
        version = self.version if isinstance(self.version, Unset) else (None, str(self.version).encode(), "text/plain")
        icon = self.icon if isinstance(self.icon, Unset) else (None, str(self.icon).encode(), "text/plain")
        website = self.website if isinstance(self.website, Unset) else (None, str(self.website).encode(), "text/plain")
        website_found = (
            self.website_found
            if isinstance(self.website_found, Unset)
            else (None, str(self.website_found).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "name": name,
                "product": product,
                "user": user,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if version is not UNSET:
            field_dict["version"] = version
        if icon is not UNSET:
            field_dict["icon"] = icon
        if website is not UNSET:
            field_dict["website"] = website
        if website_found is not UNSET:
            field_dict["website_found"] = website_found

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        product = d.pop("product")

        user = d.pop("user")

        tags = cast(List[str], d.pop("tags", UNSET))

        confidence = d.pop("confidence", UNSET)

        version = d.pop("version", UNSET)

        icon = d.pop("icon", UNSET)

        website = d.pop("website", UNSET)

        website_found = d.pop("website_found", UNSET)

        app_analysis_request = cls(
            name=name,
            product=product,
            user=user,
            tags=tags,
            confidence=confidence,
            version=version,
            icon=icon,
            website=website,
            website_found=website_found,
        )

        app_analysis_request.additional_properties = d
        return app_analysis_request

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

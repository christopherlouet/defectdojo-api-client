import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAnalysis")


@_attrs_define
class AppAnalysis:
    """
    Attributes:
        id (int):
        name (str):
        created (datetime.datetime):
        product (int):
        user (int):
        tags (Union[Unset, List[str]]):
        confidence (Union[Unset, None, int]):
        version (Union[Unset, None, str]):
        icon (Union[Unset, None, str]):
        website (Union[Unset, None, str]):
        website_found (Union[Unset, None, str]):
    """

    id: int
    name: str
    created: datetime.datetime
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
        id = self.id
        name = self.name
        created = self.created.isoformat()

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
                "id": id,
                "name": name,
                "created": created,
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
        id = d.pop("id")

        name = d.pop("name")

        created = isoparse(d.pop("created"))

        product = d.pop("product")

        user = d.pop("user")

        tags = cast(List[str], d.pop("tags", UNSET))

        confidence = d.pop("confidence", UNSET)

        version = d.pop("version", UNSET)

        icon = d.pop("icon", UNSET)

        website = d.pop("website", UNSET)

        website_found = d.pop("website_found", UNSET)

        app_analysis = cls(
            id=id,
            name=name,
            created=created,
            product=product,
            user=user,
            tags=tags,
            confidence=confidence,
            version=version,
            icon=icon,
            website=website,
            website_found=website_found,
        )

        app_analysis.additional_properties = d
        return app_analysis

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

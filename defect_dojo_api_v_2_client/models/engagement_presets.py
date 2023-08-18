import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EngagementPresets")


@_attrs_define
class EngagementPresets:
    """
    Attributes:
        id (int):
        created (datetime.datetime):
        product (int):
        title (Union[Unset, str]): Brief description of preset.
        notes (Union[Unset, None, str]): Description of what needs to be tested or setting up environment for testing
        scope (Union[Unset, str]): Scope of Engagement testing, IP's/Resources/URL's)
        test_type (Union[Unset, List[int]]):
        network_locations (Union[Unset, List[int]]):
    """

    id: int
    created: datetime.datetime
    product: int
    title: Union[Unset, str] = UNSET
    notes: Union[Unset, None, str] = UNSET
    scope: Union[Unset, str] = UNSET
    test_type: Union[Unset, List[int]] = UNSET
    network_locations: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created = self.created.isoformat()

        product = self.product
        title = self.title
        notes = self.notes
        scope = self.scope
        test_type: Union[Unset, List[int]] = UNSET
        if not isinstance(self.test_type, Unset):
            test_type = self.test_type

        network_locations: Union[Unset, List[int]] = UNSET
        if not isinstance(self.network_locations, Unset):
            network_locations = self.network_locations

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "product": product,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if notes is not UNSET:
            field_dict["notes"] = notes
        if scope is not UNSET:
            field_dict["scope"] = scope
        if test_type is not UNSET:
            field_dict["test_type"] = test_type
        if network_locations is not UNSET:
            field_dict["network_locations"] = network_locations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        created = isoparse(d.pop("created"))

        product = d.pop("product")

        title = d.pop("title", UNSET)

        notes = d.pop("notes", UNSET)

        scope = d.pop("scope", UNSET)

        test_type = cast(List[int], d.pop("test_type", UNSET))

        network_locations = cast(List[int], d.pop("network_locations", UNSET))

        engagement_presets = cls(
            id=id,
            created=created,
            product=product,
            title=title,
            notes=notes,
            scope=scope,
            test_type=test_type,
            network_locations=network_locations,
        )

        engagement_presets.additional_properties = d
        return engagement_presets

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

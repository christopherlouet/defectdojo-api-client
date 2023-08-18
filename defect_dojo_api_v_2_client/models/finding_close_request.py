import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindingCloseRequest")


@_attrs_define
class FindingCloseRequest:
    """
    Attributes:
        is_mitigated (Union[Unset, bool]):
        mitigated (Union[Unset, datetime.datetime]):
        false_p (Union[Unset, bool]):
        out_of_scope (Union[Unset, bool]):
        duplicate (Union[Unset, bool]):
    """

    is_mitigated: Union[Unset, bool] = UNSET
    mitigated: Union[Unset, datetime.datetime] = UNSET
    false_p: Union[Unset, bool] = UNSET
    out_of_scope: Union[Unset, bool] = UNSET
    duplicate: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_mitigated = self.is_mitigated
        mitigated: Union[Unset, str] = UNSET
        if not isinstance(self.mitigated, Unset):
            mitigated = self.mitigated.isoformat()

        false_p = self.false_p
        out_of_scope = self.out_of_scope
        duplicate = self.duplicate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_mitigated is not UNSET:
            field_dict["is_mitigated"] = is_mitigated
        if mitigated is not UNSET:
            field_dict["mitigated"] = mitigated
        if false_p is not UNSET:
            field_dict["false_p"] = false_p
        if out_of_scope is not UNSET:
            field_dict["out_of_scope"] = out_of_scope
        if duplicate is not UNSET:
            field_dict["duplicate"] = duplicate

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        is_mitigated = (
            self.is_mitigated
            if isinstance(self.is_mitigated, Unset)
            else (None, str(self.is_mitigated).encode(), "text/plain")
        )
        mitigated: Union[Unset, bytes] = UNSET
        if not isinstance(self.mitigated, Unset):
            mitigated = self.mitigated.isoformat().encode()

        false_p = self.false_p if isinstance(self.false_p, Unset) else (None, str(self.false_p).encode(), "text/plain")
        out_of_scope = (
            self.out_of_scope
            if isinstance(self.out_of_scope, Unset)
            else (None, str(self.out_of_scope).encode(), "text/plain")
        )
        duplicate = (
            self.duplicate if isinstance(self.duplicate, Unset) else (None, str(self.duplicate).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if is_mitigated is not UNSET:
            field_dict["is_mitigated"] = is_mitigated
        if mitigated is not UNSET:
            field_dict["mitigated"] = mitigated
        if false_p is not UNSET:
            field_dict["false_p"] = false_p
        if out_of_scope is not UNSET:
            field_dict["out_of_scope"] = out_of_scope
        if duplicate is not UNSET:
            field_dict["duplicate"] = duplicate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_mitigated = d.pop("is_mitigated", UNSET)

        _mitigated = d.pop("mitigated", UNSET)
        mitigated: Union[Unset, datetime.datetime]
        if isinstance(_mitigated, Unset):
            mitigated = UNSET
        else:
            mitigated = isoparse(_mitigated)

        false_p = d.pop("false_p", UNSET)

        out_of_scope = d.pop("out_of_scope", UNSET)

        duplicate = d.pop("duplicate", UNSET)

        finding_close_request = cls(
            is_mitigated=is_mitigated,
            mitigated=mitigated,
            false_p=false_p,
            out_of_scope=out_of_scope,
            duplicate=duplicate,
        )

        finding_close_request.additional_properties = d
        return finding_close_request

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

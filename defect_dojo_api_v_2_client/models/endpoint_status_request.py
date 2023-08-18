import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointStatusRequest")


@_attrs_define
class EndpointStatusRequest:
    """
    Attributes:
        endpoint (int):
        finding (int):
        date (Union[Unset, datetime.date]):
        mitigated (Union[Unset, bool]):
        false_positive (Union[Unset, bool]):
        out_of_scope (Union[Unset, bool]):
        risk_accepted (Union[Unset, bool]):
        mitigated_by (Union[Unset, None, int]):
    """

    endpoint: int
    finding: int
    date: Union[Unset, datetime.date] = UNSET
    mitigated: Union[Unset, bool] = UNSET
    false_positive: Union[Unset, bool] = UNSET
    out_of_scope: Union[Unset, bool] = UNSET
    risk_accepted: Union[Unset, bool] = UNSET
    mitigated_by: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint = self.endpoint
        finding = self.finding
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        mitigated = self.mitigated
        false_positive = self.false_positive
        out_of_scope = self.out_of_scope
        risk_accepted = self.risk_accepted
        mitigated_by = self.mitigated_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "finding": finding,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if mitigated is not UNSET:
            field_dict["mitigated"] = mitigated
        if false_positive is not UNSET:
            field_dict["false_positive"] = false_positive
        if out_of_scope is not UNSET:
            field_dict["out_of_scope"] = out_of_scope
        if risk_accepted is not UNSET:
            field_dict["risk_accepted"] = risk_accepted
        if mitigated_by is not UNSET:
            field_dict["mitigated_by"] = mitigated_by

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        endpoint = (
            self.endpoint if isinstance(self.endpoint, Unset) else (None, str(self.endpoint).encode(), "text/plain")
        )
        finding = self.finding if isinstance(self.finding, Unset) else (None, str(self.finding).encode(), "text/plain")
        date: Union[Unset, bytes] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat().encode()

        mitigated = (
            self.mitigated if isinstance(self.mitigated, Unset) else (None, str(self.mitigated).encode(), "text/plain")
        )
        false_positive = (
            self.false_positive
            if isinstance(self.false_positive, Unset)
            else (None, str(self.false_positive).encode(), "text/plain")
        )
        out_of_scope = (
            self.out_of_scope
            if isinstance(self.out_of_scope, Unset)
            else (None, str(self.out_of_scope).encode(), "text/plain")
        )
        risk_accepted = (
            self.risk_accepted
            if isinstance(self.risk_accepted, Unset)
            else (None, str(self.risk_accepted).encode(), "text/plain")
        )
        mitigated_by = (
            self.mitigated_by
            if isinstance(self.mitigated_by, Unset)
            else (None, str(self.mitigated_by).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "endpoint": endpoint,
                "finding": finding,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if mitigated is not UNSET:
            field_dict["mitigated"] = mitigated
        if false_positive is not UNSET:
            field_dict["false_positive"] = false_positive
        if out_of_scope is not UNSET:
            field_dict["out_of_scope"] = out_of_scope
        if risk_accepted is not UNSET:
            field_dict["risk_accepted"] = risk_accepted
        if mitigated_by is not UNSET:
            field_dict["mitigated_by"] = mitigated_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        endpoint = d.pop("endpoint")

        finding = d.pop("finding")

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        mitigated = d.pop("mitigated", UNSET)

        false_positive = d.pop("false_positive", UNSET)

        out_of_scope = d.pop("out_of_scope", UNSET)

        risk_accepted = d.pop("risk_accepted", UNSET)

        mitigated_by = d.pop("mitigated_by", UNSET)

        endpoint_status_request = cls(
            endpoint=endpoint,
            finding=finding,
            date=date,
            mitigated=mitigated,
            false_positive=false_positive,
            out_of_scope=out_of_scope,
            risk_accepted=risk_accepted,
            mitigated_by=mitigated_by,
        )

        endpoint_status_request.additional_properties = d
        return endpoint_status_request

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

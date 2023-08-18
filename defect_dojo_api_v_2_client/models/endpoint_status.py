import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointStatus")


@_attrs_define
class EndpointStatus:
    """
    Attributes:
        id (int):
        endpoint (int):
        finding (int):
        date (Union[Unset, datetime.date]):
        last_modified (Optional[datetime.datetime]):
        mitigated (Union[Unset, bool]):
        mitigated_time (Optional[datetime.datetime]):
        false_positive (Union[Unset, bool]):
        out_of_scope (Union[Unset, bool]):
        risk_accepted (Union[Unset, bool]):
        mitigated_by (Union[Unset, None, int]):
    """

    id: int
    endpoint: int
    finding: int
    last_modified: Optional[datetime.datetime]
    mitigated_time: Optional[datetime.datetime]
    date: Union[Unset, datetime.date] = UNSET
    mitigated: Union[Unset, bool] = UNSET
    false_positive: Union[Unset, bool] = UNSET
    out_of_scope: Union[Unset, bool] = UNSET
    risk_accepted: Union[Unset, bool] = UNSET
    mitigated_by: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        endpoint = self.endpoint
        finding = self.finding
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        last_modified = self.last_modified.isoformat() if self.last_modified else None

        mitigated = self.mitigated
        mitigated_time = self.mitigated_time.isoformat() if self.mitigated_time else None

        false_positive = self.false_positive
        out_of_scope = self.out_of_scope
        risk_accepted = self.risk_accepted
        mitigated_by = self.mitigated_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "endpoint": endpoint,
                "finding": finding,
                "last_modified": last_modified,
                "mitigated_time": mitigated_time,
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
        id = d.pop("id")

        endpoint = d.pop("endpoint")

        finding = d.pop("finding")

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        _last_modified = d.pop("last_modified")
        last_modified: Optional[datetime.datetime]
        if _last_modified is None:
            last_modified = None
        else:
            last_modified = isoparse(_last_modified)

        mitigated = d.pop("mitigated", UNSET)

        _mitigated_time = d.pop("mitigated_time")
        mitigated_time: Optional[datetime.datetime]
        if _mitigated_time is None:
            mitigated_time = None
        else:
            mitigated_time = isoparse(_mitigated_time)

        false_positive = d.pop("false_positive", UNSET)

        out_of_scope = d.pop("out_of_scope", UNSET)

        risk_accepted = d.pop("risk_accepted", UNSET)

        mitigated_by = d.pop("mitigated_by", UNSET)

        endpoint_status = cls(
            id=id,
            endpoint=endpoint,
            finding=finding,
            date=date,
            last_modified=last_modified,
            mitigated=mitigated,
            mitigated_time=mitigated_time,
            false_positive=false_positive,
            out_of_scope=out_of_scope,
            risk_accepted=risk_accepted,
            mitigated_by=mitigated_by,
        )

        endpoint_status.additional_properties = d
        return endpoint_status

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

from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AcceptedRiskRequest")


@_attrs_define
class AcceptedRiskRequest:
    """
    Attributes:
        vulnerability_id (str): An id of a vulnerability in a security advisory associated with this finding. Can be a
            Common Vulnerabilities and Exposure (CVE) or from other sources.
        justification (str): Justification for accepting findings with this vulnerability id
        accepted_by (str): Name or email of person who accepts the risk
    """

    vulnerability_id: str
    justification: str
    accepted_by: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vulnerability_id = self.vulnerability_id
        justification = self.justification
        accepted_by = self.accepted_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vulnerability_id": vulnerability_id,
                "justification": justification,
                "accepted_by": accepted_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vulnerability_id = d.pop("vulnerability_id")

        justification = d.pop("justification")

        accepted_by = d.pop("accepted_by")

        accepted_risk_request = cls(
            vulnerability_id=vulnerability_id,
            justification=justification,
            accepted_by=accepted_by,
        )

        accepted_risk_request.additional_properties = d
        return accepted_risk_request

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

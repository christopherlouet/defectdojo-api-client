from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.burp_raw_request_response_req_resp_item import BurpRawRequestResponseReqRespItem


T = TypeVar("T", bound="BurpRawRequestResponse")


@_attrs_define
class BurpRawRequestResponse:
    """
    Attributes:
        req_resp (List['BurpRawRequestResponseReqRespItem']):
    """

    req_resp: List["BurpRawRequestResponseReqRespItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        req_resp = []
        for req_resp_item_data in self.req_resp:
            req_resp_item = req_resp_item_data.to_dict()

            req_resp.append(req_resp_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "req_resp": req_resp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.burp_raw_request_response_req_resp_item import BurpRawRequestResponseReqRespItem

        d = src_dict.copy()
        req_resp = []
        _req_resp = d.pop("req_resp")
        for req_resp_item_data in _req_resp:
            req_resp_item = BurpRawRequestResponseReqRespItem.from_dict(req_resp_item_data)

            req_resp.append(req_resp_item)

        burp_raw_request_response = cls(
            req_resp=req_resp,
        )

        burp_raw_request_response.additional_properties = d
        return burp_raw_request_response

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

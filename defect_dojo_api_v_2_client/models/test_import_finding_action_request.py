from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.test_import_finding_action_request_action import TestImportFindingActionRequestAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestImportFindingActionRequest")


@_attrs_define
class TestImportFindingActionRequest:
    """
    Attributes:
        action (Union[Unset, None, TestImportFindingActionRequestAction]): * `N` - created
            * `C` - closed
            * `R` - reactivated
            * `U` - left untouched
    """

    action: Union[Unset, None, TestImportFindingActionRequestAction] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action: Union[Unset, None, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value if self.action else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _action = d.pop("action", UNSET)
        action: Union[Unset, None, TestImportFindingActionRequestAction]
        if _action is None:
            action = None
        elif isinstance(_action, Unset):
            action = UNSET
        else:
            action = TestImportFindingActionRequestAction(_action)

        test_import_finding_action_request = cls(
            action=action,
        )

        test_import_finding_action_request.additional_properties = d
        return test_import_finding_action_request

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

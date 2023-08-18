import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.test_import_finding_action_action import TestImportFindingActionAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestImportFindingAction")


@_attrs_define
class TestImportFindingAction:
    """
    Attributes:
        id (int):
        created (datetime.datetime):
        modified (datetime.datetime):
        test_import (int):
        finding (int):
        action (Union[Unset, None, TestImportFindingActionAction]): * `N` - created
            * `C` - closed
            * `R` - reactivated
            * `U` - left untouched
    """

    id: int
    created: datetime.datetime
    modified: datetime.datetime
    test_import: int
    finding: int
    action: Union[Unset, None, TestImportFindingActionAction] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created = self.created.isoformat()

        modified = self.modified.isoformat()

        test_import = self.test_import
        finding = self.finding
        action: Union[Unset, None, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value if self.action else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "modified": modified,
                "test_import": test_import,
                "finding": finding,
            }
        )
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        created = isoparse(d.pop("created"))

        modified = isoparse(d.pop("modified"))

        test_import = d.pop("test_import")

        finding = d.pop("finding")

        _action = d.pop("action", UNSET)
        action: Union[Unset, None, TestImportFindingActionAction]
        if _action is None:
            action = None
        elif isinstance(_action, Unset):
            action = UNSET
        else:
            action = TestImportFindingActionAction(_action)

        test_import_finding_action = cls(
            id=id,
            created=created,
            modified=modified,
            test_import=test_import,
            finding=finding,
            action=action,
        )

        test_import_finding_action.additional_properties = d
        return test_import_finding_action

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

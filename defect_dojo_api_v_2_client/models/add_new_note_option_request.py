from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddNewNoteOptionRequest")


@_attrs_define
class AddNewNoteOptionRequest:
    """
    Attributes:
        entry (str):
        private (Union[Unset, bool]):
        note_type (Union[Unset, None, int]):
    """

    entry: str
    private: Union[Unset, bool] = UNSET
    note_type: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry = self.entry
        private = self.private
        note_type = self.note_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry": entry,
            }
        )
        if private is not UNSET:
            field_dict["private"] = private
        if note_type is not UNSET:
            field_dict["note_type"] = note_type

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        entry = self.entry if isinstance(self.entry, Unset) else (None, str(self.entry).encode(), "text/plain")
        private = self.private if isinstance(self.private, Unset) else (None, str(self.private).encode(), "text/plain")
        note_type = (
            self.note_type if isinstance(self.note_type, Unset) else (None, str(self.note_type).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "entry": entry,
            }
        )
        if private is not UNSET:
            field_dict["private"] = private
        if note_type is not UNSET:
            field_dict["note_type"] = note_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entry = d.pop("entry")

        private = d.pop("private", UNSET)

        note_type = d.pop("note_type", UNSET)

        add_new_note_option_request = cls(
            entry=entry,
            private=private,
            note_type=note_type,
        )

        add_new_note_option_request.additional_properties = d
        return add_new_note_option_request

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

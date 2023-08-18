from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoteRequest")


@_attrs_define
class NoteRequest:
    """
    Attributes:
        entry (str):
        private (Union[Unset, bool]):
        edited (Union[Unset, bool]):
    """

    entry: str
    private: Union[Unset, bool] = UNSET
    edited: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry = self.entry
        private = self.private
        edited = self.edited

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry": entry,
            }
        )
        if private is not UNSET:
            field_dict["private"] = private
        if edited is not UNSET:
            field_dict["edited"] = edited

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        entry = self.entry if isinstance(self.entry, Unset) else (None, str(self.entry).encode(), "text/plain")
        private = self.private if isinstance(self.private, Unset) else (None, str(self.private).encode(), "text/plain")
        edited = self.edited if isinstance(self.edited, Unset) else (None, str(self.edited).encode(), "text/plain")

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
        if edited is not UNSET:
            field_dict["edited"] = edited

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entry = d.pop("entry")

        private = d.pop("private", UNSET)

        edited = d.pop("edited", UNSET)

        note_request = cls(
            entry=entry,
            private=private,
            edited=edited,
        )

        note_request.additional_properties = d
        return note_request

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

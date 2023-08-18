from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.note import Note


T = TypeVar("T", bound="EngagementToNotes")


@_attrs_define
class EngagementToNotes:
    """
    Attributes:
        notes (List['Note']):
        engagement_id (Optional[int]):
    """

    notes: List["Note"]
    engagement_id: Optional[int]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notes = []
        for notes_item_data in self.notes:
            notes_item = notes_item_data.to_dict()

            notes.append(notes_item)

        engagement_id = self.engagement_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notes": notes,
                "engagement_id": engagement_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.note import Note

        d = src_dict.copy()
        notes = []
        _notes = d.pop("notes")
        for notes_item_data in _notes:
            notes_item = Note.from_dict(notes_item_data)

            notes.append(notes_item)

        engagement_id = d.pop("engagement_id")

        engagement_to_notes = cls(
            notes=notes,
            engagement_id=engagement_id,
        )

        engagement_to_notes.additional_properties = d
        return engagement_to_notes

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

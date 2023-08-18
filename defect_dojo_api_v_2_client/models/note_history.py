import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.note_type import NoteType
    from ..models.user_stub import UserStub


T = TypeVar("T", bound="NoteHistory")


@_attrs_define
class NoteHistory:
    """
    Attributes:
        id (int):
        current_editor (UserStub):
        note_type (NoteType):
        data (str):
        time (Optional[datetime.datetime]):
    """

    id: int
    current_editor: "UserStub"
    note_type: "NoteType"
    data: str
    time: Optional[datetime.datetime]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        current_editor = self.current_editor.to_dict()

        note_type = self.note_type.to_dict()

        data = self.data
        time = self.time.isoformat() if self.time else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "current_editor": current_editor,
                "note_type": note_type,
                "data": data,
                "time": time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.note_type import NoteType
        from ..models.user_stub import UserStub

        d = src_dict.copy()
        id = d.pop("id")

        current_editor = UserStub.from_dict(d.pop("current_editor"))

        note_type = NoteType.from_dict(d.pop("note_type"))

        data = d.pop("data")

        _time = d.pop("time")
        time: Optional[datetime.datetime]
        if _time is None:
            time = None
        else:
            time = isoparse(_time)

        note_history = cls(
            id=id,
            current_editor=current_editor,
            note_type=note_type,
            data=data,
            time=time,
        )

        note_history.additional_properties = d
        return note_history

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

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note_history import NoteHistory
    from ..models.note_type import NoteType
    from ..models.user_stub import UserStub


T = TypeVar("T", bound="Note")


@_attrs_define
class Note:
    """
    Attributes:
        id (int):
        author (UserStub):
        history (List['NoteHistory']):
        note_type (NoteType):
        entry (str):
        date (datetime.datetime):
        editor (Optional[UserStub]):
        private (Union[Unset, bool]):
        edited (Union[Unset, bool]):
        edit_time (Optional[datetime.datetime]):
    """

    id: int
    author: "UserStub"
    history: List["NoteHistory"]
    note_type: "NoteType"
    entry: str
    date: datetime.datetime
    editor: Optional["UserStub"]
    edit_time: Optional[datetime.datetime]
    private: Union[Unset, bool] = UNSET
    edited: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        author = self.author.to_dict()

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()

            history.append(history_item)

        note_type = self.note_type.to_dict()

        entry = self.entry
        date = self.date.isoformat()

        editor = self.editor.to_dict() if self.editor else None

        private = self.private
        edited = self.edited
        edit_time = self.edit_time.isoformat() if self.edit_time else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "author": author,
                "history": history,
                "note_type": note_type,
                "entry": entry,
                "date": date,
                "editor": editor,
                "edit_time": edit_time,
            }
        )
        if private is not UNSET:
            field_dict["private"] = private
        if edited is not UNSET:
            field_dict["edited"] = edited

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.note_history import NoteHistory
        from ..models.note_type import NoteType
        from ..models.user_stub import UserStub

        d = src_dict.copy()
        id = d.pop("id")

        author = UserStub.from_dict(d.pop("author"))

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = NoteHistory.from_dict(history_item_data)

            history.append(history_item)

        note_type = NoteType.from_dict(d.pop("note_type"))

        entry = d.pop("entry")

        date = isoparse(d.pop("date"))

        _editor = d.pop("editor")
        editor: Optional[UserStub]
        if _editor is None:
            editor = None
        else:
            editor = UserStub.from_dict(_editor)

        private = d.pop("private", UNSET)

        edited = d.pop("edited", UNSET)

        _edit_time = d.pop("edit_time")
        edit_time: Optional[datetime.datetime]
        if _edit_time is None:
            edit_time = None
        else:
            edit_time = isoparse(_edit_time)

        note = cls(
            id=id,
            author=author,
            history=history,
            note_type=note_type,
            entry=entry,
            date=date,
            editor=editor,
            private=private,
            edited=edited,
            edit_time=edit_time,
        )

        note.additional_properties = d
        return note

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

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file import File


T = TypeVar("T", bound="EngagementToFiles")


@_attrs_define
class EngagementToFiles:
    """
    Attributes:
        files (List['File']):
        engagement_id (Optional[int]):
    """

    files: List["File"]
    engagement_id: Optional[int]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()

            files.append(files_item)

        engagement_id = self.engagement_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
                "engagement_id": engagement_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file import File

        d = src_dict.copy()
        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = File.from_dict(files_item_data)

            files.append(files_item)

        engagement_id = d.pop("engagement_id")

        engagement_to_files = cls(
            files=files,
            engagement_id=engagement_id,
        )

        engagement_to_files.additional_properties = d
        return engagement_to_files

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

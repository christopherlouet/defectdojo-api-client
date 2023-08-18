from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LanguageTypeRequest")


@_attrs_define
class LanguageTypeRequest:
    """
    Attributes:
        language (str):
        color (Union[Unset, None, str]):
    """

    language: str
    color: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        color = self.color

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        language = (
            self.language if isinstance(self.language, Unset) else (None, str(self.language).encode(), "text/plain")
        )
        color = self.color if isinstance(self.color, Unset) else (None, str(self.color).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "language": language,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language")

        color = d.pop("color", UNSET)

        language_type_request = cls(
            language=language,
            color=color,
        )

        language_type_request.additional_properties = d
        return language_type_request

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

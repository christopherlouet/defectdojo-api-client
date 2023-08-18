from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LanguageRequest")


@_attrs_define
class LanguageRequest:
    """
    Attributes:
        language (int):
        product (int):
        files (Union[Unset, None, int]):
        blank (Union[Unset, None, int]):
        comment (Union[Unset, None, int]):
        code (Union[Unset, None, int]):
        user (Union[Unset, None, int]):
    """

    language: int
    product: int
    files: Union[Unset, None, int] = UNSET
    blank: Union[Unset, None, int] = UNSET
    comment: Union[Unset, None, int] = UNSET
    code: Union[Unset, None, int] = UNSET
    user: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        product = self.product
        files = self.files
        blank = self.blank
        comment = self.comment
        code = self.code
        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "product": product,
            }
        )
        if files is not UNSET:
            field_dict["files"] = files
        if blank is not UNSET:
            field_dict["blank"] = blank
        if comment is not UNSET:
            field_dict["comment"] = comment
        if code is not UNSET:
            field_dict["code"] = code
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        language = (
            self.language if isinstance(self.language, Unset) else (None, str(self.language).encode(), "text/plain")
        )
        product = self.product if isinstance(self.product, Unset) else (None, str(self.product).encode(), "text/plain")
        files = self.files if isinstance(self.files, Unset) else (None, str(self.files).encode(), "text/plain")
        blank = self.blank if isinstance(self.blank, Unset) else (None, str(self.blank).encode(), "text/plain")
        comment = self.comment if isinstance(self.comment, Unset) else (None, str(self.comment).encode(), "text/plain")
        code = self.code if isinstance(self.code, Unset) else (None, str(self.code).encode(), "text/plain")
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "language": language,
                "product": product,
            }
        )
        if files is not UNSET:
            field_dict["files"] = files
        if blank is not UNSET:
            field_dict["blank"] = blank
        if comment is not UNSET:
            field_dict["comment"] = comment
        if code is not UNSET:
            field_dict["code"] = code
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language")

        product = d.pop("product")

        files = d.pop("files", UNSET)

        blank = d.pop("blank", UNSET)

        comment = d.pop("comment", UNSET)

        code = d.pop("code", UNSET)

        user = d.pop("user", UNSET)

        language_request = cls(
            language=language,
            product=product,
            files=files,
            blank=blank,
            comment=comment,
            code=code,
            user=user,
        )

        language_request.additional_properties = d
        return language_request

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

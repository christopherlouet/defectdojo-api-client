import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_import_request_import_settings import TestImportRequestImportSettings


T = TypeVar("T", bound="TestImportRequest")


@_attrs_define
class TestImportRequest:
    """
    Attributes:
        import_settings (Union[Unset, None, TestImportRequestImportSettings]):
        type (Union[Unset, str]):
        version (Union[Unset, None, str]):
        build_id (Union[Unset, None, str]): Build ID that was tested, a reimport may update this field.
        commit_hash (Union[Unset, None, str]): Commit hash tested, a reimport may update this field.
        branch_tag (Union[Unset, None, str]): Tag or branch that was tested, a reimport may update this field.
    """

    import_settings: Union[Unset, None, "TestImportRequestImportSettings"] = UNSET
    type: Union[Unset, str] = UNSET
    version: Union[Unset, None, str] = UNSET
    build_id: Union[Unset, None, str] = UNSET
    commit_hash: Union[Unset, None, str] = UNSET
    branch_tag: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        import_settings: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.import_settings, Unset):
            import_settings = self.import_settings.to_dict() if self.import_settings else None

        type = self.type
        version = self.version
        build_id = self.build_id
        commit_hash = self.commit_hash
        branch_tag = self.branch_tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if import_settings is not UNSET:
            field_dict["import_settings"] = import_settings
        if type is not UNSET:
            field_dict["type"] = type
        if version is not UNSET:
            field_dict["version"] = version
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        import_settings: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.import_settings, Unset):
            import_settings = (
                (None, json.dumps(self.import_settings.to_dict()).encode(), "application/json")
                if self.import_settings
                else None
            )

        type = self.type if isinstance(self.type, Unset) else (None, str(self.type).encode(), "text/plain")
        version = self.version if isinstance(self.version, Unset) else (None, str(self.version).encode(), "text/plain")
        build_id = (
            self.build_id if isinstance(self.build_id, Unset) else (None, str(self.build_id).encode(), "text/plain")
        )
        commit_hash = (
            self.commit_hash
            if isinstance(self.commit_hash, Unset)
            else (None, str(self.commit_hash).encode(), "text/plain")
        )
        branch_tag = (
            self.branch_tag
            if isinstance(self.branch_tag, Unset)
            else (None, str(self.branch_tag).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if import_settings is not UNSET:
            field_dict["import_settings"] = import_settings
        if type is not UNSET:
            field_dict["type"] = type
        if version is not UNSET:
            field_dict["version"] = version
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.test_import_request_import_settings import TestImportRequestImportSettings

        d = src_dict.copy()
        _import_settings = d.pop("import_settings", UNSET)
        import_settings: Union[Unset, None, TestImportRequestImportSettings]
        if _import_settings is None:
            import_settings = None
        elif isinstance(_import_settings, Unset):
            import_settings = UNSET
        else:
            import_settings = TestImportRequestImportSettings.from_dict(_import_settings)

        type = d.pop("type", UNSET)

        version = d.pop("version", UNSET)

        build_id = d.pop("build_id", UNSET)

        commit_hash = d.pop("commit_hash", UNSET)

        branch_tag = d.pop("branch_tag", UNSET)

        test_import_request = cls(
            import_settings=import_settings,
            type=type,
            version=version,
            build_id=build_id,
            commit_hash=commit_hash,
            branch_tag=branch_tag,
        )

        test_import_request.additional_properties = d
        return test_import_request

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

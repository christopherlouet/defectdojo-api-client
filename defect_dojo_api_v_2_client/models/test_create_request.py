import datetime
import json
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestCreateRequest")


@_attrs_define
class TestCreateRequest:
    """
    Attributes:
        engagement (int):
        target_start (datetime.datetime):
        target_end (datetime.datetime):
        test_type (int):
        notes (Union[Unset, List[Optional[int]]]):
        tags (Union[Unset, List[str]]):
        scan_type (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        percent_complete (Union[Unset, None, int]):
        version (Union[Unset, None, str]):
        build_id (Union[Unset, None, str]): Build ID that was tested, a reimport may update this field.
        commit_hash (Union[Unset, None, str]): Commit hash tested, a reimport may update this field.
        branch_tag (Union[Unset, None, str]): Tag or branch that was tested, a reimport may update this field.
        lead (Union[Unset, None, int]):
        environment (Union[Unset, None, int]):
        api_scan_configuration (Union[Unset, None, int]):
    """

    engagement: int
    target_start: datetime.datetime
    target_end: datetime.datetime
    test_type: int
    notes: Union[Unset, List[Optional[int]]] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    scan_type: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    percent_complete: Union[Unset, None, int] = UNSET
    version: Union[Unset, None, str] = UNSET
    build_id: Union[Unset, None, str] = UNSET
    commit_hash: Union[Unset, None, str] = UNSET
    branch_tag: Union[Unset, None, str] = UNSET
    lead: Union[Unset, None, int] = UNSET
    environment: Union[Unset, None, int] = UNSET
    api_scan_configuration: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        engagement = self.engagement
        target_start = self.target_start.isoformat()

        target_end = self.target_end.isoformat()

        test_type = self.test_type
        notes: Union[Unset, List[Optional[int]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        scan_type = self.scan_type
        title = self.title
        description = self.description
        percent_complete = self.percent_complete
        version = self.version
        build_id = self.build_id
        commit_hash = self.commit_hash
        branch_tag = self.branch_tag
        lead = self.lead
        environment = self.environment
        api_scan_configuration = self.api_scan_configuration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "engagement": engagement,
                "target_start": target_start,
                "target_end": target_end,
                "test_type": test_type,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes
        if tags is not UNSET:
            field_dict["tags"] = tags
        if scan_type is not UNSET:
            field_dict["scan_type"] = scan_type
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if percent_complete is not UNSET:
            field_dict["percent_complete"] = percent_complete
        if version is not UNSET:
            field_dict["version"] = version
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag
        if lead is not UNSET:
            field_dict["lead"] = lead
        if environment is not UNSET:
            field_dict["environment"] = environment
        if api_scan_configuration is not UNSET:
            field_dict["api_scan_configuration"] = api_scan_configuration

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        engagement = (
            self.engagement
            if isinstance(self.engagement, Unset)
            else (None, str(self.engagement).encode(), "text/plain")
        )
        target_start = self.target_start.isoformat().encode()

        target_end = self.target_end.isoformat().encode()

        test_type = (
            self.test_type if isinstance(self.test_type, Unset) else (None, str(self.test_type).encode(), "text/plain")
        )
        notes: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.notes, Unset):
            _temp_notes = self.notes
            notes = (None, json.dumps(_temp_notes).encode(), "application/json")

        tags: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = self.tags
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        scan_type = (
            self.scan_type if isinstance(self.scan_type, Unset) else (None, str(self.scan_type).encode(), "text/plain")
        )
        title = self.title if isinstance(self.title, Unset) else (None, str(self.title).encode(), "text/plain")
        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        percent_complete = (
            self.percent_complete
            if isinstance(self.percent_complete, Unset)
            else (None, str(self.percent_complete).encode(), "text/plain")
        )
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
        lead = self.lead if isinstance(self.lead, Unset) else (None, str(self.lead).encode(), "text/plain")
        environment = (
            self.environment
            if isinstance(self.environment, Unset)
            else (None, str(self.environment).encode(), "text/plain")
        )
        api_scan_configuration = (
            self.api_scan_configuration
            if isinstance(self.api_scan_configuration, Unset)
            else (None, str(self.api_scan_configuration).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "engagement": engagement,
                "target_start": target_start,
                "target_end": target_end,
                "test_type": test_type,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes
        if tags is not UNSET:
            field_dict["tags"] = tags
        if scan_type is not UNSET:
            field_dict["scan_type"] = scan_type
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if percent_complete is not UNSET:
            field_dict["percent_complete"] = percent_complete
        if version is not UNSET:
            field_dict["version"] = version
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag
        if lead is not UNSET:
            field_dict["lead"] = lead
        if environment is not UNSET:
            field_dict["environment"] = environment
        if api_scan_configuration is not UNSET:
            field_dict["api_scan_configuration"] = api_scan_configuration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        engagement = d.pop("engagement")

        target_start = isoparse(d.pop("target_start"))

        target_end = isoparse(d.pop("target_end"))

        test_type = d.pop("test_type")

        notes = cast(List[Optional[int]], d.pop("notes", UNSET))

        tags = cast(List[str], d.pop("tags", UNSET))

        scan_type = d.pop("scan_type", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        percent_complete = d.pop("percent_complete", UNSET)

        version = d.pop("version", UNSET)

        build_id = d.pop("build_id", UNSET)

        commit_hash = d.pop("commit_hash", UNSET)

        branch_tag = d.pop("branch_tag", UNSET)

        lead = d.pop("lead", UNSET)

        environment = d.pop("environment", UNSET)

        api_scan_configuration = d.pop("api_scan_configuration", UNSET)

        test_create_request = cls(
            engagement=engagement,
            target_start=target_start,
            target_end=target_end,
            test_type=test_type,
            notes=notes,
            tags=tags,
            scan_type=scan_type,
            title=title,
            description=description,
            percent_complete=percent_complete,
            version=version,
            build_id=build_id,
            commit_hash=commit_hash,
            branch_tag=branch_tag,
            lead=lead,
            environment=environment,
            api_scan_configuration=api_scan_configuration,
        )

        test_create_request.additional_properties = d
        return test_create_request

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

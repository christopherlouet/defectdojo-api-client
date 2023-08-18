import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.engagement_engagement_type import EngagementEngagementType
from ..models.engagement_status import EngagementStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File
    from ..models.note import Note


T = TypeVar("T", bound="Engagement")


@_attrs_define
class Engagement:
    """
    Attributes:
        id (int):
        target_start (datetime.date):
        target_end (datetime.date):
        active (bool):
        progress (str):
        done_testing (bool):
        product (int):
        notes (List['Note']):
        files (List['File']):
        risk_acceptance (List[int]):
        tags (Union[Unset, List[str]]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        version (Union[Unset, None, str]): Version of the product the engagement tested.
        first_contacted (Union[Unset, None, datetime.date]):
        reason (Union[Unset, None, str]):
        updated (Optional[datetime.datetime]):
        created (Optional[datetime.datetime]):
        tracker (Union[Unset, None, str]): Link to epic or ticket system with changes to version.
        test_strategy (Union[Unset, None, str]):
        threat_model (Union[Unset, bool]):
        api_test (Union[Unset, bool]):
        pen_test (Union[Unset, bool]):
        check_list (Union[Unset, bool]):
        status (Union[Unset, None, EngagementStatus]): * `Not Started` - Not Started
            * `Blocked` - Blocked
            * `Cancelled` - Cancelled
            * `Completed` - Completed
            * `In Progress` - In Progress
            * `On Hold` - On Hold
            * `Waiting for Resource` - Waiting for Resource
        tmodel_path (Optional[str]):
        engagement_type (Union[Unset, None, EngagementEngagementType]): * `Interactive` - Interactive
            * `CI/CD` - CI/CD
        build_id (Union[Unset, None, str]): Build ID of the product the engagement tested.
        commit_hash (Union[Unset, None, str]): Commit hash from repo
        branch_tag (Union[Unset, None, str]): Tag or branch of the product the engagement tested.
        source_code_management_uri (Union[Unset, None, str]): Resource link to source code
        deduplication_on_engagement (Union[Unset, bool]): If enabled deduplication will only mark a finding in this
            engagement as duplicate of another finding if both findings are in this engagement. If disabled, deduplication
            is on the product level.
        lead (Union[Unset, None, int]):
        requester (Union[Unset, None, int]):
        preset (Union[Unset, None, int]): Settings and notes for performing this engagement.
        report_type (Union[Unset, None, int]):
        build_server (Union[Unset, None, int]): Build server responsible for CI/CD test
        source_code_management_server (Union[Unset, None, int]): Source code server for CI/CD test
        orchestration_engine (Union[Unset, None, int]): Orchestration service responsible for CI/CD test
    """

    id: int
    target_start: datetime.date
    target_end: datetime.date
    active: bool
    progress: str
    done_testing: bool
    product: int
    notes: List["Note"]
    files: List["File"]
    risk_acceptance: List[int]
    updated: Optional[datetime.datetime]
    created: Optional[datetime.datetime]
    tmodel_path: Optional[str]
    tags: Union[Unset, List[str]] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, str] = UNSET
    first_contacted: Union[Unset, None, datetime.date] = UNSET
    reason: Union[Unset, None, str] = UNSET
    tracker: Union[Unset, None, str] = UNSET
    test_strategy: Union[Unset, None, str] = UNSET
    threat_model: Union[Unset, bool] = UNSET
    api_test: Union[Unset, bool] = UNSET
    pen_test: Union[Unset, bool] = UNSET
    check_list: Union[Unset, bool] = UNSET
    status: Union[Unset, None, EngagementStatus] = UNSET
    engagement_type: Union[Unset, None, EngagementEngagementType] = UNSET
    build_id: Union[Unset, None, str] = UNSET
    commit_hash: Union[Unset, None, str] = UNSET
    branch_tag: Union[Unset, None, str] = UNSET
    source_code_management_uri: Union[Unset, None, str] = UNSET
    deduplication_on_engagement: Union[Unset, bool] = UNSET
    lead: Union[Unset, None, int] = UNSET
    requester: Union[Unset, None, int] = UNSET
    preset: Union[Unset, None, int] = UNSET
    report_type: Union[Unset, None, int] = UNSET
    build_server: Union[Unset, None, int] = UNSET
    source_code_management_server: Union[Unset, None, int] = UNSET
    orchestration_engine: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        target_start = self.target_start.isoformat()
        target_end = self.target_end.isoformat()
        active = self.active
        progress = self.progress
        done_testing = self.done_testing
        product = self.product
        notes = []
        for notes_item_data in self.notes:
            notes_item = notes_item_data.to_dict()

            notes.append(notes_item)

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()

            files.append(files_item)

        risk_acceptance = self.risk_acceptance

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        name = self.name
        description = self.description
        version = self.version
        first_contacted: Union[Unset, None, str] = UNSET
        if not isinstance(self.first_contacted, Unset):
            first_contacted = self.first_contacted.isoformat() if self.first_contacted else None

        reason = self.reason
        updated = self.updated.isoformat() if self.updated else None

        created = self.created.isoformat() if self.created else None

        tracker = self.tracker
        test_strategy = self.test_strategy
        threat_model = self.threat_model
        api_test = self.api_test
        pen_test = self.pen_test
        check_list = self.check_list
        status: Union[Unset, None, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

        tmodel_path = self.tmodel_path
        engagement_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.engagement_type, Unset):
            engagement_type = self.engagement_type.value if self.engagement_type else None

        build_id = self.build_id
        commit_hash = self.commit_hash
        branch_tag = self.branch_tag
        source_code_management_uri = self.source_code_management_uri
        deduplication_on_engagement = self.deduplication_on_engagement
        lead = self.lead
        requester = self.requester
        preset = self.preset
        report_type = self.report_type
        build_server = self.build_server
        source_code_management_server = self.source_code_management_server
        orchestration_engine = self.orchestration_engine

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "target_start": target_start,
                "target_end": target_end,
                "active": active,
                "progress": progress,
                "done_testing": done_testing,
                "product": product,
                "notes": notes,
                "files": files,
                "risk_acceptance": risk_acceptance,
                "updated": updated,
                "created": created,
                "tmodel_path": tmodel_path,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if version is not UNSET:
            field_dict["version"] = version
        if first_contacted is not UNSET:
            field_dict["first_contacted"] = first_contacted
        if reason is not UNSET:
            field_dict["reason"] = reason
        if tracker is not UNSET:
            field_dict["tracker"] = tracker
        if test_strategy is not UNSET:
            field_dict["test_strategy"] = test_strategy
        if threat_model is not UNSET:
            field_dict["threat_model"] = threat_model
        if api_test is not UNSET:
            field_dict["api_test"] = api_test
        if pen_test is not UNSET:
            field_dict["pen_test"] = pen_test
        if check_list is not UNSET:
            field_dict["check_list"] = check_list
        if status is not UNSET:
            field_dict["status"] = status
        if engagement_type is not UNSET:
            field_dict["engagement_type"] = engagement_type
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag
        if source_code_management_uri is not UNSET:
            field_dict["source_code_management_uri"] = source_code_management_uri
        if deduplication_on_engagement is not UNSET:
            field_dict["deduplication_on_engagement"] = deduplication_on_engagement
        if lead is not UNSET:
            field_dict["lead"] = lead
        if requester is not UNSET:
            field_dict["requester"] = requester
        if preset is not UNSET:
            field_dict["preset"] = preset
        if report_type is not UNSET:
            field_dict["report_type"] = report_type
        if build_server is not UNSET:
            field_dict["build_server"] = build_server
        if source_code_management_server is not UNSET:
            field_dict["source_code_management_server"] = source_code_management_server
        if orchestration_engine is not UNSET:
            field_dict["orchestration_engine"] = orchestration_engine

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file import File
        from ..models.note import Note

        d = src_dict.copy()
        id = d.pop("id")

        target_start = isoparse(d.pop("target_start")).date()

        target_end = isoparse(d.pop("target_end")).date()

        active = d.pop("active")

        progress = d.pop("progress")

        done_testing = d.pop("done_testing")

        product = d.pop("product")

        notes = []
        _notes = d.pop("notes")
        for notes_item_data in _notes:
            notes_item = Note.from_dict(notes_item_data)

            notes.append(notes_item)

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = File.from_dict(files_item_data)

            files.append(files_item)

        risk_acceptance = cast(List[int], d.pop("risk_acceptance"))

        tags = cast(List[str], d.pop("tags", UNSET))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        version = d.pop("version", UNSET)

        _first_contacted = d.pop("first_contacted", UNSET)
        first_contacted: Union[Unset, None, datetime.date]
        if _first_contacted is None:
            first_contacted = None
        elif isinstance(_first_contacted, Unset):
            first_contacted = UNSET
        else:
            first_contacted = isoparse(_first_contacted).date()

        reason = d.pop("reason", UNSET)

        _updated = d.pop("updated")
        updated: Optional[datetime.datetime]
        if _updated is None:
            updated = None
        else:
            updated = isoparse(_updated)

        _created = d.pop("created")
        created: Optional[datetime.datetime]
        if _created is None:
            created = None
        else:
            created = isoparse(_created)

        tracker = d.pop("tracker", UNSET)

        test_strategy = d.pop("test_strategy", UNSET)

        threat_model = d.pop("threat_model", UNSET)

        api_test = d.pop("api_test", UNSET)

        pen_test = d.pop("pen_test", UNSET)

        check_list = d.pop("check_list", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, None, EngagementStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = EngagementStatus(_status)

        tmodel_path = d.pop("tmodel_path")

        _engagement_type = d.pop("engagement_type", UNSET)
        engagement_type: Union[Unset, None, EngagementEngagementType]
        if _engagement_type is None:
            engagement_type = None
        elif isinstance(_engagement_type, Unset):
            engagement_type = UNSET
        else:
            engagement_type = EngagementEngagementType(_engagement_type)

        build_id = d.pop("build_id", UNSET)

        commit_hash = d.pop("commit_hash", UNSET)

        branch_tag = d.pop("branch_tag", UNSET)

        source_code_management_uri = d.pop("source_code_management_uri", UNSET)

        deduplication_on_engagement = d.pop("deduplication_on_engagement", UNSET)

        lead = d.pop("lead", UNSET)

        requester = d.pop("requester", UNSET)

        preset = d.pop("preset", UNSET)

        report_type = d.pop("report_type", UNSET)

        build_server = d.pop("build_server", UNSET)

        source_code_management_server = d.pop("source_code_management_server", UNSET)

        orchestration_engine = d.pop("orchestration_engine", UNSET)

        engagement = cls(
            id=id,
            target_start=target_start,
            target_end=target_end,
            active=active,
            progress=progress,
            done_testing=done_testing,
            product=product,
            notes=notes,
            files=files,
            risk_acceptance=risk_acceptance,
            tags=tags,
            name=name,
            description=description,
            version=version,
            first_contacted=first_contacted,
            reason=reason,
            updated=updated,
            created=created,
            tracker=tracker,
            test_strategy=test_strategy,
            threat_model=threat_model,
            api_test=api_test,
            pen_test=pen_test,
            check_list=check_list,
            status=status,
            tmodel_path=tmodel_path,
            engagement_type=engagement_type,
            build_id=build_id,
            commit_hash=commit_hash,
            branch_tag=branch_tag,
            source_code_management_uri=source_code_management_uri,
            deduplication_on_engagement=deduplication_on_engagement,
            lead=lead,
            requester=requester,
            preset=preset,
            report_type=report_type,
            build_server=build_server,
            source_code_management_server=source_code_management_server,
            orchestration_engine=orchestration_engine,
        )

        engagement.additional_properties = d
        return engagement

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

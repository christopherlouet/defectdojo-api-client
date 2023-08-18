import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="JIRAIssue")


@_attrs_define
class JIRAIssue:
    """
    Attributes:
        id (int):
        url (str):
        jira_id (str):
        jira_key (str):
        jira_creation (Union[Unset, None, datetime.datetime]): The date a Jira issue was created from this finding.
        jira_change (Union[Unset, None, datetime.datetime]): The date the linked Jira issue was last modified.
        jira_project (Union[Unset, None, int]):
        finding (Union[Unset, None, int]):
        engagement (Union[Unset, None, int]):
        finding_group (Union[Unset, None, int]):
    """

    id: int
    url: str
    jira_id: str
    jira_key: str
    jira_creation: Union[Unset, None, datetime.datetime] = UNSET
    jira_change: Union[Unset, None, datetime.datetime] = UNSET
    jira_project: Union[Unset, None, int] = UNSET
    finding: Union[Unset, None, int] = UNSET
    engagement: Union[Unset, None, int] = UNSET
    finding_group: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        jira_id = self.jira_id
        jira_key = self.jira_key
        jira_creation: Union[Unset, None, str] = UNSET
        if not isinstance(self.jira_creation, Unset):
            jira_creation = self.jira_creation.isoformat() if self.jira_creation else None

        jira_change: Union[Unset, None, str] = UNSET
        if not isinstance(self.jira_change, Unset):
            jira_change = self.jira_change.isoformat() if self.jira_change else None

        jira_project = self.jira_project
        finding = self.finding
        engagement = self.engagement
        finding_group = self.finding_group

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "jira_id": jira_id,
                "jira_key": jira_key,
            }
        )
        if jira_creation is not UNSET:
            field_dict["jira_creation"] = jira_creation
        if jira_change is not UNSET:
            field_dict["jira_change"] = jira_change
        if jira_project is not UNSET:
            field_dict["jira_project"] = jira_project
        if finding is not UNSET:
            field_dict["finding"] = finding
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if finding_group is not UNSET:
            field_dict["finding_group"] = finding_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        jira_id = d.pop("jira_id")

        jira_key = d.pop("jira_key")

        _jira_creation = d.pop("jira_creation", UNSET)
        jira_creation: Union[Unset, None, datetime.datetime]
        if _jira_creation is None:
            jira_creation = None
        elif isinstance(_jira_creation, Unset):
            jira_creation = UNSET
        else:
            jira_creation = isoparse(_jira_creation)

        _jira_change = d.pop("jira_change", UNSET)
        jira_change: Union[Unset, None, datetime.datetime]
        if _jira_change is None:
            jira_change = None
        elif isinstance(_jira_change, Unset):
            jira_change = UNSET
        else:
            jira_change = isoparse(_jira_change)

        jira_project = d.pop("jira_project", UNSET)

        finding = d.pop("finding", UNSET)

        engagement = d.pop("engagement", UNSET)

        finding_group = d.pop("finding_group", UNSET)

        jira_issue = cls(
            id=id,
            url=url,
            jira_id=jira_id,
            jira_key=jira_key,
            jira_creation=jira_creation,
            jira_change=jira_change,
            jira_project=jira_project,
            finding=finding,
            engagement=engagement,
            finding_group=finding_group,
        )

        jira_issue.additional_properties = d
        return jira_issue

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

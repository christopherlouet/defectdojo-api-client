from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.jira_issue import JIRAIssue


T = TypeVar("T", bound="FindingGroup")


@_attrs_define
class FindingGroup:
    """
    Attributes:
        id (int):
        name (str):
        test (int):
        jira_issue (JIRAIssue):
    """

    id: int
    name: str
    test: int
    jira_issue: "JIRAIssue"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        test = self.test
        jira_issue = self.jira_issue.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "test": test,
                "jira_issue": jira_issue,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.jira_issue import JIRAIssue

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        test = d.pop("test")

        jira_issue = JIRAIssue.from_dict(d.pop("jira_issue"))

        finding_group = cls(
            id=id,
            name=name,
            test=test,
            jira_issue=jira_issue,
        )

        finding_group.additional_properties = d
        return finding_group

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

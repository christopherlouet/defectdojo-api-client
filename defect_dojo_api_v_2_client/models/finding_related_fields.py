from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.finding_test import FindingTest
    from ..models.jira_issue import JIRAIssue


T = TypeVar("T", bound="FindingRelatedFields")


@_attrs_define
class FindingRelatedFields:
    """
    Attributes:
        test (FindingTest):
        jira (JIRAIssue):
    """

    test: "FindingTest"
    jira: "JIRAIssue"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        test = self.test.to_dict()

        jira = self.jira.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test": test,
                "jira": jira,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.finding_test import FindingTest
        from ..models.jira_issue import JIRAIssue

        d = src_dict.copy()
        test = FindingTest.from_dict(d.pop("test"))

        jira = JIRAIssue.from_dict(d.pop("jira"))

        finding_related_fields = cls(
            test=test,
            jira=jira,
        )

        finding_related_fields.additional_properties = d
        return finding_related_fields

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

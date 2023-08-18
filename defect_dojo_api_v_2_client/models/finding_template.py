import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vulnerability_id_template import VulnerabilityIdTemplate


T = TypeVar("T", bound="FindingTemplate")


@_attrs_define
class FindingTemplate:
    """
    Attributes:
        id (int):
        title (str):
        tags (Union[Unset, List[str]]):
        vulnerability_ids (Union[Unset, List['VulnerabilityIdTemplate']]):
        cwe (Union[Unset, None, int]):
        cvssv3 (Union[Unset, None, str]):
        severity (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        mitigation (Union[Unset, None, str]):
        impact (Union[Unset, None, str]):
        references (Union[Unset, None, str]):
        last_used (Optional[datetime.datetime]):
        numerical_severity (Optional[str]):
        template_match (Union[Unset, bool]): Enables this template for matching remediation advice. Match will be
            applied to all active, verified findings by CWE.
        template_match_title (Union[Unset, bool]): Matches by title text (contains search) and CWE.
    """

    id: int
    title: str
    last_used: Optional[datetime.datetime]
    numerical_severity: Optional[str]
    tags: Union[Unset, List[str]] = UNSET
    vulnerability_ids: Union[Unset, List["VulnerabilityIdTemplate"]] = UNSET
    cwe: Union[Unset, None, int] = UNSET
    cvssv3: Union[Unset, None, str] = UNSET
    severity: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    mitigation: Union[Unset, None, str] = UNSET
    impact: Union[Unset, None, str] = UNSET
    references: Union[Unset, None, str] = UNSET
    template_match: Union[Unset, bool] = UNSET
    template_match_title: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        vulnerability_ids: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vulnerability_ids, Unset):
            vulnerability_ids = []
            for vulnerability_ids_item_data in self.vulnerability_ids:
                vulnerability_ids_item = vulnerability_ids_item_data.to_dict()

                vulnerability_ids.append(vulnerability_ids_item)

        cwe = self.cwe
        cvssv3 = self.cvssv3
        severity = self.severity
        description = self.description
        mitigation = self.mitigation
        impact = self.impact
        references = self.references
        last_used = self.last_used.isoformat() if self.last_used else None

        numerical_severity = self.numerical_severity
        template_match = self.template_match
        template_match_title = self.template_match_title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "last_used": last_used,
                "numerical_severity": numerical_severity,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if vulnerability_ids is not UNSET:
            field_dict["vulnerability_ids"] = vulnerability_ids
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if cvssv3 is not UNSET:
            field_dict["cvssv3"] = cvssv3
        if severity is not UNSET:
            field_dict["severity"] = severity
        if description is not UNSET:
            field_dict["description"] = description
        if mitigation is not UNSET:
            field_dict["mitigation"] = mitigation
        if impact is not UNSET:
            field_dict["impact"] = impact
        if references is not UNSET:
            field_dict["references"] = references
        if template_match is not UNSET:
            field_dict["template_match"] = template_match
        if template_match_title is not UNSET:
            field_dict["template_match_title"] = template_match_title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.vulnerability_id_template import VulnerabilityIdTemplate

        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title")

        tags = cast(List[str], d.pop("tags", UNSET))

        vulnerability_ids = []
        _vulnerability_ids = d.pop("vulnerability_ids", UNSET)
        for vulnerability_ids_item_data in _vulnerability_ids or []:
            vulnerability_ids_item = VulnerabilityIdTemplate.from_dict(vulnerability_ids_item_data)

            vulnerability_ids.append(vulnerability_ids_item)

        cwe = d.pop("cwe", UNSET)

        cvssv3 = d.pop("cvssv3", UNSET)

        severity = d.pop("severity", UNSET)

        description = d.pop("description", UNSET)

        mitigation = d.pop("mitigation", UNSET)

        impact = d.pop("impact", UNSET)

        references = d.pop("references", UNSET)

        _last_used = d.pop("last_used")
        last_used: Optional[datetime.datetime]
        if _last_used is None:
            last_used = None
        else:
            last_used = isoparse(_last_used)

        numerical_severity = d.pop("numerical_severity")

        template_match = d.pop("template_match", UNSET)

        template_match_title = d.pop("template_match_title", UNSET)

        finding_template = cls(
            id=id,
            title=title,
            tags=tags,
            vulnerability_ids=vulnerability_ids,
            cwe=cwe,
            cvssv3=cvssv3,
            severity=severity,
            description=description,
            mitigation=mitigation,
            impact=impact,
            references=references,
            last_used=last_used,
            numerical_severity=numerical_severity,
            template_match=template_match,
            template_match_title=template_match_title,
        )

        finding_template.additional_properties = d
        return finding_template

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

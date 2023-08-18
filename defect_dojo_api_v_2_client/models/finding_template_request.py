import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vulnerability_id_template_request import VulnerabilityIdTemplateRequest


T = TypeVar("T", bound="FindingTemplateRequest")


@_attrs_define
class FindingTemplateRequest:
    """
    Attributes:
        title (str):
        tags (Union[Unset, List[str]]):
        vulnerability_ids (Union[Unset, List['VulnerabilityIdTemplateRequest']]):
        cwe (Union[Unset, None, int]):
        cvssv3 (Union[Unset, None, str]):
        severity (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        mitigation (Union[Unset, None, str]):
        impact (Union[Unset, None, str]):
        references (Union[Unset, None, str]):
        template_match (Union[Unset, bool]): Enables this template for matching remediation advice. Match will be
            applied to all active, verified findings by CWE.
        template_match_title (Union[Unset, bool]): Matches by title text (contains search) and CWE.
    """

    title: str
    tags: Union[Unset, List[str]] = UNSET
    vulnerability_ids: Union[Unset, List["VulnerabilityIdTemplateRequest"]] = UNSET
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
        template_match = self.template_match
        template_match_title = self.template_match_title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
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

    def to_multipart(self) -> Dict[str, Any]:
        title = self.title if isinstance(self.title, Unset) else (None, str(self.title).encode(), "text/plain")
        tags: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = self.tags
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        vulnerability_ids: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.vulnerability_ids, Unset):
            _temp_vulnerability_ids = []
            for vulnerability_ids_item_data in self.vulnerability_ids:
                vulnerability_ids_item = vulnerability_ids_item_data.to_dict()

                _temp_vulnerability_ids.append(vulnerability_ids_item)
            vulnerability_ids = (None, json.dumps(_temp_vulnerability_ids).encode(), "application/json")

        cwe = self.cwe if isinstance(self.cwe, Unset) else (None, str(self.cwe).encode(), "text/plain")
        cvssv3 = self.cvssv3 if isinstance(self.cvssv3, Unset) else (None, str(self.cvssv3).encode(), "text/plain")
        severity = (
            self.severity if isinstance(self.severity, Unset) else (None, str(self.severity).encode(), "text/plain")
        )
        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        mitigation = (
            self.mitigation
            if isinstance(self.mitigation, Unset)
            else (None, str(self.mitigation).encode(), "text/plain")
        )
        impact = self.impact if isinstance(self.impact, Unset) else (None, str(self.impact).encode(), "text/plain")
        references = (
            self.references
            if isinstance(self.references, Unset)
            else (None, str(self.references).encode(), "text/plain")
        )
        template_match = (
            self.template_match
            if isinstance(self.template_match, Unset)
            else (None, str(self.template_match).encode(), "text/plain")
        )
        template_match_title = (
            self.template_match_title
            if isinstance(self.template_match_title, Unset)
            else (None, str(self.template_match_title).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "title": title,
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
        from ..models.vulnerability_id_template_request import VulnerabilityIdTemplateRequest

        d = src_dict.copy()
        title = d.pop("title")

        tags = cast(List[str], d.pop("tags", UNSET))

        vulnerability_ids = []
        _vulnerability_ids = d.pop("vulnerability_ids", UNSET)
        for vulnerability_ids_item_data in _vulnerability_ids or []:
            vulnerability_ids_item = VulnerabilityIdTemplateRequest.from_dict(vulnerability_ids_item_data)

            vulnerability_ids.append(vulnerability_ids_item)

        cwe = d.pop("cwe", UNSET)

        cvssv3 = d.pop("cvssv3", UNSET)

        severity = d.pop("severity", UNSET)

        description = d.pop("description", UNSET)

        mitigation = d.pop("mitigation", UNSET)

        impact = d.pop("impact", UNSET)

        references = d.pop("references", UNSET)

        template_match = d.pop("template_match", UNSET)

        template_match_title = d.pop("template_match_title", UNSET)

        finding_template_request = cls(
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
            template_match=template_match,
            template_match_title=template_match_title,
        )

        finding_template_request.additional_properties = d
        return finding_template_request

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

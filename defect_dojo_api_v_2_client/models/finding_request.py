import datetime
import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vulnerability_id_request import VulnerabilityIdRequest


T = TypeVar("T", bound="FindingRequest")


@_attrs_define
class FindingRequest:
    """
    Attributes:
        title (str): A short description of the flaw.
        severity (str): The severity level of this flaw (Critical, High, Medium, Low, Informational).
        description (str): Longer more descriptive information about the flaw.
        numerical_severity (str): The numerical representation of the severity (S0, S1, S2, S3, S4).
        tags (Union[Unset, List[str]]):
        push_to_jira (Union[Unset, bool]):
        vulnerability_ids (Union[Unset, List['VulnerabilityIdRequest']]):
        reporter (Union[Unset, int]):
        date (Union[Unset, datetime.date]): The date the flaw was discovered.
        sla_start_date (Union[Unset, None, datetime.date]): (readonly)The date used as start date for SLA calculation.
            Set by expiring risk acceptances. Empty by default, causing a fallback to 'date'.
        cwe (Union[Unset, None, int]): The CWE number associated with this flaw.
        cvssv3 (Union[Unset, None, str]): Common Vulnerability Scoring System version 3 (CVSSv3) score associated with
            this flaw.
        cvssv3_score (Union[Unset, None, float]): Numerical CVSSv3 score for the vulnerability. If the vector is given,
            the score is updated while saving the finding
        mitigation (Union[Unset, None, str]): Text describing how to best fix the flaw.
        impact (Union[Unset, None, str]): Text describing the impact this flaw has on systems, products, enterprise,
            etc.
        steps_to_reproduce (Union[Unset, None, str]): Text describing the steps that must be followed in order to
            reproduce the flaw / bug.
        severity_justification (Union[Unset, None, str]): Text describing why a certain severity was associated with
            this flaw.
        references (Union[Unset, None, str]): The external documentation available for this flaw.
        active (Union[Unset, bool]): Denotes if this flaw is active or not.
        verified (Union[Unset, bool]): Denotes if this flaw has been manually verified by the tester.
        false_p (Union[Unset, bool]): Denotes if this flaw has been deemed a false positive by the tester.
        duplicate (Union[Unset, bool]): Denotes if this flaw is a duplicate of other flaws reported.
        out_of_scope (Union[Unset, bool]): Denotes if this flaw falls outside the scope of the test and/or engagement.
        risk_accepted (Union[Unset, bool]): Denotes if this finding has been marked as an accepted risk.
        under_review (Union[Unset, bool]): Denotes is this flaw is currently being reviewed.
        under_defect_review (Union[Unset, bool]): Denotes if this finding is under defect review.
        is_mitigated (Union[Unset, bool]): Denotes if this flaw has been fixed.
        line (Union[Unset, None, int]): Source line number of the attack vector.
        file_path (Union[Unset, None, str]): Identified file(s) containing the flaw.
        component_name (Union[Unset, None, str]): Name of the affected component (library name, part of a system, ...).
        component_version (Union[Unset, None, str]): Version of the affected component.
        static_finding (Union[Unset, bool]): Flaw has been detected from a Static Application Security Testing tool
            (SAST).
        dynamic_finding (Union[Unset, bool]): Flaw has been detected from a Dynamic Application Security Testing tool
            (DAST).
        unique_id_from_tool (Union[Unset, None, str]): Vulnerability technical id from the source tool. Allows to track
            unique vulnerabilities.
        vuln_id_from_tool (Union[Unset, None, str]): Non-unique technical id from the source tool associated with the
            vulnerability type.
        sast_source_object (Union[Unset, None, str]): Source object (variable, function...) of the attack vector.
        sast_sink_object (Union[Unset, None, str]): Sink object (variable, function...) of the attack vector.
        sast_source_line (Union[Unset, None, int]): Source line number of the attack vector.
        sast_source_file_path (Union[Unset, None, str]): Source file path of the attack vector.
        nb_occurences (Union[Unset, None, int]): Number of occurences in the source tool when several vulnerabilites
            were found and aggregated by the scanner.
        publish_date (Union[Unset, None, datetime.date]): Date when this vulnerability was made publicly available.
        service (Union[Unset, None, str]): A service is a self-contained piece of functionality within a Product. This
            is an optional field which is used in deduplication of findings when set.
        planned_remediation_date (Union[Unset, None, datetime.date]): The date the flaw is expected to be remediated.
        planned_remediation_version (Union[Unset, None, str]): The target version when the vulnerability should be fixed
            / remediated
        effort_for_fixing (Union[Unset, None, str]): Effort for fixing / remediating the vulnerability (Low, Medium,
            High)
        review_requested_by (Union[Unset, None, int]): Documents who requested a review for this finding.
        defect_review_requested_by (Union[Unset, None, int]): Documents who requested a defect review for this flaw.
        sonarqube_issue (Union[Unset, None, int]): The SonarQube issue associated with this finding.
        reviewers (Union[Unset, List[int]]): Documents who reviewed the flaw.
    """

    title: str
    severity: str
    description: str
    numerical_severity: str
    tags: Union[Unset, List[str]] = UNSET
    push_to_jira: Union[Unset, bool] = False
    vulnerability_ids: Union[Unset, List["VulnerabilityIdRequest"]] = UNSET
    reporter: Union[Unset, int] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    sla_start_date: Union[Unset, None, datetime.date] = UNSET
    cwe: Union[Unset, None, int] = UNSET
    cvssv3: Union[Unset, None, str] = UNSET
    cvssv3_score: Union[Unset, None, float] = UNSET
    mitigation: Union[Unset, None, str] = UNSET
    impact: Union[Unset, None, str] = UNSET
    steps_to_reproduce: Union[Unset, None, str] = UNSET
    severity_justification: Union[Unset, None, str] = UNSET
    references: Union[Unset, None, str] = UNSET
    active: Union[Unset, bool] = UNSET
    verified: Union[Unset, bool] = UNSET
    false_p: Union[Unset, bool] = UNSET
    duplicate: Union[Unset, bool] = UNSET
    out_of_scope: Union[Unset, bool] = UNSET
    risk_accepted: Union[Unset, bool] = UNSET
    under_review: Union[Unset, bool] = UNSET
    under_defect_review: Union[Unset, bool] = UNSET
    is_mitigated: Union[Unset, bool] = UNSET
    line: Union[Unset, None, int] = UNSET
    file_path: Union[Unset, None, str] = UNSET
    component_name: Union[Unset, None, str] = UNSET
    component_version: Union[Unset, None, str] = UNSET
    static_finding: Union[Unset, bool] = UNSET
    dynamic_finding: Union[Unset, bool] = UNSET
    unique_id_from_tool: Union[Unset, None, str] = UNSET
    vuln_id_from_tool: Union[Unset, None, str] = UNSET
    sast_source_object: Union[Unset, None, str] = UNSET
    sast_sink_object: Union[Unset, None, str] = UNSET
    sast_source_line: Union[Unset, None, int] = UNSET
    sast_source_file_path: Union[Unset, None, str] = UNSET
    nb_occurences: Union[Unset, None, int] = UNSET
    publish_date: Union[Unset, None, datetime.date] = UNSET
    service: Union[Unset, None, str] = UNSET
    planned_remediation_date: Union[Unset, None, datetime.date] = UNSET
    planned_remediation_version: Union[Unset, None, str] = UNSET
    effort_for_fixing: Union[Unset, None, str] = UNSET
    review_requested_by: Union[Unset, None, int] = UNSET
    defect_review_requested_by: Union[Unset, None, int] = UNSET
    sonarqube_issue: Union[Unset, None, int] = UNSET
    reviewers: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        severity = self.severity
        description = self.description
        numerical_severity = self.numerical_severity
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        push_to_jira = self.push_to_jira
        vulnerability_ids: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vulnerability_ids, Unset):
            vulnerability_ids = []
            for vulnerability_ids_item_data in self.vulnerability_ids:
                vulnerability_ids_item = vulnerability_ids_item_data.to_dict()

                vulnerability_ids.append(vulnerability_ids_item)

        reporter = self.reporter
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        sla_start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.sla_start_date, Unset):
            sla_start_date = self.sla_start_date.isoformat() if self.sla_start_date else None

        cwe = self.cwe
        cvssv3 = self.cvssv3
        cvssv3_score = self.cvssv3_score
        mitigation = self.mitigation
        impact = self.impact
        steps_to_reproduce = self.steps_to_reproduce
        severity_justification = self.severity_justification
        references = self.references
        active = self.active
        verified = self.verified
        false_p = self.false_p
        duplicate = self.duplicate
        out_of_scope = self.out_of_scope
        risk_accepted = self.risk_accepted
        under_review = self.under_review
        under_defect_review = self.under_defect_review
        is_mitigated = self.is_mitigated
        line = self.line
        file_path = self.file_path
        component_name = self.component_name
        component_version = self.component_version
        static_finding = self.static_finding
        dynamic_finding = self.dynamic_finding
        unique_id_from_tool = self.unique_id_from_tool
        vuln_id_from_tool = self.vuln_id_from_tool
        sast_source_object = self.sast_source_object
        sast_sink_object = self.sast_sink_object
        sast_source_line = self.sast_source_line
        sast_source_file_path = self.sast_source_file_path
        nb_occurences = self.nb_occurences
        publish_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.publish_date, Unset):
            publish_date = self.publish_date.isoformat() if self.publish_date else None

        service = self.service
        planned_remediation_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.planned_remediation_date, Unset):
            planned_remediation_date = (
                self.planned_remediation_date.isoformat() if self.planned_remediation_date else None
            )

        planned_remediation_version = self.planned_remediation_version
        effort_for_fixing = self.effort_for_fixing
        review_requested_by = self.review_requested_by
        defect_review_requested_by = self.defect_review_requested_by
        sonarqube_issue = self.sonarqube_issue
        reviewers: Union[Unset, List[int]] = UNSET
        if not isinstance(self.reviewers, Unset):
            reviewers = self.reviewers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "severity": severity,
                "description": description,
                "numerical_severity": numerical_severity,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if push_to_jira is not UNSET:
            field_dict["push_to_jira"] = push_to_jira
        if vulnerability_ids is not UNSET:
            field_dict["vulnerability_ids"] = vulnerability_ids
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if date is not UNSET:
            field_dict["date"] = date
        if sla_start_date is not UNSET:
            field_dict["sla_start_date"] = sla_start_date
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if cvssv3 is not UNSET:
            field_dict["cvssv3"] = cvssv3
        if cvssv3_score is not UNSET:
            field_dict["cvssv3_score"] = cvssv3_score
        if mitigation is not UNSET:
            field_dict["mitigation"] = mitigation
        if impact is not UNSET:
            field_dict["impact"] = impact
        if steps_to_reproduce is not UNSET:
            field_dict["steps_to_reproduce"] = steps_to_reproduce
        if severity_justification is not UNSET:
            field_dict["severity_justification"] = severity_justification
        if references is not UNSET:
            field_dict["references"] = references
        if active is not UNSET:
            field_dict["active"] = active
        if verified is not UNSET:
            field_dict["verified"] = verified
        if false_p is not UNSET:
            field_dict["false_p"] = false_p
        if duplicate is not UNSET:
            field_dict["duplicate"] = duplicate
        if out_of_scope is not UNSET:
            field_dict["out_of_scope"] = out_of_scope
        if risk_accepted is not UNSET:
            field_dict["risk_accepted"] = risk_accepted
        if under_review is not UNSET:
            field_dict["under_review"] = under_review
        if under_defect_review is not UNSET:
            field_dict["under_defect_review"] = under_defect_review
        if is_mitigated is not UNSET:
            field_dict["is_mitigated"] = is_mitigated
        if line is not UNSET:
            field_dict["line"] = line
        if file_path is not UNSET:
            field_dict["file_path"] = file_path
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if component_version is not UNSET:
            field_dict["component_version"] = component_version
        if static_finding is not UNSET:
            field_dict["static_finding"] = static_finding
        if dynamic_finding is not UNSET:
            field_dict["dynamic_finding"] = dynamic_finding
        if unique_id_from_tool is not UNSET:
            field_dict["unique_id_from_tool"] = unique_id_from_tool
        if vuln_id_from_tool is not UNSET:
            field_dict["vuln_id_from_tool"] = vuln_id_from_tool
        if sast_source_object is not UNSET:
            field_dict["sast_source_object"] = sast_source_object
        if sast_sink_object is not UNSET:
            field_dict["sast_sink_object"] = sast_sink_object
        if sast_source_line is not UNSET:
            field_dict["sast_source_line"] = sast_source_line
        if sast_source_file_path is not UNSET:
            field_dict["sast_source_file_path"] = sast_source_file_path
        if nb_occurences is not UNSET:
            field_dict["nb_occurences"] = nb_occurences
        if publish_date is not UNSET:
            field_dict["publish_date"] = publish_date
        if service is not UNSET:
            field_dict["service"] = service
        if planned_remediation_date is not UNSET:
            field_dict["planned_remediation_date"] = planned_remediation_date
        if planned_remediation_version is not UNSET:
            field_dict["planned_remediation_version"] = planned_remediation_version
        if effort_for_fixing is not UNSET:
            field_dict["effort_for_fixing"] = effort_for_fixing
        if review_requested_by is not UNSET:
            field_dict["review_requested_by"] = review_requested_by
        if defect_review_requested_by is not UNSET:
            field_dict["defect_review_requested_by"] = defect_review_requested_by
        if sonarqube_issue is not UNSET:
            field_dict["sonarqube_issue"] = sonarqube_issue
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        title = self.title if isinstance(self.title, Unset) else (None, str(self.title).encode(), "text/plain")
        severity = (
            self.severity if isinstance(self.severity, Unset) else (None, str(self.severity).encode(), "text/plain")
        )
        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        numerical_severity = (
            self.numerical_severity
            if isinstance(self.numerical_severity, Unset)
            else (None, str(self.numerical_severity).encode(), "text/plain")
        )
        tags: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = self.tags
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        push_to_jira = (
            self.push_to_jira
            if isinstance(self.push_to_jira, Unset)
            else (None, str(self.push_to_jira).encode(), "text/plain")
        )
        vulnerability_ids: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.vulnerability_ids, Unset):
            _temp_vulnerability_ids = []
            for vulnerability_ids_item_data in self.vulnerability_ids:
                vulnerability_ids_item = vulnerability_ids_item_data.to_dict()

                _temp_vulnerability_ids.append(vulnerability_ids_item)
            vulnerability_ids = (None, json.dumps(_temp_vulnerability_ids).encode(), "application/json")

        reporter = (
            self.reporter if isinstance(self.reporter, Unset) else (None, str(self.reporter).encode(), "text/plain")
        )
        date: Union[Unset, bytes] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat().encode()

        sla_start_date: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.sla_start_date, Unset):
            sla_start_date = self.sla_start_date.isoformat().encode() if self.sla_start_date else None

        cwe = self.cwe if isinstance(self.cwe, Unset) else (None, str(self.cwe).encode(), "text/plain")
        cvssv3 = self.cvssv3 if isinstance(self.cvssv3, Unset) else (None, str(self.cvssv3).encode(), "text/plain")
        cvssv3_score = (
            self.cvssv3_score
            if isinstance(self.cvssv3_score, Unset)
            else (None, str(self.cvssv3_score).encode(), "text/plain")
        )
        mitigation = (
            self.mitigation
            if isinstance(self.mitigation, Unset)
            else (None, str(self.mitigation).encode(), "text/plain")
        )
        impact = self.impact if isinstance(self.impact, Unset) else (None, str(self.impact).encode(), "text/plain")
        steps_to_reproduce = (
            self.steps_to_reproduce
            if isinstance(self.steps_to_reproduce, Unset)
            else (None, str(self.steps_to_reproduce).encode(), "text/plain")
        )
        severity_justification = (
            self.severity_justification
            if isinstance(self.severity_justification, Unset)
            else (None, str(self.severity_justification).encode(), "text/plain")
        )
        references = (
            self.references
            if isinstance(self.references, Unset)
            else (None, str(self.references).encode(), "text/plain")
        )
        active = self.active if isinstance(self.active, Unset) else (None, str(self.active).encode(), "text/plain")
        verified = (
            self.verified if isinstance(self.verified, Unset) else (None, str(self.verified).encode(), "text/plain")
        )
        false_p = self.false_p if isinstance(self.false_p, Unset) else (None, str(self.false_p).encode(), "text/plain")
        duplicate = (
            self.duplicate if isinstance(self.duplicate, Unset) else (None, str(self.duplicate).encode(), "text/plain")
        )
        out_of_scope = (
            self.out_of_scope
            if isinstance(self.out_of_scope, Unset)
            else (None, str(self.out_of_scope).encode(), "text/plain")
        )
        risk_accepted = (
            self.risk_accepted
            if isinstance(self.risk_accepted, Unset)
            else (None, str(self.risk_accepted).encode(), "text/plain")
        )
        under_review = (
            self.under_review
            if isinstance(self.under_review, Unset)
            else (None, str(self.under_review).encode(), "text/plain")
        )
        under_defect_review = (
            self.under_defect_review
            if isinstance(self.under_defect_review, Unset)
            else (None, str(self.under_defect_review).encode(), "text/plain")
        )
        is_mitigated = (
            self.is_mitigated
            if isinstance(self.is_mitigated, Unset)
            else (None, str(self.is_mitigated).encode(), "text/plain")
        )
        line = self.line if isinstance(self.line, Unset) else (None, str(self.line).encode(), "text/plain")
        file_path = (
            self.file_path if isinstance(self.file_path, Unset) else (None, str(self.file_path).encode(), "text/plain")
        )
        component_name = (
            self.component_name
            if isinstance(self.component_name, Unset)
            else (None, str(self.component_name).encode(), "text/plain")
        )
        component_version = (
            self.component_version
            if isinstance(self.component_version, Unset)
            else (None, str(self.component_version).encode(), "text/plain")
        )
        static_finding = (
            self.static_finding
            if isinstance(self.static_finding, Unset)
            else (None, str(self.static_finding).encode(), "text/plain")
        )
        dynamic_finding = (
            self.dynamic_finding
            if isinstance(self.dynamic_finding, Unset)
            else (None, str(self.dynamic_finding).encode(), "text/plain")
        )
        unique_id_from_tool = (
            self.unique_id_from_tool
            if isinstance(self.unique_id_from_tool, Unset)
            else (None, str(self.unique_id_from_tool).encode(), "text/plain")
        )
        vuln_id_from_tool = (
            self.vuln_id_from_tool
            if isinstance(self.vuln_id_from_tool, Unset)
            else (None, str(self.vuln_id_from_tool).encode(), "text/plain")
        )
        sast_source_object = (
            self.sast_source_object
            if isinstance(self.sast_source_object, Unset)
            else (None, str(self.sast_source_object).encode(), "text/plain")
        )
        sast_sink_object = (
            self.sast_sink_object
            if isinstance(self.sast_sink_object, Unset)
            else (None, str(self.sast_sink_object).encode(), "text/plain")
        )
        sast_source_line = (
            self.sast_source_line
            if isinstance(self.sast_source_line, Unset)
            else (None, str(self.sast_source_line).encode(), "text/plain")
        )
        sast_source_file_path = (
            self.sast_source_file_path
            if isinstance(self.sast_source_file_path, Unset)
            else (None, str(self.sast_source_file_path).encode(), "text/plain")
        )
        nb_occurences = (
            self.nb_occurences
            if isinstance(self.nb_occurences, Unset)
            else (None, str(self.nb_occurences).encode(), "text/plain")
        )
        publish_date: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.publish_date, Unset):
            publish_date = self.publish_date.isoformat().encode() if self.publish_date else None

        service = self.service if isinstance(self.service, Unset) else (None, str(self.service).encode(), "text/plain")
        planned_remediation_date: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.planned_remediation_date, Unset):
            planned_remediation_date = (
                self.planned_remediation_date.isoformat().encode() if self.planned_remediation_date else None
            )

        planned_remediation_version = (
            self.planned_remediation_version
            if isinstance(self.planned_remediation_version, Unset)
            else (None, str(self.planned_remediation_version).encode(), "text/plain")
        )
        effort_for_fixing = (
            self.effort_for_fixing
            if isinstance(self.effort_for_fixing, Unset)
            else (None, str(self.effort_for_fixing).encode(), "text/plain")
        )
        review_requested_by = (
            self.review_requested_by
            if isinstance(self.review_requested_by, Unset)
            else (None, str(self.review_requested_by).encode(), "text/plain")
        )
        defect_review_requested_by = (
            self.defect_review_requested_by
            if isinstance(self.defect_review_requested_by, Unset)
            else (None, str(self.defect_review_requested_by).encode(), "text/plain")
        )
        sonarqube_issue = (
            self.sonarqube_issue
            if isinstance(self.sonarqube_issue, Unset)
            else (None, str(self.sonarqube_issue).encode(), "text/plain")
        )
        reviewers: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.reviewers, Unset):
            _temp_reviewers = self.reviewers
            reviewers = (None, json.dumps(_temp_reviewers).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "title": title,
                "severity": severity,
                "description": description,
                "numerical_severity": numerical_severity,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if push_to_jira is not UNSET:
            field_dict["push_to_jira"] = push_to_jira
        if vulnerability_ids is not UNSET:
            field_dict["vulnerability_ids"] = vulnerability_ids
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if date is not UNSET:
            field_dict["date"] = date
        if sla_start_date is not UNSET:
            field_dict["sla_start_date"] = sla_start_date
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if cvssv3 is not UNSET:
            field_dict["cvssv3"] = cvssv3
        if cvssv3_score is not UNSET:
            field_dict["cvssv3_score"] = cvssv3_score
        if mitigation is not UNSET:
            field_dict["mitigation"] = mitigation
        if impact is not UNSET:
            field_dict["impact"] = impact
        if steps_to_reproduce is not UNSET:
            field_dict["steps_to_reproduce"] = steps_to_reproduce
        if severity_justification is not UNSET:
            field_dict["severity_justification"] = severity_justification
        if references is not UNSET:
            field_dict["references"] = references
        if active is not UNSET:
            field_dict["active"] = active
        if verified is not UNSET:
            field_dict["verified"] = verified
        if false_p is not UNSET:
            field_dict["false_p"] = false_p
        if duplicate is not UNSET:
            field_dict["duplicate"] = duplicate
        if out_of_scope is not UNSET:
            field_dict["out_of_scope"] = out_of_scope
        if risk_accepted is not UNSET:
            field_dict["risk_accepted"] = risk_accepted
        if under_review is not UNSET:
            field_dict["under_review"] = under_review
        if under_defect_review is not UNSET:
            field_dict["under_defect_review"] = under_defect_review
        if is_mitigated is not UNSET:
            field_dict["is_mitigated"] = is_mitigated
        if line is not UNSET:
            field_dict["line"] = line
        if file_path is not UNSET:
            field_dict["file_path"] = file_path
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if component_version is not UNSET:
            field_dict["component_version"] = component_version
        if static_finding is not UNSET:
            field_dict["static_finding"] = static_finding
        if dynamic_finding is not UNSET:
            field_dict["dynamic_finding"] = dynamic_finding
        if unique_id_from_tool is not UNSET:
            field_dict["unique_id_from_tool"] = unique_id_from_tool
        if vuln_id_from_tool is not UNSET:
            field_dict["vuln_id_from_tool"] = vuln_id_from_tool
        if sast_source_object is not UNSET:
            field_dict["sast_source_object"] = sast_source_object
        if sast_sink_object is not UNSET:
            field_dict["sast_sink_object"] = sast_sink_object
        if sast_source_line is not UNSET:
            field_dict["sast_source_line"] = sast_source_line
        if sast_source_file_path is not UNSET:
            field_dict["sast_source_file_path"] = sast_source_file_path
        if nb_occurences is not UNSET:
            field_dict["nb_occurences"] = nb_occurences
        if publish_date is not UNSET:
            field_dict["publish_date"] = publish_date
        if service is not UNSET:
            field_dict["service"] = service
        if planned_remediation_date is not UNSET:
            field_dict["planned_remediation_date"] = planned_remediation_date
        if planned_remediation_version is not UNSET:
            field_dict["planned_remediation_version"] = planned_remediation_version
        if effort_for_fixing is not UNSET:
            field_dict["effort_for_fixing"] = effort_for_fixing
        if review_requested_by is not UNSET:
            field_dict["review_requested_by"] = review_requested_by
        if defect_review_requested_by is not UNSET:
            field_dict["defect_review_requested_by"] = defect_review_requested_by
        if sonarqube_issue is not UNSET:
            field_dict["sonarqube_issue"] = sonarqube_issue
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.vulnerability_id_request import VulnerabilityIdRequest

        d = src_dict.copy()
        title = d.pop("title")

        severity = d.pop("severity")

        description = d.pop("description")

        numerical_severity = d.pop("numerical_severity")

        tags = cast(List[str], d.pop("tags", UNSET))

        push_to_jira = d.pop("push_to_jira", UNSET)

        vulnerability_ids = []
        _vulnerability_ids = d.pop("vulnerability_ids", UNSET)
        for vulnerability_ids_item_data in _vulnerability_ids or []:
            vulnerability_ids_item = VulnerabilityIdRequest.from_dict(vulnerability_ids_item_data)

            vulnerability_ids.append(vulnerability_ids_item)

        reporter = d.pop("reporter", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        _sla_start_date = d.pop("sla_start_date", UNSET)
        sla_start_date: Union[Unset, None, datetime.date]
        if _sla_start_date is None:
            sla_start_date = None
        elif isinstance(_sla_start_date, Unset):
            sla_start_date = UNSET
        else:
            sla_start_date = isoparse(_sla_start_date).date()

        cwe = d.pop("cwe", UNSET)

        cvssv3 = d.pop("cvssv3", UNSET)

        cvssv3_score = d.pop("cvssv3_score", UNSET)

        mitigation = d.pop("mitigation", UNSET)

        impact = d.pop("impact", UNSET)

        steps_to_reproduce = d.pop("steps_to_reproduce", UNSET)

        severity_justification = d.pop("severity_justification", UNSET)

        references = d.pop("references", UNSET)

        active = d.pop("active", UNSET)

        verified = d.pop("verified", UNSET)

        false_p = d.pop("false_p", UNSET)

        duplicate = d.pop("duplicate", UNSET)

        out_of_scope = d.pop("out_of_scope", UNSET)

        risk_accepted = d.pop("risk_accepted", UNSET)

        under_review = d.pop("under_review", UNSET)

        under_defect_review = d.pop("under_defect_review", UNSET)

        is_mitigated = d.pop("is_mitigated", UNSET)

        line = d.pop("line", UNSET)

        file_path = d.pop("file_path", UNSET)

        component_name = d.pop("component_name", UNSET)

        component_version = d.pop("component_version", UNSET)

        static_finding = d.pop("static_finding", UNSET)

        dynamic_finding = d.pop("dynamic_finding", UNSET)

        unique_id_from_tool = d.pop("unique_id_from_tool", UNSET)

        vuln_id_from_tool = d.pop("vuln_id_from_tool", UNSET)

        sast_source_object = d.pop("sast_source_object", UNSET)

        sast_sink_object = d.pop("sast_sink_object", UNSET)

        sast_source_line = d.pop("sast_source_line", UNSET)

        sast_source_file_path = d.pop("sast_source_file_path", UNSET)

        nb_occurences = d.pop("nb_occurences", UNSET)

        _publish_date = d.pop("publish_date", UNSET)
        publish_date: Union[Unset, None, datetime.date]
        if _publish_date is None:
            publish_date = None
        elif isinstance(_publish_date, Unset):
            publish_date = UNSET
        else:
            publish_date = isoparse(_publish_date).date()

        service = d.pop("service", UNSET)

        _planned_remediation_date = d.pop("planned_remediation_date", UNSET)
        planned_remediation_date: Union[Unset, None, datetime.date]
        if _planned_remediation_date is None:
            planned_remediation_date = None
        elif isinstance(_planned_remediation_date, Unset):
            planned_remediation_date = UNSET
        else:
            planned_remediation_date = isoparse(_planned_remediation_date).date()

        planned_remediation_version = d.pop("planned_remediation_version", UNSET)

        effort_for_fixing = d.pop("effort_for_fixing", UNSET)

        review_requested_by = d.pop("review_requested_by", UNSET)

        defect_review_requested_by = d.pop("defect_review_requested_by", UNSET)

        sonarqube_issue = d.pop("sonarqube_issue", UNSET)

        reviewers = cast(List[int], d.pop("reviewers", UNSET))

        finding_request = cls(
            title=title,
            severity=severity,
            description=description,
            numerical_severity=numerical_severity,
            tags=tags,
            push_to_jira=push_to_jira,
            vulnerability_ids=vulnerability_ids,
            reporter=reporter,
            date=date,
            sla_start_date=sla_start_date,
            cwe=cwe,
            cvssv3=cvssv3,
            cvssv3_score=cvssv3_score,
            mitigation=mitigation,
            impact=impact,
            steps_to_reproduce=steps_to_reproduce,
            severity_justification=severity_justification,
            references=references,
            active=active,
            verified=verified,
            false_p=false_p,
            duplicate=duplicate,
            out_of_scope=out_of_scope,
            risk_accepted=risk_accepted,
            under_review=under_review,
            under_defect_review=under_defect_review,
            is_mitigated=is_mitigated,
            line=line,
            file_path=file_path,
            component_name=component_name,
            component_version=component_version,
            static_finding=static_finding,
            dynamic_finding=dynamic_finding,
            unique_id_from_tool=unique_id_from_tool,
            vuln_id_from_tool=vuln_id_from_tool,
            sast_source_object=sast_source_object,
            sast_sink_object=sast_sink_object,
            sast_source_line=sast_source_line,
            sast_source_file_path=sast_source_file_path,
            nb_occurences=nb_occurences,
            publish_date=publish_date,
            service=service,
            planned_remediation_date=planned_remediation_date,
            planned_remediation_version=planned_remediation_version,
            effort_for_fixing=effort_for_fixing,
            review_requested_by=review_requested_by,
            defect_review_requested_by=defect_review_requested_by,
            sonarqube_issue=sonarqube_issue,
            reviewers=reviewers,
        )

        finding_request.additional_properties = d
        return finding_request

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

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vulnerability_id import VulnerabilityId


T = TypeVar("T", bound="FindingCreate")


@_attrs_define
class FindingCreate:
    """
    Attributes:
        id (int):
        notes (List[Optional[int]]):
        test (int):
        found_by (List[int]):
        title (str): A short description of the flaw.
        severity (str): The severity level of this flaw (Critical, High, Medium, Low, Informational).
        description (str): Longer more descriptive information about the flaw.
        active (bool): Denotes if this flaw is active or not.
        verified (bool): Denotes if this flaw has been manually verified by the tester.
        numerical_severity (str): The numerical representation of the severity (S0, S1, S2, S3, S4).
        endpoints (List[int]): The hosts within the product that are susceptible to this flaw. + The status of the
            endpoint associated with this flaw (Vulnerable, Mitigated, ...).
        files (List[int]): Files(s) related to the flaw.
        thread_id (Union[Unset, int]):
        url (Union[Unset, None, str]):
        tags (Union[Unset, List[str]]):
        push_to_jira (Union[Unset, bool]):
        vulnerability_ids (Union[Unset, List['VulnerabilityId']]):
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
        false_p (Union[Unset, bool]): Denotes if this flaw has been deemed a false positive by the tester.
        duplicate (Union[Unset, bool]): Denotes if this flaw is a duplicate of other flaws reported.
        out_of_scope (Union[Unset, bool]): Denotes if this flaw falls outside the scope of the test and/or engagement.
        risk_accepted (Union[Unset, bool]): Denotes if this finding has been marked as an accepted risk.
        under_review (Union[Unset, bool]): Denotes is this flaw is currently being reviewed.
        last_status_update (Optional[datetime.datetime]): Timestamp of latest status update (change in status related
            fields).
        under_defect_review (Union[Unset, bool]): Denotes if this finding is under defect review.
        is_mitigated (Union[Unset, bool]): Denotes if this flaw has been fixed.
        mitigated (Optional[datetime.datetime]): Denotes if this flaw has been fixed by storing the date it was fixed.
        last_reviewed (Optional[datetime.datetime]): Provides the date the flaw was last 'touched' by a tester.
        param (Optional[str]): Parameter used to trigger the issue (DAST).
        payload (Optional[str]): Payload used to attack the service / application and trigger the bug / problem.
        hash_code (Optional[str]): A hash over a configurable set of fields that is used for findings deduplication.
        line (Union[Unset, None, int]): Source line number of the attack vector.
        file_path (Union[Unset, None, str]): Identified file(s) containing the flaw.
        component_name (Union[Unset, None, str]): Name of the affected component (library name, part of a system, ...).
        component_version (Union[Unset, None, str]): Version of the affected component.
        static_finding (Union[Unset, bool]): Flaw has been detected from a Static Application Security Testing tool
            (SAST).
        dynamic_finding (Union[Unset, bool]): Flaw has been detected from a Dynamic Application Security Testing tool
            (DAST).
        created (Optional[datetime.datetime]): The date the finding was created inside DefectDojo.
        scanner_confidence (Optional[int]): Confidence level of vulnerability which is supplied by the scanner.
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
        duplicate_finding (Optional[int]): Link to the original finding if this finding is a duplicate.
        review_requested_by (Union[Unset, None, int]): Documents who requested a review for this finding.
        defect_review_requested_by (Union[Unset, None, int]): Documents who requested a defect review for this flaw.
        mitigated_by (Optional[int]): Documents who has marked this flaw as fixed.
        last_reviewed_by (Optional[int]): Provides the person who last reviewed the flaw.
        sonarqube_issue (Union[Unset, None, int]): The SonarQube issue associated with this finding.
        reviewers (Union[Unset, List[int]]): Documents who reviewed the flaw.
    """

    id: int
    notes: List[Optional[int]]
    test: int
    found_by: List[int]
    title: str
    severity: str
    description: str
    active: bool
    verified: bool
    numerical_severity: str
    endpoints: List[int]
    files: List[int]
    last_status_update: Optional[datetime.datetime]
    mitigated: Optional[datetime.datetime]
    last_reviewed: Optional[datetime.datetime]
    param: Optional[str]
    payload: Optional[str]
    hash_code: Optional[str]
    created: Optional[datetime.datetime]
    scanner_confidence: Optional[int]
    duplicate_finding: Optional[int]
    mitigated_by: Optional[int]
    last_reviewed_by: Optional[int]
    thread_id: Union[Unset, int] = 0
    url: Union[Unset, None, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    push_to_jira: Union[Unset, bool] = False
    vulnerability_ids: Union[Unset, List["VulnerabilityId"]] = UNSET
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
        id = self.id
        notes = self.notes

        test = self.test
        found_by = self.found_by

        title = self.title
        severity = self.severity
        description = self.description
        active = self.active
        verified = self.verified
        numerical_severity = self.numerical_severity
        endpoints = self.endpoints

        files = self.files

        thread_id = self.thread_id
        url = self.url
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
        false_p = self.false_p
        duplicate = self.duplicate
        out_of_scope = self.out_of_scope
        risk_accepted = self.risk_accepted
        under_review = self.under_review
        last_status_update = self.last_status_update.isoformat() if self.last_status_update else None

        under_defect_review = self.under_defect_review
        is_mitigated = self.is_mitigated
        mitigated = self.mitigated.isoformat() if self.mitigated else None

        last_reviewed = self.last_reviewed.isoformat() if self.last_reviewed else None

        param = self.param
        payload = self.payload
        hash_code = self.hash_code
        line = self.line
        file_path = self.file_path
        component_name = self.component_name
        component_version = self.component_version
        static_finding = self.static_finding
        dynamic_finding = self.dynamic_finding
        created = self.created.isoformat() if self.created else None

        scanner_confidence = self.scanner_confidence
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
        duplicate_finding = self.duplicate_finding
        review_requested_by = self.review_requested_by
        defect_review_requested_by = self.defect_review_requested_by
        mitigated_by = self.mitigated_by
        last_reviewed_by = self.last_reviewed_by
        sonarqube_issue = self.sonarqube_issue
        reviewers: Union[Unset, List[int]] = UNSET
        if not isinstance(self.reviewers, Unset):
            reviewers = self.reviewers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "notes": notes,
                "test": test,
                "found_by": found_by,
                "title": title,
                "severity": severity,
                "description": description,
                "active": active,
                "verified": verified,
                "numerical_severity": numerical_severity,
                "endpoints": endpoints,
                "files": files,
                "last_status_update": last_status_update,
                "mitigated": mitigated,
                "last_reviewed": last_reviewed,
                "param": param,
                "payload": payload,
                "hash_code": hash_code,
                "created": created,
                "scanner_confidence": scanner_confidence,
                "duplicate_finding": duplicate_finding,
                "mitigated_by": mitigated_by,
                "last_reviewed_by": last_reviewed_by,
            }
        )
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if url is not UNSET:
            field_dict["url"] = url
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
        from ..models.vulnerability_id import VulnerabilityId

        d = src_dict.copy()
        id = d.pop("id")

        notes = cast(List[Optional[int]], d.pop("notes"))

        test = d.pop("test")

        found_by = cast(List[int], d.pop("found_by"))

        title = d.pop("title")

        severity = d.pop("severity")

        description = d.pop("description")

        active = d.pop("active")

        verified = d.pop("verified")

        numerical_severity = d.pop("numerical_severity")

        endpoints = cast(List[int], d.pop("endpoints"))

        files = cast(List[int], d.pop("files"))

        thread_id = d.pop("thread_id", UNSET)

        url = d.pop("url", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        push_to_jira = d.pop("push_to_jira", UNSET)

        vulnerability_ids = []
        _vulnerability_ids = d.pop("vulnerability_ids", UNSET)
        for vulnerability_ids_item_data in _vulnerability_ids or []:
            vulnerability_ids_item = VulnerabilityId.from_dict(vulnerability_ids_item_data)

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

        false_p = d.pop("false_p", UNSET)

        duplicate = d.pop("duplicate", UNSET)

        out_of_scope = d.pop("out_of_scope", UNSET)

        risk_accepted = d.pop("risk_accepted", UNSET)

        under_review = d.pop("under_review", UNSET)

        _last_status_update = d.pop("last_status_update")
        last_status_update: Optional[datetime.datetime]
        if _last_status_update is None:
            last_status_update = None
        else:
            last_status_update = isoparse(_last_status_update)

        under_defect_review = d.pop("under_defect_review", UNSET)

        is_mitigated = d.pop("is_mitigated", UNSET)

        _mitigated = d.pop("mitigated")
        mitigated: Optional[datetime.datetime]
        if _mitigated is None:
            mitigated = None
        else:
            mitigated = isoparse(_mitigated)

        _last_reviewed = d.pop("last_reviewed")
        last_reviewed: Optional[datetime.datetime]
        if _last_reviewed is None:
            last_reviewed = None
        else:
            last_reviewed = isoparse(_last_reviewed)

        param = d.pop("param")

        payload = d.pop("payload")

        hash_code = d.pop("hash_code")

        line = d.pop("line", UNSET)

        file_path = d.pop("file_path", UNSET)

        component_name = d.pop("component_name", UNSET)

        component_version = d.pop("component_version", UNSET)

        static_finding = d.pop("static_finding", UNSET)

        dynamic_finding = d.pop("dynamic_finding", UNSET)

        _created = d.pop("created")
        created: Optional[datetime.datetime]
        if _created is None:
            created = None
        else:
            created = isoparse(_created)

        scanner_confidence = d.pop("scanner_confidence")

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

        duplicate_finding = d.pop("duplicate_finding")

        review_requested_by = d.pop("review_requested_by", UNSET)

        defect_review_requested_by = d.pop("defect_review_requested_by", UNSET)

        mitigated_by = d.pop("mitigated_by")

        last_reviewed_by = d.pop("last_reviewed_by")

        sonarqube_issue = d.pop("sonarqube_issue", UNSET)

        reviewers = cast(List[int], d.pop("reviewers", UNSET))

        finding_create = cls(
            id=id,
            notes=notes,
            test=test,
            found_by=found_by,
            title=title,
            severity=severity,
            description=description,
            active=active,
            verified=verified,
            numerical_severity=numerical_severity,
            endpoints=endpoints,
            files=files,
            thread_id=thread_id,
            url=url,
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
            false_p=false_p,
            duplicate=duplicate,
            out_of_scope=out_of_scope,
            risk_accepted=risk_accepted,
            under_review=under_review,
            last_status_update=last_status_update,
            under_defect_review=under_defect_review,
            is_mitigated=is_mitigated,
            mitigated=mitigated,
            last_reviewed=last_reviewed,
            param=param,
            payload=payload,
            hash_code=hash_code,
            line=line,
            file_path=file_path,
            component_name=component_name,
            component_version=component_version,
            static_finding=static_finding,
            dynamic_finding=dynamic_finding,
            created=created,
            scanner_confidence=scanner_confidence,
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
            duplicate_finding=duplicate_finding,
            review_requested_by=review_requested_by,
            defect_review_requested_by=defect_review_requested_by,
            mitigated_by=mitigated_by,
            last_reviewed_by=last_reviewed_by,
            sonarqube_issue=sonarqube_issue,
            reviewers=reviewers,
        )

        finding_create.additional_properties = d
        return finding_create

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

import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.findings_list_created import FindingsListCreated
from ...models.findings_list_date import FindingsListDate
from ...models.findings_list_jira_creation import FindingsListJiraCreation
from ...models.findings_list_jira_last_update import FindingsListJiraLastUpdate
from ...models.findings_list_last_reviewed import FindingsListLastReviewed
from ...models.findings_list_mitigated import FindingsListMitigated
from ...models.findings_list_o_item import FindingsListOItem
from ...models.findings_list_prefetch_item import FindingsListPrefetchItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active: Union[Unset, None, bool] = UNSET,
    component_name: Union[Unset, None, str] = UNSET,
    component_version: Union[Unset, None, str] = UNSET,
    created: Union[Unset, None, FindingsListCreated] = UNSET,
    cvssv3: Union[Unset, None, str] = UNSET,
    cvssv3_score: Union[Unset, None, float] = UNSET,
    cwe: Union[Unset, None, List[int]] = UNSET,
    date: Union[Unset, None, FindingsListDate] = UNSET,
    defect_review_requested_by: Union[Unset, None, List[int]] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    duplicate: Union[Unset, None, bool] = UNSET,
    duplicate_finding: Union[Unset, None, int] = UNSET,
    dynamic_finding: Union[Unset, None, bool] = UNSET,
    effort_for_fixing: Union[Unset, None, str] = UNSET,
    endpoints: Union[Unset, None, List[int]] = UNSET,
    false_p: Union[Unset, None, bool] = UNSET,
    file_path: Union[Unset, None, str] = UNSET,
    finding_group: Union[Unset, None, List[float]] = UNSET,
    found_by: Union[Unset, None, List[int]] = UNSET,
    has_jira: Union[Unset, None, bool] = UNSET,
    hash_code: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, List[int]] = UNSET,
    impact: Union[Unset, None, str] = UNSET,
    inherited_tags: Union[Unset, None, List[List[int]]] = UNSET,
    is_mitigated: Union[Unset, None, bool] = UNSET,
    jira_change: Union[Unset, None, FindingsListJiraLastUpdate] = UNSET,
    jira_creation: Union[Unset, None, FindingsListJiraCreation] = UNSET,
    last_reviewed: Union[Unset, None, FindingsListLastReviewed] = UNSET,
    last_reviewed_by: Union[Unset, None, List[int]] = UNSET,
    last_status_update: Union[Unset, None, datetime.datetime] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    mitigated: Union[Unset, None, FindingsListMitigated] = UNSET,
    mitigated_by: Union[Unset, None, List[int]] = UNSET,
    mitigation: Union[Unset, None, str] = UNSET,
    nb_occurences: Union[Unset, None, List[int]] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    not_test_engagement_product_tags: Union[Unset, None, List[str]] = UNSET,
    not_test_engagement_tags: Union[Unset, None, List[str]] = UNSET,
    not_test_tags: Union[Unset, None, List[str]] = UNSET,
    numerical_severity: Union[Unset, None, str] = UNSET,
    o: Union[Unset, None, List[FindingsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    out_of_scope: Union[Unset, None, bool] = UNSET,
    param: Union[Unset, None, str] = UNSET,
    payload: Union[Unset, None, str] = UNSET,
    planned_remediation_date: Union[Unset, None, datetime.date] = UNSET,
    planned_remediation_version: Union[Unset, None, str] = UNSET,
    prefetch: Union[Unset, None, List[FindingsListPrefetchItem]] = UNSET,
    product_name: Union[Unset, None, str] = UNSET,
    product_name_contains: Union[Unset, None, str] = UNSET,
    publish_date: Union[Unset, None, datetime.date] = UNSET,
    references: Union[Unset, None, str] = UNSET,
    related_fields: Union[Unset, None, bool] = UNSET,
    reporter: Union[Unset, None, List[int]] = UNSET,
    review_requested_by: Union[Unset, None, List[int]] = UNSET,
    reviewers: Union[Unset, None, List[int]] = UNSET,
    risk_acceptance: Union[Unset, None, float] = UNSET,
    risk_accepted: Union[Unset, None, bool] = UNSET,
    sast_sink_object: Union[Unset, None, str] = UNSET,
    sast_source_file_path: Union[Unset, None, str] = UNSET,
    sast_source_line: Union[Unset, None, List[int]] = UNSET,
    sast_source_object: Union[Unset, None, str] = UNSET,
    scanner_confidence: Union[Unset, None, List[int]] = UNSET,
    service: Union[Unset, None, str] = UNSET,
    severity: Union[Unset, None, str] = UNSET,
    severity_justification: Union[Unset, None, str] = UNSET,
    sla_start_date: Union[Unset, None, datetime.date] = UNSET,
    sonarqube_issue: Union[Unset, None, List[int]] = UNSET,
    static_finding: Union[Unset, None, bool] = UNSET,
    steps_to_reproduce: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    test: Union[Unset, None, int] = UNSET,
    test_engagement: Union[Unset, None, List[int]] = UNSET,
    test_engagement_product: Union[Unset, None, List[int]] = UNSET,
    test_engagement_product_prod_type: Union[Unset, None, List[int]] = UNSET,
    test_engagement_product_tags: Union[Unset, None, List[str]] = UNSET,
    test_engagement_tags: Union[Unset, None, List[str]] = UNSET,
    test_tags: Union[Unset, None, List[str]] = UNSET,
    test_test_type: Union[Unset, None, List[int]] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    under_defect_review: Union[Unset, None, bool] = UNSET,
    under_review: Union[Unset, None, bool] = UNSET,
    unique_id_from_tool: Union[Unset, None, str] = UNSET,
    verified: Union[Unset, None, bool] = UNSET,
    vuln_id_from_tool: Union[Unset, None, str] = UNSET,
    vulnerability_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["active"] = active

    params["component_name"] = component_name

    params["component_version"] = component_version

    json_created: Union[Unset, None, int] = UNSET
    if not isinstance(created, Unset):
        json_created = created.value if created else None

    params["created"] = json_created

    params["cvssv3"] = cvssv3

    params["cvssv3_score"] = cvssv3_score

    json_cwe: Union[Unset, None, List[int]] = UNSET
    if not isinstance(cwe, Unset):
        if cwe is None:
            json_cwe = None
        else:
            json_cwe = cwe

    params["cwe"] = json_cwe

    json_date: Union[Unset, None, int] = UNSET
    if not isinstance(date, Unset):
        json_date = date.value if date else None

    params["date"] = json_date

    json_defect_review_requested_by: Union[Unset, None, List[int]] = UNSET
    if not isinstance(defect_review_requested_by, Unset):
        if defect_review_requested_by is None:
            json_defect_review_requested_by = None
        else:
            json_defect_review_requested_by = defect_review_requested_by

    params["defect_review_requested_by"] = json_defect_review_requested_by

    params["description"] = description

    params["duplicate"] = duplicate

    params["duplicate_finding"] = duplicate_finding

    params["dynamic_finding"] = dynamic_finding

    params["effort_for_fixing"] = effort_for_fixing

    json_endpoints: Union[Unset, None, List[int]] = UNSET
    if not isinstance(endpoints, Unset):
        if endpoints is None:
            json_endpoints = None
        else:
            json_endpoints = endpoints

    params["endpoints"] = json_endpoints

    params["false_p"] = false_p

    params["file_path"] = file_path

    json_finding_group: Union[Unset, None, List[float]] = UNSET
    if not isinstance(finding_group, Unset):
        if finding_group is None:
            json_finding_group = None
        else:
            json_finding_group = finding_group

    params["finding_group"] = json_finding_group

    json_found_by: Union[Unset, None, List[int]] = UNSET
    if not isinstance(found_by, Unset):
        if found_by is None:
            json_found_by = None
        else:
            json_found_by = found_by

    params["found_by"] = json_found_by

    params["has_jira"] = has_jira

    params["hash_code"] = hash_code

    json_id: Union[Unset, None, List[int]] = UNSET
    if not isinstance(id, Unset):
        if id is None:
            json_id = None
        else:
            json_id = id

    params["id"] = json_id

    params["impact"] = impact

    json_inherited_tags: Union[Unset, None, List[List[int]]] = UNSET
    if not isinstance(inherited_tags, Unset):
        if inherited_tags is None:
            json_inherited_tags = None
        else:
            json_inherited_tags = []
            for inherited_tags_item_data in inherited_tags:
                inherited_tags_item = inherited_tags_item_data

                json_inherited_tags.append(inherited_tags_item)

    params["inherited_tags"] = json_inherited_tags

    params["is_mitigated"] = is_mitigated

    json_jira_change: Union[Unset, None, int] = UNSET
    if not isinstance(jira_change, Unset):
        json_jira_change = jira_change.value if jira_change else None

    params["jira_change"] = json_jira_change

    json_jira_creation: Union[Unset, None, int] = UNSET
    if not isinstance(jira_creation, Unset):
        json_jira_creation = jira_creation.value if jira_creation else None

    params["jira_creation"] = json_jira_creation

    json_last_reviewed: Union[Unset, None, int] = UNSET
    if not isinstance(last_reviewed, Unset):
        json_last_reviewed = last_reviewed.value if last_reviewed else None

    params["last_reviewed"] = json_last_reviewed

    json_last_reviewed_by: Union[Unset, None, List[int]] = UNSET
    if not isinstance(last_reviewed_by, Unset):
        if last_reviewed_by is None:
            json_last_reviewed_by = None
        else:
            json_last_reviewed_by = last_reviewed_by

    params["last_reviewed_by"] = json_last_reviewed_by

    json_last_status_update: Union[Unset, None, str] = UNSET
    if not isinstance(last_status_update, Unset):
        json_last_status_update = last_status_update.isoformat() if last_status_update else None

    params["last_status_update"] = json_last_status_update

    params["limit"] = limit

    json_mitigated: Union[Unset, None, int] = UNSET
    if not isinstance(mitigated, Unset):
        json_mitigated = mitigated.value if mitigated else None

    params["mitigated"] = json_mitigated

    json_mitigated_by: Union[Unset, None, List[int]] = UNSET
    if not isinstance(mitigated_by, Unset):
        if mitigated_by is None:
            json_mitigated_by = None
        else:
            json_mitigated_by = mitigated_by

    params["mitigated_by"] = json_mitigated_by

    params["mitigation"] = mitigation

    json_nb_occurences: Union[Unset, None, List[int]] = UNSET
    if not isinstance(nb_occurences, Unset):
        if nb_occurences is None:
            json_nb_occurences = None
        else:
            json_nb_occurences = nb_occurences

    params["nb_occurences"] = json_nb_occurences

    params["not_tag"] = not_tag

    json_not_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(not_tags, Unset):
        if not_tags is None:
            json_not_tags = None
        else:
            json_not_tags = not_tags

    params["not_tags"] = json_not_tags

    json_not_test_engagement_product_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(not_test_engagement_product_tags, Unset):
        if not_test_engagement_product_tags is None:
            json_not_test_engagement_product_tags = None
        else:
            json_not_test_engagement_product_tags = not_test_engagement_product_tags

    params["not_test__engagement__product__tags"] = json_not_test_engagement_product_tags

    json_not_test_engagement_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(not_test_engagement_tags, Unset):
        if not_test_engagement_tags is None:
            json_not_test_engagement_tags = None
        else:
            json_not_test_engagement_tags = not_test_engagement_tags

    params["not_test__engagement__tags"] = json_not_test_engagement_tags

    json_not_test_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(not_test_tags, Unset):
        if not_test_tags is None:
            json_not_test_tags = None
        else:
            json_not_test_tags = not_test_tags

    params["not_test__tags"] = json_not_test_tags

    params["numerical_severity"] = numerical_severity

    json_o: Union[Unset, None, List[str]] = UNSET
    if not isinstance(o, Unset):
        if o is None:
            json_o = None
        else:
            json_o = []
            for o_item_data in o:
                o_item = o_item_data.value

                json_o.append(o_item)

    params["o"] = json_o

    params["offset"] = offset

    params["out_of_scope"] = out_of_scope

    params["param"] = param

    params["payload"] = payload

    json_planned_remediation_date: Union[Unset, None, str] = UNSET
    if not isinstance(planned_remediation_date, Unset):
        json_planned_remediation_date = planned_remediation_date.isoformat() if planned_remediation_date else None

    params["planned_remediation_date"] = json_planned_remediation_date

    params["planned_remediation_version"] = planned_remediation_version

    json_prefetch: Union[Unset, None, List[str]] = UNSET
    if not isinstance(prefetch, Unset):
        if prefetch is None:
            json_prefetch = None
        else:
            json_prefetch = []
            for prefetch_item_data in prefetch:
                prefetch_item = prefetch_item_data.value

                json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    params["product_name"] = product_name

    params["product_name_contains"] = product_name_contains

    json_publish_date: Union[Unset, None, str] = UNSET
    if not isinstance(publish_date, Unset):
        json_publish_date = publish_date.isoformat() if publish_date else None

    params["publish_date"] = json_publish_date

    params["references"] = references

    params["related_fields"] = related_fields

    json_reporter: Union[Unset, None, List[int]] = UNSET
    if not isinstance(reporter, Unset):
        if reporter is None:
            json_reporter = None
        else:
            json_reporter = reporter

    params["reporter"] = json_reporter

    json_review_requested_by: Union[Unset, None, List[int]] = UNSET
    if not isinstance(review_requested_by, Unset):
        if review_requested_by is None:
            json_review_requested_by = None
        else:
            json_review_requested_by = review_requested_by

    params["review_requested_by"] = json_review_requested_by

    json_reviewers: Union[Unset, None, List[int]] = UNSET
    if not isinstance(reviewers, Unset):
        if reviewers is None:
            json_reviewers = None
        else:
            json_reviewers = reviewers

    params["reviewers"] = json_reviewers

    params["risk_acceptance"] = risk_acceptance

    params["risk_accepted"] = risk_accepted

    params["sast_sink_object"] = sast_sink_object

    params["sast_source_file_path"] = sast_source_file_path

    json_sast_source_line: Union[Unset, None, List[int]] = UNSET
    if not isinstance(sast_source_line, Unset):
        if sast_source_line is None:
            json_sast_source_line = None
        else:
            json_sast_source_line = sast_source_line

    params["sast_source_line"] = json_sast_source_line

    params["sast_source_object"] = sast_source_object

    json_scanner_confidence: Union[Unset, None, List[int]] = UNSET
    if not isinstance(scanner_confidence, Unset):
        if scanner_confidence is None:
            json_scanner_confidence = None
        else:
            json_scanner_confidence = scanner_confidence

    params["scanner_confidence"] = json_scanner_confidence

    params["service"] = service

    params["severity"] = severity

    params["severity_justification"] = severity_justification

    json_sla_start_date: Union[Unset, None, str] = UNSET
    if not isinstance(sla_start_date, Unset):
        json_sla_start_date = sla_start_date.isoformat() if sla_start_date else None

    params["sla_start_date"] = json_sla_start_date

    json_sonarqube_issue: Union[Unset, None, List[int]] = UNSET
    if not isinstance(sonarqube_issue, Unset):
        if sonarqube_issue is None:
            json_sonarqube_issue = None
        else:
            json_sonarqube_issue = sonarqube_issue

    params["sonarqube_issue"] = json_sonarqube_issue

    params["static_finding"] = static_finding

    params["steps_to_reproduce"] = steps_to_reproduce

    params["tag"] = tag

    json_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(tags, Unset):
        if tags is None:
            json_tags = None
        else:
            json_tags = tags

    params["tags"] = json_tags

    params["test"] = test

    json_test_engagement: Union[Unset, None, List[int]] = UNSET
    if not isinstance(test_engagement, Unset):
        if test_engagement is None:
            json_test_engagement = None
        else:
            json_test_engagement = test_engagement

    params["test__engagement"] = json_test_engagement

    json_test_engagement_product: Union[Unset, None, List[int]] = UNSET
    if not isinstance(test_engagement_product, Unset):
        if test_engagement_product is None:
            json_test_engagement_product = None
        else:
            json_test_engagement_product = test_engagement_product

    params["test__engagement__product"] = json_test_engagement_product

    json_test_engagement_product_prod_type: Union[Unset, None, List[int]] = UNSET
    if not isinstance(test_engagement_product_prod_type, Unset):
        if test_engagement_product_prod_type is None:
            json_test_engagement_product_prod_type = None
        else:
            json_test_engagement_product_prod_type = test_engagement_product_prod_type

    params["test__engagement__product__prod_type"] = json_test_engagement_product_prod_type

    json_test_engagement_product_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(test_engagement_product_tags, Unset):
        if test_engagement_product_tags is None:
            json_test_engagement_product_tags = None
        else:
            json_test_engagement_product_tags = test_engagement_product_tags

    params["test__engagement__product__tags"] = json_test_engagement_product_tags

    json_test_engagement_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(test_engagement_tags, Unset):
        if test_engagement_tags is None:
            json_test_engagement_tags = None
        else:
            json_test_engagement_tags = test_engagement_tags

    params["test__engagement__tags"] = json_test_engagement_tags

    json_test_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(test_tags, Unset):
        if test_tags is None:
            json_test_tags = None
        else:
            json_test_tags = test_tags

    params["test__tags"] = json_test_tags

    json_test_test_type: Union[Unset, None, List[int]] = UNSET
    if not isinstance(test_test_type, Unset):
        if test_test_type is None:
            json_test_test_type = None
        else:
            json_test_test_type = test_test_type

    params["test__test_type"] = json_test_test_type

    params["title"] = title

    params["under_defect_review"] = under_defect_review

    params["under_review"] = under_review

    params["unique_id_from_tool"] = unique_id_from_tool

    params["verified"] = verified

    params["vuln_id_from_tool"] = vuln_id_from_tool

    params["vulnerability_id"] = vulnerability_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/findings/",
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    active: Union[Unset, None, bool] = UNSET,
    component_name: Union[Unset, None, str] = UNSET,
    component_version: Union[Unset, None, str] = UNSET,
    created: Union[Unset, None, FindingsListCreated] = UNSET,
    cvssv3: Union[Unset, None, str] = UNSET,
    cvssv3_score: Union[Unset, None, float] = UNSET,
    cwe: Union[Unset, None, List[int]] = UNSET,
    date: Union[Unset, None, FindingsListDate] = UNSET,
    defect_review_requested_by: Union[Unset, None, List[int]] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    duplicate: Union[Unset, None, bool] = UNSET,
    duplicate_finding: Union[Unset, None, int] = UNSET,
    dynamic_finding: Union[Unset, None, bool] = UNSET,
    effort_for_fixing: Union[Unset, None, str] = UNSET,
    endpoints: Union[Unset, None, List[int]] = UNSET,
    false_p: Union[Unset, None, bool] = UNSET,
    file_path: Union[Unset, None, str] = UNSET,
    finding_group: Union[Unset, None, List[float]] = UNSET,
    found_by: Union[Unset, None, List[int]] = UNSET,
    has_jira: Union[Unset, None, bool] = UNSET,
    hash_code: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, List[int]] = UNSET,
    impact: Union[Unset, None, str] = UNSET,
    inherited_tags: Union[Unset, None, List[List[int]]] = UNSET,
    is_mitigated: Union[Unset, None, bool] = UNSET,
    jira_change: Union[Unset, None, FindingsListJiraLastUpdate] = UNSET,
    jira_creation: Union[Unset, None, FindingsListJiraCreation] = UNSET,
    last_reviewed: Union[Unset, None, FindingsListLastReviewed] = UNSET,
    last_reviewed_by: Union[Unset, None, List[int]] = UNSET,
    last_status_update: Union[Unset, None, datetime.datetime] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    mitigated: Union[Unset, None, FindingsListMitigated] = UNSET,
    mitigated_by: Union[Unset, None, List[int]] = UNSET,
    mitigation: Union[Unset, None, str] = UNSET,
    nb_occurences: Union[Unset, None, List[int]] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    not_test_engagement_product_tags: Union[Unset, None, List[str]] = UNSET,
    not_test_engagement_tags: Union[Unset, None, List[str]] = UNSET,
    not_test_tags: Union[Unset, None, List[str]] = UNSET,
    numerical_severity: Union[Unset, None, str] = UNSET,
    o: Union[Unset, None, List[FindingsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    out_of_scope: Union[Unset, None, bool] = UNSET,
    param: Union[Unset, None, str] = UNSET,
    payload: Union[Unset, None, str] = UNSET,
    planned_remediation_date: Union[Unset, None, datetime.date] = UNSET,
    planned_remediation_version: Union[Unset, None, str] = UNSET,
    prefetch: Union[Unset, None, List[FindingsListPrefetchItem]] = UNSET,
    product_name: Union[Unset, None, str] = UNSET,
    product_name_contains: Union[Unset, None, str] = UNSET,
    publish_date: Union[Unset, None, datetime.date] = UNSET,
    references: Union[Unset, None, str] = UNSET,
    related_fields: Union[Unset, None, bool] = UNSET,
    reporter: Union[Unset, None, List[int]] = UNSET,
    review_requested_by: Union[Unset, None, List[int]] = UNSET,
    reviewers: Union[Unset, None, List[int]] = UNSET,
    risk_acceptance: Union[Unset, None, float] = UNSET,
    risk_accepted: Union[Unset, None, bool] = UNSET,
    sast_sink_object: Union[Unset, None, str] = UNSET,
    sast_source_file_path: Union[Unset, None, str] = UNSET,
    sast_source_line: Union[Unset, None, List[int]] = UNSET,
    sast_source_object: Union[Unset, None, str] = UNSET,
    scanner_confidence: Union[Unset, None, List[int]] = UNSET,
    service: Union[Unset, None, str] = UNSET,
    severity: Union[Unset, None, str] = UNSET,
    severity_justification: Union[Unset, None, str] = UNSET,
    sla_start_date: Union[Unset, None, datetime.date] = UNSET,
    sonarqube_issue: Union[Unset, None, List[int]] = UNSET,
    static_finding: Union[Unset, None, bool] = UNSET,
    steps_to_reproduce: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    test: Union[Unset, None, int] = UNSET,
    test_engagement: Union[Unset, None, List[int]] = UNSET,
    test_engagement_product: Union[Unset, None, List[int]] = UNSET,
    test_engagement_product_prod_type: Union[Unset, None, List[int]] = UNSET,
    test_engagement_product_tags: Union[Unset, None, List[str]] = UNSET,
    test_engagement_tags: Union[Unset, None, List[str]] = UNSET,
    test_tags: Union[Unset, None, List[str]] = UNSET,
    test_test_type: Union[Unset, None, List[int]] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    under_defect_review: Union[Unset, None, bool] = UNSET,
    under_review: Union[Unset, None, bool] = UNSET,
    unique_id_from_tool: Union[Unset, None, str] = UNSET,
    verified: Union[Unset, None, bool] = UNSET,
    vuln_id_from_tool: Union[Unset, None, str] = UNSET,
    vulnerability_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        active (Union[Unset, None, bool]):
        component_name (Union[Unset, None, str]):
        component_version (Union[Unset, None, str]):
        created (Union[Unset, None, FindingsListCreated]):
        cvssv3 (Union[Unset, None, str]):
        cvssv3_score (Union[Unset, None, float]):
        cwe (Union[Unset, None, List[int]]):
        date (Union[Unset, None, FindingsListDate]):
        defect_review_requested_by (Union[Unset, None, List[int]]):
        description (Union[Unset, None, str]):
        duplicate (Union[Unset, None, bool]):
        duplicate_finding (Union[Unset, None, int]):
        dynamic_finding (Union[Unset, None, bool]):
        effort_for_fixing (Union[Unset, None, str]):
        endpoints (Union[Unset, None, List[int]]):
        false_p (Union[Unset, None, bool]):
        file_path (Union[Unset, None, str]):
        finding_group (Union[Unset, None, List[float]]):
        found_by (Union[Unset, None, List[int]]):
        has_jira (Union[Unset, None, bool]):
        hash_code (Union[Unset, None, str]):
        id (Union[Unset, None, List[int]]):
        impact (Union[Unset, None, str]):
        inherited_tags (Union[Unset, None, List[List[int]]]):
        is_mitigated (Union[Unset, None, bool]):
        jira_change (Union[Unset, None, FindingsListJiraLastUpdate]):
        jira_creation (Union[Unset, None, FindingsListJiraCreation]):
        last_reviewed (Union[Unset, None, FindingsListLastReviewed]):
        last_reviewed_by (Union[Unset, None, List[int]]):
        last_status_update (Union[Unset, None, datetime.datetime]):
        limit (Union[Unset, None, int]):
        mitigated (Union[Unset, None, FindingsListMitigated]):
        mitigated_by (Union[Unset, None, List[int]]):
        mitigation (Union[Unset, None, str]):
        nb_occurences (Union[Unset, None, List[int]]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        not_test_engagement_product_tags (Union[Unset, None, List[str]]):
        not_test_engagement_tags (Union[Unset, None, List[str]]):
        not_test_tags (Union[Unset, None, List[str]]):
        numerical_severity (Union[Unset, None, str]):
        o (Union[Unset, None, List[FindingsListOItem]]):
        offset (Union[Unset, None, int]):
        out_of_scope (Union[Unset, None, bool]):
        param (Union[Unset, None, str]):
        payload (Union[Unset, None, str]):
        planned_remediation_date (Union[Unset, None, datetime.date]):
        planned_remediation_version (Union[Unset, None, str]):
        prefetch (Union[Unset, None, List[FindingsListPrefetchItem]]):
        product_name (Union[Unset, None, str]):
        product_name_contains (Union[Unset, None, str]):
        publish_date (Union[Unset, None, datetime.date]):
        references (Union[Unset, None, str]):
        related_fields (Union[Unset, None, bool]):
        reporter (Union[Unset, None, List[int]]):
        review_requested_by (Union[Unset, None, List[int]]):
        reviewers (Union[Unset, None, List[int]]):
        risk_acceptance (Union[Unset, None, float]):
        risk_accepted (Union[Unset, None, bool]):
        sast_sink_object (Union[Unset, None, str]):
        sast_source_file_path (Union[Unset, None, str]):
        sast_source_line (Union[Unset, None, List[int]]):
        sast_source_object (Union[Unset, None, str]):
        scanner_confidence (Union[Unset, None, List[int]]):
        service (Union[Unset, None, str]):
        severity (Union[Unset, None, str]):
        severity_justification (Union[Unset, None, str]):
        sla_start_date (Union[Unset, None, datetime.date]):
        sonarqube_issue (Union[Unset, None, List[int]]):
        static_finding (Union[Unset, None, bool]):
        steps_to_reproduce (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        test (Union[Unset, None, int]):
        test_engagement (Union[Unset, None, List[int]]):
        test_engagement_product (Union[Unset, None, List[int]]):
        test_engagement_product_prod_type (Union[Unset, None, List[int]]):
        test_engagement_product_tags (Union[Unset, None, List[str]]):
        test_engagement_tags (Union[Unset, None, List[str]]):
        test_tags (Union[Unset, None, List[str]]):
        test_test_type (Union[Unset, None, List[int]]):
        title (Union[Unset, None, str]):
        under_defect_review (Union[Unset, None, bool]):
        under_review (Union[Unset, None, bool]):
        unique_id_from_tool (Union[Unset, None, str]):
        verified (Union[Unset, None, bool]):
        vuln_id_from_tool (Union[Unset, None, str]):
        vulnerability_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        active=active,
        component_name=component_name,
        component_version=component_version,
        created=created,
        cvssv3=cvssv3,
        cvssv3_score=cvssv3_score,
        cwe=cwe,
        date=date,
        defect_review_requested_by=defect_review_requested_by,
        description=description,
        duplicate=duplicate,
        duplicate_finding=duplicate_finding,
        dynamic_finding=dynamic_finding,
        effort_for_fixing=effort_for_fixing,
        endpoints=endpoints,
        false_p=false_p,
        file_path=file_path,
        finding_group=finding_group,
        found_by=found_by,
        has_jira=has_jira,
        hash_code=hash_code,
        id=id,
        impact=impact,
        inherited_tags=inherited_tags,
        is_mitigated=is_mitigated,
        jira_change=jira_change,
        jira_creation=jira_creation,
        last_reviewed=last_reviewed,
        last_reviewed_by=last_reviewed_by,
        last_status_update=last_status_update,
        limit=limit,
        mitigated=mitigated,
        mitigated_by=mitigated_by,
        mitigation=mitigation,
        nb_occurences=nb_occurences,
        not_tag=not_tag,
        not_tags=not_tags,
        not_test_engagement_product_tags=not_test_engagement_product_tags,
        not_test_engagement_tags=not_test_engagement_tags,
        not_test_tags=not_test_tags,
        numerical_severity=numerical_severity,
        o=o,
        offset=offset,
        out_of_scope=out_of_scope,
        param=param,
        payload=payload,
        planned_remediation_date=planned_remediation_date,
        planned_remediation_version=planned_remediation_version,
        prefetch=prefetch,
        product_name=product_name,
        product_name_contains=product_name_contains,
        publish_date=publish_date,
        references=references,
        related_fields=related_fields,
        reporter=reporter,
        review_requested_by=review_requested_by,
        reviewers=reviewers,
        risk_acceptance=risk_acceptance,
        risk_accepted=risk_accepted,
        sast_sink_object=sast_sink_object,
        sast_source_file_path=sast_source_file_path,
        sast_source_line=sast_source_line,
        sast_source_object=sast_source_object,
        scanner_confidence=scanner_confidence,
        service=service,
        severity=severity,
        severity_justification=severity_justification,
        sla_start_date=sla_start_date,
        sonarqube_issue=sonarqube_issue,
        static_finding=static_finding,
        steps_to_reproduce=steps_to_reproduce,
        tag=tag,
        tags=tags,
        test=test,
        test_engagement=test_engagement,
        test_engagement_product=test_engagement_product,
        test_engagement_product_prod_type=test_engagement_product_prod_type,
        test_engagement_product_tags=test_engagement_product_tags,
        test_engagement_tags=test_engagement_tags,
        test_tags=test_tags,
        test_test_type=test_test_type,
        title=title,
        under_defect_review=under_defect_review,
        under_review=under_review,
        unique_id_from_tool=unique_id_from_tool,
        verified=verified,
        vuln_id_from_tool=vuln_id_from_tool,
        vulnerability_id=vulnerability_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    active: Union[Unset, None, bool] = UNSET,
    component_name: Union[Unset, None, str] = UNSET,
    component_version: Union[Unset, None, str] = UNSET,
    created: Union[Unset, None, FindingsListCreated] = UNSET,
    cvssv3: Union[Unset, None, str] = UNSET,
    cvssv3_score: Union[Unset, None, float] = UNSET,
    cwe: Union[Unset, None, List[int]] = UNSET,
    date: Union[Unset, None, FindingsListDate] = UNSET,
    defect_review_requested_by: Union[Unset, None, List[int]] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    duplicate: Union[Unset, None, bool] = UNSET,
    duplicate_finding: Union[Unset, None, int] = UNSET,
    dynamic_finding: Union[Unset, None, bool] = UNSET,
    effort_for_fixing: Union[Unset, None, str] = UNSET,
    endpoints: Union[Unset, None, List[int]] = UNSET,
    false_p: Union[Unset, None, bool] = UNSET,
    file_path: Union[Unset, None, str] = UNSET,
    finding_group: Union[Unset, None, List[float]] = UNSET,
    found_by: Union[Unset, None, List[int]] = UNSET,
    has_jira: Union[Unset, None, bool] = UNSET,
    hash_code: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, List[int]] = UNSET,
    impact: Union[Unset, None, str] = UNSET,
    inherited_tags: Union[Unset, None, List[List[int]]] = UNSET,
    is_mitigated: Union[Unset, None, bool] = UNSET,
    jira_change: Union[Unset, None, FindingsListJiraLastUpdate] = UNSET,
    jira_creation: Union[Unset, None, FindingsListJiraCreation] = UNSET,
    last_reviewed: Union[Unset, None, FindingsListLastReviewed] = UNSET,
    last_reviewed_by: Union[Unset, None, List[int]] = UNSET,
    last_status_update: Union[Unset, None, datetime.datetime] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    mitigated: Union[Unset, None, FindingsListMitigated] = UNSET,
    mitigated_by: Union[Unset, None, List[int]] = UNSET,
    mitigation: Union[Unset, None, str] = UNSET,
    nb_occurences: Union[Unset, None, List[int]] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    not_test_engagement_product_tags: Union[Unset, None, List[str]] = UNSET,
    not_test_engagement_tags: Union[Unset, None, List[str]] = UNSET,
    not_test_tags: Union[Unset, None, List[str]] = UNSET,
    numerical_severity: Union[Unset, None, str] = UNSET,
    o: Union[Unset, None, List[FindingsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    out_of_scope: Union[Unset, None, bool] = UNSET,
    param: Union[Unset, None, str] = UNSET,
    payload: Union[Unset, None, str] = UNSET,
    planned_remediation_date: Union[Unset, None, datetime.date] = UNSET,
    planned_remediation_version: Union[Unset, None, str] = UNSET,
    prefetch: Union[Unset, None, List[FindingsListPrefetchItem]] = UNSET,
    product_name: Union[Unset, None, str] = UNSET,
    product_name_contains: Union[Unset, None, str] = UNSET,
    publish_date: Union[Unset, None, datetime.date] = UNSET,
    references: Union[Unset, None, str] = UNSET,
    related_fields: Union[Unset, None, bool] = UNSET,
    reporter: Union[Unset, None, List[int]] = UNSET,
    review_requested_by: Union[Unset, None, List[int]] = UNSET,
    reviewers: Union[Unset, None, List[int]] = UNSET,
    risk_acceptance: Union[Unset, None, float] = UNSET,
    risk_accepted: Union[Unset, None, bool] = UNSET,
    sast_sink_object: Union[Unset, None, str] = UNSET,
    sast_source_file_path: Union[Unset, None, str] = UNSET,
    sast_source_line: Union[Unset, None, List[int]] = UNSET,
    sast_source_object: Union[Unset, None, str] = UNSET,
    scanner_confidence: Union[Unset, None, List[int]] = UNSET,
    service: Union[Unset, None, str] = UNSET,
    severity: Union[Unset, None, str] = UNSET,
    severity_justification: Union[Unset, None, str] = UNSET,
    sla_start_date: Union[Unset, None, datetime.date] = UNSET,
    sonarqube_issue: Union[Unset, None, List[int]] = UNSET,
    static_finding: Union[Unset, None, bool] = UNSET,
    steps_to_reproduce: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    test: Union[Unset, None, int] = UNSET,
    test_engagement: Union[Unset, None, List[int]] = UNSET,
    test_engagement_product: Union[Unset, None, List[int]] = UNSET,
    test_engagement_product_prod_type: Union[Unset, None, List[int]] = UNSET,
    test_engagement_product_tags: Union[Unset, None, List[str]] = UNSET,
    test_engagement_tags: Union[Unset, None, List[str]] = UNSET,
    test_tags: Union[Unset, None, List[str]] = UNSET,
    test_test_type: Union[Unset, None, List[int]] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    under_defect_review: Union[Unset, None, bool] = UNSET,
    under_review: Union[Unset, None, bool] = UNSET,
    unique_id_from_tool: Union[Unset, None, str] = UNSET,
    verified: Union[Unset, None, bool] = UNSET,
    vuln_id_from_tool: Union[Unset, None, str] = UNSET,
    vulnerability_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        active (Union[Unset, None, bool]):
        component_name (Union[Unset, None, str]):
        component_version (Union[Unset, None, str]):
        created (Union[Unset, None, FindingsListCreated]):
        cvssv3 (Union[Unset, None, str]):
        cvssv3_score (Union[Unset, None, float]):
        cwe (Union[Unset, None, List[int]]):
        date (Union[Unset, None, FindingsListDate]):
        defect_review_requested_by (Union[Unset, None, List[int]]):
        description (Union[Unset, None, str]):
        duplicate (Union[Unset, None, bool]):
        duplicate_finding (Union[Unset, None, int]):
        dynamic_finding (Union[Unset, None, bool]):
        effort_for_fixing (Union[Unset, None, str]):
        endpoints (Union[Unset, None, List[int]]):
        false_p (Union[Unset, None, bool]):
        file_path (Union[Unset, None, str]):
        finding_group (Union[Unset, None, List[float]]):
        found_by (Union[Unset, None, List[int]]):
        has_jira (Union[Unset, None, bool]):
        hash_code (Union[Unset, None, str]):
        id (Union[Unset, None, List[int]]):
        impact (Union[Unset, None, str]):
        inherited_tags (Union[Unset, None, List[List[int]]]):
        is_mitigated (Union[Unset, None, bool]):
        jira_change (Union[Unset, None, FindingsListJiraLastUpdate]):
        jira_creation (Union[Unset, None, FindingsListJiraCreation]):
        last_reviewed (Union[Unset, None, FindingsListLastReviewed]):
        last_reviewed_by (Union[Unset, None, List[int]]):
        last_status_update (Union[Unset, None, datetime.datetime]):
        limit (Union[Unset, None, int]):
        mitigated (Union[Unset, None, FindingsListMitigated]):
        mitigated_by (Union[Unset, None, List[int]]):
        mitigation (Union[Unset, None, str]):
        nb_occurences (Union[Unset, None, List[int]]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        not_test_engagement_product_tags (Union[Unset, None, List[str]]):
        not_test_engagement_tags (Union[Unset, None, List[str]]):
        not_test_tags (Union[Unset, None, List[str]]):
        numerical_severity (Union[Unset, None, str]):
        o (Union[Unset, None, List[FindingsListOItem]]):
        offset (Union[Unset, None, int]):
        out_of_scope (Union[Unset, None, bool]):
        param (Union[Unset, None, str]):
        payload (Union[Unset, None, str]):
        planned_remediation_date (Union[Unset, None, datetime.date]):
        planned_remediation_version (Union[Unset, None, str]):
        prefetch (Union[Unset, None, List[FindingsListPrefetchItem]]):
        product_name (Union[Unset, None, str]):
        product_name_contains (Union[Unset, None, str]):
        publish_date (Union[Unset, None, datetime.date]):
        references (Union[Unset, None, str]):
        related_fields (Union[Unset, None, bool]):
        reporter (Union[Unset, None, List[int]]):
        review_requested_by (Union[Unset, None, List[int]]):
        reviewers (Union[Unset, None, List[int]]):
        risk_acceptance (Union[Unset, None, float]):
        risk_accepted (Union[Unset, None, bool]):
        sast_sink_object (Union[Unset, None, str]):
        sast_source_file_path (Union[Unset, None, str]):
        sast_source_line (Union[Unset, None, List[int]]):
        sast_source_object (Union[Unset, None, str]):
        scanner_confidence (Union[Unset, None, List[int]]):
        service (Union[Unset, None, str]):
        severity (Union[Unset, None, str]):
        severity_justification (Union[Unset, None, str]):
        sla_start_date (Union[Unset, None, datetime.date]):
        sonarqube_issue (Union[Unset, None, List[int]]):
        static_finding (Union[Unset, None, bool]):
        steps_to_reproduce (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        test (Union[Unset, None, int]):
        test_engagement (Union[Unset, None, List[int]]):
        test_engagement_product (Union[Unset, None, List[int]]):
        test_engagement_product_prod_type (Union[Unset, None, List[int]]):
        test_engagement_product_tags (Union[Unset, None, List[str]]):
        test_engagement_tags (Union[Unset, None, List[str]]):
        test_tags (Union[Unset, None, List[str]]):
        test_test_type (Union[Unset, None, List[int]]):
        title (Union[Unset, None, str]):
        under_defect_review (Union[Unset, None, bool]):
        under_review (Union[Unset, None, bool]):
        unique_id_from_tool (Union[Unset, None, str]):
        verified (Union[Unset, None, bool]):
        vuln_id_from_tool (Union[Unset, None, str]):
        vulnerability_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        active=active,
        component_name=component_name,
        component_version=component_version,
        created=created,
        cvssv3=cvssv3,
        cvssv3_score=cvssv3_score,
        cwe=cwe,
        date=date,
        defect_review_requested_by=defect_review_requested_by,
        description=description,
        duplicate=duplicate,
        duplicate_finding=duplicate_finding,
        dynamic_finding=dynamic_finding,
        effort_for_fixing=effort_for_fixing,
        endpoints=endpoints,
        false_p=false_p,
        file_path=file_path,
        finding_group=finding_group,
        found_by=found_by,
        has_jira=has_jira,
        hash_code=hash_code,
        id=id,
        impact=impact,
        inherited_tags=inherited_tags,
        is_mitigated=is_mitigated,
        jira_change=jira_change,
        jira_creation=jira_creation,
        last_reviewed=last_reviewed,
        last_reviewed_by=last_reviewed_by,
        last_status_update=last_status_update,
        limit=limit,
        mitigated=mitigated,
        mitigated_by=mitigated_by,
        mitigation=mitigation,
        nb_occurences=nb_occurences,
        not_tag=not_tag,
        not_tags=not_tags,
        not_test_engagement_product_tags=not_test_engagement_product_tags,
        not_test_engagement_tags=not_test_engagement_tags,
        not_test_tags=not_test_tags,
        numerical_severity=numerical_severity,
        o=o,
        offset=offset,
        out_of_scope=out_of_scope,
        param=param,
        payload=payload,
        planned_remediation_date=planned_remediation_date,
        planned_remediation_version=planned_remediation_version,
        prefetch=prefetch,
        product_name=product_name,
        product_name_contains=product_name_contains,
        publish_date=publish_date,
        references=references,
        related_fields=related_fields,
        reporter=reporter,
        review_requested_by=review_requested_by,
        reviewers=reviewers,
        risk_acceptance=risk_acceptance,
        risk_accepted=risk_accepted,
        sast_sink_object=sast_sink_object,
        sast_source_file_path=sast_source_file_path,
        sast_source_line=sast_source_line,
        sast_source_object=sast_source_object,
        scanner_confidence=scanner_confidence,
        service=service,
        severity=severity,
        severity_justification=severity_justification,
        sla_start_date=sla_start_date,
        sonarqube_issue=sonarqube_issue,
        static_finding=static_finding,
        steps_to_reproduce=steps_to_reproduce,
        tag=tag,
        tags=tags,
        test=test,
        test_engagement=test_engagement,
        test_engagement_product=test_engagement_product,
        test_engagement_product_prod_type=test_engagement_product_prod_type,
        test_engagement_product_tags=test_engagement_product_tags,
        test_engagement_tags=test_engagement_tags,
        test_tags=test_tags,
        test_test_type=test_test_type,
        title=title,
        under_defect_review=under_defect_review,
        under_review=under_review,
        unique_id_from_tool=unique_id_from_tool,
        verified=verified,
        vuln_id_from_tool=vuln_id_from_tool,
        vulnerability_id=vulnerability_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

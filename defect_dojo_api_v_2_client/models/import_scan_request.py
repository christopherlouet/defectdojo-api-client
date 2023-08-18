import datetime
import json
from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.import_scan_request_group_by import ImportScanRequestGroupBy
from ..models.import_scan_request_minimum_severity import ImportScanRequestMinimumSeverity
from ..models.import_scan_request_scan_type import ImportScanRequestScanType
from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="ImportScanRequest")


@_attrs_define
class ImportScanRequest:
    """
    Attributes:
        active (bool): Override the active setting from the tool.
        verified (bool): Override the verified setting from the tool.
        scan_type (ImportScanRequestScanType): * `Acunetix Scan` - Acunetix Scan
            * `Acunetix360 Scan` - Acunetix360 Scan
            * `Anchore Engine Scan` - Anchore Engine Scan
            * `Anchore Enterprise Policy Check` - Anchore Enterprise Policy Check
            * `Anchore Grype` - Anchore Grype
            * `AnchoreCTL Policies Report` - AnchoreCTL Policies Report
            * `AnchoreCTL Vuln Report` - AnchoreCTL Vuln Report
            * `AppSpider Scan` - AppSpider Scan
            * `Aqua Scan` - Aqua Scan
            * `Arachni Scan` - Arachni Scan
            * `AuditJS Scan` - AuditJS Scan
            * `AWS Prowler Scan` - AWS Prowler Scan
            * `AWS Prowler V3` - AWS Prowler V3
            * `AWS Scout2 Scan` - AWS Scout2 Scan
            * `AWS Security Finding Format (ASFF) Scan` - AWS Security Finding Format (ASFF) Scan
            * `AWS Security Hub Scan` - AWS Security Hub Scan
            * `Azure Security Center Recommendations Scan` - Azure Security Center Recommendations Scan
            * `Bandit Scan` - Bandit Scan
            * `BlackDuck API` - BlackDuck API
            * `Blackduck Component Risk` - Blackduck Component Risk
            * `Blackduck Hub Scan` - Blackduck Hub Scan
            * `Brakeman Scan` - Brakeman Scan
            * `Bugcrowd API Import` - Bugcrowd API Import
            * `BugCrowd Scan` - BugCrowd Scan
            * `Bundler-Audit Scan` - Bundler-Audit Scan
            * `Burp Enterprise Scan` - Burp Enterprise Scan
            * `Burp GraphQL API` - Burp GraphQL API
            * `Burp REST API` - Burp REST API
            * `Burp Scan` - Burp Scan
            * `CargoAudit Scan` - CargoAudit Scan
            * `Checkmarx OSA` - Checkmarx OSA
            * `Checkmarx Scan` - Checkmarx Scan
            * `Checkmarx Scan detailed` - Checkmarx Scan detailed
            * `Checkov Scan` - Checkov Scan
            * `Clair Klar Scan` - Clair Klar Scan
            * `Clair Scan` - Clair Scan
            * `Cloudsploit Scan` - Cloudsploit Scan
            * `Cobalt.io API Import` - Cobalt.io API Import
            * `Cobalt.io Scan` - Cobalt.io Scan
            * `Codechecker Report native` - Codechecker Report native
            * `Contrast Scan` - Contrast Scan
            * `Coverity API` - Coverity API
            * `Crashtest Security JSON File` - Crashtest Security JSON File
            * `Crashtest Security XML File` - Crashtest Security XML File
            * `CredScan Scan` - CredScan Scan
            * `CycloneDX Scan` - CycloneDX Scan
            * `DawnScanner Scan` - DawnScanner Scan
            * `Dependency Check Scan` - Dependency Check Scan
            * `Dependency Track Finding Packaging Format (FPF) Export` - Dependency Track Finding Packaging Format (FPF)
            Export
            * `Detect-secrets Scan` - Detect-secrets Scan
            * `docker-bench-security Scan` - docker-bench-security Scan
            * `Dockle Scan` - Dockle Scan
            * `DrHeader JSON Importer` - DrHeader JSON Importer
            * `DSOP Scan` - DSOP Scan
            * `Edgescan Scan` - Edgescan Scan
            * `ESLint Scan` - ESLint Scan
            * `Fortify Scan` - Fortify Scan
            * `Generic Findings Import` - Generic Findings Import
            * `Ggshield Scan` - Ggshield Scan
            * `Github Vulnerability Scan` - Github Vulnerability Scan
            * `GitLab API Fuzzing Report Scan` - GitLab API Fuzzing Report Scan
            * `GitLab Container Scan` - GitLab Container Scan
            * `GitLab DAST Report` - GitLab DAST Report
            * `GitLab Dependency Scanning Report` - GitLab Dependency Scanning Report
            * `GitLab SAST Report` - GitLab SAST Report
            * `GitLab Secret Detection Report` - GitLab Secret Detection Report
            * `Gitleaks Scan` - Gitleaks Scan
            * `Gosec Scanner` - Gosec Scanner
            * `Govulncheck Scanner` - Govulncheck Scanner
            * `HackerOne Cases` - HackerOne Cases
            * `Hadolint Dockerfile check` - Hadolint Dockerfile check
            * `Harbor Vulnerability Scan` - Harbor Vulnerability Scan
            * `Horusec Scan` - Horusec Scan
            * `HuskyCI Report` - HuskyCI Report
            * `Hydra Scan` - Hydra Scan
            * `IBM AppScan DAST` - IBM AppScan DAST
            * `Immuniweb Scan` - Immuniweb Scan
            * `IntSights Report` - IntSights Report
            * `JFrog Xray API Summary Artifact Scan` - JFrog Xray API Summary Artifact Scan
            * `JFrog Xray Scan` - JFrog Xray Scan
            * `JFrog Xray Unified Scan` - JFrog Xray Unified Scan
            * `KICS Scan` - KICS Scan
            * `Kiuwan Scan` - Kiuwan Scan
            * `kube-bench Scan` - kube-bench Scan
            * `Meterian Scan` - Meterian Scan
            * `Microfocus Webinspect Scan` - Microfocus Webinspect Scan
            * `MobSF Scan` - MobSF Scan
            * `Mobsfscan Scan` - Mobsfscan Scan
            * `Mozilla Observatory Scan` - Mozilla Observatory Scan
            * `Netsparker Scan` - Netsparker Scan
            * `NeuVector (compliance)` - NeuVector (compliance)
            * `NeuVector (REST)` - NeuVector (REST)
            * `Nexpose Scan` - Nexpose Scan
            * `Nikto Scan` - Nikto Scan
            * `Nmap Scan` - Nmap Scan
            * `Node Security Platform Scan` - Node Security Platform Scan
            * `NPM Audit Scan` - NPM Audit Scan
            * `Nuclei Scan` - Nuclei Scan
            * `Openscap Vulnerability Scan` - Openscap Vulnerability Scan
            * `OpenVAS CSV` - OpenVAS CSV
            * `ORT evaluated model Importer` - ORT evaluated model Importer
            * `OssIndex Devaudit SCA Scan Importer` - OssIndex Devaudit SCA Scan Importer
            * `Outpost24 Scan` - Outpost24 Scan
            * `PHP Security Audit v2` - PHP Security Audit v2
            * `PHP Symfony Security Check` - PHP Symfony Security Check
            * `pip-audit Scan` - pip-audit Scan
            * `PMD Scan` - PMD Scan
            * `Popeye Scan` - Popeye Scan
            * `PWN SAST` - PWN SAST
            * `Qualys Infrastructure Scan (WebGUI XML)` - Qualys Infrastructure Scan (WebGUI XML)
            * `Qualys Scan` - Qualys Scan
            * `Qualys Webapp Scan` - Qualys Webapp Scan
            * `Retire.js Scan` - Retire.js Scan
            * `Risk Recon API Importer` - Risk Recon API Importer
            * `Rubocop Scan` - Rubocop Scan
            * `Rusty Hog Scan` - Rusty Hog Scan
            * `SARIF` - SARIF
            * `Scantist Scan` - Scantist Scan
            * `Scout Suite Scan` - Scout Suite Scan
            * `Semgrep JSON Report` - Semgrep JSON Report
            * `SKF Scan` - SKF Scan
            * `Snyk Scan` - Snyk Scan
            * `Solar Appscreener Scan` - Solar Appscreener Scan
            * `SonarQube API Import` - SonarQube API Import
            * `SonarQube Scan` - SonarQube Scan
            * `SonarQube Scan detailed` - SonarQube Scan detailed
            * `Sonatype Application Scan` - Sonatype Application Scan
            * `SpotBugs Scan` - SpotBugs Scan
            * `SSL Labs Scan` - SSL Labs Scan
            * `Sslscan` - Sslscan
            * `Sslyze Scan` - Sslyze Scan
            * `SSLyze Scan (JSON)` - SSLyze Scan (JSON)
            * `StackHawk HawkScan` - StackHawk HawkScan
            * `Talisman Scan` - Talisman Scan
            * `Tenable Scan` - Tenable Scan
            * `Terrascan Scan` - Terrascan Scan
            * `Testssl Scan` - Testssl Scan
            * `TFSec Scan` - TFSec Scan
            * `Trivy Operator Scan` - Trivy Operator Scan
            * `Trivy Scan` - Trivy Scan
            * `Trufflehog Scan` - Trufflehog Scan
            * `Trufflehog3 Scan` - Trufflehog3 Scan
            * `Trustwave Fusion API Scan` - Trustwave Fusion API Scan
            * `Trustwave Scan (CSV)` - Trustwave Scan (CSV)
            * `Twistlock Image Scan` - Twistlock Image Scan
            * `VCG Scan` - VCG Scan
            * `Veracode Scan` - Veracode Scan
            * `Veracode SourceClear Scan` - Veracode SourceClear Scan
            * `Vulners` - Vulners
            * `Wapiti Scan` - Wapiti Scan
            * `Wazuh` - Wazuh
            * `WFuzz JSON report` - WFuzz JSON report
            * `Whispers Scan` - Whispers Scan
            * `WhiteHat Sentinel` - WhiteHat Sentinel
            * `Whitesource Scan` - Whitesource Scan
            * `Wpscan` - Wpscan
            * `Xanitizer Scan` - Xanitizer Scan
            * `Yarn Audit Scan` - Yarn Audit Scan
            * `ZAP Scan` - ZAP Scan
        scan_date (Union[Unset, datetime.date]): Scan completion date will be used on all findings.
        minimum_severity (Union[Unset, ImportScanRequestMinimumSeverity]): Minimum severity level to be imported

            * `Info` - Info
            * `Low` - Low
            * `Medium` - Medium
            * `High` - High
            * `Critical` - Critical Default: ImportScanRequestMinimumSeverity.INFO.
        endpoint_to_add (Union[Unset, int]): The IP address, host name or full URL. It must be valid
        file (Union[Unset, File]):
        product_type_name (Union[Unset, str]):
        product_name (Union[Unset, str]):
        engagement_name (Union[Unset, str]):
        engagement_end_date (Union[Unset, datetime.date]): End Date for Engagement. Default is current time + 365 days.
            Required format year-month-day
        source_code_management_uri (Union[Unset, str]): Resource link to source code
        engagement (Union[Unset, int]):
        test_title (Union[Unset, str]):
        auto_create_context (Union[Unset, bool]):
        deduplication_on_engagement (Union[Unset, bool]):
        lead (Union[Unset, None, int]):
        tags (Union[Unset, List[str]]): Add tags that help describe this scan.
        close_old_findings (Union[Unset, bool]): Select if old findings no longer present in the report get closed as
            mitigated when importing. If service has been set, only the findings for this service will be closed.
        close_old_findings_product_scope (Union[Unset, bool]): Select if close_old_findings applies to all findings of
            the same type in the product. By default, it is false meaning that only old findings of the same type in the
            engagement are in scope.
        push_to_jira (Union[Unset, bool]):
        environment (Union[Unset, str]):
        version (Union[Unset, str]): Version that was scanned.
        build_id (Union[Unset, str]): ID of the build that was scanned.
        branch_tag (Union[Unset, str]): Branch or Tag that was scanned.
        commit_hash (Union[Unset, str]): Commit that was scanned.
        api_scan_configuration (Union[Unset, None, int]):
        service (Union[Unset, str]): A service is a self-contained piece of functionality within a Product. This is an
            optional field which is used in deduplication and closing of old findings when set. This affects the whole
            engagement/product depending on your deduplication scope.
        group_by (Union[Unset, ImportScanRequestGroupBy]): Choose an option to automatically group new findings by the
            chosen option.

            * `component_name` - Component Name
            * `component_name+component_version` - Component Name + Version
            * `file_path` - File path
            * `finding_title` - Finding Title
        create_finding_groups_for_all_findings (Union[Unset, bool]): If set to false, finding groups will only be
            created when there is more than one grouped finding Default: True.
    """

    active: bool
    verified: bool
    scan_type: ImportScanRequestScanType
    scan_date: Union[Unset, datetime.date] = UNSET
    minimum_severity: Union[Unset, ImportScanRequestMinimumSeverity] = ImportScanRequestMinimumSeverity.INFO
    endpoint_to_add: Union[Unset, int] = UNSET
    file: Union[Unset, File] = UNSET
    product_type_name: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    engagement_name: Union[Unset, str] = UNSET
    engagement_end_date: Union[Unset, datetime.date] = UNSET
    source_code_management_uri: Union[Unset, str] = UNSET
    engagement: Union[Unset, int] = UNSET
    test_title: Union[Unset, str] = UNSET
    auto_create_context: Union[Unset, bool] = UNSET
    deduplication_on_engagement: Union[Unset, bool] = UNSET
    lead: Union[Unset, None, int] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    close_old_findings: Union[Unset, bool] = False
    close_old_findings_product_scope: Union[Unset, bool] = False
    push_to_jira: Union[Unset, bool] = False
    environment: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    build_id: Union[Unset, str] = UNSET
    branch_tag: Union[Unset, str] = UNSET
    commit_hash: Union[Unset, str] = UNSET
    api_scan_configuration: Union[Unset, None, int] = UNSET
    service: Union[Unset, str] = UNSET
    group_by: Union[Unset, ImportScanRequestGroupBy] = UNSET
    create_finding_groups_for_all_findings: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        verified = self.verified
        scan_type = self.scan_type.value

        scan_date: Union[Unset, str] = UNSET
        if not isinstance(self.scan_date, Unset):
            scan_date = self.scan_date.isoformat()

        minimum_severity: Union[Unset, str] = UNSET
        if not isinstance(self.minimum_severity, Unset):
            minimum_severity = self.minimum_severity.value

        endpoint_to_add = self.endpoint_to_add
        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        product_type_name = self.product_type_name
        product_name = self.product_name
        engagement_name = self.engagement_name
        engagement_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.engagement_end_date, Unset):
            engagement_end_date = self.engagement_end_date.isoformat()

        source_code_management_uri = self.source_code_management_uri
        engagement = self.engagement
        test_title = self.test_title
        auto_create_context = self.auto_create_context
        deduplication_on_engagement = self.deduplication_on_engagement
        lead = self.lead
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        close_old_findings = self.close_old_findings
        close_old_findings_product_scope = self.close_old_findings_product_scope
        push_to_jira = self.push_to_jira
        environment = self.environment
        version = self.version
        build_id = self.build_id
        branch_tag = self.branch_tag
        commit_hash = self.commit_hash
        api_scan_configuration = self.api_scan_configuration
        service = self.service
        group_by: Union[Unset, str] = UNSET
        if not isinstance(self.group_by, Unset):
            group_by = self.group_by.value

        create_finding_groups_for_all_findings = self.create_finding_groups_for_all_findings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "verified": verified,
                "scan_type": scan_type,
            }
        )
        if scan_date is not UNSET:
            field_dict["scan_date"] = scan_date
        if minimum_severity is not UNSET:
            field_dict["minimum_severity"] = minimum_severity
        if endpoint_to_add is not UNSET:
            field_dict["endpoint_to_add"] = endpoint_to_add
        if file is not UNSET:
            field_dict["file"] = file
        if product_type_name is not UNSET:
            field_dict["product_type_name"] = product_type_name
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if engagement_name is not UNSET:
            field_dict["engagement_name"] = engagement_name
        if engagement_end_date is not UNSET:
            field_dict["engagement_end_date"] = engagement_end_date
        if source_code_management_uri is not UNSET:
            field_dict["source_code_management_uri"] = source_code_management_uri
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if test_title is not UNSET:
            field_dict["test_title"] = test_title
        if auto_create_context is not UNSET:
            field_dict["auto_create_context"] = auto_create_context
        if deduplication_on_engagement is not UNSET:
            field_dict["deduplication_on_engagement"] = deduplication_on_engagement
        if lead is not UNSET:
            field_dict["lead"] = lead
        if tags is not UNSET:
            field_dict["tags"] = tags
        if close_old_findings is not UNSET:
            field_dict["close_old_findings"] = close_old_findings
        if close_old_findings_product_scope is not UNSET:
            field_dict["close_old_findings_product_scope"] = close_old_findings_product_scope
        if push_to_jira is not UNSET:
            field_dict["push_to_jira"] = push_to_jira
        if environment is not UNSET:
            field_dict["environment"] = environment
        if version is not UNSET:
            field_dict["version"] = version
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if api_scan_configuration is not UNSET:
            field_dict["api_scan_configuration"] = api_scan_configuration
        if service is not UNSET:
            field_dict["service"] = service
        if group_by is not UNSET:
            field_dict["group_by"] = group_by
        if create_finding_groups_for_all_findings is not UNSET:
            field_dict["create_finding_groups_for_all_findings"] = create_finding_groups_for_all_findings

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        active = self.active if isinstance(self.active, Unset) else (None, str(self.active).encode(), "text/plain")
        verified = (
            self.verified if isinstance(self.verified, Unset) else (None, str(self.verified).encode(), "text/plain")
        )
        scan_type = (None, str(self.scan_type.value).encode(), "text/plain")

        scan_date: Union[Unset, bytes] = UNSET
        if not isinstance(self.scan_date, Unset):
            scan_date = self.scan_date.isoformat().encode()

        minimum_severity: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.minimum_severity, Unset):
            minimum_severity = (None, str(self.minimum_severity.value).encode(), "text/plain")

        endpoint_to_add = (
            self.endpoint_to_add
            if isinstance(self.endpoint_to_add, Unset)
            else (None, str(self.endpoint_to_add).encode(), "text/plain")
        )
        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        product_type_name = (
            self.product_type_name
            if isinstance(self.product_type_name, Unset)
            else (None, str(self.product_type_name).encode(), "text/plain")
        )
        product_name = (
            self.product_name
            if isinstance(self.product_name, Unset)
            else (None, str(self.product_name).encode(), "text/plain")
        )
        engagement_name = (
            self.engagement_name
            if isinstance(self.engagement_name, Unset)
            else (None, str(self.engagement_name).encode(), "text/plain")
        )
        engagement_end_date: Union[Unset, bytes] = UNSET
        if not isinstance(self.engagement_end_date, Unset):
            engagement_end_date = self.engagement_end_date.isoformat().encode()

        source_code_management_uri = (
            self.source_code_management_uri
            if isinstance(self.source_code_management_uri, Unset)
            else (None, str(self.source_code_management_uri).encode(), "text/plain")
        )
        engagement = (
            self.engagement
            if isinstance(self.engagement, Unset)
            else (None, str(self.engagement).encode(), "text/plain")
        )
        test_title = (
            self.test_title
            if isinstance(self.test_title, Unset)
            else (None, str(self.test_title).encode(), "text/plain")
        )
        auto_create_context = (
            self.auto_create_context
            if isinstance(self.auto_create_context, Unset)
            else (None, str(self.auto_create_context).encode(), "text/plain")
        )
        deduplication_on_engagement = (
            self.deduplication_on_engagement
            if isinstance(self.deduplication_on_engagement, Unset)
            else (None, str(self.deduplication_on_engagement).encode(), "text/plain")
        )
        lead = self.lead if isinstance(self.lead, Unset) else (None, str(self.lead).encode(), "text/plain")
        tags: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = self.tags
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        close_old_findings = (
            self.close_old_findings
            if isinstance(self.close_old_findings, Unset)
            else (None, str(self.close_old_findings).encode(), "text/plain")
        )
        close_old_findings_product_scope = (
            self.close_old_findings_product_scope
            if isinstance(self.close_old_findings_product_scope, Unset)
            else (None, str(self.close_old_findings_product_scope).encode(), "text/plain")
        )
        push_to_jira = (
            self.push_to_jira
            if isinstance(self.push_to_jira, Unset)
            else (None, str(self.push_to_jira).encode(), "text/plain")
        )
        environment = (
            self.environment
            if isinstance(self.environment, Unset)
            else (None, str(self.environment).encode(), "text/plain")
        )
        version = self.version if isinstance(self.version, Unset) else (None, str(self.version).encode(), "text/plain")
        build_id = (
            self.build_id if isinstance(self.build_id, Unset) else (None, str(self.build_id).encode(), "text/plain")
        )
        branch_tag = (
            self.branch_tag
            if isinstance(self.branch_tag, Unset)
            else (None, str(self.branch_tag).encode(), "text/plain")
        )
        commit_hash = (
            self.commit_hash
            if isinstance(self.commit_hash, Unset)
            else (None, str(self.commit_hash).encode(), "text/plain")
        )
        api_scan_configuration = (
            self.api_scan_configuration
            if isinstance(self.api_scan_configuration, Unset)
            else (None, str(self.api_scan_configuration).encode(), "text/plain")
        )
        service = self.service if isinstance(self.service, Unset) else (None, str(self.service).encode(), "text/plain")
        group_by: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.group_by, Unset):
            group_by = (None, str(self.group_by.value).encode(), "text/plain")

        create_finding_groups_for_all_findings = (
            self.create_finding_groups_for_all_findings
            if isinstance(self.create_finding_groups_for_all_findings, Unset)
            else (None, str(self.create_finding_groups_for_all_findings).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "active": active,
                "verified": verified,
                "scan_type": scan_type,
            }
        )
        if scan_date is not UNSET:
            field_dict["scan_date"] = scan_date
        if minimum_severity is not UNSET:
            field_dict["minimum_severity"] = minimum_severity
        if endpoint_to_add is not UNSET:
            field_dict["endpoint_to_add"] = endpoint_to_add
        if file is not UNSET:
            field_dict["file"] = file
        if product_type_name is not UNSET:
            field_dict["product_type_name"] = product_type_name
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if engagement_name is not UNSET:
            field_dict["engagement_name"] = engagement_name
        if engagement_end_date is not UNSET:
            field_dict["engagement_end_date"] = engagement_end_date
        if source_code_management_uri is not UNSET:
            field_dict["source_code_management_uri"] = source_code_management_uri
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if test_title is not UNSET:
            field_dict["test_title"] = test_title
        if auto_create_context is not UNSET:
            field_dict["auto_create_context"] = auto_create_context
        if deduplication_on_engagement is not UNSET:
            field_dict["deduplication_on_engagement"] = deduplication_on_engagement
        if lead is not UNSET:
            field_dict["lead"] = lead
        if tags is not UNSET:
            field_dict["tags"] = tags
        if close_old_findings is not UNSET:
            field_dict["close_old_findings"] = close_old_findings
        if close_old_findings_product_scope is not UNSET:
            field_dict["close_old_findings_product_scope"] = close_old_findings_product_scope
        if push_to_jira is not UNSET:
            field_dict["push_to_jira"] = push_to_jira
        if environment is not UNSET:
            field_dict["environment"] = environment
        if version is not UNSET:
            field_dict["version"] = version
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if api_scan_configuration is not UNSET:
            field_dict["api_scan_configuration"] = api_scan_configuration
        if service is not UNSET:
            field_dict["service"] = service
        if group_by is not UNSET:
            field_dict["group_by"] = group_by
        if create_finding_groups_for_all_findings is not UNSET:
            field_dict["create_finding_groups_for_all_findings"] = create_finding_groups_for_all_findings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active = d.pop("active")

        verified = d.pop("verified")

        scan_type = ImportScanRequestScanType(d.pop("scan_type"))

        _scan_date = d.pop("scan_date", UNSET)
        scan_date: Union[Unset, datetime.date]
        if isinstance(_scan_date, Unset):
            scan_date = UNSET
        else:
            scan_date = isoparse(_scan_date).date()

        _minimum_severity = d.pop("minimum_severity", UNSET)
        minimum_severity: Union[Unset, ImportScanRequestMinimumSeverity]
        if isinstance(_minimum_severity, Unset):
            minimum_severity = UNSET
        else:
            minimum_severity = ImportScanRequestMinimumSeverity(_minimum_severity)

        endpoint_to_add = d.pop("endpoint_to_add", UNSET)

        _file = d.pop("file", UNSET)
        file: Union[Unset, File]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        product_type_name = d.pop("product_type_name", UNSET)

        product_name = d.pop("product_name", UNSET)

        engagement_name = d.pop("engagement_name", UNSET)

        _engagement_end_date = d.pop("engagement_end_date", UNSET)
        engagement_end_date: Union[Unset, datetime.date]
        if isinstance(_engagement_end_date, Unset):
            engagement_end_date = UNSET
        else:
            engagement_end_date = isoparse(_engagement_end_date).date()

        source_code_management_uri = d.pop("source_code_management_uri", UNSET)

        engagement = d.pop("engagement", UNSET)

        test_title = d.pop("test_title", UNSET)

        auto_create_context = d.pop("auto_create_context", UNSET)

        deduplication_on_engagement = d.pop("deduplication_on_engagement", UNSET)

        lead = d.pop("lead", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        close_old_findings = d.pop("close_old_findings", UNSET)

        close_old_findings_product_scope = d.pop("close_old_findings_product_scope", UNSET)

        push_to_jira = d.pop("push_to_jira", UNSET)

        environment = d.pop("environment", UNSET)

        version = d.pop("version", UNSET)

        build_id = d.pop("build_id", UNSET)

        branch_tag = d.pop("branch_tag", UNSET)

        commit_hash = d.pop("commit_hash", UNSET)

        api_scan_configuration = d.pop("api_scan_configuration", UNSET)

        service = d.pop("service", UNSET)

        _group_by = d.pop("group_by", UNSET)
        group_by: Union[Unset, ImportScanRequestGroupBy]
        if isinstance(_group_by, Unset):
            group_by = UNSET
        else:
            group_by = ImportScanRequestGroupBy(_group_by)

        create_finding_groups_for_all_findings = d.pop("create_finding_groups_for_all_findings", UNSET)

        import_scan_request = cls(
            active=active,
            verified=verified,
            scan_type=scan_type,
            scan_date=scan_date,
            minimum_severity=minimum_severity,
            endpoint_to_add=endpoint_to_add,
            file=file,
            product_type_name=product_type_name,
            product_name=product_name,
            engagement_name=engagement_name,
            engagement_end_date=engagement_end_date,
            source_code_management_uri=source_code_management_uri,
            engagement=engagement,
            test_title=test_title,
            auto_create_context=auto_create_context,
            deduplication_on_engagement=deduplication_on_engagement,
            lead=lead,
            tags=tags,
            close_old_findings=close_old_findings,
            close_old_findings_product_scope=close_old_findings_product_scope,
            push_to_jira=push_to_jira,
            environment=environment,
            version=version,
            build_id=build_id,
            branch_tag=branch_tag,
            commit_hash=commit_hash,
            api_scan_configuration=api_scan_configuration,
            service=service,
            group_by=group_by,
            create_finding_groups_for_all_findings=create_finding_groups_for_all_findings,
        )

        import_scan_request.additional_properties = d
        return import_scan_request

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

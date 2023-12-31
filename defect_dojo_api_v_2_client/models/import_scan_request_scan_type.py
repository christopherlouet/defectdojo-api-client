from enum import Enum


class ImportScanRequestScanType(str, Enum):
    ACUNETIX360_SCAN = "Acunetix360 Scan"
    ACUNETIX_SCAN = "Acunetix Scan"
    ANCHORECTL_POLICIES_REPORT = "AnchoreCTL Policies Report"
    ANCHORECTL_VULN_REPORT = "AnchoreCTL Vuln Report"
    ANCHORE_ENGINE_SCAN = "Anchore Engine Scan"
    ANCHORE_ENTERPRISE_POLICY_CHECK = "Anchore Enterprise Policy Check"
    ANCHORE_GRYPE = "Anchore Grype"
    APPSPIDER_SCAN = "AppSpider Scan"
    AQUA_SCAN = "Aqua Scan"
    ARACHNI_SCAN = "Arachni Scan"
    AUDITJS_SCAN = "AuditJS Scan"
    AWS_PROWLER_SCAN = "AWS Prowler Scan"
    AWS_PROWLER_V3 = "AWS Prowler V3"
    AWS_SCOUT2_SCAN = "AWS Scout2 Scan"
    AWS_SECURITY_FINDING_FORMAT_ASFF_SCAN = "AWS Security Finding Format (ASFF) Scan"
    AWS_SECURITY_HUB_SCAN = "AWS Security Hub Scan"
    AZURE_SECURITY_CENTER_RECOMMENDATIONS_SCAN = "Azure Security Center Recommendations Scan"
    BANDIT_SCAN = "Bandit Scan"
    BLACKDUCK_API = "BlackDuck API"
    BLACKDUCK_COMPONENT_RISK = "Blackduck Component Risk"
    BLACKDUCK_HUB_SCAN = "Blackduck Hub Scan"
    BRAKEMAN_SCAN = "Brakeman Scan"
    BUGCROWD_API_IMPORT = "Bugcrowd API Import"
    BUGCROWD_SCAN = "BugCrowd Scan"
    BUNDLER_AUDIT_SCAN = "Bundler-Audit Scan"
    BURP_ENTERPRISE_SCAN = "Burp Enterprise Scan"
    BURP_GRAPHQL_API = "Burp GraphQL API"
    BURP_REST_API = "Burp REST API"
    BURP_SCAN = "Burp Scan"
    CARGOAUDIT_SCAN = "CargoAudit Scan"
    CHECKMARX_OSA = "Checkmarx OSA"
    CHECKMARX_SCAN = "Checkmarx Scan"
    CHECKMARX_SCAN_DETAILED = "Checkmarx Scan detailed"
    CHECKOV_SCAN = "Checkov Scan"
    CLAIR_KLAR_SCAN = "Clair Klar Scan"
    CLAIR_SCAN = "Clair Scan"
    CLOUDSPLOIT_SCAN = "Cloudsploit Scan"
    COBALT_IO_API_IMPORT = "Cobalt.io API Import"
    COBALT_IO_SCAN = "Cobalt.io Scan"
    CODECHECKER_REPORT_NATIVE = "Codechecker Report native"
    CONTRAST_SCAN = "Contrast Scan"
    COVERITY_API = "Coverity API"
    CRASHTEST_SECURITY_JSON_FILE = "Crashtest Security JSON File"
    CRASHTEST_SECURITY_XML_FILE = "Crashtest Security XML File"
    CREDSCAN_SCAN = "CredScan Scan"
    CYCLONEDX_SCAN = "CycloneDX Scan"
    DAWNSCANNER_SCAN = "DawnScanner Scan"
    DEPENDENCY_CHECK_SCAN = "Dependency Check Scan"
    DEPENDENCY_TRACK_FINDING_PACKAGING_FORMAT_FPF_EXPORT = "Dependency Track Finding Packaging Format (FPF) Export"
    DETECT_SECRETS_SCAN = "Detect-secrets Scan"
    DOCKER_BENCH_SECURITY_SCAN = "docker-bench-security Scan"
    DOCKLE_SCAN = "Dockle Scan"
    DRHEADER_JSON_IMPORTER = "DrHeader JSON Importer"
    DSOP_SCAN = "DSOP Scan"
    EDGESCAN_SCAN = "Edgescan Scan"
    ESLINT_SCAN = "ESLint Scan"
    FORTIFY_SCAN = "Fortify Scan"
    GENERIC_FINDINGS_IMPORT = "Generic Findings Import"
    GGSHIELD_SCAN = "Ggshield Scan"
    GITHUB_VULNERABILITY_SCAN = "Github Vulnerability Scan"
    GITLAB_API_FUZZING_REPORT_SCAN = "GitLab API Fuzzing Report Scan"
    GITLAB_CONTAINER_SCAN = "GitLab Container Scan"
    GITLAB_DAST_REPORT = "GitLab DAST Report"
    GITLAB_DEPENDENCY_SCANNING_REPORT = "GitLab Dependency Scanning Report"
    GITLAB_SAST_REPORT = "GitLab SAST Report"
    GITLAB_SECRET_DETECTION_REPORT = "GitLab Secret Detection Report"
    GITLEAKS_SCAN = "Gitleaks Scan"
    GOSEC_SCANNER = "Gosec Scanner"
    GOVULNCHECK_SCANNER = "Govulncheck Scanner"
    HACKERONE_CASES = "HackerOne Cases"
    HADOLINT_DOCKERFILE_CHECK = "Hadolint Dockerfile check"
    HARBOR_VULNERABILITY_SCAN = "Harbor Vulnerability Scan"
    HORUSEC_SCAN = "Horusec Scan"
    HUSKYCI_REPORT = "HuskyCI Report"
    HYDRA_SCAN = "Hydra Scan"
    IBM_APPSCAN_DAST = "IBM AppScan DAST"
    IMMUNIWEB_SCAN = "Immuniweb Scan"
    INTSIGHTS_REPORT = "IntSights Report"
    JFROG_XRAY_API_SUMMARY_ARTIFACT_SCAN = "JFrog Xray API Summary Artifact Scan"
    JFROG_XRAY_SCAN = "JFrog Xray Scan"
    JFROG_XRAY_UNIFIED_SCAN = "JFrog Xray Unified Scan"
    KICS_SCAN = "KICS Scan"
    KIUWAN_SCAN = "Kiuwan Scan"
    KUBE_BENCH_SCAN = "kube-bench Scan"
    METERIAN_SCAN = "Meterian Scan"
    MICROFOCUS_WEBINSPECT_SCAN = "Microfocus Webinspect Scan"
    MOBSFSCAN_SCAN = "Mobsfscan Scan"
    MOBSF_SCAN = "MobSF Scan"
    MOZILLA_OBSERVATORY_SCAN = "Mozilla Observatory Scan"
    NETSPARKER_SCAN = "Netsparker Scan"
    NEUVECTOR_COMPLIANCE = "NeuVector (compliance)"
    NEUVECTOR_REST = "NeuVector (REST)"
    NEXPOSE_SCAN = "Nexpose Scan"
    NIKTO_SCAN = "Nikto Scan"
    NMAP_SCAN = "Nmap Scan"
    NODE_SECURITY_PLATFORM_SCAN = "Node Security Platform Scan"
    NPM_AUDIT_SCAN = "NPM Audit Scan"
    NUCLEI_SCAN = "Nuclei Scan"
    OPENSCAP_VULNERABILITY_SCAN = "Openscap Vulnerability Scan"
    OPENVAS_CSV = "OpenVAS CSV"
    ORT_EVALUATED_MODEL_IMPORTER = "ORT evaluated model Importer"
    OSSINDEX_DEVAUDIT_SCA_SCAN_IMPORTER = "OssIndex Devaudit SCA Scan Importer"
    OUTPOST24_SCAN = "Outpost24 Scan"
    PHP_SECURITY_AUDIT_V2 = "PHP Security Audit v2"
    PHP_SYMFONY_SECURITY_CHECK = "PHP Symfony Security Check"
    PIP_AUDIT_SCAN = "pip-audit Scan"
    PMD_SCAN = "PMD Scan"
    POPEYE_SCAN = "Popeye Scan"
    PWN_SAST = "PWN SAST"
    QUALYS_INFRASTRUCTURE_SCAN_WEBGUI_XML = "Qualys Infrastructure Scan (WebGUI XML)"
    QUALYS_SCAN = "Qualys Scan"
    QUALYS_WEBAPP_SCAN = "Qualys Webapp Scan"
    RETIRE_JS_SCAN = "Retire.js Scan"
    RISK_RECON_API_IMPORTER = "Risk Recon API Importer"
    RUBOCOP_SCAN = "Rubocop Scan"
    RUSTY_HOG_SCAN = "Rusty Hog Scan"
    SARIF = "SARIF"
    SCANTIST_SCAN = "Scantist Scan"
    SCOUT_SUITE_SCAN = "Scout Suite Scan"
    SEMGREP_JSON_REPORT = "Semgrep JSON Report"
    SKF_SCAN = "SKF Scan"
    SNYK_SCAN = "Snyk Scan"
    SOLAR_APPSCREENER_SCAN = "Solar Appscreener Scan"
    SONARQUBE_API_IMPORT = "SonarQube API Import"
    SONARQUBE_SCAN = "SonarQube Scan"
    SONARQUBE_SCAN_DETAILED = "SonarQube Scan detailed"
    SONATYPE_APPLICATION_SCAN = "Sonatype Application Scan"
    SPOTBUGS_SCAN = "SpotBugs Scan"
    SSLSCAN = "Sslscan"
    SSLYZE_SCAN = "Sslyze Scan"
    SSLYZE_SCAN_JSON = "SSLyze Scan (JSON)"
    SSL_LABS_SCAN = "SSL Labs Scan"
    STACKHAWK_HAWKSCAN = "StackHawk HawkScan"
    TALISMAN_SCAN = "Talisman Scan"
    TENABLE_SCAN = "Tenable Scan"
    TERRASCAN_SCAN = "Terrascan Scan"
    TESTSSL_SCAN = "Testssl Scan"
    TFSEC_SCAN = "TFSec Scan"
    TRIVY_OPERATOR_SCAN = "Trivy Operator Scan"
    TRIVY_SCAN = "Trivy Scan"
    TRUFFLEHOG3_SCAN = "Trufflehog3 Scan"
    TRUFFLEHOG_SCAN = "Trufflehog Scan"
    TRUSTWAVE_FUSION_API_SCAN = "Trustwave Fusion API Scan"
    TRUSTWAVE_SCAN_CSV = "Trustwave Scan (CSV)"
    TWISTLOCK_IMAGE_SCAN = "Twistlock Image Scan"
    VCG_SCAN = "VCG Scan"
    VERACODE_SCAN = "Veracode Scan"
    VERACODE_SOURCECLEAR_SCAN = "Veracode SourceClear Scan"
    VULNERS = "Vulners"
    WAPITI_SCAN = "Wapiti Scan"
    WAZUH = "Wazuh"
    WFUZZ_JSON_REPORT = "WFuzz JSON report"
    WHISPERS_SCAN = "Whispers Scan"
    WHITEHAT_SENTINEL = "WhiteHat Sentinel"
    WHITESOURCE_SCAN = "Whitesource Scan"
    WPSCAN = "Wpscan"
    XANITIZER_SCAN = "Xanitizer Scan"
    YARN_AUDIT_SCAN = "Yarn Audit Scan"
    ZAP_SCAN = "ZAP Scan"

    def __str__(self) -> str:
        return str(self.value)

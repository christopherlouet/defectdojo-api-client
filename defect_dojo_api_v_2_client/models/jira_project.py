from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jira_project_custom_fields import JIRAProjectCustomFields


T = TypeVar("T", bound="JIRAProject")


@_attrs_define
class JIRAProject:
    """
    Attributes:
        id (int):
        project_key (Union[Unset, str]):
        issue_template_dir (Union[Unset, None, str]): Choose the folder containing the Django templates used to render
            the JIRA issue description. These are stored in dojo/templates/issue-trackers. Leave empty to use the default
            jira_full templates.
        component (Union[Unset, str]):
        custom_fields (Union[Unset, None, JIRAProjectCustomFields]): JIRA custom field JSON mapping of Id to value, e.g.
            {"customfield_10122": [{"name": "8.0.1"}]}
        default_assignee (Union[Unset, None, str]): JIRA default assignee (name). If left blank then it defaults to
            whatever is configured in JIRA.
        jira_labels (Union[Unset, None, str]): JIRA issue labels space seperated
        add_vulnerability_id_to_jira_label (Union[Unset, bool]):
        push_all_issues (Union[Unset, bool]): Automatically maintain parity with JIRA. Always create and update JIRA
            tickets for findings in this Product.
        enable_engagement_epic_mapping (Union[Unset, bool]):
        push_notes (Union[Unset, bool]):
        product_jira_sla_notification (Union[Unset, bool]):
        risk_acceptance_expiration_notification (Union[Unset, bool]):
        jira_instance (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        engagement (Union[Unset, None, int]):
    """

    id: int
    project_key: Union[Unset, str] = UNSET
    issue_template_dir: Union[Unset, None, str] = UNSET
    component: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, None, "JIRAProjectCustomFields"] = UNSET
    default_assignee: Union[Unset, None, str] = UNSET
    jira_labels: Union[Unset, None, str] = UNSET
    add_vulnerability_id_to_jira_label: Union[Unset, bool] = UNSET
    push_all_issues: Union[Unset, bool] = UNSET
    enable_engagement_epic_mapping: Union[Unset, bool] = UNSET
    push_notes: Union[Unset, bool] = UNSET
    product_jira_sla_notification: Union[Unset, bool] = UNSET
    risk_acceptance_expiration_notification: Union[Unset, bool] = UNSET
    jira_instance: Union[Unset, None, int] = UNSET
    product: Union[Unset, None, int] = UNSET
    engagement: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        project_key = self.project_key
        issue_template_dir = self.issue_template_dir
        component = self.component
        custom_fields: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict() if self.custom_fields else None

        default_assignee = self.default_assignee
        jira_labels = self.jira_labels
        add_vulnerability_id_to_jira_label = self.add_vulnerability_id_to_jira_label
        push_all_issues = self.push_all_issues
        enable_engagement_epic_mapping = self.enable_engagement_epic_mapping
        push_notes = self.push_notes
        product_jira_sla_notification = self.product_jira_sla_notification
        risk_acceptance_expiration_notification = self.risk_acceptance_expiration_notification
        jira_instance = self.jira_instance
        product = self.product
        engagement = self.engagement

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if project_key is not UNSET:
            field_dict["project_key"] = project_key
        if issue_template_dir is not UNSET:
            field_dict["issue_template_dir"] = issue_template_dir
        if component is not UNSET:
            field_dict["component"] = component
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if default_assignee is not UNSET:
            field_dict["default_assignee"] = default_assignee
        if jira_labels is not UNSET:
            field_dict["jira_labels"] = jira_labels
        if add_vulnerability_id_to_jira_label is not UNSET:
            field_dict["add_vulnerability_id_to_jira_label"] = add_vulnerability_id_to_jira_label
        if push_all_issues is not UNSET:
            field_dict["push_all_issues"] = push_all_issues
        if enable_engagement_epic_mapping is not UNSET:
            field_dict["enable_engagement_epic_mapping"] = enable_engagement_epic_mapping
        if push_notes is not UNSET:
            field_dict["push_notes"] = push_notes
        if product_jira_sla_notification is not UNSET:
            field_dict["product_jira_sla_notification"] = product_jira_sla_notification
        if risk_acceptance_expiration_notification is not UNSET:
            field_dict["risk_acceptance_expiration_notification"] = risk_acceptance_expiration_notification
        if jira_instance is not UNSET:
            field_dict["jira_instance"] = jira_instance
        if product is not UNSET:
            field_dict["product"] = product
        if engagement is not UNSET:
            field_dict["engagement"] = engagement

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.jira_project_custom_fields import JIRAProjectCustomFields

        d = src_dict.copy()
        id = d.pop("id")

        project_key = d.pop("project_key", UNSET)

        issue_template_dir = d.pop("issue_template_dir", UNSET)

        component = d.pop("component", UNSET)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, None, JIRAProjectCustomFields]
        if _custom_fields is None:
            custom_fields = None
        elif isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = JIRAProjectCustomFields.from_dict(_custom_fields)

        default_assignee = d.pop("default_assignee", UNSET)

        jira_labels = d.pop("jira_labels", UNSET)

        add_vulnerability_id_to_jira_label = d.pop("add_vulnerability_id_to_jira_label", UNSET)

        push_all_issues = d.pop("push_all_issues", UNSET)

        enable_engagement_epic_mapping = d.pop("enable_engagement_epic_mapping", UNSET)

        push_notes = d.pop("push_notes", UNSET)

        product_jira_sla_notification = d.pop("product_jira_sla_notification", UNSET)

        risk_acceptance_expiration_notification = d.pop("risk_acceptance_expiration_notification", UNSET)

        jira_instance = d.pop("jira_instance", UNSET)

        product = d.pop("product", UNSET)

        engagement = d.pop("engagement", UNSET)

        jira_project = cls(
            id=id,
            project_key=project_key,
            issue_template_dir=issue_template_dir,
            component=component,
            custom_fields=custom_fields,
            default_assignee=default_assignee,
            jira_labels=jira_labels,
            add_vulnerability_id_to_jira_label=add_vulnerability_id_to_jira_label,
            push_all_issues=push_all_issues,
            enable_engagement_epic_mapping=enable_engagement_epic_mapping,
            push_notes=push_notes,
            product_jira_sla_notification=product_jira_sla_notification,
            risk_acceptance_expiration_notification=risk_acceptance_expiration_notification,
            jira_instance=jira_instance,
            product=product,
            engagement=engagement,
        )

        jira_project.additional_properties = d
        return jira_project

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

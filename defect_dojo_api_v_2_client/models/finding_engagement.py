import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.finding_engagement_engagement_type import FindingEngagementEngagementType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finding_product import FindingProduct


T = TypeVar("T", bound="FindingEngagement")


@_attrs_define
class FindingEngagement:
    """
    Attributes:
        id (int):
        target_start (datetime.date):
        target_end (datetime.date):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        product (Union[Unset, FindingProduct]):
        branch_tag (Union[Unset, None, str]): Tag or branch of the product the engagement tested.
        engagement_type (Union[Unset, None, FindingEngagementEngagementType]): * `Interactive` - Interactive
            * `CI/CD` - CI/CD
        build_id (Union[Unset, None, str]): Build ID of the product the engagement tested.
        commit_hash (Union[Unset, None, str]): Commit hash from repo
        version (Union[Unset, None, str]): Version of the product the engagement tested.
        created (Optional[datetime.datetime]):
        updated (Optional[datetime.datetime]):
    """

    id: int
    target_start: datetime.date
    target_end: datetime.date
    created: Optional[datetime.datetime]
    updated: Optional[datetime.datetime]
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    product: Union[Unset, "FindingProduct"] = UNSET
    branch_tag: Union[Unset, None, str] = UNSET
    engagement_type: Union[Unset, None, FindingEngagementEngagementType] = UNSET
    build_id: Union[Unset, None, str] = UNSET
    commit_hash: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        target_start = self.target_start.isoformat()
        target_end = self.target_end.isoformat()
        name = self.name
        description = self.description
        product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        branch_tag = self.branch_tag
        engagement_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.engagement_type, Unset):
            engagement_type = self.engagement_type.value if self.engagement_type else None

        build_id = self.build_id
        commit_hash = self.commit_hash
        version = self.version
        created = self.created.isoformat() if self.created else None

        updated = self.updated.isoformat() if self.updated else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "target_start": target_start,
                "target_end": target_end,
                "created": created,
                "updated": updated,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if product is not UNSET:
            field_dict["product"] = product
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag
        if engagement_type is not UNSET:
            field_dict["engagement_type"] = engagement_type
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.finding_product import FindingProduct

        d = src_dict.copy()
        id = d.pop("id")

        target_start = isoparse(d.pop("target_start")).date()

        target_end = isoparse(d.pop("target_end")).date()

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _product = d.pop("product", UNSET)
        product: Union[Unset, FindingProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = FindingProduct.from_dict(_product)

        branch_tag = d.pop("branch_tag", UNSET)

        _engagement_type = d.pop("engagement_type", UNSET)
        engagement_type: Union[Unset, None, FindingEngagementEngagementType]
        if _engagement_type is None:
            engagement_type = None
        elif isinstance(_engagement_type, Unset):
            engagement_type = UNSET
        else:
            engagement_type = FindingEngagementEngagementType(_engagement_type)

        build_id = d.pop("build_id", UNSET)

        commit_hash = d.pop("commit_hash", UNSET)

        version = d.pop("version", UNSET)

        _created = d.pop("created")
        created: Optional[datetime.datetime]
        if _created is None:
            created = None
        else:
            created = isoparse(_created)

        _updated = d.pop("updated")
        updated: Optional[datetime.datetime]
        if _updated is None:
            updated = None
        else:
            updated = isoparse(_updated)

        finding_engagement = cls(
            id=id,
            target_start=target_start,
            target_end=target_end,
            name=name,
            description=description,
            product=product,
            branch_tag=branch_tag,
            engagement_type=engagement_type,
            build_id=build_id,
            commit_hash=commit_hash,
            version=version,
            created=created,
            updated=updated,
        )

        finding_engagement.additional_properties = d
        return finding_engagement

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

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finding_engagement import FindingEngagement
    from ..models.finding_environment import FindingEnvironment
    from ..models.finding_test_type import FindingTestType


T = TypeVar("T", bound="FindingTest")


@_attrs_define
class FindingTest:
    """
    Attributes:
        id (int):
        title (Union[Unset, None, str]):
        test_type (Union[Unset, FindingTestType]):
        engagement (Union[Unset, FindingEngagement]):
        environment (Union[Unset, FindingEnvironment]):
        branch_tag (Union[Unset, None, str]): Tag or branch that was tested, a reimport may update this field.
        build_id (Union[Unset, None, str]): Build ID that was tested, a reimport may update this field.
        commit_hash (Union[Unset, None, str]): Commit hash tested, a reimport may update this field.
        version (Union[Unset, None, str]):
    """

    id: int
    title: Union[Unset, None, str] = UNSET
    test_type: Union[Unset, "FindingTestType"] = UNSET
    engagement: Union[Unset, "FindingEngagement"] = UNSET
    environment: Union[Unset, "FindingEnvironment"] = UNSET
    branch_tag: Union[Unset, None, str] = UNSET
    build_id: Union[Unset, None, str] = UNSET
    commit_hash: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        test_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.test_type, Unset):
            test_type = self.test_type.to_dict()

        engagement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.engagement, Unset):
            engagement = self.engagement.to_dict()

        environment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        branch_tag = self.branch_tag
        build_id = self.build_id
        commit_hash = self.commit_hash
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if test_type is not UNSET:
            field_dict["test_type"] = test_type
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if environment is not UNSET:
            field_dict["environment"] = environment
        if branch_tag is not UNSET:
            field_dict["branch_tag"] = branch_tag
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.finding_engagement import FindingEngagement
        from ..models.finding_environment import FindingEnvironment
        from ..models.finding_test_type import FindingTestType

        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title", UNSET)

        _test_type = d.pop("test_type", UNSET)
        test_type: Union[Unset, FindingTestType]
        if isinstance(_test_type, Unset):
            test_type = UNSET
        else:
            test_type = FindingTestType.from_dict(_test_type)

        _engagement = d.pop("engagement", UNSET)
        engagement: Union[Unset, FindingEngagement]
        if isinstance(_engagement, Unset):
            engagement = UNSET
        else:
            engagement = FindingEngagement.from_dict(_engagement)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, FindingEnvironment]
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = FindingEnvironment.from_dict(_environment)

        branch_tag = d.pop("branch_tag", UNSET)

        build_id = d.pop("build_id", UNSET)

        commit_hash = d.pop("commit_hash", UNSET)

        version = d.pop("version", UNSET)

        finding_test = cls(
            id=id,
            title=title,
            test_type=test_type,
            engagement=engagement,
            environment=environment,
            branch_tag=branch_tag,
            build_id=build_id,
            commit_hash=commit_hash,
            version=version,
        )

        finding_test.additional_properties = d
        return finding_test

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

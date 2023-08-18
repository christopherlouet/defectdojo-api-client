from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointMetaImporter")


@_attrs_define
class EndpointMetaImporter:
    """
    Attributes:
        file (str):
        product_id (int):
        create_endpoints (Union[Unset, bool]):  Default: True.
        create_tags (Union[Unset, bool]):  Default: True.
        create_dojo_meta (Union[Unset, bool]):
        product_name (Union[Unset, str]):
        product (Union[Unset, int]):
    """

    file: str
    product_id: int
    create_endpoints: Union[Unset, bool] = True
    create_tags: Union[Unset, bool] = True
    create_dojo_meta: Union[Unset, bool] = False
    product_name: Union[Unset, str] = UNSET
    product: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file = self.file
        product_id = self.product_id
        create_endpoints = self.create_endpoints
        create_tags = self.create_tags
        create_dojo_meta = self.create_dojo_meta
        product_name = self.product_name
        product = self.product

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "product_id": product_id,
            }
        )
        if create_endpoints is not UNSET:
            field_dict["create_endpoints"] = create_endpoints
        if create_tags is not UNSET:
            field_dict["create_tags"] = create_tags
        if create_dojo_meta is not UNSET:
            field_dict["create_dojo_meta"] = create_dojo_meta
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file = d.pop("file")

        product_id = d.pop("product_id")

        create_endpoints = d.pop("create_endpoints", UNSET)

        create_tags = d.pop("create_tags", UNSET)

        create_dojo_meta = d.pop("create_dojo_meta", UNSET)

        product_name = d.pop("product_name", UNSET)

        product = d.pop("product", UNSET)

        endpoint_meta_importer = cls(
            file=file,
            product_id=product_id,
            create_endpoints=create_endpoints,
            create_tags=create_tags,
            create_dojo_meta=create_dojo_meta,
            product_name=product_name,
            product=product,
        )

        endpoint_meta_importer.additional_properties = d
        return endpoint_meta_importer

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

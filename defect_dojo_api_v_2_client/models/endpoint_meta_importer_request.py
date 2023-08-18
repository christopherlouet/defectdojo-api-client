from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="EndpointMetaImporterRequest")


@_attrs_define
class EndpointMetaImporterRequest:
    """
    Attributes:
        file (File):
        create_endpoints (Union[Unset, bool]):  Default: True.
        create_tags (Union[Unset, bool]):  Default: True.
        create_dojo_meta (Union[Unset, bool]):
        product_name (Union[Unset, str]):
        product (Union[Unset, int]):
    """

    file: File
    create_endpoints: Union[Unset, bool] = True
    create_tags: Union[Unset, bool] = True
    create_dojo_meta: Union[Unset, bool] = False
    product_name: Union[Unset, str] = UNSET
    product: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

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

    def to_multipart(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        create_endpoints = (
            self.create_endpoints
            if isinstance(self.create_endpoints, Unset)
            else (None, str(self.create_endpoints).encode(), "text/plain")
        )
        create_tags = (
            self.create_tags
            if isinstance(self.create_tags, Unset)
            else (None, str(self.create_tags).encode(), "text/plain")
        )
        create_dojo_meta = (
            self.create_dojo_meta
            if isinstance(self.create_dojo_meta, Unset)
            else (None, str(self.create_dojo_meta).encode(), "text/plain")
        )
        product_name = (
            self.product_name
            if isinstance(self.product_name, Unset)
            else (None, str(self.product_name).encode(), "text/plain")
        )
        product = self.product if isinstance(self.product, Unset) else (None, str(self.product).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "file": file,
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
        file = File(payload=BytesIO(d.pop("file")))

        create_endpoints = d.pop("create_endpoints", UNSET)

        create_tags = d.pop("create_tags", UNSET)

        create_dojo_meta = d.pop("create_dojo_meta", UNSET)

        product_name = d.pop("product_name", UNSET)

        product = d.pop("product", UNSET)

        endpoint_meta_importer_request = cls(
            file=file,
            create_endpoints=create_endpoints,
            create_tags=create_tags,
            create_dojo_meta=create_dojo_meta,
            product_name=product_name,
            product=product,
        )

        endpoint_meta_importer_request.additional_properties = d
        return endpoint_meta_importer_request

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

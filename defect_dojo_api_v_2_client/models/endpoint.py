from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Endpoint")


@_attrs_define
class Endpoint:
    """
    Attributes:
        id (int):
        endpoint_params (List[int]):
        findings (List[int]):
        tags (Union[Unset, List[str]]):
        protocol (Union[Unset, None, str]): The communication protocol/scheme such as 'http', 'ftp', 'dns', etc.
        userinfo (Union[Unset, None, str]): User info as 'alice', 'bob', etc.
        host (Union[Unset, None, str]): The host name or IP address. It must not include the port number. For example
            '127.0.0.1', 'localhost', 'yourdomain.com'.
        port (Union[Unset, None, int]): The network port associated with the endpoint.
        path (Union[Unset, None, str]): The location of the resource, it must not start with a '/'. For example
            endpoint/420/edit
        query (Union[Unset, None, str]): The query string, the question mark should be omitted.For example
            'group=4&team=8'
        fragment (Union[Unset, None, str]): The fragment identifier which follows the hash mark. The hash mark should be
            omitted. For example 'section-13', 'paragraph-2'.
        product (Union[Unset, None, int]):
    """

    id: int
    endpoint_params: List[int]
    findings: List[int]
    tags: Union[Unset, List[str]] = UNSET
    protocol: Union[Unset, None, str] = UNSET
    userinfo: Union[Unset, None, str] = UNSET
    host: Union[Unset, None, str] = UNSET
    port: Union[Unset, None, int] = UNSET
    path: Union[Unset, None, str] = UNSET
    query: Union[Unset, None, str] = UNSET
    fragment: Union[Unset, None, str] = UNSET
    product: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        endpoint_params = self.endpoint_params

        findings = self.findings

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        protocol = self.protocol
        userinfo = self.userinfo
        host = self.host
        port = self.port
        path = self.path
        query = self.query
        fragment = self.fragment
        product = self.product

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "endpoint_params": endpoint_params,
                "findings": findings,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if userinfo is not UNSET:
            field_dict["userinfo"] = userinfo
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if path is not UNSET:
            field_dict["path"] = path
        if query is not UNSET:
            field_dict["query"] = query
        if fragment is not UNSET:
            field_dict["fragment"] = fragment
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        endpoint_params = cast(List[int], d.pop("endpoint_params"))

        findings = cast(List[int], d.pop("findings"))

        tags = cast(List[str], d.pop("tags", UNSET))

        protocol = d.pop("protocol", UNSET)

        userinfo = d.pop("userinfo", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        path = d.pop("path", UNSET)

        query = d.pop("query", UNSET)

        fragment = d.pop("fragment", UNSET)

        product = d.pop("product", UNSET)

        endpoint = cls(
            id=id,
            endpoint_params=endpoint_params,
            findings=findings,
            tags=tags,
            protocol=protocol,
            userinfo=userinfo,
            host=host,
            port=port,
            path=path,
            query=query,
            fragment=fragment,
            product=product,
        )

        endpoint.additional_properties = d
        return endpoint

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

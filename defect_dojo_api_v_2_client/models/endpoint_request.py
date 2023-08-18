import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointRequest")


@_attrs_define
class EndpointRequest:
    """
    Attributes:
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
        field_dict.update({})
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

    def to_multipart(self) -> Dict[str, Any]:
        tags: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = self.tags
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        protocol = (
            self.protocol if isinstance(self.protocol, Unset) else (None, str(self.protocol).encode(), "text/plain")
        )
        userinfo = (
            self.userinfo if isinstance(self.userinfo, Unset) else (None, str(self.userinfo).encode(), "text/plain")
        )
        host = self.host if isinstance(self.host, Unset) else (None, str(self.host).encode(), "text/plain")
        port = self.port if isinstance(self.port, Unset) else (None, str(self.port).encode(), "text/plain")
        path = self.path if isinstance(self.path, Unset) else (None, str(self.path).encode(), "text/plain")
        query = self.query if isinstance(self.query, Unset) else (None, str(self.query).encode(), "text/plain")
        fragment = (
            self.fragment if isinstance(self.fragment, Unset) else (None, str(self.fragment).encode(), "text/plain")
        )
        product = self.product if isinstance(self.product, Unset) else (None, str(self.product).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
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
        tags = cast(List[str], d.pop("tags", UNSET))

        protocol = d.pop("protocol", UNSET)

        userinfo = d.pop("userinfo", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        path = d.pop("path", UNSET)

        query = d.pop("query", UNSET)

        fragment = d.pop("fragment", UNSET)

        product = d.pop("product", UNSET)

        endpoint_request = cls(
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

        endpoint_request.additional_properties = d
        return endpoint_request

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

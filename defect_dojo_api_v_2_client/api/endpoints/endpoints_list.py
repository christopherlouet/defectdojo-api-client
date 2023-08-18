from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.endpoints_list_o_item import EndpointsListOItem
from ...models.paginated_endpoint_list import PaginatedEndpointList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fragment: Union[Unset, None, str] = UNSET,
    host: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[EndpointsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    port: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    protocol: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    userinfo: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fragment"] = fragment

    params["host"] = host

    params["id"] = id

    params["limit"] = limit

    params["not_tag"] = not_tag

    json_not_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(not_tags, Unset):
        if not_tags is None:
            json_not_tags = None
        else:
            json_not_tags = not_tags

    params["not_tags"] = json_not_tags

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

    params["path"] = path

    params["port"] = port

    params["product"] = product

    params["protocol"] = protocol

    params["query"] = query

    params["tag"] = tag

    json_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(tags, Unset):
        if tags is None:
            json_tags = None
        else:
            json_tags = tags

    params["tags"] = json_tags

    params["userinfo"] = userinfo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/endpoints/",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedEndpointList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedEndpointList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedEndpointList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    fragment: Union[Unset, None, str] = UNSET,
    host: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[EndpointsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    port: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    protocol: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    userinfo: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedEndpointList]:
    """
    Args:
        fragment (Union[Unset, None, str]):
        host (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[EndpointsListOItem]]):
        offset (Union[Unset, None, int]):
        path (Union[Unset, None, str]):
        port (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        protocol (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        userinfo (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEndpointList]
    """

    kwargs = _get_kwargs(
        fragment=fragment,
        host=host,
        id=id,
        limit=limit,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        path=path,
        port=port,
        product=product,
        protocol=protocol,
        query=query,
        tag=tag,
        tags=tags,
        userinfo=userinfo,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    fragment: Union[Unset, None, str] = UNSET,
    host: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[EndpointsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    port: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    protocol: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    userinfo: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedEndpointList]:
    """
    Args:
        fragment (Union[Unset, None, str]):
        host (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[EndpointsListOItem]]):
        offset (Union[Unset, None, int]):
        path (Union[Unset, None, str]):
        port (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        protocol (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        userinfo (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEndpointList
    """

    return sync_detailed(
        client=client,
        fragment=fragment,
        host=host,
        id=id,
        limit=limit,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        path=path,
        port=port,
        product=product,
        protocol=protocol,
        query=query,
        tag=tag,
        tags=tags,
        userinfo=userinfo,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    fragment: Union[Unset, None, str] = UNSET,
    host: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[EndpointsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    port: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    protocol: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    userinfo: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedEndpointList]:
    """
    Args:
        fragment (Union[Unset, None, str]):
        host (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[EndpointsListOItem]]):
        offset (Union[Unset, None, int]):
        path (Union[Unset, None, str]):
        port (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        protocol (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        userinfo (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEndpointList]
    """

    kwargs = _get_kwargs(
        fragment=fragment,
        host=host,
        id=id,
        limit=limit,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        path=path,
        port=port,
        product=product,
        protocol=protocol,
        query=query,
        tag=tag,
        tags=tags,
        userinfo=userinfo,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    fragment: Union[Unset, None, str] = UNSET,
    host: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[EndpointsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    port: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    protocol: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    userinfo: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedEndpointList]:
    """
    Args:
        fragment (Union[Unset, None, str]):
        host (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[EndpointsListOItem]]):
        offset (Union[Unset, None, int]):
        path (Union[Unset, None, str]):
        port (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        protocol (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        userinfo (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEndpointList
    """

    return (
        await asyncio_detailed(
            client=client,
            fragment=fragment,
            host=host,
            id=id,
            limit=limit,
            not_tag=not_tag,
            not_tags=not_tags,
            o=o,
            offset=offset,
            path=path,
            port=port,
            product=product,
            protocol=protocol,
            query=query,
            tag=tag,
            tags=tags,
            userinfo=userinfo,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metadata_list_prefetch_item import MetadataListPrefetchItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    endpoint: Union[Unset, None, int] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    prefetch: Union[Unset, None, List[MetadataListPrefetchItem]] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    value: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["endpoint"] = endpoint

    params["finding"] = finding

    params["id"] = id

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    json_prefetch: Union[Unset, None, List[str]] = UNSET
    if not isinstance(prefetch, Unset):
        if prefetch is None:
            json_prefetch = None
        else:
            json_prefetch = []
            for prefetch_item_data in prefetch:
                prefetch_item = prefetch_item_data.value

                json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    params["product"] = product

    params["value"] = value

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/metadata/",
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    endpoint: Union[Unset, None, int] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    prefetch: Union[Unset, None, List[MetadataListPrefetchItem]] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    value: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        endpoint (Union[Unset, None, int]):
        finding (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        prefetch (Union[Unset, None, List[MetadataListPrefetchItem]]):
        product (Union[Unset, None, int]):
        value (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        endpoint=endpoint,
        finding=finding,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        product=product,
        value=value,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    endpoint: Union[Unset, None, int] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    prefetch: Union[Unset, None, List[MetadataListPrefetchItem]] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    value: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        endpoint (Union[Unset, None, int]):
        finding (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        prefetch (Union[Unset, None, List[MetadataListPrefetchItem]]):
        product (Union[Unset, None, int]):
        value (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        endpoint=endpoint,
        finding=finding,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        product=product,
        value=value,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

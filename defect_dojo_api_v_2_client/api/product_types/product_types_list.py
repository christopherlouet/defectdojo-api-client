import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.product_types_list_prefetch_item import ProductTypesListPrefetchItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created: Union[Unset, None, datetime.datetime] = UNSET,
    critical_product: Union[Unset, None, bool] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    key_product: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    prefetch: Union[Unset, None, List[ProductTypesListPrefetchItem]] = UNSET,
    updated: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_created: Union[Unset, None, str] = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat() if created else None

    params["created"] = json_created

    params["critical_product"] = critical_product

    params["id"] = id

    params["key_product"] = key_product

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

    json_updated: Union[Unset, None, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat() if updated else None

    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/product_types/",
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
    created: Union[Unset, None, datetime.datetime] = UNSET,
    critical_product: Union[Unset, None, bool] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    key_product: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    prefetch: Union[Unset, None, List[ProductTypesListPrefetchItem]] = UNSET,
    updated: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Any]:
    """
    Args:
        created (Union[Unset, None, datetime.datetime]):
        critical_product (Union[Unset, None, bool]):
        id (Union[Unset, None, int]):
        key_product (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        prefetch (Union[Unset, None, List[ProductTypesListPrefetchItem]]):
        updated (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        created=created,
        critical_product=critical_product,
        id=id,
        key_product=key_product,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        updated=updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, None, datetime.datetime] = UNSET,
    critical_product: Union[Unset, None, bool] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    key_product: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    prefetch: Union[Unset, None, List[ProductTypesListPrefetchItem]] = UNSET,
    updated: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Any]:
    """
    Args:
        created (Union[Unset, None, datetime.datetime]):
        critical_product (Union[Unset, None, bool]):
        id (Union[Unset, None, int]):
        key_product (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        prefetch (Union[Unset, None, List[ProductTypesListPrefetchItem]]):
        updated (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        created=created,
        critical_product=critical_product,
        id=id,
        key_product=key_product,
        limit=limit,
        name=name,
        offset=offset,
        prefetch=prefetch,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

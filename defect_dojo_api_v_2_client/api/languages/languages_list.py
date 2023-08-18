from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.languages_list_prefetch_item import LanguagesListPrefetchItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: Union[Unset, None, int] = UNSET,
    language: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    prefetch: Union[Unset, None, List[LanguagesListPrefetchItem]] = UNSET,
    product: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["id"] = id

    params["language"] = language

    params["limit"] = limit

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/languages/",
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
    id: Union[Unset, None, int] = UNSET,
    language: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    prefetch: Union[Unset, None, List[LanguagesListPrefetchItem]] = UNSET,
    product: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        id (Union[Unset, None, int]):
        language (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        prefetch (Union[Unset, None, List[LanguagesListPrefetchItem]]):
        product (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        language=language,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product=product,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, None, int] = UNSET,
    language: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    prefetch: Union[Unset, None, List[LanguagesListPrefetchItem]] = UNSET,
    product: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        id (Union[Unset, None, int]):
        language (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        prefetch (Union[Unset, None, List[LanguagesListPrefetchItem]]):
        product (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        language=language,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        product=product,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

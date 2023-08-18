from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_engagement_presets_list import PaginatedEngagementPresetsList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["id"] = id

    params["limit"] = limit

    params["offset"] = offset

    params["product"] = product

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/engagement_presets/",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedEngagementPresetsList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedEngagementPresetsList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedEngagementPresetsList]:
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
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedEngagementPresetsList]:
    """
    Args:
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEngagementPresetsList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        product=product,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedEngagementPresetsList]:
    """
    Args:
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEngagementPresetsList
    """

    return sync_detailed(
        client=client,
        id=id,
        limit=limit,
        offset=offset,
        product=product,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedEngagementPresetsList]:
    """
    Args:
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEngagementPresetsList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        product=product,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedEngagementPresetsList]:
    """
    Args:
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEngagementPresetsList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            limit=limit,
            offset=offset,
            product=product,
            title=title,
        )
    ).parsed

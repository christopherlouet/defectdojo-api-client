from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: Union[Unset, None, int] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["id"] = id

    params["key"] = key

    params["limit"] = limit

    params["offset"] = offset

    params["status"] = status

    params["type"] = type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/sonarqube_issues/",
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
    key: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        id (Union[Unset, None, int]):
        key (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        status (Union[Unset, None, str]):
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        key=key,
        limit=limit,
        offset=offset,
        status=status,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, None, int] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        id (Union[Unset, None, int]):
        key (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        status (Union[Unset, None, str]):
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        key=key,
        limit=limit,
        offset=offset,
        status=status,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

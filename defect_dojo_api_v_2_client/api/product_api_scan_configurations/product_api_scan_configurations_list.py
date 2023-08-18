from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    service_key_1: Union[Unset, None, str] = UNSET,
    service_key_2: Union[Unset, None, str] = UNSET,
    service_key_3: Union[Unset, None, str] = UNSET,
    tool_configuration: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["id"] = id

    params["limit"] = limit

    params["offset"] = offset

    params["product"] = product

    params["service_key_1"] = service_key_1

    params["service_key_2"] = service_key_2

    params["service_key_3"] = service_key_3

    params["tool_configuration"] = tool_configuration

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/product_api_scan_configurations/",
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
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    service_key_1: Union[Unset, None, str] = UNSET,
    service_key_2: Union[Unset, None, str] = UNSET,
    service_key_3: Union[Unset, None, str] = UNSET,
    tool_configuration: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        service_key_1 (Union[Unset, None, str]):
        service_key_2 (Union[Unset, None, str]):
        service_key_3 (Union[Unset, None, str]):
        tool_configuration (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        product=product,
        service_key_1=service_key_1,
        service_key_2=service_key_2,
        service_key_3=service_key_3,
        tool_configuration=tool_configuration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    service_key_1: Union[Unset, None, str] = UNSET,
    service_key_2: Union[Unset, None, str] = UNSET,
    service_key_3: Union[Unset, None, str] = UNSET,
    tool_configuration: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        service_key_1 (Union[Unset, None, str]):
        service_key_2 (Union[Unset, None, str]):
        service_key_3 (Union[Unset, None, str]):
        tool_configuration (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        product=product,
        service_key_1=service_key_1,
        service_key_2=service_key_2,
        service_key_3=service_key_3,
        tool_configuration=tool_configuration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

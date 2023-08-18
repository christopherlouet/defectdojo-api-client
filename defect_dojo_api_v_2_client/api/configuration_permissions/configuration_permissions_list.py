from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_configuration_permission_list import PaginatedConfigurationPermissionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    codename: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["codename"] = codename

    params["id"] = id

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/configuration_permissions/",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedConfigurationPermissionList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedConfigurationPermissionList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedConfigurationPermissionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    codename: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedConfigurationPermissionList]:
    """
    Args:
        codename (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConfigurationPermissionList]
    """

    kwargs = _get_kwargs(
        codename=codename,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    codename: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedConfigurationPermissionList]:
    """
    Args:
        codename (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConfigurationPermissionList
    """

    return sync_detailed(
        client=client,
        codename=codename,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    codename: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedConfigurationPermissionList]:
    """
    Args:
        codename (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConfigurationPermissionList]
    """

    kwargs = _get_kwargs(
        codename=codename,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    codename: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedConfigurationPermissionList]:
    """
    Args:
        codename (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConfigurationPermissionList
    """

    return (
        await asyncio_detailed(
            client=client,
            codename=codename,
            id=id,
            limit=limit,
            name=name,
            offset=offset,
        )
    ).parsed

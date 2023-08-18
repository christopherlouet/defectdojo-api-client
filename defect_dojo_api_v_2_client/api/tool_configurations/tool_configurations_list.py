from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tool_configurations_list_authentication_type import ToolConfigurationsListAuthenticationType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authentication_type: Union[Unset, None, ToolConfigurationsListAuthenticationType] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    tool_type: Union[Unset, None, int] = UNSET,
    url_query: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_authentication_type: Union[Unset, None, str] = UNSET
    if not isinstance(authentication_type, Unset):
        json_authentication_type = authentication_type.value if authentication_type else None

    params["authentication_type"] = json_authentication_type

    params["id"] = id

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    params["tool_type"] = tool_type

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/tool_configurations/",
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
    authentication_type: Union[Unset, None, ToolConfigurationsListAuthenticationType] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    tool_type: Union[Unset, None, int] = UNSET,
    url_query: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        authentication_type (Union[Unset, None, ToolConfigurationsListAuthenticationType]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        tool_type (Union[Unset, None, int]):
        url_query (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        authentication_type=authentication_type,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        tool_type=tool_type,
        url_query=url_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    authentication_type: Union[Unset, None, ToolConfigurationsListAuthenticationType] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    tool_type: Union[Unset, None, int] = UNSET,
    url_query: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        authentication_type (Union[Unset, None, ToolConfigurationsListAuthenticationType]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        tool_type (Union[Unset, None, int]):
        url_query (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        authentication_type=authentication_type,
        id=id,
        limit=limit,
        name=name,
        offset=offset,
        tool_type=tool_type,
        url_query=url_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

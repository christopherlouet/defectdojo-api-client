from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_endpoint_status_list import PaginatedEndpointStatusList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    endpoint: Union[Unset, None, int] = UNSET,
    false_positive: Union[Unset, None, bool] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    mitigated: Union[Unset, None, bool] = UNSET,
    mitigated_by: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    out_of_scope: Union[Unset, None, bool] = UNSET,
    risk_accepted: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["endpoint"] = endpoint

    params["false_positive"] = false_positive

    params["finding"] = finding

    params["limit"] = limit

    params["mitigated"] = mitigated

    params["mitigated_by"] = mitigated_by

    params["offset"] = offset

    params["out_of_scope"] = out_of_scope

    params["risk_accepted"] = risk_accepted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/endpoint_status/",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedEndpointStatusList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedEndpointStatusList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedEndpointStatusList]:
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
    false_positive: Union[Unset, None, bool] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    mitigated: Union[Unset, None, bool] = UNSET,
    mitigated_by: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    out_of_scope: Union[Unset, None, bool] = UNSET,
    risk_accepted: Union[Unset, None, bool] = UNSET,
) -> Response[PaginatedEndpointStatusList]:
    """
    Args:
        endpoint (Union[Unset, None, int]):
        false_positive (Union[Unset, None, bool]):
        finding (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        mitigated (Union[Unset, None, bool]):
        mitigated_by (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        out_of_scope (Union[Unset, None, bool]):
        risk_accepted (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEndpointStatusList]
    """

    kwargs = _get_kwargs(
        endpoint=endpoint,
        false_positive=false_positive,
        finding=finding,
        limit=limit,
        mitigated=mitigated,
        mitigated_by=mitigated_by,
        offset=offset,
        out_of_scope=out_of_scope,
        risk_accepted=risk_accepted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    endpoint: Union[Unset, None, int] = UNSET,
    false_positive: Union[Unset, None, bool] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    mitigated: Union[Unset, None, bool] = UNSET,
    mitigated_by: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    out_of_scope: Union[Unset, None, bool] = UNSET,
    risk_accepted: Union[Unset, None, bool] = UNSET,
) -> Optional[PaginatedEndpointStatusList]:
    """
    Args:
        endpoint (Union[Unset, None, int]):
        false_positive (Union[Unset, None, bool]):
        finding (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        mitigated (Union[Unset, None, bool]):
        mitigated_by (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        out_of_scope (Union[Unset, None, bool]):
        risk_accepted (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEndpointStatusList
    """

    return sync_detailed(
        client=client,
        endpoint=endpoint,
        false_positive=false_positive,
        finding=finding,
        limit=limit,
        mitigated=mitigated,
        mitigated_by=mitigated_by,
        offset=offset,
        out_of_scope=out_of_scope,
        risk_accepted=risk_accepted,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    endpoint: Union[Unset, None, int] = UNSET,
    false_positive: Union[Unset, None, bool] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    mitigated: Union[Unset, None, bool] = UNSET,
    mitigated_by: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    out_of_scope: Union[Unset, None, bool] = UNSET,
    risk_accepted: Union[Unset, None, bool] = UNSET,
) -> Response[PaginatedEndpointStatusList]:
    """
    Args:
        endpoint (Union[Unset, None, int]):
        false_positive (Union[Unset, None, bool]):
        finding (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        mitigated (Union[Unset, None, bool]):
        mitigated_by (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        out_of_scope (Union[Unset, None, bool]):
        risk_accepted (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEndpointStatusList]
    """

    kwargs = _get_kwargs(
        endpoint=endpoint,
        false_positive=false_positive,
        finding=finding,
        limit=limit,
        mitigated=mitigated,
        mitigated_by=mitigated_by,
        offset=offset,
        out_of_scope=out_of_scope,
        risk_accepted=risk_accepted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    endpoint: Union[Unset, None, int] = UNSET,
    false_positive: Union[Unset, None, bool] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    mitigated: Union[Unset, None, bool] = UNSET,
    mitigated_by: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    out_of_scope: Union[Unset, None, bool] = UNSET,
    risk_accepted: Union[Unset, None, bool] = UNSET,
) -> Optional[PaginatedEndpointStatusList]:
    """
    Args:
        endpoint (Union[Unset, None, int]):
        false_positive (Union[Unset, None, bool]):
        finding (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        mitigated (Union[Unset, None, bool]):
        mitigated_by (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        out_of_scope (Union[Unset, None, bool]):
        risk_accepted (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEndpointStatusList
    """

    return (
        await asyncio_detailed(
            client=client,
            endpoint=endpoint,
            false_positive=false_positive,
            finding=finding,
            limit=limit,
            mitigated=mitigated,
            mitigated_by=mitigated_by,
            offset=offset,
            out_of_scope=out_of_scope,
            risk_accepted=risk_accepted,
        )
    ).parsed

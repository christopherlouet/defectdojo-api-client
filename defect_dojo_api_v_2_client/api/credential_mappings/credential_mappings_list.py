from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_credential_mapping_list import PaginatedCredentialMappingList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cred_id: Union[Unset, None, int] = UNSET,
    engagement: Union[Unset, None, int] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    is_authn_provider: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    test: Union[Unset, None, int] = UNSET,
    url_query: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["cred_id"] = cred_id

    params["engagement"] = engagement

    params["finding"] = finding

    params["is_authn_provider"] = is_authn_provider

    params["limit"] = limit

    params["offset"] = offset

    params["product"] = product

    params["test"] = test

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/credential_mappings/",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedCredentialMappingList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedCredentialMappingList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedCredentialMappingList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cred_id: Union[Unset, None, int] = UNSET,
    engagement: Union[Unset, None, int] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    is_authn_provider: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    test: Union[Unset, None, int] = UNSET,
    url_query: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedCredentialMappingList]:
    """
    Args:
        cred_id (Union[Unset, None, int]):
        engagement (Union[Unset, None, int]):
        finding (Union[Unset, None, int]):
        is_authn_provider (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        test (Union[Unset, None, int]):
        url_query (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCredentialMappingList]
    """

    kwargs = _get_kwargs(
        cred_id=cred_id,
        engagement=engagement,
        finding=finding,
        is_authn_provider=is_authn_provider,
        limit=limit,
        offset=offset,
        product=product,
        test=test,
        url_query=url_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cred_id: Union[Unset, None, int] = UNSET,
    engagement: Union[Unset, None, int] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    is_authn_provider: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    test: Union[Unset, None, int] = UNSET,
    url_query: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedCredentialMappingList]:
    """
    Args:
        cred_id (Union[Unset, None, int]):
        engagement (Union[Unset, None, int]):
        finding (Union[Unset, None, int]):
        is_authn_provider (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        test (Union[Unset, None, int]):
        url_query (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCredentialMappingList
    """

    return sync_detailed(
        client=client,
        cred_id=cred_id,
        engagement=engagement,
        finding=finding,
        is_authn_provider=is_authn_provider,
        limit=limit,
        offset=offset,
        product=product,
        test=test,
        url_query=url_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cred_id: Union[Unset, None, int] = UNSET,
    engagement: Union[Unset, None, int] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    is_authn_provider: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    test: Union[Unset, None, int] = UNSET,
    url_query: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedCredentialMappingList]:
    """
    Args:
        cred_id (Union[Unset, None, int]):
        engagement (Union[Unset, None, int]):
        finding (Union[Unset, None, int]):
        is_authn_provider (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        test (Union[Unset, None, int]):
        url_query (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCredentialMappingList]
    """

    kwargs = _get_kwargs(
        cred_id=cred_id,
        engagement=engagement,
        finding=finding,
        is_authn_provider=is_authn_provider,
        limit=limit,
        offset=offset,
        product=product,
        test=test,
        url_query=url_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cred_id: Union[Unset, None, int] = UNSET,
    engagement: Union[Unset, None, int] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    is_authn_provider: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    test: Union[Unset, None, int] = UNSET,
    url_query: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedCredentialMappingList]:
    """
    Args:
        cred_id (Union[Unset, None, int]):
        engagement (Union[Unset, None, int]):
        finding (Union[Unset, None, int]):
        is_authn_provider (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        test (Union[Unset, None, int]):
        url_query (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCredentialMappingList
    """

    return (
        await asyncio_detailed(
            client=client,
            cred_id=cred_id,
            engagement=engagement,
            finding=finding,
            is_authn_provider=is_authn_provider,
            limit=limit,
            offset=offset,
            product=product,
            test=test,
            url_query=url_query,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_app_analysis_list import PaginatedAppAnalysisList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    user: Union[Unset, None, int] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["name"] = name

    params["not_tag"] = not_tag

    json_not_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(not_tags, Unset):
        if not_tags is None:
            json_not_tags = None
        else:
            json_not_tags = not_tags

    params["not_tags"] = json_not_tags

    params["offset"] = offset

    params["product"] = product

    params["tag"] = tag

    json_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(tags, Unset):
        if tags is None:
            json_tags = None
        else:
            json_tags = tags

    params["tags"] = json_tags

    params["user"] = user

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/technologies/",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedAppAnalysisList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedAppAnalysisList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedAppAnalysisList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    user: Union[Unset, None, int] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedAppAnalysisList]:
    """
    Args:
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        user (Union[Unset, None, int]):
        version (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAppAnalysisList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        name=name,
        not_tag=not_tag,
        not_tags=not_tags,
        offset=offset,
        product=product,
        tag=tag,
        tags=tags,
        user=user,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    user: Union[Unset, None, int] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedAppAnalysisList]:
    """
    Args:
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        user (Union[Unset, None, int]):
        version (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAppAnalysisList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        name=name,
        not_tag=not_tag,
        not_tags=not_tags,
        offset=offset,
        product=product,
        tag=tag,
        tags=tags,
        user=user,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    user: Union[Unset, None, int] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedAppAnalysisList]:
    """
    Args:
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        user (Union[Unset, None, int]):
        version (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAppAnalysisList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        name=name,
        not_tag=not_tag,
        not_tags=not_tags,
        offset=offset,
        product=product,
        tag=tag,
        tags=tags,
        user=user,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    user: Union[Unset, None, int] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedAppAnalysisList]:
    """
    Args:
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        user (Union[Unset, None, int]):
        version (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAppAnalysisList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            name=name,
            not_tag=not_tag,
            not_tags=not_tags,
            offset=offset,
            product=product,
            tag=tag,
            tags=tags,
            user=user,
            version=version,
        )
    ).parsed

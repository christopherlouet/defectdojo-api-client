import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.engagements_list_o_item import EngagementsListOItem
from ...models.engagements_list_status import EngagementsListStatus
from ...models.paginated_engagement_list import PaginatedEngagementList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active: Union[Unset, None, bool] = UNSET,
    api_test: Union[Unset, None, bool] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    not_product_tags: Union[Unset, None, List[str]] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[EngagementsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    pen_test: Union[Unset, None, bool] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    product_prod_type: Union[Unset, None, List[int]] = UNSET,
    product_tags: Union[Unset, None, List[str]] = UNSET,
    report_type: Union[Unset, None, int] = UNSET,
    requester: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, EngagementsListStatus] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    target_end: Union[Unset, None, datetime.date] = UNSET,
    target_start: Union[Unset, None, datetime.date] = UNSET,
    threat_model: Union[Unset, None, bool] = UNSET,
    updated: Union[Unset, None, datetime.datetime] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["active"] = active

    params["api_test"] = api_test

    params["id"] = id

    params["limit"] = limit

    params["name"] = name

    json_not_product_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(not_product_tags, Unset):
        if not_product_tags is None:
            json_not_product_tags = None
        else:
            json_not_product_tags = not_product_tags

    params["not_product__tags"] = json_not_product_tags

    params["not_tag"] = not_tag

    json_not_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(not_tags, Unset):
        if not_tags is None:
            json_not_tags = None
        else:
            json_not_tags = not_tags

    params["not_tags"] = json_not_tags

    json_o: Union[Unset, None, List[str]] = UNSET
    if not isinstance(o, Unset):
        if o is None:
            json_o = None
        else:
            json_o = []
            for o_item_data in o:
                o_item = o_item_data.value

                json_o.append(o_item)

    params["o"] = json_o

    params["offset"] = offset

    params["pen_test"] = pen_test

    params["product"] = product

    json_product_prod_type: Union[Unset, None, List[int]] = UNSET
    if not isinstance(product_prod_type, Unset):
        if product_prod_type is None:
            json_product_prod_type = None
        else:
            json_product_prod_type = product_prod_type

    params["product__prod_type"] = json_product_prod_type

    json_product_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(product_tags, Unset):
        if product_tags is None:
            json_product_tags = None
        else:
            json_product_tags = product_tags

    params["product__tags"] = json_product_tags

    params["report_type"] = report_type

    params["requester"] = requester

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    params["tag"] = tag

    json_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(tags, Unset):
        if tags is None:
            json_tags = None
        else:
            json_tags = tags

    params["tags"] = json_tags

    json_target_end: Union[Unset, None, str] = UNSET
    if not isinstance(target_end, Unset):
        json_target_end = target_end.isoformat() if target_end else None

    params["target_end"] = json_target_end

    json_target_start: Union[Unset, None, str] = UNSET
    if not isinstance(target_start, Unset):
        json_target_start = target_start.isoformat() if target_start else None

    params["target_start"] = json_target_start

    params["threat_model"] = threat_model

    json_updated: Union[Unset, None, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat() if updated else None

    params["updated"] = json_updated

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/engagements/",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedEngagementList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedEngagementList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedEngagementList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    active: Union[Unset, None, bool] = UNSET,
    api_test: Union[Unset, None, bool] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    not_product_tags: Union[Unset, None, List[str]] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[EngagementsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    pen_test: Union[Unset, None, bool] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    product_prod_type: Union[Unset, None, List[int]] = UNSET,
    product_tags: Union[Unset, None, List[str]] = UNSET,
    report_type: Union[Unset, None, int] = UNSET,
    requester: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, EngagementsListStatus] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    target_end: Union[Unset, None, datetime.date] = UNSET,
    target_start: Union[Unset, None, datetime.date] = UNSET,
    threat_model: Union[Unset, None, bool] = UNSET,
    updated: Union[Unset, None, datetime.datetime] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedEngagementList]:
    """
    Args:
        active (Union[Unset, None, bool]):
        api_test (Union[Unset, None, bool]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        not_product_tags (Union[Unset, None, List[str]]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[EngagementsListOItem]]):
        offset (Union[Unset, None, int]):
        pen_test (Union[Unset, None, bool]):
        product (Union[Unset, None, int]):
        product_prod_type (Union[Unset, None, List[int]]):
        product_tags (Union[Unset, None, List[str]]):
        report_type (Union[Unset, None, int]):
        requester (Union[Unset, None, int]):
        status (Union[Unset, None, EngagementsListStatus]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        target_end (Union[Unset, None, datetime.date]):
        target_start (Union[Unset, None, datetime.date]):
        threat_model (Union[Unset, None, bool]):
        updated (Union[Unset, None, datetime.datetime]):
        version (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEngagementList]
    """

    kwargs = _get_kwargs(
        active=active,
        api_test=api_test,
        id=id,
        limit=limit,
        name=name,
        not_product_tags=not_product_tags,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        pen_test=pen_test,
        product=product,
        product_prod_type=product_prod_type,
        product_tags=product_tags,
        report_type=report_type,
        requester=requester,
        status=status,
        tag=tag,
        tags=tags,
        target_end=target_end,
        target_start=target_start,
        threat_model=threat_model,
        updated=updated,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    active: Union[Unset, None, bool] = UNSET,
    api_test: Union[Unset, None, bool] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    not_product_tags: Union[Unset, None, List[str]] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[EngagementsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    pen_test: Union[Unset, None, bool] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    product_prod_type: Union[Unset, None, List[int]] = UNSET,
    product_tags: Union[Unset, None, List[str]] = UNSET,
    report_type: Union[Unset, None, int] = UNSET,
    requester: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, EngagementsListStatus] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    target_end: Union[Unset, None, datetime.date] = UNSET,
    target_start: Union[Unset, None, datetime.date] = UNSET,
    threat_model: Union[Unset, None, bool] = UNSET,
    updated: Union[Unset, None, datetime.datetime] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedEngagementList]:
    """
    Args:
        active (Union[Unset, None, bool]):
        api_test (Union[Unset, None, bool]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        not_product_tags (Union[Unset, None, List[str]]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[EngagementsListOItem]]):
        offset (Union[Unset, None, int]):
        pen_test (Union[Unset, None, bool]):
        product (Union[Unset, None, int]):
        product_prod_type (Union[Unset, None, List[int]]):
        product_tags (Union[Unset, None, List[str]]):
        report_type (Union[Unset, None, int]):
        requester (Union[Unset, None, int]):
        status (Union[Unset, None, EngagementsListStatus]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        target_end (Union[Unset, None, datetime.date]):
        target_start (Union[Unset, None, datetime.date]):
        threat_model (Union[Unset, None, bool]):
        updated (Union[Unset, None, datetime.datetime]):
        version (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEngagementList
    """

    return sync_detailed(
        client=client,
        active=active,
        api_test=api_test,
        id=id,
        limit=limit,
        name=name,
        not_product_tags=not_product_tags,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        pen_test=pen_test,
        product=product,
        product_prod_type=product_prod_type,
        product_tags=product_tags,
        report_type=report_type,
        requester=requester,
        status=status,
        tag=tag,
        tags=tags,
        target_end=target_end,
        target_start=target_start,
        threat_model=threat_model,
        updated=updated,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    active: Union[Unset, None, bool] = UNSET,
    api_test: Union[Unset, None, bool] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    not_product_tags: Union[Unset, None, List[str]] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[EngagementsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    pen_test: Union[Unset, None, bool] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    product_prod_type: Union[Unset, None, List[int]] = UNSET,
    product_tags: Union[Unset, None, List[str]] = UNSET,
    report_type: Union[Unset, None, int] = UNSET,
    requester: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, EngagementsListStatus] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    target_end: Union[Unset, None, datetime.date] = UNSET,
    target_start: Union[Unset, None, datetime.date] = UNSET,
    threat_model: Union[Unset, None, bool] = UNSET,
    updated: Union[Unset, None, datetime.datetime] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedEngagementList]:
    """
    Args:
        active (Union[Unset, None, bool]):
        api_test (Union[Unset, None, bool]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        not_product_tags (Union[Unset, None, List[str]]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[EngagementsListOItem]]):
        offset (Union[Unset, None, int]):
        pen_test (Union[Unset, None, bool]):
        product (Union[Unset, None, int]):
        product_prod_type (Union[Unset, None, List[int]]):
        product_tags (Union[Unset, None, List[str]]):
        report_type (Union[Unset, None, int]):
        requester (Union[Unset, None, int]):
        status (Union[Unset, None, EngagementsListStatus]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        target_end (Union[Unset, None, datetime.date]):
        target_start (Union[Unset, None, datetime.date]):
        threat_model (Union[Unset, None, bool]):
        updated (Union[Unset, None, datetime.datetime]):
        version (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedEngagementList]
    """

    kwargs = _get_kwargs(
        active=active,
        api_test=api_test,
        id=id,
        limit=limit,
        name=name,
        not_product_tags=not_product_tags,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        pen_test=pen_test,
        product=product,
        product_prod_type=product_prod_type,
        product_tags=product_tags,
        report_type=report_type,
        requester=requester,
        status=status,
        tag=tag,
        tags=tags,
        target_end=target_end,
        target_start=target_start,
        threat_model=threat_model,
        updated=updated,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    active: Union[Unset, None, bool] = UNSET,
    api_test: Union[Unset, None, bool] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    not_product_tags: Union[Unset, None, List[str]] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[EngagementsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    pen_test: Union[Unset, None, bool] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    product_prod_type: Union[Unset, None, List[int]] = UNSET,
    product_tags: Union[Unset, None, List[str]] = UNSET,
    report_type: Union[Unset, None, int] = UNSET,
    requester: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, EngagementsListStatus] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    target_end: Union[Unset, None, datetime.date] = UNSET,
    target_start: Union[Unset, None, datetime.date] = UNSET,
    threat_model: Union[Unset, None, bool] = UNSET,
    updated: Union[Unset, None, datetime.datetime] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedEngagementList]:
    """
    Args:
        active (Union[Unset, None, bool]):
        api_test (Union[Unset, None, bool]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        not_product_tags (Union[Unset, None, List[str]]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[EngagementsListOItem]]):
        offset (Union[Unset, None, int]):
        pen_test (Union[Unset, None, bool]):
        product (Union[Unset, None, int]):
        product_prod_type (Union[Unset, None, List[int]]):
        product_tags (Union[Unset, None, List[str]]):
        report_type (Union[Unset, None, int]):
        requester (Union[Unset, None, int]):
        status (Union[Unset, None, EngagementsListStatus]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        target_end (Union[Unset, None, datetime.date]):
        target_start (Union[Unset, None, datetime.date]):
        threat_model (Union[Unset, None, bool]):
        updated (Union[Unset, None, datetime.datetime]):
        version (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedEngagementList
    """

    return (
        await asyncio_detailed(
            client=client,
            active=active,
            api_test=api_test,
            id=id,
            limit=limit,
            name=name,
            not_product_tags=not_product_tags,
            not_tag=not_tag,
            not_tags=not_tags,
            o=o,
            offset=offset,
            pen_test=pen_test,
            product=product,
            product_prod_type=product_prod_type,
            product_tags=product_tags,
            report_type=report_type,
            requester=requester,
            status=status,
            tag=tag,
            tags=tags,
            target_end=target_end,
            target_start=target_start,
            threat_model=threat_model,
            updated=updated,
            version=version,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.products_list_created import ProductsListCreated
from ...models.products_list_o_item import ProductsListOItem
from ...models.products_list_prefetch_item import ProductsListPrefetchItem
from ...models.products_list_updated import ProductsListUpdated
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    business_criticality: Union[Unset, None, str] = UNSET,
    created: Union[Unset, None, ProductsListCreated] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    external_audience: Union[Unset, None, bool] = UNSET,
    id: Union[Unset, None, List[int]] = UNSET,
    internet_accessible: Union[Unset, None, bool] = UNSET,
    lifecycle: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_exact: Union[Unset, None, str] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[ProductsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    origin: Union[Unset, None, str] = UNSET,
    platform: Union[Unset, None, str] = UNSET,
    prefetch: Union[Unset, None, List[ProductsListPrefetchItem]] = UNSET,
    prod_numeric_grade: Union[Unset, None, List[int]] = UNSET,
    prod_type: Union[Unset, None, List[int]] = UNSET,
    product_manager: Union[Unset, None, List[int]] = UNSET,
    regulations: Union[Unset, None, List[int]] = UNSET,
    revenue: Union[Unset, None, float] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    team_manager: Union[Unset, None, List[int]] = UNSET,
    technical_contact: Union[Unset, None, List[int]] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
    updated: Union[Unset, None, ProductsListUpdated] = UNSET,
    user_records: Union[Unset, None, List[int]] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["business_criticality"] = business_criticality

    json_created: Union[Unset, None, int] = UNSET
    if not isinstance(created, Unset):
        json_created = created.value if created else None

    params["created"] = json_created

    params["description"] = description

    params["external_audience"] = external_audience

    json_id: Union[Unset, None, List[int]] = UNSET
    if not isinstance(id, Unset):
        if id is None:
            json_id = None
        else:
            json_id = id

    params["id"] = json_id

    params["internet_accessible"] = internet_accessible

    params["lifecycle"] = lifecycle

    params["limit"] = limit

    params["name"] = name

    params["name_exact"] = name_exact

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

    params["origin"] = origin

    params["platform"] = platform

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

    json_prod_numeric_grade: Union[Unset, None, List[int]] = UNSET
    if not isinstance(prod_numeric_grade, Unset):
        if prod_numeric_grade is None:
            json_prod_numeric_grade = None
        else:
            json_prod_numeric_grade = prod_numeric_grade

    params["prod_numeric_grade"] = json_prod_numeric_grade

    json_prod_type: Union[Unset, None, List[int]] = UNSET
    if not isinstance(prod_type, Unset):
        if prod_type is None:
            json_prod_type = None
        else:
            json_prod_type = prod_type

    params["prod_type"] = json_prod_type

    json_product_manager: Union[Unset, None, List[int]] = UNSET
    if not isinstance(product_manager, Unset):
        if product_manager is None:
            json_product_manager = None
        else:
            json_product_manager = product_manager

    params["product_manager"] = json_product_manager

    json_regulations: Union[Unset, None, List[int]] = UNSET
    if not isinstance(regulations, Unset):
        if regulations is None:
            json_regulations = None
        else:
            json_regulations = regulations

    params["regulations"] = json_regulations

    params["revenue"] = revenue

    params["tag"] = tag

    json_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(tags, Unset):
        if tags is None:
            json_tags = None
        else:
            json_tags = tags

    params["tags"] = json_tags

    json_team_manager: Union[Unset, None, List[int]] = UNSET
    if not isinstance(team_manager, Unset):
        if team_manager is None:
            json_team_manager = None
        else:
            json_team_manager = team_manager

    params["team_manager"] = json_team_manager

    json_technical_contact: Union[Unset, None, List[int]] = UNSET
    if not isinstance(technical_contact, Unset):
        if technical_contact is None:
            json_technical_contact = None
        else:
            json_technical_contact = technical_contact

    params["technical_contact"] = json_technical_contact

    json_tid: Union[Unset, None, List[int]] = UNSET
    if not isinstance(tid, Unset):
        if tid is None:
            json_tid = None
        else:
            json_tid = tid

    params["tid"] = json_tid

    json_updated: Union[Unset, None, int] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.value if updated else None

    params["updated"] = json_updated

    json_user_records: Union[Unset, None, List[int]] = UNSET
    if not isinstance(user_records, Unset):
        if user_records is None:
            json_user_records = None
        else:
            json_user_records = user_records

    params["user_records"] = json_user_records

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/products/",
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
    business_criticality: Union[Unset, None, str] = UNSET,
    created: Union[Unset, None, ProductsListCreated] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    external_audience: Union[Unset, None, bool] = UNSET,
    id: Union[Unset, None, List[int]] = UNSET,
    internet_accessible: Union[Unset, None, bool] = UNSET,
    lifecycle: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_exact: Union[Unset, None, str] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[ProductsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    origin: Union[Unset, None, str] = UNSET,
    platform: Union[Unset, None, str] = UNSET,
    prefetch: Union[Unset, None, List[ProductsListPrefetchItem]] = UNSET,
    prod_numeric_grade: Union[Unset, None, List[int]] = UNSET,
    prod_type: Union[Unset, None, List[int]] = UNSET,
    product_manager: Union[Unset, None, List[int]] = UNSET,
    regulations: Union[Unset, None, List[int]] = UNSET,
    revenue: Union[Unset, None, float] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    team_manager: Union[Unset, None, List[int]] = UNSET,
    technical_contact: Union[Unset, None, List[int]] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
    updated: Union[Unset, None, ProductsListUpdated] = UNSET,
    user_records: Union[Unset, None, List[int]] = UNSET,
) -> Response[Any]:
    """
    Args:
        business_criticality (Union[Unset, None, str]):
        created (Union[Unset, None, ProductsListCreated]):
        description (Union[Unset, None, str]):
        external_audience (Union[Unset, None, bool]):
        id (Union[Unset, None, List[int]]):
        internet_accessible (Union[Unset, None, bool]):
        lifecycle (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        name_exact (Union[Unset, None, str]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[ProductsListOItem]]):
        offset (Union[Unset, None, int]):
        origin (Union[Unset, None, str]):
        platform (Union[Unset, None, str]):
        prefetch (Union[Unset, None, List[ProductsListPrefetchItem]]):
        prod_numeric_grade (Union[Unset, None, List[int]]):
        prod_type (Union[Unset, None, List[int]]):
        product_manager (Union[Unset, None, List[int]]):
        regulations (Union[Unset, None, List[int]]):
        revenue (Union[Unset, None, float]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        team_manager (Union[Unset, None, List[int]]):
        technical_contact (Union[Unset, None, List[int]]):
        tid (Union[Unset, None, List[int]]):
        updated (Union[Unset, None, ProductsListUpdated]):
        user_records (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        business_criticality=business_criticality,
        created=created,
        description=description,
        external_audience=external_audience,
        id=id,
        internet_accessible=internet_accessible,
        lifecycle=lifecycle,
        limit=limit,
        name=name,
        name_exact=name_exact,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        origin=origin,
        platform=platform,
        prefetch=prefetch,
        prod_numeric_grade=prod_numeric_grade,
        prod_type=prod_type,
        product_manager=product_manager,
        regulations=regulations,
        revenue=revenue,
        tag=tag,
        tags=tags,
        team_manager=team_manager,
        technical_contact=technical_contact,
        tid=tid,
        updated=updated,
        user_records=user_records,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    business_criticality: Union[Unset, None, str] = UNSET,
    created: Union[Unset, None, ProductsListCreated] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    external_audience: Union[Unset, None, bool] = UNSET,
    id: Union[Unset, None, List[int]] = UNSET,
    internet_accessible: Union[Unset, None, bool] = UNSET,
    lifecycle: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_exact: Union[Unset, None, str] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[ProductsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    origin: Union[Unset, None, str] = UNSET,
    platform: Union[Unset, None, str] = UNSET,
    prefetch: Union[Unset, None, List[ProductsListPrefetchItem]] = UNSET,
    prod_numeric_grade: Union[Unset, None, List[int]] = UNSET,
    prod_type: Union[Unset, None, List[int]] = UNSET,
    product_manager: Union[Unset, None, List[int]] = UNSET,
    regulations: Union[Unset, None, List[int]] = UNSET,
    revenue: Union[Unset, None, float] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    team_manager: Union[Unset, None, List[int]] = UNSET,
    technical_contact: Union[Unset, None, List[int]] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
    updated: Union[Unset, None, ProductsListUpdated] = UNSET,
    user_records: Union[Unset, None, List[int]] = UNSET,
) -> Response[Any]:
    """
    Args:
        business_criticality (Union[Unset, None, str]):
        created (Union[Unset, None, ProductsListCreated]):
        description (Union[Unset, None, str]):
        external_audience (Union[Unset, None, bool]):
        id (Union[Unset, None, List[int]]):
        internet_accessible (Union[Unset, None, bool]):
        lifecycle (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        name_exact (Union[Unset, None, str]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[ProductsListOItem]]):
        offset (Union[Unset, None, int]):
        origin (Union[Unset, None, str]):
        platform (Union[Unset, None, str]):
        prefetch (Union[Unset, None, List[ProductsListPrefetchItem]]):
        prod_numeric_grade (Union[Unset, None, List[int]]):
        prod_type (Union[Unset, None, List[int]]):
        product_manager (Union[Unset, None, List[int]]):
        regulations (Union[Unset, None, List[int]]):
        revenue (Union[Unset, None, float]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        team_manager (Union[Unset, None, List[int]]):
        technical_contact (Union[Unset, None, List[int]]):
        tid (Union[Unset, None, List[int]]):
        updated (Union[Unset, None, ProductsListUpdated]):
        user_records (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        business_criticality=business_criticality,
        created=created,
        description=description,
        external_audience=external_audience,
        id=id,
        internet_accessible=internet_accessible,
        lifecycle=lifecycle,
        limit=limit,
        name=name,
        name_exact=name_exact,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        origin=origin,
        platform=platform,
        prefetch=prefetch,
        prod_numeric_grade=prod_numeric_grade,
        prod_type=prod_type,
        product_manager=product_manager,
        regulations=regulations,
        revenue=revenue,
        tag=tag,
        tags=tags,
        team_manager=team_manager,
        technical_contact=technical_contact,
        tid=tid,
        updated=updated,
        user_records=user_records,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tests_list_o_item import TestsListOItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    actual_time: Union[Unset, None, str] = UNSET,
    api_scan_configuration: Union[Unset, None, int] = UNSET,
    branch_tag: Union[Unset, None, str] = UNSET,
    build_id: Union[Unset, None, str] = UNSET,
    commit_hash: Union[Unset, None, str] = UNSET,
    engagement: Union[Unset, None, int] = UNSET,
    engagement_product_tags: Union[Unset, None, List[str]] = UNSET,
    engagement_tags: Union[Unset, None, List[str]] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    not_engagement_product_tags: Union[Unset, None, List[str]] = UNSET,
    not_engagement_tags: Union[Unset, None, List[str]] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    notes: Union[Unset, None, List[int]] = UNSET,
    o: Union[Unset, None, List[TestsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    percent_complete: Union[Unset, None, int] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    target_end: Union[Unset, None, datetime.datetime] = UNSET,
    target_start: Union[Unset, None, datetime.datetime] = UNSET,
    test_type: Union[Unset, None, int] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["actual_time"] = actual_time

    params["api_scan_configuration"] = api_scan_configuration

    params["branch_tag"] = branch_tag

    params["build_id"] = build_id

    params["commit_hash"] = commit_hash

    params["engagement"] = engagement

    json_engagement_product_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(engagement_product_tags, Unset):
        if engagement_product_tags is None:
            json_engagement_product_tags = None
        else:
            json_engagement_product_tags = engagement_product_tags

    params["engagement__product__tags"] = json_engagement_product_tags

    json_engagement_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(engagement_tags, Unset):
        if engagement_tags is None:
            json_engagement_tags = None
        else:
            json_engagement_tags = engagement_tags

    params["engagement__tags"] = json_engagement_tags

    params["id"] = id

    params["limit"] = limit

    json_not_engagement_product_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(not_engagement_product_tags, Unset):
        if not_engagement_product_tags is None:
            json_not_engagement_product_tags = None
        else:
            json_not_engagement_product_tags = not_engagement_product_tags

    params["not_engagement__product__tags"] = json_not_engagement_product_tags

    json_not_engagement_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(not_engagement_tags, Unset):
        if not_engagement_tags is None:
            json_not_engagement_tags = None
        else:
            json_not_engagement_tags = not_engagement_tags

    params["not_engagement__tags"] = json_not_engagement_tags

    params["not_tag"] = not_tag

    json_not_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(not_tags, Unset):
        if not_tags is None:
            json_not_tags = None
        else:
            json_not_tags = not_tags

    params["not_tags"] = json_not_tags

    json_notes: Union[Unset, None, List[int]] = UNSET
    if not isinstance(notes, Unset):
        if notes is None:
            json_notes = None
        else:
            json_notes = notes

    params["notes"] = json_notes

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

    params["percent_complete"] = percent_complete

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

    params["test_type"] = test_type

    params["title"] = title

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/tests/",
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
    actual_time: Union[Unset, None, str] = UNSET,
    api_scan_configuration: Union[Unset, None, int] = UNSET,
    branch_tag: Union[Unset, None, str] = UNSET,
    build_id: Union[Unset, None, str] = UNSET,
    commit_hash: Union[Unset, None, str] = UNSET,
    engagement: Union[Unset, None, int] = UNSET,
    engagement_product_tags: Union[Unset, None, List[str]] = UNSET,
    engagement_tags: Union[Unset, None, List[str]] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    not_engagement_product_tags: Union[Unset, None, List[str]] = UNSET,
    not_engagement_tags: Union[Unset, None, List[str]] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    notes: Union[Unset, None, List[int]] = UNSET,
    o: Union[Unset, None, List[TestsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    percent_complete: Union[Unset, None, int] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    target_end: Union[Unset, None, datetime.datetime] = UNSET,
    target_start: Union[Unset, None, datetime.datetime] = UNSET,
    test_type: Union[Unset, None, int] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        actual_time (Union[Unset, None, str]):
        api_scan_configuration (Union[Unset, None, int]):
        branch_tag (Union[Unset, None, str]):
        build_id (Union[Unset, None, str]):
        commit_hash (Union[Unset, None, str]):
        engagement (Union[Unset, None, int]):
        engagement_product_tags (Union[Unset, None, List[str]]):
        engagement_tags (Union[Unset, None, List[str]]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        not_engagement_product_tags (Union[Unset, None, List[str]]):
        not_engagement_tags (Union[Unset, None, List[str]]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        notes (Union[Unset, None, List[int]]):
        o (Union[Unset, None, List[TestsListOItem]]):
        offset (Union[Unset, None, int]):
        percent_complete (Union[Unset, None, int]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        target_end (Union[Unset, None, datetime.datetime]):
        target_start (Union[Unset, None, datetime.datetime]):
        test_type (Union[Unset, None, int]):
        title (Union[Unset, None, str]):
        version (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        actual_time=actual_time,
        api_scan_configuration=api_scan_configuration,
        branch_tag=branch_tag,
        build_id=build_id,
        commit_hash=commit_hash,
        engagement=engagement,
        engagement_product_tags=engagement_product_tags,
        engagement_tags=engagement_tags,
        id=id,
        limit=limit,
        not_engagement_product_tags=not_engagement_product_tags,
        not_engagement_tags=not_engagement_tags,
        not_tag=not_tag,
        not_tags=not_tags,
        notes=notes,
        o=o,
        offset=offset,
        percent_complete=percent_complete,
        tag=tag,
        tags=tags,
        target_end=target_end,
        target_start=target_start,
        test_type=test_type,
        title=title,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    actual_time: Union[Unset, None, str] = UNSET,
    api_scan_configuration: Union[Unset, None, int] = UNSET,
    branch_tag: Union[Unset, None, str] = UNSET,
    build_id: Union[Unset, None, str] = UNSET,
    commit_hash: Union[Unset, None, str] = UNSET,
    engagement: Union[Unset, None, int] = UNSET,
    engagement_product_tags: Union[Unset, None, List[str]] = UNSET,
    engagement_tags: Union[Unset, None, List[str]] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    not_engagement_product_tags: Union[Unset, None, List[str]] = UNSET,
    not_engagement_tags: Union[Unset, None, List[str]] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    notes: Union[Unset, None, List[int]] = UNSET,
    o: Union[Unset, None, List[TestsListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    percent_complete: Union[Unset, None, int] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    target_end: Union[Unset, None, datetime.datetime] = UNSET,
    target_start: Union[Unset, None, datetime.datetime] = UNSET,
    test_type: Union[Unset, None, int] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        actual_time (Union[Unset, None, str]):
        api_scan_configuration (Union[Unset, None, int]):
        branch_tag (Union[Unset, None, str]):
        build_id (Union[Unset, None, str]):
        commit_hash (Union[Unset, None, str]):
        engagement (Union[Unset, None, int]):
        engagement_product_tags (Union[Unset, None, List[str]]):
        engagement_tags (Union[Unset, None, List[str]]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        not_engagement_product_tags (Union[Unset, None, List[str]]):
        not_engagement_tags (Union[Unset, None, List[str]]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        notes (Union[Unset, None, List[int]]):
        o (Union[Unset, None, List[TestsListOItem]]):
        offset (Union[Unset, None, int]):
        percent_complete (Union[Unset, None, int]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        target_end (Union[Unset, None, datetime.datetime]):
        target_start (Union[Unset, None, datetime.datetime]):
        test_type (Union[Unset, None, int]):
        title (Union[Unset, None, str]):
        version (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        actual_time=actual_time,
        api_scan_configuration=api_scan_configuration,
        branch_tag=branch_tag,
        build_id=build_id,
        commit_hash=commit_hash,
        engagement=engagement,
        engagement_product_tags=engagement_product_tags,
        engagement_tags=engagement_tags,
        id=id,
        limit=limit,
        not_engagement_product_tags=not_engagement_product_tags,
        not_engagement_tags=not_engagement_tags,
        not_tag=not_tag,
        not_tags=not_tags,
        notes=notes,
        o=o,
        offset=offset,
        percent_complete=percent_complete,
        tag=tag,
        tags=tags,
        target_end=target_end,
        target_start=target_start,
        test_type=test_type,
        title=title,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

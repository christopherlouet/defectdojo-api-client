from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finding_templates_list_o_item import FindingTemplatesListOItem
from ...models.paginated_finding_template_list import PaginatedFindingTemplateList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cwe: Union[Unset, None, int] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    mitigation: Union[Unset, None, str] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[FindingTemplatesListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    severity: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["cwe"] = cwe

    params["description"] = description

    params["id"] = id

    params["limit"] = limit

    params["mitigation"] = mitigation

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

    params["severity"] = severity

    params["tag"] = tag

    json_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(tags, Unset):
        if tags is None:
            json_tags = None
        else:
            json_tags = tags

    params["tags"] = json_tags

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/finding_templates/",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedFindingTemplateList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedFindingTemplateList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedFindingTemplateList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cwe: Union[Unset, None, int] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    mitigation: Union[Unset, None, str] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[FindingTemplatesListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    severity: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedFindingTemplateList]:
    """
    Args:
        cwe (Union[Unset, None, int]):
        description (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        mitigation (Union[Unset, None, str]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[FindingTemplatesListOItem]]):
        offset (Union[Unset, None, int]):
        severity (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedFindingTemplateList]
    """

    kwargs = _get_kwargs(
        cwe=cwe,
        description=description,
        id=id,
        limit=limit,
        mitigation=mitigation,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        severity=severity,
        tag=tag,
        tags=tags,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cwe: Union[Unset, None, int] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    mitigation: Union[Unset, None, str] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[FindingTemplatesListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    severity: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedFindingTemplateList]:
    """
    Args:
        cwe (Union[Unset, None, int]):
        description (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        mitigation (Union[Unset, None, str]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[FindingTemplatesListOItem]]):
        offset (Union[Unset, None, int]):
        severity (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedFindingTemplateList
    """

    return sync_detailed(
        client=client,
        cwe=cwe,
        description=description,
        id=id,
        limit=limit,
        mitigation=mitigation,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        severity=severity,
        tag=tag,
        tags=tags,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cwe: Union[Unset, None, int] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    mitigation: Union[Unset, None, str] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[FindingTemplatesListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    severity: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedFindingTemplateList]:
    """
    Args:
        cwe (Union[Unset, None, int]):
        description (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        mitigation (Union[Unset, None, str]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[FindingTemplatesListOItem]]):
        offset (Union[Unset, None, int]):
        severity (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedFindingTemplateList]
    """

    kwargs = _get_kwargs(
        cwe=cwe,
        description=description,
        id=id,
        limit=limit,
        mitigation=mitigation,
        not_tag=not_tag,
        not_tags=not_tags,
        o=o,
        offset=offset,
        severity=severity,
        tag=tag,
        tags=tags,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cwe: Union[Unset, None, int] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    mitigation: Union[Unset, None, str] = UNSET,
    not_tag: Union[Unset, None, str] = UNSET,
    not_tags: Union[Unset, None, List[str]] = UNSET,
    o: Union[Unset, None, List[FindingTemplatesListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    severity: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedFindingTemplateList]:
    """
    Args:
        cwe (Union[Unset, None, int]):
        description (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        mitigation (Union[Unset, None, str]):
        not_tag (Union[Unset, None, str]):
        not_tags (Union[Unset, None, List[str]]):
        o (Union[Unset, None, List[FindingTemplatesListOItem]]):
        offset (Union[Unset, None, int]):
        severity (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        tags (Union[Unset, None, List[str]]):
        title (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedFindingTemplateList
    """

    return (
        await asyncio_detailed(
            client=client,
            cwe=cwe,
            description=description,
            id=id,
            limit=limit,
            mitigation=mitigation,
            not_tag=not_tag,
            not_tags=not_tags,
            o=o,
            offset=offset,
            severity=severity,
            tag=tag,
            tags=tags,
            title=title,
        )
    ).parsed

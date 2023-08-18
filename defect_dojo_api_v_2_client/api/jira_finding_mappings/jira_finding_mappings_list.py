from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_jira_issue_list import PaginatedJIRAIssueList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    engagement: Union[Unset, None, int] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    finding_group: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    jira_id: Union[Unset, None, str] = UNSET,
    jira_key: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["engagement"] = engagement

    params["finding"] = finding

    params["finding_group"] = finding_group

    params["id"] = id

    params["jira_id"] = jira_id

    params["jira_key"] = jira_key

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/jira_finding_mappings/",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedJIRAIssueList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedJIRAIssueList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedJIRAIssueList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    engagement: Union[Unset, None, int] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    finding_group: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    jira_id: Union[Unset, None, str] = UNSET,
    jira_key: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedJIRAIssueList]:
    """
    Args:
        engagement (Union[Unset, None, int]):
        finding (Union[Unset, None, int]):
        finding_group (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        jira_id (Union[Unset, None, str]):
        jira_key (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJIRAIssueList]
    """

    kwargs = _get_kwargs(
        engagement=engagement,
        finding=finding,
        finding_group=finding_group,
        id=id,
        jira_id=jira_id,
        jira_key=jira_key,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    engagement: Union[Unset, None, int] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    finding_group: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    jira_id: Union[Unset, None, str] = UNSET,
    jira_key: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedJIRAIssueList]:
    """
    Args:
        engagement (Union[Unset, None, int]):
        finding (Union[Unset, None, int]):
        finding_group (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        jira_id (Union[Unset, None, str]):
        jira_key (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJIRAIssueList
    """

    return sync_detailed(
        client=client,
        engagement=engagement,
        finding=finding,
        finding_group=finding_group,
        id=id,
        jira_id=jira_id,
        jira_key=jira_key,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    engagement: Union[Unset, None, int] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    finding_group: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    jira_id: Union[Unset, None, str] = UNSET,
    jira_key: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedJIRAIssueList]:
    """
    Args:
        engagement (Union[Unset, None, int]):
        finding (Union[Unset, None, int]):
        finding_group (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        jira_id (Union[Unset, None, str]):
        jira_key (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJIRAIssueList]
    """

    kwargs = _get_kwargs(
        engagement=engagement,
        finding=finding,
        finding_group=finding_group,
        id=id,
        jira_id=jira_id,
        jira_key=jira_key,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    engagement: Union[Unset, None, int] = UNSET,
    finding: Union[Unset, None, int] = UNSET,
    finding_group: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    jira_id: Union[Unset, None, str] = UNSET,
    jira_key: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedJIRAIssueList]:
    """
    Args:
        engagement (Union[Unset, None, int]):
        finding (Union[Unset, None, int]):
        finding_group (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        jira_id (Union[Unset, None, str]):
        jira_key (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJIRAIssueList
    """

    return (
        await asyncio_detailed(
            client=client,
            engagement=engagement,
            finding=finding,
            finding_group=finding_group,
            id=id,
            jira_id=jira_id,
            jira_key=jira_key,
            limit=limit,
            offset=offset,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_jira_project_list import PaginatedJIRAProjectList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    component: Union[Unset, None, str] = UNSET,
    enable_engagement_epic_mapping: Union[Unset, None, bool] = UNSET,
    engagement: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    jira_instance: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    project_key: Union[Unset, None, str] = UNSET,
    push_all_issues: Union[Unset, None, bool] = UNSET,
    push_notes: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["component"] = component

    params["enable_engagement_epic_mapping"] = enable_engagement_epic_mapping

    params["engagement"] = engagement

    params["id"] = id

    params["jira_instance"] = jira_instance

    params["limit"] = limit

    params["offset"] = offset

    params["product"] = product

    params["project_key"] = project_key

    params["push_all_issues"] = push_all_issues

    params["push_notes"] = push_notes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/jira_projects/",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedJIRAProjectList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedJIRAProjectList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedJIRAProjectList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    component: Union[Unset, None, str] = UNSET,
    enable_engagement_epic_mapping: Union[Unset, None, bool] = UNSET,
    engagement: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    jira_instance: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    project_key: Union[Unset, None, str] = UNSET,
    push_all_issues: Union[Unset, None, bool] = UNSET,
    push_notes: Union[Unset, None, bool] = UNSET,
) -> Response[PaginatedJIRAProjectList]:
    """
    Args:
        component (Union[Unset, None, str]):
        enable_engagement_epic_mapping (Union[Unset, None, bool]):
        engagement (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        jira_instance (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        project_key (Union[Unset, None, str]):
        push_all_issues (Union[Unset, None, bool]):
        push_notes (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJIRAProjectList]
    """

    kwargs = _get_kwargs(
        component=component,
        enable_engagement_epic_mapping=enable_engagement_epic_mapping,
        engagement=engagement,
        id=id,
        jira_instance=jira_instance,
        limit=limit,
        offset=offset,
        product=product,
        project_key=project_key,
        push_all_issues=push_all_issues,
        push_notes=push_notes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    component: Union[Unset, None, str] = UNSET,
    enable_engagement_epic_mapping: Union[Unset, None, bool] = UNSET,
    engagement: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    jira_instance: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    project_key: Union[Unset, None, str] = UNSET,
    push_all_issues: Union[Unset, None, bool] = UNSET,
    push_notes: Union[Unset, None, bool] = UNSET,
) -> Optional[PaginatedJIRAProjectList]:
    """
    Args:
        component (Union[Unset, None, str]):
        enable_engagement_epic_mapping (Union[Unset, None, bool]):
        engagement (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        jira_instance (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        project_key (Union[Unset, None, str]):
        push_all_issues (Union[Unset, None, bool]):
        push_notes (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJIRAProjectList
    """

    return sync_detailed(
        client=client,
        component=component,
        enable_engagement_epic_mapping=enable_engagement_epic_mapping,
        engagement=engagement,
        id=id,
        jira_instance=jira_instance,
        limit=limit,
        offset=offset,
        product=product,
        project_key=project_key,
        push_all_issues=push_all_issues,
        push_notes=push_notes,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    component: Union[Unset, None, str] = UNSET,
    enable_engagement_epic_mapping: Union[Unset, None, bool] = UNSET,
    engagement: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    jira_instance: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    project_key: Union[Unset, None, str] = UNSET,
    push_all_issues: Union[Unset, None, bool] = UNSET,
    push_notes: Union[Unset, None, bool] = UNSET,
) -> Response[PaginatedJIRAProjectList]:
    """
    Args:
        component (Union[Unset, None, str]):
        enable_engagement_epic_mapping (Union[Unset, None, bool]):
        engagement (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        jira_instance (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        project_key (Union[Unset, None, str]):
        push_all_issues (Union[Unset, None, bool]):
        push_notes (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJIRAProjectList]
    """

    kwargs = _get_kwargs(
        component=component,
        enable_engagement_epic_mapping=enable_engagement_epic_mapping,
        engagement=engagement,
        id=id,
        jira_instance=jira_instance,
        limit=limit,
        offset=offset,
        product=product,
        project_key=project_key,
        push_all_issues=push_all_issues,
        push_notes=push_notes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    component: Union[Unset, None, str] = UNSET,
    enable_engagement_epic_mapping: Union[Unset, None, bool] = UNSET,
    engagement: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    jira_instance: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product: Union[Unset, None, int] = UNSET,
    project_key: Union[Unset, None, str] = UNSET,
    push_all_issues: Union[Unset, None, bool] = UNSET,
    push_notes: Union[Unset, None, bool] = UNSET,
) -> Optional[PaginatedJIRAProjectList]:
    """
    Args:
        component (Union[Unset, None, str]):
        enable_engagement_epic_mapping (Union[Unset, None, bool]):
        engagement (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        jira_instance (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        product (Union[Unset, None, int]):
        project_key (Union[Unset, None, str]):
        push_all_issues (Union[Unset, None, bool]):
        push_notes (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJIRAProjectList
    """

    return (
        await asyncio_detailed(
            client=client,
            component=component,
            enable_engagement_epic_mapping=enable_engagement_epic_mapping,
            engagement=engagement,
            id=id,
            jira_instance=jira_instance,
            limit=limit,
            offset=offset,
            product=product,
            project_key=project_key,
            push_all_issues=push_all_issues,
            push_notes=push_notes,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_contact_infos_list_prefetch_item import UserContactInfosListPrefetchItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    block_execution: Union[Unset, None, bool] = UNSET,
    cell_number: Union[Unset, None, str] = UNSET,
    force_password_reset: Union[Unset, None, bool] = UNSET,
    github_username: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    phone_number: Union[Unset, None, str] = UNSET,
    prefetch: Union[Unset, None, List[UserContactInfosListPrefetchItem]] = UNSET,
    slack_user_id: Union[Unset, None, str] = UNSET,
    slack_username: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    twitter_username: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["block_execution"] = block_execution

    params["cell_number"] = cell_number

    params["force_password_reset"] = force_password_reset

    params["github_username"] = github_username

    params["limit"] = limit

    params["offset"] = offset

    params["phone_number"] = phone_number

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

    params["slack_user_id"] = slack_user_id

    params["slack_username"] = slack_username

    params["title"] = title

    params["twitter_username"] = twitter_username

    params["user"] = user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/user_contact_infos/",
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
    block_execution: Union[Unset, None, bool] = UNSET,
    cell_number: Union[Unset, None, str] = UNSET,
    force_password_reset: Union[Unset, None, bool] = UNSET,
    github_username: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    phone_number: Union[Unset, None, str] = UNSET,
    prefetch: Union[Unset, None, List[UserContactInfosListPrefetchItem]] = UNSET,
    slack_user_id: Union[Unset, None, str] = UNSET,
    slack_username: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    twitter_username: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        block_execution (Union[Unset, None, bool]):
        cell_number (Union[Unset, None, str]):
        force_password_reset (Union[Unset, None, bool]):
        github_username (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        phone_number (Union[Unset, None, str]):
        prefetch (Union[Unset, None, List[UserContactInfosListPrefetchItem]]):
        slack_user_id (Union[Unset, None, str]):
        slack_username (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        twitter_username (Union[Unset, None, str]):
        user (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        block_execution=block_execution,
        cell_number=cell_number,
        force_password_reset=force_password_reset,
        github_username=github_username,
        limit=limit,
        offset=offset,
        phone_number=phone_number,
        prefetch=prefetch,
        slack_user_id=slack_user_id,
        slack_username=slack_username,
        title=title,
        twitter_username=twitter_username,
        user=user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    block_execution: Union[Unset, None, bool] = UNSET,
    cell_number: Union[Unset, None, str] = UNSET,
    force_password_reset: Union[Unset, None, bool] = UNSET,
    github_username: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    phone_number: Union[Unset, None, str] = UNSET,
    prefetch: Union[Unset, None, List[UserContactInfosListPrefetchItem]] = UNSET,
    slack_user_id: Union[Unset, None, str] = UNSET,
    slack_username: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    twitter_username: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        block_execution (Union[Unset, None, bool]):
        cell_number (Union[Unset, None, str]):
        force_password_reset (Union[Unset, None, bool]):
        github_username (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        phone_number (Union[Unset, None, str]):
        prefetch (Union[Unset, None, List[UserContactInfosListPrefetchItem]]):
        slack_user_id (Union[Unset, None, str]):
        slack_username (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        twitter_username (Union[Unset, None, str]):
        user (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        block_execution=block_execution,
        cell_number=cell_number,
        force_password_reset=force_password_reset,
        github_username=github_username,
        limit=limit,
        offset=offset,
        phone_number=phone_number,
        prefetch=prefetch,
        slack_user_id=slack_user_id,
        slack_username=slack_username,
        title=title,
        twitter_username=twitter_username,
        user=user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

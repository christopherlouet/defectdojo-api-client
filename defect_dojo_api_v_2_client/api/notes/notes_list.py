import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    author: Union[Unset, None, int] = UNSET,
    date: Union[Unset, None, datetime.datetime] = UNSET,
    edit_time: Union[Unset, None, datetime.datetime] = UNSET,
    edited: Union[Unset, None, bool] = UNSET,
    editor: Union[Unset, None, int] = UNSET,
    entry: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    private: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["author"] = author

    json_date: Union[Unset, None, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat() if date else None

    params["date"] = json_date

    json_edit_time: Union[Unset, None, str] = UNSET
    if not isinstance(edit_time, Unset):
        json_edit_time = edit_time.isoformat() if edit_time else None

    params["edit_time"] = json_edit_time

    params["edited"] = edited

    params["editor"] = editor

    params["entry"] = entry

    params["id"] = id

    params["limit"] = limit

    params["offset"] = offset

    params["private"] = private

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/notes/",
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
    author: Union[Unset, None, int] = UNSET,
    date: Union[Unset, None, datetime.datetime] = UNSET,
    edit_time: Union[Unset, None, datetime.datetime] = UNSET,
    edited: Union[Unset, None, bool] = UNSET,
    editor: Union[Unset, None, int] = UNSET,
    entry: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    private: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        author (Union[Unset, None, int]):
        date (Union[Unset, None, datetime.datetime]):
        edit_time (Union[Unset, None, datetime.datetime]):
        edited (Union[Unset, None, bool]):
        editor (Union[Unset, None, int]):
        entry (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        private (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        author=author,
        date=date,
        edit_time=edit_time,
        edited=edited,
        editor=editor,
        entry=entry,
        id=id,
        limit=limit,
        offset=offset,
        private=private,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    author: Union[Unset, None, int] = UNSET,
    date: Union[Unset, None, datetime.datetime] = UNSET,
    edit_time: Union[Unset, None, datetime.datetime] = UNSET,
    edited: Union[Unset, None, bool] = UNSET,
    editor: Union[Unset, None, int] = UNSET,
    entry: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    private: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        author (Union[Unset, None, int]):
        date (Union[Unset, None, datetime.datetime]):
        edit_time (Union[Unset, None, datetime.datetime]):
        edited (Union[Unset, None, bool]):
        editor (Union[Unset, None, int]):
        entry (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        private (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        author=author,
        date=date,
        edit_time=edit_time,
        edited=edited,
        editor=editor,
        entry=entry,
        id=id,
        limit=limit,
        offset=offset,
        private=private,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

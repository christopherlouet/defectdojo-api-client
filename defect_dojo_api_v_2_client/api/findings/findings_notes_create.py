from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_new_note_option_request import AddNewNoteOptionRequest
from ...models.note import Note
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    form_data: AddNewNoteOptionRequest,
    multipart_data: AddNewNoteOptionRequest,
    json_body: AddNewNoteOptionRequest,
) -> Dict[str, Any]:
    pass

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/api/v2/findings/{id}/notes/".format(
            id=id,
        ),
        "data": form_data.to_dict(),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Note]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Note.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Note]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: AddNewNoteOptionRequest,
    multipart_data: AddNewNoteOptionRequest,
    json_body: AddNewNoteOptionRequest,
) -> Response[Note]:
    """
    Args:
        id (int):
        multipart_data (AddNewNoteOptionRequest):
        json_body (AddNewNoteOptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Note]
    """

    kwargs = _get_kwargs(
        id=id,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: AddNewNoteOptionRequest,
    multipart_data: AddNewNoteOptionRequest,
    json_body: AddNewNoteOptionRequest,
) -> Optional[Note]:
    """
    Args:
        id (int):
        multipart_data (AddNewNoteOptionRequest):
        json_body (AddNewNoteOptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Note
    """

    return sync_detailed(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: AddNewNoteOptionRequest,
    multipart_data: AddNewNoteOptionRequest,
    json_body: AddNewNoteOptionRequest,
) -> Response[Note]:
    """
    Args:
        id (int):
        multipart_data (AddNewNoteOptionRequest):
        json_body (AddNewNoteOptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Note]
    """

    kwargs = _get_kwargs(
        id=id,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: AddNewNoteOptionRequest,
    multipart_data: AddNewNoteOptionRequest,
    json_body: AddNewNoteOptionRequest,
) -> Optional[Note]:
    """
    Args:
        id (int):
        multipart_data (AddNewNoteOptionRequest):
        json_body (AddNewNoteOptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Note
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed

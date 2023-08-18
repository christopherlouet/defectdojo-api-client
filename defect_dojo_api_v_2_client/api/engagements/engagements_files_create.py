from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_new_file_option_request import AddNewFileOptionRequest
from ...models.file import File
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    multipart_data: AddNewFileOptionRequest,
) -> Dict[str, Any]:
    pass

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/api/v2/engagements/{id}/files/".format(
            id=id,
        ),
        "files": multipart_multipart_data,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[File]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = File.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[File]:
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
    multipart_data: AddNewFileOptionRequest,
) -> Response[File]:
    """
    Args:
        id (int):
        multipart_data (AddNewFileOptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        id=id,
        multipart_data=multipart_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    multipart_data: AddNewFileOptionRequest,
) -> Optional[File]:
    """
    Args:
        id (int):
        multipart_data (AddNewFileOptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        id=id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    multipart_data: AddNewFileOptionRequest,
) -> Response[File]:
    """
    Args:
        id (int):
        multipart_data (AddNewFileOptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        id=id,
        multipart_data=multipart_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    multipart_data: AddNewFileOptionRequest,
) -> Optional[File]:
    """
    Args:
        id (int):
        multipart_data (AddNewFileOptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed

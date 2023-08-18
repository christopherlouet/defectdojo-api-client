from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.language_type import LanguageType
from ...models.language_type_request import LanguageTypeRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    form_data: LanguageTypeRequest,
    multipart_data: LanguageTypeRequest,
    json_body: LanguageTypeRequest,
) -> Dict[str, Any]:
    pass

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "put",
        "url": "/api/v2/language_types/{id}/".format(
            id=id,
        ),
        "data": form_data.to_dict(),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[LanguageType]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LanguageType.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[LanguageType]:
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
    form_data: LanguageTypeRequest,
    multipart_data: LanguageTypeRequest,
    json_body: LanguageTypeRequest,
) -> Response[LanguageType]:
    """
    Args:
        id (int):
        multipart_data (LanguageTypeRequest):
        json_body (LanguageTypeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LanguageType]
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
    form_data: LanguageTypeRequest,
    multipart_data: LanguageTypeRequest,
    json_body: LanguageTypeRequest,
) -> Optional[LanguageType]:
    """
    Args:
        id (int):
        multipart_data (LanguageTypeRequest):
        json_body (LanguageTypeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LanguageType
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
    form_data: LanguageTypeRequest,
    multipart_data: LanguageTypeRequest,
    json_body: LanguageTypeRequest,
) -> Response[LanguageType]:
    """
    Args:
        id (int):
        multipart_data (LanguageTypeRequest):
        json_body (LanguageTypeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LanguageType]
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
    form_data: LanguageTypeRequest,
    multipart_data: LanguageTypeRequest,
    json_body: LanguageTypeRequest,
) -> Optional[LanguageType]:
    """
    Args:
        id (int):
        multipart_data (LanguageTypeRequest):
        json_body (LanguageTypeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LanguageType
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

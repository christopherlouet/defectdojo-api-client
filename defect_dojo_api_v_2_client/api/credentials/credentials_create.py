from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credential import Credential
from ...models.credential_request import CredentialRequest
from ...types import Response


def _get_kwargs(
    *,
    form_data: CredentialRequest,
    multipart_data: CredentialRequest,
    json_body: CredentialRequest,
) -> Dict[str, Any]:
    pass

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/api/v2/credentials/",
        "data": form_data.to_dict(),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Credential]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Credential.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Credential]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: CredentialRequest,
    multipart_data: CredentialRequest,
    json_body: CredentialRequest,
) -> Response[Credential]:
    """
    Args:
        multipart_data (CredentialRequest):
        json_body (CredentialRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Credential]
    """

    kwargs = _get_kwargs(
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    form_data: CredentialRequest,
    multipart_data: CredentialRequest,
    json_body: CredentialRequest,
) -> Optional[Credential]:
    """
    Args:
        multipart_data (CredentialRequest):
        json_body (CredentialRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Credential
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: CredentialRequest,
    multipart_data: CredentialRequest,
    json_body: CredentialRequest,
) -> Response[Credential]:
    """
    Args:
        multipart_data (CredentialRequest):
        json_body (CredentialRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Credential]
    """

    kwargs = _get_kwargs(
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    form_data: CredentialRequest,
    multipart_data: CredentialRequest,
    json_body: CredentialRequest,
) -> Optional[Credential]:
    """
    Args:
        multipart_data (CredentialRequest):
        json_body (CredentialRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Credential
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_contact_info import UserContactInfo
from ...models.user_contact_info_request import UserContactInfoRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    form_data: UserContactInfoRequest,
    multipart_data: UserContactInfoRequest,
    json_body: UserContactInfoRequest,
) -> Dict[str, Any]:
    pass

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "put",
        "url": "/api/v2/user_contact_infos/{id}/".format(
            id=id,
        ),
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UserContactInfo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserContactInfo.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UserContactInfo]:
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
    form_data: UserContactInfoRequest,
    multipart_data: UserContactInfoRequest,
    json_body: UserContactInfoRequest,
) -> Response[UserContactInfo]:
    """
    Args:
        id (int):
        multipart_data (UserContactInfoRequest):
        json_body (UserContactInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserContactInfo]
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
    form_data: UserContactInfoRequest,
    multipart_data: UserContactInfoRequest,
    json_body: UserContactInfoRequest,
) -> Optional[UserContactInfo]:
    """
    Args:
        id (int):
        multipart_data (UserContactInfoRequest):
        json_body (UserContactInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserContactInfo
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
    form_data: UserContactInfoRequest,
    multipart_data: UserContactInfoRequest,
    json_body: UserContactInfoRequest,
) -> Response[UserContactInfo]:
    """
    Args:
        id (int):
        multipart_data (UserContactInfoRequest):
        json_body (UserContactInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserContactInfo]
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
    form_data: UserContactInfoRequest,
    multipart_data: UserContactInfoRequest,
    json_body: UserContactInfoRequest,
) -> Optional[UserContactInfo]:
    """
    Args:
        id (int):
        multipart_data (UserContactInfoRequest):
        json_body (UserContactInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserContactInfo
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

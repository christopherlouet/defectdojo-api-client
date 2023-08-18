from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.jira_instance import JIRAInstance
from ...models.jira_instance_request import JIRAInstanceRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    form_data: JIRAInstanceRequest,
    multipart_data: JIRAInstanceRequest,
    json_body: JIRAInstanceRequest,
) -> Dict[str, Any]:
    pass

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "put",
        "url": "/api/v2/jira_configurations/{id}/".format(
            id=id,
        ),
        "data": form_data.to_dict(),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[JIRAInstance]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JIRAInstance.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[JIRAInstance]:
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
    form_data: JIRAInstanceRequest,
    multipart_data: JIRAInstanceRequest,
    json_body: JIRAInstanceRequest,
) -> Response[JIRAInstance]:
    """
    Args:
        id (int):
        multipart_data (JIRAInstanceRequest):
        json_body (JIRAInstanceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JIRAInstance]
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
    form_data: JIRAInstanceRequest,
    multipart_data: JIRAInstanceRequest,
    json_body: JIRAInstanceRequest,
) -> Optional[JIRAInstance]:
    """
    Args:
        id (int):
        multipart_data (JIRAInstanceRequest):
        json_body (JIRAInstanceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JIRAInstance
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
    form_data: JIRAInstanceRequest,
    multipart_data: JIRAInstanceRequest,
    json_body: JIRAInstanceRequest,
) -> Response[JIRAInstance]:
    """
    Args:
        id (int):
        multipart_data (JIRAInstanceRequest):
        json_body (JIRAInstanceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JIRAInstance]
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
    form_data: JIRAInstanceRequest,
    multipart_data: JIRAInstanceRequest,
    json_body: JIRAInstanceRequest,
) -> Optional[JIRAInstance]:
    """
    Args:
        id (int):
        multipart_data (JIRAInstanceRequest):
        json_body (JIRAInstanceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JIRAInstance
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

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.finding_template import FindingTemplate
from ...models.finding_template_request import FindingTemplateRequest
from ...types import Response


def _get_kwargs(
    *,
    form_data: FindingTemplateRequest,
    multipart_data: FindingTemplateRequest,
    json_body: FindingTemplateRequest,
) -> Dict[str, Any]:
    pass

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/api/v2/finding_templates/",
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FindingTemplate]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = FindingTemplate.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FindingTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: FindingTemplateRequest,
    multipart_data: FindingTemplateRequest,
    json_body: FindingTemplateRequest,
) -> Response[FindingTemplate]:
    """
    Args:
        multipart_data (FindingTemplateRequest):
        json_body (FindingTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FindingTemplate]
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
    form_data: FindingTemplateRequest,
    multipart_data: FindingTemplateRequest,
    json_body: FindingTemplateRequest,
) -> Optional[FindingTemplate]:
    """
    Args:
        multipart_data (FindingTemplateRequest):
        json_body (FindingTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FindingTemplate
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
    form_data: FindingTemplateRequest,
    multipart_data: FindingTemplateRequest,
    json_body: FindingTemplateRequest,
) -> Response[FindingTemplate]:
    """
    Args:
        multipart_data (FindingTemplateRequest):
        json_body (FindingTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FindingTemplate]
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
    form_data: FindingTemplateRequest,
    multipart_data: FindingTemplateRequest,
    json_body: FindingTemplateRequest,
) -> Optional[FindingTemplate]:
    """
    Args:
        multipart_data (FindingTemplateRequest):
        json_body (FindingTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FindingTemplate
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed

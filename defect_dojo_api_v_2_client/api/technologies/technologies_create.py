from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_analysis import AppAnalysis
from ...models.app_analysis_request import AppAnalysisRequest
from ...types import Response


def _get_kwargs(
    *,
    form_data: AppAnalysisRequest,
    multipart_data: AppAnalysisRequest,
    json_body: AppAnalysisRequest,
) -> Dict[str, Any]:
    pass

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/api/v2/technologies/",
        "data": form_data.to_dict(),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[AppAnalysis]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = AppAnalysis.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[AppAnalysis]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: AppAnalysisRequest,
    multipart_data: AppAnalysisRequest,
    json_body: AppAnalysisRequest,
) -> Response[AppAnalysis]:
    """
    Args:
        multipart_data (AppAnalysisRequest):
        json_body (AppAnalysisRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAnalysis]
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
    form_data: AppAnalysisRequest,
    multipart_data: AppAnalysisRequest,
    json_body: AppAnalysisRequest,
) -> Optional[AppAnalysis]:
    """
    Args:
        multipart_data (AppAnalysisRequest):
        json_body (AppAnalysisRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAnalysis
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
    form_data: AppAnalysisRequest,
    multipart_data: AppAnalysisRequest,
    json_body: AppAnalysisRequest,
) -> Response[AppAnalysis]:
    """
    Args:
        multipart_data (AppAnalysisRequest):
        json_body (AppAnalysisRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAnalysis]
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
    form_data: AppAnalysisRequest,
    multipart_data: AppAnalysisRequest,
    json_body: AppAnalysisRequest,
) -> Optional[AppAnalysis]:
    """
    Args:
        multipart_data (AppAnalysisRequest):
        json_body (AppAnalysisRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAnalysis
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed

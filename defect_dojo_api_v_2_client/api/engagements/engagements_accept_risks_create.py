from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.accepted_risk_request import AcceptedRiskRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    form_data: List["AcceptedRiskRequest"],
    multipart_data: List["AcceptedRiskRequest"],
    json_body: List["AcceptedRiskRequest"],
) -> Dict[str, Any]:
    pass

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    multipart_multipart_data = []
    for multipart_data_item_data in multipart_data:
        multipart_data_item = multipart_data_item_data.to_dict()

        multipart_multipart_data.append(multipart_data_item)

    return {
        "method": "post",
        "url": "/api/v2/engagements/{id}/accept_risks/".format(
            id=id,
        ),
        "data": form_data.to_dict(),
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
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: List["AcceptedRiskRequest"],
    multipart_data: List["AcceptedRiskRequest"],
    json_body: List["AcceptedRiskRequest"],
) -> Response[Any]:
    """
    Args:
        id (int):
        multipart_data (List['AcceptedRiskRequest']):
        json_body (List['AcceptedRiskRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: List["AcceptedRiskRequest"],
    multipart_data: List["AcceptedRiskRequest"],
    json_body: List["AcceptedRiskRequest"],
) -> Response[Any]:
    """
    Args:
        id (int):
        multipart_data (List['AcceptedRiskRequest']):
        json_body (List['AcceptedRiskRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

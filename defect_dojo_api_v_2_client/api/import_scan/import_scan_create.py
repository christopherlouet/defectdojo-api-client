from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.import_scan_request import ImportScanRequest
from ...types import Response


def _get_kwargs(
    *,
    multipart_data: ImportScanRequest,
) -> Dict[str, Any]:
    pass

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/api/v2/import-scan/",
        "files": multipart_multipart_data,
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
    multipart_data: ImportScanRequest,
) -> Response[Any]:
    """Imports a scan report into an engagement or product.

    By ID:
    - Create a Product (or use an existing product)
    - Create an Engagement inside the product
    - Provide the id of the engagement in the `engagement` parameter

    In this scenario a new Test will be created inside the engagement.

    By Names:
    - Create a Product (or use an existing product)
    - Create an Engagement inside the product
    - Provide `product_name`
    - Provide `engagement_name`
    - Optionally provide `product_type_name`

    In this scenario Defect Dojo will look up the Engagement by the provided details.

    When using names you can let the importer automatically create Engagements, Products and
    Product_Types
    by using `auto_create_context=True`.

    When `auto_create_context` is set to `True` you can use `deduplication_on_engagement` to restrict
    deduplication for
    imported Findings to the newly created Engagement.

    Args:
        multipart_data (ImportScanRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: ImportScanRequest,
) -> Response[Any]:
    """Imports a scan report into an engagement or product.

    By ID:
    - Create a Product (or use an existing product)
    - Create an Engagement inside the product
    - Provide the id of the engagement in the `engagement` parameter

    In this scenario a new Test will be created inside the engagement.

    By Names:
    - Create a Product (or use an existing product)
    - Create an Engagement inside the product
    - Provide `product_name`
    - Provide `engagement_name`
    - Optionally provide `product_type_name`

    In this scenario Defect Dojo will look up the Engagement by the provided details.

    When using names you can let the importer automatically create Engagements, Products and
    Product_Types
    by using `auto_create_context=True`.

    When `auto_create_context` is set to `True` you can use `deduplication_on_engagement` to restrict
    deduplication for
    imported Findings to the newly created Engagement.

    Args:
        multipart_data (ImportScanRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

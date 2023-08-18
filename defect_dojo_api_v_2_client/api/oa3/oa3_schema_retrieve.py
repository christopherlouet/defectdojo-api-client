from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.oa_3_schema_retrieve_format import Oa3SchemaRetrieveFormat
from ...models.oa_3_schema_retrieve_lang import Oa3SchemaRetrieveLang
from ...models.oa_3_schema_retrieve_response_200 import Oa3SchemaRetrieveResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    format_: Union[Unset, None, Oa3SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, None, Oa3SchemaRetrieveLang] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    json_lang: Union[Unset, None, str] = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang.value if lang else None

    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/oa3/schema/",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Oa3SchemaRetrieveResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Oa3SchemaRetrieveResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Oa3SchemaRetrieveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, Oa3SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, None, Oa3SchemaRetrieveLang] = UNSET,
) -> Response[Oa3SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json

    Args:
        format_ (Union[Unset, None, Oa3SchemaRetrieveFormat]):
        lang (Union[Unset, None, Oa3SchemaRetrieveLang]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Oa3SchemaRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        format_=format_,
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, Oa3SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, None, Oa3SchemaRetrieveLang] = UNSET,
) -> Optional[Oa3SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json

    Args:
        format_ (Union[Unset, None, Oa3SchemaRetrieveFormat]):
        lang (Union[Unset, None, Oa3SchemaRetrieveLang]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Oa3SchemaRetrieveResponse200
    """

    return sync_detailed(
        client=client,
        format_=format_,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, Oa3SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, None, Oa3SchemaRetrieveLang] = UNSET,
) -> Response[Oa3SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json

    Args:
        format_ (Union[Unset, None, Oa3SchemaRetrieveFormat]):
        lang (Union[Unset, None, Oa3SchemaRetrieveLang]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Oa3SchemaRetrieveResponse200]
    """

    kwargs = _get_kwargs(
        format_=format_,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, Oa3SchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, None, Oa3SchemaRetrieveLang] = UNSET,
) -> Optional[Oa3SchemaRetrieveResponse200]:
    """OpenApi3 schema for this API. Format can be selected via content negotiation.

    - YAML: application/vnd.oai.openapi
    - JSON: application/vnd.oai.openapi+json

    Args:
        format_ (Union[Unset, None, Oa3SchemaRetrieveFormat]):
        lang (Union[Unset, None, Oa3SchemaRetrieveLang]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Oa3SchemaRetrieveResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
            lang=lang,
        )
    ).parsed

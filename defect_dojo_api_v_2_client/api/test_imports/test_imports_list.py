import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.test_imports_list_prefetch_item import TestImportsListPrefetchItem
from ...models.test_imports_list_test_import_finding_action_action import TestImportsListTestImportFindingActionAction
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    branch_tag: Union[Unset, None, str] = UNSET,
    build_id: Union[Unset, None, str] = UNSET,
    commit_hash: Union[Unset, None, str] = UNSET,
    findings_affected: Union[Unset, None, List[int]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    prefetch: Union[Unset, None, List[TestImportsListPrefetchItem]] = UNSET,
    test: Union[Unset, None, int] = UNSET,
    test_import_finding_action_action: Union[Unset, None, TestImportsListTestImportFindingActionAction] = UNSET,
    test_import_finding_action_created: Union[Unset, None, datetime.datetime] = UNSET,
    test_import_finding_action_finding: Union[Unset, None, int] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["branch_tag"] = branch_tag

    params["build_id"] = build_id

    params["commit_hash"] = commit_hash

    json_findings_affected: Union[Unset, None, List[int]] = UNSET
    if not isinstance(findings_affected, Unset):
        if findings_affected is None:
            json_findings_affected = None
        else:
            json_findings_affected = findings_affected

    params["findings_affected"] = json_findings_affected

    params["limit"] = limit

    params["offset"] = offset

    json_prefetch: Union[Unset, None, List[str]] = UNSET
    if not isinstance(prefetch, Unset):
        if prefetch is None:
            json_prefetch = None
        else:
            json_prefetch = []
            for prefetch_item_data in prefetch:
                prefetch_item = prefetch_item_data.value

                json_prefetch.append(prefetch_item)

    params["prefetch"] = json_prefetch

    params["test"] = test

    json_test_import_finding_action_action: Union[Unset, None, str] = UNSET
    if not isinstance(test_import_finding_action_action, Unset):
        json_test_import_finding_action_action = (
            test_import_finding_action_action.value if test_import_finding_action_action else None
        )

    params["test_import_finding_action__action"] = json_test_import_finding_action_action

    json_test_import_finding_action_created: Union[Unset, None, str] = UNSET
    if not isinstance(test_import_finding_action_created, Unset):
        json_test_import_finding_action_created = (
            test_import_finding_action_created.isoformat() if test_import_finding_action_created else None
        )

    params["test_import_finding_action__created"] = json_test_import_finding_action_created

    params["test_import_finding_action__finding"] = test_import_finding_action_finding

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/test_imports/",
        "params": params,
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
    branch_tag: Union[Unset, None, str] = UNSET,
    build_id: Union[Unset, None, str] = UNSET,
    commit_hash: Union[Unset, None, str] = UNSET,
    findings_affected: Union[Unset, None, List[int]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    prefetch: Union[Unset, None, List[TestImportsListPrefetchItem]] = UNSET,
    test: Union[Unset, None, int] = UNSET,
    test_import_finding_action_action: Union[Unset, None, TestImportsListTestImportFindingActionAction] = UNSET,
    test_import_finding_action_created: Union[Unset, None, datetime.datetime] = UNSET,
    test_import_finding_action_finding: Union[Unset, None, int] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        branch_tag (Union[Unset, None, str]):
        build_id (Union[Unset, None, str]):
        commit_hash (Union[Unset, None, str]):
        findings_affected (Union[Unset, None, List[int]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        prefetch (Union[Unset, None, List[TestImportsListPrefetchItem]]):
        test (Union[Unset, None, int]):
        test_import_finding_action_action (Union[Unset, None,
            TestImportsListTestImportFindingActionAction]):
        test_import_finding_action_created (Union[Unset, None, datetime.datetime]):
        test_import_finding_action_finding (Union[Unset, None, int]):
        version (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        branch_tag=branch_tag,
        build_id=build_id,
        commit_hash=commit_hash,
        findings_affected=findings_affected,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        test=test,
        test_import_finding_action_action=test_import_finding_action_action,
        test_import_finding_action_created=test_import_finding_action_created,
        test_import_finding_action_finding=test_import_finding_action_finding,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    branch_tag: Union[Unset, None, str] = UNSET,
    build_id: Union[Unset, None, str] = UNSET,
    commit_hash: Union[Unset, None, str] = UNSET,
    findings_affected: Union[Unset, None, List[int]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    prefetch: Union[Unset, None, List[TestImportsListPrefetchItem]] = UNSET,
    test: Union[Unset, None, int] = UNSET,
    test_import_finding_action_action: Union[Unset, None, TestImportsListTestImportFindingActionAction] = UNSET,
    test_import_finding_action_created: Union[Unset, None, datetime.datetime] = UNSET,
    test_import_finding_action_finding: Union[Unset, None, int] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        branch_tag (Union[Unset, None, str]):
        build_id (Union[Unset, None, str]):
        commit_hash (Union[Unset, None, str]):
        findings_affected (Union[Unset, None, List[int]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        prefetch (Union[Unset, None, List[TestImportsListPrefetchItem]]):
        test (Union[Unset, None, int]):
        test_import_finding_action_action (Union[Unset, None,
            TestImportsListTestImportFindingActionAction]):
        test_import_finding_action_created (Union[Unset, None, datetime.datetime]):
        test_import_finding_action_finding (Union[Unset, None, int]):
        version (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        branch_tag=branch_tag,
        build_id=build_id,
        commit_hash=commit_hash,
        findings_affected=findings_affected,
        limit=limit,
        offset=offset,
        prefetch=prefetch,
        test=test,
        test_import_finding_action_action=test_import_finding_action_action,
        test_import_finding_action_created=test_import_finding_action_created,
        test_import_finding_action_finding=test_import_finding_action_finding,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

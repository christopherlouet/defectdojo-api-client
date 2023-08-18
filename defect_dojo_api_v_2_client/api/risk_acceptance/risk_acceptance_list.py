import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.risk_acceptance_list_decision import RiskAcceptanceListDecision
from ...models.risk_acceptance_list_o_item import RiskAcceptanceListOItem
from ...models.risk_acceptance_list_security_recommendation import RiskAcceptanceListSecurityRecommendation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    accepted_by: Union[Unset, None, str] = UNSET,
    accepted_findings: Union[Unset, None, List[int]] = UNSET,
    decision: Union[Unset, None, RiskAcceptanceListDecision] = UNSET,
    decision_details: Union[Unset, None, str] = UNSET,
    expiration_date: Union[Unset, None, datetime.datetime] = UNSET,
    expiration_date_handled: Union[Unset, None, datetime.datetime] = UNSET,
    expiration_date_warned: Union[Unset, None, datetime.datetime] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    notes: Union[Unset, None, List[int]] = UNSET,
    o: Union[Unset, None, List[RiskAcceptanceListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    owner: Union[Unset, None, int] = UNSET,
    reactivate_expired: Union[Unset, None, bool] = UNSET,
    recommendation: Union[Unset, None, RiskAcceptanceListSecurityRecommendation] = UNSET,
    recommendation_details: Union[Unset, None, str] = UNSET,
    restart_sla_expired: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["accepted_by"] = accepted_by

    json_accepted_findings: Union[Unset, None, List[int]] = UNSET
    if not isinstance(accepted_findings, Unset):
        if accepted_findings is None:
            json_accepted_findings = None
        else:
            json_accepted_findings = accepted_findings

    params["accepted_findings"] = json_accepted_findings

    json_decision: Union[Unset, None, str] = UNSET
    if not isinstance(decision, Unset):
        json_decision = decision.value if decision else None

    params["decision"] = json_decision

    params["decision_details"] = decision_details

    json_expiration_date: Union[Unset, None, str] = UNSET
    if not isinstance(expiration_date, Unset):
        json_expiration_date = expiration_date.isoformat() if expiration_date else None

    params["expiration_date"] = json_expiration_date

    json_expiration_date_handled: Union[Unset, None, str] = UNSET
    if not isinstance(expiration_date_handled, Unset):
        json_expiration_date_handled = expiration_date_handled.isoformat() if expiration_date_handled else None

    params["expiration_date_handled"] = json_expiration_date_handled

    json_expiration_date_warned: Union[Unset, None, str] = UNSET
    if not isinstance(expiration_date_warned, Unset):
        json_expiration_date_warned = expiration_date_warned.isoformat() if expiration_date_warned else None

    params["expiration_date_warned"] = json_expiration_date_warned

    params["limit"] = limit

    params["name"] = name

    json_notes: Union[Unset, None, List[int]] = UNSET
    if not isinstance(notes, Unset):
        if notes is None:
            json_notes = None
        else:
            json_notes = notes

    params["notes"] = json_notes

    json_o: Union[Unset, None, List[str]] = UNSET
    if not isinstance(o, Unset):
        if o is None:
            json_o = None
        else:
            json_o = []
            for o_item_data in o:
                o_item = o_item_data.value

                json_o.append(o_item)

    params["o"] = json_o

    params["offset"] = offset

    params["owner"] = owner

    params["reactivate_expired"] = reactivate_expired

    json_recommendation: Union[Unset, None, str] = UNSET
    if not isinstance(recommendation, Unset):
        json_recommendation = recommendation.value if recommendation else None

    params["recommendation"] = json_recommendation

    params["recommendation_details"] = recommendation_details

    params["restart_sla_expired"] = restart_sla_expired

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v2/risk_acceptance/",
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
    accepted_by: Union[Unset, None, str] = UNSET,
    accepted_findings: Union[Unset, None, List[int]] = UNSET,
    decision: Union[Unset, None, RiskAcceptanceListDecision] = UNSET,
    decision_details: Union[Unset, None, str] = UNSET,
    expiration_date: Union[Unset, None, datetime.datetime] = UNSET,
    expiration_date_handled: Union[Unset, None, datetime.datetime] = UNSET,
    expiration_date_warned: Union[Unset, None, datetime.datetime] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    notes: Union[Unset, None, List[int]] = UNSET,
    o: Union[Unset, None, List[RiskAcceptanceListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    owner: Union[Unset, None, int] = UNSET,
    reactivate_expired: Union[Unset, None, bool] = UNSET,
    recommendation: Union[Unset, None, RiskAcceptanceListSecurityRecommendation] = UNSET,
    recommendation_details: Union[Unset, None, str] = UNSET,
    restart_sla_expired: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        accepted_by (Union[Unset, None, str]):
        accepted_findings (Union[Unset, None, List[int]]):
        decision (Union[Unset, None, RiskAcceptanceListDecision]):
        decision_details (Union[Unset, None, str]):
        expiration_date (Union[Unset, None, datetime.datetime]):
        expiration_date_handled (Union[Unset, None, datetime.datetime]):
        expiration_date_warned (Union[Unset, None, datetime.datetime]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        notes (Union[Unset, None, List[int]]):
        o (Union[Unset, None, List[RiskAcceptanceListOItem]]):
        offset (Union[Unset, None, int]):
        owner (Union[Unset, None, int]):
        reactivate_expired (Union[Unset, None, bool]):
        recommendation (Union[Unset, None, RiskAcceptanceListSecurityRecommendation]):
        recommendation_details (Union[Unset, None, str]):
        restart_sla_expired (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        accepted_by=accepted_by,
        accepted_findings=accepted_findings,
        decision=decision,
        decision_details=decision_details,
        expiration_date=expiration_date,
        expiration_date_handled=expiration_date_handled,
        expiration_date_warned=expiration_date_warned,
        limit=limit,
        name=name,
        notes=notes,
        o=o,
        offset=offset,
        owner=owner,
        reactivate_expired=reactivate_expired,
        recommendation=recommendation,
        recommendation_details=recommendation_details,
        restart_sla_expired=restart_sla_expired,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    accepted_by: Union[Unset, None, str] = UNSET,
    accepted_findings: Union[Unset, None, List[int]] = UNSET,
    decision: Union[Unset, None, RiskAcceptanceListDecision] = UNSET,
    decision_details: Union[Unset, None, str] = UNSET,
    expiration_date: Union[Unset, None, datetime.datetime] = UNSET,
    expiration_date_handled: Union[Unset, None, datetime.datetime] = UNSET,
    expiration_date_warned: Union[Unset, None, datetime.datetime] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    notes: Union[Unset, None, List[int]] = UNSET,
    o: Union[Unset, None, List[RiskAcceptanceListOItem]] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    owner: Union[Unset, None, int] = UNSET,
    reactivate_expired: Union[Unset, None, bool] = UNSET,
    recommendation: Union[Unset, None, RiskAcceptanceListSecurityRecommendation] = UNSET,
    recommendation_details: Union[Unset, None, str] = UNSET,
    restart_sla_expired: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """
    Args:
        accepted_by (Union[Unset, None, str]):
        accepted_findings (Union[Unset, None, List[int]]):
        decision (Union[Unset, None, RiskAcceptanceListDecision]):
        decision_details (Union[Unset, None, str]):
        expiration_date (Union[Unset, None, datetime.datetime]):
        expiration_date_handled (Union[Unset, None, datetime.datetime]):
        expiration_date_warned (Union[Unset, None, datetime.datetime]):
        limit (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        notes (Union[Unset, None, List[int]]):
        o (Union[Unset, None, List[RiskAcceptanceListOItem]]):
        offset (Union[Unset, None, int]):
        owner (Union[Unset, None, int]):
        reactivate_expired (Union[Unset, None, bool]):
        recommendation (Union[Unset, None, RiskAcceptanceListSecurityRecommendation]):
        recommendation_details (Union[Unset, None, str]):
        restart_sla_expired (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        accepted_by=accepted_by,
        accepted_findings=accepted_findings,
        decision=decision,
        decision_details=decision_details,
        expiration_date=expiration_date,
        expiration_date_handled=expiration_date_handled,
        expiration_date_warned=expiration_date_warned,
        limit=limit,
        name=name,
        notes=notes,
        o=o,
        offset=offset,
        owner=owner,
        reactivate_expired=reactivate_expired,
        recommendation=recommendation,
        recommendation_details=recommendation_details,
        restart_sla_expired=restart_sla_expired,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

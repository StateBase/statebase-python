from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.trace_list_response import TraceListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    session_id: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    start_time: None | str | Unset = UNSET,
    end_time: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_session_id: None | str | Unset
    if isinstance(session_id, Unset):
        json_session_id = UNSET
    else:
        json_session_id = session_id
    params["session_id"] = json_session_id

    json_action: None | str | Unset
    if isinstance(action, Unset):
        json_action = UNSET
    else:
        json_action = action
    params["action"] = json_action

    json_resource_type: None | str | Unset
    if isinstance(resource_type, Unset):
        json_resource_type = UNSET
    else:
        json_resource_type = resource_type
    params["resource_type"] = json_resource_type

    json_resource_id: None | str | Unset
    if isinstance(resource_id, Unset):
        json_resource_id = UNSET
    else:
        json_resource_id = resource_id
    params["resource_id"] = json_resource_id

    json_start_time: None | str | Unset
    if isinstance(start_time, Unset):
        json_start_time = UNSET
    else:
        json_start_time = start_time
    params["start_time"] = json_start_time

    json_end_time: None | str | Unset
    if isinstance(end_time, Unset):
        json_end_time = UNSET
    else:
        json_end_time = end_time
    params["end_time"] = json_end_time

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/traces",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TraceListResponse | None:
    if response.status_code == 200:
        response_200 = TraceListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | TraceListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    session_id: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    start_time: None | str | Unset = UNSET,
    end_time: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[HTTPValidationError | TraceListResponse]:
    """List Traces

     Retrieves traces with optional filtering.

    Args:
        session_id (None | str | Unset): Filter by session
        action (None | str | Unset): Filter by action type
        resource_type (None | str | Unset): Filter by resource type
        resource_id (None | str | Unset): Filter by resource identifier
        start_time (None | str | Unset): Filter traces after this time (ISO 8601)
        end_time (None | str | Unset): Filter traces before this time (ISO 8601)
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TraceListResponse]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        action=action,
        resource_type=resource_type,
        resource_id=resource_id,
        start_time=start_time,
        end_time=end_time,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    session_id: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    start_time: None | str | Unset = UNSET,
    end_time: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> HTTPValidationError | TraceListResponse | None:
    """List Traces

     Retrieves traces with optional filtering.

    Args:
        session_id (None | str | Unset): Filter by session
        action (None | str | Unset): Filter by action type
        resource_type (None | str | Unset): Filter by resource type
        resource_id (None | str | Unset): Filter by resource identifier
        start_time (None | str | Unset): Filter traces after this time (ISO 8601)
        end_time (None | str | Unset): Filter traces before this time (ISO 8601)
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TraceListResponse
    """

    return sync_detailed(
        client=client,
        session_id=session_id,
        action=action,
        resource_type=resource_type,
        resource_id=resource_id,
        start_time=start_time,
        end_time=end_time,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    session_id: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    start_time: None | str | Unset = UNSET,
    end_time: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> Response[HTTPValidationError | TraceListResponse]:
    """List Traces

     Retrieves traces with optional filtering.

    Args:
        session_id (None | str | Unset): Filter by session
        action (None | str | Unset): Filter by action type
        resource_type (None | str | Unset): Filter by resource type
        resource_id (None | str | Unset): Filter by resource identifier
        start_time (None | str | Unset): Filter traces after this time (ISO 8601)
        end_time (None | str | Unset): Filter traces before this time (ISO 8601)
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TraceListResponse]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        action=action,
        resource_type=resource_type,
        resource_id=resource_id,
        start_time=start_time,
        end_time=end_time,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    session_id: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    start_time: None | str | Unset = UNSET,
    end_time: None | str | Unset = UNSET,
    limit: int | Unset = 50,
) -> HTTPValidationError | TraceListResponse | None:
    """List Traces

     Retrieves traces with optional filtering.

    Args:
        session_id (None | str | Unset): Filter by session
        action (None | str | Unset): Filter by action type
        resource_type (None | str | Unset): Filter by resource type
        resource_id (None | str | Unset): Filter by resource identifier
        start_time (None | str | Unset): Filter traces after this time (ISO 8601)
        end_time (None | str | Unset): Filter traces before this time (ISO 8601)
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TraceListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            session_id=session_id,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
    ).parsed

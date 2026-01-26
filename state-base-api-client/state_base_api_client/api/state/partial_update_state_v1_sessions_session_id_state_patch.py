from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.state_partial_update_request import StatePartialUpdateRequest
from ...models.state_partial_update_response import StatePartialUpdateResponse
from ...types import Response


def _get_kwargs(
    session_id: str,
    *,
    body: StatePartialUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/sessions/{session_id}/state".format(
            session_id=quote(str(session_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | StatePartialUpdateResponse | None:
    if response.status_code == 200:
        response_200 = StatePartialUpdateResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | StatePartialUpdateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StatePartialUpdateRequest,
) -> Response[HTTPValidationError | StatePartialUpdateResponse]:
    """Partial Update State

     Updates specific fields within the session state.

    Args:
        session_id (str):
        body (StatePartialUpdateRequest): Request model for partial state update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StatePartialUpdateResponse]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StatePartialUpdateRequest,
) -> HTTPValidationError | StatePartialUpdateResponse | None:
    """Partial Update State

     Updates specific fields within the session state.

    Args:
        session_id (str):
        body (StatePartialUpdateRequest): Request model for partial state update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StatePartialUpdateResponse
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StatePartialUpdateRequest,
) -> Response[HTTPValidationError | StatePartialUpdateResponse]:
    """Partial Update State

     Updates specific fields within the session state.

    Args:
        session_id (str):
        body (StatePartialUpdateRequest): Request model for partial state update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StatePartialUpdateResponse]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StatePartialUpdateRequest,
) -> HTTPValidationError | StatePartialUpdateResponse | None:
    """Partial Update State

     Updates specific fields within the session state.

    Args:
        session_id (str):
        body (StatePartialUpdateRequest): Request model for partial state update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StatePartialUpdateResponse
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            body=body,
        )
    ).parsed

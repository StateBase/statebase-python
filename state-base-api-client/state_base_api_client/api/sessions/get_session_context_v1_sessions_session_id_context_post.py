from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.context_request import ContextRequest
from ...models.context_response import ContextResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    session_id: str,
    *,
    body: ContextRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sessions/{session_id}/context".format(
            session_id=quote(str(session_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContextResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ContextResponse.from_dict(response.json())

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
) -> Response[ContextResponse | HTTPValidationError]:
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
    body: ContextRequest,
) -> Response[ContextResponse | HTTPValidationError]:
    """Get Context

     Retrieves consolidated context (state, relevant memories, recent turns) for an agent.

    Args:
        session_id (str):
        body (ContextRequest): Request model for retrieving context.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContextResponse | HTTPValidationError]
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
    body: ContextRequest,
) -> ContextResponse | HTTPValidationError | None:
    """Get Context

     Retrieves consolidated context (state, relevant memories, recent turns) for an agent.

    Args:
        session_id (str):
        body (ContextRequest): Request model for retrieving context.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContextResponse | HTTPValidationError
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
    body: ContextRequest,
) -> Response[ContextResponse | HTTPValidationError]:
    """Get Context

     Retrieves consolidated context (state, relevant memories, recent turns) for an agent.

    Args:
        session_id (str):
        body (ContextRequest): Request model for retrieving context.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContextResponse | HTTPValidationError]
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
    body: ContextRequest,
) -> ContextResponse | HTTPValidationError | None:
    """Get Context

     Retrieves consolidated context (state, relevant memories, recent turns) for an agent.

    Args:
        session_id (str):
        body (ContextRequest): Request model for retrieving context.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContextResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            body=body,
        )
    ).parsed

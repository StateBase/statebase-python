from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.state_history_response import StateHistoryResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    session_id: str,
    *,
    limit: int | Unset = 50,
    since_version: int | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    json_since_version: int | None | Unset
    if isinstance(since_version, Unset):
        json_since_version = UNSET
    else:
        json_since_version = since_version
    params["since_version"] = json_since_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sessions/{session_id}/state/history".format(
            session_id=quote(str(session_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | StateHistoryResponse | None:
    if response.status_code == 200:
        response_200 = StateHistoryResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | StateHistoryResponse]:
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
    limit: int | Unset = 50,
    since_version: int | None | Unset = UNSET,
) -> Response[HTTPValidationError | StateHistoryResponse]:
    """Get State History

     Retrieves the history of state changes for a session.

    Args:
        session_id (str):
        limit (int | Unset):  Default: 50.
        since_version (int | None | Unset): Only return versions after this version

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StateHistoryResponse]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        limit=limit,
        since_version=since_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    since_version: int | None | Unset = UNSET,
) -> HTTPValidationError | StateHistoryResponse | None:
    """Get State History

     Retrieves the history of state changes for a session.

    Args:
        session_id (str):
        limit (int | Unset):  Default: 50.
        since_version (int | None | Unset): Only return versions after this version

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StateHistoryResponse
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
        limit=limit,
        since_version=since_version,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    since_version: int | None | Unset = UNSET,
) -> Response[HTTPValidationError | StateHistoryResponse]:
    """Get State History

     Retrieves the history of state changes for a session.

    Args:
        session_id (str):
        limit (int | Unset):  Default: 50.
        since_version (int | None | Unset): Only return versions after this version

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StateHistoryResponse]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        limit=limit,
        since_version=since_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    since_version: int | None | Unset = UNSET,
) -> HTTPValidationError | StateHistoryResponse | None:
    """Get State History

     Retrieves the history of state changes for a session.

    Args:
        session_id (str):
        limit (int | Unset):  Default: 50.
        since_version (int | None | Unset): Only return versions after this version

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StateHistoryResponse
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            limit=limit,
            since_version=since_version,
        )
    ).parsed

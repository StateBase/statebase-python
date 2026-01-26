from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.session_list_response import SessionListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent_id: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
    created_after: None | str | Unset = UNSET,
    created_before: None | str | Unset = UNSET,
    metadata: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_agent_id: None | str | Unset
    if isinstance(agent_id, Unset):
        json_agent_id = UNSET
    else:
        json_agent_id = agent_id
    params["agent_id"] = json_agent_id

    params["limit"] = limit

    json_starting_after: None | str | Unset
    if isinstance(starting_after, Unset):
        json_starting_after = UNSET
    else:
        json_starting_after = starting_after
    params["starting_after"] = json_starting_after

    json_created_after: None | str | Unset
    if isinstance(created_after, Unset):
        json_created_after = UNSET
    else:
        json_created_after = created_after
    params["created_after"] = json_created_after

    json_created_before: None | str | Unset
    if isinstance(created_before, Unset):
        json_created_before = UNSET
    else:
        json_created_before = created_before
    params["created_before"] = json_created_before

    json_metadata: None | str | Unset
    if isinstance(metadata, Unset):
        json_metadata = UNSET
    else:
        json_metadata = metadata
    params["metadata"] = json_metadata

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sessions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SessionListResponse | None:
    if response.status_code == 200:
        response_200 = SessionListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SessionListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
    created_after: None | str | Unset = UNSET,
    created_before: None | str | Unset = UNSET,
    metadata: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SessionListResponse]:
    """List Sessions

     Lists all sessions for the authenticated account with optional filtering.

    Args:
        agent_id (None | str | Unset): Filter by agent identifier
        limit (int | Unset): Maximum results Default: 20.
        starting_after (None | str | Unset): Pagination cursor
        created_after (None | str | Unset): Filter sessions created after
        created_before (None | str | Unset): Filter sessions created before
        metadata (None | str | Unset): Filter by metadata (JSON)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SessionListResponse]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        limit=limit,
        starting_after=starting_after,
        created_after=created_after,
        created_before=created_before,
        metadata=metadata,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
    created_after: None | str | Unset = UNSET,
    created_before: None | str | Unset = UNSET,
    metadata: None | str | Unset = UNSET,
) -> HTTPValidationError | SessionListResponse | None:
    """List Sessions

     Lists all sessions for the authenticated account with optional filtering.

    Args:
        agent_id (None | str | Unset): Filter by agent identifier
        limit (int | Unset): Maximum results Default: 20.
        starting_after (None | str | Unset): Pagination cursor
        created_after (None | str | Unset): Filter sessions created after
        created_before (None | str | Unset): Filter sessions created before
        metadata (None | str | Unset): Filter by metadata (JSON)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SessionListResponse
    """

    return sync_detailed(
        client=client,
        agent_id=agent_id,
        limit=limit,
        starting_after=starting_after,
        created_after=created_after,
        created_before=created_before,
        metadata=metadata,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
    created_after: None | str | Unset = UNSET,
    created_before: None | str | Unset = UNSET,
    metadata: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SessionListResponse]:
    """List Sessions

     Lists all sessions for the authenticated account with optional filtering.

    Args:
        agent_id (None | str | Unset): Filter by agent identifier
        limit (int | Unset): Maximum results Default: 20.
        starting_after (None | str | Unset): Pagination cursor
        created_after (None | str | Unset): Filter sessions created after
        created_before (None | str | Unset): Filter sessions created before
        metadata (None | str | Unset): Filter by metadata (JSON)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SessionListResponse]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        limit=limit,
        starting_after=starting_after,
        created_after=created_after,
        created_before=created_before,
        metadata=metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
    created_after: None | str | Unset = UNSET,
    created_before: None | str | Unset = UNSET,
    metadata: None | str | Unset = UNSET,
) -> HTTPValidationError | SessionListResponse | None:
    """List Sessions

     Lists all sessions for the authenticated account with optional filtering.

    Args:
        agent_id (None | str | Unset): Filter by agent identifier
        limit (int | Unset): Maximum results Default: 20.
        starting_after (None | str | Unset): Pagination cursor
        created_after (None | str | Unset): Filter sessions created after
        created_before (None | str | Unset): Filter sessions created before
        metadata (None | str | Unset): Filter by metadata (JSON)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SessionListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            agent_id=agent_id,
            limit=limit,
            starting_after=starting_after,
            created_after=created_after,
            created_before=created_before,
            metadata=metadata,
        )
    ).parsed

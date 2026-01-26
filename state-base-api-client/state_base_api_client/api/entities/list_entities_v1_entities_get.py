from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity_list_response import EntityListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    session_id: None | str | Unset = UNSET,
    entity_type: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_session_id: None | str | Unset
    if isinstance(session_id, Unset):
        json_session_id = UNSET
    else:
        json_session_id = session_id
    params["session_id"] = json_session_id

    json_entity_type: None | str | Unset
    if isinstance(entity_type, Unset):
        json_entity_type = UNSET
    else:
        json_entity_type = entity_type
    params["entity_type"] = json_entity_type

    params["limit"] = limit

    json_starting_after: None | str | Unset
    if isinstance(starting_after, Unset):
        json_starting_after = UNSET
    else:
        json_starting_after = starting_after
    params["starting_after"] = json_starting_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/entities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EntityListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EntityListResponse.from_dict(response.json())

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
) -> Response[EntityListResponse | HTTPValidationError]:
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
    entity_type: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
) -> Response[EntityListResponse | HTTPValidationError]:
    """List Entities

     Lists entities with optional filtering.

    Args:
        session_id (None | str | Unset): Filter by session
        entity_type (None | str | Unset): Filter by entity type
        limit (int | Unset):  Default: 20.
        starting_after (None | str | Unset): Pagination cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntityListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        entity_type=entity_type,
        limit=limit,
        starting_after=starting_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    session_id: None | str | Unset = UNSET,
    entity_type: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
) -> EntityListResponse | HTTPValidationError | None:
    """List Entities

     Lists entities with optional filtering.

    Args:
        session_id (None | str | Unset): Filter by session
        entity_type (None | str | Unset): Filter by entity type
        limit (int | Unset):  Default: 20.
        starting_after (None | str | Unset): Pagination cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntityListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        session_id=session_id,
        entity_type=entity_type,
        limit=limit,
        starting_after=starting_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    session_id: None | str | Unset = UNSET,
    entity_type: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
) -> Response[EntityListResponse | HTTPValidationError]:
    """List Entities

     Lists entities with optional filtering.

    Args:
        session_id (None | str | Unset): Filter by session
        entity_type (None | str | Unset): Filter by entity type
        limit (int | Unset):  Default: 20.
        starting_after (None | str | Unset): Pagination cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntityListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        entity_type=entity_type,
        limit=limit,
        starting_after=starting_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    session_id: None | str | Unset = UNSET,
    entity_type: None | str | Unset = UNSET,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
) -> EntityListResponse | HTTPValidationError | None:
    """List Entities

     Lists entities with optional filtering.

    Args:
        session_id (None | str | Unset): Filter by session
        entity_type (None | str | Unset): Filter by entity type
        limit (int | Unset):  Default: 20.
        starting_after (None | str | Unset): Pagination cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntityListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            session_id=session_id,
            entity_type=entity_type,
            limit=limit,
            starting_after=starting_after,
        )
    ).parsed

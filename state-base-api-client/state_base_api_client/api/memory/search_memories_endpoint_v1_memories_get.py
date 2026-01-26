from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.memory_search_response import MemorySearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    session_id: None | str | Unset = UNSET,
    types: None | str | Unset = UNSET,
    tags: None | str | Unset = UNSET,
    top_k: int | Unset = 10,
    threshold: float | Unset = 0.7,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    json_session_id: None | str | Unset
    if isinstance(session_id, Unset):
        json_session_id = UNSET
    else:
        json_session_id = session_id
    params["session_id"] = json_session_id

    json_types: None | str | Unset
    if isinstance(types, Unset):
        json_types = UNSET
    else:
        json_types = types
    params["types"] = json_types

    json_tags: None | str | Unset
    if isinstance(tags, Unset):
        json_tags = UNSET
    else:
        json_tags = tags
    params["tags"] = json_tags

    params["top_k"] = top_k

    params["threshold"] = threshold

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/memories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MemorySearchResponse | None:
    if response.status_code == 200:
        response_200 = MemorySearchResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | MemorySearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    session_id: None | str | Unset = UNSET,
    types: None | str | Unset = UNSET,
    tags: None | str | Unset = UNSET,
    top_k: int | Unset = 10,
    threshold: float | Unset = 0.7,
) -> Response[HTTPValidationError | MemorySearchResponse]:
    """Search Memories

     Performs semantic similarity search across memories.

    Args:
        query (str): Search query text
        session_id (None | str | Unset): Limit search to specific session
        types (None | str | Unset): Filter by memory types (comma-separated)
        tags (None | str | Unset): Filter by tags (comma-separated)
        top_k (int | Unset):  Default: 10.
        threshold (float | Unset):  Default: 0.7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemorySearchResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        session_id=session_id,
        types=types,
        tags=tags,
        top_k=top_k,
        threshold=threshold,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    session_id: None | str | Unset = UNSET,
    types: None | str | Unset = UNSET,
    tags: None | str | Unset = UNSET,
    top_k: int | Unset = 10,
    threshold: float | Unset = 0.7,
) -> HTTPValidationError | MemorySearchResponse | None:
    """Search Memories

     Performs semantic similarity search across memories.

    Args:
        query (str): Search query text
        session_id (None | str | Unset): Limit search to specific session
        types (None | str | Unset): Filter by memory types (comma-separated)
        tags (None | str | Unset): Filter by tags (comma-separated)
        top_k (int | Unset):  Default: 10.
        threshold (float | Unset):  Default: 0.7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemorySearchResponse
    """

    return sync_detailed(
        client=client,
        query=query,
        session_id=session_id,
        types=types,
        tags=tags,
        top_k=top_k,
        threshold=threshold,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    session_id: None | str | Unset = UNSET,
    types: None | str | Unset = UNSET,
    tags: None | str | Unset = UNSET,
    top_k: int | Unset = 10,
    threshold: float | Unset = 0.7,
) -> Response[HTTPValidationError | MemorySearchResponse]:
    """Search Memories

     Performs semantic similarity search across memories.

    Args:
        query (str): Search query text
        session_id (None | str | Unset): Limit search to specific session
        types (None | str | Unset): Filter by memory types (comma-separated)
        tags (None | str | Unset): Filter by tags (comma-separated)
        top_k (int | Unset):  Default: 10.
        threshold (float | Unset):  Default: 0.7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemorySearchResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        session_id=session_id,
        types=types,
        tags=tags,
        top_k=top_k,
        threshold=threshold,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    session_id: None | str | Unset = UNSET,
    types: None | str | Unset = UNSET,
    tags: None | str | Unset = UNSET,
    top_k: int | Unset = 10,
    threshold: float | Unset = 0.7,
) -> HTTPValidationError | MemorySearchResponse | None:
    """Search Memories

     Performs semantic similarity search across memories.

    Args:
        query (str): Search query text
        session_id (None | str | Unset): Limit search to specific session
        types (None | str | Unset): Filter by memory types (comma-separated)
        tags (None | str | Unset): Filter by tags (comma-separated)
        top_k (int | Unset):  Default: 10.
        threshold (float | Unset):  Default: 0.7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemorySearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            session_id=session_id,
            types=types,
            tags=tags,
            top_k=top_k,
            threshold=threshold,
        )
    ).parsed

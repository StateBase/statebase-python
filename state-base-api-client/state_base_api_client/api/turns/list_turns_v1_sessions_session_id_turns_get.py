from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.turn_list_response import TurnListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    session_id: str,
    *,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
    order: str | Unset = "desc",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    json_starting_after: None | str | Unset
    if isinstance(starting_after, Unset):
        json_starting_after = UNSET
    else:
        json_starting_after = starting_after
    params["starting_after"] = json_starting_after

    params["order"] = order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sessions/{session_id}/turns".format(
            session_id=quote(str(session_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TurnListResponse | None:
    if response.status_code == 200:
        response_200 = TurnListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TurnListResponse]:
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
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
    order: str | Unset = "desc",
) -> Response[HTTPValidationError | TurnListResponse]:
    """List Turns

     Lists all turns within a session.

    Args:
        session_id (str):
        limit (int | Unset):  Default: 20.
        starting_after (None | str | Unset):
        order (str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TurnListResponse]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        limit=limit,
        starting_after=starting_after,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
    order: str | Unset = "desc",
) -> HTTPValidationError | TurnListResponse | None:
    """List Turns

     Lists all turns within a session.

    Args:
        session_id (str):
        limit (int | Unset):  Default: 20.
        starting_after (None | str | Unset):
        order (str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TurnListResponse
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
        limit=limit,
        starting_after=starting_after,
        order=order,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
    order: str | Unset = "desc",
) -> Response[HTTPValidationError | TurnListResponse]:
    """List Turns

     Lists all turns within a session.

    Args:
        session_id (str):
        limit (int | Unset):  Default: 20.
        starting_after (None | str | Unset):
        order (str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TurnListResponse]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        limit=limit,
        starting_after=starting_after,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    starting_after: None | str | Unset = UNSET,
    order: str | Unset = "desc",
) -> HTTPValidationError | TurnListResponse | None:
    """List Turns

     Lists all turns within a session.

    Args:
        session_id (str):
        limit (int | Unset):  Default: 20.
        starting_after (None | str | Unset):
        order (str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TurnListResponse
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            limit=limit,
            starting_after=starting_after,
            order=order,
        )
    ).parsed

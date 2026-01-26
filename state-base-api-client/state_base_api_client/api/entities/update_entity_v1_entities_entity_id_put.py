from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity_update_request import EntityUpdateRequest
from ...models.entity_update_response import EntityUpdateResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    entity_id: str,
    *,
    body: EntityUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/entities/{entity_id}".format(
            entity_id=quote(str(entity_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EntityUpdateResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EntityUpdateResponse.from_dict(response.json())

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
) -> Response[EntityUpdateResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EntityUpdateRequest,
) -> Response[EntityUpdateResponse | HTTPValidationError]:
    """Update Entity

     Updates entity attributes.

    Args:
        entity_id (str):
        body (EntityUpdateRequest): Request model for updating an entity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntityUpdateResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        entity_id=entity_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EntityUpdateRequest,
) -> EntityUpdateResponse | HTTPValidationError | None:
    """Update Entity

     Updates entity attributes.

    Args:
        entity_id (str):
        body (EntityUpdateRequest): Request model for updating an entity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntityUpdateResponse | HTTPValidationError
    """

    return sync_detailed(
        entity_id=entity_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EntityUpdateRequest,
) -> Response[EntityUpdateResponse | HTTPValidationError]:
    """Update Entity

     Updates entity attributes.

    Args:
        entity_id (str):
        body (EntityUpdateRequest): Request model for updating an entity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntityUpdateResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        entity_id=entity_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EntityUpdateRequest,
) -> EntityUpdateResponse | HTTPValidationError | None:
    """Update Entity

     Updates entity attributes.

    Args:
        entity_id (str):
        body (EntityUpdateRequest): Request model for updating an entity.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntityUpdateResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            entity_id=entity_id,
            client=client,
            body=body,
        )
    ).parsed

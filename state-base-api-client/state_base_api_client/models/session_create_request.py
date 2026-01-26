from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_create_request_initial_state_type_0 import SessionCreateRequestInitialStateType0
    from ..models.session_create_request_metadata_type_0 import SessionCreateRequestMetadataType0


T = TypeVar("T", bound="SessionCreateRequest")


@_attrs_define
class SessionCreateRequest:
    """Request model for creating a new session.

    Attributes:
        agent_id (str): Unique agent identifier
        metadata (None | SessionCreateRequestMetadataType0 | Unset): Arbitrary metadata for the session
        initial_state (None | SessionCreateRequestInitialStateType0 | Unset): Initial state values
        ttl_seconds (int | None | Unset): Session TTL in seconds
    """

    agent_id: str
    metadata: None | SessionCreateRequestMetadataType0 | Unset = UNSET
    initial_state: None | SessionCreateRequestInitialStateType0 | Unset = UNSET
    ttl_seconds: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_create_request_initial_state_type_0 import SessionCreateRequestInitialStateType0
        from ..models.session_create_request_metadata_type_0 import SessionCreateRequestMetadataType0

        agent_id = self.agent_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, SessionCreateRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        initial_state: dict[str, Any] | None | Unset
        if isinstance(self.initial_state, Unset):
            initial_state = UNSET
        elif isinstance(self.initial_state, SessionCreateRequestInitialStateType0):
            initial_state = self.initial_state.to_dict()
        else:
            initial_state = self.initial_state

        ttl_seconds: int | None | Unset
        if isinstance(self.ttl_seconds, Unset):
            ttl_seconds = UNSET
        else:
            ttl_seconds = self.ttl_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if initial_state is not UNSET:
            field_dict["initial_state"] = initial_state
        if ttl_seconds is not UNSET:
            field_dict["ttl_seconds"] = ttl_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_create_request_initial_state_type_0 import SessionCreateRequestInitialStateType0
        from ..models.session_create_request_metadata_type_0 import SessionCreateRequestMetadataType0

        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        def _parse_metadata(data: object) -> None | SessionCreateRequestMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SessionCreateRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionCreateRequestMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_initial_state(data: object) -> None | SessionCreateRequestInitialStateType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                initial_state_type_0 = SessionCreateRequestInitialStateType0.from_dict(data)

                return initial_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionCreateRequestInitialStateType0 | Unset, data)

        initial_state = _parse_initial_state(d.pop("initial_state", UNSET))

        def _parse_ttl_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ttl_seconds = _parse_ttl_seconds(d.pop("ttl_seconds", UNSET))

        session_create_request = cls(
            agent_id=agent_id,
            metadata=metadata,
            initial_state=initial_state,
            ttl_seconds=ttl_seconds,
        )

        session_create_request.additional_properties = d
        return session_create_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

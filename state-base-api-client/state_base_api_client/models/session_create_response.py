from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_create_response_metadata_type_0 import SessionCreateResponseMetadataType0
    from ..models.session_create_response_state import SessionCreateResponseState


T = TypeVar("T", bound="SessionCreateResponse")


@_attrs_define
class SessionCreateResponse:
    """Response model for session creation.

    Attributes:
        id (str):
        agent_id (str):
        created_at (str):
        updated_at (str):
        metadata (None | SessionCreateResponseMetadataType0):
        state (SessionCreateResponseState):
        memory_count (int):
        turn_count (int):
        ttl_expires_at (None | str):
        object_ (str | Unset):  Default: 'session'.
    """

    id: str
    agent_id: str
    created_at: str
    updated_at: str
    metadata: None | SessionCreateResponseMetadataType0
    state: SessionCreateResponseState
    memory_count: int
    turn_count: int
    ttl_expires_at: None | str
    object_: str | Unset = "session"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_create_response_metadata_type_0 import SessionCreateResponseMetadataType0

        id = self.id

        agent_id = self.agent_id

        created_at = self.created_at

        updated_at = self.updated_at

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, SessionCreateResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        state = self.state.to_dict()

        memory_count = self.memory_count

        turn_count = self.turn_count

        ttl_expires_at: None | str
        ttl_expires_at = self.ttl_expires_at

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "agent_id": agent_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "metadata": metadata,
                "state": state,
                "memory_count": memory_count,
                "turn_count": turn_count,
                "ttl_expires_at": ttl_expires_at,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_create_response_metadata_type_0 import SessionCreateResponseMetadataType0
        from ..models.session_create_response_state import SessionCreateResponseState

        d = dict(src_dict)
        id = d.pop("id")

        agent_id = d.pop("agent_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_metadata(data: object) -> None | SessionCreateResponseMetadataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SessionCreateResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionCreateResponseMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata"))

        state = SessionCreateResponseState.from_dict(d.pop("state"))

        memory_count = d.pop("memory_count")

        turn_count = d.pop("turn_count")

        def _parse_ttl_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ttl_expires_at = _parse_ttl_expires_at(d.pop("ttl_expires_at"))

        object_ = d.pop("object", UNSET)

        session_create_response = cls(
            id=id,
            agent_id=agent_id,
            created_at=created_at,
            updated_at=updated_at,
            metadata=metadata,
            state=state,
            memory_count=memory_count,
            turn_count=turn_count,
            ttl_expires_at=ttl_expires_at,
            object_=object_,
        )

        session_create_response.additional_properties = d
        return session_create_response

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

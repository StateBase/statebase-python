from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_metadata_update_response_metadata_type_0 import SessionMetadataUpdateResponseMetadataType0


T = TypeVar("T", bound="SessionMetadataUpdateResponse")


@_attrs_define
class SessionMetadataUpdateResponse:
    """Response model for metadata update.

    Attributes:
        id (str):
        agent_id (str):
        updated_at (str):
        metadata (None | SessionMetadataUpdateResponseMetadataType0):
        ttl_expires_at (None | str):
        object_ (str | Unset):  Default: 'session'.
    """

    id: str
    agent_id: str
    updated_at: str
    metadata: None | SessionMetadataUpdateResponseMetadataType0
    ttl_expires_at: None | str
    object_: str | Unset = "session"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_metadata_update_response_metadata_type_0 import SessionMetadataUpdateResponseMetadataType0

        id = self.id

        agent_id = self.agent_id

        updated_at = self.updated_at

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, SessionMetadataUpdateResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        ttl_expires_at: None | str
        ttl_expires_at = self.ttl_expires_at

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "agent_id": agent_id,
                "updated_at": updated_at,
                "metadata": metadata,
                "ttl_expires_at": ttl_expires_at,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_metadata_update_response_metadata_type_0 import SessionMetadataUpdateResponseMetadataType0

        d = dict(src_dict)
        id = d.pop("id")

        agent_id = d.pop("agent_id")

        updated_at = d.pop("updated_at")

        def _parse_metadata(data: object) -> None | SessionMetadataUpdateResponseMetadataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SessionMetadataUpdateResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionMetadataUpdateResponseMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata"))

        def _parse_ttl_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ttl_expires_at = _parse_ttl_expires_at(d.pop("ttl_expires_at"))

        object_ = d.pop("object", UNSET)

        session_metadata_update_response = cls(
            id=id,
            agent_id=agent_id,
            updated_at=updated_at,
            metadata=metadata,
            ttl_expires_at=ttl_expires_at,
            object_=object_,
        )

        session_metadata_update_response.additional_properties = d
        return session_metadata_update_response

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

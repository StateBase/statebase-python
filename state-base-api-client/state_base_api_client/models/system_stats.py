from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemStats")


@_attrs_define
class SystemStats:
    """Aggregate system statistics.

    Attributes:
        total_sessions (int):
        total_turns (int):
        total_memories (int):
        total_entities (int):
        active_sessions_24h (int):
        storage_usage_bytes (int | None | Unset):  Default: 0.
    """

    total_sessions: int
    total_turns: int
    total_memories: int
    total_entities: int
    active_sessions_24h: int
    storage_usage_bytes: int | None | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_sessions = self.total_sessions

        total_turns = self.total_turns

        total_memories = self.total_memories

        total_entities = self.total_entities

        active_sessions_24h = self.active_sessions_24h

        storage_usage_bytes: int | None | Unset
        if isinstance(self.storage_usage_bytes, Unset):
            storage_usage_bytes = UNSET
        else:
            storage_usage_bytes = self.storage_usage_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_sessions": total_sessions,
                "total_turns": total_turns,
                "total_memories": total_memories,
                "total_entities": total_entities,
                "active_sessions_24h": active_sessions_24h,
            }
        )
        if storage_usage_bytes is not UNSET:
            field_dict["storage_usage_bytes"] = storage_usage_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_sessions = d.pop("total_sessions")

        total_turns = d.pop("total_turns")

        total_memories = d.pop("total_memories")

        total_entities = d.pop("total_entities")

        active_sessions_24h = d.pop("active_sessions_24h")

        def _parse_storage_usage_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_usage_bytes = _parse_storage_usage_bytes(d.pop("storage_usage_bytes", UNSET))

        system_stats = cls(
            total_sessions=total_sessions,
            total_turns=total_turns,
            total_memories=total_memories,
            total_entities=total_entities,
            active_sessions_24h=active_sessions_24h,
            storage_usage_bytes=storage_usage_bytes,
        )

        system_stats.additional_properties = d
        return system_stats

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

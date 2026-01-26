from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionListItem")


@_attrs_define
class SessionListItem:
    """Session list item model (reduced details).

    Attributes:
        id (str):
        agent_id (str):
        created_at (str):
        updated_at (str):
        memory_count (int):
        turn_count (int):
        object_ (str | Unset):  Default: 'session'.
    """

    id: str
    agent_id: str
    created_at: str
    updated_at: str
    memory_count: int
    turn_count: int
    object_: str | Unset = "session"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        agent_id = self.agent_id

        created_at = self.created_at

        updated_at = self.updated_at

        memory_count = self.memory_count

        turn_count = self.turn_count

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "agent_id": agent_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "memory_count": memory_count,
                "turn_count": turn_count,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        agent_id = d.pop("agent_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        memory_count = d.pop("memory_count")

        turn_count = d.pop("turn_count")

        object_ = d.pop("object", UNSET)

        session_list_item = cls(
            id=id,
            agent_id=agent_id,
            created_at=created_at,
            updated_at=updated_at,
            memory_count=memory_count,
            turn_count=turn_count,
            object_=object_,
        )

        session_list_item.additional_properties = d
        return session_list_item

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

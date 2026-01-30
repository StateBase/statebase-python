from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.context_response_memories_item import ContextResponseMemoriesItem
    from ..models.context_response_recent_turns_item import ContextResponseRecentTurnsItem
    from ..models.context_response_state import ContextResponseState


T = TypeVar("T", bound="ContextResponse")


@_attrs_define
class ContextResponse:
    """Response model for session context.

    Attributes:
        state (ContextResponseState):
        memories (list[ContextResponseMemoriesItem]):
        recent_turns (list[ContextResponseRecentTurnsItem]):
    """

    state: ContextResponseState
    memories: list[ContextResponseMemoriesItem]
    recent_turns: list[ContextResponseRecentTurnsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.to_dict()

        memories = []
        for memories_item_data in self.memories:
            memories_item = memories_item_data.to_dict()
            memories.append(memories_item)

        recent_turns = []
        for recent_turns_item_data in self.recent_turns:
            recent_turns_item = recent_turns_item_data.to_dict()
            recent_turns.append(recent_turns_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "memories": memories,
                "recent_turns": recent_turns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context_response_memories_item import ContextResponseMemoriesItem
        from ..models.context_response_recent_turns_item import ContextResponseRecentTurnsItem
        from ..models.context_response_state import ContextResponseState

        d = dict(src_dict)
        state = ContextResponseState.from_dict(d.pop("state"))

        memories = []
        _memories = d.pop("memories")
        for memories_item_data in _memories:
            memories_item = ContextResponseMemoriesItem.from_dict(memories_item_data)

            memories.append(memories_item)

        recent_turns = []
        _recent_turns = d.pop("recent_turns")
        for recent_turns_item_data in _recent_turns:
            recent_turns_item = ContextResponseRecentTurnsItem.from_dict(recent_turns_item_data)

            recent_turns.append(recent_turns_item)

        context_response = cls(
            state=state,
            memories=memories,
            recent_turns=recent_turns,
        )

        context_response.additional_properties = d
        return context_response

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

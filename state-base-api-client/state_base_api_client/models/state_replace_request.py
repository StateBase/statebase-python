from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.state_replace_request_state import StateReplaceRequestState


T = TypeVar("T", bound="StateReplaceRequest")


@_attrs_define
class StateReplaceRequest:
    """Request model for replacing state.

    Attributes:
        state (StateReplaceRequestState): Complete state object
    """

    state: StateReplaceRequestState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_replace_request_state import StateReplaceRequestState

        d = dict(src_dict)
        state = StateReplaceRequestState.from_dict(d.pop("state"))

        state_replace_request = cls(
            state=state,
        )

        state_replace_request.additional_properties = d
        return state_replace_request

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.state_rollback_response_state import StateRollbackResponseState


T = TypeVar("T", bound="StateRollbackResponse")


@_attrs_define
class StateRollbackResponse:
    """Response model for rollback operation.

    Attributes:
        success (bool):
        new_version (int):
        restored_from_version (int):
        state (StateRollbackResponseState):
        trace_id (str):
    """

    success: bool
    new_version: int
    restored_from_version: int
    state: StateRollbackResponseState
    trace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        new_version = self.new_version

        restored_from_version = self.restored_from_version

        state = self.state.to_dict()

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "new_version": new_version,
                "restored_from_version": restored_from_version,
                "state": state,
                "trace_id": trace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_rollback_response_state import StateRollbackResponseState

        d = dict(src_dict)
        success = d.pop("success")

        new_version = d.pop("new_version")

        restored_from_version = d.pop("restored_from_version")

        state = StateRollbackResponseState.from_dict(d.pop("state"))

        trace_id = d.pop("trace_id")

        state_rollback_response = cls(
            success=success,
            new_version=new_version,
            restored_from_version=restored_from_version,
            state=state,
            trace_id=trace_id,
        )

        state_rollback_response.additional_properties = d
        return state_rollback_response

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

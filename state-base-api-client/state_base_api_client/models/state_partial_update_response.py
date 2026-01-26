from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.state_partial_update_response_data import StatePartialUpdateResponseData
    from ..models.state_partial_update_response_state import StatePartialUpdateResponseState


T = TypeVar("T", bound="StatePartialUpdateResponse")


@_attrs_define
class StatePartialUpdateResponse:
    """Response model for partial state update.

    Attributes:
        data (StatePartialUpdateResponseData):
        session_id (str):
        version (int):
        state (StatePartialUpdateResponseState):
        updated_at (str):
    """

    data: StatePartialUpdateResponseData
    session_id: str
    version: int
    state: StatePartialUpdateResponseState
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        session_id = self.session_id

        version = self.version

        state = self.state.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "session_id": session_id,
                "version": version,
                "state": state,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_partial_update_response_data import StatePartialUpdateResponseData
        from ..models.state_partial_update_response_state import StatePartialUpdateResponseState

        d = dict(src_dict)
        data = StatePartialUpdateResponseData.from_dict(d.pop("data"))

        session_id = d.pop("session_id")

        version = d.pop("version")

        state = StatePartialUpdateResponseState.from_dict(d.pop("state"))

        updated_at = d.pop("updated_at")

        state_partial_update_response = cls(
            data=data,
            session_id=session_id,
            version=version,
            state=state,
            updated_at=updated_at,
        )

        state_partial_update_response.additional_properties = d
        return state_partial_update_response

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

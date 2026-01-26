from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.state_version_model_state import StateVersionModelState


T = TypeVar("T", bound="StateVersionModel")


@_attrs_define
class StateVersionModel:
    """State version model for history.

    Attributes:
        version (int):
        state (StateVersionModelState):
        created_at (str):
        updated_by (None | str):
    """

    version: int
    state: StateVersionModelState
    created_at: str
    updated_by: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        state = self.state.to_dict()

        created_at = self.created_at

        updated_by: None | str
        updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "state": state,
                "created_at": created_at,
                "updated_by": updated_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_version_model_state import StateVersionModelState

        d = dict(src_dict)
        version = d.pop("version")

        state = StateVersionModelState.from_dict(d.pop("state"))

        created_at = d.pop("created_at")

        def _parse_updated_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_by = _parse_updated_by(d.pop("updated_by"))

        state_version_model = cls(
            version=version,
            state=state,
            created_at=created_at,
            updated_by=updated_by,
        )

        state_version_model.additional_properties = d
        return state_version_model

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

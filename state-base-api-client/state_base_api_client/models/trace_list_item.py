from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TraceListItem")


@_attrs_define
class TraceListItem:
    """Trace list item model.

    Attributes:
        id (str):
        session_id (str):
        action (str):
        resource_type (str):
        resource_id (str):
        actor (str):
        timestamp (str):
    """

    id: str
    session_id: str
    action: str
    resource_type: str
    resource_id: str
    actor: str
    timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        session_id = self.session_id

        action = self.action

        resource_type = self.resource_type

        resource_id = self.resource_id

        actor = self.actor

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "session_id": session_id,
                "action": action,
                "resource_type": resource_type,
                "resource_id": resource_id,
                "actor": actor,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        session_id = d.pop("session_id")

        action = d.pop("action")

        resource_type = d.pop("resource_type")

        resource_id = d.pop("resource_id")

        actor = d.pop("actor")

        timestamp = d.pop("timestamp")

        trace_list_item = cls(
            id=id,
            session_id=session_id,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            actor=actor,
            timestamp=timestamp,
        )

        trace_list_item.additional_properties = d
        return trace_list_item

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

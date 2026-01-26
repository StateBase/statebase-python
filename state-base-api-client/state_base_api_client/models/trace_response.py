from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.trace_context import TraceContext
    from ..models.trace_response_details_type_0 import TraceResponseDetailsType0


T = TypeVar("T", bound="TraceResponse")


@_attrs_define
class TraceResponse:
    """Response model for trace details.

    Attributes:
        id (str):
        session_id (str):
        action (str):
        resource_type (str):
        resource_id (str):
        actor (str):
        actor_id (None | str):
        details (None | TraceResponseDetailsType0):
        context (None | TraceContext):
        timestamp (str):
        ip_address (None | str):
    """

    id: str
    session_id: str
    action: str
    resource_type: str
    resource_id: str
    actor: str
    actor_id: None | str
    details: None | TraceResponseDetailsType0
    context: None | TraceContext
    timestamp: str
    ip_address: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_context import TraceContext
        from ..models.trace_response_details_type_0 import TraceResponseDetailsType0

        id = self.id

        session_id = self.session_id

        action = self.action

        resource_type = self.resource_type

        resource_id = self.resource_id

        actor = self.actor

        actor_id: None | str
        actor_id = self.actor_id

        details: dict[str, Any] | None
        if isinstance(self.details, TraceResponseDetailsType0):
            details = self.details.to_dict()
        else:
            details = self.details

        context: dict[str, Any] | None
        if isinstance(self.context, TraceContext):
            context = self.context.to_dict()
        else:
            context = self.context

        timestamp = self.timestamp

        ip_address: None | str
        ip_address = self.ip_address

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
                "actor_id": actor_id,
                "details": details,
                "context": context,
                "timestamp": timestamp,
                "ip_address": ip_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_context import TraceContext
        from ..models.trace_response_details_type_0 import TraceResponseDetailsType0

        d = dict(src_dict)
        id = d.pop("id")

        session_id = d.pop("session_id")

        action = d.pop("action")

        resource_type = d.pop("resource_type")

        resource_id = d.pop("resource_id")

        actor = d.pop("actor")

        def _parse_actor_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        actor_id = _parse_actor_id(d.pop("actor_id"))

        def _parse_details(data: object) -> None | TraceResponseDetailsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = TraceResponseDetailsType0.from_dict(data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TraceResponseDetailsType0, data)

        details = _parse_details(d.pop("details"))

        def _parse_context(data: object) -> None | TraceContext:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_0 = TraceContext.from_dict(data)

                return context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TraceContext, data)

        context = _parse_context(d.pop("context"))

        timestamp = d.pop("timestamp")

        def _parse_ip_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip_address = _parse_ip_address(d.pop("ip_address"))

        trace_response = cls(
            id=id,
            session_id=session_id,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            actor=actor,
            actor_id=actor_id,
            details=details,
            context=context,
            timestamp=timestamp,
            ip_address=ip_address,
        )

        trace_response.additional_properties = d
        return trace_response

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

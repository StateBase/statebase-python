from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContextRequest")


@_attrs_define
class ContextRequest:
    """Request model for retrieving context.

    Attributes:
        query (None | str | Unset): Query to search relevant memories
        memory_limit (int | Unset): Max memories to return Default: 5.
        turn_limit (int | Unset): Max recent turns to return Default: 5.
    """

    query: None | str | Unset = UNSET
    memory_limit: int | Unset = 5
    turn_limit: int | Unset = 5
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        memory_limit = self.memory_limit

        turn_limit = self.turn_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if memory_limit is not UNSET:
            field_dict["memory_limit"] = memory_limit
        if turn_limit is not UNSET:
            field_dict["turn_limit"] = turn_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        memory_limit = d.pop("memory_limit", UNSET)

        turn_limit = d.pop("turn_limit", UNSET)

        context_request = cls(
            query=query,
            memory_limit=memory_limit,
            turn_limit=turn_limit,
        )

        context_request.additional_properties = d
        return context_request

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

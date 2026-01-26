from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MemorySearchResult")


@_attrs_define
class MemorySearchResult:
    """Search result item model.

    Attributes:
        id (str):
        session_id (str):
        content (str):
        type_ (str):
        score (float):
    """

    id: str
    session_id: str
    content: str
    type_: str
    score: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        session_id = self.session_id

        content = self.content

        type_ = self.type_

        score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "session_id": session_id,
                "content": content,
                "type": type_,
                "score": score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        session_id = d.pop("session_id")

        content = d.pop("content")

        type_ = d.pop("type")

        score = d.pop("score")

        memory_search_result = cls(
            id=id,
            session_id=session_id,
            content=content,
            type_=type_,
            score=score,
        )

        memory_search_result.additional_properties = d
        return memory_search_result

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

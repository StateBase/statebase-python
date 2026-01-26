from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryUpdateResponse")


@_attrs_define
class MemoryUpdateResponse:
    """Response model for memory update.

    Attributes:
        id (str):
        updated_at (str):
        content (str):
        type_ (str):
        tags (list[str] | None):
        version (int):
        object_ (str | Unset):  Default: 'memory'.
    """

    id: str
    updated_at: str
    content: str
    type_: str
    tags: list[str] | None
    version: int
    object_: str | Unset = "memory"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        updated_at = self.updated_at

        content = self.content

        type_ = self.type_

        tags: list[str] | None
        if isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        version = self.version

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "updated_at": updated_at,
                "content": content,
                "type": type_,
                "tags": tags,
                "version": version,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        updated_at = d.pop("updated_at")

        content = d.pop("content")

        type_ = d.pop("type")

        def _parse_tags(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        tags = _parse_tags(d.pop("tags"))

        version = d.pop("version")

        object_ = d.pop("object", UNSET)

        memory_update_response = cls(
            id=id,
            updated_at=updated_at,
            content=content,
            type_=type_,
            tags=tags,
            version=version,
            object_=object_,
        )

        memory_update_response.additional_properties = d
        return memory_update_response

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

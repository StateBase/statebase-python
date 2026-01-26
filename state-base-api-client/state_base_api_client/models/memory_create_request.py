from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_create_request_metadata_type_0 import MemoryCreateRequestMetadataType0


T = TypeVar("T", bound="MemoryCreateRequest")


@_attrs_define
class MemoryCreateRequest:
    """Request model for creating a new memory.

    Attributes:
        session_id (str): Session to associate with memory
        content (str): Memory content text
        type_ (str | Unset): Memory classification Default: 'general'.
        tags (list[str] | None | Unset): Tags for categorization
        metadata (MemoryCreateRequestMetadataType0 | None | Unset): Additional metadata
        embed (bool | Unset): Generate vector embedding Default: True.
    """

    session_id: str
    content: str
    type_: str | Unset = "general"
    tags: list[str] | None | Unset = UNSET
    metadata: MemoryCreateRequestMetadataType0 | None | Unset = UNSET
    embed: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.memory_create_request_metadata_type_0 import MemoryCreateRequestMetadataType0

        session_id = self.session_id

        content = self.content

        type_ = self.type_

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, MemoryCreateRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        embed = self.embed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
                "content": content,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if tags is not UNSET:
            field_dict["tags"] = tags
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if embed is not UNSET:
            field_dict["embed"] = embed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_create_request_metadata_type_0 import MemoryCreateRequestMetadataType0

        d = dict(src_dict)
        session_id = d.pop("session_id")

        content = d.pop("content")

        type_ = d.pop("type", UNSET)

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_metadata(data: object) -> MemoryCreateRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = MemoryCreateRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MemoryCreateRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        embed = d.pop("embed", UNSET)

        memory_create_request = cls(
            session_id=session_id,
            content=content,
            type_=type_,
            tags=tags,
            metadata=metadata,
            embed=embed,
        )

        memory_create_request.additional_properties = d
        return memory_create_request

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_response_metadata_type_0 import MemoryResponseMetadataType0


T = TypeVar("T", bound="MemoryResponse")


@_attrs_define
class MemoryResponse:
    """Response model for memory details.

    Attributes:
        id (str):
        session_id (str):
        created_at (str):
        content (str):
        type_ (str):
        tags (list[str] | None):
        metadata (MemoryResponseMetadataType0 | None):
        embedding_id (None | str):
        vector_available (bool):
        object_ (str | Unset):  Default: 'memory'.
    """

    id: str
    session_id: str
    created_at: str
    content: str
    type_: str
    tags: list[str] | None
    metadata: MemoryResponseMetadataType0 | None
    embedding_id: None | str
    vector_available: bool
    object_: str | Unset = "memory"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.memory_response_metadata_type_0 import MemoryResponseMetadataType0

        id = self.id

        session_id = self.session_id

        created_at = self.created_at

        content = self.content

        type_ = self.type_

        tags: list[str] | None
        if isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, MemoryResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        embedding_id: None | str
        embedding_id = self.embedding_id

        vector_available = self.vector_available

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "session_id": session_id,
                "created_at": created_at,
                "content": content,
                "type": type_,
                "tags": tags,
                "metadata": metadata,
                "embedding_id": embedding_id,
                "vector_available": vector_available,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_response_metadata_type_0 import MemoryResponseMetadataType0

        d = dict(src_dict)
        id = d.pop("id")

        session_id = d.pop("session_id")

        created_at = d.pop("created_at")

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

        def _parse_metadata(data: object) -> MemoryResponseMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = MemoryResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MemoryResponseMetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        def _parse_embedding_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        embedding_id = _parse_embedding_id(d.pop("embedding_id"))

        vector_available = d.pop("vector_available")

        object_ = d.pop("object", UNSET)

        memory_response = cls(
            id=id,
            session_id=session_id,
            created_at=created_at,
            content=content,
            type_=type_,
            tags=tags,
            metadata=metadata,
            embedding_id=embedding_id,
            vector_available=vector_available,
            object_=object_,
        )

        memory_response.additional_properties = d
        return memory_response

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

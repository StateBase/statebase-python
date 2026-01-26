from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityListItem")


@_attrs_define
class EntityListItem:
    """Entity list item model (reduced details).

    Attributes:
        id (str):
        entity_type (str):
        entity_id (str):
        created_at (str):
        object_ (str | Unset):  Default: 'entity'.
    """

    id: str
    entity_type: str
    entity_id: str
    created_at: str
    object_: str | Unset = "entity"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        entity_type = self.entity_type

        entity_id = self.entity_id

        created_at = self.created_at

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "entity_type": entity_type,
                "entity_id": entity_id,
                "created_at": created_at,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        entity_type = d.pop("entity_type")

        entity_id = d.pop("entity_id")

        created_at = d.pop("created_at")

        object_ = d.pop("object", UNSET)

        entity_list_item = cls(
            id=id,
            entity_type=entity_type,
            entity_id=entity_id,
            created_at=created_at,
            object_=object_,
        )

        entity_list_item.additional_properties = d
        return entity_list_item

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

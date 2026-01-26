from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_update_response_attributes import EntityUpdateResponseAttributes


T = TypeVar("T", bound="EntityUpdateResponse")


@_attrs_define
class EntityUpdateResponse:
    """Response model for entity update.

    Attributes:
        id (str):
        updated_at (str):
        attributes (EntityUpdateResponseAttributes):
        version (int):
        object_ (str | Unset):  Default: 'entity'.
    """

    id: str
    updated_at: str
    attributes: EntityUpdateResponseAttributes
    version: int
    object_: str | Unset = "entity"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        updated_at = self.updated_at

        attributes = self.attributes.to_dict()

        version = self.version

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "updated_at": updated_at,
                "attributes": attributes,
                "version": version,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_update_response_attributes import EntityUpdateResponseAttributes

        d = dict(src_dict)
        id = d.pop("id")

        updated_at = d.pop("updated_at")

        attributes = EntityUpdateResponseAttributes.from_dict(d.pop("attributes"))

        version = d.pop("version")

        object_ = d.pop("object", UNSET)

        entity_update_response = cls(
            id=id,
            updated_at=updated_at,
            attributes=attributes,
            version=version,
            object_=object_,
        )

        entity_update_response.additional_properties = d
        return entity_update_response

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

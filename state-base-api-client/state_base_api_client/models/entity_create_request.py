from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.entity_create_request_attributes import EntityCreateRequestAttributes


T = TypeVar("T", bound="EntityCreateRequest")


@_attrs_define
class EntityCreateRequest:
    """Request model for creating a new entity.

    Attributes:
        session_id (str): Session to associate with entity
        entity_type (str): Entity type (e.g., 'product', 'customer')
        entity_id (str): Application-level entity ID
        attributes (EntityCreateRequestAttributes): Entity attributes
    """

    session_id: str
    entity_type: str
    entity_id: str
    attributes: EntityCreateRequestAttributes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        entity_type = self.entity_type

        entity_id = self.entity_id

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session_id": session_id,
                "entity_type": entity_type,
                "entity_id": entity_id,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_create_request_attributes import EntityCreateRequestAttributes

        d = dict(src_dict)
        session_id = d.pop("session_id")

        entity_type = d.pop("entity_type")

        entity_id = d.pop("entity_id")

        attributes = EntityCreateRequestAttributes.from_dict(d.pop("attributes"))

        entity_create_request = cls(
            session_id=session_id,
            entity_type=entity_type,
            entity_id=entity_id,
            attributes=attributes,
        )

        entity_create_request.additional_properties = d
        return entity_create_request

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

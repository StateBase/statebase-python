from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TurnListItem")


@_attrs_define
class TurnListItem:
    """Turn list item model (reduced details).

    Attributes:
        id (str):
        created_at (str):
        turn_number (int):
        input_preview (str):
        output_preview (str):
        object_ (str | Unset):  Default: 'turn'.
    """

    id: str
    created_at: str
    turn_number: int
    input_preview: str
    output_preview: str
    object_: str | Unset = "turn"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at

        turn_number = self.turn_number

        input_preview = self.input_preview

        output_preview = self.output_preview

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "turn_number": turn_number,
                "input_preview": input_preview,
                "output_preview": output_preview,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("created_at")

        turn_number = d.pop("turn_number")

        input_preview = d.pop("input_preview")

        output_preview = d.pop("output_preview")

        object_ = d.pop("object", UNSET)

        turn_list_item = cls(
            id=id,
            created_at=created_at,
            turn_number=turn_number,
            input_preview=input_preview,
            output_preview=output_preview,
            object_=object_,
        )

        turn_list_item.additional_properties = d
        return turn_list_item

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

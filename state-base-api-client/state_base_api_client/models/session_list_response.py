from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.session_list_item import SessionListItem


T = TypeVar("T", bound="SessionListResponse")


@_attrs_define
class SessionListResponse:
    """Response model for session listing.

    Attributes:
        data (list[SessionListItem]):
        has_more (bool):
        first_id (None | str):
        last_id (None | str):
    """

    data: list[SessionListItem]
    has_more: bool
    first_id: None | str
    last_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        has_more = self.has_more

        first_id: None | str
        first_id = self.first_id

        last_id: None | str
        last_id = self.last_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "has_more": has_more,
                "first_id": first_id,
                "last_id": last_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_list_item import SessionListItem

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = SessionListItem.from_dict(data_item_data)

            data.append(data_item)

        has_more = d.pop("has_more")

        def _parse_first_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_id = _parse_first_id(d.pop("first_id"))

        def _parse_last_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_id = _parse_last_id(d.pop("last_id"))

        session_list_response = cls(
            data=data,
            has_more=has_more,
            first_id=first_id,
            last_id=last_id,
        )

        session_list_response.additional_properties = d
        return session_list_response

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

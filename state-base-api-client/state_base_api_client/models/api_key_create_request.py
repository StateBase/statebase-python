from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="APIKeyCreateRequest")


@_attrs_define
class APIKeyCreateRequest:
    """
    Attributes:
        name (str):
        rate_limit (int | Unset):  Default: 100.
        expires_days (int | None | Unset):
        owner_id (None | str | Unset):
    """

    name: str
    rate_limit: int | Unset = 100
    expires_days: int | None | Unset = UNSET
    owner_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        rate_limit = self.rate_limit

        expires_days: int | None | Unset
        if isinstance(self.expires_days, Unset):
            expires_days = UNSET
        else:
            expires_days = self.expires_days

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if rate_limit is not UNSET:
            field_dict["rate_limit"] = rate_limit
        if expires_days is not UNSET:
            field_dict["expires_days"] = expires_days
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        rate_limit = d.pop("rate_limit", UNSET)

        def _parse_expires_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_days = _parse_expires_days(d.pop("expires_days", UNSET))

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))

        api_key_create_request = cls(
            name=name,
            rate_limit=rate_limit,
            expires_days=expires_days,
            owner_id=owner_id,
        )

        api_key_create_request.additional_properties = d
        return api_key_create_request

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

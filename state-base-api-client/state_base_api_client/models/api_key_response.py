from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="APIKeyResponse")


@_attrs_define
class APIKeyResponse:
    """
    Attributes:
        id (str):
        key_prefix (str):
        name (str):
        is_active (bool):
        rate_limit (int):
        created_at (str):
        last_used_at (None | str):
        expires_at (None | str):
        total_requests (int):
        full_key (None | str | Unset):
    """

    id: str
    key_prefix: str
    name: str
    is_active: bool
    rate_limit: int
    created_at: str
    last_used_at: None | str
    expires_at: None | str
    total_requests: int
    full_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key_prefix = self.key_prefix

        name = self.name

        is_active = self.is_active

        rate_limit = self.rate_limit

        created_at = self.created_at

        last_used_at: None | str
        last_used_at = self.last_used_at

        expires_at: None | str
        expires_at = self.expires_at

        total_requests = self.total_requests

        full_key: None | str | Unset
        if isinstance(self.full_key, Unset):
            full_key = UNSET
        else:
            full_key = self.full_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "key_prefix": key_prefix,
                "name": name,
                "is_active": is_active,
                "rate_limit": rate_limit,
                "created_at": created_at,
                "last_used_at": last_used_at,
                "expires_at": expires_at,
                "total_requests": total_requests,
            }
        )
        if full_key is not UNSET:
            field_dict["full_key"] = full_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        key_prefix = d.pop("key_prefix")

        name = d.pop("name")

        is_active = d.pop("is_active")

        rate_limit = d.pop("rate_limit")

        created_at = d.pop("created_at")

        def _parse_last_used_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        total_requests = d.pop("total_requests")

        def _parse_full_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_key = _parse_full_key(d.pop("full_key", UNSET))

        api_key_response = cls(
            id=id,
            key_prefix=key_prefix,
            name=name,
            is_active=is_active,
            rate_limit=rate_limit,
            created_at=created_at,
            last_used_at=last_used_at,
            expires_at=expires_at,
            total_requests=total_requests,
            full_key=full_key,
        )

        api_key_response.additional_properties = d
        return api_key_response

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

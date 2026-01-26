from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.activity_time_series import ActivityTimeSeries
    from ..models.system_stats import SystemStats


T = TypeVar("T", bound="DashboardOverviewResponse")


@_attrs_define
class DashboardOverviewResponse:
    """Dashboard home stats.

    Attributes:
        stats (SystemStats): Aggregate system statistics.
        recent_activity (list[ActivityTimeSeries]):
    """

    stats: SystemStats
    recent_activity: list[ActivityTimeSeries]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stats = self.stats.to_dict()

        recent_activity = []
        for recent_activity_item_data in self.recent_activity:
            recent_activity_item = recent_activity_item_data.to_dict()
            recent_activity.append(recent_activity_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stats": stats,
                "recent_activity": recent_activity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_time_series import ActivityTimeSeries
        from ..models.system_stats import SystemStats

        d = dict(src_dict)
        stats = SystemStats.from_dict(d.pop("stats"))

        recent_activity = []
        _recent_activity = d.pop("recent_activity")
        for recent_activity_item_data in _recent_activity:
            recent_activity_item = ActivityTimeSeries.from_dict(recent_activity_item_data)

            recent_activity.append(recent_activity_item)

        dashboard_overview_response = cls(
            stats=stats,
            recent_activity=recent_activity,
        )

        dashboard_overview_response.additional_properties = d
        return dashboard_overview_response

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

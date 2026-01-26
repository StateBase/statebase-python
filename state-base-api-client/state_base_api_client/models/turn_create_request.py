from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.turn_create_request_metadata_type_0 import TurnCreateRequestMetadataType0
    from ..models.turn_input import TurnInput
    from ..models.turn_output import TurnOutput


T = TypeVar("T", bound="TurnCreateRequest")


@_attrs_define
class TurnCreateRequest:
    """Request model for creating a new turn.

    Attributes:
        input_ (TurnInput): Input content for a turn.
        output (TurnOutput): Output content from a turn.
        metadata (None | TurnCreateRequestMetadataType0 | Unset): Additional metadata
        reasoning (None | str | Unset): Agent reasoning trace
    """

    input_: TurnInput
    output: TurnOutput
    metadata: None | TurnCreateRequestMetadataType0 | Unset = UNSET
    reasoning: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.turn_create_request_metadata_type_0 import TurnCreateRequestMetadataType0

        input_ = self.input_.to_dict()

        output = self.output.to_dict()

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, TurnCreateRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        reasoning: None | str | Unset
        if isinstance(self.reasoning, Unset):
            reasoning = UNSET
        else:
            reasoning = self.reasoning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
                "output": output,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if reasoning is not UNSET:
            field_dict["reasoning"] = reasoning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.turn_create_request_metadata_type_0 import TurnCreateRequestMetadataType0
        from ..models.turn_input import TurnInput
        from ..models.turn_output import TurnOutput

        d = dict(src_dict)
        input_ = TurnInput.from_dict(d.pop("input"))

        output = TurnOutput.from_dict(d.pop("output"))

        def _parse_metadata(data: object) -> None | TurnCreateRequestMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = TurnCreateRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TurnCreateRequestMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_reasoning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reasoning = _parse_reasoning(d.pop("reasoning", UNSET))

        turn_create_request = cls(
            input_=input_,
            output=output,
            metadata=metadata,
            reasoning=reasoning,
        )

        turn_create_request.additional_properties = d
        return turn_create_request

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

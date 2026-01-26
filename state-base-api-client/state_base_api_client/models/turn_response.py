from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.turn_input import TurnInput
    from ..models.turn_output import TurnOutput
    from ..models.turn_response_metadata_type_0 import TurnResponseMetadataType0


T = TypeVar("T", bound="TurnResponse")


@_attrs_define
class TurnResponse:
    """Response model for turn details.

    Attributes:
        id (str):
        session_id (str):
        created_at (str):
        turn_number (int):
        input_ (TurnInput): Input content for a turn.
        output (TurnOutput): Output content from a turn.
        metadata (None | TurnResponseMetadataType0):
        reasoning (None | str):
        object_ (str | Unset):  Default: 'turn'.
    """

    id: str
    session_id: str
    created_at: str
    turn_number: int
    input_: TurnInput
    output: TurnOutput
    metadata: None | TurnResponseMetadataType0
    reasoning: None | str
    object_: str | Unset = "turn"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.turn_response_metadata_type_0 import TurnResponseMetadataType0

        id = self.id

        session_id = self.session_id

        created_at = self.created_at

        turn_number = self.turn_number

        input_ = self.input_.to_dict()

        output = self.output.to_dict()

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, TurnResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        reasoning: None | str
        reasoning = self.reasoning

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "session_id": session_id,
                "created_at": created_at,
                "turn_number": turn_number,
                "input": input_,
                "output": output,
                "metadata": metadata,
                "reasoning": reasoning,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.turn_input import TurnInput
        from ..models.turn_output import TurnOutput
        from ..models.turn_response_metadata_type_0 import TurnResponseMetadataType0

        d = dict(src_dict)
        id = d.pop("id")

        session_id = d.pop("session_id")

        created_at = d.pop("created_at")

        turn_number = d.pop("turn_number")

        input_ = TurnInput.from_dict(d.pop("input"))

        output = TurnOutput.from_dict(d.pop("output"))

        def _parse_metadata(data: object) -> None | TurnResponseMetadataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = TurnResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TurnResponseMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata"))

        def _parse_reasoning(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reasoning = _parse_reasoning(d.pop("reasoning"))

        object_ = d.pop("object", UNSET)

        turn_response = cls(
            id=id,
            session_id=session_id,
            created_at=created_at,
            turn_number=turn_number,
            input_=input_,
            output=output,
            metadata=metadata,
            reasoning=reasoning,
            object_=object_,
        )

        turn_response.additional_properties = d
        return turn_response

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

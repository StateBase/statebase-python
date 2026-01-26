"""
StateBase SDK Models
"""
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field


class SessionCreateRequest(BaseModel):
    agent_id: str
    metadata: Optional[Dict[str, Any]] = None
    initial_state: Optional[Dict[str, Any]] = None
    ttl_seconds: Optional[int] = None


class SessionResponse(BaseModel):
    object: str = "session"
    id: str
    agent_id: str
    created_at: str
    updated_at: str
    metadata: Optional[Dict[str, Any]] = None
    state: Dict[str, Any]
    memory_count: int
    turn_count: int
    ttl_expires_at: Optional[str] = None


class TurnInput(BaseModel):
    type: str
    content: str


class TurnOutput(BaseModel):
    type: str
    content: str


class TurnCreateRequest(BaseModel):
    input: TurnInput
    output: TurnOutput
    metadata: Optional[Dict[str, Any]] = None
    reasoning: Optional[str] = None


class TurnResponse(BaseModel):
    object: str = "turn"
    id: str
    session_id: str
    turn_number: int
    input: TurnInput
    output: TurnOutput
    metadata: Optional[Dict[str, Any]] = None
    reasoning: Optional[str] = None
    state_before: Dict[str, Any]
    state_after: Dict[str, Any]
    created_at: str


class MemoryCreateRequest(BaseModel):
    content: str
    memory_type: str = "fact"
    session_id: Optional[str] = None
    tags: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None


class MemoryResponse(BaseModel):
    object: str = "memory"
    id: str
    content: str
    memory_type: str
    session_id: Optional[str] = None
    tags: List[str] = []
    metadata: Optional[Dict[str, Any]] = None
    created_at: str
    updated_at: str


class StateUpdateRequest(BaseModel):
    updates: Dict[str, Any]
    reasoning: Optional[str] = None


class StateReplaceRequest(BaseModel):
    state: Dict[str, Any]
    reasoning: Optional[str] = None

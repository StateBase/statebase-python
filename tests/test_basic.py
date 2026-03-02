import pytest
from statebase import StateBase, AsyncStateBase
from statebase.models import SessionResponse

def test_client_init():
    """Verify that clients can be initialized"""
    client = StateBase(api_key="sb_test_123")
    assert client.base_url == "https://api.statebase.org"
    
def test_models():
    """Verify that models can be instantiated"""
    # Simple dummy data
    data = {
        "id": "sess_123",
        "agent_id": "test_agent",
        "created_at": "2023-01-01T00:00:00Z",
        "updated_at": "2023-01-01T00:00:00Z",
        "state": {"count": 1},
        "memory_count": 0,
        "turn_count": 0
    }
    session = SessionResponse(**data)
    assert session.id == "sess_123"
    assert session.state["count"] == 1

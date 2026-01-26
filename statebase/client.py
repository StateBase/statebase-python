"""
StateBase Python SDK - Synchronous Client
"""
import httpx
from typing import Optional, Dict, Any, List
from .models import (
    SessionCreateRequest,
    SessionResponse,
    TurnCreateRequest,
    TurnResponse,
    MemoryCreateRequest,
    MemoryResponse,
    StateUpdateRequest,
)


class StateBase:
    """Synchronous client for StateBase API"""
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.statebase.org",
        timeout: float = 30.0
    ):
        """
        Initialize StateBase client.
        
        Args:
            api_key: Your StateBase API key
            base_url: Base URL for the API (default: production)
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.client = httpx.Client(
            headers={
                "X-API-Key": api_key,
                "Content-Type": "application/json"
            },
            timeout=timeout
        )
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self.close()
    
    def close(self):
        """Close the HTTP client"""
        self.client.close()
    
    # Sessions
    def create_session(
        self,
        agent_id: str,
        metadata: Optional[Dict[str, Any]] = None,
        initial_state: Optional[Dict[str, Any]] = None,
        ttl_seconds: Optional[int] = None
    ) -> SessionResponse:
        """Create a new session"""
        response = self.client.post(
            f"{self.base_url}/v1/sessions",
            json={
                "agent_id": agent_id,
                "metadata": metadata,
                "initial_state": initial_state,
                "ttl_seconds": ttl_seconds
            }
        )
        response.raise_for_status()
        return SessionResponse(**response.json())
    
    def get_session(self, session_id: str) -> SessionResponse:
        """Get session by ID"""
        response = self.client.get(f"{self.base_url}/v1/sessions/{session_id}")
        response.raise_for_status()
        return SessionResponse(**response.json())
    
    def delete_session(self, session_id: str) -> None:
        """Delete a session"""
        response = self.client.delete(f"{self.base_url}/v1/sessions/{session_id}")
        response.raise_for_status()
    
    # Turns
    def create_turn(
        self,
        session_id: str,
        input_content: str,
        output_content: str,
        input_type: str = "text",
        output_type: str = "text",
        metadata: Optional[Dict[str, Any]] = None,
        reasoning: Optional[str] = None
    ) -> TurnResponse:
        """Create a new turn in a session"""
        response = self.client.post(
            f"{self.base_url}/v1/sessions/{session_id}/turns",
            json={
                "input": {"type": input_type, "content": input_content},
                "output": {"type": output_type, "content": output_content},
                "metadata": metadata,
                "reasoning": reasoning
            }
        )
        response.raise_for_status()
        return TurnResponse(**response.json())
    
    # State
    def get_state(self, session_id: str) -> Dict[str, Any]:
        """Get current state of a session"""
        response = self.client.get(f"{self.base_url}/v1/sessions/{session_id}/state")
        response.raise_for_status()
        return response.json()
    
    def update_state(
        self,
        session_id: str,
        updates: Dict[str, Any],
        reasoning: Optional[str] = None
    ) -> Dict[str, Any]:
        """Partially update session state"""
        response = self.client.patch(
            f"{self.base_url}/v1/sessions/{session_id}/state",
            json={"state": updates, "reasoning": reasoning}
        )
        response.raise_for_status()
        return response.json()
    
    def replace_state(
        self,
        session_id: str,
        state: Dict[str, Any],
        reasoning: Optional[str] = None
    ) -> Dict[str, Any]:
        """Replace entire session state"""
        response = self.client.put(
            f"{self.base_url}/v1/sessions/{session_id}/state",
            json={"state": state, "reasoning": reasoning}
        )
        response.raise_for_status()
        return response.json()
    
    # Memories
    def create_memory(
        self,
        content: str,
        memory_type: str = "fact",
        session_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> MemoryResponse:
        """Create a new memory"""
        response = self.client.post(
            f"{self.base_url}/v1/memories",
            json={
                "content": content,
                "type": memory_type,
                "session_id": session_id,
                "tags": tags,
                "metadata": metadata
            }
        )
        response.raise_for_status()
        return MemoryResponse(**response.json())
    
    def search_memories(
        self,
        query: str,
        session_id: Optional[str] = None,
        memory_type: Optional[str] = None,
        limit: int = 10
    ) -> List[MemoryResponse]:
        """Search memories by semantic similarity"""
        params = {"query": query, "limit": limit}
        if session_id:
            params["session_id"] = session_id
        if memory_type:
            params["types"] = memory_type
        
        response = self.client.get(f"{self.base_url}/v1/memories/search", params=params)
        response.raise_for_status()
        return [MemoryResponse(**m) for m in response.json().get("data", [])]
    
    # Health
    def health(self) -> Dict[str, Any]:
        """Check API health"""
        response = self.client.get(f"{self.base_url}/health")
        response.raise_for_status()
        return response.json()

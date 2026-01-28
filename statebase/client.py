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

class SessionsClient:
    def __init__(self, client: httpx.Client, base_url: str):
        self.client = client
        self.base_url = base_url

    def create(
        self,
        agent_id: str,
        user_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        initial_state: Optional[Dict[str, Any]] = None,
        ttl_seconds: Optional[int] = None
    ) -> SessionResponse:
        """Create a new session"""
        payload = {
            "agent_id": agent_id,
            "metadata": metadata,
            "initial_state": initial_state,
            "ttl_seconds": ttl_seconds,
        }
        if user_id:
            payload["user_id"] = user_id

        response = self.client.post(f"{self.base_url}/v1/sessions", json=payload)
        response.raise_for_status()
        return SessionResponse(**response.json())

    def get(self, session_id: str) -> SessionResponse:
        """Get session by ID"""
        response = self.client.get(f"{self.base_url}/v1/sessions/{session_id}")
        response.raise_for_status()
        return SessionResponse(**response.json())
    
    def get_context(self, session_id: str, query: str) -> Dict[str, Any]:
        """Get processed context for LLM generation"""
        response = self.client.post(
            f"{self.base_url}/v1/sessions/{session_id}/context",
            json={"query": query}
        )
        response.raise_for_status()
        return response.json()

    def add_turn(
        self,
        session_id: str,
        input: Any,
        output: Any,
        metadata: Optional[Dict[str, Any]] = None,
        reasoning: Optional[str] = None
    ) -> TurnResponse:
        """Log a turn to a session"""
        # Handle simple string usage
        if isinstance(input, str):
            input = {"type": "text", "content": input}
        if isinstance(output, str):
            output = {"type": "text", "content": output}

        response = self.client.post(
            f"{self.base_url}/v1/sessions/{session_id}/turns",
            json={
                "input": input,
                "output": output,
                "metadata": metadata,
                "reasoning": reasoning
            }
        )
        response.raise_for_status()
        return TurnResponse(**response.json())

    def update_state(
        self,
        session_id: str,
        state: Dict[str, Any],
        reasoning: Optional[str] = None
    ) -> Dict[str, Any]:
        """Partially update session state"""
        response = self.client.patch(
            f"{self.base_url}/v1/sessions/{session_id}/state",
            json={"state": state, "reasoning": reasoning}
        )
        response.raise_for_status()
        return response.json()


class MemoryClient:
    def __init__(self, client: httpx.Client, base_url: str):
        self.client = client
        self.base_url = base_url

    def add(
        self,
        content: str,
        user_id: Optional[str] = None,
        agent_id: Optional[str] = None,
        type: str = "fact",
        session_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> MemoryResponse:
        """Create a new memory"""
        response = self.client.post(
            f"{self.base_url}/v1/memories",
            json={
                "content": content,
                "type": type,
                "session_id": session_id,
                "user_id": user_id,
                "agent_id": agent_id,
                "tags": tags,
                "metadata": metadata
            }
        )
        response.raise_for_status()
        return MemoryResponse(**response.json())

    def search(
        self,
        query: str,
        user_id: Optional[str] = None,
        session_id: Optional[str] = None,
        types: Optional[List[str]] = None,
        limit: int = 10,
        threshold: float = 0.75
    ) -> List[MemoryResponse]:
        """Search memories"""
        params = {"query": query, "limit": limit, "threshold": threshold}
        if session_id:
            params["session_id"] = session_id
        if user_id:
            params["user_id"] = user_id
        # Handle list in query params if needed, simplified here
        
        response = self.client.get(f"{self.base_url}/v1/memories/search", params=params)
        response.raise_for_status()
        return [MemoryResponse(**m) for m in response.json().get("data", [])]


class StateBase:
    """Synchronous client for StateBase API"""
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.statebase.org",
        timeout: float = 30.0
    ):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.client = httpx.Client(
            headers={
                "Authorization": f"Bearer {api_key}",
                "X-API-Key": api_key, # Support both styles for now
                "Content-Type": "application/json"
            },
            timeout=timeout
        )

        # Namespaced Clients
        self.sessions = SessionsClient(self.client, self.base_url)
        self.memory = MemoryClient(self.client, self.base_url)
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self.close()
    
    def close(self):
        self.client.close()

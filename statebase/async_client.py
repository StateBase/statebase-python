"""
StateBase Python SDK - Async Client
"""
import httpx
from typing import Optional, Dict, Any, List
from .models import (
    SessionResponse,
    TurnResponse,
    MemoryResponse,
    MemorySearchResult,
    StateGetResponse,
)


class AsyncStateBase:
    """Asynchronous client for StateBase API"""
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.statebase.org",
        timeout: float = 30.0
    ):
        """
        Initialize async StateBase client.
        
        Args:
            api_key: Your StateBase API key
            base_url: Base URL for the API
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.client = httpx.AsyncClient(
            headers={
                "X-API-Key": api_key,
                "Content-Type": "application/json"
            },
            timeout=timeout
        )
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, *args):
        await self.close()
    
    async def close(self):
        """Close the HTTP client"""
        await self.client.aclose()
    
    # Sessions
    async def create_session(
        self,
        agent_id: str,
        metadata: Optional[Dict[str, Any]] = None,
        initial_state: Optional[Dict[str, Any]] = None,
        ttl_seconds: Optional[int] = None
    ) -> SessionResponse:
        """Create a new session"""
        response = await self.client.post(
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
    
    async def get_session(self, session_id: str) -> SessionResponse:
        """Get session by ID"""
        response = await self.client.get(f"{self.base_url}/v1/sessions/{session_id}")
        response.raise_for_status()
        return SessionResponse(**response.json())
    
    async def delete_session(self, session_id: str) -> None:
        """Delete a session"""
        response = await self.client.delete(f"{self.base_url}/v1/sessions/{session_id}")
        response.raise_for_status()

    async def get_context(
        self,
        session_id: str,
        query: Optional[str] = None,
        memory_limit: int = 5,
        turn_limit: int = 5
    ) -> Dict[str, Any]:
        """Get consolidated context (state, relevant memories, recent turns)"""
        payload = {
            "query": query,
            "memory_limit": memory_limit,
            "turn_limit": turn_limit
        }
        response = await self.client.post(
            f"{self.base_url}/v1/sessions/{session_id}/context",
            json=payload
        )
        response.raise_for_status()
        return response.json()
    
    # Turns
    async def create_turn(
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
        response = await self.client.post(
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
    async def get_state(self, session_id: str) -> Dict[str, Any]:
        """Get current state of a session"""
        response = await self.client.get(f"{self.base_url}/v1/sessions/{session_id}/state")
        response.raise_for_status()
        return response.json()
    
    async def update_state(
        self,
        session_id: str,
        state: Dict[str, Any],
        reasoning: Optional[str] = None
    ) -> Dict[str, Any]:
        """Partially update session state"""
        response = await self.client.patch(
            f"{self.base_url}/v1/sessions/{session_id}/state",
            json={"state": state, "reasoning": reasoning}
        )
        response.raise_for_status()
        return response.json()
    
    async def replace_state(
        self,
        session_id: str,
        state: Dict[str, Any],
        reasoning: Optional[str] = None
    ) -> Dict[str, Any]:
        """Replace entire session state"""
        response = await self.client.put(
            f"{self.base_url}/v1/sessions/{session_id}/state",
            json={"state": state, "reasoning": reasoning}
        )
        response.raise_for_status()
        return response.json()
    
    # Memories
    async def create_memory(
        self,
        content: str,
        type: str = "fact",
        session_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> MemoryResponse:
        """Create a new memory"""
        response = await self.client.post(
            f"{self.base_url}/v1/memories",
            json={
                "content": content,
                "type": type,
                "session_id": session_id,
                "tags": tags,
                "metadata": metadata
            }
        )
        response.raise_for_status()
        return MemoryResponse(**response.json())
    
    async def search_memories(
        self,
        query: str,
        session_id: Optional[str] = None,
        types: Optional[str] = None,
        tags: Optional[str] = None,
        limit: int = 10,
        threshold: float = 0.7
    ) -> List[MemorySearchResult]:
        """Search memories using semantic similarity"""
        params = {
            "query": query,
            "limit": limit,
            "threshold": threshold
        }
        if session_id:
            params["session_id"] = session_id
        if types:
            params["types"] = types
        if tags:
            params["tags"] = tags
        
        response = await self.client.get(f"{self.base_url}/v1/memories", params=params)
        response.raise_for_status()
        return [MemorySearchResult(**m) for m in response.json().get("data", [])]

    async def list_turns(self, session_id: str, limit: int = 20, starting_after: Optional[str] = None) -> List[TurnResponse]:
        """List turns in a session"""
        params = {"limit": limit}
        if starting_after:
            params["starting_after"] = starting_after
        response = await self.client.get(f"{self.base_url}/v1/sessions/{session_id}/turns", params=params)
        response.raise_for_status()
        return [TurnResponse(**t) for t in response.json().get("data", [])]
    
    # Health
    async def health(self) -> Dict[str, Any]:
        """Check API health"""
        response = await self.client.get(f"{self.base_url}/health")
        response.raise_for_status()
        return response.json()

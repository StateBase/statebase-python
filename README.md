# StateBase Python SDK

The official Python client for [StateBase](https://statebase.org) - The Reliability Layer for Production AI Agents.

Manage persistent memory, deterministic state, and real-time observability for your AI agents with a simple, unified API.

[![PyPI version](https://badge.fury.io/py/statebase.svg)](https://badge.fury.io/py/statebase)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📦 Installation

```bash
pip install statebase
```

## 🚀 Quick Start

### API Key
You need a StateBase API Key. You can get one by signing up at [statebase.org](https://statebase.org) or hosting your own instance.

### Usage

```python
from statebase import StateBase

# Initialize the client
client = StateBase(api_key="sb_live_...")

# 1. Create a Session with strict state
session = client.create_session(
    agent_id="support-agent-01",
    initial_state={
        "status": "active",
        "context": {"user": "alice"}
    }
)
print(f"Session ID: {session.id}")

# 2. Add Persistent Memory (Vector-embedded automatically)
client.create_memory(
    session_id=session.id,
    content="User prefers email notifications",
    type="preference"
)

# 3. Log a Turn (Trace input/output)
client.create_turn(
    session_id=session.id,
    input="What are my preferences?",
    output="You prefer email notifications.",
    metadata={"model": "gpt-4"}
)

# 4. Update State safely
client.update_state(
    session_id=session.id,
    updates={"last_action": "notification_check"},
    reasoning="User asked for preferences"
)
```

## ⚡ Async Support

Build high-performance agents with fully async methods:

```python
import asyncio
from statebase import AsyncStateBase

async def main():
    async with AsyncStateBase(api_key="sb_live_...") as client:
        # Search memories semantically
        memories = await client.search_memories(
            query="notification preference",
            session_id="session_123"
        )
        print(memories)

if __name__ == "__main__":
    asyncio.run(main())
```

## 🛠 Features

*   **Persistent Memory**: Long-term vector storage for agent knowledge.
*   **State Management**: Track and rollback agent state changes deterministically.
*   **Observability**: Trace every turn, input, and output.
*   **Type Safety**: Full Pydantic models for request/response validation.
*   **Async/Sync**: First-class support for both synchronous and asynchronous patterns.

## 📚 Documentation

For full API documentation, visit [docs.statebase.org](https://docs.statebase.org).

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
